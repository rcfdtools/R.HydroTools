"""
ideam_bulk_download.py  (basado en el skill 'ideam-data-download')
---------------------------------------------------------------
Descarga series de tiempo del IDEAM (portal Atención al Ciudadano / DHIME) para UN CONJUNTO
de estaciones listadas en un archivo de texto, para las variables CAUDAL y/o PRECIPITACIÓN.

El script:
  1. Lee el listado de estaciones desde un archivo de texto (una por línea).
  2. Para cada estación consulta el Catálogo Nacional de Estaciones (datos.gov.co / Socrata)
     y el catálogo interno del IDEAM (MapServer/8) para obtener detalles y fechas de registro.
  3. Descarga las series vía la API REST del DHIME (token + ConsultarListaSeriesTiempoEstacionesPorFiltroString).
  4. Guarda un CSV por estación/variable y un CSV maestro de resumen.

El catálogo de estaciones (datos.gov.co) es de solo lectura/consulta; la descarga de series
usa el mismo flujo que la web oficial de Atención al Ciudadano (token de servicio embebido).

Uso:
  python ideam_bulk_download.py --lista estaciones.txt --variable CAUDAL --inicio 2000-01-01 --fin 2021-12-31
  python ideam_bulk_download.py --lista estaciones.txt --variable PRECIPITACION --inicio 2000-01-01
  python ideam_bulk_download.py --lista estaciones.txt --variable CAUDAL PRECIPITACION --todo

Formato del archivo de lista (estaciones.txt), una por línea:
  23067050
  23067020
  # las líneas que empiezan con # son comentarios
  11000010   # puedes poner código y (opcional) un nombre/comentario separado por espacios/tab

También acepta "codigo  etiqueta" para forzar una etiqueta concreta, p.ej.:
  23067050  Q_MEDIA_D
"""

import argparse
import base64
import io
import json
import os
import sys
import zipfile
import time
import requests
from urllib.parse import urlencode

# ----------------------------------------------------------------------------
# Endpoints (verificados 2026-07, ver skill ideam-data-download)
# ----------------------------------------------------------------------------
DHIME_BASE = "https://modulopersonalizado.ideam.gov.co/DhimeServicePortal"
TOKEN_URL = f"{DHIME_BASE}/token"
# Ruta verificada que funciona: /api/Listas/...  (el skill documenta /api/Lists/... que da 404;
# probamos ambas en orden, sin lanzar excepción hasta agotarlas).
DOWNLOAD_PATHS = [
    "/api/Listas/ConsultarListaSeriesTiempoEstacionesPorFiltroString",
    "/api/Lists/ConsultarListaSeriesTiempoEstacionesPorFiltroString",
]
USER, PASS = "apiuser_sgdhm", "mvm2017*"

MAPSRV = "https://dhime.ideam.gov.co/server/rest/services/CNE/Estaciones/MapServer"
CATALOG_URL = "https://www.datos.gov.co/resource/cqmv-a99d.json"
#CATALOG_URL = "https://www.datos.gov.co/resource/hp9r-jxuu.json"

# Etiquetas conocidas por variable. Las etiquetas se descubren DINÁMICAMENTE desde el
# catálogo interno del IDEAM (MapServer/8); estos diccionarios solo sirven de respaldo/etiquetas
# por defecto y para mostrar descripciones amigables.
VARIABLES = {
    "CAUDAL": {
        "idparametro": "CAUDAL",
        "etiquetas": {
            "Q_MEDIA_D": "Caudal medio diario",
            "Q_MEDIA_M": "Caudal medio mensual",
            "Q_MEDIA_A": "Caudal medio anual",
            "Q_MX_D": "Caudal máximo diario",
            "Q_MN_D": "Caudal mínimo diario",
            "CAUDAL_H": "Caudal horario",
        },
        "default": "Q_MEDIA_D",
        "unidad": "m^3/s",
    },
    "PRECIPITACION": {
        "idparametro": "PRECIPITACION",
        "etiquetas": {
            "PTPG_TT_D": "Precipitación total diaria",
            "PTPG_TT_M": "Precipitación total mensual",
            "PTPG_TT_A": "Precipitación total anual",
            "PTPG_MX_D": "Precipitación máxima diaria",
            "PTPG_MX_M": "Precipitación máxima mensual",
            "PTPG_MX_A": "Precipitación máxima anual en 1 hora",
            "PTPG_MX_TT_A": "Precipitación máxima anual en un día",
            "PTPM_TT_D": "Precipitación total diaria (convencional)",
            "PTPM_TT_M": "Precipitación total mensual (convencional)",
            "PTPM_TT_A": "Precipitación total anual (convencional)",
            "PP_H": "Precipitación horaria",
            "PTPM_CON": "Día pluviométrico (convencional)",
            "PTPM_CON": "PTPM_MX_TT_A",
            "PTPM_MX_TT_M": "PTPM_MX_TT_M",
            "HIS_PTPM_TT_M": "HIS_PTPM_TT_M",
            "PTPM_CON_INTER": "PTPM_CON_INTER",
            "PTPM_TT_M_INTER": "PTPM_TT_M_INTER",
            "PTPM_TT_M_CAL": "PTPM_TT_M_CAL",
            "PT_AUT_10": "PT_AUT_10",
        },
        # Orden de PREFERENCIA cuando no se usa --todas-etiquetas: se descarga la primera
        # disponible en esta lista (prioriza la diaria total).
        "preferencia": ["PTPG_TT_D", "PTPM_TT_D", "PTPG_TT_M", "PTPM_TT_M",
                        "PTPG_MX_D", "PTPG_TT_A", "PTPM_TT_A", "PP_H"],
        "default": None,  # se descubre dinámicamente desde el catálogo
        "unidad": "mm",
    },
}


# ----------------------------------------------------------------------------
# Funciones de red
# ----------------------------------------------------------------------------
def obtener_token():
    r = requests.post(TOKEN_URL, data={"username": USER, "password": PASS, "grant_type": "password"},
                      headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}, timeout=40)
    r.raise_for_status()
    return r.json()["access_token"]


def consultar_catalogo_datos_abiertos(codigo):
    """Devuelve el dict del Catálogo Nacional de Estaciones (datos.gov.co) para un código.
    Es un enriquecimiento opcional: el catálogo no contiene todas las estaciones del IDEAM,
    así que un resultado vacío no es un error."""
    try:
        r = requests.get(CATALOG_URL, params={"codigo": codigo}, timeout=40)
        r.raise_for_status()
        data = r.json()
        if isinstance(data, list) and data:
            return data[0]
    except Exception as e:
        print(f"    [catalogo datos.gov.co] no disponible para {codigo}: {e}")
    return {}


def consultar_series_metadata_ideam(codigo):
    """Devuelve lista de {idparametro, etiqueta, descripcion} desde MapServer/8 del IDEAM."""
    try:
        url = f"{MAPSRV}/8/query"
        params = {"where": f"idestacion = '{codigo}'", "outFields": "*",
                  "f": "json", "returnGeometry": "false", "resultRecordCount": 100}
        r = requests.get(url, params=params, timeout=40)
        r.raise_for_status()
        feats = r.json().get("features", [])
        out = []
        for f in feats:
            a = f["attributes"]
            if a.get("idparametro"):
                out.append({
                    "idparametro": a["idparametro"],
                    "etiqueta": a.get("etiqueta"),
                    "descripcion": a.get("descripcion"),
                })
        return out
    except Exception as e:
        print(f"    [metadata IDEAM] no disponible para {codigo}: {e}")
        return []


def descargar_serie(tok, codigo, variable, etiqueta, inicio, fin, salida):
    """Intenta descargar una serie. Devuelve (ok, n_filas, mensaje).
    - ok=True  -> se guardó el CSV.
    - ok=False con mensaje 'SIN_DATOS' -> la etiqueta es válida pero no hay registros en el rango.
    - ok=False otro mensaje -> error (ruta caída, etiqueta no servible, etc.)."""
    filtro = {
        "fechaInicio": inicio, "fechaFin": fin,
        "mostrarGrado": "true", "mostrarCalificador": "true", "mostrarNivelAprobacion": "true",
        "tipoReporte": "csv", "sort": "", "group": "",
        "filter": f"(IdParametro~eq~'{variable}'~and~Etiqueta~eq~'{etiqueta}'~and~IdEstacion~eq~'{codigo}')",
    }
    fs = urlencode(filtro)
    items = [{
        "IdParametro": variable, "Etiqueta": etiqueta,
        "EsEjeY1": False, "EsEjeY2": False, "EsTipoLinea": False, "EsTipoBarra": False,
        "TipoSerie": "Estandar", "Calculo": "",
    }]
    last_err = None
    for path in DOWNLOAD_PATHS:
        url = f"{DHIME_BASE}{path}?{fs}"
        try:
            r = requests.post(url, data=json.dumps(items),
                              headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/json"},
                              timeout=300)
            if r.status_code != 200:
                last_err = f"HTTP {r.status_code}"
                continue  # prueba la otra ruta
            try:
                j = r.json()
            except Exception:
                last_err = "respuesta no JSON"
                continue
            if not j.get("zip"):
                # "sin datos en rango" es un resultado válido, NO reintentar otra ruta
                return False, 0, j.get("mensaje") or "SIN_DATOS"
            raw = base64.b64decode(j["zip"])
            z = zipfile.ZipFile(io.BytesIO(raw))
            name = z.namelist()[0]
            csv_bytes = z.read(name)
            with open(salida, "wb") as f:
                f.write(csv_bytes)
            n = csv_bytes.decode("utf-8", "replace").count("\n")
            return True, n, None
        except Exception as e:
            last_err = str(e)
    return False, 0, last_err or "error_desconocido"


def fechas_registro_csv(path):
    """Lee el CSV descargado y devuelve (inicio, fin, n_registros) de la columna Fecha."""
    try:
        import csv
        fechas = []
        with open(path, encoding="utf-8", errors="replace") as f:
            for row in csv.DictReader(f):
                fechas.append(row.get("Fecha", "").strip())
        fechas = [x for x in fechas if x]
        if not fechas:
            return None, None, 0
        return fechas[0][:10], fechas[-1][:10], len(fechas)
    except Exception:
        return None, None, 0


# ----------------------------------------------------------------------------
# Lógica principal
# ----------------------------------------------------------------------------
def leer_lista(path):
    estaciones = []
    with open(path, encoding="utf-8", errors="replace") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            partes = linea.split()
            codigo = partes[0]
            etiqueta_forzada = partes[1] if len(partes) > 1 and not partes[1].startswith("#") else None
            estaciones.append((codigo, etiqueta_forzada))
    return estaciones


def main():
    ap = argparse.ArgumentParser(description="Descarga masiva IDEAM DHIME (caudal/precipitación) por listado")
    ap.add_argument("--lista", required=True, help="Archivo de texto con los códigos de estación (uno por línea)")
    ap.add_argument("--variable", nargs="+", required=True,
                    choices=list(VARIABLES.keys()),
                    help="Variable(s) a descargar: CAUDAL y/o PRECIPITACION")
    ap.add_argument("--inicio", default="2000-01-01")
    ap.add_argument("--fin", default="2021-12-31")
    ap.add_argument("--salida-dir", default="descargas_ideam", help="Carpeta de salida")
    ap.add_argument("--todas-etiquetas", action="store_true",
                    help="Descargar TODAS las etiquetas disponibles de la variable (no solo la diaria)")
    args = ap.parse_args()

    os.makedirs(args.salida_dir, exist_ok=True)
    estaciones = leer_lista(args.lista)
    if not estaciones:
        print("ERROR: el listado está vacío.", file=sys.stderr)
        sys.exit(1)
    print(f"Listado: {len(estaciones)} estación(es) | variables: {args.variable} | rango {args.inicio}..{args.fin}")

    tok = obtener_token()
    print("Token IDEAM obtenido OK")

    resumen = []  # filas del CSV maestro

    for codigo, etiqueta_forzada in estaciones:
        print(f"\n=== Estación {codigo} ===")

        # 1) Catálogo datos.gov.co
        cat = consultar_catalogo_datos_abiertos(codigo)
        if cat:
            print(f"    Catálogo D.A.: {cat.get('nombre','?')} | {cat.get('categoria','?')} | "
                  f"estado={cat.get('estado','?')} | {cat.get('departamento','?')}/{cat.get('municipio','?')} | "
                  f"inst={cat.get('fecha_instalacion','?')} | susp={cat.get('fecha_suspension','-')}")
        else:
            print("    Catálogo D.A.: sin coincidencia (o no disponible)")

        # 2) Metadata de series del IDEAM
        meta = consultar_series_metadata_ideam(codigo)

        for var in args.variable:
            cfg = VARIABLES[var]
            idp = cfg["idparametro"]
            # Etiquetas REALES disponibles para esta variable en esta estación (catálogo IDEAM)
            ets_disponibles = sorted({m["etiqueta"] for m in meta if m["idparametro"] == idp and m["etiqueta"]})

            if etiqueta_forzada:
                etiquetas_a_usar = [etiqueta_forzada]
            elif args.todas_etiquetas:
                etiquetas_a_usar = ets_disponibles  # descarga todo lo que exista
            else:
                # Elige la MEJOR etiqueta según el orden de preferencia de la variable.
                orden = cfg.get("preferencia") or ([cfg["default"]] if cfg["default"] else [])
                elegida = next((e for e in orden if e in ets_disponibles), None)
                etiquetas_a_usar = [elegida] if elegida else []

            if not etiquetas_a_usar:
                print(f"    [{var}] sin etiquetas disponibles en el catálogo IDEAM para esta estación.")
                resumen.append([codigo, cat.get("nombre", ""), var, "", "", cat.get("estado", ""),
                                "", "SIN_ETIQUETA", ""])
                continue

            for etq in etiquetas_a_usar:
                if not etq:
                    continue
                desc = cfg["etiquetas"].get(etq, etq)
                fname = f"{codigo}_{var}_{etq}.csv"
                fpath = os.path.join(args.salida_dir, fname)
                print(f"    [{var}/{etq}] {desc} -> {fname} ...", end=" ", flush=True)
                ok, n, err = descargar_serie(tok, codigo, idp, etq, args.inicio, args.fin, fpath)
                if ok:
                    fi, ff, nr = fechas_registro_csv(fpath)
                    print(f"OK ({nr} filas, {fi}..{ff})")
                    resumen.append([codigo, cat.get("nombre", ""), var, etq, desc,
                                    cat.get("estado", ""), f"{fi}..{ff}", "OK", nr])
                elif err == "SIN_DATOS" or "no hay información" in str(err):
                    # La etiqueta es válida pero no hay registros en el rango pedido.
                    print(f"SIN DATOS en rango {args.inicio}..{args.fin}")
                    resumen.append([codigo, cat.get("nombre", ""), var, etq, desc,
                                    cat.get("estado", ""), "", "SIN_DATOS_EN_RANGO", 0])
                else:
                    print(f"FALLO: {err}")
                    resumen.append([codigo, cat.get("nombre", ""), var, etq, desc,
                                    cat.get("estado", ""), "", f"FALLO: {err}", 0])
                time.sleep(0.5)  # cortesía hacia el servicio

    # CSV maestro
    import csv
    master = os.path.join(args.salida_dir, "resumen_descarga.csv")
    with open(master, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["CodigoEstacion", "Nombre", "Variable", "Etiqueta", "Descripcion",
                    "EstadoCatalogo", "RangoFechas", "Estado", "NRegistros"])
        w.writerows(resumen)
    print(f"\nResumen guardado en: {master}  ({len(resumen)} filas)")


if __name__ == "__main__":
    main()

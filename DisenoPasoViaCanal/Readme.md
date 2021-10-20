## Diseño geométrico de pasos de vía en canales usando alcantarillas por área equivalente a descarga libre.

Dimensionar la geometría de sección requerida para transpotar el caudal de diseño de creciente bajo pasos de vía usando área equivalente. Es recomendable ubicar los pasos de vía en zonas de corte, en la que se disponga de una profundidad a la base del canal dominante mayor a la profundidad hidráulica de diseño; de este modo se podrán utilizar tuberías de diámetros superiores garantizando el tránsito hidráulico a descarga libre. 

### Procedimiento general
1. Realizar el diseño geométrico del paso de vía utilizando este libro.
2. Copiar todos los datos de la hoja GISCulvertPoint al libro de Excel R.HydroTools.DisenoPasoViaCanalGIS.xls.
3. Desde ArcMAP o ArcCatalog, ejecutar el Model Builder Toolbox R.HydroTools.DisenoPasoViaCanal.tbx. Se recomienda utilizar la ruta absoluta D:\R.HydroTools\DisenoPasoViaCanal\.
4. Visualizar las capas geográficas 3D de alcantarillas en ArcMAP y Autodek CIVIL3D.
5. Crear sólidos de las tuberías 3D en CIVIL3D o en Autocad usando Sweep y SolidEdit.
6. Realizar el diseño de la expansión y la contracción utilizando el libro de diseño R.HydroTools.DisenoEstructuraContraccionExpansionSubcritico.xlsm (HCMC0013).

### Funcionalidades
* Resuelve el número de alcantarillas principales y secundarias requeridas a partir de los parámetros de entrada.
* Grafica las secciones del canal y paso de vía con localización de alcantarillas obtenidas.
* Crea la tabla de datos geográficos para la creación de nodos y lineas 3D de eje, clave y batea.
* Resuleve la pendiente de las alcantarilla para modelos 1D en función de las secciones de referencia utilizadas para la localización.
* Mediante la caja de herramientas ESRI ArcGIS for Desktop R.HydroTools.DisenoPasoViaCanal.tbx, crea los nodos y líneas 3D y exporta las lineas cota, eje y batea a Autocad.


## Ilustraciones

![R.HydroTools.DisenoPasoViaCanal.Screenshot1](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoPasoViaCanal/Screenshot/Screenshot1.png)
![R.HydroTools.DisenoPasoViaCanal.Screenshot2](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoPasoViaCanal/Screenshot/Screenshot2.png)
![R.HydroTools.DisenoPasoViaCanal.Screenshot3](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoPasoViaCanal/Screenshot/Screenshot3.png)
![R.HydroTools.DisenoPasoViaCanal.Screenshot4](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoPasoViaCanal/Screenshot/Screenshot4.png)
![R.HydroTools.DisenoPasoViaCanal.Screenshot5](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoPasoViaCanal/Screenshot/Screenshot5.png)
![R.HydroTools.DisenoPasoViaCanal.Screenshot6](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoPasoViaCanal/Screenshot/Screenshot6.png)
![R.HydroTools.DisenoPasoViaCanal.Screenshot7](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoPasoViaCanal/Screenshot/Screenshot7.png)
![R.HydroTools.DisenoPasoViaCanal.Screenshot8](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoPasoViaCanal/Screenshot/Screenshot8.png)
![R.HydroTools.DisenoPasoViaCanal.Screenshot9](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoPasoViaCanal/Screenshot/Screenshot9.png)
![R.HydroTools.DisenoPasoViaCanal.Screenshot10](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoPasoViaCanal/Screenshot/Screenshot10.png)
![R.HydroTools.DisenoPasoViaCanal.Screenshot11](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoPasoViaCanal/Screenshot/Screenshot11.png)
![R.HydroTools.DisenoPasoViaCanal.Screenshot12](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoPasoViaCanal/Screenshot/Screenshot12.png)
![R.HydroTools.DisenoPasoViaCanal.Screenshot13](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoPasoViaCanal/Screenshot/Screenshot13.png)
![R.HydroTools.DisenoPasoViaCanal.Screenshot14](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoPasoViaCanal/Screenshot/Screenshot14.png)


## Keywords
Culvert design. ModelBuilder. Invert elevation.


## Control de versiones

Versión | Descripción
--- | ---
| v.20190523 | Tuberías paralelas funcionales para cuadrante direccional NE.
| v.20200921 | Inclusión de evaluación de tuberías paralelas mediante cuadrantes direccionales NE, NW, SE, SW en VBA. Permite obtener ejes en cualquier dirección.
| v.20200925 | En GISSetup se incluyeron atributos requeridos para la construcción de la tabla Culverts de HEC-RAS 1D. Estandarización de nombres de campos de atributos para compatibilidad con HEC-RAS. SeccionCompuesta y GraficoSeccion ahora representan hasta 500 alcantarillas secundarias. Modificado el ArcToolBox de ArcGIS incluyendo nuevos atributos en alcantarillas. En GISSetup se ha incluído una opción para resolver la pendiente de las alcantarillas para modelación en HEC-RAS 1D. Ajuste representación lámina de agua en pasos de vía.
| v.20211020 | Actualización general de formato y gráficas.


## Licencia, cláusulas y condiciones de uso
https://github.com/rcfdtools/R.HydroTools/wiki/License


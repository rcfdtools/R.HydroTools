'Diseno geometrico de pasos de via en canales usando alcantarillas por area equivalente a descarga libre.
'Versión: 20211020
'https://github.com/rcfdtools/R.HydroTools/tree/main/DisenoPasoViaCanal
'Información, licencia y condiciones de uso en https://github.com/rcfdtools/R.HydroTools/wiki/License
'VisualBasic for applications.
Sub R_GISCulvertPoint()
    vAppName = "R.GISCulvertPoint"
    vCreateBy = "https://github.com/rcfdtools"
    vTInicioCalc = Timer()
    vHojaDatos = "GISSetup"
    vHojaGIS = "GISCulvertPoint"
    Sheets(vHojaDatos).Select
    vCXInicio = Range("C4")                     'Coordenada X del punto inicial eje GIS
    vCYInicio = Range("D4")                     'Coordenada Y del punto inical eje GIS
    vCZInicio = Range("E4")                     'Coordenada Z del punto inical eje GIS
    vCXFin = Range("C5")                        'Coordenada X del punto final eje GIS
    vCYFin = Range("D5")                        'Coordenada Y del punto final eje GIS
    vCZFin = Range("E5")                        'Coordenada Z del punto final eje GIS
    vNap = Range("C10")                         '# alcantarillas principales
    vOp = Range("C11")                          'Offset eje alcantarilla principal, m
    vDxp = Range("C12")                         'Desplazamiento en x alcantarilla principal, m
    vDyp = Range("C13")                         'Desplazamiento en y alcantarilla principal, m
    vBp = Range("C14")                          'Ancho base paso vía paso vía sección dominante, m
    vDap = Range("C15")                         'Dap, diametro alcantarilla principal, m
    vSap = Range("C16")                         'Separación alcantarilla principal, m
    vNas = Range("E10")                         '# alcantarillas secundarias
    vOs = Range("E11")                          'Offset eje alcantarilla principal, m
    vDxs = Range("E12")                         'Desplazamiento en x alcantarilla principal, m
    vDys = Range("E13")                         'Desplazamiento en y alcantarilla principal, m
    vBs = Range("E14")                          'Ancho base paso vía paso vía sección creciente, m
    vDas = Range("E15")                         'Diametro alcantarilla secundaria, m
    vAlpha = Range("C8")                        'Rotación eje linea GIS, radianes
    vLa = Range("C6")                           'La, longitud alcantarilla, m
    vHd = Range("E17")                          'Hd, altura sección dominante, m
    vRiver = Range("C19")                       'River Name, nombre del río
    vReach = Range("C20")                       'River Reach, nombre del tramo del río
    vRS = Range("C21")                          'River Station, nombre de la estación de localización del paso de vía o abscisa
    vDistUpStrXS = Range("C22")                 'Distance to UpStream XS, m. Distancia al paso de vía desde la sección aguas arriba
    vBin = 0                                    'Marcación nodo 0-inicial, 1-final
    i = 1                                       'Incremento global
    
    'Limpiar hoja de volcado de datos
    Sheets(vHojaGIS).Select
    Sheets(vHojaGIS).Range("A2:Z5000").ClearContents
    
    'Tuberías principales sobre base sección dominante
    'Cuadrande direccional NE
    If vCXFin >= vCXInicio And vCYFin >= vCYInicio Then
        vCXBancaIzqInicio = vCXInicio - ((vOp * vNap) / 2 + (vDxp / 2)) * Sin(vAlpha)   'Coordenada inicial en x de la tubería mas lejana a la izquierda
        vCYBancaIzqInicio = vCYInicio + ((vOp * vNap) / 2 + (vDxp / 2)) * Cos(vAlpha)   'Coordenada inicial en y de la tubería mas lejana a la izquierda
        vCXBancaIzqFin = vCXFin - ((vOp * vNap) / 2 + (vDxp / 2)) * Sin(vAlpha)         'Coordenada final en x de la tubería mas lejana a la izquierda
        vCYBancaIzqFin = vCYFin + ((vOp * vNap) / 2 + (vDxp / 2)) * Cos(vAlpha)         'Coordenada final  en y de la tubería mas lejana a la izquierda
    End If
    'Cuadrande direccional NW
    If vCXFin <= vCXInicio And vCYFin >= vCYInicio Then
        vCXBancaIzqInicio = vCXInicio - ((vOp * vNap) / 2 + (vDxp / 2)) * Sin(vAlpha)   'Coordenada inicial en x de la tubería mas lejana a la izquierda
        vCYBancaIzqInicio = vCYInicio - ((vOp * vNap) / 2 + (vDxp / 2)) * Cos(vAlpha)   'Coordenada inicial en y de la tubería mas lejana a la izquierda
        vCXBancaIzqFin = vCXFin - ((vOp * vNap) / 2 + (vDxp / 2)) * Sin(vAlpha)         'Coordenada final en x de la tubería mas lejana a la izquierda
        vCYBancaIzqFin = vCYFin - ((vOp * vNap) / 2 + (vDxp / 2)) * Cos(vAlpha)         'Coordenada final  en y de la tubería mas lejana a la izquierda
    End If
    'Cuadrande direccional SE
    If vCXFin >= vCXInicio And vCYFin <= vCYInicio Then
        vCXBancaIzqInicio = vCXInicio + ((vOp * vNap) / 2 + (vDxp / 2)) * Sin(vAlpha)  'Coordenada inicial en x de la tubería mas lejana a la izquierda
        vCYBancaIzqInicio = vCYInicio + ((vOp * vNap) / 2 + (vDxp / 2)) * Cos(vAlpha)   'Coordenada inicial en y de la tubería mas lejana a la izquierda
        vCXBancaIzqFin = vCXFin + ((vOp * vNap) / 2 + (vDxp / 2)) * Sin(vAlpha)          'Coordenada final en x de la tubería mas lejana a la izquierda
        vCYBancaIzqFin = vCYFin + ((vOp * vNap) / 2 + (vDxp / 2)) * Cos(vAlpha)         'Coordenada final  en y de la tubería mas lejana a la izquierda
    End If
    'Cuadrande direccional SW
    If vCXFin <= vCXInicio And vCYFin <= vCYInicio Then
        vCXBancaIzqInicio = vCXInicio + ((vOp * vNap) / 2 + (vDxp / 2)) * Sin(vAlpha)   'Coordenada inicial en x de la tubería mas lejana a la izquierda
        vCYBancaIzqInicio = vCYInicio - ((vOp * vNap) / 2 + (vDxp / 2)) * Cos(vAlpha)   'Coordenada inicial en y de la tubería mas lejana a la izquierda
        vCXBancaIzqFin = vCXFin + ((vOp * vNap) / 2 + (vDxp / 2)) * Sin(vAlpha)         'Coordenada final en x de la tubería mas lejana a la izquierda
        vCYBancaIzqFin = vCYFin - ((vOp * vNap) / 2 + (vDxp / 2)) * Cos(vAlpha)         'Coordenada final  en y de la tubería mas lejana a la izquierda
    End If
    iAux = 1
    While i < vNap * 2 + 1
        Cells(i + 1, 1) = i
        Cells(i + 1, 2) = "AlcCentral" 'usar 12 caracteres para compatibilidad con HEC-RAS
        Cells(i + 1, 4) = vBin
        If vBin = 0 Then
            Cells(i + 1, 3) = iAux
            'Cuadrande direccional NE
            If vCXFin >= vCXInicio And vCYFin >= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaIzqInicio + vDxp * iAux
                Cells(i + 1, 6) = vCYBancaIzqInicio - vDyp * iAux
            End If
            'Cuadrande direccional NW
            If vCXFin <= vCXInicio And vCYFin >= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaIzqInicio + vDxp * iAux
                Cells(i + 1, 6) = vCYBancaIzqInicio + vDyp * iAux
            End If
            'Cuadrande direccional SE
            If vCXFin >= vCXInicio And vCYFin <= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaIzqInicio - vDxp * iAux
                Cells(i + 1, 6) = vCYBancaIzqInicio - vDyp * iAux
            End If
            'Cuadrande direccional SW
            If vCXFin <= vCXInicio And vCYFin <= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaIzqInicio - vDxp * iAux
                Cells(i + 1, 6) = vCYBancaIzqInicio + vDyp * iAux
            End If
            Cells(i + 1, 7) = vCZInicio
            Cells(i + 1, 8) = vCZInicio + vDap
            Cells(i + 1, 9) = vCZInicio + vDap / 2
            Cells(i + 1, 10) = vLa
            Cells(i + 1, 11) = vDap
            Cells(i + 1, 12) = vRiver
            Cells(i + 1, 13) = vReach
            Cells(i + 1, 14) = vRS
            Cells(i + 1, 16) = "A" & iAux
            vBin = 1
        Else
            Cells(i + 1, 3) = iAux - 1
            'Cuadrande direccional NE
            If vCXFin >= vCXInicio And vCYFin >= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaIzqFin + vDxp * (iAux - 1)
                Cells(i + 1, 6) = vCYBancaIzqFin - vDyp * (iAux - 1)
            End If
            'Cuadrande direccional NW
            If vCXFin <= vCXInicio And vCYFin >= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaIzqFin + vDxp * (iAux - 1)
                Cells(i + 1, 6) = vCYBancaIzqFin + vDyp * (iAux - 1)
            End If
            'Cuadrande direccional SE
            If vCXFin >= vCXInicio And vCYFin <= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaIzqFin - vDxp * (iAux - 1)
                Cells(i + 1, 6) = vCYBancaIzqFin - vDyp * (iAux - 1)
            End If
            'Cuadrande direccional SW
            If vCXFin <= vCXInicio And vCYFin <= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaIzqFin - vDxp * (iAux - 1)
                Cells(i + 1, 6) = vCYBancaIzqFin + vDyp * (iAux - 1)
            End If
            Cells(i + 1, 7) = vCZFin
            Cells(i + 1, 8) = vCZFin + vDap
            Cells(i + 1, 9) = vCZFin + vDap / 2
            Cells(i + 1, 10) = vLa
            Cells(i + 1, 11) = vDap
            Cells(i + 1, 12) = vRiver
            Cells(i + 1, 13) = vReach
            Cells(i + 1, 14) = vRS
            Cells(i + 1, 16) = "A" & iAux
            vBin = 0
        End If
        i = i + 1
        If i Mod 2 = 0 Then iAux = iAux + 1
    Wend
    
    'Tuberías secundarias lado izquierdo sobre base sección creciente
    'Cuadrande direccional NE
    If vCXFin >= vCXInicio And vCYFin >= vCYInicio Then
        vCXBancaIzqInicio = vCXInicio - ((vBs / 2) + (vOs / 2)) * Sin(vAlpha)    'Coordenada inicial en x de la tubería mas lejana a la izquierda
        vCYBancaIzqInicio = vCYInicio + ((vBs / 2) + (vOs / 2)) * Cos(vAlpha)    'Coordenada inicial en y de la tubería mas lejana a la izquierda
        vCXBancaIzqFin = vCXFin - ((vBs / 2) + (vOs / 2)) * Sin(vAlpha)          'Coordenada final en x de la tubería mas lejana a la izquierda
        vCYBancaIzqFin = vCYFin + ((vBs / 2) + (vOs / 2)) * Cos(vAlpha)          'Coordenada final  en y de la tubería mas lejana a la izquierda
    End If
    'Cuadrande direccional NW
    If vCXFin <= vCXInicio And vCYFin >= vCYInicio Then
        vCXBancaIzqInicio = vCXInicio - ((vBs / 2) + (vOs / 2)) * Sin(vAlpha)    'Coordenada inicial en x de la tubería mas lejana a la izquierda
        vCYBancaIzqInicio = vCYInicio - ((vBs / 2) + (vOs / 2)) * Cos(vAlpha)    'Coordenada inicial en y de la tubería mas lejana a la izquierda
        vCXBancaIzqFin = vCXFin - ((vBs / 2) + (vOs / 2)) * Sin(vAlpha)          'Coordenada final en x de la tubería mas lejana a la izquierda
        vCYBancaIzqFin = vCYFin - ((vBs / 2) + (vOs / 2)) * Cos(vAlpha)          'Coordenada final  en y de la tubería mas lejana a la izquierda
    End If
    'Cuadrande direccional SE
    If vCXFin >= vCXInicio And vCYFin <= vCYInicio Then
        vCXBancaIzqInicio = vCXInicio + ((vBs / 2) + (vOs / 2)) * Sin(vAlpha)    'Coordenada inicial en x de la tubería mas lejana a la izquierda
        vCYBancaIzqInicio = vCYInicio + ((vBs / 2) + (vOs / 2)) * Cos(vAlpha)    'Coordenada inicial en y de la tubería mas lejana a la izquierda
        vCXBancaIzqFin = vCXFin + ((vBs / 2) + (vOs / 2)) * Sin(vAlpha)          'Coordenada final en x de la tubería mas lejana a la izquierda
        vCYBancaIzqFin = vCYFin + ((vBs / 2) + (vOs / 2)) * Cos(vAlpha)          'Coordenada final  en y de la tubería mas lejana a la izquierda
    End If
    'Cuadrande direccional SW
    If vCXFin <= vCXInicio And vCYFin <= vCYInicio Then
        vCXBancaIzqInicio = vCXInicio + ((vBs / 2) + (vOs / 2)) * Sin(vAlpha)    'Coordenada inicial en x de la tubería mas lejana a la izquierda
        vCYBancaIzqInicio = vCYInicio - ((vBs / 2) + (vOs / 2)) * Cos(vAlpha)    'Coordenada inicial en y de la tubería mas lejana a la izquierda
        vCXBancaIzqFin = vCXFin + ((vBs / 2) + (vOs / 2)) * Sin(vAlpha)          'Coordenada final en x de la tubería mas lejana a la izquierda
        vCYBancaIzqFin = vCYFin - ((vBs / 2) + (vOs / 2)) * Cos(vAlpha)          'Coordenada final  en y de la tubería mas lejana a la izquierda
    End If
    iAux = vNap + 1
    iAux1 = 1
    While i < vNap * 2 + vNas + 1
        Cells(i + 1, 1) = i
        Cells(i + 1, 2) = "AlcSecundIzq" 'usar 12 caracteres para compatibilidad con HEC-RAS
        Cells(i + 1, 4) = vBin
        If vBin = 0 Then
            Cells(i + 1, 3) = iAux
            'Cuadrande direccional NE
            If vCXFin >= vCXInicio And vCYFin >= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaIzqInicio + vDxs * iAux1
                Cells(i + 1, 6) = vCYBancaIzqInicio - vDys * iAux1
            End If
            'Cuadrande direccional NW
            If vCXFin <= vCXInicio And vCYFin >= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaIzqInicio + vDxs * iAux1
                Cells(i + 1, 6) = vCYBancaIzqInicio + vDys * iAux1
            End If
            'Cuadrande direccional SE
            If vCXFin >= vCXInicio And vCYFin <= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaIzqInicio - vDxs * iAux1
                Cells(i + 1, 6) = vCYBancaIzqInicio - vDys * iAux1
            End If
            'Cuadrande direccional SW
            If vCXFin <= vCXInicio And vCYFin <= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaIzqInicio - vDxs * iAux1
                Cells(i + 1, 6) = vCYBancaIzqInicio + vDys * iAux1
            End If
            Cells(i + 1, 7) = vCZInicio + vHd
            Cells(i + 1, 8) = vCZInicio + vHd + vDas
            Cells(i + 1, 9) = vCZInicio + vHd + vDas / 2
            Cells(i + 1, 10) = vLa
            Cells(i + 1, 11) = vDas
            Cells(i + 1, 12) = vRiver
            Cells(i + 1, 13) = vReach
            Cells(i + 1, 14) = vRS
            Cells(i + 1, 16) = "A" & iAux
            vBin = 1
        Else
            Cells(i + 1, 3) = iAux - 1
            'Cuadrande direccional NE
            If vCXFin >= vCXInicio And vCYFin >= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaIzqFin + vDxs * (iAux1 - 1)
                Cells(i + 1, 6) = vCYBancaIzqFin - vDys * (iAux1 - 1)
            End If
            'Cuadrande direccional NW
            If vCXFin <= vCXInicio And vCYFin >= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaIzqFin + vDxs * (iAux1 - 1)
                Cells(i + 1, 6) = vCYBancaIzqFin + vDys * (iAux1 - 1)
            End If
            'Cuadrande direccional SE
            If vCXFin >= vCXInicio And vCYFin <= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaIzqFin - vDxs * (iAux1 - 1)
                Cells(i + 1, 6) = vCYBancaIzqFin - vDys * (iAux1 - 1)
            End If
            'Cuadrande direccional SW
            If vCXFin <= vCXInicio And vCYFin <= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaIzqFin - vDxs * (iAux1 - 1)
                Cells(i + 1, 6) = vCYBancaIzqFin + vDys * (iAux1 - 1)
            End If
            Cells(i + 1, 7) = vCZFin + vHd
            Cells(i + 1, 8) = vCZFin + vHd + vDas
            Cells(i + 1, 9) = vCZFin + vHd + vDas / 2
            Cells(i + 1, 10) = vLa
            Cells(i + 1, 11) = vDas
            Cells(i + 1, 12) = vRiver
            Cells(i + 1, 13) = vReach
            Cells(i + 1, 14) = vRS
            Cells(i + 1, 16) = "A" & iAux
            vBin = 0
        End If
        i = i + 1
        If i Mod 2 = 0 Then
            iAux = iAux + 1
            iAux1 = iAux1 + 1
        End If
    Wend
    
    'Tuberías secundarias lado derecho sobre base sección creciente
    'Cuadrande direccional NE
    If vCXFin >= vCXInicio And vCYFin >= vCYInicio Then
        vCXBancaDerInicio = vCXInicio + ((vBs / 2) + (vOs / 2)) * Sin(vAlpha)    'Coordenada inicial en x de la tubería mas lejana a la derecha
        vCYBancaDerInicio = vCYInicio - ((vBs / 2) + (vOs / 2)) * Cos(vAlpha)    'Coordenada inicial en y de la tubería mas lejana a la derecha
        vCXBancaDerFin = vCXFin + ((vBs / 2) + (vOs / 2)) * Sin(vAlpha)          'Coordenada final en x de la tubería mas lejana a la derecha
        vCYBancaDerFin = vCYFin - ((vBs / 2) + (vOs / 2)) * Cos(vAlpha)          'Coordenada final  en y de la tubería mas lejana a la derecha
    End If
    'Cuadrande direccional NW
    If vCXFin <= vCXInicio And vCYFin >= vCYInicio Then
        vCXBancaDerInicio = vCXInicio + ((vBs / 2) + (vOs / 2)) * Sin(vAlpha)    'Coordenada inicial en x de la tubería mas lejana a la derecha
        vCYBancaDerInicio = vCYInicio + ((vBs / 2) + (vOs / 2)) * Cos(vAlpha)    'Coordenada inicial en y de la tubería mas lejana a la derecha
        vCXBancaDerFin = vCXFin + ((vBs / 2) + (vOs / 2)) * Sin(vAlpha)          'Coordenada final en x de la tubería mas lejana a la derecha
        vCYBancaDerFin = vCYFin + ((vBs / 2) + (vOs / 2)) * Cos(vAlpha)          'Coordenada final  en y de la tubería mas lejana a la derecha
    End If
    'Cuadrande direccional SE
    If vCXFin >= vCXInicio And vCYFin <= vCYInicio Then
        vCXBancaDerInicio = vCXInicio - ((vBs / 2) + (vOs / 2)) * Sin(vAlpha)    'Coordenada inicial en x de la tubería mas lejana a la derecha
        vCYBancaDerInicio = vCYInicio - ((vBs / 2) + (vOs / 2)) * Cos(vAlpha)    'Coordenada inicial en y de la tubería mas lejana a la derecha
        vCXBancaDerFin = vCXFin - ((vBs / 2) + (vOs / 2)) * Sin(vAlpha)          'Coordenada final en x de la tubería mas lejana a la derecha
        vCYBancaDerFin = vCYFin - ((vBs / 2) + (vOs / 2)) * Cos(vAlpha)          'Coordenada final  en y de la tubería mas lejana a la derecha
    End If
    'Cuadrande direccional SW
    If vCXFin <= vCXInicio And vCYFin <= vCYInicio Then
        vCXBancaDerInicio = vCXInicio - ((vBs / 2) + (vOs / 2)) * Sin(vAlpha)    'Coordenada inicial en x de la tubería mas lejana a la derecha
        vCYBancaDerInicio = vCYInicio + ((vBs / 2) + (vOs / 2)) * Cos(vAlpha)    'Coordenada inicial en y de la tubería mas lejana a la derecha
        vCXBancaDerFin = vCXFin - ((vBs / 2) + (vOs / 2)) * Sin(vAlpha)          'Coordenada final en x de la tubería mas lejana a la derecha
        vCYBancaDerFin = vCYFin + ((vBs / 2) + (vOs / 2)) * Cos(vAlpha)          'Coordenada final  en y de la tubería mas lejana a la derecha
    End If
    iAux = vNap + 1 + (vNas / 2)
    iAux1 = 1
    While i < vNap * 2 + vNas * 2 + 1
        Cells(i + 1, 1) = i
        Cells(i + 1, 2) = "AlcSecundDer" 'usar 12 caracteres para compatibilidad con HEC-RAS
        Cells(i + 1, 4) = vBin
        If vBin = 0 Then
            Cells(i + 1, 3) = iAux
            'Cuadrande direccional NE
            If vCXFin >= vCXInicio And vCYFin >= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaDerInicio - vDxs * iAux1
                Cells(i + 1, 6) = vCYBancaDerInicio + vDys * iAux1
            End If
            'Cuadrande direccional NW
            If vCXFin <= vCXInicio And vCYFin >= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaDerInicio - vDxs * iAux1
                Cells(i + 1, 6) = vCYBancaDerInicio - vDys * iAux1
            End If
            'Cuadrande direccional SE
            If vCXFin >= vCXInicio And vCYFin <= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaDerInicio + vDxs * iAux1
                Cells(i + 1, 6) = vCYBancaDerInicio + vDys * iAux1
            End If
            'Cuadrande direccional SW
            If vCXFin <= vCXInicio And vCYFin <= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaDerInicio + vDxs * iAux1
                Cells(i + 1, 6) = vCYBancaDerInicio - vDys * iAux1
            End If
            Cells(i + 1, 7) = vCZInicio + vHd
            Cells(i + 1, 8) = vCZInicio + vHd + vDas
            Cells(i + 1, 9) = vCZInicio + vHd + vDas / 2
            Cells(i + 1, 10) = vLa
            Cells(i + 1, 11) = vDas
            Cells(i + 1, 12) = vRiver
            Cells(i + 1, 13) = vReach
            Cells(i + 1, 14) = vRS
            Cells(i + 1, 16) = "A" & iAux
            vBin = 1
        Else
            Cells(i + 1, 3) = iAux - 1
            'Cuadrande direccional NE
            If vCXFin >= vCXInicio And vCYFin >= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaDerFin - vDxs * (iAux1 - 1)
                Cells(i + 1, 6) = vCYBancaDerFin + vDys * (iAux1 - 1)
            End If
            'Cuadrande direccional NW
            If vCXFin <= vCXInicio And vCYFin >= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaDerFin - vDxs * (iAux1 - 1)
                Cells(i + 1, 6) = vCYBancaDerFin - vDys * (iAux1 - 1)
            End If
            'Cuadrande direccional SE
            If vCXFin >= vCXInicio And vCYFin <= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaDerFin + vDxs * (iAux1 - 1)
                Cells(i + 1, 6) = vCYBancaDerFin + vDys * (iAux1 - 1)
            End If
            'Cuadrande direccional SW
            If vCXFin <= vCXInicio And vCYFin <= vCYInicio Then
                Cells(i + 1, 5) = vCXBancaDerFin + vDxs * (iAux1 - 1)
                Cells(i + 1, 6) = vCYBancaDerFin - vDys * (iAux1 - 1)
            End If
            Cells(i + 1, 7) = vCZFin + vHd
            Cells(i + 1, 8) = vCZFin + vHd + vDas
            Cells(i + 1, 9) = vCZFin + vHd + vDas / 2
            Cells(i + 1, 10) = vLa
            Cells(i + 1, 11) = vDas
            Cells(i + 1, 12) = vRiver
            Cells(i + 1, 13) = vReach
            Cells(i + 1, 14) = vRS
            Cells(i + 1, 16) = "A" & iAux
            vBin = 0
        End If
        i = i + 1
        If i Mod 2 = 0 Then
            iAux = iAux + 1
            iAux1 = iAux1 + 1
        End If
    Wend
    'Sheets(vHojaGIS).Range("L1") = i - 1       'Test
End Sub

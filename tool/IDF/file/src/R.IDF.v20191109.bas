Attribute VB_Name = "IDF"
Sub R_HydroStormMarker()
    'Creado por: r.cfdtools@gmail.com
    'Información, licencia y condiciones de uso en https://github.com/r-cfdtools/R.HydroStormMarkerIDF
    vAppName = "R.HydroStormMarker"
    vCreateBy = "r.cfdtools@gmail.com"
    vTInicioCalc = Timer()
    vHojaDatos = "Datos"
    vHojaTormentaResumen = "TormentaResumen"
    vHojaIDFCluster = "IDFCluster"
    vHojaIDFClusterIntensidad = "IDFClusterIntensidad"
    vHojaIDFValores = "IDFValores"
    vHojaIDFSerie = "IDFSerie"
    vHojaSetup = "Setup"
    Sheets(vHojaDatos).Select
    vCeldaRegistros = "C5"
    vCeldaNumTormentas = "E4"
    vCeldaIntervalo = "E3"
    vCeldaCeroIntermedio = "E5"         'Numero de ceros intermedios permitidos en una misma tormenta
    vCeldaBorraCeroInter = "G5"         'Eliminar filas con ceros consecutivos intermedios
    vCeldaMaxDuracion = "I3"            'Máxima duración encontrada en todas las tormentas
    vCeldaIDFCluster = "I4"             'Calcular valores máximos por cluster de duración
    vCeldaMaxDuracionUsr = "I5"         'Máxima duración definida por el usuario para IDF Clústers
    vColAnno = 2                        'Columna B de Años
    vColDato = 6                        'Columna F de datos
    vFilaRotulo = 8                     'Fila de rótulos de datos
    vFilaInicio = 9                     'Fila de inicio de datos
    vColCerosIde = 9                    'Columna I para marcación de celdas con ceros consecutivos
    vColTormentaNum = 10                'Columna J para marcación de tormentas
    vColDatoAcumulado = 11              'Columna K de para acumulación de valores por tormenta
    vColFrecAcum = 12                   'Columna L de marcación de intervalos o frecuencias acumuladas por evento
    vColIDFCluster = 13                 'Columna M de inicio de valores calculados para IDF Cluster
    vRegistros = (Range("B9").End(xlDown).Row) - vFilaInicio + 1 'Total de registros a procesar
    Range(vCeldaRegistros) = vRegistros
    vRegistrosIDFCluster = Sheets(vHojaIDFClusterIntensidad).Range("C5")
    vRegistrosTr = Sheets(vHojaIDFClusterIntensidad).Range("E3")
    vFilaFin = vFilaInicio + vRegistros
    vFilaFinIDFCluster = vFilaInicio + vRegistrosIDFCluster
    vMsgBoxTxt = "Registros a procesar: " & vRegistros & vbNewLine & Now & vbNewLine & vbNewLine & vCreateBy & vbNewLine & vbNewLine & "Antes de ejecutar limpie los filtros " & vbNewLine & "de la hoja Datos y TormentaResumen" & vbNewLine & "y cierre los otros libros de Excel." & vbNewLine & vbNewLine & "Continuar..."
    Dim answer As Integer
    vAnswer = MsgBox(vMsgBoxTxt, vbYesNo + vbQuestion, vAppName)
    vCuentaTormenta = 1
    
    If vAnswer = vbYes Then
    
        'LIMPIAR ANALISIS ACTUAL
        Sheets(vHojaDatos).Range(Cells(vFilaInicio, vColCerosIde), Cells(1048576, vColFrecAcum)).ClearContents
        Sheets(vHojaDatos).Range(Cells(vFilaRotulo, vColIDFCluster), Cells(1048576, 10000)).ClearContents
        Sheets(vHojaDatos).Range("M7").ClearContents
        Sheets(vHojaTormentaResumen).Range("A3:L1048576").ClearContents
        Sheets(vHojaIDFCluster).Range("C8:ZZ8").ClearContents
        Sheets(vHojaIDFCluster).Range("A9:ZZ1048576").ClearContents
        Sheets(vHojaIDFClusterIntensidad).Range("C8:ZZ8").ClearContents
        Sheets(vHojaIDFClusterIntensidad).Range("A9:ZZ1048576").ClearContents
        Sheets(vHojaIDFValores).Range("B8:H1048576").ClearContents
        Sheets(vHojaIDFSerie).Range("B9:H1048576").ClearContents
    
        'BORRADO Y MARCADO DE CEROS CONSECUTIVOS DE LA SERIE
        If Range(vCeldaBorraCeroInter) = "SI" Then
            For i = vFilaInicio To vFilaFin - 1
                If Cells(i, vColDato) = 0 And Cells(i + 1, vColDato) = 0 And Cells(i + 2, vColDato) = 0 Then
                    Range(Cells(i, 2), Cells(i, 12)).ClearContents 'Limpiar celdas de la fila identificada entre columnas 2 y 12
                Else
                    Cells(i, vColCerosIde) = 1
                End If
            Next i
            If Range(vCeldaCeroIntermedio) > 1 Then Range(vCeldaCeroIntermedio) = 1
            Sheets(vHojaDatos).Range("B9:H1048576").Sort Key1:=Range("H9:H1048576"), Header:=xlNo
            vRegistros = (Range("B9").End(xlDown).Row) - vFilaInicio + 1 'Total de registros a procesar
            vFilaFin = vFilaInicio + vRegistros
            Range(vCeldaRegistros) = vRegistros
        Else
            For i = vFilaInicio To vFilaFin - 1
                If Cells(i, vColDato) = 0 And Cells(i + 1, vColDato) = 0 And Cells(i + 2, vColDato) = 0 Then
                    Cells(i, vColCerosIde) = 1
                End If
            Next i
        End If
        
        'IDENTIFICACIÓN Y NUMERACIÓN DE TORMENTAS
        For i = vFilaInicio To vFilaFin - 1
            Cells(i, vColTormentaNum) = vCuentaTormenta
            If Range(vCeldaCeroIntermedio) <= 0 Then 'Sin ceros consecutivos
                If Cells(i, vColDato) > 0 And Cells(i + 1, vColDato) = 0 Then vCuentaTormenta = vCuentaTormenta + 1
            End If
            If Range(vCeldaCeroIntermedio) = 1 Then 'Un cero consecutivo
                If Cells(i, vColDato) > 0 And (Cells(i + 1, vColDato) = 0 And Cells(i + 2, vColDato) = 0) Then vCuentaTormenta = vCuentaTormenta + 1
            End If
            If Range(vCeldaCeroIntermedio) = 2 Then 'Dos ceros consecutivo
                If Cells(i, vColDato) > 0 And (Cells(i + 1, vColDato) = 0 And Cells(i + 2, vColDato) = 0 And Cells(i + 3, vColDato) = 0) Then vCuentaTormenta = vCuentaTormenta + 1
            End If
            If Range(vCeldaCeroIntermedio) >= 3 Then 'Tres ceros consecutivo
                If Cells(i, vColDato) > 0 And (Cells(i + 1, vColDato) = 0 And Cells(i + 2, vColDato) = 0 And Cells(i + 3, vColDato) = 0 And Cells(i + 4, vColDato) = 0) Then vCuentaTormenta = vCuentaTormenta + 1
            End If
        Next i
        Range(vCeldaNumTormentas) = vCuentaTormenta - 1 'Número de tormentas identificadas
    
        'ACUMULAR VALORES EN CADA TORMENTA
        vIAux1 = 3 'Fila en la tabla de TormentaResumen a partir de la cual se inicia el registro
        For i = vFilaInicio To vFilaFin
            If i = vFilaInicio Then
                Cells(i, vColDatoAcumulado) = Cells(i, vColDato)
            Else
                If Cells(i, vColTormentaNum) = Cells(i - 1, vColTormentaNum) Then
                    vDatoAcumulado = Cells(i, vColDato) + Cells(i - 1, vColDatoAcumulado)
                    Cells(i, vColDatoAcumulado) = vDatoAcumulado
                Else
                    Cells(i, vColDatoAcumulado) = Cells(i, vColDato)
                    vIAux1 = vIAux1 + 1
                End If
            End If
        Next i
    
        'MARCACIÓN DE LA COLUMNA DE FRECUENCIAS ACUMULADAS POR TORMENTA. COLOCAR LUEGO DE ACUMULAR VALORES
        'Atención: Para el correcto funcionamiento de esta opción, es necesario ejecutar previamente el algoritmo eliminación de ceros intermedios para ejecutar esta opción
        vIntervalo = 0
        vIntervaloMax = 0
        For i = vFilaInicio To vFilaFin - 1
            If Cells(i, vColTormentaNum) = Cells(i + 1, vColTormentaNum) Then
                If (Cells(i, vColDatoAcumulado) > 0) Or (Cells(i + 1, vColDatoAcumulado) > 0) Then
                    Cells(i, vColFrecAcum) = vIntervalo
                    vIntervalo = vIntervalo + Range(vCeldaIntervalo)
                End If
                
            Else
                If vIntervalo > vIntervaloMax Then vIntervaloMax = vIntervalo + Range(vCeldaIntervalo) 'Evaluación de la máxima frecuencia acumulada encontrada
                Cells(i, vColFrecAcum) = vIntervalo
                vIntervalo = 0
            End If
        Next i
        Range(vCeldaMaxDuracion) = vIntervaloMax - Range(vCeldaIntervalo)

        'REGISTRAR RESUMEN EN HOJA TormentaResumen
        vIAux1 = 3 'Fila en la tabla de TormentaResumen a partir de la cual se inicia el registro
        For i = vFilaInicio To vFilaFin
            If i <> vFilaInicio Then
                If Cells(i, vColTormentaNum) <> Cells(i - 1, vColTormentaNum) Then
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 2) = Sheets(vHojaDatos).Cells(i - 1, 2)  'Año
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 3) = Sheets(vHojaDatos).Cells(i - 1, 3)  'Mes
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 4) = Sheets(vHojaDatos).Cells(i - 1, 4)  'Día
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 5) = Sheets(vHojaDatos).Cells(i - 1, 10) 'Tormenta #
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 6) = Sheets(vHojaDatos).Cells(i - 1, 12) / Range(vCeldaIntervalo) '# Pulsos
                    If Sheets(vHojaDatos).Cells(i - 1, 12) / Range(vCeldaIntervalo) = 0 Then Sheets(vHojaTormentaResumen).Cells(vIAux1, 6) = 1
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 7) = Sheets(vHojaDatos).Cells(i - 1, 12) 'Duración
                    If Sheets(vHojaDatos).Cells(i - 1, 12) = 0 Then Sheets(vHojaTormentaResumen).Cells(vIAux1, 7) = Range(vCeldaIntervalo)
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 8) = Sheets(vHojaDatos).Cells(i - 1, 11) 'Dato acumulado o total al final del evento
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 9) = (Sheets(vHojaTormentaResumen).Cells(vIAux1, 8) * 60) / (Sheets(vHojaTormentaResumen).Cells(vIAux1, 6) * Range(vCeldaIntervalo)) 'Intensidad
                    vIAux1 = vIAux1 + 1
                End If
            End If
        Next i
    
        'CALCULO DE CLUSTERS
        'Atención: Para el correcto funcionamiento de esta opción, es necesario ejecutar previamente el algoritmo eliminación de ceros intermedios para ejecutar esta opción
        'Marcación de columnas hasta frecuencia máxima acumulada
        If Range(vCeldaMaxDuracionUsr) < Range(vCeldaMaxDuracion) And Range(vCeldaMaxDuracionUsr) > 0 Then
            vMaxNumPulsos = Range(vCeldaMaxDuracionUsr) / Range(vCeldaIntervalo)
        Else
            vMaxNumPulsos = Range(vCeldaMaxDuracion) / Range(vCeldaIntervalo)
        End If
        If Range(vCeldaIDFCluster) = "SI" Then
            Range("M7") = "CÁLCULO DE IDF CLUSTERS PARA CADA DELTA DE TIEMPO (Dt)"
            For i = 0 To vMaxNumPulsos - 1
                Cells(vFilaRotulo, vColIDFCluster + i) = (i * Range(vCeldaIntervalo)) + Range(vCeldaIntervalo)
                Sheets(vHojaIDFCluster).Cells(vFilaRotulo, 3 + i) = (i * Range(vCeldaIntervalo)) + Range(vCeldaIntervalo)
                Sheets(vHojaIDFClusterIntensidad).Cells(vFilaRotulo, 3 + i) = (i * Range(vCeldaIntervalo)) + Range(vCeldaIntervalo)
            Next i
        End If
        'Delta 1 inicial (corresponde al mismo valor del dato original) (Hoja: Datos)
         If Range(vCeldaIDFCluster) = "SI" Then
            For i = vFilaInicio To vFilaFin - 1
                iAux = 0
                If Cells(i, vColTormentaNum) = Cells(i + 1, vColTormentaNum) Then
                    Cells(i + 1, vColIDFCluster) = Cells(i + 1, vColDatoAcumulado) - Cells(i, vColDatoAcumulado)
                Else
                    If Cells(i + 1, vColDatoAcumulado) <> 0 Or Cells(i + 2, vColDatoAcumulado) <> 0 Then
                        Cells(i + 1, vColIDFCluster) = 0
                    End If
                End If
            Next i
        End If
        'Deltas 2 y siguientes (Hoja: Datos)
        vCluster = 0
        If Range(vCeldaIDFCluster) = "SI" Then
            For iAux = 2 To vMaxNumPulsos
                For i = vFilaInicio To vFilaFin - 1
                    iAux2 = 0
                    vTormentaActual = Cells(i, vColTormentaNum)
                    For iAux1 = 0 To iAux - 1
                        If Cells(i + iAux1, vColTormentaNum) = vTormentaActual Then
                            vCluster = vCluster + Cells(i + iAux1 + 1, vColIDFCluster)
                            iAux2 = iAux2 + 1
                        End If
                    Next iAux1
                    If iAux2 = iAux And Cells(i + iAux, vColTormentaNum) = vTormentaActual Then
                        If (Cells(i, vColDatoAcumulado) > 0) Or (Cells(i + 1, vColDatoAcumulado) > 0) Then
                            Cells(i + 1, vColIDFCluster + iAux - 1) = vCluster
                        End If
                    End If
                    vCluster = 0
                Next i
            Next iAux
        End If
        'Hoja IDFCluster resume los valores máximos encontrados por año para cada delta de duración.
        If Range(vCeldaIDFCluster) = "SI" Then
            vCluster = 0
            For iAux = 0 To vMaxNumPulsos - 1
                iAux2 = 0
                'vCluster = 0
                For i = vFilaInicio To vFilaFin - 1
                    If Cells(i, vColAnno) = Cells(i + 1, vColAnno) Then
                        If Cells(i, vColIDFCluster + iAux) > vCluster Then
                            vCluster = Cells(i, vColIDFCluster + iAux)
                        End If
                    Else
                        If Cells(i, vColIDFCluster + iAux) > vCluster Then 'Evalua última celda de cada año
                            vCluster = Cells(i, vColIDFCluster + iAux)
                        End If
                        Sheets(vHojaIDFCluster).Cells(vFilaInicio + iAux2, 2) = Cells(i - 1, vColAnno) 'Año
                        Sheets(vHojaIDFClusterIntensidad).Cells(vFilaInicio + iAux2, 2) = Cells(i - 1, vColAnno) 'Año
                        If vCluster <> 0 Then
                            Sheets(vHojaIDFCluster).Cells(vFilaInicio + iAux2, 3 + iAux) = vCluster 'Valor máximo
                            Sheets(vHojaIDFClusterIntensidad).Cells(vFilaInicio + iAux2, 3 + iAux) = (vCluster * 60) / ((iAux + 1) * Range(vCeldaIntervalo)) 'Intensidad máxima
                        End If
                        iAux2 = iAux2 + 1
                        vCluster = 0
                    End If
                Next i
            Next iAux
        End If
        'Hoja IDFClusterIntensidad: Calcular los valores de la curva IDF.
        If Range(vCeldaIDFCluster) = "SI" Then
            Sheets(vHojaIDFClusterIntensidad).Select
            Sheets(vHojaIDFClusterIntensidad).Cells(vFilaInicio + vRegistrosIDFCluster + 1, 2) = "Promedio"
            Sheets(vHojaIDFClusterIntensidad).Cells(vFilaInicio + vRegistrosIDFCluster + 2, 2) = "Desv. Est."
            Sheets(vHojaIDFClusterIntensidad).Cells(vFilaInicio + vRegistrosIDFCluster + 3, 2) = "n"
            Sheets(vHojaIDFClusterIntensidad).Cells(vFilaInicio + vRegistrosIDFCluster + 4, 2) = "Yn"
            Sheets(vHojaIDFClusterIntensidad).Cells(vFilaInicio + vRegistrosIDFCluster + 5, 2) = "Sn"
            Sheets(vHojaIDFClusterIntensidad).Cells(vFilaInicio + vRegistrosIDFCluster + 7, 2) = "Tr"
            
            vFilaFin = vFilaInicio + vRegistrosIDFCluster - 1
            For iAux = 0 To vMaxNumPulsos - 1
                vRango = Range(Cells(vFilaInicio, 3 + iAux), Cells(vFilaFin, 3 + iAux))
                Cells(vFilaFin + 2, 3 + iAux) = Application.Average(vRango) 'Promedio
                Cells(vFilaFin + 3, 3 + iAux) = Application.StDev(vRango) 'Desviación estándar StDev, StDevP
                Cells(vFilaFin + 4, 3 + iAux) = Application.Count(vRango) 'n
                Cells(vFilaFin + 5, 3 + iAux) = fGumbelYn(Cells(vFilaFin + 4, 3 + iAux)) 'Yn
                Cells(vFilaFin + 6, 3 + iAux) = fGumbelSn((Cells(vFilaFin + 4, 3 + iAux)), (Cells(vFilaFin + 5, 3 + iAux))) 'Sn
            Next iAux
            'Marcación de periodos de retorno Tr
            For iAux = 0 To vRegistrosTr - 1
                Cells(vFilaFin + iAux + 9, 2) = Sheets(vHojaSetup).Cells(4 + iAux, 14)
            Next iAux
            For iAux = 0 To vMaxNumPulsos - 1
                Cells(vFilaInicio + vRegistrosIDFCluster + 7, 3 + iAux) = Cells(vFilaRotulo, 3 + iAux)
            Next iAux
            'Estimación de precipitación para diferentes periodos de retorno =((-LN(-LN((1-(1/Tr)))))/(Sn/DesvStd))+(Promedio-DesvStd*(Yn/Sn))
            Range("E4") = vFilaFin + 8
            For iAux = 0 To vMaxNumPulsos - 1
                For iAux1 = 0 To vRegistrosTr - 1
                    vTr = Cells(vFilaFin + iAux1 + 9, 2)
                    vPromedio = Cells(vFilaFin + 2, 3 + iAux)
                    vDesvStd = Cells(vFilaFin + 3, 3 + iAux)
                    vYn = Cells(vFilaFin + 5, 3 + iAux)
                    vSn = Cells(vFilaFin + 6, 3 + iAux)
                    Cells(vFilaFin + iAux1 + 9, 3 + iAux) = ((-Log(-Log((1 - (1 / vTr))))) / (vSn / vDesvStd)) + (vPromedio - vDesvStd * (vYn / vSn))
                Next iAux1
            Next iAux
        End If
        'Copiado y pegado de valores estimados de precipitación para diferentes Tr en la hoja IDFValores. Requerido para la graficación de la IDF
        If Sheets(vHojaDatos).Range(vCeldaIDFCluster) = "SI" Then
            vRegInicioTr = Sheets(vHojaIDFClusterIntensidad).Range("E4")
            vRegFinTr = vRegInicioTr + Sheets(vHojaIDFClusterIntensidad).Range("E3")
            Range(Cells(vRegInicioTr, 2), Cells(vRegFinTr, 2 + vMaxNumPulsos)).Select
            Selection.Copy
            Sheets(vHojaIDFValores).Select
            Range("B8").Select
            Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks:=False, Transpose:=False
        End If
        'IDF clústers. Series de valores obtenidos para la construcción de la ecuación característica a partir de correlación múltiple
        If Sheets(vHojaDatos).Range(vCeldaIDFCluster) = "SI" Then
            For iAux = 0 To vMaxNumPulsos - 1
                For iAux1 = 0 To vRegistrosTr - 1
                    vDatoNum = (iAux * vRegistrosTr) + iAux1 + 1
                    'MsgBox vDatoNum
                    Sheets(vHojaIDFSerie).Cells(vFilaInicio + vDatoNum - 1, 2) = vDatoNum '# Dato
                    Sheets(vHojaIDFSerie).Cells(vFilaInicio + vDatoNum - 1, 3) = Sheets(vHojaIDFValores).Cells(vFilaInicio + iAux1, 3 + iAux) 'i: Intensidad
                    Sheets(vHojaIDFSerie).Cells(vFilaInicio + vDatoNum - 1, 4) = Sheets(vHojaIDFValores).Cells(vFilaInicio - 1, 3 + iAux) 'd: Duración
                    Sheets(vHojaIDFSerie).Cells(vFilaInicio + vDatoNum - 1, 5) = Sheets(vHojaIDFValores).Cells(vFilaInicio + iAux1, 2) 'f: Frecuencia o Tr
                    Sheets(vHojaIDFSerie).Cells(vFilaInicio + vDatoNum - 1, 6) = Log(Sheets(vHojaIDFSerie).Cells(vFilaInicio + vDatoNum - 1, 3)) 'Ln (i): Logaritmo de la Intensidad
                    Sheets(vHojaIDFSerie).Cells(vFilaInicio + vDatoNum - 1, 7) = Log(Sheets(vHojaIDFSerie).Cells(vFilaInicio + vDatoNum - 1, 4)) 'Ln (d): Logaritmo de la Duración
                    Sheets(vHojaIDFSerie).Cells(vFilaInicio + vDatoNum - 1, 8) = Log(Sheets(vHojaIDFSerie).Cells(vFilaInicio + vDatoNum - 1, 5)) 'Ln (f): Logaritmo de la Frecuencia o Tr
                Next iAux1
            Next iAux
        End If
                
        'TIEMPO TOTAL DE CÁLCULO
        vTFinCalc = Timer()
        vTTotalCalc = (vTFinCalc - vTInicioCalc) & "s"
        vMsgBoxTxt = "Proceso Completado" & vbNewLine & Now & vbNewLine & "dt: " & vTTotalCalc & vbNewLine & "# Tormentas: " & (vCuentaTormenta - 1) & vbNewLine & vbNewLine & vCreateBy
        MsgBox vMsgBoxTxt, , vAppName
        
    End If 'Para vAnswer
    
End Sub


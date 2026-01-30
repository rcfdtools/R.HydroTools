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
    Sheets(vHojaDatos).Select
    vCeldaRegistros = "C4"
    vCeldaNumTormentas = "E4"
    vCeldaIntervalo = "C5"
    vCeldaCeroIntermedio = "E5"         'Numero de ceros intermedios permitidos en una misma tormenta
    vCeldaBorraCeroInter = "G5"         'Eliminar filas con ceros consecutivos intermedios
    vCeldaMaxDuracion = "I3"            'Máxima duración encontrada en todas las tormentas
    vCeldaIDFCluster = "I4"             'Calcular valores máximos por cluster de duración
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
    vFilaFin = vFilaInicio + vRegistros
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
        Sheets(vHojaIDFCluster).Range("C2:ZZ2").ClearContents
        Sheets(vHojaIDFCluster).Range("A3:ZZ1048576").ClearContents
        
    
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
    
        'ACUMULAR VALORES EN CADA TORMENTA Y REGISTRAR RESUMEN EN HOJA TormentaResumen
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
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 2) = Sheets(vHojaDatos).Cells(i - 1, 2)  'Año
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 3) = Sheets(vHojaDatos).Cells(i - 1, 3)  'Mes
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 4) = Sheets(vHojaDatos).Cells(i - 1, 4)  'Día
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 5) = Sheets(vHojaDatos).Cells(i - 1, 10) 'Tormenta #
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 6) = Sheets(vHojaDatos).Cells(i - 1, 12) / Range(vCeldaIntervalo) '# Pulsos
                    If Sheets(vHojaDatos).Cells(i - 1, 12) / Range(vCeldaIntervalo) = 0 Then Sheets(vHojaTormentaResumen).Cells(vIAux1, 6) = 1
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 7) = Sheets(vHojaDatos).Cells(i - 1, 12) 'Duración
                    If Sheets(vHojaDatos).Cells(i - 1, 12) = 0 Then Sheets(vHojaTormentaResumen).Cells(vIAux1, 7) = Range(vCeldaIntervalo)
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 8) = vDatoAcumulado                      'Dato acumulado o total al final del evento
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 9) = (Sheets(vHojaTormentaResumen).Cells(vIAux1, 8) * 60) / (Sheets(vHojaTormentaResumen).Cells(vIAux1, 6) * Range(vCeldaIntervalo)) 'Intensidad
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
    
        'CALCULO DE CLUSTERS
        'Atención: Para el correcto funcionamiento de esta opción, es necesario ejecutar previamente el algoritmo eliminación de ceros intermedios para ejecutar esta opción
        'Marcación de columnas hasta frecuencia máxima acumulada
        vMaxNumPulsos = Range(vCeldaMaxDuracion) / Range(vCeldaIntervalo)
        If Range(vCeldaIDFCluster) = "SI" Then
            Range("M7") = "CÁLCULO DE IDF CLUSTERS PARA CADA DELTA DE TIEMPO (Dt)"
            For i = 0 To vMaxNumPulsos - 1
                Cells(vFilaRotulo, vColIDFCluster + i) = (i * Range(vCeldaIntervalo)) + Range(vCeldaIntervalo)
                Sheets(vHojaIDFCluster).Cells(2, 3 + i) = (i * Range(vCeldaIntervalo)) + Range(vCeldaIntervalo)
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
                        Sheets(vHojaIDFCluster).Cells(3 + iAux2, 2) = Cells(i - 1, vColAnno) 'Año
                        Sheets(vHojaIDFCluster).Cells(3 + iAux2, 3 + iAux) = vCluster 'Valor máximo
                        iAux2 = iAux2 + 1
                        vCluster = 0
                    End If
                Next i
            Next iAux
        End If
        
        'TIEMPO TOTAL DE CÁLCULO
        vTFinCalc = Timer()
        vTTotalCalc = (vTFinCalc - vTInicioCalc) & "s"
        vMsgBoxTxt = "Proceso Completado" & vbNewLine & Now & vbNewLine & "dt: " & vTTotalCalc & vbNewLine & "# Tormentas: " & (vCuentaTormenta - 1) & vbNewLine & vbNewLine & vCreateBy
        MsgBox vMsgBoxTxt, , vAppName
        
    End If 'Para vAnswer
    
End Sub

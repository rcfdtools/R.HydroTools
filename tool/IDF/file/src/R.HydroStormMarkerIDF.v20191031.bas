Attribute VB_Name = "IDF"
Sub R_HydroStormMarker()
    'Creado por: r.cfdtools@gmail.com
    'https://github.com/r-cfdtools/R.HydroStormMarker
    vAppName = "R.HydroStormMarker"
    vCreateBy = "r.cfdtools@gmail.com"
    vTInicioCalc = Timer()
    vHojaDatos = "Datos"
    vHojaTormentaResumen = "TormentaResumen"
    Sheets(vHojaDatos).Select
    vCeldaRegistros = "C4"
    vCeldaNumTormentas = "E4"
    vCeldaIntervalo = "C5"
    vCeldaCeroIntermedio = "E5"         'Numero de ceros intermedios permitidos en una misma tormenta
    vCeldaBorraCeroInter = "G5"         'Eliminar filas con ceros consecutivos intermedios
    vColDato = 6                        'Columna F de datos
    vFilaInicio = 9                     'Fila de inicio de datos
    vColCerosIde = 9                    'Columna I para marcación de celdas con ceros consecutivos
    vColTormentaNum = 10                'Columna J para marcación de tormentas
    vColDatoAcumulado = 11              'Columna K de para acumulación de valores por tormenta
    vRegistros = (Range("B9").End(xlDown).Row) - vFilaInicio + 1 'Total de registros a procesar
    Range(vCeldaRegistros) = vRegistros
    vFilaFin = vFilaInicio + vRegistros
    vMsgBoxTxt = "Registros a procesar: " & vRegistros & vbNewLine & Now & vbNewLine & vbNewLine & vCreateBy & vbNewLine & vbNewLine & "Antes de ejecutar limpie los filtros " & vbNewLine & "de la hoja Datos y TormentaResumen" & vbNewLine & "y cierre los otros libros de Excel." & vbNewLine & vbNewLine & "EJECUTAR"
    Dim answer As Integer
    vAnswer = MsgBox(vMsgBoxTxt, vbYesNo + vbQuestion, vAppName)
    vCuentaTormenta = 1
    
    If vAnswer = vbYes Then
    
        'BORRADO DE CEROS CONSECUTIVOS DE LA SERIE
        If Range(vCeldaBorraCeroInter) = "SI" Then
            For i = vFilaInicio To vFilaFin - 1
                If Cells(i, vColDato) = 0 And Cells(i + 1, vColDato) = 0 And Cells(i + 2, vColDato) = 0 Then
                    Range(Cells(i, 2), Cells(i, 12)).ClearContents 'Limpiar celdas de la fila identificada entre columnas 2 y 12
                End If
            Next i
            If Range(vCeldaCeroIntermedio) > 1 Then Range(vCeldaCeroIntermedio) = 1
        End If
        Sheets(vHojaDatos).Range("B9:H1048576").Sort Key1:=Range("H9:H1048576"), Header:=xlNo
        vRegistros = (Range("B9").End(xlDown).Row) - vFilaInicio + 1 'Total de registros a procesar
        vFilaFin = vFilaInicio + vRegistros
        Range(vCeldaRegistros) = vRegistros
        
        'LIMPIAR ANALISIS ACTUAL
        Range(Cells(vFilaInicio, vColCerosIde), Cells(1048576, vColDatoAcumulado)).ClearContents
        Sheets(vHojaTormentaResumen).Range("A3:L1048576").ClearContents
        
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
        Range(vCeldaNumTormentas) = vCuentaTormenta 'Número de tormentas identificadas
    
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
                    Sheets(vHojaTormentaResumen).Cells(vIAux1, 8) = vDatoAcumulado                      'Dato acumulado o total al final del evento
                    vIAux1 = vIAux1 + 1
                End If
            End If
        Next i
    
        'PULSOS POR CADA TORMENTA (Datos en ceros dentro de una misma tormenta no se consideran como pulso válido) A REGISTRAR RESUMEN EN HOJA TormentaResumen
        vIAux1 = 3 'Fila en la tabla de TormentaResumen a partir de la cual se inicia el registro
        vIAux2 = 1 'Conteo de pulsos validos en cada tormenta
        For i = vFilaInicio To vFilaFin
            If Cells(i, vColTormentaNum) = Cells(i + 1, vColTormentaNum) Then
                If Cells(i, vColDato) > 0 Then vIAux2 = vIAux2 + 1
            Else
                Sheets(vHojaTormentaResumen).Cells(vIAux1, 6) = vIAux2 '# Pulsos
                Sheets(vHojaTormentaResumen).Cells(vIAux1, 7) = vIAux2 * Range(vCeldaIntervalo) 'Duracion
                Sheets(vHojaTormentaResumen).Cells(vIAux1, 9) = (Sheets(vHojaTormentaResumen).Cells(vIAux1, 8) * 60) / (vIAux2 * Range(vCeldaIntervalo)) 'Intensidad
                vIAux2 = 1
                vIAux1 = vIAux1 + 1
            End If
        Next i
        
        'TIEMPO TOTAL DE CÁLCULO
        vTFinCalc = Timer()
        vTTotalCalc = (vTFinCalc - vTInicioCalc) & "s"
        vMsgBoxTxt = "Proceso Completado" & vbNewLine & Now & vbNewLine & "dt: " & vTTotalCalc & vbNewLine & "# Tormentas: " & (vCuentaTormenta - 1) & vbNewLine & vbNewLine & vCreateBy
        MsgBox vMsgBoxTxt, , vAppName
        
    End If 'Para vAnswer
    
End Sub

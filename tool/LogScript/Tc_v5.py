# -*- coding: UTF-8 -*-
# Nombre: Tc_v4.py
# Descripción: Script interactivo e iterativo para el cálculo y graficación del tiempo de concentración con control de excepción de errores y archivo de registro log.
# Requerimiento: PyCharm 2020.1+, Python 2.7.5 (ArcGIS 10.2.2), Python 3.10.0 (instalación independiente).

# Librerías
import sys
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime

# Variables internas y archivo log de resultados
i, variaciones, pendienteMinima = 0, 32, 0.001 # Incremento, variaciones y pendiente mínima
fileLog = open('Tc_v5Log.txt','w+') # w+ para crear el archivo si no existe

# Función de cálculo
def TcGiandotti(A,L,S):
    return (4*(A**0.5)+1.5*L)/(25.3*(S*L)**0.5)

# Función para creación de líneas de separación
def Separador(n, enLog): #Usando un valor por defecto de 24 guiones
    nc = '-'
    print(nc*n)
    if enLog == True:
        fileLog.write(nc*n + '\n')

# Función de impresión en pantalla y log de resultados
def PrintLog(txtPrint, enPantalla):
    if enPantalla == True:
        print(txtPrint)
    fileLog.write(txtPrint + '\n')

# Cabecera
Separador(117, True)
PrintLog('Script interactivo e iterativo en Python con graficación, control de excepción de errores y archivo log de resultados', True)
Separador(117, True)
PrintLog(   'Cálculo y graficación del Tiempo de Concentración de una cuenca hidrográfica usando la expresión de Giandotti.\n'
            'Python versión: ' + str(sys.version) + '\n'
            'matplotlib versión: ' + str(matplotlib.__version__) + '\n'
            'Encuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/LogScript\n'
            'Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License\n'
            'Créditos: r.cfdtools@gmail.com\n'
            'Ejecutado en: '+str(datetime.now())+'\n', True)
Separador(34, True)
PrintLog('Datos de entrada y cálculo general', True)
Separador(34, True)

# Procedimiento
try:
    ATxt, LTxt, STxt, imprimirTituloGraficaTxt = 'A, Área cuenca, km²: ', 'L, Longitud cauce principal, km: ', 'S, Pendiente media cauce principal, m/m: ', 'Imprimir título descriptivo en gráfica, Python 3 (y/n), Python 2 no recomendado ("n"): '
    A = float(input(ATxt))
    PrintLog(ATxt + str(A), False)
    L = float(input(LTxt))
    PrintLog(LTxt + str(L), False)
    S = float(input(STxt))
    PrintLog(STxt + str(S), False)
    imprimirTituloGrafica = input(imprimirTituloGraficaTxt)
    PrintLog(imprimirTituloGraficaTxt + str(imprimirTituloGrafica), False)
    if A > 0 and L > 0 and S > 0:
        #Calculos
        PrintLog('\nValores ingresados son válidos...', True)
        PrintLog('Tc, Tiempo de concentración, min: ' + str(round(TcGiandotti(A,L,S)*60,4)) +
                  '\n', True) #Impresión en pantalla usando +
        Separador(32, True)
        PrintLog('Resultados variando la pendiente', True)
        Separador(32, True)
        PrintLog('i\tS, m/m\tTc, min', True)
        TcGiandottiGx, TcGiandottiGy = [], [] #Listas para graficación de datos
        while i < variaciones:
            Svar =  (((S-pendienteMinima)/(variaciones-1))*i+pendienteMinima)
            #print(i+1, '\t', round(Svar,4), '\t', round(TcGiandotti(A,L,Svar)*60,4)) #Concatenación con coma
            PrintLog(str(i+1)+'\t'+str(round(Svar,4))+'\t'+str(round(TcGiandotti(A,L,Svar)*60,4)), True) #Concatenación con +
            TcGiandottiGx.append(Svar)
            TcGiandottiGy.append(TcGiandotti(A,L,Svar)*60)
            i += 1

        #Graficación de datos sin registro en Log de resultados
        PrintLog('', True)
        Separador(32, True)
        PrintLog('Listas para graficación de datos', True)
        Separador(32, True)
        PrintLog('\nS, m/m: ' + str(TcGiandottiGx), True)
        PrintLog('\nTc, min: ' + str(TcGiandottiGy), True)
        graficaTitulo = 'Tc, Tiempo de concentración\nvariando la pendiente cada ' + str(
            round(((S - pendienteMinima) / (variaciones - 1)), 4)) + ' m/m\nA, km²: ' + str(A) + ', L, km: ' + str(L)
        plt.plot(TcGiandottiGx,TcGiandottiGy, label="Tc Giandotti, min", color='black', linewidth=1, marker='p', markersize=4, markerfacecolor='black', markeredgecolor='black')
        if str(imprimirTituloGrafica.lower()) == 'y': plt.title(graficaTitulo)
        plt.xlabel('S, m/m')
        plt.ylabel('Tc, min')
        plt.show()
    else:
        print('>>>Error: Ningún valor puede ser menor o igual a cero.')
except ValueError as e:
    print('>>>Error: Dato ingresado no numérico...')
print('\nArchivo log: '+ str(fileLog))

''' 
Referencias

'''
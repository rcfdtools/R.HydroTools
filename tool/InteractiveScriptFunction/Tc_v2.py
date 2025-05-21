# -*- coding: UTF-8 -*-
# Nombre: Tc_v2.py
# Descripción: Script interactivo e iterativo para el cálculo del tiempo de concentración
# Requerimiento: PyCharm 2020.1+, Python 2.7.5 (ArcGIS 10.2.2), Python 3.10.0 (instalación independiente).

# Librerías
import sys

# Variables
i, variaciones, pendienteMinima = 0, 12, 0.001 # Incremento, variaciones y pendiente mínima

# Función de cálculo
def TCGiandotti(A,L,S):
	return (4*(A**0.5)+1.5*L)/(25.3*(S*L)**0.5)

# Función para creación de líneas de separación
def Separador(n=24): # Usando un valor por defecto de 24 guiones
	nc = '-'
	print(nc*n)

# Función para crear tablas basadas en textos
def TablaTexto(var, ancho): # Variable a formatear, ancho de columna.
    return (' ' *  (ancho-len(str(var))))

# Cabecera
Separador(40)
print ('Script interactivo e iterativo en Python')
Separador(40)
print ('Cálculo del tiempo de concentración Tc de una cuenca hidrográfica utilizando la expresión de Giandotti con pendiente variable.')
print ('Python versión: ' + str(sys.version))
print ('Encuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/InteractiveScriptFunction')
print ('Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License')
print ('Créditos: r.cfdtools@gmail.com\n')

# Variables de entrada
Separador(18)
print('Datos de entrada')
Separador(18)
A = float(input('Área cuenca, km²: '))
L = float(input('Longitud cauce principal, km: '))
S = float(input('Pendiente media cauce principal, m/m: '))
tipoImpresion = input('Imprimir con formato de tabla de texto, Python 3 (y/n), Python 2 y 3 ("y"/"n"): ')

# Cálculos
if str(tipoImpresion.lower()) == 'n':
    print('\nTc, min: ' + str(TCGiandotti(A,L,S)*60)) # Impresión en pantalla usando +
    print('\nResultados variando la pendiente y utilizando columnas tabuladas')
    Separador()
    print('i\tS, m/m\tTc, min')
    Separador()
    while i < variaciones:
        Svar =  (((S-pendienteMinima)/(variaciones-1))*i+pendienteMinima)
        #print(i+1, '\t', round(Svar,4), '\t', round(TCGiandotti(A,L,Svar)*60,4)) #Concatenación con coma
        print(str(i+1)+'\t'+str(round(Svar,4))+'\t'+str(round(TCGiandotti(A,L,Svar)*60,4))) #Concatenación con +
        i += 1
else:
    print('\nTc, min: ' + str(TCGiandotti(A,L,S)*60)) #Impresión en pantalla usando +
    print('\nResultados variando la pendiente y con formato de tabla de texto')
    vColumnaAncho = 10 # Para impresión con concatenación usando coma, al ancho total por columna se le resta 3 debido a que por cada concatenación con comas se agrega un espacio.
    vColumnas = 3
    vFilaAncho = vColumnaAncho*vColumnas+4 # Para impresión con concatenación usando coma, sumar vColumnas*3
    Separador(vFilaAncho)
    # print('|', 'i', TablaTexto("i", vColumnaAncho), '|', 'S, m/m', TablaTexto('S, m/m', vColumnaAncho), '|', 'Tc, min', TablaTexto('Tc, min', vColumnaAncho), '|')  # Python 3
    print('|' + 'i' + TablaTexto("i",vColumnaAncho) + '|' + 'S, m/m' + TablaTexto('S, m/m',vColumnaAncho) + '|' + 'Tc, min' + TablaTexto('Tc, min',vColumnaAncho) + '|') # Python 2
    Separador(vFilaAncho)
    i=0
    while i < variaciones:
        Svar =  (((S-pendienteMinima)/(variaciones-1))*i+pendienteMinima)
        # print('|', i + 1, TablaTexto((i + 1), vColumnaAncho), '|', round(Svar, 4), TablaTexto(round(Svar, 4), vColumnaAncho), '|', round(TCGiandotti(A, L, Svar) * 60, 4), TablaTexto(round(TCGiandotti(A, L, Svar) * 60, 4), vColumnaAncho), '|')
        print('|' + str(i + 1) + (TablaTexto((i + 1), vColumnaAncho)) + '|' + str(round(Svar, 4)) + (TablaTexto(round(Svar, 4), vColumnaAncho)) + '|' + str(round(TCGiandotti(A, L, Svar) * 60, 4)) + (TablaTexto(round(TCGiandotti(A, L, Svar) * 60, 4), vColumnaAncho)) + '|')
        i += 1
    Separador(vFilaAncho)
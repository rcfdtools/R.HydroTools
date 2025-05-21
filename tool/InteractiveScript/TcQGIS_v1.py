# -*- coding: UTF-8 -*-
# Nombre: TcQGIS_v1.py
# Descripción: Script interactivo para el cálculo del tiempo de concentración en QGIS
# Requerimiento: QGIS 3.22.1 con Python 3.9.5

# Librerías
from PyQt5.QtWidgets import QInputDialog
import sys

# Cabecera
print ('-------------------------------------')
print ('Script interactivo en Python con QGIS')
print ('-------------------------------------\n')
print ('Cálculo del tiempo de concentración Tc de una cuenca hidrográfica utilizando la expresión de Giandotti.')
print ('Python versión: ' + str(sys.version))
print ('Encuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/InteractiveScript')
print ('Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License')
print ('Créditos: r.cfdtools@gmail.com\n')

# Variables
A = QInputDialog.getText(None, 'Área', 'Área cuenca, km²:')
L = QInputDialog.getText(None, 'Longitud', 'Longitud cauce principal, km:')
S = QInputDialog.getText(None, 'Pendiente', 'Pendiente media cauce principal, m/m:')
A = float(A[0])
L = float(L[0])
S = float(S[0])

# Cálculos e impresión de resultados
TcGiandotti = (4*(A**0.5)+1.5*L)/(25.3*(S*L)**0.5)
print ('\nParámetros de entrada')
print ('\tÁrea cuenca, km²: ' + str(A))
print ('\tLongitud cauce principal, km: ' + str(L))
print ('\tPendiente media cauce principal, m/m: ' + str(S))
print ('\nResultados')
print ("\tTc, min: " + str(TcGiandotti*60)) # Impresión en pantalla usando +

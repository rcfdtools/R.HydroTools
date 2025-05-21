# -*- coding: UTF-8 -*-
# Nombre: Tc_v1.py
# Descripción: Script interactivo para el cálculo del tiempo de concentración
# Requerimiento: PyCharm 2020.1+, Python 2.7.5 (ArcGIS 10.2.2), Python 3.10.0 (instalación independiente). ArcGIS Pro 2.9 Notebook.

# Librerías
import sys

# Cabecera
print ('-----------------------------')
print ('Script interactivo en Python')
print ('-----------------------------\n')
print ('Cálculo del tiempo de concentración Tc de una cuenca hidrográfica utilizando la expresión de Giandotti.')
print ('Python versión: ' + str(sys.version))
print ('Encuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/InteractiveScript')
print ('Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License')
print ('Créditos: r.cfdtools@gmail.com\n')

# Variables
A = float(input("Área cuenca, km²: "))
L = float(input("Longitud cauce principal, km: "))
S = float(input("Pendiente media cauce principal, m/m: "))

# Cálculos
TCGiandotti = (4*(A**0.5)+1.5*L)/(25.3*(S*L)**0.5)
print ("\nTc, min: " + str(TCGiandotti*60)) # Impresión en pantalla usando +


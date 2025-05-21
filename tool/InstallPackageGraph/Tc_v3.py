# -*- coding: UTF-8 -*-
# Nombre: Tc_v3.py
# Descripción: Script interactivo e iterativo para el cálculo y graficación del tiempo de concentración
# Requerimiento: PyCharm 2020.1+, Python 2.7.5 (ArcGIS 10.2.2), Python 3.10.0 (instalación independiente).

# Librerías
import sys
import matplotlib
import matplotlib.pyplot as plt

# Variables
i, variaciones, pendienteMinima = 0, 12, 0.001 # Incremento, variaciones y pendiente mínima

# Función de cálculo
def TcGiandotti(A,L,S):
	return (4*(A**0.5)+1.5*L)/(25.3*(S*L)**0.5)

# Función para creación de líneas de separación
def Separador(n=24): # Usando un valor por defecto de 24 guiones
	nc = "-"
	print(nc*n)

# Cabecera
Separador(56)
print ('Script interactivo e iterativo en Python con graficación')
Separador(56)
print ('Cálculo y graficación del Tiempo de Concentración de una cuenca hidrográfica usando la expresión de Giandotti.')
print ('Python versión: ' + str(sys.version))
print ('matplotlib versión: ' + str(matplotlib.__version__))
print ('Encuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/InstallPackageGraph')
print ('Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License')
print ('Créditos: r.cfdtools@gmail.com\n')

# Variables de entrada
Separador(18)
print("Datos de entrada")
Separador(18)
A = float(input("Área cuenca, km²: "))
L = float(input("Longitud cauce principal, km: "))
S = float(input("Pendiente media cauce principal, m/m: "))
imprimirTituloGrafica = input('Imprimir título descriptivo en gráfica, Python 3 (y/n), Python 2 no recomendado ("n"): ')

# Calculos
print("\nTc, min: " + str(TcGiandotti(A,L,S)*60)) # Impresión en pantalla usando +
print("\nResultados variando la pendiente y utilizando columnas tabuladas")
Separador()
print("i\tS, m/m\tTc, min")
Separador()
TcGiandottiGx, TcGiandottiGy = [], [] # Listas para graficación de datos
while i < variaciones:
	Svar =  (((S-pendienteMinima)/(variaciones-1))*i+pendienteMinima)
	# print(i+1, "\t", round(Svar,4), "\t", round(TcGiandotti(A,L,Svar)*60,4)) # Concatenación con coma
	print(str(i+1)+"\t"+str(round(Svar,4))+"\t"+str(round(TcGiandotti(A,L,Svar)*60,4))) # Concatenación con +
	TcGiandottiGx.append(Svar)
	TcGiandottiGy.append(TcGiandotti(A,L,Svar)*60)
	i += 1

# Graficación de datos
Separador()
print("Graficación de datos")
Separador()
print("S (m/m)\n",TcGiandottiGx)
print("Tc (min)\n",TcGiandottiGy)
graficaTitulo="Tc, Tiempo de concentración\nVariando la pendiente cada "+str(round(((S-pendienteMinima)/(variaciones-1)),4))+" m/m\nA, km²: "+str(A)+", L, km: "+str(L)
plt.plot(TcGiandottiGx,TcGiandottiGy, label="Tc Giandotti, min", color='black', linewidth=1, marker='p', markersize=2, markerfacecolor='black', markeredgecolor='black')
if str(imprimirTituloGrafica.lower()) == 'y': plt.title(graficaTitulo)
plt.xlabel("S, m/m")
plt.ylabel("Tc, min")
plt.show()
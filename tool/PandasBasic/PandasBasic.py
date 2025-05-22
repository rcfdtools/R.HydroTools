# -*- coding: UTF-8 -*-
# Name: PandasBasic.py
# Description: Introducción a pandas - Representación estadística de Municipios de Colombia
# Requirements: PyCharm 2021.3+, Python 3.10.0 (instalación independiente)

# Librerías
import sys
import pandas as pd # Tested with 1.3.4 version
import matplotlib.pyplot as plt # Tested with 3.5.0 version
import openpyxl # Tested with 3.0.9 version, required from pandas for read xlsx files

# Variables
csvFilesExcelSheets = ('ArcMapValor','ArcMapCount','ArcMapPercentage','ArcGISProValor','QGIS322Valor') # Nombre de archivos CSV y hojas en libro de Microsoft Excel.
absolutePath = r'D:/R.GISPython/PandasBasic' # Usar '.' para utilizar rutas absolutas.
excelFilePath = absolutePath+'/Datos/GISClassificationMethodValue.xlsx'

# Configuración general de pandas y matplotlib
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 0)
plt.rc('figure', max_open_warning = 0) # Don't show the python figure.max_open_warning

# Función para creación de líneas de separación
def Separador(n=24): # Usando un valor por defecto de 24 guiones
	nc = "-"
	print(nc*n)

# Cabecera
Separador(76)
print ('Introducción a pandas - Representación estadística de Municipios de Colombia')
Separador(76)
print ( 'Python versión: ' + str(sys.version) + '\n'
        'Encuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/PandasBasic\n'
        'Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License\n'
        'Créditos: r.cfdtools@gmail.com\n')

# Visualización y graficación de archivos CSV
Separador(43)
print ('Visualización y graficación de archivos CSV')
Separador(43)
for i in csvFilesExcelSheets:
    #filePath = r'./Datos/'+i+'.csv' # r para prevenir saltos de línea \n
    filePath = absolutePath+'/Datos/'+i+'.csv' # r para prevenir saltos de línea \n
    dataFrame = pd.read_csv(filePath, index_col=0)
    dataFrame.head() # Primera línea corresponde a cabecera de columnas
    print('\nArchivo: '+filePath)
    print(dataFrame)
    dataFrame.plot(kind='line', xlabel='Clase', ylabel='Valor', title='Graficación de '+i+' con pandas', figsize=(8, 8), alpha=0.85, rot=0, grid=True)  # alpha for transparency
    plt.savefig(absolutePath+'/Graph/' + i + 'Pandas.png')
    plt.show()
print('\n')

# Visualización de libros de Microsoft Excel
Separador(42)
print ('Visualización de libros de Microsoft Excel')
Separador(42)
print('\nLibro de Excel: '+excelFilePath)
for i in csvFilesExcelSheets:
    print('Hoja: '+i)
    dataFrame = pd.read_excel(excelFilePath, index_col=0, sheet_name=i)
    print(dataFrame)

# Graficación manual de QGIS322Valor.csv con matplotlib
csvFileLoad = absolutePath+'/Datos/QGIS322Valor.csv'
dataFrame = pd.read_csv(csvFileLoad)
plt.figure(figsize=(8, 8), dpi=100)
plt.title('Graficación manual de '+i+' con matplotlib')
plt.plot(dataFrame['Clase'],dataFrame['Natural Breaks (Jenks)'], 'r.-', label='Natural Breaks (Jenks)')
plt.plot(dataFrame['Clase'],dataFrame['Equal Interval'], 'b.-', label='Equal Interval')
plt.plot(dataFrame['Clase'],dataFrame['Quantile'], 'g.-', label='Quantile')
plt.plot(dataFrame['Clase'],dataFrame['Pretty Breaks'], 'y.-', label='Pretty Breaks')
plt.plot(dataFrame['Clase'],dataFrame['Logarithmic Scale'], 'k.-', label='Logarithmic Scale')
plt.xlabel('Clase')
plt.ylabel('Valor')
plt.legend(loc='best', shadow=False, fontsize=11)
plt.grid()
plt.xticks(dataFrame['Clase'])
plt.savefig(absolutePath+'/Graph/QGIS322ValorMatplotlib.csv.png')
plt.show()

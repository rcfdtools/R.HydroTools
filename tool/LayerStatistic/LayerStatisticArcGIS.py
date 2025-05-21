# -*- coding: UTF-8 -*-
# Nombre: LayerStatisticArcGIS.py
# Descripción: Estadísticos de capas geográficas - ArcGIS for Desktop - ArcGIS Pro
# Requerimiento: PyCharm 2021.3+, ArcGIS 10.2.2, ArcGIS Pro 2.9.0

# Librerías
import arcpy                        # Importación de arcpy de ArcGIS for Desktop.
from arcpy import env               # Importación de librería para manejo del entorno de trabajo.
arcpy.env.overwriteOutput = True    # Permitir sobreescribir archivos en directorio del entorno de trabajo.
import sys
import matplotlib
import matplotlib.pyplot as plt

# Función para creación de líneas de separación
def Separador(n=24): # Usando un valor por defecto de 24 guiones
    nc = '-'
    print(nc*n)

# Función para consultar los campos de atributos disponibles
def CapaPropiedades(i):
    cont = 1
    totalEntidades = arcpy.GetCount_management(i)
    descGeometria = arcpy.Describe(i)
    tipoGeometria = descGeometria.shapeType
    tituloCapa = 'Campos en ' + i + ' (' + tipoGeometria + 's ' + str(totalEntidades) + ')'
    Separador(len(tituloCapa))
    print(tituloCapa)
    Separador(len(tituloCapa))
    print('  #, Campo, Tipo')
    campos = arcpy.ListFields(i)
    for campo in campos:
        print('  ' + str(cont) + ', ' + campo.name + ', ' + campo.type)  # Print field properties
        cont += 1

# Variables
absolutePath = r'D:/R.GISPython/LayerStatistic' # Usar r'.' para retornar a ruta relativa
arcpy.env.workspace = absolutePath+'/Datos/'
outputPath = absolutePath+'/Output/'
layerInput = 'Precipitacion.shp'
layerSelect = outputPath+'LayerSelect.shp'
layerStatistic = outputPath+'LayerStat.dbf'
layerStatisticXLS = outputPath+'LayerStat.xls'
layerStatisticFilter = outputPath+'LayerStatFilter.dbf'
layerStatisticFilterXLS = outputPath+'LayerStatFilter.xls'

# Cabecera
Separador(67)
print ('Estadísticos de capas geográficas - ArcGIS for Desktop - ArcGIS Pro')
Separador(67)
print ( 'Compatible con: ArcGIS for Desktop y ArcGIS Pro'
        '\nPython versión: ' + str(sys.version)+
        '\nPython rutas: ' + str(sys.path[0:5])+
        '\nmatplotlib versión: ' + str(matplotlib.__version__) +
        '\nEncuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/LayerStatistic'
        '\nCláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License'
        '\nCréditos: r.cfdtools@gmail.com\n')

# Ejecución
print(  'Capa de entrada: '+layerInput+'\n'
        'Capa de filtrado: '+layerSelect+'\n'
        'Estadísticos capa entrada:  '+layerStatistic+'\n'
        'Estadísticos capa filtrada:  '+layerStatisticFilter+'\n')
CapaPropiedades(layerInput)
print('\n  Antes de continuar, cierre ArcGIS for Desktop...')
fieldEval = input('  >>> Nombre del campo numérico a evaluar (usar comillas): ')
fieldValue = input('  >>> Filrar valores >= a: ')
showData = input('  >>> Mostrar datos detallados (Y/N) (usar comillas): ')

# Mostrar datos de la tabla de atributos original
print('\n')
Separador(40)
print('Listado de entidades sin filtro de datos')
Separador(40)
cursor = arcpy.SearchCursor(layerInput)
averageValue = 0
cont = 0
print('Index, ' + fieldEval)
listaCampoEtiqueta, listaCampoEvaluar = [], []
for fila in cursor:
    if showData.lower() == 'y':
        print(str(cont) + '\t'+ str(fila.getValue(fieldEval)))
    listaCampoEtiqueta.append(cont)
    listaCampoEvaluar.append(fila.getValue(fieldEval))
    averageValue = averageValue + fila.getValue(fieldEval)
    cont+=1
print('Conteo: ' + str(cont) + '\nPromedio: '+str(averageValue / cont))
print('Generando gráfica de barras....')
plt.bar(listaCampoEtiqueta, listaCampoEvaluar, color='darkGray')
plt.title('Valores encontrados sin filtro')
plt.xlabel('Index')
plt.ylabel(fieldEval)
plt.show()

# Mostrar datos de la tabla de atributos filtrada
print('\n')
Separador(40)
print('Listado de entidades con filtro de datos')
Separador(40)
print('Ejecutando selección por filtrado...')
arcpy.Select_analysis(layerInput, layerSelect, fieldEval+'>='+str(fieldValue))
cursor = arcpy.SearchCursor(layerSelect)
averageValue = 0
cont = 0
print('Index, ' + fieldEval)
listaCampoEtiqueta, listaCampoEvaluar = [], []
for fila in cursor:
    if fila.getValue(fieldEval) >= int(fieldValue):
        if showData.lower() == 'y':
            print(str(cont) + '\t'+ str(fila.getValue(fieldEval)))
        listaCampoEtiqueta.append(cont)
        listaCampoEvaluar.append(fila.getValue(fieldEval))
        averageValue = averageValue + fila.getValue(fieldEval)
        cont+=1
print('Conteo: ' + str(cont) + '\nPromedio: '+str(averageValue / cont))
print('Generando gráfica de barras....')
plt.bar(listaCampoEtiqueta, listaCampoEvaluar, color = 'darkGray')
plt.title('Valores encontrados con filtro ' + fieldEval + ' >= '+str(fieldValue))
plt.xlabel('Index')
plt.ylabel(fieldEval)
plt.show()

# Estadísticos compatibles con ArcGIS for Desktop y ArcGIS Pro
print('\n')
Separador(55)
print('Estadísticos detallados y exportación a Microsoft Excel')
Separador(55)
print('Ejecutando estadística para ' + outputPath + layerInput + '...')
statisticsType = [[fieldEval,'SUM'],[fieldEval,'MEAN'],[fieldEval,'MIN'],[fieldEval,'MAX'],[fieldEval,'RANGE'],[fieldEval,'STD'],[fieldEval,'COUNT'],[fieldEval,'FIRST'],[fieldEval,'LAST']]
arcpy.Statistics_analysis(layerInput,layerStatistic,statisticsType)
print('Ejecutando estadística para ' + layerSelect + ' con '+ fieldEval + ' >= ' + str(fieldValue) + '...')
arcpy.Statistics_analysis(layerSelect,layerStatisticFilter,statisticsType)
# Conversión a libro de Microsoft Excel
print ('Conversión de estadísticos a XLS file...')
arcpy.TableToExcel_conversion(layerStatistic,layerStatisticXLS)
arcpy.TableToExcel_conversion(layerStatisticFilter,layerStatisticFilterXLS)
print('\nProceso completado, visualice la capa filtrada y las tablas de resultados estadísticos en ArcGIS o en Microsoft Excel.')

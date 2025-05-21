# -*- coding: UTF-8 -*-
# Nombre: LayerStatisticQGIS3.py
# Descripción: Estadísticos de capas geográficas - QGIS 3
# Requerimiento: PyCharm 2021.3+, QGIS 3.22.1

# Librerías
from qgis.core import *
import qgis.utils
import matplotlib
import matplotlib.pyplot as plt

# Función para creación de líneas de separación
def Separador(n = 24): # Usando un valor por defecto de 24 guiones
    nc = '-'
    print(nc*n)

# Variables
#qgs = QgsApplication([], False)
absolutePath = r'D:/R.GISPython/LayerStatistic/Datos/' # Usar r'.' para retornar a ruta relativa
layerInput = absolutePath+'Precipitacion.shp'
fieldEval = 'TotalAnno' # Variable para filtrado
fieldTag = 'ESTACION' # Campo para etiquetado
fieldValue = 1200 # Variable de corte para selección
recordSample = 10 # Número de registros de ejemplo a mostrar en pantalla

# Cabecera
Separador(40)
print ('Estadísticos de capas geográficas - QGIS')
Separador(40)
print ( 'Compatible con: QGIS 3'
        '\nPython versión: ' + str(sys.version)+
        '\nPython rutas: ' + str(sys.path[0:5])+
        '\nmatplotlib versión: ' + str(matplotlib.__version__) +
        '\nEncuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/LayerStatistic'
        '\nCláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License'
        '\nCréditos: r.cfdtools@gmail.com\n')

# Ejecución de procesos geográficos
print('Capa de entrada: '+layerInput)
#layerMAPProject = iface.addVectorLayer(layerInput,'','ogr') # Cargar en mapa QGIS
layerMAPProject = QgsVectorLayer(layerInput,'','ogr') # Sin cargar en mapa QGIS
print('Layer ID:', layerMAPProject.id(),'\n')
Separador(29)
print('Campos disponibles en la capa')
Separador(29)
for field in layerMAPProject.fields():
    print(field.name(), end = ', ')
entityCount = layerMAPProject.featureCount()
print('\n')
tagShow = 'Muestra de ' + str(recordSample) + ' datos'
Separador(len(tagShow))
print('Muestra de '+str(recordSample)+' datos')
Separador(len(tagShow))
print(fieldTag+', '+fieldEval)
averageValue = 0
averageValueSelect = 0
cont = 0
contAux = 0
listaCampoEtiqueta, listaCampoEvaluar, listaCampoEvaluarFiltro = [], [], []
for i in range(0, entityCount):
    listaCampoEtiqueta.append(contAux)
    featureValue = layerMAPProject.getFeature(i)
    listaCampoEvaluar.append(featureValue[fieldEval])
    #print(featureValue[0])
    if i < recordSample:
        print(featureValue[fieldTag]+', '+str(round(featureValue[fieldEval],3)))
    averageValue = averageValue + featureValue['TotalAnno']
    if featureValue['TotalAnno'] > fieldValue:
        cont += 1
        averageValueSelect = averageValueSelect + featureValue[fieldEval]
        listaCampoEvaluarFiltro.append(-featureValue[fieldEval])
    else:
        listaCampoEvaluarFiltro.append(0)
    contAux+=1
print('\n')
Separador(23)
print('Ejecutando estadísticas')
Separador(23)
print('# Entidades sin filtro:', entityCount)
print('# Entidades con filtro:',cont)
print('Promedio sin filtro:',averageValue / entityCount)
print('Promedio con filtro >'+str(fieldValue)+':'+str(averageValueSelect / cont))
print('Generando gráfica de barras para datos no filtrados....')
plt.figure(figsize=(8, 8), dpi=100)
plt.bar(listaCampoEtiqueta, listaCampoEvaluar, color = 'darkGray', label='Sin filtro')
plt.bar(listaCampoEtiqueta, listaCampoEvaluarFiltro, color = 'red', label='Con filtro')
plt.title('Valores encontrados con y sin filtro')
plt.xlabel('Index')
plt.ylabel(fieldEval)
plt.legend(loc='best', shadow=False, fontsize=11)
plt.grid()
plt.show()

#Visualizar las propiedades de una capa seleccionada en el proyecto actual requiere una capa cargada y seleccionada en QGIS
'''
layer = qgis.utils.iface.activeLayer()
print(layer.id())
print(layer.featureCount())
'''

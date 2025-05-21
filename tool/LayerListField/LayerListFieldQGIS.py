# -*- coding: UTF-8 -*-
# Nombre: LayerListFieldQGIS.py
# Descripción: Consulta de metadatos, propiedades y atributos en capas vectoriales de proyectos geográficos
# Requerimiento: QGIS 3.22.1 con Python 3.9.5

# Librerías
import sys
from qgis.core import *
import qgis.utils
from qgis.core import QgsProject
import matplotlib
import matplotlib.pyplot as plt

# Función para creación de líneas de separación
def Separador(n=24): #Usando un valor por defecto de 24 guiones
    nc = '-'
    print(nc*n)

# Cabecera
Separador(92)
print('Consulta de metadatos, propiedades y atributos en capas vectoriales de proyectos geográficos')
Separador(92)
print( 'Compatible con: QGIS 3'
       '\nPython versión: ' + str(sys.version)+
       '\nPython rutas: ' + str(sys.path[0:5])+
       '\nmatplotlib versión: ' + str(matplotlib.__version__)+
       '\nEncuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/LayerListField'
       '\nCláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License'
       '\nCréditos: r.cfdtools@gmail.com\n')

# Mostrar la lista de capas disponibles
Separador(46)
print('Listado de capas disponibles en el mapa actual')
Separador(46)
featureList = [layer.name() for layer in QgsProject.instance().mapLayers().values()]
cont = 1
for i in featureList:
    print(' ',cont, i)
    cont += 1

# Mostrar la lista de atributos por cada capa disponible
# layer = iface.activeLayer()
for layer in QgsProject.instance().mapLayers().values():
    totalEntidades = layer.featureCount()
    #Tipo de geometría
    geomTipo = ''
    if layer.wkbType() == QgsWkbTypes.Point:
        geomTipo = 'G' + str(layer.wkbType()) + ' Puntos'
    elif layer.wkbType() == QgsWkbTypes.LineString:
        geomTipo = 'G' + str(layer.wkbType()) + ' Lineas'
    elif layer.wkbType() == QgsWkbTypes.Polygon:
        geomTipo = 'G' + str(layer.wkbType()) + ' Polígonos'
    elif layer.wkbType() == QgsWkbTypes.MultiPolygon:
        geomTipo = 'G' + str(layer.wkbType()) + ' Multi-polígonos'
    else:
        geomTipo = str(layer.wkbType())
    layerTitle = 'Campos en '+ layer.name() + ' (' + geomTipo + ' ' + str(totalEntidades) + ')'
    Separador(len(layerTitle))
    print(layerTitle)
    Separador(len(layerTitle))
    cont = 1
    for field in layer.fields():
        print('  ' + str(cont) + ', '+ field.name() + ', ' + field.typeName())
        cont += 1

# Mostrar valores encontrados
absolutePath = r'D:/R.GISPython/LayerListField/Datos/' # Ruta absoluta de datos de entrada. Usar r'./Datos' para rutas relativas.
gisFileInput = absolutePath+'Precipitacion.shp'
campoRotulo = 'ESTACIONID'
campoEvaluar = 'TotalAnno'
campoFiltro = 2000
#layerInput = iface.addVectorLayer(gisFileInput,'','ogr') #Cargar en mapa QGIS
layerInput = QgsVectorLayer(gisFileInput,'','ogr') # Sin cargar en mapa QGIS
fCount = layerInput.featureCount()
print('\nCapa a evaluar:', gisFileInput)
print('Campo para rotulación:', campoRotulo)
print('Campo a evaluar:', campoEvaluar)
print('Mostrar valores >= a:', campoFiltro,'\n')
listacampoRotulo, listacampoEvaluar = [], []
Separador(38)
print('Lista de valores encontrados >=',campoFiltro)
Separador(38)
print('  ' + campoRotulo + ', ' + campoEvaluar)
cont = 0
for i in range(0, fCount):
    feature = layerInput.getFeature(i)
    if feature[campoEvaluar] >= campoFiltro:
        #listacampoRotulo.append(int(feature[campoRotulo]))
        listacampoRotulo.append(cont)
        listacampoEvaluar.append(feature[campoEvaluar])
        print('  ' + str(feature[campoRotulo]) + ', ' + str(feature[campoEvaluar]))
        cont += 1
print('  (' + str(cont) + ' registros)')

# Graficar datos
Separador(14)
print('Graficar datos')
Separador(14)
plt.bar(listacampoRotulo, listacampoEvaluar, color = 'darkGray')
plt.style.use('fast') # https://matplotlib.org/3.1.1/gallery/style_sheets/style_sheets_reference.html
plt.title('Valores encontrados')
plt.xlabel(campoRotulo)
plt.ylabel(campoEvaluar)
plt.show()
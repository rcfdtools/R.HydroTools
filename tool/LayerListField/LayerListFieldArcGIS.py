# -*- coding: UTF-8 -*-
# Nombre: LayerListFieldArcGIS.py
# Descripción: Consulta de metadatos, propiedades y atributos en capas vectoriales de proyectos geográficos
# Requerimiento: PyCharm 2021.3+, Python 2.7.5 (ArcGIS 10.2.2)

# Librerías
from __future__ import unicode_literals  # Importación de unicodes para manejo de eñes y tildes.
import sys
import arcpy
import matplotlib
import matplotlib.pyplot as plt

# Validación unicode Python 2
pythonVersion = sys.version
print('Python '+str(pythonVersion[0])+' en ejecución...')
if int(pythonVersion[0]) == 2:
    reload(sys)
    sys.setdefaultencoding('utf8')  # Definición de unicode UTF-8

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
# Definición del espacio de trabajo. Usar r para evitar salto de línea en directorios que empiezan por la letra n.
absolutePath = r'D:/R.GISPython/LayerListField' # Usar r'.' para retornar a ruta relativa
arcpy.env.workspace = absolutePath+'/Datos'

# Cabecera
Separador(92)
print ('Consulta de metadatos, propiedades y atributos en capas vectoriales de proyectos geográficos')
Separador(92)
print ( 'Compatible con: ArcGIS for Desktop y ArcGIS Pro'
        '\nPython versión: ' + str(sys.version)+
        '\nPython rutas: ' + str(sys.path[0:5])+
        '\nmatplotlib versión: ' + str(matplotlib.__version__)+
        '\nEncuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/LayerListField'
        '\nCláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License'
        '\nCréditos: r.cfdtools@gmail.com'
        '\nLa opción 0 muestra las capas disponibles en el directorio de trabajo, sus atributos y tipos.'
        '\nPara una capa específica muestra los atributos y permite definir dos campos para su graficación.\n')

# Consultar la lista de capas disponibles
featureList = arcpy.ListFeatureClasses() # Lista de clases de entidad para el espacio de trabajo definido arcpy.env.workspace
Separador(28)
print('Listado de capas disponibles')
Separador(28)
print('Espacio de trabajo: '+arcpy.env.workspace)
cont = 1
for i in featureList:
    print('  ' + str(cont) + '  ' + i)
    cont += 1

# Mostrar la lista de campos disponibles en cada capa
try:
    numCapaEntrada = int(input('  >>> # capa a evaluar (0 -> Todas): '))
    if numCapaEntrada == 0:
        for i in featureList:
            CapaPropiedades(i)
    else:
        CapaPropiedades(featureList[numCapaEntrada-1])
        campoRotulo = input('  >>> Nombre del campo para rotulación (usar comillas): ')
        campoEvaluar = input('  >>> Nombre del campo a evaluar (usar comillas): ')
        graficoTipo = input('  >>> Tipo de gráfica (Bar, Pie) (usar comillas): ').lower()
        campoFiltro = input('  >>> Mostrar valores >= a: ')
        cursor = arcpy.SearchCursor(featureList[numCapaEntrada-1]) # Records in properties table
        listaCampoRotulo, listaCampoEvaluar, listaCampoEtiqueta = [], [], []
        tituloLista = 'Lista de valores encontrados >= ' + str(campoFiltro)
        Separador(len(tituloLista))
        print(tituloLista)
        Separador(len(tituloLista))
        print('Index, ' + campoRotulo + ', ' + campoEvaluar)
        # Propiedades encontradas para el campo a evaluar
        cont = 0
        for fila in cursor:
            if fila.getValue(campoEvaluar) >= int(campoFiltro):
                listaCampoRotulo.append(cont)
                listaCampoEtiqueta.append(fila.getValue(campoRotulo))
                listaCampoEvaluar.append(fila.getValue(campoEvaluar))
                print('  ' +  str(listaCampoRotulo[cont]) + ', ' + str(listaCampoEtiqueta[cont]) + ', ' + str(listaCampoEvaluar[cont]))
                cont += 1
        print('  (' + str(cont) + ' registros)')
        # Graficación de datos
        Separador(14)
        print('Graficar datos')
        Separador(14)
        if graficoTipo == 'bar':
            plt.bar(listaCampoRotulo, listaCampoEvaluar, color = 'darkGray')
        else:
            plt.pie(listaCampoEvaluar, labels=listaCampoRotulo)
        plt.title('Valores encontrados')
        plt.xlabel(campoRotulo)
        plt.ylabel(campoEvaluar)
        plt.show()

except NameError as e:
    print('  >>> Error: dato ingresado inválido...')
except ValueError as e:
    print('  >>> Error: error en código fuente o en datos...')
except SyntaxError as e:
    print('  >>> Error: debe ingresar un número de capa...')
except IndexError as e:
    print('  >>> Error: capa o dato  no existe...')
except RuntimeError as e:
    print('  >>> Error: atributo no existe...')

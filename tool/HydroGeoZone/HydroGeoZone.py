# -*- coding: UTF-8 -*-
# Nombre: HydroGeoZone.py
# Descripción: Zonificación hidrográfica de Colombia - Análisis de forma y densidad usando Python
# Requerimiento: PyCharm 2021.3+, ArcGIS 10.6+, ArcGIS Pro 2.9.0

# Librerías
import arcpy
from arcpy import env
import sys
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import date
import time

# Variables y datos de entrada
absolutePath = r'D:/R.GISPython/HydroGeoZone'  # Usar r'.' para retornar a ruta relativa
arcpy.env.workspace = absolutePath+'/Data/'
arcpy.env.overwriteOutput = True
dataPath = absolutePath+'/Data/'
outputPath = absolutePath+'/Output/'
outputPathGraph = absolutePath+'/Graph/'
urlGitHubFile = 'https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/'
hydroSubZoneLayerIn = dataPath+'Zonificacion_hidrografica_2013.shp'
drainageLayerIn = dataPath+'Drenaje_Sencillo.shp'
drainageLayer = outputPath+'DrenajeSencilloFiltro.shp'  # Capa drenajes filtro solo permanentes
hydroAreaLayer = outputPath+'AreaHidrografica.shp'
hydroZoneLayer = outputPath+'ZonaHidrografica.shp'
hydroSubZoneLayerProject = outputPath+'SubZonaHidrograficaProject.shp'
hydroSubZoneLayerCopy = outputPath+'SubZonaHidrografica.shp'
drainageLayerIntersect = outputPath+'DrenajeSencilloIntersect.shp'
statisticsTableDrainageDBF = outputPath+'DrenajeSencilloSubtipoEstadistica.dbf'
statisticsTableAHDBF = outputPath+'AreaHidrograficaEstadistica.dbf'
statisticsTableZHDBF = outputPath+'ZonaHidrograficaEstadistica.dbf'
statisticsTableSZHDBF = outputPath+'SubZonaHidrograficaEstadistica.dbf'
statisticsTableAHXLS = outputPath+'AreaHidrograficaEstadistica.xls'
statisticsTableZHXLS = outputPath+'ZonaHidrograficaEstadistica.xls'
statisticsTableSZHXLS = outputPath+'SubZonaHidrograficaEstadistica.xls'
fieldAHCode, fieldZHCode, fieldSZHCode = 'COD_AH', 'COD_ZH', 'COD_SZH'
fieldAHName, fieldZHName, fieldSZHName = 'NOM_AH', 'NOM_ZH', 'NOM_SZH'
drainageSubtype, drainageLen = 'ESTADO_DRE', 'SHAPE_Leng'
drainageSubtypePerm = 5101  # Código de drenajes subtipo permanente
outCoordinateSystem = "PROJCS['MAGNA-SIRGAS / Origen-Nacional',GEOGCS['GCS_MAGNA',DATUM['D_MAGNA',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',5000000.0],PARAMETER['False_Northing',2000000.0],PARAMETER['Central_Meridian',-73.0],PARAMETER['Scale_Factor',0.9992],PARAMETER['Latitude_Of_Origin',4.0],UNIT['Meter',1.0]] # GEOGCS['GCS_MAGNA',DATUM['D_MAGNA',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
evalValueKc = [[1.25, 'Casi redonda a oval redonda'], [1.5, 'Oval-redonda a oval oblonga'], [999999, 'Oval-oblonga a rectangular-oblonga']]  # Rangos coeficiente de compacidad Kc según ANLA - Colombia en modelo de datos GDB Nacional
evalAreaSZH = [[300, 0, 0], [700, 0, 0], [900, 0, 0], [1100, 0, 0], [1300, 0, 0], [1500, 0, 0], [2000, 0, 0], [2500, 0, 0], [3500, 0, 0], [5000, 0, 0], [10000, 0, 0], [20000, 0, 0], [999999, 0, 0]]  # Valores de corte para evaluar número de subzonas, posición 0 corresponde al valor de corte, posición 1 para conteo y posición 2 para acumulado.
decimalPos = 2  # Posiciones decimales para impresión de tablas en formato Markdown
consKc = 0.28209479179826
intersectActive = False  # Volver a realizar la intersección espacial y calcular las longitudes de los drenajes intersecados.
statisticActive = False  # Volver a generar estadísticos en DBF y convertir a Excel.
onlyPerDrainActive = False  # Analizar solo para drenajes permanentes.

# Log file creation
currentDate = date.today()
currentDateTxt = str(currentDate.year).zfill(4)+str(currentDate.month).zfill(2)+str(currentDate.day).zfill(2)
if onlyPerDrainActive:
    fileNameAux = 'DrainPer'
    titleAuxTxt = 'Solo drenajes subtipo permanente'
else:
    fileNameAux = 'DrainAll'
    titleAuxTxt = 'Todos los subtipos de drenaje'
fileLogName = absolutePath+'/HydroGeoZone'+fileNameAux+currentDateTxt+'.md'
fileLog = open(fileLogName, 'w+')  # w+ para crear el archivo si no existe
timeStart = time.time()

# Función para crear separador de filas cabecera en formato Markdown
def TableHeadMarkdown(n=2):
    lineSep = '|---'
    PrintLog(lineSep * n + '|', True)

# Función de impresión en pantalla y log de resultados
def PrintLog(txtPrint, onScreen=True):
    if onScreen: print(txtPrint)
    fileLog.write(txtPrint + '\n')

# Función para consultar los campos de atributos disponibles
def CapaPropiedades(capa):
    cont = 1
    totalEntidades = arcpy.GetCount_management(capa)
    descGeometria = arcpy.Describe(capa)
    tipoGeometria = descGeometria.shapeType
    PrintLog('### Campos en ' + capa + ' (' + tipoGeometria + 's ' + str(totalEntidades) + ')\n', True)
    PrintLog('| # | Campo | Tipo |', True)
    TableHeadMarkdown(3)
    campos = arcpy.ListFields(capa)
    for campo in campos:
        PrintLog('| ' + str(cont) + ' | ' + campo.name + ' | ' + campo.type + ' |', True)  # Print field properties
        cont += 1

# Cabecera
PrintLog('## Zonificación hidrográfica de Colombia - Análisis de forma y densidad usando Python - ' + titleAuxTxt, True)
PrintLog('\n![HydroGeoZone.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/HydroGeoZone.png)')
PrintLog('\n* Archivo de resultados: ' + fileLogName +
         '\n* Fecha y hora de inicio de ejecución: ' + str(datetime.now()) +
         '\n* Script compatible con: ArcGIS for Desktop 10.6+ y ArcGIS Pro'
         '\n* Python versión: ' + str(sys.version) +
         '\n* Python rutas: ' + str(sys.path[0:5]) +
         '\n* matplotlib versión: ' + str(matplotlib.__version__) +
         '\n* Encuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone'
         '\n* Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License'
         '\n* Créditos: r.cfdtools@gmail.com\n', True)
PrintLog('```\nSistema de coordenadas: ' + outCoordinateSystem + '\n```', False)  # Mostrar como código en Markdown
print('\nAntes de iniciar cierre las aplicaciones de ArcGIS for Desktop...')

PrintLog('\n### Parámetros y datos de entrada ([/Data](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone/Data))\n'
         '\n* Ruta absoluta: ' + absolutePath +
         '\n* Espacio de trabajo ArcPy: ' + arcpy.env.workspace +
         '\n* Capa de entrada SZH - Subzonas hidrográficas: ' + hydroSubZoneLayerIn +
         '\n* Capa de entrada Drenajes: ' + drainageLayerIn +
         '\n* Intersección SZH & Drenajes: ' + str(intersectActive) +
         '\n* Recálculo de estadísticos: ' + str(statisticActive) +
         '\n* Analizar solo drenajes permanentes: ' + str(onlyPerDrainActive))

PrintLog('\n## Propiedades y entidades encontradas para las capas de entrada\n')
CapaPropiedades(hydroSubZoneLayerIn)
PrintLog('\n', True)
CapaPropiedades(drainageLayerIn)
PrintLog('\n### Evaluación de drenajes por subtipo\n', True)
PrintLog('> (0 - Sin asignación, 5101 - Permanente, 5102 - Intermitente)\n', True)
arcpy.Statistics_analysis(drainageLayerIn, statisticsTableDrainageDBF, [[drainageLen, 'SUM']], [drainageSubtype])
cursor = arcpy.SearchCursor(statisticsTableDrainageDBF)
PrintLog('| Código | # Drenajes |', True)
TableHeadMarkdown(2)
for fila in cursor:
    PrintLog('| ' + str(fila.getValue(drainageSubtype)) + ' | ' + str(fila.getValue('FREQUENCY')) + ' |', True)
if onlyPerDrainActive:
    print('Filtrado de drenajes permanentes activado.'
          '\nFiltrando drenajes solo permanentes en ' + drainageLayer +
          '\nEste proceso tardará varios minutos...')
    whereFilter = '"'+drainageSubtype+'"='+str(drainageSubtypePerm)
    arcpy.Select_analysis(drainageLayerIn, drainageLayer, whereFilter)
else:
    print('Filtrado de drenajes solo permanentes desactivado...')
    drainageLayer = drainageLayerIn
print('\n')

# Procesos y cálculos
print('### Reproyección de subzonas')
print('Reproyectando SZH a '+hydroSubZoneLayerProject+'...')
print('Sistema de coordenadas: '+outCoordinateSystem)
arcpy.Project_management(hydroSubZoneLayerIn, hydroSubZoneLayerProject, outCoordinateSystem)
print('\n')

print('### Disolución de subzona, zona y área hidrográfica')
print('La capa de subzonas hidrográficas contiene polígonos con el mismo código y en entidades separadas por lo que se requiere su conversión a multiparte.')
print('Disolviendo a multiparte SZH - subzonas hidrográfica '+hydroSubZoneLayerCopy+'...')
arcpy.Dissolve_management(hydroSubZoneLayerProject, hydroSubZoneLayerCopy, fieldSZHCode, '', 'MULTI_PART', '')
print('Incorporando atributos a capa disuelta SZH - subzona hidrográfica ' + hydroSubZoneLayerCopy+'...')
arcpy.JoinField_management(hydroSubZoneLayerCopy, 'COD_SZH', hydroSubZoneLayerProject, 'COD_SZH')  # Siempre se ejecuta antes de las demás disoluciones
print('Disolviendo a multiparte AH - áreas hidrográficas '+hydroAreaLayer+'...')
arcpy.Dissolve_management(hydroSubZoneLayerCopy, hydroAreaLayer, fieldAHCode, '', 'MULTI_PART', '')
print('Disolviendo a multiparte ZH - zonas hidrográficas '+hydroZoneLayer+'...')
arcpy.Dissolve_management(hydroSubZoneLayerCopy, hydroZoneLayer, fieldZHCode, '', 'MULTI_PART', '')
print('\n')

print('### Inclusión de campos para cálculo de áreas, perímetros, longitudes, forma y densidad')
print('Agregando campo area (Area) en km²')
print('Agregando campo perimetro (Perm) en km')
print('\tAH - áreas hidrográficas...')
arcpy.AddField_management(hydroAreaLayer, 'Area', 'DOUBLE')
arcpy.AddField_management(hydroAreaLayer, 'Perm', 'DOUBLE')
print('\tZH - zonas hidrográficas...')
arcpy.AddField_management(hydroZoneLayer, 'Area', 'DOUBLE')
arcpy.AddField_management(hydroZoneLayer, 'Perm', 'DOUBLE')
print('\tSZH - subzonas hidrográficas...')
arcpy.AddField_management(hydroSubZoneLayerCopy, 'Area', 'DOUBLE')
arcpy.AddField_management(hydroSubZoneLayerCopy, 'Perm', 'DOUBLE')
print('Agregando Kc - Coeficiente de Compacidad')
print('Agregando KcTag - Coeficiente de Compacidad - Rótulo')
print('Agregando Dd - Densidad de Drenaje km/km²')
print('Agregando Dc - Densidad de corrientes 1/Km²')
print('\tAH - áreas hidrográficas...')
arcpy.AddField_management(hydroAreaLayer, 'Kc', 'DOUBLE')
arcpy.AddField_management(hydroAreaLayer, 'KcTag', 'TEXT')
arcpy.AddField_management(hydroAreaLayer, 'Dd', 'DOUBLE')
arcpy.AddField_management(hydroAreaLayer, 'Dc', 'DOUBLE')
print('\tZH - zonas hidrográficas...')
arcpy.AddField_management(hydroZoneLayer, 'Kc', 'DOUBLE')
arcpy.AddField_management(hydroZoneLayer, 'KcTag', 'TEXT')
arcpy.AddField_management(hydroZoneLayer, 'Dd', 'DOUBLE')
arcpy.AddField_management(hydroZoneLayer, 'Dc', 'DOUBLE')
print('\tSZH - subzonas hidrográficas...')
arcpy.AddField_management(hydroSubZoneLayerCopy, 'Kc', 'DOUBLE')
arcpy.AddField_management(hydroSubZoneLayerCopy, 'KcTag', 'TEXT')
arcpy.AddField_management(hydroSubZoneLayerCopy, 'Dd', 'DOUBLE')
arcpy.AddField_management(hydroSubZoneLayerCopy, 'Dc', 'DOUBLE')
print('\n')

print('### Cálculo de áreas y perímetros')
print('Compatible con ArcGIS for Desktop 10.6+ y ArcGIS Pro.')
print('Calculando area (Area) en km² y perimetro (Perm) en km')
print('\tAH - áreas hidrográficas...')
arcpy.CalculateGeometryAttributes_management(hydroAreaLayer, [['Area', 'AREA'], ['Perm', 'PERIMETER_LENGTH']], 'KILOMETERS', 'SQUARE_KILOMETERS')
print('\tZH - zonas hidrográficas...')
arcpy.CalculateGeometryAttributes_management(hydroZoneLayer, [['Area', 'AREA'], ['Perm', 'PERIMETER_LENGTH']], 'KILOMETERS', 'SQUARE_KILOMETERS')
print('\tSZH - subzonas hidrográficas...')
arcpy.CalculateGeometryAttributes_management(hydroSubZoneLayerCopy, [['Area', 'AREA'], ['Perm', 'PERIMETER_LENGTH']], 'KILOMETERS', 'SQUARE_KILOMETERS')
print('\n')

print('### Intersección de drenajes con subzonas hidrográficas y cálculo de longitud por segmento')
print('Tenga en cuenta que la definición de las subzonas hidrográficas se realizó a escala 1:500k y los drenajes a escala 1:100k, por lo que espacialmente pueden existir fragmentos de tramos de drenaje que cruzan entre zonas. Los cálculos de densidad y forma se realizan a partir de la intersección espacial fraccionada de drenajes dentro de cada área teniendo en cuenta la consideración anterior, por tal motivo, el número de tramos drenajes de la capa original `Drenaje_Sencillo.shp` puede ser diferente al número de tramos de la capa de intersección.')
if intersectActive:
    print('Intersecando drenajes con subzonas ' + drainageLayerIntersect+'...')
    print('Este proceso tardara varios minutos...')
    arcpy.Intersect_analysis([hydroSubZoneLayerCopy, drainageLayer], drainageLayerIntersect, 'ALL', '', 'LINE')
    print('Intersección completada...')
    print('Agregando campo longitud (LDre) en km a drenajes intersecados...')
    arcpy.AddField_management(drainageLayer, 'LDre', 'DOUBLE')
    print('Calculando longitud (LDre) en km para cada segmento de drenaje intersecado...')
    print('Este proceso tardara varios minutos...')
    arcpy.CalculateGeometryAttributes_management(drainageLayerIntersect, [['LDre', 'LENGTH']], 'KILOMETERS')
    print('Calculo de longitudes completado...')
else:
    print('Actualización de intersección de drenajes con subzonas desactivada...')
print('\n')

print('### Estadísticos de análisis')
if statisticActive:
    print('Generando estadísticos en DBF')
    print('\tAH - área hidrográfica ' + statisticsTableAHDBF)
    arcpy.Statistics_analysis(drainageLayerIntersect, statisticsTableAHDBF, [['LDre', 'SUM']], [fieldAHCode, fieldAHName])
    print('\tZH - zona hidrográfica ' + statisticsTableZHDBF)
    arcpy.Statistics_analysis(drainageLayerIntersect, statisticsTableZHDBF, [['LDre', 'SUM']], [fieldAHCode, fieldAHName, fieldZHCode, fieldZHName])
    print('\tSZH - subzona hidrográfica ' + statisticsTableSZHDBF)
    arcpy.Statistics_analysis(drainageLayerIntersect, statisticsTableSZHDBF, [['LDre', 'SUM']], [fieldAHCode, fieldAHName, fieldZHCode, fieldZHName, fieldSZHCode, fieldSZHName])
    print('\n')
else:
    print('Actualización de estadísticos detallados desactivada...\n')

print('Unión de capas geográficas y estadísticos')
print('Tenga en cuenta que en algunas subzonas hidrográficas pueden no existir drenajes restituidos.')
print('Uniendo capa con estadísticos ' + hydroAreaLayer)
print('\tAH - área hidrográfica ' + hydroAreaLayer)
arcpy.JoinField_management(hydroAreaLayer, 'COD_AH', statisticsTableAHDBF, 'COD_AH')
print('\tZH - zona hidrográfica ' + hydroZoneLayer)
arcpy.JoinField_management(hydroZoneLayer, 'COD_ZH', statisticsTableZHDBF, 'COD_ZH')
print('\tSZH - subzona hidrográfica ' + hydroSubZoneLayerCopy)
arcpy.JoinField_management(hydroSubZoneLayerCopy, 'COD_SZH', statisticsTableSZHDBF, 'COD_SZH')
print('\n')

PrintLog('\n## Distribución de áreas en km² de subzonas por área hidrográfica', True)
PrintLog('\n### Total nacional de SZH - subzonas hidrográficas por rango de área\n', True)
print('Imprimiendo en formato Markdown...')
PrintLog('| Rango km² | # Subzonas | Acumulado |', True)
TableHeadMarkdown(3)
cont = 0
for i in evalAreaSZH:
    cursor = arcpy.SearchCursor(hydroSubZoneLayerCopy)
    for fila in cursor:
        if fila.getValue('Area') <= i[0]: i[2] += 1
    if cont != 0:
        evalAreaSZH[cont][1] = evalAreaSZH[cont][2] - evalAreaSZH[cont-1][2]
        PrintLog('| ' + str(evalAreaSZH[cont - 1][0]) + '-' + str(evalAreaSZH[cont][0]) + ' | ' + str(i[1]) + ' | ' + str(i[2]) + ' |', True)
    else:
        evalAreaSZH[cont][1] = evalAreaSZH[cont][2]
        PrintLog('| 0-' + str(evalAreaSZH[cont][0]) + ' | ' + str(i[1]) + ' | ' + str(i[2]) + ' |', True)
    cont += 1
print('\n')

PrintLog('\n### Total SZH - subzonas hidrográficas por rango de área para cada AH - área hidrográfica\n', True)
print('Imprimiendo en formato Markdown...')
cursorZH = arcpy.SearchCursor(hydroAreaLayer)
for filaZH in cursorZH:
    for j in evalAreaSZH:  # Reinicializar acumuladores
        j[1] = 0
        j[2] = 0
    PrintLog('\n#### AH - Área hidrográfica ' + str(filaZH.getValue(fieldAHCode)) + ' - ' + str(filaZH.getValue(fieldAHName))+'\n', True)
    PrintLog('| Rango km² | # Subzonas | Acumulado |', True)
    TableHeadMarkdown(3)
    cont = 0
    for i in evalAreaSZH:
        cursorSZH = arcpy.SearchCursor(hydroSubZoneLayerCopy)
        for fila in cursorSZH:
            if fila.getValue('Area') <= i[0] and fila.getValue(fieldAHCode) == filaZH.getValue(fieldAHCode): i[2] += 1
        if cont != 0:
            evalAreaSZH[cont][1] = evalAreaSZH[cont][2] - evalAreaSZH[cont-1][2]
            PrintLog('| ' + str(evalAreaSZH[cont - 1][0]) + '-' + str(evalAreaSZH[cont][0]) + ' | ' + str(i[1]) + ' | ' + str(i[2]) + ' |', True)
        else:
            evalAreaSZH[cont][1] = evalAreaSZH[cont][2]
            PrintLog('| 0-' + str(evalAreaSZH[cont][0]) + ' | ' + str(i[1]) + ' | ' + str(i[2]) + ' |', True)
        cont += 1
    print('\n')

print('### Análisis de forma y densidad')
codeEvalKc = '''def getKcTag(Kc):
    for i in evalValueKc[:]:
        if Kc <= i[0]:
            return i[1]'''
print('Calculando Kc - Coeficiente de Compacidad, Dd - Densidad de Drenaje km/km² y Dc - Densidad de corrientes 1/Km²')
print('\tAH - áreas hidrográficas...')
arcpy.CalculateField_management(hydroAreaLayer, 'Kc', 'consKc*!Perm!/(!Area!**0.5)', 'Python')
arcpy.CalculateField_management(hydroAreaLayer, 'KcTag', 'getKcTag(float(!Kc!))', 'Python', codeEvalKc)
arcpy.CalculateField_management(hydroAreaLayer, 'Dd', '!SUM_LDre!/!Area!', 'Python')
arcpy.CalculateField_management(hydroAreaLayer, 'Dc', '!FREQUENCY!/!Area!', 'Python')
print('\tZH - zonas hidrográficas...')
arcpy.CalculateField_management(hydroZoneLayer, 'Kc', 'consKc*!Perm!/(!Area!**0.5)', 'Python')
arcpy.CalculateField_management(hydroZoneLayer, 'KcTag', 'getKcTag(float(!Kc!))', 'Python', codeEvalKc)
arcpy.CalculateField_management(hydroZoneLayer, 'Dd', '!SUM_LDre!/!Area!', 'Python')
arcpy.CalculateField_management(hydroZoneLayer, 'Dc', '!FREQUENCY!/!Area!', 'Python')
print('\tSZH - subzonas hidrográficas...')
arcpy.CalculateField_management(hydroSubZoneLayerCopy, 'Kc', 'consKc*!Perm!/(!Area!**0.5)', 'Python')
arcpy.CalculateField_management(hydroSubZoneLayerCopy, 'KcTag', 'getKcTag(float(!Kc!))', 'Python', codeEvalKc)
arcpy.CalculateField_management(hydroSubZoneLayerCopy, 'Dd', '!SUM_LDre!/!Area!', 'Python')
arcpy.CalculateField_management(hydroSubZoneLayerCopy, 'Dc', '!FREQUENCY!/!Area!', 'Python')
print('\n')

print('### Convirtiendo estadísticos y resultados a XLS')
if statisticActive:
    print('\tAH - área hidrográfica ' + statisticsTableAHXLS)
    arcpy.TableToExcel_conversion(hydroAreaLayer, statisticsTableAHXLS)
    print('\tZH - zona hidrográfica ' + statisticsTableZHXLS)
    arcpy.TableToExcel_conversion(hydroZoneLayer, statisticsTableZHXLS)
    print('\tSZH - subzona hidrográfica ' + statisticsTableSZHXLS)
    arcpy.TableToExcel_conversion(hydroSubZoneLayerCopy, statisticsTableSZHXLS)
else:
    print('Actualización de conversión a XLS desactivada...')
print('\n')

PrintLog('\n## Visualización de tablas resultados para análisis de forma y densidad', True)
PrintLog('\n### AH - área hidrográfica\n', True)
PrintLog(statisticsTableAHDBF, True)
PrintLog('\n| AH | Nombre AH | Área, km² | Perm, km | n Drenajes | Sum. LCi, km | Kc | Dd | Dc | Kc Tag |', True)
TableHeadMarkdown(10)
cursor = arcpy.SearchCursor(hydroAreaLayer)
for fila in cursor:
    PrintLog('| ' + str(fila.getValue(fieldAHCode)) + ' | ' + fila.getValue(fieldAHName) + ' | ' + str(round(fila.getValue('Area'), decimalPos)) + ' | ' + str(round(fila.getValue('Perm'), decimalPos)) + ' | ' + str(fila.getValue('FREQUENCY')) + ' | ' + str(round(fila.getValue('SUM_LDre'), decimalPos)) + ' | ' + str(round(fila.getValue('Kc'), decimalPos)) + ' | ' + str(round(fila.getValue('Dd'), decimalPos)) + ' | ' + str(round(fila.getValue('Dc'), decimalPos)) + ' | ' + fila.getValue('KcTag') + ' |', True)
PrintLog('\n### ZH - zona hidrográfica\n', True)
PrintLog(statisticsTableZHDBF, True)
PrintLog('\n| AH | Nombre AH | ZH | Nombre ZH | Área, km² | Perm, km | n Drenajes | Sum. LCi, km | Kc | Dd | Dc | Kc Tag |', True)
TableHeadMarkdown(12)
cursor = arcpy.SearchCursor(hydroZoneLayer)
for fila in cursor:
    PrintLog('| ' + str(fila.getValue(fieldAHCode)) + ' | ' + fila.getValue(fieldAHName) + ' | ' + str(fila.getValue(fieldZHCode)) + ' | ' + fila.getValue(fieldZHName) + ' | ' + str(round(fila.getValue('Area'), decimalPos)) + ' | ' + str(round(fila.getValue('Perm'), decimalPos)) + ' | ' + str(fila.getValue('FREQUENCY')) + ' | ' + str(round(fila.getValue('SUM_LDre'), decimalPos)) + ' | ' + str(round(fila.getValue('Kc'), decimalPos)) + ' | ' + str(round(fila.getValue('Dd'), decimalPos)) + ' | ' + str(round(fila.getValue('Dc'), decimalPos)) + ' | ' + fila.getValue('KcTag') + ' |', True)
PrintLog('\n### SZH - Subzona hidrográfica\n', True)
PrintLog(statisticsTableSZHDBF, True)
PrintLog('\n| AH | Nombre AH | ZH | Nombre ZH | SZH | Nombre SZH | Área, km² | Perm, km | n Drenajes | Sum. LCi, km | Kc | Dd | Dc | Kc Tag |', True)
TableHeadMarkdown(14)
cursor = arcpy.SearchCursor(hydroSubZoneLayerCopy)
for fila in cursor:
    PrintLog('| ' + str(fila.getValue(fieldAHCode)) + ' | ' + fila.getValue(fieldAHName) + ' | ' + str(fila.getValue(fieldZHCode)) + ' | ' + fila.getValue(fieldZHName) + ' | ' + str(fila.getValue(fieldSZHCode)) + ' | ' + fila.getValue(fieldSZHName) + ' | ' + str(round(fila.getValue('Area'), decimalPos)) + ' | ' + str(round(fila.getValue('Perm'), decimalPos)) + ' | ' + str(fila.getValue('FREQUENCY')) + ' | ' + str(round(fila.getValue('SUM_LDre'), decimalPos)) + ' | ' + str(round(fila.getValue('Kc'), decimalPos)) + ' | ' + str(round(fila.getValue('Dd'), decimalPos)) + ' | ' + str(round(fila.getValue('Dc'), decimalPos)) + ' | ' + fila.getValue('KcTag') + ' |', True)

PrintLog('\n### Graficas generales')
scatterVarX, scatterVarXLabel = 'Area', 'Área, km²'
scatterVarY = ['FREQUENCY', 'SUM_LDre', 'Kc', 'Dd', 'Dc']
scatterVarYLabel = ['# Drenajes', 'Sum. Long. Drenajes, km', 'Kc - Índice de Compacidad', 'Dd - Densidad de drenajes', 'Dc - Densidad de corrientes']
iLabel = 0
for iY in scatterVarY[:]:
    xPlotValues, yPlotValues = [], []
    PrintLog('\nGrafica ' + scatterVarXLabel + ' vs. ' + scatterVarYLabel[iLabel] + ' - ' + titleAuxTxt)
    PrintLog('\n![Graph' + str(iLabel) + '](' + urlGitHubFile + '/Graph/Plot' + scatterVarX + 'Vs' + iY + fileNameAux + '.png)')
    cursor = arcpy.SearchCursor(hydroSubZoneLayerCopy)
    for fila in cursor:
        xPlotValues.append(fila.getValue(scatterVarX))
        yPlotValues.append(fila.getValue(iY))
    plt.grid(color='0.95')
    plt.scatter(xPlotValues, yPlotValues, c='k', label=scatterVarYLabel[iLabel], s=12)
    plt.xlabel(scatterVarXLabel)
    plt.ylabel(scatterVarYLabel[iLabel])
    plt.legend(loc='lower right')
    plt.title(scatterVarX + ' vs. ' + scatterVarYLabel[iLabel] + ' - ' + titleAuxTxt)
    plt.savefig(outputPathGraph+'Plot'+scatterVarX+'Vs'+iY+fileNameAux+'.png')
    plt.show()
    iLabel += 1

PrintLog('\n### Archivos de resultados ([/Output](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone/Output) [/Graph](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone/Graph))\n'
         '\n* Capa AH - Área hidrográfica: ' + hydroAreaLayer +
         '\n* Capa ZH - Zona hidrográfica: ' + hydroZoneLayer +
         '\n* Capa SZH - Subzona hidrográfica: ' + hydroSubZoneLayerCopy +
         '\n* Capa Drenajes filtro permanentes: ' + drainageLayer +
         '\n* Capa intersección SZH & Drenajes: ' + drainageLayerIntersect +
         '\n* Tabla resultados AH - Área hidrográfica (dBase): ' + statisticsTableAHDBF +
         '\n* Tabla resultados ZH - Zona hidrográfica (dBase): ' + statisticsTableZHDBF +
         '\n* Tabla resultados SZH - Subzona hidrográfica (dBase): ' + statisticsTableSZHDBF +
         '\n* Tabla resultados AH - Área hidrográfica (Excel): ' + statisticsTableAHXLS +
         '\n* Tabla resultados ZH - Zona hidrográfica (Excel): ' + statisticsTableZHXLS +
         '\n* Tabla resultados SZH - Subzona hidrográfica (Excel): ' + statisticsTableSZHXLS +
         '\n* Tabla resultados Drenajes por subtipo: ' + statisticsTableDrainageDBF)

PrintLog('\n> Los mapas desplegados en [/Graph](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone/Map) han sido generados manualmente en ArcGIS a partir de los datos obtenidos utilizando los mapas de proyecto disponibles en [/Map](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone/Map).')

PrintLog('\nFecha y hora de terminación de ejecución: '+str(datetime.now()), True)
timeEnd = time.time()
PrintLog('\nProceso completado (dt = ' + str(round(timeEnd - timeStart, 1)) + ' sec o ' + str(round((timeEnd - timeStart)/60, 1)) + ' min)', True)
fileLog.close()

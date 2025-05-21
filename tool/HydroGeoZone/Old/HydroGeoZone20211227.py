# -*- coding: UTF-8 -*-

# Librerías
import arcpy
from arcpy import env
import sys
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import date

# Variables y datos de entrada
absolutePath = r'D:/R.GISPython/HydroGeoZone' # Usar r'.' para retornar a ruta relativa
arcpy.env.workspace = absolutePath+'/Data/'
arcpy.env.overwriteOutput = True
dataPath = absolutePath+'/Data/'
outputPath = absolutePath+'/Output/'
hydroSubZoneLayer = dataPath+'Zonificacion_hidrografica_2013.shp'
drainageLayerIn = dataPath+'Drenaje_Sencillo.shp'
drainageLayer = outputPath+'DrenajeSencilloFiltro.shp' # Capa drenajes filtro solo permanentes
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
drainageSubtypePerm = 5101
outCoordinateSystem = "PROJCS['MAGNA-SIRGAS / Origen-Nacional',GEOGCS['GCS_MAGNA',DATUM['D_MAGNA',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',5000000.0],PARAMETER['False_Northing',2000000.0],PARAMETER['Central_Meridian',-73.0],PARAMETER['Scale_Factor',0.9992],PARAMETER['Latitude_Of_Origin',4.0],UNIT['Meter',1.0]] # GEOGCS['GCS_MAGNA',DATUM['D_MAGNA',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
evalValueKc = [[1.25,'Casi redonda a oval redonda'], [1.5,'Oval-redonda a oval oblonga'], [999999,'Oval-oblonga a rectangular-oblonga']] # Rangos coeficiente de compacidad Kc según ANLA - Colombia en modelo de datos GDB Nacional
evalAreaSZH= [[300,0,0], [700,0,0], [900,0,0], [1100,0,0], [1300,0,0], [1500,0,0], [2000,0,0], [2500,0,0], [3500,0,0], [5000,0,0], [10000,0,0], [20000,0,0], [999999,0,0]] # Valores de corte para evaluar número de subzonas, posición 0 corresponde al valor de corte, posición 1 para conteo y posición 2 para acumulado.
decimalPos = 2 # Posiciones decimales para impresión de tablas en formato Markdown
consKc = 0.28209479179826
intersectActive = False # Volver a realizar la intersección espacial y calcular las longitudes de los drenajes intersecados.
statisticActive = False # Volver a generar estadísticos en DBF y convertir a Excel.
onlyPermanentDrainActive = False # Analizar solo para drenajes permanentes.

# Log file creation
currentDate = date.today()
currentDateTxt=str(currentDate.year)+str(currentDate.month)+str(currentDate.day)
fileLog = open(outputPath+'Report/HydroGeoZone'+currentDateTxt+'.md', 'w+') # w+ para crear el archivo si no existe

# Función para impresión de títulos con lineas
def TitleSeparator(titleText,titleType='Both'):
    # titleType: Top, Bottom, Both
    nc='-'
    nVal=len(titleText)
    if titleType == 'Both':
        print(nc*nVal)
        print(titleText)
        print(nc * nVal)
    elif  titleType == 'Top':
        print(nc*nVal)
        print(titleText)
    else:
        print(titleText)
        print(nc*nVal)

# Función para impresión de títulos en formato Markdown
def TitleMarkdown(titleText,titleLevel='###'): # ### Por defecto títulos nivel 3 o H3 en Html
    nVal=len(titleText)
    if titleType == 'Both':
        print(nc*nVal)
        print(titleText)
        print(nc * nVal)
    elif  titleType == 'Top':
        print(nc*nVal)
        print(titleText)
    else:
        print(titleText)
        print(nc*nVal)


# Función para consultar los campos de atributos disponibles
def CapaPropiedades(i):
    cont = 1
    totalEntidades = arcpy.GetCount_management(i)
    descGeometria = arcpy.Describe(i)
    tipoGeometria = descGeometria.shapeType
    tituloCapa = 'Campos en ' + i + ' (' + tipoGeometria + 's ' + str(totalEntidades) + ')'
    TitleSeparator(tituloCapa)
    print('  #, Campo, Tipo')
    campos = arcpy.ListFields(i)
    for campo in campos:
        print('  ' + str(cont) + ', ' + campo.name + ', ' + campo.type)  # Print field properties
        cont += 1

# Función de impresión en pantalla y log de resultados
def PrintLog(txtPrint, onScreen):
    if onScreen == True:
        print(txtPrint)
    fileLog.write(txtPrint + '\n')

# Cabecera
TitleSeparator('Zonificación hidrográfica de Colombia - Análisis de forma y densidad usando Python')
print ( 'Compatible con: ArcGIS for Desktop 10.6+ y ArcGIS Pro'
        '\nPython versión: ' + str(sys.version)+
        '\nPython rutas: ' + str(sys.path[0:5])+
        '\nmatplotlib versión: ' + str(matplotlib.__version__) +
        '\nEncuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone'
        '\nCláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License'
        '\nCréditos: r.cfdtools@gmail.com\n')
print('Fecha y hora de inicio de ejecución: '+str(datetime.now()))
print('Antes de iniciar cierre las aplicaciones de ArcGIS for Desktop...\n')

print('Propiedades y entidades encontradas para las capas de entrada:\n')
CapaPropiedades(hydroSubZoneLayer)
print('\n')
CapaPropiedades(drainageLayerIn)
print('Evaluando drenajes por subtipo...')
print('\t(0 - Sin asignación, 5101 - Permanente, 5102 - Intermitente)')
arcpy.Statistics_analysis(drainageLayerIn, statisticsTableDrainageDBF, [[drainageLen, 'SUM']], [drainageSubtype])
cursor = arcpy.SearchCursor(statisticsTableDrainageDBF)
for fila in cursor:
    print('\tCódigo ' + str(fila.getValue(drainageSubtype)) + ', ' + str(fila.getValue('FREQUENCY')) + ' drenajes')
if onlyPermanentDrainActive == True:
    print(  'Filtrado de drenajes permanentes activado.\n'
            'Filtrando drenajes solo permanentes en ' + drainageLayer +
            'Este proceso tardará varios minutos...')
    whereFilter = '"'+drainageSubtype+'"='+str(drainageSubtypePerm)
    arcpy.Select_analysis(drainageLayerIn, drainageLayer, whereFilter)
else:
    print('Filtrado de drenajes solo permanentes desactivado...')
    drainageLayer = drainageLayerIn
print('\n')

# Procesos y cálculos
TitleSeparator('Reproyección de subzonas','Both')
print('Reproyectando SZH a '+hydroSubZoneLayerProject+'...')
print('Sistema de coordenadas: '+outCoordinateSystem)
arcpy.Project_management(hydroSubZoneLayer, hydroSubZoneLayerProject, outCoordinateSystem)
print('\n')

TitleSeparator('Disolución de subzona, zona y área hidrográfica','Both')
print('La capa de subzonas hidrográficas contiene polígonos con el mismo código y en entidades separadas por lo que se requiere su conversión a multiparte.')
print('Disolviendo a multiparte SZH - subzonas hidrográfica '+hydroSubZoneLayerCopy+'...')
arcpy.Dissolve_management(hydroSubZoneLayerProject, hydroSubZoneLayerCopy, fieldSZHCode, '','MULTI_PART', '')
print('Incorporando atributos a capa disuelta SZH - subzona hidrográfica ' + hydroSubZoneLayerCopy+'...')
arcpy.JoinField_management(hydroSubZoneLayerCopy, 'COD_SZH', hydroSubZoneLayerProject, 'COD_SZH') # Siempre se ejecuta antes de las demás disoluciones
print('Disolviendo a multiparte AH - áreas hidrográficas '+hydroAreaLayer+'...')
arcpy.Dissolve_management(hydroSubZoneLayerCopy, hydroAreaLayer, fieldAHCode, '','MULTI_PART', '')
print('Disolviendo a multiparte ZH - zonas hidrográficas '+hydroZoneLayer+'...')
arcpy.Dissolve_management(hydroSubZoneLayerCopy, hydroZoneLayer, fieldZHCode, '','MULTI_PART', '')
print('\n')

TitleSeparator('Inclusión de campos para cálculo de áreas, perímetros, longitudes, forma y densidad','Both')
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

TitleSeparator('Cálculo de áreas y perímetros','Both')
print('Compatible con ArcGIS for Desktop 10.6+ y ArcGIS Pro.')
print('Calculando area (Area) en km² y perimetro (Perm) en km')
print('\tAH - áreas hidrográficas...')
arcpy.CalculateGeometryAttributes_management(hydroAreaLayer,[['Area','AREA'],['Perm','PERIMETER_LENGTH']],'KILOMETERS','SQUARE_KILOMETERS')
print('\tZH - zonas hidrográficas...')
arcpy.CalculateGeometryAttributes_management(hydroZoneLayer,[['Area','AREA'],['Perm','PERIMETER_LENGTH']],'KILOMETERS','SQUARE_KILOMETERS')
print('\tSZH - subzonas hidrográficas...')
arcpy.CalculateGeometryAttributes_management(hydroSubZoneLayerCopy,[['Area','AREA'],['Perm','PERIMETER_LENGTH']],'KILOMETERS','SQUARE_KILOMETERS')
print('\n')

TitleSeparator('Intersección de drenajes con subzonas hidrográficas y cálculo de longitud por segmento','Both')
print('Tenga en cuenta que la definición de las subzonas hidrográficas se realizó a escala 1:500k y los drenajes a escala 1:100k, por lo que espacialmente pueden existir fragmentos de tramos de drenaje que cruzan entre zonas. Los cálculos de densidad y forma se realizan a partir de la intersección espacial fraccionada de drenajes dentro de cada área teniendo en cuenta la consideración anterior.')
if intersectActive == True:
    print('Intersecando drenajes con subzonas ' + drainageLayerIntersect+'...')
    print('Este proceso tardara varios minutos...')
    arcpy.Intersect_analysis([hydroSubZoneLayerCopy,drainageLayer],drainageLayerIntersect,'ALL','','LINE')
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

TitleSeparator('Estadísticos de análisis','Both')
if statisticActive == True:
    print('Generando estadísticos en DBF')
    print('\tAH - área hidrográfica ' + statisticsTableAHDBF)
    arcpy.Statistics_analysis(drainageLayerIntersect, statisticsTableAHDBF, [['LDre','SUM']], [fieldAHCode, fieldAHName])
    print('\tZH - zona hidrográfica ' + statisticsTableZHDBF)
    arcpy.Statistics_analysis(drainageLayerIntersect, statisticsTableZHDBF, [['LDre','SUM']], [fieldAHCode, fieldAHName, fieldZHCode, fieldZHName])
    print('\tSZH - subzona hidrográfica ' + statisticsTableSZHDBF)
    arcpy.Statistics_analysis(drainageLayerIntersect, statisticsTableSZHDBF, [['LDre','SUM']], [fieldAHCode, fieldAHName, fieldZHCode, fieldZHName, fieldSZHCode, fieldSZHName])
    print('\n')
else:
    print('Actualización de estadísticos detallados desactivada...\n')

TitleSeparator('Unión de capas geográficas y estadísticos')
print('Tenga en cuenta que en algunas subzonas hidrográficas pueden no existir drenajes restituidos.')
print('Uniendo capa con estadísticos ' + hydroAreaLayer)
print('\tAH - área hidrográfica ' + hydroAreaLayer)
arcpy.JoinField_management(hydroAreaLayer, 'COD_AH', statisticsTableAHDBF, 'COD_AH')
print('\tZH - zona hidrográfica ' + hydroZoneLayer)
arcpy.JoinField_management(hydroZoneLayer, 'COD_ZH', statisticsTableZHDBF, 'COD_ZH')
print('\tSZH - subzona hidrográfica ' + hydroSubZoneLayerCopy)
arcpy.JoinField_management(hydroSubZoneLayerCopy, 'COD_SZH', statisticsTableSZHDBF, 'COD_SZH')
print('\n')

TitleSeparator('Total nacional de SZH - subzonas hidrográficas por rango de área')
print('Imprimiendo en formato Markdown...')
PrintLog('| Rango km² | # Subzonas | Acumulado |', True)
PrintLog('|---|---|---|', True)
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

TitleSeparator('SZH - subzonas hidrográficas por rango de área para cada AH - área hidrográfica')
print('Imprimiendo en formato Markdown...')
cursorZH = arcpy.SearchCursor(hydroAreaLayer)
for filaZH in cursorZH:
    for j in evalAreaSZH: # Reinicializar acumuladores
        j[1] = 0
        j[2] = 0
    print('AH - Área hidrográfica ' + str(filaZH.getValue(fieldAHCode)) + ' - ' + str(filaZH.getValue(fieldAHName)))
    print('| Rango km² | # Subzonas | Acumulado |')
    print('|---|---|---|')
    cont = 0
    for i in evalAreaSZH:
        cursorSZH = arcpy.SearchCursor(hydroSubZoneLayerCopy)
        for fila in cursorSZH:
            if fila.getValue('Area') <= i[0] and fila.getValue(fieldAHCode) == filaZH.getValue(fieldAHCode): i[2] += 1
        if cont != 0:
            evalAreaSZH[cont][1] = evalAreaSZH[cont][2] - evalAreaSZH[cont-1][2]
            print('| ' + str(evalAreaSZH[cont - 1][0]) + '-' + str(evalAreaSZH[cont][0]) + ' | ' + str(i[1]) + ' | ' + str(i[2]) + ' |')
        else:
            evalAreaSZH[cont][1] = evalAreaSZH[cont][2]
            print('| 0-' + str(evalAreaSZH[cont][0]) + ' | ' + str(i[1]) + ' | ' + str(i[2]) + ' |')
        cont += 1
    print('\n')

TitleSeparator('Análisis de forma y densidad', 'Both')
codeEvalKc='''def getKcTag(Kc):
    for i in evalValueKc[:]:
        if Kc <= i[0]:
            return i[1]'''
print('Calculando Kc - Coeficiente de Compacidad, Dd - Densidad de Drenaje km/km² y Dc - Densidad de corrientes 1/Km²')
print('\tAH - áreas hidrográficas...')
arcpy.CalculateField_management (hydroAreaLayer, 'Kc', 'consKc*!Perm!/(!Area!**0.5)', 'Python')
arcpy.CalculateField_management (hydroAreaLayer, 'KcTag', 'getKcTag(float(!Kc!))', 'Python', codeEvalKc)
arcpy.CalculateField_management (hydroAreaLayer, 'Dd', '!SUM_LDre!/!Area!', 'Python')
arcpy.CalculateField_management (hydroAreaLayer, 'Dc', '!FREQUENCY!/!Area!', 'Python')
print('\tZH - zonas hidrográficas...')
arcpy.CalculateField_management (hydroZoneLayer, 'Kc', 'consKc*!Perm!/(!Area!**0.5)', 'Python')
arcpy.CalculateField_management (hydroZoneLayer, 'KcTag', 'getKcTag(float(!Kc!))', 'Python', codeEvalKc)
arcpy.CalculateField_management (hydroZoneLayer, 'Dd', '!SUM_LDre!/!Area!', 'Python')
arcpy.CalculateField_management (hydroZoneLayer, 'Dc', '!FREQUENCY!/!Area!', 'Python')
print('\tSZH - subzonas hidrográficas...')
arcpy.CalculateField_management (hydroSubZoneLayerCopy, 'Kc', 'consKc*!Perm!/(!Area!**0.5)', 'Python')
arcpy.CalculateField_management (hydroSubZoneLayerCopy, 'KcTag', 'getKcTag(float(!Kc!))', 'Python', codeEvalKc)
arcpy.CalculateField_management (hydroSubZoneLayerCopy, 'Dd', '!SUM_LDre!/!Area!', 'Python')
arcpy.CalculateField_management (hydroSubZoneLayerCopy, 'Dc', '!FREQUENCY!/!Area!', 'Python')
print('\n')

TitleSeparator('Convirtiendo estadísticos y resultados a XLS', 'Both')
if statisticActive == True:
    print('\tAH - área hidrográfica ' + statisticsTableAHXLS)
    arcpy.TableToExcel_conversion(hydroAreaLayer,statisticsTableAHXLS)
    print('\tZH - zona hidrográfica ' + statisticsTableZHXLS)
    arcpy.TableToExcel_conversion(hydroZoneLayer,statisticsTableZHXLS)
    print('\tSZH - subzona hidrográfica ' + statisticsTableSZHXLS)
    arcpy.TableToExcel_conversion(hydroSubZoneLayerCopy,statisticsTableSZHXLS)
else:
    print('Actualización de conversión a XLS desactivada...')
print('\n')

TitleSeparator('Visualización de tablas resultados en formato Markdown', 'Both')
print('\nAH - área hidrográfica')
print(statisticsTableAHDBF)
print('| AH | Nombre AH | Área, km² | Perm, km | n Drenajes | Σ LCi, km | Kc | Dd | Dc | Kc Tag |')
print('|---|---|---|---|---|---|---|---|---|---|')
cursor = arcpy.SearchCursor(hydroAreaLayer)
for fila in cursor:
    print('| ' + str(fila.getValue(fieldAHCode)) + ' | ' + fila.getValue(fieldAHName) + ' | ' + str(round(fila.getValue('Area'),decimalPos)) + ' | ' + str(round(fila.getValue('Perm'),decimalPos)) + ' | ' + str(fila.getValue('FREQUENCY')) + ' | ' + str(round(fila.getValue('SUM_LDre'),decimalPos)) + ' | ' + str(round(fila.getValue('Kc'),decimalPos)) + ' | ' + str(round(fila.getValue('Dd'),decimalPos)) + ' | ' + str(round(fila.getValue('Dc'),decimalPos)) + ' | ' + fila.getValue('KcTag') + ' |')
print('\nZH - zona hidrográfica')
print(statisticsTableZHDBF)
print('| AH | Nombre AH | ZH | Nombre ZH | Área, km² | Perm, km | n Drenajes | Σ LCi, km | Kc | Dd | Dc | Kc Tag |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|')
cursor = arcpy.SearchCursor(hydroZoneLayer)
for fila in cursor:
    print('| ' + str(fila.getValue(fieldAHCode)) + ' | ' + fila.getValue(fieldAHName) + ' | ' + str(fila.getValue(fieldZHCode)) + ' | ' + fila.getValue(fieldZHName) + ' | ' + str(round(fila.getValue('Area'),decimalPos)) + ' | ' + str(round(fila.getValue('Perm'),decimalPos)) + ' | ' + str(fila.getValue('FREQUENCY')) + ' | ' + str(round(fila.getValue('SUM_LDre'),decimalPos)) + ' | ' + str(round(fila.getValue('Kc'),decimalPos)) + ' | ' + str(round(fila.getValue('Dd'),decimalPos)) + ' | ' + str(round(fila.getValue('Dc'),decimalPos)) + ' | ' + fila.getValue('KcTag') + ' |')
print('\nSZH - Subzona hidrográfica')
print(statisticsTableSZHDBF)
print('| AH | Nombre AH | ZH | Nombre ZH | SZH | Nombre SZH | Área, km² | Perm, km | n Drenajes | Σ LCi, km | Kc | Dd | Dc | Kc Tag |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
cursor = arcpy.SearchCursor(hydroSubZoneLayerCopy)
for fila in cursor:
    print('| ' + str(fila.getValue(fieldAHCode)) + ' | ' + fila.getValue(fieldAHName) + ' | ' + str(fila.getValue(fieldZHCode)) + ' | ' + fila.getValue(fieldZHName) + ' | ' + str(fila.getValue(fieldSZHCode)) + ' | ' + fila.getValue(fieldSZHName) + ' | ' + str(round(fila.getValue('Area'),decimalPos)) + ' | ' + str(round(fila.getValue('Perm'),decimalPos)) + ' | ' + str(fila.getValue('FREQUENCY')) + ' | ' + str(round(fila.getValue('SUM_LDre'),decimalPos)) + ' | ' + str(round(fila.getValue('Kc'),decimalPos)) + ' | ' + str(round(fila.getValue('Dd'),decimalPos)) + ' | ' + str(round(fila.getValue('Dc'),decimalPos)) + ' | ' + fila.getValue('KcTag') + ' |')

fileLog.close()
print('\nFecha y hora de terminación de ejecución: '+str(datetime.now()))
print('Proceso finalizado.')
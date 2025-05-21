# -*- coding: UTF-8 -*-
# Name: CNEStationStatistic.py
# Description: Catálogo nacional de estaciones hidroclimatológicas del IDEAM - Colombia, descarga y análisis.
# Requirements: PyCharm 2021.3+, Python 3.10.0 (instalación independiente)

# Libraries
import pandas as pd # Tested with 1.3.4 version.
# import numpy as np # Tested with 1.21.4 version. # Has to be installed with not import required.
# import xlrd # Tested with 2.0.1 version. # Has to be installed with not import required.
from datetime import datetime
from datetime import date
import requests
import matplotlib.pyplot as plt
import os.path
import CNEStationDictionary # Import CNEStationDictionary.py
import matplotlib as mpl

# General variables
urlFile = 'http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls'
fileName = 'CNE_IDEAM'
fileExtension = '.xls'
sampleRecord = 12 # Number of records to show in the sample
showRecordSample = False  # Print some sample records
showAllRecords = False  # Print all the records at the report tail
showGraphScreen = False  # Show graphs on the screen. This script always update ./Graph & ./PivotTable
thermalLevelCaldas = True  # True for Caldas classification, False for conventional classification range
graphTransparency = 1 # Save color for paper print versions, 1 for full color. Doesn't apply for pie charts
stationName = 'nombre'
latitudeName = 'latitud'
longitudeName = 'longitud'
elevationName = 'altitud'
categoryName = 'CATEGORIA'
technologyName = 'TECNOLOGIA'
stateActiveName = 'ESTADO'
installationDate = 'FECHA_INSTALACION'
geoStateName = 'DEPARTAMENTO'
geoOperativeAreaName = 'AREA_OPERATIVA'
geoHydroAreaName = 'AREA_HIDROGRAFICA'
geoHydroZoneName = 'ZONA_HIDROGRAFICA'
geoHydroSubZoneName = 'SUBZONA_HIDROGRAFICA'
thermalLevelRefConv = [[1000,'Cálido, 24°C+, <= 1000 meters'],
                       [2000,'Templado, 18°C+, <= 2000 meters'],
                       [3000,'Frío, 12°C+, <= 3000 meters'],
                       [4000,'Páramo, 0°C, <= 4000 meters'],
                       [99999,'Glacial, 0°C-, > 4000 meters']] # Elevation value in meters
thermalLevelRefCaldas = [[800,'Cálido, T>=24°C, <=800meter'],
                         [1800,'Templado, 24°C>T>18°C, <=1800meter'],
                         [2800,'Frío, 18°C>T>12°C, <=2800meter'],
                         [3700,'Muy Frío, 12°C>T>6°C, <=3700meter'],
                         [4700,'Extremadamente Frio, 6°C>T>0°C, <=4700meter'],
                         [99999,'Nival, T<0°C, >4700meter']] # Elevation value in meters
graphTitlePrefix='CNE IDEAM Colombia -  '
mySignature = 'By https://github.com/rcfdtools/R.GISPython' # Signature for print in graphs header
urlGraphPivotTable = 'https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic' # URL path for print in graphs

# General pandas and matplotlib settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 0)
mpl.rc('figure', max_open_warning = 0) # Don't show the python figure.max_open_warning

# Separation title line function
def SeparatorTitle(n=24): # Default using 24 - characters
    nc = '-'
    print(nc*n)

# Thermal level evaluation function
def thermalLevelF(elevation):
    for i in thermalLevelRef[:]:
        if elevation <= i[0]:
            return i[1]

# Downloading and reading the file
fileDownloadText = 'File downloaded and updated = No'
currentDate = date.today()
currentDateTxt=str(currentDate.year).zfill(4)+str(currentDate.month).zfill(2)+str(currentDate.day).zfill(2)
fileRequest = requests.get(urlFile)
fileSave = './Data/'+fileName+'_'+currentDateTxt+fileExtension
if fileRequest:
    if os.path.isfile(fileSave) == False:
        open(fileSave, 'wb').write(fileRequest.content)
        fileDownloadText = 'File downloaded and updated = Yes'
stationTable = pd.read_excel(fileSave)
pd.set_option('display.max_rows', stationTable.shape[0]+1) # Show all the records
pd.set_option('display.max_columns', None) # Show all the records

# Header and general file summary
shapeTable = stationTable.shape # Row and columns array size
SeparatorTitle(72)
print('Catálogo nacional de estaciones hidroclimatológicas del IDEAM - Colombia')
SeparatorTitle(72)
print(  '\nEjecutado en: '+str(datetime.now()),
        '\nData summary for '+fileSave,
        '\nUrl: '+urlFile,
        '\nStations file by: Instituto de Hidrología, Meteorología y Estudios Ambientales',
        '\nhttp://www.ideam.gov.co/web/atencion-y-participacion-ciudadana/condiciones-y-terminos-de-uso-de-la-informacion',
        '\nDataframe type: '+str(type(stationTable)),
        '\n'+fileDownloadText,
        '\nStations: '+ str(stationTable.shape[0])+'\nAttributes: '+ str(stationTable.shape[1]),
        '\nEncuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic'
        '\nCláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License'
        '\nCréditos: r.cfdtools@gmail.com\n')

# Sample records
if showRecordSample == True:
    SeparatorTitle(14)
    print('Sample records')
    SeparatorTitle(14)
    print('\nFirst '+str(sampleRecord)+' records: ')
    print(stationTable.head(sampleRecord)) # By default show 5 records
    print('Last '+str(sampleRecord)+' records: ')
    print(stationTable.tail(sampleRecord)) # By default show 5 records
    print('\n')

# Attributes summary
SeparatorTitle(27)
print('Attributes an types founded')
SeparatorTitle(27)
print(stationTable.columns)
print('\nTypes: ')
print(stationTable.dtypes) # With stationTable.columns you can get the attributes names in an array.
print('\nGeneral dataframe information: ')
print(stationTable.info())
print('\n')

# Basic dataframe statistics
SeparatorTitle(18)
print('General statistics')
SeparatorTitle(18)
print('\nBasic dataframe statistics: ')
print(stationTable.describe())
stationTable.describe().to_csv('./BasicTable/BasicDataframeStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/BasicDataframeStatistic'+currentDateTxt+'.csv')
print('\nCategory - Count: ')
print(stationTable[categoryName].value_counts())
stationTable[categoryName].value_counts().to_csv('./BasicTable/CategoryStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/CategoryStatistic'+currentDateTxt+'.csv')
print('\nCategory - Normalize percentage rate: ')
print(stationTable[categoryName].value_counts(normalize=True).round(4))
stationTable[categoryName].value_counts(normalize=True).to_csv('./BasicTable/CategoryStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/CategoryStatisticNormalize'+currentDateTxt+'.csv')
print('\nTechnology - Count: ')
print(stationTable[technologyName].value_counts())
stationTable[technologyName].value_counts().to_csv('./BasicTable/TechnologyStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/TechnologyStatistic'+currentDateTxt+'.csv')
print('\nTechnology - Normalize percentage rate: ')
print(stationTable[technologyName].value_counts(normalize=True).round(4))
stationTable[technologyName].value_counts(normalize=True).to_csv('./BasicTable/TechnologyStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/TechnologyStatisticNormalize'+currentDateTxt+'.csv')
print('\nStatus - Count: ')
print(stationTable[stateActiveName].value_counts())
stationTable[stateActiveName].value_counts().to_csv('./BasicTable/StatusStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/StatusStatistic'+currentDateTxt+'.csv')
print('\nStatus - Normalize percentage rate: ')
print(stationTable[stateActiveName].value_counts(normalize=True).round(4))
stationTable[stateActiveName].value_counts(normalize=True).to_csv('./BasicTable/StatusStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/StatusStatisticNormalize'+currentDateTxt+'.csv')
print('\nGeographical state location- Count: ')
print(stationTable[geoStateName].value_counts())
stationTable[geoStateName].value_counts().to_csv('./BasicTable/GeoStateStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoStateStatistic'+currentDateTxt+'.csv')
print('\nGeographical state location - Normalize percentage rate: ')
print(stationTable[geoStateName].value_counts(normalize=True).round(4))
stationTable[geoStateName].value_counts(normalize=True).to_csv('./BasicTable/GeoStateStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoStateStatisticNormalize'+currentDateTxt+'.csv')
print('\nGeographical operative area - Count: ')
print(stationTable[geoOperativeAreaName].value_counts())
stationTable[geoOperativeAreaName].value_counts().to_csv('./BasicTable/GeoOperativeAreaStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoOperativeAreaStatistic'+currentDateTxt+'.csv')
print('\nGeographical operative area - Normalize percentage rate: ')
print(stationTable[geoOperativeAreaName].value_counts(normalize=True).round(4))
stationTable[geoOperativeAreaName].value_counts(normalize=True).to_csv('./BasicTable/GeoOperativeAreaStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoOperativeAreaStatisticNormalize'+currentDateTxt+'.csv')
print('\nHydrographic area - Count: ')
print(stationTable[geoHydroAreaName].value_counts())
stationTable[geoHydroAreaName].value_counts().to_csv('./BasicTable/GeoHydroAreaStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoHydroAreaStatistic'+currentDateTxt+'.csv')
print('\nHydrographic area - Normalize percentage rate: ')
print(stationTable[geoHydroAreaName].value_counts(normalize=True).round(4))
stationTable[geoHydroAreaName].value_counts(normalize=True).to_csv('./BasicTable/GeoHydroAreaStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoHydroAreaStatisticNormalize'+currentDateTxt+'.csv')
print('\nHydrographic zone - Count: ')
print(stationTable[geoHydroZoneName].value_counts())
stationTable[geoHydroZoneName].value_counts().to_csv('./BasicTable/GeoHydroZoneStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoHydroZoneStatistic'+currentDateTxt+'.csv')
print('\nHydrographic zone - Normalize percentage rate: ')
print(stationTable[geoHydroZoneName].value_counts(normalize=True).round(4))
stationTable[geoHydroZoneName].value_counts(normalize=True).to_csv('./BasicTable/GeoHydroZoneStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoHydroZoneStatisticNormalize'+currentDateTxt+'.csv')
print('\nHydrographic subzone - Count: ')
print(stationTable[geoHydroSubZoneName].value_counts())
stationTable[geoHydroSubZoneName].value_counts().to_csv('./BasicTable/GeoHydroSubZoneStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoHydroSubZoneStatistic'+currentDateTxt+'.csv')
print('\nHydrographic subzone - Normalize percentage rate: ')
print(stationTable[geoHydroSubZoneName].value_counts(normalize=True).round(4))
stationTable[geoHydroSubZoneName].value_counts(normalize=True).to_csv('./BasicTable/GeoHydroSubZoneStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoHydroSubZoneStatisticNormalize'+currentDateTxt+'.csv')
print('\nInstallation year - Count: ')
stationTable.sort_values(installationDate, ascending=True, inplace=True) # Reorder and uptate the dataframe by installation date records
stationTableYearCount = pd.DatetimeIndex(stationTable[installationDate]).year.value_counts(sort=False).round(0)
print(pd.DatetimeIndex(stationTable[installationDate]).year.value_counts(sort=False).round(0))
pd.DatetimeIndex(stationTable[installationDate]).year.value_counts(sort=False).to_csv('./BasicTable/InstallationYearStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/InstallationYearStatistic'+currentDateTxt+'.csv')
print('\nInstallation year - Normalize percentage rate: ')
print(pd.DatetimeIndex(stationTable[installationDate]).year.value_counts(sort=False, normalize=True).round(6))
pd.DatetimeIndex(stationTable[installationDate]).year.value_counts(sort=False, normalize=True).to_csv('./BasicTable/InstallationYearStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/InstallationYearStatisticNormalize'+currentDateTxt+'.csv')
print('\n')

# Pivot tables
SeparatorTitle(23)
print('Pivot tables and graphs')
SeparatorTitle(23)
print('\n')
# Category
pivotTable=stationTable.pivot_table(index=categoryName, columns=stateActiveName, values=technologyName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='barh', xlabel='Category', ylabel='Stations', title=graphTitlePrefix+'Stations by Category - Date:  '+str(currentDate)+'\n'+mySignature, figsize=(16,10), alpha=graphTransparency, rot=0, stacked=True) # alpha for transparency
plt.savefig('./Graph/CategoryPivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/CategoryPivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/CategoryPivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/CategoryPivot'+currentDateTxt+'.csv')
print('\n')
# Technology
pivotTable = stationTable.pivot_table(index=technologyName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Technology', ylabel='Stations', title=graphTitlePrefix+'Stations by Technology - Date: '+str(currentDate)+'\n'+mySignature, figsize=(8,8), fontsize=11, alpha=graphTransparency, rot=0, stacked=True )
plt.savefig('./Graph/TechnologyPivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/TechnologyPivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.plot(kind='pie', title=graphTitlePrefix+'Stations by Technology - Date: '+str(currentDate)+'\n'+mySignature, figsize=(24,8), startangle=30, subplots=True, autopct='%1.1f%%', fontsize=12, legend=False)
plt.savefig('./Graph/TechnologyPivotPie'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/TechnologyPivotPie'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/TechnologyPivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/TechnologyPivot'+currentDateTxt+'.csv')
print('\n')
# Geographical state
pivotTable=stationTable.pivot_table(index=geoStateName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Geographical state', ylabel='Stations', title=graphTitlePrefix+'Stations by Geographical State - Date: '+str(currentDate)+'\n'+mySignature, figsize=(14,18), alpha=graphTransparency, rot=-90, stacked=True)
plt.savefig('./Graph/GeoStatePivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/GeoStatePivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/GeoStatePivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/GeoStatePivot'+currentDateTxt+'.csv')
print('\n')
# Geographical operative area
pivotTable=stationTable.pivot_table(index=geoOperativeAreaName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Geographical operative area', ylabel='Stations', title=graphTitlePrefix+'Stations by Geographical Operative Area - Date: '+str(currentDate)+'\n'+mySignature, figsize=(10,16), alpha=graphTransparency, rot=-90, stacked=True)
plt.savefig('./Graph/GeoOperativeAreaPivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/GeoOperativeAreaPivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/GeoOperativeAreaPivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/GeoOperativeAreaPivot'+currentDateTxt+'.csv')
print('\n')
# Geographical hydrological area
pivotTable=stationTable.pivot_table(index=geoHydroAreaName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Geographical hydrological area', ylabel='Stations', title=graphTitlePrefix+'Stations by Geographical Hydrological Area - Date: '+str(currentDate)+'\n'+mySignature, figsize=(12,10), alpha=graphTransparency, rot=0, stacked=True, subplots=True, fontsize=11, grid=False, legend=False)
plt.savefig('./Graph/GeoHydroAreaPivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/GeoHydroAreaPivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/GeoHydroAreaPivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/GeoHydroAreaPivot'+currentDateTxt+'.csv')
print('\n')
# Geographical hydrological zone
pivotTable=stationTable.pivot_table(index=geoHydroZoneName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Geographical hydrological zone', ylabel='Stations', title=graphTitlePrefix+'Stations by Geographical Hydrological Zone - Date: '+str(currentDate)+'\n'+mySignature, figsize=(12,12), alpha=graphTransparency, rot=-90, stacked=True, fontsize=10)
plt.savefig('./Graph/GeoHydroZonePivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/GeoHydroZonePivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/GeoHydroZonePivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/GeoHydroZonePivot'+currentDateTxt+'.csv')
print('\n')
# Geographical hydrological subzone
pivotTable=stationTable.pivot_table(index=geoHydroSubZoneName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Geographical hydrological subzone', ylabel='Stations', title=graphTitlePrefix+'Stations by Geographical Hydrological Subzone - Date: '+str(currentDate)+'\n'+mySignature, figsize=(44,20), alpha=graphTransparency, rot=-90, stacked=True)
plt.savefig('./Graph/GeoHydroSubzonePivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/GeoHydroSubzonePivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/GeoHydroSubzonePivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/GeoHydroSubzonePivot'+currentDateTxt+'.csv')
print('\n')
# Installed stations by year
pivotTable = stationTable.pivot_table(index=pd.DatetimeIndex(stationTable[installationDate]).year, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Year', ylabel='Stations', title=graphTitlePrefix+'Installed Stations by year - Date: '+str(currentDate)+'\n'+mySignature, figsize=(22,12), alpha=graphTransparency, rot=-90, stacked=True)
plt.savefig('./Graph/InstallationYearPivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/InstallationYearPivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/InstallationYearPivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/InstallationYearPivot'+currentDateTxt+'.csv')
print('\n')

# Geospatial array
geoArray = stationTable[[latitudeName,longitudeName,elevationName]]
SeparatorTitle(39)
print('Geospatial array sample with '+str(sampleRecord)+' records')
SeparatorTitle(39)
print(geoArray.head(sampleRecord))
print('Dataframe type: '+str(type(geoArray))+'\n')

# Thermal level evaluation
if thermalLevelCaldas == True:
    thermalLevelRef = thermalLevelRefCaldas
    thermalLevelRefTitle = "Caldas classification"
    SeparatorTitleVal = 48
else:
    thermalLevelRef = thermalLevelRefConv
    thermalLevelRefTitle = "Conventional classification"
    SeparatorTitleVal = 54
SeparatorTitle(SeparatorTitleVal)
print('Thermal level evaluation - '+thermalLevelRefTitle)
SeparatorTitle(SeparatorTitleVal)
print('\nThermal level reference array:')
print(pd.DataFrame(thermalLevelRef,columns=['Elevation ref value','Thermic level']))
print('\n')
thermalLevelArray = []
for i in geoArray[elevationName]:
    thermalLevelArray.append(thermalLevelF(i))
stationTable['ThermalLevelValue']=thermalLevelArray
print('Geospatial array sample with '+str(sampleRecord)+' records:')
geoArray=stationTable[[geoStateName, stationName,latitudeName,longitudeName,elevationName,'ThermalLevelValue']]
print(geoArray.head(sampleRecord))
print('\nThermal level statistics:')
print('Count:')
print(geoArray['ThermalLevelValue'].value_counts())
print('\nNormalize percentage rate:')
print(geoArray['ThermalLevelValue'].value_counts(normalize=True).round(4))
print('\n')
pivotTable = stationTable.pivot_table(index='ThermalLevelValue', columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Thermal level', ylabel='Stations', title=graphTitlePrefix+'Stations by Thermal Level - Date: '+str(currentDate)+'\n'+mySignature, figsize=(12,12), fontsize=11, rot=10, stacked=True, alpha=graphTransparency)
plt.savefig('./Graph/ThermalLevelPivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/ThermalLevelPivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.plot(kind='pie', title=graphTitlePrefix+'Stations by Thermal Level - Date: '+str(currentDate)+'\n'+mySignature, figsize=(36,8), startangle=60, subplots=True, autopct='%1.1f%%', fontsize=12, legend=False)
plt.savefig('./Graph/ThermalLevelPivotPie'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/ThermalLevelPivotPie'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/ThermalLevelPivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/ThermalLevelPivot'+currentDateTxt+'.csv')
print('\n')

# General scatter plot map stations
SeparatorTitle(24)
print('General map plot station')
SeparatorTitle(24)
pivotTable=geoArray.plot.scatter(x=longitudeName, y=latitudeName, c=elevationName, colormap='viridis', colorbar=True, title=graphTitlePrefix+'Stations scatter plot map with altitude - Date: '+str(currentDate)+'\n'+mySignature, figsize=(10,11), grid=True, alpha=graphTransparency)
if showGraphScreen == True: plt.show()
plt.savefig('./Graph/StationScatterPlotMap'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/StationScatterPlotMap'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
geoArray.to_csv('./PivotTable/StationScatterPlotMap'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/StationScatterPlotMap'+currentDateTxt+'.csv')
# Geo State scatter plot map stations
geoStateList = stationTable[geoStateName].unique()
for i in geoStateList:
    #print(i)
    geoArrayState = geoArray[geoStateName].str.contains(i)
    #print(geoArray[geoArrayState])
    pivotTable=geoArray[geoArrayState].plot.scatter(x=longitudeName, y=latitudeName, c=elevationName, colormap='viridis', colorbar=True, title=graphTitlePrefix+'Stations scatter plot map with altitude - Date: '+str(currentDate)+'\n'+mySignature+'\n'+i, figsize=(10,11), grid=True, alpha=graphTransparency)
    if showGraphScreen == True: plt.show()
    plt.savefig('./Graph/PlotMap/StationScatterPlotMap' + i + currentDateTxt + '.png')
    print('Graph >> ' + urlGraphPivotTable + '/Graph/PlotMap/StationScatterPlotMap' + i + currentDateTxt + '.png')

# Show all data
if showAllRecords == True:
    SeparatorTitle(41)
    print('Stations in '+fileSave)
    SeparatorTitle(41)
    print('Index: ' + str(stationTable.index))
    pd.set_option('display.max_rows',stationTable.shape[0]+1)
    print(geoArray[[stationName,latitudeName,longitudeName]])
print('\n')

# General definitions
SeparatorTitle(8)
print('Appendix')
SeparatorTitle(8)
print('\nSource: IDEAM Colombia - Clasificación de los climas\nhttp://atlas.ideam.gov.co/basefiles/clima-text.pdf')
print('\n[Station categories]\n')
for i in CNEStationDictionary.stationCategoryDictEs:
    print(i[0]+': '+i[1]+'\n')
print('\n[Station status]\n')
for i in CNEStationDictionary.stationStatusDictEs:
    print(i[0]+': '+i[1]+'\n')
print('\n[Station technologies]\n')
for i in CNEStationDictionary.stationTechnologyDictEs:
    print(i[0]+': '+i[1]+'\n')


import pandas as pd # Tested with 1.3.4 version.
import numpy as np # Tested with 1.21.4 version.
import xlrd # Tested with 2.0.1 version.

# General vars
urlFile=r'http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls'
fileName='CNE_IDEAM.xls'
sampleRecord=12 # Number of records to show in the sample
showRecordSample=True # Print all the records
showAllRecords=False # Print all the records
latitudeName='latitud'
longitudeName='longitud'
elevationName='altitud'
thermalLevel=[1000,2000,3000,4000,9999] # Elevation value in meters
thermalLevelTag=['Cálido, 24°C+, <= 1000 meters','Templado, 18°C+, <= 2000 meters','Frío, 12°C+, <= 3000 meters','Páramo, 0°C, <= 4000 meters','Nieves,0°C-, > 4000 meters'] # Elevation value in meters
thermalLevelRef=np.array([[1000,'Cálido, 24°C+, <= 1000 meters'],[2000,'Templado, 18°C+, <= 2000 meters'],[3000,'Frío, 12°C+, <= 3000 meters'],[4000,'Páramo, 0°C, <= 4000 meters'],[99999,'Nieves,0°C-, > 4000 meters']])

# Separation title lines function
def Separador(n=24): # Usando un valor por defecto de 24 guiones
	nc = '-'
	print(nc*n)

# Thermal level evaluation function
def thermalLevelF(elevation):
    for i in thermalLevel:
        if elevation<=i:
            return i

# Reading the CNE_IDEAM.xls file
stationTable = pd.read_excel('./Data/'+fileName)

# Resumen
Separador(33)
print('Resumen de datos en '+fileName)
Separador(33)
print('Url: '+urlFile)
print('Dataframe type: '+str(type(stationTable)))
shapeTable=stationTable.shape # Row and columns array size
print('Stations: '+ str(stationTable.shape[0])+'\nAttributes : '+ str(stationTable.shape[1])+'\n')

if showRecordSample == True:
    Separador(14)
    print('Sample records')
    Separador(14)
    print('First '+str(sampleRecord)+' records:')
    print(stationTable.head(sampleRecord)) # By default show 5 records
    print('Last '+str(sampleRecord)+' records:')
    print(stationTable.tail(sampleRecord)) # By default show 5 records
    print('\n')
Separador(25)
print('Attributes an types founded')
Separador(25)
print(stationTable.columns)
print('\nTypes:')
print(stationTable.dtypes) # With stationTable.columns you can get the attributes names in an array.
print('\n')
Separador(37)
print('General information of the dataframe')
Separador(37)
print(stationTable.info())
print('\n')
Separador(26)
print('Basic dataframe statistics')
Separador(26)
print(stationTable.describe())
geoArray=stationTable[[latitudeName,longitudeName,elevationName]]
print('\n')
Separador(39)
print('Geospatial array sample with '+str(sampleRecord)+' records')
Separador(39)
print(geoArray.head(sampleRecord))
print('Dataframe type: '+str(type(geoArray))+'\n')
Separador(18)
print('Eval thermic level')
Separador(18)
print(pd.DataFrame(thermalLevelRef,columns=['Elevation','Thermic level']))
print('\n')
thermalLevelArray = []
for i in geoArray[elevationName]:
    thermalLevelArray.append(thermalLevelF(i))
stationTable['ThermalLevelValue']=thermalLevelArray
geoArray=stationTable[[latitudeName,longitudeName,elevationName,'ThermalLevelValue']]
print(geoArray.head(sampleRecord))
print('\nThermal level statistics:')
print('Count:')
print(geoArray['ThermalLevelValue'].value_counts())
print('\nNormalize percentage rate:')
print(geoArray['ThermalLevelValue'].value_counts(normalize=True))




# Show all data
if showAllRecords == True:
    print('\n')
    Separador(22)
    print('Datos en '+fileName)
    Separador(22)
    print('Index: ' + str(stationTable.index))
    pd.set_option('display.max_rows',stationTable.shape[0])
    print(stationTable)

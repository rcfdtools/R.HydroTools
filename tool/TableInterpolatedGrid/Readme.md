<div align="center"><img alt="R.HydroTools" src="../../file/graph/R.HydroTools.svg" width="300px"></div>

## Interpolación y representación espacial de series de datos meteorológicos con simbología de rampa única
Keywords: `arcgis-for-desktop` `arcgis-pro` `arcpy` `env` `workspace` `sys` `os` `shutil` `rmtree` `mkdir()` `time` `datetime` `warnings` `read()` `write()` `matplotlib` `numpy` `makexyeventlayer_management()` `select_analysis()` `idw()` `getrasterproperties_management()` `gp.rastercalculator_sa()` `addcolormap_management()` `readline()` `rstrip()` `split()` `close()` `len()`

A partir de series de datos diarias o mensuales contenidas en registros discretos dentro de archivos de texto separados por comas o CSV, interpolar y representar espacialmente datos hidrometeorológicos usando re-escalamiento a rampa única de color.

![TableInterpolatedGrid.png](Screenshot/TableInterpolatedGrid.png)

### Antecedentes

En el desarrollo de estudios hidrológicos, comúnmente se realiza la espacialización de variables meteorológicas en series temporales a través de procesos de interpolación, que luego son visualizadas desde interfases gráficas o GUI dentro de sistemas de información geográfica - SIG. Si bien este sistema facilita los procesos de análisis, existe un problema en su representación relacionado con el estilo de visualización, que para una rampa de color específica representa los valores de las celdas o pixeles desde el valor mínimo hasta el valor máximo encontrado, sin embargo, cuando se requiere analizar visualmente multiples grillas de una misma serie temporal (p.ej, una serie mensual precipitación media con 12 grillas), los colores utilizados en la representación para una misma rampa de referencia, no corresponden con los valores obtenidos en las demás grillas debido a que los valores mínimos y máximos pueden ser diferentes en cada una.

Para representar correctamente la serie temporal de la variable en estudio y poder visualizar bidimensional o tridimensionalmente las grillas de resultados, es necesario re-escalar los valores de todas las grillas a mapas de colores únicos a partir del mínimo y máximo encontrado en toda la serie de datos de entrada; de esta forma, en la representación, un valor discreto (p.ej, 100 milímetros de lluvia) existente en múltiples grillas será representado con el mismo color en la visualización.


### Caso de estudio

Estudio de variables hidrometeorológicos (precipitación, evaporación y brillo solar a nivel diario medio y mensual) en diferentes zonas de Colombia - Suramérica a partir de datos escalados utilizando series procesadas a partir de datos registrados por el [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM](http://www.ideam.gov.co/) de Colombia.


### Requerimientos

* [Python 2.7+ de ArcGIS for Desktop 10.6+](https://www.esri.com/en-us/home)
* [ArcGIS Pro 2.9+](https://www.esri.com/en-us/home)
* [PyCharm 2021.3+ Commmunity](https://www.jetbrains.com/pycharm/download/#section=windows) 
* [Sistema operativo Microsoft Windows](https://www.microsoft.com/en-us/windows?r=1)
* [matplotlib](https://matplotlib.org/)

> Para la actualización de librerías existentes o la instalación de librerías adicionales, se recomienda la creación y uso de ambientes virtuales para no modificar las versiones originales de Python sobre ArcMAP y QGIS.


### Funcionalidades

* Evaluación preliminar del archivo de entrada identificando el número de atributos y registros de datos.
* Previsualización de datos de entrada a partir del número de registros indicado por el usuario.
* Selección de variable numérica a representar. 
* Representación en grafica de texto mediante barras horizontales con % de referencia de cada valor discreto respecto al valor máximo encontrado.
* Estadísticos generales (conteo, no nulos, nulos, máximo, mínimo, sumatoria, promedio) de la variable seleccionada para el análisis.
* Evaluación de tamaño espacial del dominio a representar.
* Selección del tipo de frecuencia (diaria o mensual) a analizar. Diarios se evalúan en julianos de 1 a 366 y mensuales de 1 a 12. El usuario puede decidir si genera toda la serie temporal o una fracción (p.ej, para una serie de datos diarios, el usuario puede elegir solo generar los datos del primer trimestre correspondiente a los julianos entre el día 1 y 90 para años bisiestos)
* Selección del sistema de proyección de coordenadas - CRS. Se han incorporado en el módulo `TableInterpolatedGridModule.py` dentro del arreglo `coordSystem`, diferentes sistemas predeterminados.
* Definición de la resolución de salida de los mapas a interpolar. El valor se ingresa en función de las unidades del CRS seleccionado. El script hace una recomendación del tamaño de pixel para la interpolación y visualización a partir de 150 pixeles o celdas en la menor dimensión horizontal o vertical.
* Selección de rampa de colores (128, 256, 512, 1024 valores discretos únicos de color) a utilizar en la representación.
* Interpolación espacial masiva de grillas a partir de la escala temporal definida, teniendo en cuenta los parámetros definidos previamente.
* Reescalamiento de grillas principales a grillas de representación por simbología única utilizando algebra de mapas.
* Generación, almacenamiento y publicación de gráfica de serie de datos y previsualización de grillas con `matplotlib` para la variable en estudio. 

> Actualmente el script no dispone de representación segmentada (slices) para de una serie diaria elegir el juliano inicial y final. 
 
> Tenga en cuenta que la resolución espacial definida para la interpolación de grillas se define a partir del sistema de unidades, p.ej, para los sistemas MAGNA que contienen sistema proyectado, el valor de entrada se define en metros y para el CRS WGS84 el valor de entrada se define en grados decimales. 

 
### Ruta de ejecución

Para el desarrollo de este microcontenido se recomienda que los scripts y demás archivos requeridos se alojen en `D:\R.GISPython\TableInterpolatedGrid\` utilizando la siguiente estructura de directorios. 

| Directorio                                     | Descripción                                                                                                              |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [/Data](Data)                                  | Directorio de datos de entrada.                                                                                          |
| [/Graph](Graph)                                | Directorio con gráficas e ilustraciones.                                                                                 |
| [/Map](Map)                                    | Directorio con mapas para visualización de resultados en ArcGIS for Desktop y ArcGIS Pro.                                |
| [/Old](Old)                                    | Directorio con versiones antiguas del script y módulos.                                                                  |
| /OutputColorMap                                | Directorio de salida de grillas remuestreadas con rampa única de color.                                                  |
| /OutputGrid                                    | Directorio de salida de grillas generadas.                                                                               |
| [/PDF](PDF)                                    | Directorio con registros de ejecución en formado Adobe Acrobat.                                                          |
| [/Screenshot](Screenshot)                      | Capturas de pantalla con resultados de ejecución.                                                                        |
| /Temp                                          | Directorio donde se localizan los archivos de forma temporales generados para la creación de las grillas interpoladas.   |

> Los directorios `/OutputColorMap`, `/OutputGrid`, `/Temp` se crean automáticamente en la unidad local y no son visibles en el repositorio de GitHub debido al tamaño de los archivos generados. 


### Estructura de datos de entrada

Para la correcta ejecución del script se requiere que los archivos de texto separados por comas utilicen al menos la siguiente estructura:

| Campo  | Descripción                      | Aplica diarios | Aplica mensuales |
|--------|----------------------------------|----------------|------------------|
| Julian | Número de día del año de 1 a 366 | ✓              | ✕               |
| Month  | Mes del año de 1 a 12            | ✕              | ✓               |
| CX     | Coordenada en x o este           | ✓              | ✓               |
| CY     | Coordenada en y o noerte         | ✓              | ✓               |
| Var    | Variable númerica a representar  | ✓              | ✓               |


> En un mismo archivo de entrada pueden existir múltiples columnas `Var` (VTemp, VPrec, VEvap...) registrando diferentes variables meteorológicas, para lo cual el usuario podrá elegir la variable de entrada a analizar a partir de la lista de atributos encontrados.

> En representaciones diarias, el juliano 366 corresponde al día 29 de febrero para años bisiestos. 

### Procedimiento general

1. Descargar o clonar este microcontenido en `D:\R.GISPython\TableInterpolatedGrid\`

![MicrosoftWindowsFolder.png](Screenshot/MicrosoftWindowsFolder.png)

2. En PyCharm, configure los entornos virtuales para los intérpretes de Python para ArcGIS for Desktop y ArcGIS Pro.  

![Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3PythonInterpreter.png](Screenshot/Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3PythonInterpreter.png)

![Python3.7.11ArcGISPro2.9.0PyCharm2021.3PythonInterpreter.png](Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3PythonInterpreter.png)

> Para la explicación del procedimiento general utilizaremos Python 3.7.11 de ArcGIS Pro 2.9.0.

3. En PyCharm, abra y ejecute el script `TableInterpolatedGrid.py`, podrá observar un la cabecera resumen de ejecución, los requerimientos de ejecución y los valores definidos en las variables de entrada para el caso de estudio a evaluar, el archivo de entrada a procesar, el identificador del log de registro de ejecución, los atributos encontrados y el total de registros en el archivo CSV incluida la cabecera. Digite `Y` para continuar.

> Antes de la ejecución, se recomienda cerrar las aplicaciones de ArcGIS for Desktop. El script puede ser ejecutado directamente desde un Notebook de ArcGIS Pro sin usar PyCharm y con la interfaz de usuario gráfica abierta.
 
> El archivo ejemplo de entrada a procesar, corresponde a la precipitación media mensual de varias estaciones meteorológicas.   

![Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleIntro.png](Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleIntro.png)

4. Digite el número de registros de muestra que quiere imprimir en pantalla, p.ej, 24 que corresponde a 24 meses de datos para la primera estación encontrada. 

![Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleRecordSample.png](Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleRecordSample.png)

5. Indique el número de columna que será utilizada como variable numérica de análisis, p.ej, 11 que corresponde al valor de precipitación registrado cada mes para cada estación.

![Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleFieldName.png](Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleFieldName.png)

6. Indique si quiere representar en una gráfica de texto tipo barras, los valores discretos de todos los registros encontrados. Digite `Y`.

![Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleGraphText.png](Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleGraphText.png)

Luego de la visualización de la gráfica de texto podrá observar los estadísticos generales de la variable en estudio y el tamaño espacial del dominio obtenido a partir de las coordenadas de entrada en la serie de datos.

![Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleStatDomain.png](Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleStatDomain.png)

7. Indique la frecuencia temporal a analizar, p.ej, 2 para datos mensuales y el total de grillas a generar. 

![Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleFrecuencyGrids.png](Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleFrecuencyGrids.png)

8. Indique el sistema de coordenadas a utilizar en la creación de los archivos temporales de nodos shapefile y en la creación de las grillas interpoladas. Para este ejercicio utilizaremos `07  WKID: 9377, MAGNA-SIRGAS / Origen-Nacional`.

![Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleCRS.png](Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleCRS.png)

9. Indique la resolución a utilizar en la creación de las grillas interpoladas de salida, p.ej, 100 metros para el CRS seleccionado.

![Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleResolution.png](Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleResolution.png)

10. Seleccione la rampa de color a utilizar en los mapas de color reescalados, p.ej, 13 para la rampa `Green Sea - Blue Sea - Purple - Red - Orange - Yellow` que contiene 512 colores discretos interpolados a partir de 18 colores de referencia.

![Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleColorRamp.png](Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleColorRamp.png)

13. Luego de definida la rampa de color, iniciará la creación de los archivos temporales en `/Temp` de estaciones para cada mes (o cada día dependiendo de la frecuencia seleccionada y los datos de entrada), la generación de las grillas interpoladas en `/OutputGrid` y el reescalamiento a grillas de representación en `/OutputColorMap`. 

![Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleCreatingGrids.png](Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleCreatingGrids.png)

![Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleCreatingColorGrids.png](Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleCreatingColorGrids.png)

14. Revise el resumen de resultados y los estadísticos de valores máximos y mínimos en celdas.

![Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleSummary.png](Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3ConsoleSummary.png)

15. En ArcScene de ArcGIS for Desktop, cargue y visualice las grillas de resultados.

En las opciones de configuración de la escena para `Scene Layers` establezca la exageración vertical en 250, para cada grilla defina las alturas base a partir de los valores discretos de cada pixel en la propia imagen y en la resolución de salida establezca el valor de la resolución utilizada en la creación de las grillas.

![ArcScene10.2.2VerticalExaggeration.png](Screenshot/ArcScene10.2.2VerticalExaggeration.png)

![ArcScene10.2.2BaseHeights.png](Screenshot/ArcScene10.2.2BaseHeights.png)

![ArcScene10.2.2RasterSurfaceResolution.png](Screenshot/ArcScene10.2.2RasterSurfaceResolution.png)

![ArcScene10.2.2OutputGrid.png](Screenshot/ArcScene10.2.2OutputGrid.png)
![ArcScene10.2.2OutputColorMap.png](Screenshot/ArcScene10.2.2OutputColorMap.png)


### Ejecuciones

#### Ejecución en ArcGIS for Desktop sobre PyCharm

![Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3.png](Screenshot/Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3.png)


#### Ejecución en ArcGIS Pro sobre PyCharm

![Python3.7.11ArcGISPro2.9.0PyCharm2021.3.png](Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3.png)


#### Carpetas de resultados

![OutputGrid.png](Screenshot/OutputGrid.png)
![OutputColorMap.png](Screenshot/OutputColorMap.png)


#### Ejemplo de previsualización de log de resultados, grillas de salida y gráfica de muestreo de valores mensuales

[Log de resultados](PDF/1641147594.pdf)

![Value data plot](Graph/1641147594PlotBar.png)

Grillas principales de salida sin remuestreo de rampa de color

![FileGRDM001.tif](Graph/1641147594GRDM001.png)
![FileGRDM002.tif](Graph/1641147594GRDM002.png)
![FileGRDM003.tif](Graph/1641147594GRDM003.png)
![FileGRDM004.tif](Graph/1641147594GRDM004.png)
![FileGRDM005.tif](Graph/1641147594GRDM005.png)
![FileGRDM006.tif](Graph/1641147594GRDM006.png)
![FileGRDM007.tif](Graph/1641147594GRDM007.png)
![FileGRDM008.tif](Graph/1641147594GRDM008.png)
![FileGRDM009.tif](Graph/1641147594GRDM009.png)
![FileGRDM010.tif](Graph/1641147594GRDM010.png)
![FileGRDM011.tif](Graph/1641147594GRDM011.png)
![FileGRDM012.tif](Graph/1641147594GRDM012.png)

Grillas principales de salida con remuestreo de rampa de color

![FileGRDM001ColorMap.tif](Graph/1641147594GRDM001ColorMap.png)
![FileGRDM002ColorMap.tif](Graph/1641147594GRDM002ColorMap.png)
![FileGRDM003ColorMap.tif](Graph/1641147594GRDM003ColorMap.png)
![FileGRDM004ColorMap.tif](Graph/1641147594GRDM004ColorMap.png)
![FileGRDM005ColorMap.tif](Graph/1641147594GRDM005ColorMap.png)
![FileGRDM006ColorMap.tif](Graph/1641147594GRDM006ColorMap.png)
![FileGRDM007ColorMap.tif](Graph/1641147594GRDM007ColorMap.png)
![FileGRDM008ColorMap.tif](Graph/1641147594GRDM008ColorMap.png)
![FileGRDM009ColorMap.tif](Graph/1641147594GRDM009ColorMap.png)
![FileGRDM010ColorMap.tif](Graph/1641147594GRDM010ColorMap.png)
![FileGRDM011ColorMap.tif](Graph/1641147594GRDM011ColorMap.png)
![FileGRDM012ColorMap.tif](Graph/1641147594GRDM012ColorMap.png)

### Scripts

#### Script [TableInterpolatedGrid.py](TableInterpolatedGrid.py)

```
# -*- coding: UTF-8 -*-
# Script name: TableInterpolatedGrid.py
# Description: Interpolación y representación espacial de datos hidrometeorológicos en rango de escala única
# Requirements: PyCharm 2021.3+, ArcGIS 10+, ArcGIS Pro 2.9.0

# Libraries
import arcpy
from arcpy import env
from arcpy.sa import *
import sys
import os.path
import shutil
import time
import warnings
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
import TableInterpolatedGridModule as rtg

# Local variables
studyCase = 'Estudio de la precipitación diaria media en el Departamento del Cesar - Colombia - Suramérica'
warnings.filterwarnings('ignore')
absolutePath = r'D:/R.GISPython/TableInterpolatedGrid/' # .'/' for relative path
env.workspace = absolutePath + 'OutputGrid'
outputPath = absolutePath+'OutputGrid/'
outputPathColorMap = absolutePath+'OutputColorMap/'
outputTemp = absolutePath+'Temp/'
fileCSVIn = absolutePath+'Data/Sample3PrecipitationAverageMonthly.csv'
shapefileTemp = outputTemp+'TempShapefile.shp'
colorMapStyleFolder = absolutePath+'ColorMapStyle/'
logExecutionFle = open('TableInterpolatedGridLog.csv', 'a')
urlGitHub = 'https://github.com/rcfdtools/R.GISPython/blob/main/TableInterpolatedGrid'
timeStart = time.time()
os.system('color 0E')
arcpy.env.overwriteOutput = True
gridSampleScreenShow = False
gridSampleResolution = 96  # dpi

# Header
rtg.printtitle('Spatial interpolation and representation of meteorological data in a unique symbology ramp', 'both', False)
print('\nExecution date & time: ' + str(datetime.now()) +
      '\nScript compatibility: ArcGIS for Desktop 10.6+ y ArcGIS Pro'
      '\nPython version: ' + str(sys.version) +
      '\nPython path: ' + str(sys.path[0:5]) +
      '\nmatplotlib version: ' + str(matplotlib.__version__) +
      '\nRepository: https://github.com/rcfdtools/R.GISPython/tree/main/TableInterpolatedGrid'
      '\nLicense and conditions: https://github.com/rcfdtools/R.GISPython/wiki/License'
      '\nCredits: r.cfdtools@gmail.com\n')

# Requirements
rtg.printtitle('Requirements')
print('\nValid table format file: comma separated values .csv'
      '\nFloat or double values required period as decimal separator.'
      '\nCSV file with header row.'
      '\nField or attribute names can not content comma or special characters.'
      '\nHeader attributes names required: Julian (1-366), Month (1-12), CX, CX, Var.'
      '\nVar correspond to the numeric variable for analysis. User can choice the var name.'
      '\nCompatible with ArcGIS for Desktop 10+ and ArcGIS Pro.'
      '\nArcGIS Spatial analyst extension: ' + arcpy.CheckOutExtension('Spatial') + '\n')

# Preprocessing variables
rtg.printtitle('Study case & File data summary')
dTime = datetime.today()  # Get timezone naive now
#logFileNumber = int(dTime.timestamp()) # Compatible with Python 3
logFileNumber = int(time.mktime(dTime.timetuple())) # Compatible with Python 2 & 3
print('\nStudy case: ' + studyCase +
      '\nInput file: ' + fileCSVIn +
      '\nLog file #: ' + str(logFileNumber))
fieldsCSV = rtg.csvtotalfieldfound(fileCSVIn)
totalRecords = rtg.csvtotalrecordfound(fileCSVIn)
print('\n' + rtg.systemprompt() + 'Attention - If you are using ArcGIS for Desktop with Python 2, all the options may be enter using quotes...')
input('\n' + rtg.systemprompt() + "Attention - Close all your ArcGIS for Desktop applications and type 'Y' to continue >> ")
rtg.csvsamplerecord(fileCSVIn, totalRecords+1)
fieldNumberEval = rtg.csvheader(fileCSVIn, totalRecords, fieldsCSV)
print('\n')
rtg.graphtxt(fileCSVIn, totalRecords, fieldNumberEval[0])
print('\n')
StatisticCSV = rtg.csvstatistic(fileCSVIn, totalRecords, fieldNumberEval[0])
maxVal = StatisticCSV[3]
minVal = StatisticCSV[4]
spatialDomainCSV = rtg.csvspacialdomain(fileCSVIn)
gidCellSizeRecommended = spatialDomainCSV[2]
fieldEvalStr = fieldNumberEval[1]
dataFrequency = rtg.datafrequency()
frequencyFieldOpt = dataFrequency[1]
frequencyMaxVal = int(dataFrequency[0])
numGrid = rtg.optionrange('Total grids to create ', 1, frequencyMaxVal)
userCRS = rtg.crscoordsystem()
gridResolution = rtg.optionrangefloat(('Output grid resolution for the coordinate system selected (%f recommended for %s pixels)' % (gidCellSizeRecommended, str(spatialDomainCSV[3]))), 0, 10000)
colorMapFileArray = rtg.colormapstyle(colorMapStyleFolder)
colorMapFile = colorMapFileArray[0]
colorMapFilePrev = colorMapFileArray[1]
colorMapFileColors = float(colorMapFileArray[2])
numColor = int(colorMapFileColors)
slopeRampData = numColor / (maxVal - minVal)
os.system(colorMapFilePrev)


# Delete previous data Temp and Out folder created
try:
    shutil.rmtree(outputPath)  # Remove Out folder
except:
    print(rtg.systemprompt() + 'Out folder does not exists')
os.mkdir(outputPath)  # Create empty Out folder
try:
    shutil.rmtree(outputPathColorMap)  # Remove Temp folder
except:
    print(rtg.systemprompt() + 'Out Color Map folder does not exists')
os.mkdir(outputPathColorMap)  # Create empty Temp folder
try:
    shutil.rmtree(outputTemp)  # Remove Temp folder
except:
    print(rtg.systemprompt() + 'Temp folder does not exists')
os.mkdir(outputTemp)  # Create empty Temp folder


# Grid builder section
numGridStr = str(numGrid)
incV = 1; maxValPixelValue = -1e99; minValPixelValue = 1e99; dayMonthMax = 0; dayMonthMin = 0;
print('\n')
rtg.printtitle('Creating ' + numGridStr + ' file grids', 'both')
while incV <= numGrid:
    incVStr = str(incV)

    # Process: Make XY Event Layer
    eventLyr = 'EventLyr' + incVStr
    arcpy.MakeXYEventLayer_management(fileCSVIn, 'CX', 'CY', eventLyr, userCRS, '')

    # Process: Select records from Julian day number
    frequencyFieldOptTxt = '\"'+frequencyFieldOpt+'\" ='
    arcpy.Select_analysis(eventLyr, shapefileTemp, frequencyFieldOptTxt + incVStr)

    # Process: IDW - Inverse Distance Weight Intepolation
    gridDayNFileName = 'GRDM' + incVStr.zfill(3) + '.tif'
    gridDayNTiff = outputPath + gridDayNFileName
    #arcpy.gp.Idw_sa(shapefileTemp, 'Var', gridDayNTiff, gridResolution, '2', 'VAR 12', '')
    #arcpy.gp.Idw_sa(shapefileTemp, fieldEvalStr, gridDayNTiff, gridResolution, '2', '', '')
    power = 2
    searchRadius = RadiusVariable(10, 150000)
    outIDW = Idw(shapefileTemp, fieldEvalStr, gridResolution, power, searchRadius) 
    outIDW.save(gridDayNTiff)

    # Remove and create Temp folder
    shutil.rmtree(outputTemp)  # Remove Temp folder
    os.mkdir(outputTemp)  # Create empty Temp folder

    # Process: Show created raster properties
    cyMax = arcpy.GetRasterProperties_management(gridDayNTiff, 'TOP', '')
    cyMaxAux = float(cyMax.getOutput(0))
    cyMin = arcpy.GetRasterProperties_management(gridDayNTiff, 'BOTTOM', '')
    cyMinAux = float(cyMin.getOutput(0))
    ySize = (cyMaxAux - cyMinAux) / 1000
    cxMax = arcpy.GetRasterProperties_management(gridDayNTiff, 'RIGHT', '')
    cxMaxAux = float(cxMax.getOutput(0))
    cxMin = arcpy.GetRasterProperties_management(gridDayNTiff, 'LEFT', '')
    cxMinAux = float(cxMin.getOutput(0))
    xSize = (cxMaxAux - cxMinAux) / 1000
    valMax = arcpy.GetRasterProperties_management(gridDayNTiff, 'MAXIMUM', '')
    valMaxAux = float(valMax.getOutput(0))
    valMin = arcpy.GetRasterProperties_management(gridDayNTiff, 'MINIMUM', '')
    valMinAux = float(valMin.getOutput(0))
    print('File' + gridDayNFileName + ' - High, km: ' + str(ySize) + ' - Width, km: ' + str(xSize) + ' - Min: ' + str(round(valMinAux, 4)) + ' - Max: ' + str(round(valMaxAux, 4)) + ' - Ok...')
    if valMaxAux > maxValPixelValue:
        maxValPixelValue = valMaxAux
        dayMonthMax = incV
    if valMinAux < minValPixelValue:
        minValPixelValue = valMinAux
        dayMonthMin = incV

    # Plot and save each grid sample
    gridImg = plt.imread(gridDayNTiff)
    pltFig = matplotlib.pyplot.gcf()
    pltFig.set_size_inches(6, 6)
    plt.imshow(gridImg)
    plt.xlabel('CX pixels')
    plt.ylabel('CY pixels')
    plt.title(str(logFileNumber) + 'GridSampleGRDM' + incVStr.zfill(3) + '.png')
    plt.imshow(gridImg[:, :, 0], cmap=plt.cm.coolwarm)  # cmap=plt.cm.Spectral or cmap=plt.cm.hot
    plt.colorbar()
    plt.savefig(absolutePath + '/Graph/' + str(logFileNumber) + 'GRDM' + incVStr.zfill(3) + '.png', dpi=gridSampleResolution)
    if gridSampleScreenShow:
        plt.show()
    plt.close()
    print(urlGitHub + '/Graph/' + str(logFileNumber) + 'GRDM' + incVStr.zfill(3) + '.png')
    incV += 1


# Grid color map using integer scale
incV = 1; maxValPixelValueStr = str(maxValPixelValue); minValStr = str(minVal); numColorStr = str(numColor); slopeRampDataStr = str(slopeRampData);
print('\n')
rtg.printtitle('Creating ' + str(numGridStr) + ' grid color scaled files ('+(str(numColor)) + ' colors)')
print('\nAll database values'
      '\nMax data value: ' + str(maxVal) +
      '\nMin data value: ' + str(minVal) +
      '\nSlope colors ramp: ' + str(slopeRampData) +
      '\n\nGrids created'
      '\nMax pixel value: ' + str(maxValPixelValue) +
      '\nMin pixel value: ' + str(minValPixelValue) + '\n')
while incV <= numGrid:
    incVStr = str(incV)
    gridDayNFileName = 'GRDM' + incVStr.zfill(3) + '.tif'
    gridDayNTiffSorce = outputPath + gridDayNFileName
    gridDayNTiffTarget = outputPathColorMap + gridDayNFileName
    vAlgebraMapClc = 'Con((Int(((\''+gridDayNTiffSorce+'\'-'+minValStr+')*'+slopeRampDataStr+')))>'+numColorStr+','+numColorStr+',(Int(((\''+gridDayNTiffSorce+'\'-'+minValStr+')*'+slopeRampDataStr+'))))'
    arcpy.gp.RasterCalculator_sa(vAlgebraMapClc, gridDayNTiffTarget)
    arcpy.AddColormap_management(gridDayNTiffTarget, '', colorMapFile)
    print('File color map ' + gridDayNFileName + ' - Ok...')

    # Plot and save each color map grid sample
    gridImg = plt.imread(gridDayNTiffTarget)
    pltFig = matplotlib.pyplot.gcf()
    pltFig.set_size_inches(6, 6)
    plt.imshow(gridImg)
    plt.xlabel('CX pixels')
    plt.ylabel('CY pixels')
    plt.title(str(logFileNumber) + 'GridSampleGRDM' + incVStr.zfill(3) + 'ColorMap.png')
    plt.imshow(gridImg[:, :, 0], cmap=plt.cm.coolwarm)  # cmap=plt.cm.Spectral or cmap=plt.cm.hot
    plt.colorbar()
    plt.savefig(absolutePath + '/Graph/' + str(logFileNumber) + 'GRDM' + incVStr.zfill(3) + 'ColorMap.png', dpi=gridSampleResolution)
    if gridSampleScreenShow:
        plt.show()
    plt.close()
    print(urlGitHub + '/Graph/' + str(logFileNumber) + 'GRDM' + incVStr.zfill(3) + 'ColorMap.png')
    incV += 1


# General plot
pltFig = matplotlib.pyplot.gcf()
pltFig.set_size_inches(12, 6)
plt.grid(color='0.95')
plt.bar(StatisticCSV[7], StatisticCSV[8], color='k')
plt.xlabel('Record #')
plt.ylabel('Var')
plt.title('Current values over the CSV file for the selected Var\nLog #: '+str(logFileNumber))
plt.savefig(absolutePath+'/Graph/'+str(logFileNumber)+'PlotBar.png', dpi=gridSampleResolution)
if gridSampleScreenShow:
    plt.show()
plt.close()


# Show final process resume
timeEnd = time.time()
print('\n')
rtg.printtitle('Statistics and summary grid creation report')
print('\nGrids created on: ' + outputPath +
      '\nColor Map Grids created on: ' + outputPathColorMap +
      '\nMinimum pixel value all grids: ' + str(round(minValPixelValue, 4)) +
      '\nMaximum pixel value all grids: ' + str(round(maxValPixelValue, 4)) +
      '\nArcScene Z Scale conversion: ' + str(round((maxValPixelValue/colorMapFileColors), 6)) +
      '\nDay or Month with maximum value: ' + str(dayMonthMax) +
      '\nManual print PDF as: ' + absolutePath+ '/PDF/' + str(logFileNumber) + '.pdf' +
      '\nValue data plot: '+urlGitHub+'/Graph/'+str(logFileNumber)+'PlotBar.png' +
      '\nProcess accomplished (dt = ' + str(round(timeEnd - timeStart, 1)) + 'sec or ' + str(round((timeEnd - timeStart)/60, 1)) + 'min)')
from datetime import datetime
logExecutionFle.write(str(logFileNumber) + ',' + str(datetime.now()) + ',' + fileCSVIn + ',"' + str(studyCase) + '"\n')
logExecutionFle.close()
vExit = input("\n%s Type 'Y' to exit >> " % (rtg.systemprompt()))
```

#### Script [TableInterpolatedGridModule.py](TableInterpolatedGridModule.py)

```
# Module name: TableInterpolatedGridModule.py
# Description: CSV process file module.
# Requirements: PyCharm 2021.3+, ArcGIS 10+, ArcGIS Pro 2.9.0
# Tested in Python 2.7.5, 2.7.12, 3.7.11
# Credits: r.cfdtools@gmail.com

import numpy as np

# System prompt
def systemprompt():
    systemprompt = '{R} '
    return systemprompt

# Print titles
def printtitle(titleText, titleType = 'both', showTab = False):
    # titleType: Top, Bottom, both
    nc = '-'
    valLen = len(titleText)
    tabTxt = ''
    if showTab:
        tabTxt = '\t'
    if titleType == 'both':
        print(tabTxt + nc * valLen)
        print(tabTxt + titleText)
        print(tabTxt + nc * valLen)
    elif titleType == 'Top':
        print(tabTxt + nc * valLen)
        print(tabTxt + titleText)
    else:
        print(tabTxt + titleText)
        print(tabTxt + nc * valLen)

# Range options for integers or list values
def optionrange(txtMsg, minOpt, maxOpt):
    valOpt = 0
    while valOpt == 0:
        valueUser = input('\n%s%s (%d/%d): >> ' % (systemprompt(), txtMsg, minOpt, maxOpt))
        if type(valueUser) != int:
            try:
                valueUser = int(valueUser)
                if valueUser >= minOpt and valueUser <= maxOpt:
                    print('Entry option was %d.' % (valueUser))
                    valOpt = 1
                else:
                    print('%sAttention, value out of range (%d-%d).' % (systemprompt(), minOpt, maxOpt))
            except:
                #print('%s Attention, ivalLenid value. Enter an integer value.' %(systemprompt()))
                vExcept = 0
    return valueUser


# Range options for floats values in a range
# For example for grid resolutions
def optionrangefloat(txtMsg, minOpt, maxOpt):
    valOpt = 0
    while valOpt == 0:
        valueUser = input('%s%s (%d/%d): >> ' % (systemprompt(), txtMsg, minOpt, maxOpt))
        if type(valueUser) != float:
            try:
                valueUser = float(valueUser)
                if valueUser >= minOpt and valueUser <= maxOpt:
                    print('Entry option was %f.' % (valueUser))
                    valOpt = 1
                else:
                    print('%sAttention, value out of range (%d-%d).' % (systemprompt(), minOpt, maxOpt))
            except:
                #  print('%s Atention, ivalLenid value. Enter an integer value.' %(systemprompt()))
                vExcept = 0
    return valueUser


# Option Yes/No
def optionyesno(txtMsg):
    valOpt = 0
    while valOpt == 0:
        valueUser = input('%s%s (Y/N) >> ' % (systemprompt(), txtMsg))
        if type(valueUser) == str:
            valueUserlow = valueUser.lower()
            if valueUserlow == 'y' or valueUserlow == 'n': 
                valOpt = 1
            else:
                print('Option %s ivalLenid. Try again.\n' % (valueUser))
    print('Entry option was %s.' % (valueUser))
    return valueUser.lower()


# Total fields founded in the CSV file
# userFileName: Complete File name to process
def csvtotalfieldfound(userFileName):
    userFile = open (userFileName)
    recordLine = userFile.readline().rstrip('\n')  # rstrip remove jump line
    recordLineArray = recordLine.split(',')
    fieldsLen = len(recordLineArray)
    print('Attributes: %d' % (fieldsLen))
    userFile.close()
    return fieldsLen


# Total records founded
# userFileName: Complete File name to process
def csvtotalrecordfound(userFileName):
    userFile = open(userFileName)  # Open only for reading
    totalRecord = len(open(userFileName).readlines())
    if totalRecord == 0:
        print('Records: 0')
    else:
        print('Records: %d' % (totalRecord-1))
    totalRecord -= 1
    userFile.close()
    return totalRecord


# Spatial domain and grid size recommended
# userFileName: Complete File name to process
def csvspacialdomain(userFileName):
    printtitle('Spatial domain in the station records')
    fieldsLen = csvtotalfieldfound(userFileName)
    userFile = open(userFileName)  # Open only for reading
    recordLine = userFile.readline().rstrip('\n')  # rstrip remove jump line # Read de header line
    recordLineArray = recordLine.split(',')
    # Eval column number with CX and CY Values
    cxNum, cyNum = -1, -1
    for j in range(0, fieldsLen):
        if recordLineArray[j].upper() == 'CX':
            cxNum = j
            print('CX field number: ' + str(cxNum+1))
        elif recordLineArray[j].upper() == 'CY':
            cyNum = j
            print('CY field number: ' + str(cyNum+1))
    if cxNum == -1 or cyNum == -1:
        print('Alert: Cy or CY fiends not found')
    totalRecord = len(open(userFileName).readlines())
    if totalRecord == 0:
        print('No records found.')
    else:
        print('%d records found.' % (totalRecord-1))
    totalRecord -= 1
    cyMax, cyMin, cxMax, cxMin = 0, 1e99, 0, 1e99
    for i in range(0, totalRecord):
        recordLine = userFile.readline().rstrip('\n')  # rstrip remove jump line
        recordLineArray = recordLine.split(',')
        if recordLineArray[cxNum] != '\n' and recordLineArray[cxNum] != '' and recordLineArray[cyNum] != '\n' and recordLineArray[cyNum] != '':
            if float(recordLineArray[cxNum]) > cxMax: cxMax = float(recordLineArray[cxNum])
            if float(recordLineArray[cxNum]) < cxMin: cxMin = float(recordLineArray[cxNum])
            if float(recordLineArray[cyNum]) > cyMax: cyMax = float(recordLineArray[cyNum])
            if float(recordLineArray[cyNum]) < cyMin: cyMin = float(recordLineArray[cyNum])
    spatialDomainWidth = cxMax - cxMin
    spatialDomaintHeigh = cyMax - cyMin
    numPixel = 150
    if spatialDomainWidth > spatialDomaintHeigh:
        vGridCellSizeRecommended = spatialDomaintHeigh / numPixel  # Divide minor value into 150 pixels
    else:
        vGridCellSizeRecommended = spatialDomainWidth / numPixel  # Divide minor value into 150 pixels
    print('CX max: %f  CX min: %f  Width: %f' % (cxMax, cxMin, spatialDomainWidth))
    print('CY max: %f  CY min: %f  Heigh: %f' % (cyMax, cyMin, spatialDomaintHeigh))
    print('Recommended grid cell size: ' + str(vGridCellSizeRecommended))
    print('(Using as reference 150 pixels in the shortest horizontal or vertical spatial length)\n')
    userFile.close()
    return (spatialDomainWidth, spatialDomaintHeigh, vGridCellSizeRecommended, numPixel)


# Show records sample
# userFileName: Complete File name to process
# totalRecord: Total rows in the file
def csvsamplerecord(userFileName, totalRecord):
    userFile = open(userFileName)
    csvNumRecordSample = optionrange('Number sample records for print with header', 0, totalRecord)
    print('\n')
    printtitle('Data file record sample (%d records)' % (csvNumRecordSample))
    for j in range(0, csvNumRecordSample):
        recordLine = userFile.readline().rstrip('\n')  # rstrip remove jump line
        recordLineArray = recordLine.split(',')
        print((str(j+1).zfill(6))+' ' + str(recordLineArray))
    userFile.close()


# Daily or montly data
def datafrequency():
    dataFrequencyArray = np.array([
        (1, 366, 'Dayly', 'Julian'),
        (2, 12, 'Monthly', 'Month')])
    dataFrequencyArrayCount = len(dataFrequencyArray)
    print('Frequencies: ' + str(dataFrequencyArrayCount))
    printtitle('ID, Max. val, Frequency field required')
    for j in range(0, dataFrequencyArrayCount):
        print(str((dataFrequencyArray[j, 0]).zfill(2)) + '  ' + str((dataFrequencyArray[j, 1].zfill(4))) + '  ' + dataFrequencyArray[j, 2] + '  ' + dataFrequencyArray[j, 3])
    dataFrequencyArrayOpt = optionrange('Frequency to use', 1, (dataFrequencyArrayCount))
    frequencyMaxVal = dataFrequencyArray[(dataFrequencyArrayOpt-1), 1]
    frequencyField = dataFrequencyArray[(dataFrequencyArrayOpt-1), 3]
    return (frequencyMaxVal, frequencyField)


# CRS - Coordinate reference system
def crscoordsystem():
    coordSystem = np.array([
        (1, 'WKID: 4326, WGS84', 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'),
        (2, 'WKID: 3116, MAGNA Colombia Origen Bogota', 'PROJCS["MAGNA_Colombia_Bogota",GEOGCS["GCS_MAGNA",DATUM["D_MAGNA",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",1000000.0],PARAMETER["False_Northing",1000000.0],PARAMETER["Central_Meridian",-74.07750791666666],PARAMETER["Scale_Factor",1.0],PARAMETER["Latitude_Of_Origin",4.596200416666666],UNIT["Meter",1.0]],VERTCS["WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]]'),
        (3, 'WKID: 3117, MAGNA Colombia Origen Este', 'PROJCS["MAGNA_Colombia_Este",GEOGCS["GCS_MAGNA",DATUM["D_MAGNA",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",1000000.0],PARAMETER["False_Northing",1000000.0],PARAMETER["Central_Meridian",-71.07750791666666],PARAMETER["Scale_Factor",1.0],PARAMETER["Latitude_Of_Origin",4.596200416666666],UNIT["Meter",1.0]],VERTCS["WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]]'),
        (4, 'WKID: 3118, MAGNA Colombia Origen Este Este', 'PROJCS["MAGNA_Colombia_Este_Este",GEOGCS["GCS_MAGNA",DATUM["D_MAGNA",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",1000000.0],PARAMETER["False_Northing",1000000.0],PARAMETER["Central_Meridian",-68.07750791666666],PARAMETER["Scale_Factor",1.0],PARAMETER["Latitude_Of_Origin",4.596200416666666],UNIT["Meter",1.0]],VERTCS["WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]]'),
        (5, 'WKID: 3115, MAGNA Colombia Origen Oeste', 'PROJCS["MAGNA_Colombia_Oeste",GEOGCS["GCS_MAGNA",DATUM["D_MAGNA",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",1000000.0],PARAMETER["False_Northing",1000000.0],PARAMETER["Central_Meridian",-77.07750791666666],PARAMETER["Scale_Factor",1.0],PARAMETER["Latitude_Of_Origin",4.596200416666666],UNIT["Meter",1.0]],VERTCS["WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]]'),
        (6, 'WKID: 3114, MAGNA Colombia Origen Oeste oeste', 'PROJCS["MAGNA_Colombia_Oeste_Oeste",GEOGCS["GCS_MAGNA",DATUM["D_MAGNA",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",1000000.0],PARAMETER["False_Northing",1000000.0],PARAMETER["Central_Meridian",-80.07750791666666],PARAMETER["Scale_Factor",1.0],PARAMETER["Latitude_Of_Origin",4.596200416666666],UNIT["Meter",1.0]],VERTCS["WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]]'),
        (7, 'WKID: 9377, MAGNA-SIRGAS / Origen-Nacional', 'PROJCS["MAGNA_Colombia_Origen_Unico",GEOGCS["GCS_MAGNA",DATUM["D_MAGNA",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",5000000.0],PARAMETER["False_Northing",2000000.0],PARAMETER["Central_Meridian",-73.0],PARAMETER["Scale_Factor",0.9992],PARAMETER["Latitude_Of_Origin",4.0],UNIT["Meter",1.0]]')])
    coordSystemCount = len(coordSystem)
    print('\nCoordinate systems: ' + str(coordSystemCount))
    printtitle('ID, Coordinate system')
    for j in range(0, coordSystemCount):
        print(str((coordSystem[j, 0])).zfill(2) + '  ' + (coordSystem[j, 1].zfill(4)))
    coordSystemOpt = optionrange('Coordinate system to use', 1, (coordSystemCount))
    coordSystemVal = coordSystem[(coordSystemOpt-1), 2]
    print('\n' + coordSystemVal + '\n')
    return (coordSystemVal)


# Headers
# userFileName: Complete File name to process
# totalRecord: Total rows in the file
# totalRecord: Total fields in the file
def csvheader(userFileName, totalRecord, fieldsLen):
    userFile = open(userFileName)
    recordLine = userFile.readline().rstrip('\n')  # rstrip remove jump line
    recordLineArray = recordLine.split(',')
    print('\nHeaders in data file:')
    printtitle('#, Field name')
    for k in range(0, fieldsLen):
        print('('+(str(k+1).zfill(2))+') ' + recordLineArray[k])
    fieldNumberEval = optionrange('Field number to eval', 1, fieldsLen)
    vFieldEvalStr = recordLineArray[fieldNumberEval-1]
    userFile.close()
    print('Variable in use is ['+vFieldEvalStr+']\n')
    return (fieldNumberEval, vFieldEvalStr)


# Statistics
# userFileName: Complete File name to process
# totalRecord: Total rows in the file
# fieldNumberEval: Column field number to eval
def csvstatistic(userFileName, totalRecord, fieldNumberEval):
    printtitle('Statistics')
    userFile = open(userFileName)
    recordLine = userFile.readline().rstrip('\n')  # strip remove jump line
    varSum = 0
    varMax = -1e-99
    varMin = 1e99
    varCount = 0
    varXPlot, varYPlot = [], [] 
    for i in range(0, totalRecord):
        recordLine = userFile.readline().rstrip('\n')  # strip remove jump line
        recordLineArray = recordLine.split(',')
        # print('Var ',i,' ',recordLineArray[fieldNumberEval-1])
        if recordLineArray[fieldNumberEval-1] != '\n' and recordLineArray[fieldNumberEval-1] != '':
            varCount += 1
            # Eval Total
            varSum += float(recordLineArray[fieldNumberEval-1])
            # Eval Maximum
            if float(recordLineArray[fieldNumberEval-1]) > varMax:
                varMax = float(recordLineArray[fieldNumberEval-1])
            # Eval Minimum
            if float(recordLineArray[fieldNumberEval-1]) < varMin:
                varMin = float(recordLineArray[fieldNumberEval-1])      
            # Plot vars array
            varXPlot.append(i+1)
            varYPlot.append(float(recordLineArray[fieldNumberEval-1]))
    varAverage = varSum/varCount
    varNulls = totalRecord-varCount
    print('Registers: ' + str(totalRecord) +
          '\nCount: ' + str( varCount) + ' (not null)' +
          '\nNulls: ' + str(varNulls) +
          '\nMax: ' + str(varMax) +
          '\nMin: ' + str(varMin) +
          '\nSum: ' + str(varSum) +
          '\nAvg: ' + str(varAverage) + '\n')
    return (totalRecord, varCount, varNulls, varMax, varMin, varSum, varAverage, varXPlot, varYPlot)
    userFile.close()


# Color map styles
# folderColorMapStyle: Complete folder color map styles path
def colormapstyle(folderColorMapStyle):
    colorMapStyleArray = np.array([
        (0, 1, 128, 'ColorMap1 - Grayscale: White - Black'),
        (1, 1, 256, 'ColorMap1 - Grayscale: White - Black'),
        (2, 2, 128, 'ColorMap2 - Grayscale invert: Black - White'),
        (3, 2, 256, 'ColorMap2 - Grayscale invert: Black - White'),
        (4, 3, 128, 'ColorMap3 - Pantone 2: Red - Green'),
        (5, 3, 256, 'ColorMap3 - Pantone 2: Red - Green'),
        (6, 4, 128, 'ColorMap4 - Pantone 3: Blue - Red - Green'),
        (7, 4, 256, 'ColorMap4 - Pantone 3: Blue - Red - Green'),
        (8, 5, 256, 'ColorMap5 - Pantone 4: Blue - Red - Green - Yellow'),
        (9, 5, 512, 'ColorMap5 - Pantone 4: Blue - Red - Green - Yellow'),
        (10, 6, 256, 'ColorMap6 - Laser print: Orange - Light BLue - Magenta - Dark Blue - Yellow - Green - Red'),
        (11, 6, 512, 'ColorMap6 - Laser print: Orange - Light BLue - Magenta - Dark Blue - Yellow - Green - Red'),
        (12, 6, 1024, 'ColorMap6 - Laser print: Orange - Light BLue - Magenta - Dark Blue - Yellow - Green - Red'),
        (13, 7, 256, 'ColorMap7: Yellow - Pink - Green - Blue'),
        (14, 7, 512, 'ColorMap7: Yellow - Pink - Green - Blue'),
        (15, 7, 1024, 'ColorMap7: Yellow - Pink - Green - Blue'),
        (16, 8, 256, 'ColorMap8: Gray - Aquamarine - Sea Blue'),
        (17, 8, 512, 'ColorMap8: Gray - Aquamarine - Sea Blue'),
        (18, 8, 1024, 'ColorMap8: Gray - Aquamarine - Sea Blue'),
        (19, 9, 256, 'ColorMap9: Dark Pink - Mercury - Lime - Green'),
        (20, 9, 512, 'ColorMap9: Dark Pink - Mercury - Lime - Green'),
        (21, 9, 1024, 'ColorMap9: Dark Pink - Mercury - Lime - Green'),
        (22, 10, 256, 'ColorMap10 - HKS Color: Green - Yellow - Red'),
        (23, 10, 512, 'ColorMap10 - HKS Color: Green - Yellow - Red'),
        (24, 10, 1024, 'ColorMap10 - HKS Color: Green - Yellow - Red'),
        (25, 11, 256, 'ColorMap11 - HKS Colors Extend: Green - Yellow - Red - Purple'),
        (26, 11, 512, 'ColorMap11 - HKS Colors Extend: Green - Yellow - Red - Purple'),
        (27, 11, 1024, 'ColorMap11 - HKS Colors Extend: Green - Yellow - Red - Purple'),
        (28, 11, 2048, 'ColorMap11 - HKS Colors Extend: Green - Yellow - Red - Purple'),
        (29, 12, 256, 'ColorMap12: Green Sea - Blue Sea - Purple - Red - Orange - Yellow'),
        (30, 12, 512, 'ColorMap12: Green Sea - Blue Sea - Purple - Red - Orange - Yellow'),
        (31, 12, 1024, 'ColorMap12: Green Sea - Blue Sea - Purple - Red - Orange - Yellow'),
        (32, 12, 2048, 'ColorMap12: Green Sea - Blue Sea - Purple - Red - Orange - Yellow'),
        (33, 13, 256, 'ColorMap13: Green Sea - Blue Sea - Purple - Red - Orange - Yellow - Green - Yellow - Red - Purple'),
        (34, 13, 512, 'ColorMap13: Green Sea - Blue Sea - Purple - Red - Orange - Yellow - Green - Yellow - Red - Purple'),
        (35, 13, 1024, 'ColorMap13: Green Sea - Blue Sea - Purple - Red - Orange - Yellow - Green - Yellow - Red - Purple'),
        (36, 13, 2048, 'ColorMap13: Green Sea - Blue Sea - Purple - Red - Orange - Yellow - Green - Yellow - Red - Purple')])
    colorMapStyleCount = len(colorMapStyleArray)
    print('\nTotal Color Map Styles: ' + str(colorMapStyleCount))
    printtitle('#, Id, Colors, Color map style name')
    for j in range(0, colorMapStyleCount):
        print(str((colorMapStyleArray[j, 0]).zfill(2)) + ' ' + str((colorMapStyleArray[j, 1]).zfill(2)) + ' ' + str((colorMapStyleArray[j, 2].zfill(4))) + ' ' + colorMapStyleArray[j, 3])
    colorMapFileOpt = optionrange('Ramp color number', 0, (colorMapStyleCount-1))
    for k in range(0, colorMapStyleCount):
        if str(colorMapFileOpt) == str(colorMapStyleArray[k, 0]):
            colorMapFileId = colorMapStyleArray[colorMapFileOpt, 1]
            colorMapFileColors = colorMapStyleArray[colorMapFileOpt, 2]
    colorMapFile = folderColorMapStyle+'ColorMapArcGIS'+colorMapFileColors+'s'+str(colorMapFileId)+'.clr'
    colorMapFilePrev = folderColorMapStyle+'ColorMapArcGIS'+colorMapFileColors+'s'+str(colorMapFileId)+'.png'
    print('\nColor map file:', colorMapFile)
    print('Color map sample:', colorMapFilePrev)
    return (colorMapFile, colorMapFilePrev, colorMapFileColors)


# Plot text graph values between 0 and maximum value founded
# varMaxVal: Max val into all data set
# valOpt: Value to scale respect max val
def graphtxt(userFileName, totalRecord, fieldNumberEval):
    optionAswer = optionyesno('Print all records in source file as text graph')
    if optionAswer.lower() == 'y':
        printtitle('Graph text format in field # ' + str(fieldNumberEval))
        userFile = open(userFileName)
        recordLine = userFile.readline().rstrip('\n')
        varMax = -1e-99
        for i in range(0, totalRecord):
            recordLine = userFile.readline().rstrip('\n')
            recordLineArray = recordLine.split(',')
            if recordLineArray[fieldNumberEval-1] != '\n' and recordLineArray[fieldNumberEval-1] != '':
                if float(recordLineArray[fieldNumberEval-1]) > varMax:
                    varMax = float(recordLineArray[fieldNumberEval-1])
        print('Max value: ' + str(varMax))
        userFile.close()
        userFile = open(userFileName)
        recordLine = userFile.readline().rstrip('\n')
        for l in range(1, totalRecord+1):
            recordLine = userFile.readline().rstrip('\n')
            recordLineArray = recordLine.split(',')
            if recordLineArray[fieldNumberEval-1] != '\n' and recordLineArray[fieldNumberEval-1] != '':
                valOpt = float(recordLineArray[fieldNumberEval-1])
                # print('\l:',valOpt)
                barChar = '|'
                barCharMaxChar = 50
                barFactorAmpVar = 100
                barValue = ((int(valOpt*barFactorAmpVar)) * barCharMaxChar) / (int(varMax*barFactorAmpVar))
                barCharMaxCharLess = (barCharMaxChar - int(barValue))
                barValuePorc = valOpt * 100 / varMax
                barValuePrintA = barChar * int(barValue)
                barValuePrintB = ' ' * int(barCharMaxCharLess)
                print((str(l).zfill(5)) + ' [' + barValuePrintA + barValuePrintB + '] ' + str(round(valOpt, 4)) + ' of ' + str(varMax) + ' (' + str(round(barValuePorc, 1)) + '%)')
        userFile.close()
        #  print('\n')


# Plot text graph values between 0 and maximum value founded
# varMaxVal: Max val into all data set
# valOpt: Value to scale respect max val
def graphtxtonevalue(varMax, valOpt):
    varMax = float(varMax)
    barChar = '|'
    barCharMaxChar = 50
    barFactorAmpVar = 100
    barValue = ((int(valOpt*barFactorAmpVar)) * barCharMaxChar) / (int(varMax*barFactorAmpVar))
    barCharMaxCharLess = (barCharMaxChar - int(barValue))
    barValuePorc = str(round((valOpt * 100) / varMax, 2))
    print('[' + (barValue*barChar) + (barCharMaxCharLess*' ') + ']' + str(valOpt) + ' of ' + str(varMax) + ' ('+barValuePorc+'%)')
```

#### Funciones asociadas al módulo 

| Función                | Descripción                                                                                                                                                                             |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| systemprompt()         | Prompt para identificación de líneas de consola que requieren acción de usuario, se identifica como {R}.                                                                                |
| printtitle()           | Impresión de títulos con estilo de líneas superior, inferior o ambos. Permite impresión tabulada.                                                                                       |
| optionrange()          | Validación de opción de entrada de usuario para valores enteros dentro de un rango específico de valores.                                                                               |
| optionrangefloat()     | Validación de opción de entrada de usuario para valores flotantes dentro de un rango específico de valores.                                                                             |
| optionyesno()          | Validación de opción de entrada de usuario para valores respuestas con Sí (Y) o Nó (N).                                                                                                 |
| csvtotalfieldfound(()  | A partir de la ruta de localización del archivo .csv, cuenta el número de atributos o columnas disponibles.                                                                             |
| csvtotalrecordfound(() | A partir de la ruta de localización del archivo .csv, cuenta el número de registros incluida la cabecera de columna.                                                                    |
| csvspacialdomain()     | A partir de los registros contenidos en el archivo de entrada, evalúa el tamaño del dominio espacial de los datos.                                                                      |
| csvsamplerecord()      | A partir de los registros contenidos en el archivo de entrada y un número de registros indicado por el usuario, imprime una muestra de los datos de entrada incluida la cabecera.       |
| datafrecuency()        | Frecuencias disponibles para análisis para selección de usuario: Diaria o Mensual. El usuario puede elegir el número de grillas a generar a partir del tipo de frecuencia seleccionada. |
| crscoordsystem()       | Sistemas de referencia de coordenadas predeterminados para la referenciación espacial de los archivos de forma temporales y las grillas interpoladas.                                   |
| crscoordsystem()       | Sistemas de referencia de coordenadas predeterminados para la referenciación espacial de los archivos de forma temporales y las grillas interpoladas.                                   |
| csvheader()            | Lista los nombres de los atributos disponibles en el archivo de entrada y solicita al usuario el atributo a utilizar en el análisis correspondiente a la variable a interpolar.         |
| csvstatistic()         | Para la variable especificada en `csvheader()` calcula los siguientes estadísticos: Registros, Conteo no nulos, Conteo nulos, Máximo, Mínimo, Suma y Promedio.                          |
| colormapstyle()        | Lista de estilos de rampa de color seleccionables por el usuario para la representación de las grillas re-escaladas.                                                                    |
| graphtxt()             | Grafica e imprime como texto en la consola de ejecución, todos los valores discretos encontrados de la variable a analizar.                                                             |
| graphtxtonevalue(()    | Grafica e imprime como texto en la consola de ejecución, un valor definido respecto a un valor máximo establecido.                                                                      |

> La función `optionrange()` valida la entrada numérica y en caso de contener valores decimales, válida la parte entera como entrada de usuario. 

> Para las funciones `optionrange()`, `optionrangefloat()` y `optionyesno()`, en caso de que la opción ingresada no pueda ser validada o esté fuera de rango, se solicita nuevamente el valor hasta que se ingrese un valor válido.
 
> La función `optionyesno()` válida que la entrada sea una cadena de texto y evalúa si se ingresa en mayúsculas o minúsculas la opción solicitada. En Python 2 sobre ArcGIS for Desktop 10+, es necesario ingresar la respuesta entre comillas, p.ej, `'Y'`, `'y'`, `'N'` o `'n'`.

> La función `csvspacialdomain()` identifica el número de columna donde se encuentran los valores CX o longitudes y CY o latitudes; calcula el tamaño horizontal y vertical del dominio espacial y divide la menor dimensión entre 150 celdas o pixeles para sugerir el tamaño de pixel a utilizar en las interpolaciones espaciales.

> El script no presenta en la función `datafrecuency()` una opción específica para series de datos anuales, sin embargo, utilizando la frecuencia `Díaria` a partir de Julianos, se pueden generar interpolaciones hasta 366 años. Los valores de la columna `Var` o la columna numérica a representar, deberán corresponder a datos escalados a nivel anual.   

> En caso de que el usuario requiera un CRS diferente a los predeterminados en `crscoordsystem()`, en el arreglo `coordSystem` se pueden agregar nuevos sistemas o modificar los existentes. Los parámetros de entrada del CRS pueden ser obtenidos a través de un archivo .prj asociado a un archivo de formas shapefile previamente georeferenciado.

> La función `csvstatistic()` además de calcular los estadísticos generales, almacena en listas, el número de registro y los valores discretos de la variable seleccionada para su posterior graficación con `matplotlib`. 

> Las rampas de colores en formato .clr incluidas en la carpeta `ColorMapStyle` han sido creadas por r.cfdtools.


### Referencias

* https://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-functions/checkoutextension.htm
* https://stackoverflow.com/questions/7852855/in-python-how-do-you-convert-a-datetime-object-to-seconds
* https://stackoverflow.com/questions/34165941/how-to-display-tiff-file-in-color
* https://www.codegrepper.com/code-examples/python/python+2.7+datetime+to+timestamp
* https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
* https://www.tutorialspoint.com/how-to-clear-the-memory-completely-of-all-matplotlib-plots
* https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_collection.html#sphx-glr-gallery-shapes-and-collections-ellipse-collection-py
* https://matplotlib.org/stable/tutorials/colors/colormaps.html


### Compatibilidad

* Compatible con ArcGIS for Desktop 10 o superior.
* Compatible con ArcGIS Pro.


### Control de versiones

| Versión    | Descripción                                                                                                                                                                                                                                                                                                         | Autor                                     | Horas |
|------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|:-----:|
| 2022.01.07 | Actualización de módulo `TableInterpolatedGridModule.py` con nueva versión de estilos generados en https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle                                                                                                                                                 | [rcfdtools](https://github.com/rcfdtools) |  12   |
| 2022.01.02 | Inclusión de gráfica de barras para todos los datos encontrados con publicación y direccionamiento a GitHub en carpeta `/Graph` usando el código de registro Log. Generación, almacenamiento y publicación de gráfica de serie de datos y previsualización de grillas con `matplotlib` para la variable en estudio. | [rcfdtools](https://github.com/rcfdtools) |  12   |
| 2022.01.01 | Actualización de documentación, optimización de print con concatenación usando + para visualización idéntica en consola para versiones 2 y 3 de Python.                                                                                                                                                             | [rcfdtools](https://github.com/rcfdtools) |  12   |
| 2021.12.31 | Actualización para compatibilidad con Python 3 y ArcGIS Pro. Optimización de script. Log de registro.                                                                                                                                                                                                               | [rcfdtools](https://github.com/rcfdtools) |  12   |
| 2018.01.24 | Versión con módulo y funciones.                                                                                                                                                                                                                                                                                     | [rcfdtools](https://github.com/rcfdtools) |  12   |
| 2017.11.23 | Versión inicial sobre Python 2 solo compatible con ArcGIS for Desktop.                                                                                                                                                                                                                                              | [rcfdtools](https://github.com/rcfdtools) |  12   |


### Licencia, cláusulas y condiciones de uso

_R.HydroTools es de uso libre para fines académicos, conoce nuestra [licencia, cláusulas, condiciones de uso](../../LICENSE.md) y como referenciar los contenidos publicados en este repositorio._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [r.cfdtools](https://github.com/rcfdtools) en GitHub._

| [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.HydroTools/discussions/xxx) |
|-----------------------------------|------------------------------------------------------------------------------------------|

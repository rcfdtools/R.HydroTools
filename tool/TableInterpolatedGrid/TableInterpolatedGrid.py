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
logExecutionFile = open('TableInterpolatedGridLog.csv', 'a')
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
logExecutionFile.write(str(logFileNumber) + ',' + str(datetime.now()) + ',' + fileCSVIn + ',"' + str(studyCase) + '"\n')
logExecutionFile.close()
vExit = input("\n%s Type 'Y' to exit >> " % (rtg.systemprompt()))

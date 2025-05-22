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

# This script is use for plot the scatter plot graph from all the stations

# Libraries
import OpenWeatherSetup as ows
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

# General pandas and matplotlib settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 0)
mpl.rc('figure', max_open_warning = 0) # Don't show the python figure.max_open_warning
mpl.rc('font', size=10)
mpl.rc('axes', titlesize=10)
sns.set_style('white')  # darkgrid, whitegrid, dark, white, ticks

# Print in Markdown format
def printmd(txtPrint, onScreen=True):
    if onScreen: print(txtPrint)
    fileOutputMarkdown.write(txtPrint + '\n')

# Variables
dataFrameCSV = pd.read_csv(ows.filePath+'/Output/'+ows.fileCSV, encoding='ISO-8859-1')
fileNameMd = ows.fileNameCNE + '_OWM_Zonal_' + ows.currentDateTxt + '.md'
fileOutputMarkdownName = ows.filePath + '/Output/' + fileNameMd
fileOutputMarkdown = open(fileOutputMarkdownName, 'w+')
#dataFrameCSV['HourA'] = dataFrameCSV.Datetime.dt.hour
#dataFrameCSV.dropna(inplace=True)
showPlot = False # Show on screen

# General information
if ows.showHistorical:
    callType = 'Historical'
else:
    callType = 'Forecast'
printmd('\n## ' + ows.mainTitle + ' - Zonal Analysis - ' + callType +
        '\n\nStudy case: ' + ows.studyCase +
        '\n\n### GitHub repository and system information\n' +
        '\n* Python version: ' + str(sys.version) +
        '\n* Python path: ' + str(sys.path[0:5]) +
        '\n* matplotlib version: ' + str(mpl.__version__) +
        '\n* seaborn version: ' + str(sns.__version__) +
        '\n* Repository: https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather' +
        '\n* License and conditions: https://github.com/rcfdtools/R.GISPython/wiki/License' +
        '\n* Credits: r.cfdtools@gmail.com' +
        '\n\n### General parameters\n' +
        '\n* Current date time: ' + str(ows.currentDateTime) +
        '\n* Unix time to eval: ' + str(ows.timeStampVal) +
        '\n* Days before (for historical data): ' + str(ows.daysBefore) +
        '\n* Show historical: ' + str(ows.showHistorical) +
        '\n* File: ' + ows.fileCSV +
        '\n* Type: ' + str(type(dataFrameCSV)) +
        '\n* Shape: ' + str(dataFrameCSV.shape))
print('\n\nDataframe info:\n'+ str(dataFrameCSV.info()))
#print('\nRecords sample\n %s' %(str(dataFrameCSV.head())))

# Station list
stationName = dataFrameCSV['Station'].unique()
geoArrayCNE = dataFrameCSV[['Station', 'Statname', 'Latitude', 'Longitude', 'Elevation', 'Category', 'Technology', 'Status', 'State', 'County', 'Stream', 'Operator', 'AHName', 'SZName', 'SZHName']]
records = len(geoArrayCNE)
printmd('\n\n### Stations or locations list'
        '\n\nThe below table show the station or location list used for the zonal analysis display in this report for the current study case.\n')
printmd('| Station | Statname | Latitude° | Longitude°|  Elevation| Category | Technology | Status | State | County | Stream | Operator | AHName | SZName | SZHName |')
printmd('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for i in stationName:
    valid = True
    for k in range(1, records):
        if i == geoArrayCNE['Station'][k] and valid:
            fileNameMd = ows.fileNameCNE + '_Station' + str(i) + '_OWM_' + ows.currentDateTxt + '.md'
            printmd('| [%s](%s) | %s | %f | %f |  %f | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (str(i), fileNameMd, geoArrayCNE['Statname'][k], geoArrayCNE['Latitude'][k], geoArrayCNE['Longitude'][k], geoArrayCNE['Elevation'][k], geoArrayCNE['Category'][k], geoArrayCNE['Technology'][k], geoArrayCNE['Status'][k], geoArrayCNE['State'][k], geoArrayCNE['County'][k], geoArrayCNE['Stream'][k], geoArrayCNE['Operator'][k], geoArrayCNE['AHName'][k], geoArrayCNE['SZName'][k], geoArrayCNE['SZHName'][k]))
            valid = False

# Plot vars with geographic location
#sns.set(rc={'figure.figsize': (6, 6)})
printmd('\n\n### Latitude vs. Longitude Maps (relational plot)'
        '\n\nThis maps show the hourly spatial distribution for each collected weather variable from the OWM.')
for i in ows.plotParameters:
    if ows.unitSys == 'metric':
        units = i[0] + ' (' + i[1] + ')'
    else:
        units = i[0] + ' (' + i[2] + ')'
    plotName = ows.fileNameCNE + '_RelPlotMap_OWM_' + i[0] + '_' + ows.currentDateTxt + '.png'
    plotFile = ows.filePath + '/Graph/' + plotName
    plotFileGitHub = ows.urlGitHub + '/Graph/' + plotName
    # sns.relplot(x=i[0], y=i[1], hue=i[2], col=i[3], palette=i[4], data=dataFrameCSV)
    #sns.relplot(x=i[0], y=i[1], hue=i[2], col='Hour', palette=i[4], col_wrap=4, height=5, aspect=8/8, data=dataFrameCSV)
    sns.relplot(x='Longitude', y='Latitude', hue=i[0], col='Hour', palette=i[3], col_wrap=4, height=2, data=dataFrameCSV)
    #plt.title('Stations Map for ' + i[2])
    #plt.grid(color='lightgray', linestyle='-', linewidth=0.25)
    plt.savefig(plotFile)
    if showPlot: plt.show()
    printmd('\n#### ' + units + ' - Map')
    printmd('![%s](%s)' % (plotName, plotFileGitHub))

# JointPlots
iAux, jAux = 0, 0 # Variables for not repeat previous pair plots, p.ej, Temp vs. Clouds is the same as Clouds vs. Temp.
printmd('\n\n### Joint plots'
        '\n\nThis plots show the relation between the weather variables with hourly distribution from the collected data from the OWM.')
for i in ows.plotParameters:
    for j in ows.plotParameters:
        if i != j and jAux >= iAux:
            plotName = ows.fileNameCNE + '_JointPlot_OWM_' + i[0] + '_' + j[0] + '_' + ows.currentDateTxt + '.png'
            plotFile = ows.filePath + '/Graph/' + plotName
            plotFileGitHub = ows.urlGitHub + '/Graph/' + plotName
            if ows.unitSys == 'metric':
                xLabel = i[0] + ' (' + i[1] + ')'
                yLabel = j[0] + ' (' + j[1] + ')'
            else:
                xLabel = i[0] + ' (' + i[2] + ')'
                yLabel = j[0] + ' (' + j[2] + ')'
            g = sns.jointplot(data=dataFrameCSV, x=i[0], y=j[0], hue='Hour', palette='autumn', height=8, space=0, ratio=5)
            g.set_axis_labels(xlabel=xLabel, ylabel=yLabel, fontsize=11)
            plt.savefig(plotFile)
            if showPlot: plt.show()
            printmd('\n#### ' + xLabel + ' vs. ' + yLabel)
            printmd('![%s](%s)' %(plotName, plotFileGitHub))
            #print('Plotting ' + plotName)
        jAux += 1
    iAux += 1
    jAux = 0

# Plot confidence analysis
printmd('\n\n### Confidence analysis categorized'
        '\n\nThis graphs show the confidence analysis for each collected weather variable from the OWM categorized by the CNE descriptors.')
for i in ows.plotParameters:
    for j in ows.plotConfidenceHue:
        plotName = ows.fileNameCNE + '_RelPlotHue_OWM_' + i[0] + '_' + j + '_' + ows.currentDateTxt + '.png'
        plotFile = ows.filePath + '/Graph/' + plotName
        plotFileGitHub = ows.urlGitHub + '/Graph/' + plotName
        if ows.unitSys == 'metric':
            yLabel = i[0] + ' (' + i[1] + ')'
            units = i[0] + ' (' + i[1] + ')' + ' by ' + j
        else:
            yLabel = i[0] + ' (' + i[2] + ')'
            units = i[0] + ' (' + i[2] + ')' + ' by ' + j
        #g = sns.lineplot(data=dataFrameCSV, x=dataFrameCSV.Hour, y=i[0], hue=j)
        #g = sns.relplot(data=dataFrameCSV, x='Hour', y=i[0], col='Status', hue=j, kind='line')
        g = sns.relplot(data=dataFrameCSV, x='Hour', y=i[0], hue=j, kind='line', height=8, palette='autumn')
        #plt.title('Confidence analysis')
        g.set_axis_labels(ylabel=yLabel, fontsize=11)
        plt.xticks(np.arange(0, 24, 1.0))
        plt.grid(color='lightgray', linestyle='-', linewidth=0.25)
        plt.savefig(plotFile)
        if showPlot: plt.show()
        printmd('\n#### ' + units + ' - Confidence analysis')
        printmd('![%s](%s)' % (plotName, plotFileGitHub))

print('\n{R} Process completed.')
printmd('\n\n_¡Encontraste útil este microcontenido!, apoya su difusión marcando este repositorio con una estrella!_')

# Test
#sns.relplot(x='Temp', y='Humidity', hue='Humidity', col='Hour', palette='viridis_r', col_wrap=4, height=2, data=dataFrameCSV)

#sns.kdeplot(x=dataFrameCSV.Latitude, y=dataFrameCSV.Longitude, shade=True, cbar=True)
#showPlot: plt.show()

# -*- coding: UTF-8 -*-
# Script name: OpenWeatherPlot.py
# Description: Plot weather values for the IDEAM National Station Catalog - CNE from OWM
# Requirements: Python 3.10.0, matplotlib 3.5.0

# Libraries
import OpenWeatherSetup as ows
import sys
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# General pandas and matplotlib settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 0)
mpl.rc('figure', max_open_warning = 0) # Don't show the python figure.max_open_warning
mpl.rc('font', size=10)
mpl.rc('axes', titlesize=10)
mpl.use("Agg")  # Prevent the error: Fail to create pixmap with Tk_GetPixmap in TkImgPhotoInstanceSetSize. Don't use with seaborn

# Variables
graphTransparency = 0.75 # Save color for paper print versions, 1 for full color. Doesn't apply for pie charts
showGraphScreen = False
dataFrameCSV = pd.read_csv(ows.filePath+'/Output/'+ows.fileCSV, encoding='ISO-8859-1')

# Collection data analysis from CSV file
print('\n## ' + ows.mainTitle)
print('\n* Python version: ' + str(sys.version) +
      '\n* Python path: ' + str(sys.path[0:5]) +
      '\n* matplotlib version: ' + str(mpl.__version__) +
      '\n* Repository: https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather' +
      '\n* License and conditions: https://github.com/rcfdtools/R.GISPython/wiki/License' +
      '\n* Credits: r.cfdtools@gmail.com')
print('\n### Collection data analysis\n'
      '\n* Dataframe type: '+str(type(dataFrameCSV)),
      '\n* Records: ' + str(dataFrameCSV.shape[0]) +
      '\n* Attributes: ' + str(dataFrameCSV.shape[1]))
print('\n### General CSV information\n')
print(dataFrameCSV.info())
print('\n### Plot hourly graph\n')
stationList = dataFrameCSV['Station'].unique()
for i in stationList:
    for parameter in ows.plotParameters:
        dataFrameCSVFilter = dataFrameCSV[dataFrameCSV['Station'] == i]
        plotFile = ows.filePath + '/Graph/' + ows.fileNameCNE + '_Station' + str(i) + '_OWM_' + parameter[0] + '_' + ows.currentDateTxt + '.png'
        print('* Hourly graph - ' + str(i) + ': ' + plotFile)
        mainArray = dataFrameCSVFilter[
            ['Station', 'Statname', 'Clouds', 'Dewpoint', 'Feelslike', 'Humidity', 'Pressure', 'Rain', 'Temp', 'UVI', 'Visibility', 'Winddeg','Windgust', 'Windspeed', 'Hour', 'Datetime']]
        #print(dataFrameCSVFilter['Datetime'])
        #print(mainArray)
        if ows.unitSys == 'metric':
            ylabelvar = parameter[0] + ', ' + parameter[1]
        else:
            ylabelvar = parameter[0] + ', ' + parameter[2]
        plotTitle = 'Station ' + str(i)
        plotLine = mainArray.plot.line(xlabel='Hour', ylabel=ylabelvar ,  x='Hour', y=parameter[0],title=plotTitle, figsize=(5, 4), c='k', grid=False, marker=".", markersize=8, alpha=graphTransparency)
        plt.grid(color='lightgray', linestyle='-', linewidth=0.25)
        plt.yticks(rotation=0)
        plt.xticks(rotation=90)
        #plt.xlim(0, 23)
        plt.xticks(np.arange(0, 24, 1.0))
        plt.savefig(plotFile)
        if showGraphScreen == True: plt.show()
        plt.close('all')



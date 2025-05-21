# -*- coding: UTF-8 -*-
# Script name: OpenWeather.py
# Description: Weather values for the IDEAM National Station Catalog - CNE from OWM
# Requirements: Python 3.10.0, matplotlib 3.5.0
# API data from https://openweathermap.org/

# Libraries
import os
import requests
import json
import time
import sys
import pandas as pd
from pprint import pprint
from datetime import datetime
import matplotlib as mpl
import OpenWeatherSetup as ows

# Markdown header separator table function
def tableseparatormarkdown(n=2):
    lineSep = '|---'
    printmd(lineSep * n + '|', True)

# Print in CSV format
def printcsv(txtPrint, onScreen=True):
    if onScreen: print(txtPrint)
    fileOutputCSV.write(txtPrint + '\n')

# Print in Markdown format
def printmd(txtPrint, onScreen=True):
    if onScreen: print(txtPrint)
    fileOutputMarkdown.write(txtPrint + '\n')

# Variables
apiKey = '**********************'  # Your OWM API key code here
timeStart = time.time()
unitVal = [  # Parameter, unit metric system, unit imperial system, openweathermap name.
    ('Temperature', '°C', '°F', 'temp'),
    ('Dew Point', '°C', '°F', 'dew_point'),
    ('Feels like', '°C', '°F', 'feels_like'),
    ('Clouds', '%', '%', 'clouds'),
    ('Humidity', '%', '%', 'humidity'),
    ('Pressure', 'hPa', 'hPa', 'pressure'),
    ('Wind Direction', '°', '°', 'wind_deg'),
    ('Wind Speed', 'm/s', 'mi/h', 'wind_speed'),
    ('Wind Gust', 'm/s', 'mi/h', 'wind_gust'),
    ('Rain', 'mm', 'mm', 'rain'),
    ('Visibility','m', 'm', 'visibility'),
    ('UV Index','DN', 'DN', 'uvi')]
csvParameters = [  # Parameter names for the output CSV file: r.cfdtools, IDEAM, OpenWeather.
    ('Station', 'CODIGO', 'N/A', 'Station code'),
    ('Statname', 'nombre', 'N/A', 'Station name'),
    ('Latitude', 'latitud', 'lat', 'Geolocation latitude degrees'),
    ('Longitude', 'longitud' ,'lon', 'Geolocation longitude degrees'),
    ('Elevation', 'altitud', 'N/A', 'Elevation over the sea level'),
    ('Category', 'CATEGORIA', 'N/A', 'Station category: pluviometric, limnimetric, pluviograph, limnigraph, ordinary climatology, principal climatology, special meteorologic, soil meteorological, main synoptic, secundary synotic, radiosonde, mareographic'),
    ('Technology', 'TECNOLOGIA', 'N/A', 'Main technology: conventional, automatic assisted with telemetry, automatic not assisted with telemetry'),
    ('Status', 'ESTADO', 'N/A', 'Functional status: active, suspended, under maintenance'),
    ('InstDate', 'FECHA_INSTALACION', 'N/A', 'Installation date'),
    ('SuspDate', 'FECHA_SUSPENSION', 'N/A', 'Suspension date'),
    ('State', 'DEPARTAMENTO', 'N/A', 'Geopolitical location state'),
    ('County', 'MUNICIPIO', 'N/A', 'Geopolitical location county'),
    ('Stream', 'CORRIENTE', 'N/A', 'Stream point or near stream'),
    ('Operator', 'AREA_OPERATIVA', 'N/A', 'Gouvernament operator'),
    ('AHName', 'AREA_HIDROGRAFICA', 'N/A', 'AH - Hydrographic area. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone)'),
    ('SZName', 'ZONA_HIDROGRAFICA', 'N/A', 'ZH - Hydrographic zone. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone)'),
    ('SZHName', 'SUBZONA_HIDROGRAFICA', 'N/A', 'SZH - Hydrographic subzone. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone)'),
    ('Timezone', 'N/A', 'timezone', 'Global time zone'),
    ('Datetime', 'N/A', 'N/A', 'Date and time of the weather values'),
    ('Clouds', 'N/A', 'clouds', 'Cloudiness'),
    ('Dewpoint', 'N/A', 'dew_point', 'Atmospheric temperature (varying according to pressure and humidity) below which water droplets begin to condense and dew can form.'),
    ('Feelslike', 'N/A', 'feels_like', 'Temperature. This temperature parameter accounts for the human perception of weather'),
    ('Humidity', 'N/A', 'humidity', 'Humidity'),
    ('Pressure', 'N/A', 'pressure', 'Atmospheric pressure on the sea level'),
    ('Rain', 'N/A', 'rain', 'Rain volume for last hour'),
    ('Temp', 'N/A', 'temp', 'Temperature'),
    ('UVI', 'N/A', 'uvi', 'Current UV index'),
    ('Visibility', 'N/A', 'visibility', 'Average visibility'),
    ('Winddeg', 'N/A', 'wind_deg', 'Wind direction, degrees (meteorological)'),
    ('Windgust', 'N/A', 'wind_gust', 'Wind gust'),
    ('Windspeed', 'N/A', 'wind_speed', 'Wind speed'),
    ('OWMid', 'N/A', 'id', 'Weather identification over OWM'),
    ('OWMmain', 'N/A', 'main', 'Group of weather parameters (Rain, Snow, Extreme etc.)'),
    ('OWMdesc', 'N/A', 'description', 'Weather condition within the group. [More info.](https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2)'),
    ('OWMicon', 'N/A', 'icon', 'Weather icon id. [More info.](https://openweathermap.org/weather-conditions#How-to-get-icon-URL)'),
    ('Hour', 'N/A', 'N/A', 'Hour can be used like a Pseudo julian value for spatial intepolation. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/TableInterpolatedGrid)')]
urlFileCNE = 'http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls'
fileExtensionCNE = '.xls'
stationCodeCNE = 'CODIGO'
stationNameCNE = 'nombre'
latitudeCNE = 'latitud'
longitudeCNE = 'longitud'
elevationNameCNE = 'altitud'
categoryNameCNE = 'CATEGORIA'
technologyNameCNE = 'TECNOLOGIA'
statusNameCNE = 'ESTADO'
installationDateCNE = 'FECHA_INSTALACION'
suspensionDateCNE = 'FECHA_SUSPENSION'
geoStateNameCNE = 'DEPARTAMENTO'
geoCountyNameCNE = 'MUNICIPIO'
geoStreamNameCNE = 'CORRIENTE'
geoOperativeAreaNameCNE = 'AREA_OPERATIVA'
geoHydroAreaNameCNE = 'AREA_HIDROGRAFICA'
geoHydroZoneNameCNE = 'ZONA_HIDROGRAFICA'
geoHydroSubZoneNameCNE = 'SUBZONA_HIDROGRAFICA'
urlIcon = 'http://openweathermap.org/img/w/'
printDetail = True  # Print JSON dictionary on screen and Markdown files
updateCNEFile = True  # Download the IDEAM CNE file
requestOWMData = True  # Get API responses

# General filter variables related with the currente CNE IDEAM metadata file
# May you consider that for free OWM accounts, you can only get 1000 API responses every day.
# More information: https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic
stationCodeFilter = ['All', 26055120, 1508500053]  # 'All' at the first position or your required values.
categoryFilter = ['All']  # 'All' at the first position or 'Pluviométrica', 'Limnimétrica', 'Limnigráfica', 'Climática Ordinaria', 'Climática Principal', 'Pluviográfica', 'Meteorológica Especial', 'Agrometeorológica', 'Sinóptica Principal', 'Radio Sonda', 'Mareográfica', 'Sinóptica Secundaria'.
technologyFilter = ['All', 'Automática sin Telemetría']  # 'All' at the first position or your required values or 'Automática con Telemetría', 'Automática sin Telemetría', 'Convencional'
statusFilter = ['All', 'Activa', 'En Mantenimiento']  # 'All' at the first position or 'Activa', 'En Mantenimiento', 'Suspendida'
geoStateFilter = ['Bogotá']  # 'All' at the first position or your required values or e.g. 'Cundinamarca', 'Boyacá', 'Cesar'...
geoCountyFilter = ['All']  # 'All' at the first position or your required values.
geoStreamFilter = ['All']  # 'All' at the first position or your required values.
geoOperativeAreaFilter = ['All']  # 'All' at the first position or your required values.
geoHydroAreaFilter = ['All']  # 'All' at the first position or your required values or e.g. 'Amazonas', 'Caribe', 'Magdalena Cauca', 'Orinoco', 'Pacifico'
geoHydroZoneFilter = ['All']  # 'All' at the first position or your required values.
geoHydroSubZoneFilter = ['All']  # 'All' at the first position or your required values.

# General pandas and matplotlib settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 0)
mpl.rc('figure', max_open_warning = 0) # Don't show the python figure.max_open_warning

# Downloading and reading the CNE file
fileSaveCNE = ows.filePath+'/Data/'+ows.fileNameCNE+'_'+ows.currentDateTxt+fileExtensionCNE
fileOutputCSV = open(ows.filePath+'/Output/'+ows.fileCSV, 'w+')
fileDownloadText = 'CNE IDEAM file downloaded and updated: No'
if updateCNEFile:
    fileRequest = requests.get(urlFileCNE)
    if fileRequest:
        if os.path.isfile(fileSaveCNE) == False:
            open(fileSaveCNE, 'wb').write(fileRequest.content)
            fileDownloadText = 'CNE IDEAM file downloaded and updated: Yes'
else:
    open(fileSaveCNE)
    fileDownloadText = 'CNE IDEAM file downloaded and updated: No'
stationTableCNE = pd.read_excel(fileSaveCNE, index_col=0, sheet_name='CNE')
pd.set_option('display.max_rows', stationTableCNE.shape[0]+1)  # Show all the records
pd.set_option('display.max_columns', None)  # Show all the records

# Show CNE records and weather values
numStationsCNE = stationTableCNE.shape[0]  # numStationsCNE = 10
if ows.showHistorical:
    callType = 'Historical'
else:
    callType = 'Forecast'

# Print and export CNE stations and weather parameters
geoArrayCNE = stationTableCNE[[stationCodeCNE, stationNameCNE, latitudeCNE, longitudeCNE, elevationNameCNE, categoryNameCNE, technologyNameCNE, statusNameCNE, installationDateCNE, suspensionDateCNE, geoStateNameCNE, geoCountyNameCNE, geoStreamNameCNE, geoOperativeAreaNameCNE, geoHydroAreaNameCNE, geoHydroZoneNameCNE, geoHydroSubZoneNameCNE]]
csvHeader = 'Station,Statname,Latitude,Longitude,Elevation,Category,Technology,Status,InstDate,SuspDate,State,County,Stream,Operator,AHName,SZName,SZHName,Timezone,Datetime,Clouds,Dewpoint,Feelslike,Humidity,Pressure,Rain,Temp,UVI,Visibility,Winddeg,Windgust,Windspeed,OWMid,OWMmain,OWMdesc,OWMicon,Hour'
printcsv(csvHeader, False)
countStationsEval = 0
for i in range(1, numStationsCNE+1):
    if (geoArrayCNE[stationCodeCNE][i] in stationCodeFilter or stationCodeFilter[0] == 'All') and (geoArrayCNE[categoryNameCNE][i] in categoryFilter or categoryFilter[0] == 'All') and (geoArrayCNE[technologyNameCNE][i] in technologyFilter or technologyFilter[0] == 'All') and (geoArrayCNE[statusNameCNE][i] in statusFilter or statusFilter[0] == 'All') and (geoArrayCNE[geoStateNameCNE][i] in geoStateFilter or geoStateFilter[0] == 'All') and (geoArrayCNE[geoCountyNameCNE][i] in geoCountyFilter or geoCountyFilter[0] == 'All') and (geoArrayCNE[geoStreamNameCNE][i] in geoStreamFilter or geoStreamFilter[0] == 'All') and (geoArrayCNE[geoOperativeAreaNameCNE][i] in geoOperativeAreaFilter or geoOperativeAreaFilter[0] == 'All') and (geoArrayCNE[geoHydroAreaNameCNE][i] in geoHydroAreaFilter or geoHydroAreaFilter[0] == 'All') and (geoArrayCNE[geoHydroZoneNameCNE][i] in geoHydroZoneFilter or geoHydroZoneFilter[0] == 'All') and (geoArrayCNE[geoHydroSubZoneNameCNE][i] in geoHydroSubZoneFilter or geoHydroSubZoneFilter[0] == 'All'):
        fileNameMd = ows.fileNameCNE + '_Station' + str(geoArrayCNE[stationCodeCNE][i]) +'_OWM_' + ows.currentDateTxt + '.md'
        fileGitHub = ows.urlGitHub + '/Output/' + fileNameMd
        fileOutputMarkdownName = ows.filePath + '/Output/' + fileNameMd
        fileOutputMarkdown = open(fileOutputMarkdownName, 'w+')
        printmd('\n## ' + ows.mainTitle + ' - ' + str(geoArrayCNE[stationNameCNE][i]) + ' - ' + callType)
        printmd('\nStudy case: ' + ows.studyCase +
                '\n\n### GitHub repository and system information\n' +
                '\n* Python version: ' + str(sys.version) +
                '\n* Python path: ' + str(sys.path[0:5]) +
                '\n* matplotlib version: ' + str(mpl.__version__) +
                '\n* Repository: https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather' +
                '\n* License and conditions: https://github.com/rcfdtools/R.GISPython/wiki/License' +
                '\n* Credits: r.cfdtools@gmail.com' +
                '\n\n### General parameters\n' +
                '\n* Current date time: ' + str(ows.currentDateTime) +
                '\n* Unix time to eval: ' + str(ows.timeStampVal) +
                '\n* Days before (for historical data): ' + str(ows.daysBefore) +
                '\n* Show historical: ' + str(ows.showHistorical) +
                '\n* Show OWM API detail: ' + str(printDetail) +
                '\n* Request OWM data: ' + str(requestOWMData) +
                '\n* Unit system: ' + ows.unitSys +
                '\n* Icons source: ' + urlIcon +
                '\n* CNE IDEAM source: ' + urlFileCNE +
                '\n* CNE IDEAM file: ' + str(fileSaveCNE) +
                '\n* ' + str(fileDownloadText) +
                '\n* CNE IDEAM stations: ' + str(numStationsCNE) +
                '\n* CNE IDEAM attributes: ' + str(stationTableCNE.shape[1]) +
                '\n* CNE IDEAM station code filter: ' + str(stationCodeFilter) +
                '\n* CNE IDEAM category filter: ' + str(categoryFilter) +
                '\n* CNE IDEAM technology filter: ' + str(technologyFilter) +
                '\n* CNE IDEAM status filter: ' + str(statusFilter) +
                '\n* CNE IDEAM state filter: ' + str(geoStateFilter) +
                '\n* CNE IDEAM county filter: ' + str(geoCountyFilter) +
                '\n* CNE IDEAM stream filter: ' + str(geoStreamFilter) +
                '\n* CNE IDEAM operator filter: ' + str(geoOperativeAreaFilter) +
                '\n* CNE IDEAM hydro area filter: ' + str(geoHydroAreaFilter) +
                '\n* CNE IDEAM hydro zone filter: ' + str(geoHydroZoneFilter) +
                '\n* CNE IDEAM hydro subzone filter: ' + str(geoHydroSubZoneFilter) +
                '\n* Related files: [Station Markdown, ](' + fileGitHub + ')' + '[General CSV]( ' + ows.urlGitHub + '/Output/' + ows.fileCSV + ')' )
        printmd('\n> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. ')
        printmd('\n> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. ')
        printmd('\n#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=' + str(geoArrayCNE[latitudeCNE][i]) + ',' + str(
            geoArrayCNE[longitudeCNE][i]) + ') or [Openstreet Map](https://www.openstreetmap.org/query?lat=' + str(
            geoArrayCNE[latitudeCNE][i]) + '&lon=' + str(geoArrayCNE[longitudeCNE][i]) + ')')
        printmd('\n| Parameter | Value |' +
                '\n|---|---|' +
                '\n| Code | ' + str(geoArrayCNE[stationCodeCNE][i]) + ' |'
                '\n| Name | ' + str(geoArrayCNE[stationNameCNE][i]) + ' |'
                '\n| Latitude, ° | ' + str(geoArrayCNE[latitudeCNE][i]) + ' |'
                '\n| Longitude, ° | ' + str(geoArrayCNE[longitudeCNE][i]) + ' |'
                '\n| Elevation, m | ' + str(geoArrayCNE[elevationNameCNE][i]) + ' |'
                '\n| Category | ' + str(geoArrayCNE[categoryNameCNE][i]) + ' |'
                '\n| Technology | ' + str(geoArrayCNE[technologyNameCNE][i]) + ' |'
                '\n| Status | ' + str(geoArrayCNE[statusNameCNE][i]) + ' |'
                '\n| Installation date | ' + str(geoArrayCNE[installationDateCNE][i]) + ' |'
                '\n| Suspension date | ' + str(geoArrayCNE[suspensionDateCNE][i]) + ' |'
                '\n| State | ' + str(geoArrayCNE[geoStateNameCNE][i]) + ' |'
                '\n| County | ' + str(geoArrayCNE[geoCountyNameCNE][i]) + ' |'
                '\n| Stream | ' + str(geoArrayCNE[geoStreamNameCNE][i]) + ' |'
                '\n| Operator | ' + str(geoArrayCNE[geoOperativeAreaNameCNE][i]) + ' |'
                '\n| AH - Hydrographic area | ' + str(geoArrayCNE[geoHydroAreaNameCNE][i]) + ' |'
                '\n| ZH - Hydrographic zone | ' + str(geoArrayCNE[geoHydroZoneNameCNE][i]) + ' |'
                '\n| SZH - Hydrographic subzone | ' + str(geoArrayCNE[geoHydroSubZoneNameCNE][i]) + ' |')
        printmd(
            '\n> For `Show historical`, `True` means that we are getting weather historic values with the `Time Machine` option from the openweathermap server, `False` means that we are getting the `Forecast` weather values.')

        # Print units system
        printmd('\n#### Unit system (%s)\n' % (ows.unitSys))
        printmd('| Parameter | Unit metric system | Unit imperial system | openweathermap name |')
        tableseparatormarkdown(4)
        for ii in unitVal:
            printmd('| %s | %s | %s | %s |' % (ii[0], ii[1], ii[2], ii[3]))
        printmd('\n> mi: Miles unit for imperial system')
        printmd('\n> DN: Dimensionless numbers')

        # Print CSV parameters
        printmd('\n#### File parameters over the generated comma separated values - CSV\n')
        printmd('| r.cfdtools | CNE IDEAM | OpenWeather | Description |')
        tableseparatormarkdown(4)
        for jj in csvParameters:
            printmd('| %s | %s | %s | %s |' % (jj[0], jj[1], jj[2], jj[3]))
        printmd('\n> Some definitions are taken from https://openweathermap.org/')
        printmd(
            '\n> N/A: Does not apply. Some parameters become from the IDEAM CNE file or from the openweathermap dictionary API')

        # Print API URL data
        printmd('\n### (CNE index %s) Open Weather values for station %s - %s' % (str(i), str(geoArrayCNE[stationCodeCNE][i]), str(geoArrayCNE[stationNameCNE][i])))
        if ows.showHistorical:
            url = 'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=%f&lon=%f&dt=%i&units=%s&appid=%s' % (geoArrayCNE[latitudeCNE][i], geoArrayCNE[longitudeCNE][i], ows.timeStampVal, ows.unitSys, apiKey)
        else:
            url = 'https://api.openweathermap.org/data/2.5/onecall?lat=%f&lon=%f&&units=%s&appid=%s' % (geoArrayCNE[latitudeCNE][i], geoArrayCNE[longitudeCNE][i], ows.unitSys, apiKey)
        print('\nURL: ' + url)
        if requestOWMData:
            response = requests.get(url)
            data = json.loads(response.text)
            # Print API JSON data dictionary
            if printDetail:
                print('\nType: ' + str(type(data)))
                print('\nPrimary keys:')
                for l in data:
                    print('  ' + str(l))
                printmd('\nJSON data from API OWM:')
                printmd('\n```')
                printmd(str(data), True)
                #pprint(data)  # Print with format but not into Markdown file
                printmd('\n```')
                print('Temperature at same today time: ' + str(data['current']['temp']))

            # CSV conversion
            hourly = data['hourly']
            printmd('\n| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |', True)
            tableseparatormarkdown(37)
            for entry in hourly:
                if 'rain' in entry:
                    rain = entry['rain']['1h']
                else:
                    rain = ''
                if 'wind_gust' in entry:
                    wind_gust = entry['wind_gust']
                else:
                    wind_gust = ''
                weather = entry['weather'][0]
                csvHeader = 'Station,Statname,Latitude,Longitude,Elevation,Category,Technology,Status,InstDate,SuspDate,State,County,Stream,Operator,AHName,SZName,SZHName,Timezone,Datetime,Clouds,Dewpoint,Feelslike,Humidity,Pressure,Rain,Temp,UVI,Visibility,Winddeg,Windgust,Windspeed,OWMid,OWMmain,OWMdesc,OWMicon,Hour'
                txtPrintCSV = '%s,"%s",%f,%f,%f,"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",%s,%s,%f,%f,%f,%f,%f,%s,%f,%f,%f,%f,%s,%f,%i,%s,%s,%s,%s' % (str(geoArrayCNE[stationCodeCNE][i]), geoArrayCNE[stationNameCNE][i], geoArrayCNE[latitudeCNE][i], geoArrayCNE[longitudeCNE][i], geoArrayCNE[elevationNameCNE][i], geoArrayCNE[categoryNameCNE][i], geoArrayCNE[technologyNameCNE][i], geoArrayCNE[statusNameCNE][i], geoArrayCNE[installationDateCNE][i], geoArrayCNE[suspensionDateCNE][i], geoArrayCNE[geoStateNameCNE][i], geoArrayCNE[geoCountyNameCNE][i], geoArrayCNE[geoStreamNameCNE][i], geoArrayCNE[geoOperativeAreaNameCNE][i], geoArrayCNE[geoHydroAreaNameCNE][i], geoArrayCNE[geoHydroZoneNameCNE][i], geoArrayCNE[geoHydroSubZoneNameCNE][i], data['timezone'], datetime.utcfromtimestamp(entry['dt']).strftime('%Y-%m-%d %H:%M:%S'), entry['clouds'], entry['dew_point'], entry['feels_like'], entry['humidity'], entry['pressure'], rain, entry['temp'], entry['uvi'], entry['visibility'], entry['wind_deg'], wind_gust, entry['wind_speed'], weather['id'] , weather['main'], weather['description'], weather['icon'], datetime.utcfromtimestamp(entry['dt']).strftime('%H'))
                #txtPrintCSV = '%s' % (str(geoArrayCNE[stationCodeCNE][i]))
                printcsv(txtPrintCSV, False)
                iconShow = '!['+weather['icon']+'.png]('+urlIcon+weather['icon']+'.png)'
                txtPrintMd = '| %s | %s | "%s" | %f | %f | %f | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %f | %f | %f | %f | %f | %s | %f | %f | %f | %f | %s | %f | %i | %s | %s | %s | %s |' % (iconShow, str(geoArrayCNE[stationCodeCNE][i]), geoArrayCNE[stationNameCNE][i], geoArrayCNE[latitudeCNE][i], geoArrayCNE[longitudeCNE][i], geoArrayCNE[elevationNameCNE][i], geoArrayCNE[categoryNameCNE][i], geoArrayCNE[technologyNameCNE][i], geoArrayCNE[statusNameCNE][i], geoArrayCNE[installationDateCNE][i], geoArrayCNE[suspensionDateCNE][i], geoArrayCNE[geoStateNameCNE][i], geoArrayCNE[geoCountyNameCNE][i], geoArrayCNE[geoStreamNameCNE][i], geoArrayCNE[geoOperativeAreaNameCNE][i], geoArrayCNE[geoHydroAreaNameCNE][i], geoArrayCNE[geoHydroZoneNameCNE][i], geoArrayCNE[geoHydroSubZoneNameCNE][i], data['timezone'], datetime.utcfromtimestamp(entry['dt']).strftime('%Y-%m-%d %H:%M:%S'), entry['clouds'], entry['dew_point'], entry['feels_like'], entry['humidity'], entry['pressure'], rain, entry['temp'], entry['uvi'], entry['visibility'], entry['wind_deg'], wind_gust, entry['wind_speed'], weather['id'] , weather['main'], weather['description'], weather['icon'], datetime.utcfromtimestamp(entry['dt']).strftime('%H'))
                printmd(txtPrintMd, True)

            # Graph list
            printmd('\n\n### Weather plots\n')
            for parameter in ows.plotParameters:
                plotName = ows.fileNameCNE + '_Station' + str(geoArrayCNE[stationCodeCNE][i]) + '_OWM_' + parameter[0] + '_' + ows.currentDateTxt + '.png'
                plotFile = ows.urlGitHub + '/Graph/' + plotName
                printmd('![' + str(plotName) + '](' + str(plotFile) + ')')
        countStationsEval += 1
fileOutputCSV.close()
timeEnd = time.time()

print('\n### Summary\n' +
      '\n* Stations filtered and processed: ' + str(countStationsEval) +
      '\n* Percentage stations (' + str(countStationsEval) + '/' + str(numStationsCNE) + '): ' + str(round(countStationsEval/numStationsCNE*100, 2)) + '%'
      '\n* Process accomplished (dt = ' + str(round(timeEnd - timeStart, 1)) + 'sec or ' + str(round((timeEnd - timeStart)/60, 1)) + 'min)')

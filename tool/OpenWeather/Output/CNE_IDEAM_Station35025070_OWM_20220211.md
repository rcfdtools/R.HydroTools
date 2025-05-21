
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - TAQUES LOS [35025070] - Historical

Study case: Weather evaluation from historical openweathermap data for the CNE IDEAM network stations in Bogotá - Colombia - Suramérica

### GitHub repository and system information

* Python version: 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)]
* Python path: ['D:\\R.GISPython\\OpenWeather', 'D:\\R.GISPython', 'D:\\R.GISPython.wiki', 'C:\\Python310\\python310.zip', 'C:\\Python310\\DLLs']
* matplotlib version: 3.5.1
* Repository: https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather
* License and conditions: https://github.com/rcfdtools/R.GISPython/wiki/License
* Credits: r.cfdtools@gmail.com

### General parameters

* Current date time: 2022-02-11 17:24:58.576252
* Unix time to eval: 1644427498
* Days before (for historical data): 2
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220211.xls
* CNE IDEAM file downloaded and updated: Yes
* CNE IDEAM stations: 4499
* CNE IDEAM attributes: 20
* CNE IDEAM station code filter: ['All', 26055120, 1508500053]
* CNE IDEAM category filter: ['All']
* CNE IDEAM technology filter: ['All', 'Automática sin Telemetría']
* CNE IDEAM status filter: ['All', 'Activa', 'En Mantenimiento']
* CNE IDEAM state filter: ['Bogotá']
* CNE IDEAM county filter: ['All']
* CNE IDEAM stream filter: ['All']
* CNE IDEAM operator filter: ['All']
* CNE IDEAM hydro area filter: ['All']
* CNE IDEAM hydro zone filter: ['All']
* CNE IDEAM hydro subzone filter: ['All']
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35025070_OWM_20220211.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220211.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.19666667,-74.19094444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.19666667&lon=-74.19094444)

| Parameter | Value |
|---|---|
| Code | 35025070 |
| Name | TAQUES LOS [35025070] |
| Latitude, ° | 4.19666667 |
| Longitude, ° | -74.19094444 |
| Elevation, m | 3150 |
| Category | Pluviométrica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1986-01-14 19:00:00 |
| Suspension date | NaT |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | 0 |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Río Guayuriba |

> For `Show historical`, `True` means that we are getting weather historic values with the `Time Machine` option from the openweathermap server, `False` means that we are getting the `Forecast` weather values.

#### Unit system (metric)

| Parameter | Unit metric system | Unit imperial system | openweathermap name |
|---|---|---|---|
| Temperature | °C | °F | temp |
| Dew Point | °C | °F | dew_point |
| Feels like | °C | °F | feels_like |
| Clouds | % | % | clouds |
| Humidity | % | % | humidity |
| Pressure | hPa | hPa | pressure |
| Wind Direction | ° | ° | wind_deg |
| Wind Speed | m/s | mi/h | wind_speed |
| Wind Gust | m/s | mi/h | wind_gust |
| Rain | mm | mm | rain |
| Visibility | m | m | visibility |
| UV Index | DN | DN | uvi |

> mi: Miles unit for imperial system

> DN: Dimensionless numbers

#### File parameters over the generated comma separated values - CSV

| r.cfdtools | CNE IDEAM | OpenWeather | Description |
|---|---|---|---|
| Station | CODIGO | N/A | Station code |
| Statname | nombre | N/A | Station name |
| Latitude | latitud | lat | Geolocation latitude degrees |
| Longitude | longitud | lon | Geolocation longitude degrees |
| Elevation | altitud | N/A | Elevation over the sea level |
| Category | CATEGORIA | N/A | Station category: pluviometric, limnimetric, pluviograph, limnigraph, ordinary climatology, principal climatology, special meteorologic, soil meteorological, main synoptic, secundary synotic, radiosonde, mareographic |
| Technology | TECNOLOGIA | N/A | Main technology: conventional, automatic assisted with telemetry, automatic not assisted with telemetry |
| Status | ESTADO | N/A | Functional status: active, suspended, under maintenance |
| InstDate | FECHA_INSTALACION | N/A | Installation date |
| SuspDate | FECHA_SUSPENSION | N/A | Suspension date |
| State | DEPARTAMENTO | N/A | Geopolitical location state |
| County | MUNICIPIO | N/A | Geopolitical location county |
| Stream | CORRIENTE | N/A | Stream point or near stream |
| Operator | AREA_OPERATIVA | N/A | Gouvernament operator |
| AHName | AREA_HIDROGRAFICA | N/A | AH - Hydrographic area. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone) |
| SZName | ZONA_HIDROGRAFICA | N/A | ZH - Hydrographic zone. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone) |
| SZHName | SUBZONA_HIDROGRAFICA | N/A | SZH - Hydrographic subzone. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone) |
| Timezone | N/A | timezone | Global time zone |
| Datetime | N/A | N/A | Date and time of the weather values |
| Clouds | N/A | clouds | Cloudiness |
| Dewpoint | N/A | dew_point | Atmospheric temperature (varying according to pressure and humidity) below which water droplets begin to condense and dew can form. |
| Feelslike | N/A | feels_like | Temperature. This temperature parameter accounts for the human perception of weather |
| Humidity | N/A | humidity | Humidity |
| Pressure | N/A | pressure | Atmospheric pressure on the sea level |
| Rain | N/A | rain | Rain volume for last hour |
| Temp | N/A | temp | Temperature |
| UVI | N/A | uvi | Current UV index |
| Visibility | N/A | visibility | Average visibility |
| Winddeg | N/A | wind_deg | Wind direction, degrees (meteorological) |
| Windgust | N/A | wind_gust | Wind gust |
| Windspeed | N/A | wind_speed | Wind speed |
| OWMid | N/A | id | Weather identification over OWM |
| OWMmain | N/A | main | Group of weather parameters (Rain, Snow, Extreme etc.) |
| OWMdesc | N/A | description | Weather condition within the group. [More info.](https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2) |
| OWMicon | N/A | icon | Weather icon id. [More info.](https://openweathermap.org/weather-conditions#How-to-get-icon-URL) |
| Hour | N/A | N/A | Hour can be used like a Pseudo julian value for spatial intepolation. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/TableInterpolatedGrid) |

> Some definitions are taken from https://openweathermap.org/

> N/A: Does not apply. Some parameters become from the IDEAM CNE file or from the openweathermap dictionary API

### (CNE index 1864) Open Weather values for station 35025070 - TAQUES LOS [35025070]

JSON data from API OWM:

```
{'lat': 4.1967, 'lon': -74.1909, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644427498, 'sunrise': 1644405119, 'sunset': 1644448205, 'temp': 14.57, 'feels_like': 14.3, 'pressure': 1016, 'humidity': 85, 'dew_point': 12.08, 'uvi': 12.94, 'clouds': 100, 'visibility': 6544, 'wind_speed': 0.26, 'wind_deg': 80, 'wind_gust': 1.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644364800, 'temp': 7.57, 'feels_like': 7.57, 'pressure': 1017, 'humidity': 96, 'dew_point': 6.97, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 125, 'wind_gust': 1.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644368400, 'temp': 6.57, 'feels_like': 6.57, 'pressure': 1018, 'humidity': 94, 'dew_point': 5.67, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 128, 'wind_gust': 1.1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644372000, 'temp': 6.57, 'feels_like': 6.57, 'pressure': 1019, 'humidity': 93, 'dew_point': 5.52, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 114, 'wind_gust': 1.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644375600, 'temp': 4.57, 'feels_like': 4.57, 'pressure': 1020, 'humidity': 91, 'dew_point': 3.23, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 114, 'wind_gust': 1.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644379200, 'temp': 4.57, 'feels_like': 4.57, 'pressure': 1020, 'humidity': 90, 'dew_point': 3.07, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 115, 'wind_gust': 1.59, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644382800, 'temp': 4.57, 'feels_like': 4.57, 'pressure': 1019, 'humidity': 90, 'dew_point': 3.07, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 117, 'wind_gust': 1.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644386400, 'temp': 3.57, 'feels_like': 3.57, 'pressure': 1018, 'humidity': 91, 'dew_point': 2.24, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 120, 'wind_gust': 1.05, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644390000, 'temp': 3.57, 'feels_like': 3.57, 'pressure': 1017, 'humidity': 91, 'dew_point': 2.24, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 121, 'wind_gust': 1.09, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644393600, 'temp': 4.57, 'feels_like': 4.57, 'pressure': 1017, 'humidity': 91, 'dew_point': 3.23, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 115, 'wind_gust': 1.14, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644397200, 'temp': 4.57, 'feels_like': 4.57, 'pressure': 1017, 'humidity': 92, 'dew_point': 3.38, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 111, 'wind_gust': 1.19, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644400800, 'temp': 4.57, 'feels_like': 4.57, 'pressure': 1017, 'humidity': 92, 'dew_point': 3.38, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 102, 'wind_gust': 1.39, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644404400, 'temp': 5.57, 'feels_like': 5.57, 'pressure': 1017, 'humidity': 91, 'dew_point': 4.22, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 104, 'wind_gust': 1.37, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644408000, 'temp': 5.57, 'feels_like': 5.57, 'pressure': 1018, 'humidity': 89, 'dew_point': 3.9, 'uvi': 0.15, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 88, 'wind_gust': 1.43, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644411600, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1018, 'humidity': 83, 'dew_point': 5.85, 'uvi': 2.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 68, 'wind_gust': 1.64, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644415200, 'temp': 10.57, 'feels_like': 9.77, 'pressure': 1018, 'humidity': 80, 'dew_point': 7.27, 'uvi': 5.32, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 50, 'wind_gust': 1.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644418800, 'temp': 12.57, 'feels_like': 11.95, 'pressure': 1018, 'humidity': 79, 'dew_point': 9.03, 'uvi': 8.92, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 25, 'wind_gust': 1.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644422400, 'temp': 13.57, 'feels_like': 13.18, 'pressure': 1017, 'humidity': 84, 'dew_point': 10.92, 'uvi': 11.89, 'clouds': 100, 'visibility': 9340, 'wind_speed': 0.38, 'wind_deg': 51, 'wind_gust': 1.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644426000, 'temp': 14.57, 'feels_like': 14.3, 'pressure': 1016, 'humidity': 85, 'dew_point': 12.08, 'uvi': 12.94, 'clouds': 100, 'visibility': 6544, 'wind_speed': 0.26, 'wind_deg': 80, 'wind_gust': 1.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644429600, 'temp': 14.57, 'feels_like': 14.38, 'pressure': 1015, 'humidity': 88, 'dew_point': 12.61, 'uvi': 11.76, 'clouds': 92, 'visibility': 5466, 'wind_speed': 0.15, 'wind_deg': 197, 'wind_gust': 1.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644433200, 'temp': 11.57, 'feels_like': 11.16, 'pressure': 1014, 'humidity': 91, 'dew_point': 10.15, 'uvi': 8.13, 'clouds': 99, 'visibility': 5300, 'wind_speed': 0.1, 'wind_deg': 137, 'wind_gust': 1.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 1}}, {'dt': 1644436800, 'temp': 11.57, 'feels_like': 11.18, 'pressure': 1013, 'humidity': 92, 'dew_point': 10.32, 'uvi': 4.75, 'clouds': 100, 'visibility': 4527, 'wind_speed': 0.28, 'wind_deg': 100, 'wind_gust': 1.45, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 3.16}}, {'dt': 1644440400, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1013, 'humidity': 93, 'dew_point': 7.5, 'uvi': 1.96, 'clouds': 100, 'visibility': 4264, 'wind_speed': 0.38, 'wind_deg': 77, 'wind_gust': 1.36, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.37}}, {'dt': 1644444000, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1014, 'humidity': 93, 'dew_point': 7.5, 'uvi': 0.4, 'clouds': 99, 'visibility': 4630, 'wind_speed': 0.42, 'wind_deg': 49, 'wind_gust': 1.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644447600, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1015, 'humidity': 98, 'dew_point': 8.27, 'uvi': 0, 'clouds': 98, 'visibility': 1438, 'wind_speed': 0.68, 'wind_deg': 70, 'wind_gust': 1.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 00:00:00 | 100.000000 | 6.970000 | 7.570000 | 96.000000 | 1017.000000 |  | 7.570000 | 0.000000 | 10000.000000 | 125.000000 | 1.09 | 0.440000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 01:00:00 | 100.000000 | 5.670000 | 6.570000 | 94.000000 | 1018.000000 |  | 6.570000 | 0.000000 | 10000.000000 | 128.000000 | 1.1 | 0.570000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 02:00:00 | 100.000000 | 5.520000 | 6.570000 | 93.000000 | 1019.000000 |  | 6.570000 | 0.000000 | 10000.000000 | 114.000000 | 1.42 | 0.900000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 03:00:00 | 99.000000 | 3.230000 | 4.570000 | 91.000000 | 1020.000000 |  | 4.570000 | 0.000000 | 10000.000000 | 114.000000 | 1.54 | 1.090000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 04:00:00 | 92.000000 | 3.070000 | 4.570000 | 90.000000 | 1020.000000 |  | 4.570000 | 0.000000 | 10000.000000 | 115.000000 | 1.59 | 1.170000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 05:00:00 | 93.000000 | 3.070000 | 4.570000 | 90.000000 | 1019.000000 |  | 4.570000 | 0.000000 | 10000.000000 | 117.000000 | 1.5 | 1.020000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 06:00:00 | 70.000000 | 2.240000 | 3.570000 | 91.000000 | 1018.000000 |  | 3.570000 | 0.000000 | 10000.000000 | 120.000000 | 1.05 | 0.720000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 07:00:00 | 80.000000 | 2.240000 | 3.570000 | 91.000000 | 1017.000000 |  | 3.570000 | 0.000000 | 10000.000000 | 121.000000 | 1.09 | 0.770000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 08:00:00 | 77.000000 | 3.230000 | 4.570000 | 91.000000 | 1017.000000 |  | 4.570000 | 0.000000 | 10000.000000 | 115.000000 | 1.14 | 0.700000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 09:00:00 | 79.000000 | 3.380000 | 4.570000 | 92.000000 | 1017.000000 |  | 4.570000 | 0.000000 | 10000.000000 | 111.000000 | 1.19 | 0.840000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 10:00:00 | 77.000000 | 3.380000 | 4.570000 | 92.000000 | 1017.000000 |  | 4.570000 | 0.000000 | 10000.000000 | 102.000000 | 1.39 | 0.860000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 11:00:00 | 77.000000 | 4.220000 | 5.570000 | 91.000000 | 1017.000000 |  | 5.570000 | 0.000000 | 10000.000000 | 104.000000 | 1.37 | 0.920000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 12:00:00 | 100.000000 | 3.900000 | 5.570000 | 89.000000 | 1018.000000 |  | 5.570000 | 0.150000 | 10000.000000 | 88.000000 | 1.43 | 0.770000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 13:00:00 | 100.000000 | 5.850000 | 8.570000 | 83.000000 | 1018.000000 |  | 8.570000 | 2.260000 | 10000.000000 | 68.000000 | 1.64 | 0.680000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 14:00:00 | 100.000000 | 7.270000 | 9.770000 | 80.000000 | 1018.000000 |  | 10.570000 | 5.320000 | 10000.000000 | 50.000000 | 1.76 | 0.440000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 15:00:00 | 100.000000 | 9.030000 | 11.950000 | 79.000000 | 1018.000000 |  | 12.570000 | 8.920000 | 10000.000000 | 25.000000 | 1.79 | 0.400000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 16:00:00 | 100.000000 | 10.920000 | 13.180000 | 84.000000 | 1017.000000 |  | 13.570000 | 11.890000 | 9340.000000 | 51.000000 | 1.72 | 0.380000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 17:00:00 | 100.000000 | 12.080000 | 14.300000 | 85.000000 | 1016.000000 |  | 14.570000 | 12.940000 | 6544.000000 | 80.000000 | 1.68 | 0.260000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 18:00:00 | 92.000000 | 12.610000 | 14.380000 | 88.000000 | 1015.000000 |  | 14.570000 | 11.760000 | 5466.000000 | 197.000000 | 1.84 | 0.150000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 19:00:00 | 99.000000 | 10.150000 | 11.160000 | 91.000000 | 1014.000000 | 1 | 11.570000 | 8.130000 | 5300.000000 | 137.000000 | 1.57 | 0.100000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 20:00:00 | 100.000000 | 10.320000 | 11.180000 | 92.000000 | 1013.000000 | 3.16 | 11.570000 | 4.750000 | 4527.000000 | 100.000000 | 1.45 | 0.280000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 21:00:00 | 100.000000 | 7.500000 | 8.570000 | 93.000000 | 1013.000000 | 2.37 | 8.570000 | 1.960000 | 4264.000000 | 77.000000 | 1.36 | 0.380000 | 501 | Rain | moderate rain | 10d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 22:00:00 | 99.000000 | 7.500000 | 8.570000 | 93.000000 | 1014.000000 |  | 8.570000 | 0.400000 | 4630.000000 | 49.000000 | 1.22 | 0.420000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 23:00:00 | 98.000000 | 8.270000 | 8.570000 | 98.000000 | 1015.000000 |  | 8.570000 | 0.000000 | 1438.000000 | 70.000000 | 1.22 | 0.680000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35025070_OWM_Clouds_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Clouds_20220211.png)
![CNE_IDEAM_Station35025070_OWM_Dewpoint_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Dewpoint_20220211.png)
![CNE_IDEAM_Station35025070_OWM_Feelslike_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Feelslike_20220211.png)
![CNE_IDEAM_Station35025070_OWM_Humidity_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Humidity_20220211.png)
![CNE_IDEAM_Station35025070_OWM_Pressure_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Pressure_20220211.png)
![CNE_IDEAM_Station35025070_OWM_Rain_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Rain_20220211.png)
![CNE_IDEAM_Station35025070_OWM_Temp_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Temp_20220211.png)
![CNE_IDEAM_Station35025070_OWM_UVI_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_UVI_20220211.png)
![CNE_IDEAM_Station35025070_OWM_Visibility_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Visibility_20220211.png)
![CNE_IDEAM_Station35025070_OWM_Winddeg_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Winddeg_20220211.png)
![CNE_IDEAM_Station35025070_OWM_Windgust_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Windgust_20220211.png)
![CNE_IDEAM_Station35025070_OWM_Windspeed_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Windspeed_20220211.png)

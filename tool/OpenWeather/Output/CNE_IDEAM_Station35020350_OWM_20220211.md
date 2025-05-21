
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BETANIA [35020350] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35020350_OWM_20220211.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220211.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.21888889,-74.14686111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.21888889&lon=-74.14686111)

| Parameter | Value |
|---|---|
| Code | 35020350 |
| Name | BETANIA [35020350] |
| Latitude, ° | 4.21888889 |
| Longitude, ° | -74.14686111 |
| Elevation, m | 3150 |
| Category | Pluviométrica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1986-01-15 00:00:00 |
| Suspension date | NaT |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Blanco |
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

### (CNE index 1901) Open Weather values for station 35020350 - BETANIA [35020350]

JSON data from API OWM:

```
{'lat': 4.2189, 'lon': -74.1469, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644427498, 'sunrise': 1644405110, 'sunset': 1644448193, 'temp': 16.37, 'feels_like': 16.23, 'pressure': 1016, 'humidity': 83, 'dew_point': 13.48, 'uvi': 12.94, 'clouds': 100, 'visibility': 8945, 'wind_speed': 0.68, 'wind_deg': 104, 'wind_gust': 1.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644364800, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1017, 'humidity': 96, 'dew_point': 8.77, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.29, 'wind_deg': 185, 'wind_gust': 1.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644368400, 'temp': 8.37, 'feels_like': 8.37, 'pressure': 1018, 'humidity': 94, 'dew_point': 7.46, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 176, 'wind_gust': 1.1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644372000, 'temp': 8.37, 'feels_like': 8.37, 'pressure': 1019, 'humidity': 92, 'dew_point': 7.15, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 143, 'wind_gust': 1.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644375600, 'temp': 6.37, 'feels_like': 6.37, 'pressure': 1020, 'humidity': 91, 'dew_point': 5.01, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 138, 'wind_gust': 1.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644379200, 'temp': 6.37, 'feels_like': 6.37, 'pressure': 1020, 'humidity': 90, 'dew_point': 4.85, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 134, 'wind_gust': 1.53, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644382800, 'temp': 6.37, 'feels_like': 6.37, 'pressure': 1019, 'humidity': 90, 'dew_point': 4.85, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 141, 'wind_gust': 1.47, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644386400, 'temp': 5.37, 'feels_like': 5.37, 'pressure': 1018, 'humidity': 91, 'dew_point': 4.02, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 150, 'wind_gust': 1.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644390000, 'temp': 5.37, 'feels_like': 5.37, 'pressure': 1017, 'humidity': 91, 'dew_point': 4.02, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 150, 'wind_gust': 1.06, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644393600, 'temp': 6.37, 'feels_like': 6.37, 'pressure': 1017, 'humidity': 91, 'dew_point': 5.01, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 146, 'wind_gust': 1.12, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644397200, 'temp': 6.37, 'feels_like': 6.37, 'pressure': 1017, 'humidity': 91, 'dew_point': 5.01, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 134, 'wind_gust': 1.16, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644400800, 'temp': 6.37, 'feels_like': 6.37, 'pressure': 1017, 'humidity': 91, 'dew_point': 5.01, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 121, 'wind_gust': 1.35, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644404400, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1017, 'humidity': 91, 'dew_point': 6, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 124, 'wind_gust': 1.31, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644408000, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1018, 'humidity': 89, 'dew_point': 5.68, 'uvi': 0.15, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 104, 'wind_gust': 1.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644411600, 'temp': 10.37, 'feels_like': 9.6, 'pressure': 1018, 'humidity': 82, 'dew_point': 7.43, 'uvi': 2.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 83, 'wind_gust': 1.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644415200, 'temp': 12.37, 'feels_like': 11.73, 'pressure': 1018, 'humidity': 79, 'dew_point': 8.84, 'uvi': 5.32, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 79, 'wind_gust': 1.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644418800, 'temp': 14.37, 'feels_like': 13.93, 'pressure': 1018, 'humidity': 79, 'dew_point': 10.78, 'uvi': 8.92, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 73, 'wind_gust': 1.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644422400, 'temp': 15.37, 'feels_like': 15.1, 'pressure': 1017, 'humidity': 82, 'dew_point': 12.32, 'uvi': 11.89, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 89, 'wind_gust': 1.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644426000, 'temp': 16.37, 'feels_like': 16.23, 'pressure': 1016, 'humidity': 83, 'dew_point': 13.48, 'uvi': 12.94, 'clouds': 100, 'visibility': 8945, 'wind_speed': 0.68, 'wind_deg': 104, 'wind_gust': 1.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644429600, 'temp': 16.37, 'feels_like': 16.33, 'pressure': 1015, 'humidity': 87, 'dew_point': 14.2, 'uvi': 11.76, 'clouds': 89, 'visibility': 7392, 'wind_speed': 0.44, 'wind_deg': 135, 'wind_gust': 1.93, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644433200, 'temp': 13.37, 'feels_like': 13.09, 'pressure': 1014, 'humidity': 89, 'dew_point': 11.6, 'uvi': 8.13, 'clouds': 98, 'visibility': 7543, 'wind_speed': 0.44, 'wind_deg': 124, 'wind_gust': 1.64, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.33}}, {'dt': 1644436800, 'temp': 13.37, 'feels_like': 13.16, 'pressure': 1013, 'humidity': 92, 'dew_point': 12.1, 'uvi': 4.75, 'clouds': 99, 'visibility': 5785, 'wind_speed': 0.54, 'wind_deg': 114, 'wind_gust': 1.49, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.73}}, {'dt': 1644440400, 'temp': 10.37, 'feels_like': 9.89, 'pressure': 1013, 'humidity': 93, 'dew_point': 9.29, 'uvi': 1.96, 'clouds': 99, 'visibility': 3351, 'wind_speed': 0.53, 'wind_deg': 93, 'wind_gust': 1.32, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.78}}, {'dt': 1644444000, 'temp': 10.37, 'feels_like': 9.89, 'pressure': 1014, 'humidity': 93, 'dew_point': 9.29, 'uvi': 0.4, 'clouds': 98, 'visibility': 3853, 'wind_speed': 0.52, 'wind_deg': 69, 'wind_gust': 1.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644447600, 'temp': 10.37, 'feels_like': 10.02, 'pressure': 1015, 'humidity': 98, 'dew_point': 10.07, 'uvi': 0, 'clouds': 97, 'visibility': 1184, 'wind_speed': 0.63, 'wind_deg': 75, 'wind_gust': 1.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 00:00:00 | 100.000000 | 8.770000 | 9.370000 | 96.000000 | 1017.000000 |  | 9.370000 | 0.000000 | 10000.000000 | 185.000000 | 1.09 | 0.290000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 01:00:00 | 100.000000 | 7.460000 | 8.370000 | 94.000000 | 1018.000000 |  | 8.370000 | 0.000000 | 10000.000000 | 176.000000 | 1.1 | 0.390000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 02:00:00 | 100.000000 | 7.150000 | 8.370000 | 92.000000 | 1019.000000 |  | 8.370000 | 0.000000 | 10000.000000 | 143.000000 | 1.38 | 0.510000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 03:00:00 | 97.000000 | 5.010000 | 6.370000 | 91.000000 | 1020.000000 |  | 6.370000 | 0.000000 | 10000.000000 | 138.000000 | 1.5 | 0.620000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 04:00:00 | 92.000000 | 4.850000 | 6.370000 | 90.000000 | 1020.000000 |  | 6.370000 | 0.000000 | 10000.000000 | 134.000000 | 1.53 | 0.720000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 05:00:00 | 93.000000 | 4.850000 | 6.370000 | 90.000000 | 1019.000000 |  | 6.370000 | 0.000000 | 10000.000000 | 141.000000 | 1.47 | 0.610000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 06:00:00 | 74.000000 | 4.020000 | 5.370000 | 91.000000 | 1018.000000 |  | 5.370000 | 0.000000 | 10000.000000 | 150.000000 | 1.02 | 0.450000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 07:00:00 | 83.000000 | 4.020000 | 5.370000 | 91.000000 | 1017.000000 |  | 5.370000 | 0.000000 | 10000.000000 | 150.000000 | 1.06 | 0.510000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 08:00:00 | 79.000000 | 5.010000 | 6.370000 | 91.000000 | 1017.000000 |  | 6.370000 | 0.000000 | 10000.000000 | 146.000000 | 1.12 | 0.400000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 09:00:00 | 80.000000 | 5.010000 | 6.370000 | 91.000000 | 1017.000000 |  | 6.370000 | 0.000000 | 10000.000000 | 134.000000 | 1.16 | 0.480000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 10:00:00 | 78.000000 | 5.010000 | 6.370000 | 91.000000 | 1017.000000 |  | 6.370000 | 0.000000 | 10000.000000 | 121.000000 | 1.35 | 0.410000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 11:00:00 | 78.000000 | 6.000000 | 7.370000 | 91.000000 | 1017.000000 |  | 7.370000 | 0.000000 | 10000.000000 | 124.000000 | 1.31 | 0.520000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 12:00:00 | 100.000000 | 5.680000 | 7.370000 | 89.000000 | 1018.000000 |  | 7.370000 | 0.150000 | 10000.000000 | 104.000000 | 1.31 | 0.400000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 13:00:00 | 100.000000 | 7.430000 | 9.600000 | 82.000000 | 1018.000000 |  | 10.370000 | 2.260000 | 10000.000000 | 83.000000 | 1.68 | 0.760000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 14:00:00 | 100.000000 | 8.840000 | 11.730000 | 79.000000 | 1018.000000 |  | 12.370000 | 5.320000 | 10000.000000 | 79.000000 | 1.78 | 0.640000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 15:00:00 | 100.000000 | 10.780000 | 13.930000 | 79.000000 | 1018.000000 |  | 14.370000 | 8.920000 | 10000.000000 | 73.000000 | 1.82 | 0.540000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 16:00:00 | 100.000000 | 12.320000 | 15.100000 | 82.000000 | 1017.000000 |  | 15.370000 | 11.890000 | 10000.000000 | 89.000000 | 1.84 | 0.690000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 17:00:00 | 100.000000 | 13.480000 | 16.230000 | 83.000000 | 1016.000000 |  | 16.370000 | 12.940000 | 8945.000000 | 104.000000 | 1.82 | 0.680000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 18:00:00 | 89.000000 | 14.200000 | 16.330000 | 87.000000 | 1015.000000 |  | 16.370000 | 11.760000 | 7392.000000 | 135.000000 | 1.93 | 0.440000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 19:00:00 | 98.000000 | 11.600000 | 13.090000 | 89.000000 | 1014.000000 | 1.33 | 13.370000 | 8.130000 | 7543.000000 | 124.000000 | 1.64 | 0.440000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 20:00:00 | 99.000000 | 12.100000 | 13.160000 | 92.000000 | 1013.000000 | 2.73 | 13.370000 | 4.750000 | 5785.000000 | 114.000000 | 1.49 | 0.540000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 21:00:00 | 99.000000 | 9.290000 | 9.890000 | 93.000000 | 1013.000000 | 1.78 | 10.370000 | 1.960000 | 3351.000000 | 93.000000 | 1.32 | 0.530000 | 501 | Rain | moderate rain | 10d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 22:00:00 | 98.000000 | 9.290000 | 9.890000 | 93.000000 | 1014.000000 |  | 10.370000 | 0.400000 | 3853.000000 | 69.000000 | 1.2 | 0.520000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 23:00:00 | 97.000000 | 10.070000 | 10.020000 | 98.000000 | 1015.000000 |  | 10.370000 | 0.000000 | 1184.000000 | 75.000000 | 1.11 | 0.630000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35020350_OWM_Clouds_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Clouds_20220211.png)
![CNE_IDEAM_Station35020350_OWM_Dewpoint_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Dewpoint_20220211.png)
![CNE_IDEAM_Station35020350_OWM_Feelslike_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Feelslike_20220211.png)
![CNE_IDEAM_Station35020350_OWM_Humidity_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Humidity_20220211.png)
![CNE_IDEAM_Station35020350_OWM_Pressure_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Pressure_20220211.png)
![CNE_IDEAM_Station35020350_OWM_Rain_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Rain_20220211.png)
![CNE_IDEAM_Station35020350_OWM_Temp_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Temp_20220211.png)
![CNE_IDEAM_Station35020350_OWM_UVI_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_UVI_20220211.png)
![CNE_IDEAM_Station35020350_OWM_Visibility_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Visibility_20220211.png)
![CNE_IDEAM_Station35020350_OWM_Winddeg_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Winddeg_20220211.png)
![CNE_IDEAM_Station35020350_OWM_Windgust_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Windgust_20220211.png)
![CNE_IDEAM_Station35020350_OWM_Windspeed_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Windspeed_20220211.png)

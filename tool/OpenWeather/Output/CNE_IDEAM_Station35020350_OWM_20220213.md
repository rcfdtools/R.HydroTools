
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

* Current date time: 2022-02-13 07:30:06.495901
* Unix time to eval: 1644564606
* Days before (for historical data): 2
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220213.xls
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35020350_OWM_20220213.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220213.csv)

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
{'lat': 4.2189, 'lon': -74.1469, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644564606, 'sunrise': 1644577901, 'sunset': 1644621008, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1015, 'humidity': 95, 'dew_point': 6.62, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 273, 'wind_gust': 0.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, 'hourly': [{'dt': 1644537600, 'temp': 10.37, 'feels_like': 9.92, 'pressure': 1015, 'humidity': 94, 'dew_point': 9.45, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 75, 'wind_gust': 1.24, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644541200, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1016, 'humidity': 92, 'dew_point': 8.14, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 93, 'wind_gust': 1.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644544800, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1016, 'humidity': 92, 'dew_point': 8.14, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 115, 'wind_gust': 0.64, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644548400, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1017, 'humidity': 93, 'dew_point': 8.3, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.18, 'wind_deg': 93, 'wind_gust': 0.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644552000, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1017, 'humidity': 93, 'dew_point': 8.3, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.22, 'wind_deg': 50, 'wind_gust': 0.67, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644555600, 'temp': 8.37, 'feels_like': 8.37, 'pressure': 1016, 'humidity': 94, 'dew_point': 7.46, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.14, 'wind_deg': 20, 'wind_gust': 0.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644559200, 'temp': 8.37, 'feels_like': 8.37, 'pressure': 1016, 'humidity': 94, 'dew_point': 7.46, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.07, 'wind_deg': 281, 'wind_gust': 0.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644562800, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1015, 'humidity': 94, 'dew_point': 6.47, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 245, 'wind_gust': 0.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644566400, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1015, 'humidity': 95, 'dew_point': 6.62, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 273, 'wind_gust': 0.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644570000, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1015, 'humidity': 96, 'dew_point': 6.78, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 286, 'wind_gust': 0.93, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644573600, 'temp': 6.37, 'feels_like': 6.37, 'pressure': 1015, 'humidity': 95, 'dew_point': 5.63, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 282, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644577200, 'temp': 6.37, 'feels_like': 6.37, 'pressure': 1016, 'humidity': 94, 'dew_point': 5.48, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 279, 'wind_gust': 0.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644580800, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1016, 'humidity': 91, 'dew_point': 6, 'uvi': 0.44, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 343, 'wind_gust': 0.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644584400, 'temp': 11.37, 'feels_like': 10.81, 'pressure': 1017, 'humidity': 86, 'dew_point': 9.11, 'uvi': 2.45, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 62, 'wind_gust': 1.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644588000, 'temp': 13.37, 'feels_like': 12.9, 'pressure': 1017, 'humidity': 82, 'dew_point': 10.36, 'uvi': 5.78, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 49, 'wind_gust': 1.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644591600, 'temp': 14.37, 'feels_like': 13.85, 'pressure': 1016, 'humidity': 76, 'dew_point': 10.2, 'uvi': 9.69, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 41, 'wind_gust': 1.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644595200, 'temp': 15.37, 'feels_like': 14.89, 'pressure': 1015, 'humidity': 74, 'dew_point': 10.77, 'uvi': 12.74, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 31, 'wind_gust': 2.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644598800, 'temp': 17.37, 'feels_like': 17.12, 'pressure': 1014, 'humidity': 75, 'dew_point': 12.9, 'uvi': 13.86, 'clouds': 84, 'visibility': 8988, 'wind_speed': 0.95, 'wind_deg': 31, 'wind_gust': 2.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644602400, 'temp': 16.37, 'feels_like': 16.13, 'pressure': 1013, 'humidity': 79, 'dew_point': 12.72, 'uvi': 12.6, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 21, 'wind_gust': 2.44, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644606000, 'temp': 17.37, 'feels_like': 17.38, 'pressure': 1012, 'humidity': 85, 'dew_point': 14.82, 'uvi': 8.92, 'clouds': 93, 'visibility': 6316, 'wind_speed': 0.51, 'wind_deg': 22, 'wind_gust': 2.27, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644609600, 'temp': 17.37, 'feels_like': 17.62, 'pressure': 1012, 'humidity': 94, 'dew_point': 16.4, 'uvi': 5.22, 'clouds': 97, 'visibility': 2508, 'wind_speed': 0.23, 'wind_deg': 330, 'wind_gust': 1.93, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644613200, 'temp': 14.37, 'feels_like': 14.4, 'pressure': 1012, 'humidity': 97, 'dew_point': 13.9, 'uvi': 2.15, 'clouds': 98, 'visibility': 332, 'wind_speed': 0.17, 'wind_deg': 337, 'wind_gust': 1.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644616800, 'temp': 14.37, 'feels_like': 14.42, 'pressure': 1013, 'humidity': 98, 'dew_point': 14.06, 'uvi': 0.5, 'clouds': 98, 'visibility': 127, 'wind_speed': 0.29, 'wind_deg': 65, 'wind_gust': 1.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644620400, 'temp': 13.37, 'feels_like': 13.35, 'pressure': 1014, 'humidity': 99, 'dew_point': 13.22, 'uvi': 0, 'clouds': 98, 'visibility': 126, 'wind_speed': 0.55, 'wind_deg': 75, 'wind_gust': 1.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 00:00:00 | 65.000000 | 9.450000 | 9.920000 | 94.000000 | 1015.000000 |  | 10.370000 | 0.000000 | 10000.000000 | 75.000000 | 1.24 | 0.930000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 01:00:00 | 79.000000 | 8.140000 | 9.370000 | 92.000000 | 1016.000000 |  | 9.370000 | 0.000000 | 10000.000000 | 93.000000 | 1.02 | 0.700000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 02:00:00 | 80.000000 | 8.140000 | 9.370000 | 92.000000 | 1016.000000 |  | 9.370000 | 0.000000 | 10000.000000 | 115.000000 | 0.64 | 0.310000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 03:00:00 | 76.000000 | 8.300000 | 9.370000 | 93.000000 | 1017.000000 |  | 9.370000 | 0.000000 | 10000.000000 | 93.000000 | 0.56 | 0.180000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 04:00:00 | 81.000000 | 8.300000 | 9.370000 | 93.000000 | 1017.000000 |  | 9.370000 | 0.000000 | 10000.000000 | 50.000000 | 0.67 | 0.220000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 05:00:00 | 84.000000 | 7.460000 | 8.370000 | 94.000000 | 1016.000000 |  | 8.370000 | 0.000000 | 10000.000000 | 20.000000 | 0.61 | 0.140000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 06:00:00 | 97.000000 | 7.460000 | 8.370000 | 94.000000 | 1016.000000 |  | 8.370000 | 0.000000 | 10000.000000 | 281.000000 | 0.52 | 0.070000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 07:00:00 | 100.000000 | 6.470000 | 7.370000 | 94.000000 | 1015.000000 |  | 7.370000 | 0.000000 | 10000.000000 | 245.000000 | 0.65 | 0.280000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 08:00:00 | 100.000000 | 6.620000 | 7.370000 | 95.000000 | 1015.000000 |  | 7.370000 | 0.000000 | 10000.000000 | 273.000000 | 0.71 | 0.590000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 09:00:00 | 100.000000 | 6.780000 | 7.370000 | 96.000000 | 1015.000000 |  | 7.370000 | 0.000000 | 10000.000000 | 286.000000 | 0.93 | 0.640000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 10:00:00 | 100.000000 | 5.630000 | 6.370000 | 95.000000 | 1015.000000 |  | 6.370000 | 0.000000 | 10000.000000 | 282.000000 | 0.88 | 0.610000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 11:00:00 | 98.000000 | 5.480000 | 6.370000 | 94.000000 | 1016.000000 |  | 6.370000 | 0.000000 | 10000.000000 | 279.000000 | 0.79 | 0.610000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 12:00:00 | 94.000000 | 6.000000 | 7.370000 | 91.000000 | 1016.000000 |  | 7.370000 | 0.440000 | 10000.000000 | 343.000000 | 0.86 | 0.320000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 13:00:00 | 100.000000 | 9.110000 | 10.810000 | 86.000000 | 1017.000000 |  | 11.370000 | 2.450000 | 10000.000000 | 62.000000 | 1.11 | 0.680000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 14:00:00 | 97.000000 | 10.360000 | 12.900000 | 82.000000 | 1017.000000 |  | 13.370000 | 5.780000 | 10000.000000 | 49.000000 | 1.4 | 0.760000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 15:00:00 | 89.000000 | 10.200000 | 13.850000 | 76.000000 | 1016.000000 |  | 14.370000 | 9.690000 | 10000.000000 | 41.000000 | 1.85 | 0.900000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 16:00:00 | 86.000000 | 10.770000 | 14.890000 | 74.000000 | 1015.000000 |  | 15.370000 | 12.740000 | 10000.000000 | 31.000000 | 2.09 | 0.930000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 17:00:00 | 84.000000 | 12.900000 | 17.120000 | 75.000000 | 1014.000000 |  | 17.370000 | 13.860000 | 8988.000000 | 31.000000 | 2.54 | 0.950000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 18:00:00 | 81.000000 | 12.720000 | 16.130000 | 79.000000 | 1013.000000 |  | 16.370000 | 12.600000 | 10000.000000 | 21.000000 | 2.44 | 0.710000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 19:00:00 | 93.000000 | 14.820000 | 17.380000 | 85.000000 | 1012.000000 |  | 17.370000 | 8.920000 | 6316.000000 | 22.000000 | 2.27 | 0.510000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 20:00:00 | 97.000000 | 16.400000 | 17.620000 | 94.000000 | 1012.000000 |  | 17.370000 | 5.220000 | 2508.000000 | 330.000000 | 1.93 | 0.230000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 21:00:00 | 98.000000 | 13.900000 | 14.400000 | 97.000000 | 1012.000000 |  | 14.370000 | 2.150000 | 332.000000 | 337.000000 | 1.75 | 0.170000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 22:00:00 | 98.000000 | 14.060000 | 14.420000 | 98.000000 | 1013.000000 |  | 14.370000 | 0.500000 | 127.000000 | 65.000000 | 1.65 | 0.290000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 23:00:00 | 98.000000 | 13.220000 | 13.350000 | 99.000000 | 1014.000000 |  | 13.370000 | 0.000000 | 126.000000 | 75.000000 | 1.22 | 0.550000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35020350_OWM_Clouds_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Clouds_20220213.png)
![CNE_IDEAM_Station35020350_OWM_Dewpoint_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Dewpoint_20220213.png)
![CNE_IDEAM_Station35020350_OWM_Feelslike_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Feelslike_20220213.png)
![CNE_IDEAM_Station35020350_OWM_Humidity_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Humidity_20220213.png)
![CNE_IDEAM_Station35020350_OWM_Pressure_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Pressure_20220213.png)
![CNE_IDEAM_Station35020350_OWM_Rain_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Rain_20220213.png)
![CNE_IDEAM_Station35020350_OWM_Temp_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Temp_20220213.png)
![CNE_IDEAM_Station35020350_OWM_UVI_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_UVI_20220213.png)
![CNE_IDEAM_Station35020350_OWM_Visibility_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Visibility_20220213.png)
![CNE_IDEAM_Station35020350_OWM_Winddeg_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Winddeg_20220213.png)
![CNE_IDEAM_Station35020350_OWM_Windgust_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Windgust_20220213.png)
![CNE_IDEAM_Station35020350_OWM_Windspeed_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Windspeed_20220213.png)

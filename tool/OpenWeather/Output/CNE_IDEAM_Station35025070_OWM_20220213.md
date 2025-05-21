
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35025070_OWM_20220213.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220213.csv)

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
{'lat': 4.1967, 'lon': -74.1909, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644564606, 'sunrise': 1644577910, 'sunset': 1644621020, 'temp': 5.57, 'feels_like': 5.57, 'pressure': 1015, 'humidity': 96, 'dew_point': 4.98, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 285, 'wind_gust': 0.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, 'hourly': [{'dt': 1644537600, 'temp': 8.28, 'feels_like': 8.28, 'pressure': 1015, 'humidity': 94, 'dew_point': 7.37, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 74, 'wind_gust': 1.47, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644541200, 'temp': 8.13, 'feels_like': 8.13, 'pressure': 1016, 'humidity': 92, 'dew_point': 6.91, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 88, 'wind_gust': 1.21, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644544800, 'temp': 7.68, 'feels_like': 7.68, 'pressure': 1016, 'humidity': 92, 'dew_point': 6.46, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 91, 'wind_gust': 0.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644548400, 'temp': 7.49, 'feels_like': 7.49, 'pressure': 1017, 'humidity': 93, 'dew_point': 6.43, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 70, 'wind_gust': 0.6, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644552000, 'temp': 7.41, 'feels_like': 7.41, 'pressure': 1017, 'humidity': 93, 'dew_point': 6.35, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 53, 'wind_gust': 0.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644555600, 'temp': 7.44, 'feels_like': 7.44, 'pressure': 1016, 'humidity': 94, 'dew_point': 6.54, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 38, 'wind_gust': 0.66, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644559200, 'temp': 7.11, 'feels_like': 7.11, 'pressure': 1016, 'humidity': 95, 'dew_point': 6.36, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.16, 'wind_deg': 31, 'wind_gust': 0.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644562800, 'temp': 5.57, 'feels_like': 5.57, 'pressure': 1015, 'humidity': 95, 'dew_point': 4.83, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.11, 'wind_deg': 268, 'wind_gust': 0.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644566400, 'temp': 5.57, 'feels_like': 5.57, 'pressure': 1015, 'humidity': 96, 'dew_point': 4.98, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 285, 'wind_gust': 0.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644570000, 'temp': 5.57, 'feels_like': 5.57, 'pressure': 1015, 'humidity': 96, 'dew_point': 4.98, 'uvi': 0, 'clouds': 100, 'visibility': 7171, 'wind_speed': 0.54, 'wind_deg': 306, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644573600, 'temp': 4.57, 'feels_like': 4.57, 'pressure': 1015, 'humidity': 96, 'dew_point': 3.99, 'uvi': 0, 'clouds': 100, 'visibility': 8021, 'wind_speed': 0.46, 'wind_deg': 305, 'wind_gust': 0.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644577200, 'temp': 4.57, 'feels_like': 4.57, 'pressure': 1016, 'humidity': 94, 'dew_point': 3.69, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 299, 'wind_gust': 0.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644580800, 'temp': 5.57, 'feels_like': 5.57, 'pressure': 1016, 'humidity': 91, 'dew_point': 4.22, 'uvi': 0.44, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 12, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644584400, 'temp': 9.57, 'feels_like': 9.57, 'pressure': 1017, 'humidity': 87, 'dew_point': 7.52, 'uvi': 2.45, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 44, 'wind_gust': 1.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644588000, 'temp': 11.57, 'feels_like': 10.9, 'pressure': 1017, 'humidity': 81, 'dew_point': 8.43, 'uvi': 5.78, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 23, 'wind_gust': 1.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644591600, 'temp': 12.57, 'feels_like': 11.84, 'pressure': 1016, 'humidity': 75, 'dew_point': 8.26, 'uvi': 9.69, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 11, 'wind_gust': 1.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644595200, 'temp': 13.57, 'feels_like': 12.89, 'pressure': 1015, 'humidity': 73, 'dew_point': 8.83, 'uvi': 12.74, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 354, 'wind_gust': 2.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644598800, 'temp': 15.57, 'feels_like': 15.11, 'pressure': 1014, 'humidity': 74, 'dew_point': 10.96, 'uvi': 13.86, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 352, 'wind_gust': 2.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644602400, 'temp': 14.57, 'feels_like': 14.15, 'pressure': 1013, 'humidity': 79, 'dew_point': 10.97, 'uvi': 12.6, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 337, 'wind_gust': 2.32, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644606000, 'temp': 15.57, 'feels_like': 15.38, 'pressure': 1012, 'humidity': 84, 'dew_point': 12.88, 'uvi': 8.92, 'clouds': 95, 'visibility': 7792, 'wind_speed': 0.8, 'wind_deg': 328, 'wind_gust': 2.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644609600, 'temp': 15.57, 'feels_like': 15.64, 'pressure': 1012, 'humidity': 94, 'dew_point': 14.61, 'uvi': 5.22, 'clouds': 97, 'visibility': 3552, 'wind_speed': 0.69, 'wind_deg': 304, 'wind_gust': 1.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644613200, 'temp': 12.57, 'feels_like': 12.39, 'pressure': 1012, 'humidity': 96, 'dew_point': 11.95, 'uvi': 2.15, 'clouds': 98, 'visibility': 533, 'wind_speed': 0.59, 'wind_deg': 306, 'wind_gust': 1.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644616800, 'temp': 12.57, 'feels_like': 12.44, 'pressure': 1013, 'humidity': 98, 'dew_point': 12.26, 'uvi': 0.5, 'clouds': 99, 'visibility': 140, 'wind_speed': 0.3, 'wind_deg': 348, 'wind_gust': 1.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644620400, 'temp': 11.57, 'feels_like': 11.37, 'pressure': 1014, 'humidity': 99, 'dew_point': 11.42, 'uvi': 0, 'clouds': 99, 'visibility': 141, 'wind_speed': 0.43, 'wind_deg': 52, 'wind_gust': 1.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 00:00:00 | 63.000000 | 7.370000 | 8.280000 | 94.000000 | 1015.000000 |  | 8.280000 | 0.000000 | 10000.000000 | 74.000000 | 1.47 | 1.200000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 01:00:00 | 75.000000 | 6.910000 | 8.130000 | 92.000000 | 1016.000000 |  | 8.130000 | 0.000000 | 10000.000000 | 88.000000 | 1.21 | 0.980000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 02:00:00 | 77.000000 | 6.460000 | 7.680000 | 92.000000 | 1016.000000 |  | 7.680000 | 0.000000 | 10000.000000 | 91.000000 | 0.7 | 0.510000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 03:00:00 | 74.000000 | 6.430000 | 7.490000 | 93.000000 | 1017.000000 |  | 7.490000 | 0.000000 | 10000.000000 | 70.000000 | 0.6 | 0.410000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 04:00:00 | 78.000000 | 6.350000 | 7.410000 | 93.000000 | 1017.000000 |  | 7.410000 | 0.000000 | 10000.000000 | 53.000000 | 0.74 | 0.490000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 05:00:00 | 82.000000 | 6.540000 | 7.440000 | 94.000000 | 1016.000000 |  | 7.440000 | 0.000000 | 10000.000000 | 38.000000 | 0.66 | 0.390000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 06:00:00 | 98.000000 | 6.360000 | 7.110000 | 95.000000 | 1016.000000 |  | 7.110000 | 0.000000 | 10000.000000 | 31.000000 | 0.5 | 0.160000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 07:00:00 | 100.000000 | 4.830000 | 5.570000 | 95.000000 | 1015.000000 |  | 5.570000 | 0.000000 | 10000.000000 | 268.000000 | 0.61 | 0.110000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 08:00:00 | 100.000000 | 4.980000 | 5.570000 | 96.000000 | 1015.000000 |  | 5.570000 | 0.000000 | 10000.000000 | 285.000000 | 0.71 | 0.520000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 09:00:00 | 100.000000 | 4.980000 | 5.570000 | 96.000000 | 1015.000000 |  | 5.570000 | 0.000000 | 7171.000000 | 306.000000 | 0.91 | 0.540000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 10:00:00 | 100.000000 | 3.990000 | 4.570000 | 96.000000 | 1015.000000 |  | 4.570000 | 0.000000 | 8021.000000 | 305.000000 | 0.84 | 0.460000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 11:00:00 | 99.000000 | 3.690000 | 4.570000 | 94.000000 | 1016.000000 |  | 4.570000 | 0.000000 | 10000.000000 | 299.000000 | 0.68 | 0.420000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 12:00:00 | 97.000000 | 4.220000 | 5.570000 | 91.000000 | 1016.000000 |  | 5.570000 | 0.440000 | 10000.000000 | 12.000000 | 0.88 | 0.440000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 13:00:00 | 100.000000 | 7.520000 | 9.570000 | 87.000000 | 1017.000000 |  | 9.570000 | 2.450000 | 10000.000000 | 44.000000 | 1.17 | 0.650000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 14:00:00 | 96.000000 | 8.430000 | 10.900000 | 81.000000 | 1017.000000 |  | 11.570000 | 5.780000 | 10000.000000 | 23.000000 | 1.48 | 0.760000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 15:00:00 | 86.000000 | 8.260000 | 11.840000 | 75.000000 | 1016.000000 |  | 12.570000 | 9.690000 | 10000.000000 | 11.000000 | 1.9 | 0.920000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 16:00:00 | 85.000000 | 8.830000 | 12.890000 | 73.000000 | 1015.000000 |  | 13.570000 | 12.740000 | 10000.000000 | 354.000000 | 2.11 | 1.060000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 17:00:00 | 83.000000 | 10.960000 | 15.110000 | 74.000000 | 1014.000000 |  | 15.570000 | 13.860000 | 10000.000000 | 352.000000 | 2.56 | 1.130000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 18:00:00 | 82.000000 | 10.970000 | 14.150000 | 79.000000 | 1013.000000 |  | 14.570000 | 12.600000 | 10000.000000 | 337.000000 | 2.32 | 1.010000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 19:00:00 | 95.000000 | 12.880000 | 15.380000 | 84.000000 | 1012.000000 |  | 15.570000 | 8.920000 | 7792.000000 | 328.000000 | 2.12 | 0.800000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 20:00:00 | 97.000000 | 14.610000 | 15.640000 | 94.000000 | 1012.000000 |  | 15.570000 | 5.220000 | 3552.000000 | 304.000000 | 1.92 | 0.690000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 21:00:00 | 98.000000 | 11.950000 | 12.390000 | 96.000000 | 1012.000000 |  | 12.570000 | 2.150000 | 533.000000 | 306.000000 | 1.69 | 0.590000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 22:00:00 | 99.000000 | 12.260000 | 12.440000 | 98.000000 | 1013.000000 |  | 12.570000 | 0.500000 | 140.000000 | 348.000000 | 1.51 | 0.300000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 23:00:00 | 99.000000 | 11.420000 | 11.370000 | 99.000000 | 1014.000000 |  | 11.570000 | 0.000000 | 141.000000 | 52.000000 | 1.04 | 0.430000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35025070_OWM_Clouds_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Clouds_20220213.png)
![CNE_IDEAM_Station35025070_OWM_Dewpoint_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Dewpoint_20220213.png)
![CNE_IDEAM_Station35025070_OWM_Feelslike_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Feelslike_20220213.png)
![CNE_IDEAM_Station35025070_OWM_Humidity_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Humidity_20220213.png)
![CNE_IDEAM_Station35025070_OWM_Pressure_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Pressure_20220213.png)
![CNE_IDEAM_Station35025070_OWM_Rain_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Rain_20220213.png)
![CNE_IDEAM_Station35025070_OWM_Temp_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Temp_20220213.png)
![CNE_IDEAM_Station35025070_OWM_UVI_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_UVI_20220213.png)
![CNE_IDEAM_Station35025070_OWM_Visibility_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Visibility_20220213.png)
![CNE_IDEAM_Station35025070_OWM_Winddeg_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Winddeg_20220213.png)
![CNE_IDEAM_Station35025070_OWM_Windgust_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Windgust_20220213.png)
![CNE_IDEAM_Station35025070_OWM_Windspeed_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Windspeed_20220213.png)

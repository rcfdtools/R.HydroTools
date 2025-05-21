
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

* Current date time: 2022-02-10 14:08:04.180886
* Unix time to eval: 1644329284
* Days before (for historical data): 2
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220210.xls
* CNE IDEAM file downloaded and updated: No
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35025070_OWM_20220210.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220210.csv)

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
{'lat': 4.1967, 'lon': -74.1909, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644329284, 'sunrise': 1644318722, 'sunset': 1644361797, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1019, 'humidity': 88, 'dew_point': 7.49, 'uvi': 3.32, 'clouds': 93, 'visibility': 9938, 'wind_speed': 0.25, 'wind_deg': 57, 'wind_gust': 1.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644278400, 'temp': 9.57, 'feels_like': 9.29, 'pressure': 1017, 'humidity': 94, 'dew_point': 8.65, 'uvi': 0, 'clouds': 100, 'visibility': 8658, 'wind_speed': 1.38, 'wind_deg': 115, 'wind_gust': 2.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644282000, 'temp': 9.57, 'feels_like': 9.22, 'pressure': 1018, 'humidity': 94, 'dew_point': 8.65, 'uvi': 0, 'clouds': 100, 'visibility': 7037, 'wind_speed': 1.44, 'wind_deg': 109, 'wind_gust': 2.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644285600, 'temp': 8.57, 'feels_like': 7.89, 'pressure': 1019, 'humidity': 94, 'dew_point': 7.66, 'uvi': 0, 'clouds': 100, 'visibility': 2672, 'wind_speed': 1.62, 'wind_deg': 98, 'wind_gust': 2.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644289200, 'temp': 8.57, 'feels_like': 8.19, 'pressure': 1019, 'humidity': 94, 'dew_point': 7.66, 'uvi': 0, 'clouds': 100, 'visibility': 502, 'wind_speed': 1.35, 'wind_deg': 95, 'wind_gust': 2.04, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 2.73}}, {'dt': 1644292800, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1019, 'humidity': 94, 'dew_point': 7.66, 'uvi': 0, 'clouds': 100, 'visibility': 2206, 'wind_speed': 0.66, 'wind_deg': 104, 'wind_gust': 1.31, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.75}}, {'dt': 1644296400, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1019, 'humidity': 94, 'dew_point': 7.66, 'uvi': 0, 'clouds': 100, 'visibility': 6257, 'wind_speed': 0.24, 'wind_deg': 77, 'wind_gust': 1, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 3.16}}, {'dt': 1644300000, 'temp': 7.57, 'feels_like': 7.57, 'pressure': 1018, 'humidity': 96, 'dew_point': 6.97, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.09, 'wind_deg': 19, 'wind_gust': 0.8, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.78}}, {'dt': 1644303600, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1017, 'humidity': 94, 'dew_point': 7.66, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 80, 'wind_gust': 0.87, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.78}}, {'dt': 1644307200, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1017, 'humidity': 94, 'dew_point': 7.66, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.11, 'wind_deg': 179, 'wind_gust': 0.75, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 2.05}}, {'dt': 1644310800, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1017, 'humidity': 93, 'dew_point': 7.5, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 128, 'wind_gust': 0.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1644314400, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1017, 'humidity': 93, 'dew_point': 7.5, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 113, 'wind_gust': 0.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644318000, 'temp': 7.57, 'feels_like': 7.57, 'pressure': 1018, 'humidity': 93, 'dew_point': 6.51, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 103, 'wind_gust': 1.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644321600, 'temp': 7.57, 'feels_like': 7.57, 'pressure': 1018, 'humidity': 93, 'dew_point': 6.51, 'uvi': 0.07, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 103, 'wind_gust': 1.45, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644325200, 'temp': 9.57, 'feels_like': 9.57, 'pressure': 1019, 'humidity': 90, 'dew_point': 8.01, 'uvi': 1.41, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 88, 'wind_gust': 1.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644328800, 'temp': 9.57, 'feels_like': 9.57, 'pressure': 1019, 'humidity': 88, 'dew_point': 7.68, 'uvi': 3.32, 'clouds': 93, 'visibility': 9938, 'wind_speed': 0.25, 'wind_deg': 57, 'wind_gust': 1.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644332400, 'temp': 10.57, 'feels_like': 9.93, 'pressure': 1019, 'humidity': 86, 'dew_point': 8.33, 'uvi': 5.57, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 57, 'wind_gust': 1.73, 'weather': [{'id': 503, 'main': 'Rain', 'description': 'very heavy rain', 'icon': '10d'}], 'rain': {'1h': 23.68}}, {'dt': 1644336000, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1018, 'humidity': 90, 'dew_point': 7.03, 'uvi': 5.67, 'clouds': 96, 'visibility': 7242, 'wind_speed': 0.06, 'wind_deg': 160, 'wind_gust': 1.43, 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'}], 'rain': {'1h': 13.32}}, {'dt': 1644339600, 'temp': 7.57, 'feels_like': 7.57, 'pressure': 1017, 'humidity': 92, 'dew_point': 6.36, 'uvi': 6.17, 'clouds': 96, 'visibility': 6688, 'wind_speed': 0.34, 'wind_deg': 56, 'wind_gust': 1.51, 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'}], 'rain': {'1h': 4.86}}, {'dt': 1644343200, 'temp': 9.57, 'feels_like': 9.57, 'pressure': 1016, 'humidity': 91, 'dew_point': 8.18, 'uvi': 5.61, 'clouds': 100, 'visibility': 5048, 'wind_speed': 0.33, 'wind_deg': 3, 'wind_gust': 1.17, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, {'dt': 1644346800, 'temp': 10.57, 'feels_like': 10.14, 'pressure': 1015, 'humidity': 94, 'dew_point': 9.65, 'uvi': 5.44, 'clouds': 100, 'visibility': 4536, 'wind_speed': 0.2, 'wind_deg': 346, 'wind_gust': 0.99, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644350400, 'temp': 10.57, 'feels_like': 10.19, 'pressure': 1015, 'humidity': 96, 'dew_point': 9.96, 'uvi': 3.18, 'clouds': 100, 'visibility': 1167, 'wind_speed': 0.26, 'wind_deg': 342, 'wind_gust': 1.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644354000, 'temp': 11.57, 'feels_like': 11.29, 'pressure': 1015, 'humidity': 96, 'dew_point': 10.95, 'uvi': 1.31, 'clouds': 100, 'visibility': 3153, 'wind_speed': 0.36, 'wind_deg': 42, 'wind_gust': 1.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644357600, 'temp': 11.57, 'feels_like': 11.29, 'pressure': 1016, 'humidity': 96, 'dew_point': 10.95, 'uvi': 0.5, 'clouds': 100, 'visibility': 4470, 'wind_speed': 0.59, 'wind_deg': 88, 'wind_gust': 1.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644361200, 'temp': 10.57, 'feels_like': 10.22, 'pressure': 1017, 'humidity': 97, 'dew_point': 10.11, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 100, 'wind_gust': 1.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 00:00:00 | 100.000000 | 8.650000 | 9.290000 | 94.000000 | 1017.000000 |  | 9.570000 | 0.000000 | 8658.000000 | 115.000000 | 2.04 | 1.380000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 01:00:00 | 100.000000 | 8.650000 | 9.220000 | 94.000000 | 1018.000000 |  | 9.570000 | 0.000000 | 7037.000000 | 109.000000 | 2.05 | 1.440000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 02:00:00 | 100.000000 | 7.660000 | 7.890000 | 94.000000 | 1019.000000 |  | 8.570000 | 0.000000 | 2672.000000 | 98.000000 | 2.32 | 1.620000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 03:00:00 | 100.000000 | 7.660000 | 8.190000 | 94.000000 | 1019.000000 | 2.73 | 8.570000 | 0.000000 | 502.000000 | 95.000000 | 2.04 | 1.350000 | 501 | Rain | moderate rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 04:00:00 | 100.000000 | 7.660000 | 8.570000 | 94.000000 | 1019.000000 | 0.75 | 8.570000 | 0.000000 | 2206.000000 | 104.000000 | 1.31 | 0.660000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 05:00:00 | 100.000000 | 7.660000 | 8.570000 | 94.000000 | 1019.000000 | 3.16 | 8.570000 | 0.000000 | 6257.000000 | 77.000000 | 1 | 0.240000 | 501 | Rain | moderate rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 06:00:00 | 100.000000 | 6.970000 | 7.570000 | 96.000000 | 1018.000000 | 1.78 | 7.570000 | 0.000000 | 10000.000000 | 19.000000 | 0.8 | 0.090000 | 501 | Rain | moderate rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 07:00:00 | 100.000000 | 7.660000 | 8.570000 | 94.000000 | 1017.000000 | 1.78 | 8.570000 | 0.000000 | 10000.000000 | 80.000000 | 0.87 | 0.210000 | 501 | Rain | moderate rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 08:00:00 | 100.000000 | 7.660000 | 8.570000 | 94.000000 | 1017.000000 | 2.05 | 8.570000 | 0.000000 | 10000.000000 | 179.000000 | 0.75 | 0.110000 | 501 | Rain | moderate rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 09:00:00 | 100.000000 | 7.500000 | 8.570000 | 93.000000 | 1017.000000 | 0.15 | 8.570000 | 0.000000 | 10000.000000 | 128.000000 | 0.73 | 0.320000 | 500 | Rain | light rain | 10n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 10:00:00 | 100.000000 | 7.500000 | 8.570000 | 93.000000 | 1017.000000 |  | 8.570000 | 0.000000 | 10000.000000 | 113.000000 | 0.92 | 0.780000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 11:00:00 | 100.000000 | 6.510000 | 7.570000 | 93.000000 | 1018.000000 |  | 7.570000 | 0.000000 | 10000.000000 | 103.000000 | 1.11 | 0.840000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 12:00:00 | 98.000000 | 6.510000 | 7.570000 | 93.000000 | 1018.000000 |  | 7.570000 | 0.070000 | 10000.000000 | 103.000000 | 1.45 | 0.920000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 13:00:00 | 99.000000 | 8.010000 | 9.570000 | 90.000000 | 1019.000000 |  | 9.570000 | 1.410000 | 10000.000000 | 88.000000 | 1.76 | 0.830000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 14:00:00 | 93.000000 | 7.680000 | 9.570000 | 88.000000 | 1019.000000 |  | 9.570000 | 3.320000 | 9938.000000 | 57.000000 | 1.49 | 0.250000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 15:00:00 | 94.000000 | 8.330000 | 9.930000 | 86.000000 | 1019.000000 | 23.68 | 10.570000 | 5.570000 | 10000.000000 | 57.000000 | 1.73 | 0.250000 | 503 | Rain | very heavy rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 16:00:00 | 96.000000 | 7.030000 | 8.570000 | 90.000000 | 1018.000000 | 13.32 | 8.570000 | 5.670000 | 7242.000000 | 160.000000 | 1.43 | 0.060000 | 502 | Rain | heavy intensity rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 17:00:00 | 96.000000 | 6.360000 | 7.570000 | 92.000000 | 1017.000000 | 4.86 | 7.570000 | 6.170000 | 6688.000000 | 56.000000 | 1.51 | 0.340000 | 502 | Rain | heavy intensity rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 18:00:00 | 100.000000 | 8.180000 | 9.570000 | 91.000000 | 1016.000000 | 0.56 | 9.570000 | 5.610000 | 5048.000000 | 3.000000 | 1.17 | 0.330000 | 500 | Rain | light rain | 10d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 19:00:00 | 100.000000 | 9.650000 | 10.140000 | 94.000000 | 1015.000000 |  | 10.570000 | 5.440000 | 4536.000000 | 346.000000 | 0.99 | 0.200000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 20:00:00 | 100.000000 | 9.960000 | 10.190000 | 96.000000 | 1015.000000 |  | 10.570000 | 3.180000 | 1167.000000 | 342.000000 | 1.12 | 0.260000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 21:00:00 | 100.000000 | 10.950000 | 11.290000 | 96.000000 | 1015.000000 |  | 11.570000 | 1.310000 | 3153.000000 | 42.000000 | 1.31 | 0.360000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 22:00:00 | 100.000000 | 10.950000 | 11.290000 | 96.000000 | 1016.000000 |  | 11.570000 | 0.500000 | 4470.000000 | 88.000000 | 1.52 | 0.590000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 23:00:00 | 100.000000 | 10.110000 | 10.220000 | 97.000000 | 1017.000000 |  | 10.570000 | 0.000000 | 10000.000000 | 100.000000 | 1.16 | 0.430000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35025070_OWM_Clouds_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Clouds_20220210.png)
![CNE_IDEAM_Station35025070_OWM_Dewpoint_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Dewpoint_20220210.png)
![CNE_IDEAM_Station35025070_OWM_Feelslike_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Feelslike_20220210.png)
![CNE_IDEAM_Station35025070_OWM_Humidity_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Humidity_20220210.png)
![CNE_IDEAM_Station35025070_OWM_Pressure_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Pressure_20220210.png)
![CNE_IDEAM_Station35025070_OWM_Rain_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Rain_20220210.png)
![CNE_IDEAM_Station35025070_OWM_Temp_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Temp_20220210.png)
![CNE_IDEAM_Station35025070_OWM_UVI_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_UVI_20220210.png)
![CNE_IDEAM_Station35025070_OWM_Visibility_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Visibility_20220210.png)
![CNE_IDEAM_Station35025070_OWM_Winddeg_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Winddeg_20220210.png)
![CNE_IDEAM_Station35025070_OWM_Windgust_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Windgust_20220210.png)
![CNE_IDEAM_Station35025070_OWM_Windspeed_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Windspeed_20220210.png)

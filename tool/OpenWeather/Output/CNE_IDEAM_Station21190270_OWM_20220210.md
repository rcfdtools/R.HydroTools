
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SAN JUAN [21190270] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21190270_OWM_20220210.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220210.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.03102778,-74.31116667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.03102778&lon=-74.31116667)

| Parameter | Value |
|---|---|
| Code | 21190270 |
| Name | SAN JUAN [21190270] |
| Latitude, ° | 4.03102778 |
| Longitude, ° | -74.31116667 |
| Elevation, m | 2900 |
| Category | Pluviométrica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1972-06-15 00:00:00 |
| Suspension date | NaT |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Cucuana |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Sumapaz |

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

### (CNE index 1321) Open Weather values for station 21190270 - SAN JUAN [21190270]

JSON data from API OWM:

```
{'lat': 4.031, 'lon': -74.3112, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644329284, 'sunrise': 1644318740, 'sunset': 1644361837, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1019, 'humidity': 86, 'dew_point': 6.36, 'uvi': 3.32, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 122, 'wind_gust': 1.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644278400, 'temp': 6.57, 'feels_like': 5.17, 'pressure': 1017, 'humidity': 94, 'dew_point': 5.67, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.03, 'wind_deg': 112, 'wind_gust': 2.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644282000, 'temp': 6.6, 'feels_like': 5.34, 'pressure': 1018, 'humidity': 92, 'dew_point': 5.4, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.89, 'wind_deg': 115, 'wind_gust': 2.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644285600, 'temp': 6.14, 'feels_like': 4.75, 'pressure': 1019, 'humidity': 93, 'dew_point': 5.09, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.95, 'wind_deg': 106, 'wind_gust': 2.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.65}}, {'dt': 1644289200, 'temp': 6.49, 'feels_like': 5.22, 'pressure': 1019, 'humidity': 94, 'dew_point': 5.6, 'uvi': 0, 'clouds': 100, 'visibility': 3493, 'wind_speed': 1.88, 'wind_deg': 109, 'wind_gust': 2.23, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.15}}, {'dt': 1644292800, 'temp': 6.67, 'feels_like': 5.7, 'pressure': 1019, 'humidity': 92, 'dew_point': 5.46, 'uvi': 0, 'clouds': 100, 'visibility': 9631, 'wind_speed': 1.63, 'wind_deg': 120, 'wind_gust': 1.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 1}}, {'dt': 1644296400, 'temp': 6.57, 'feels_like': 6.57, 'pressure': 1019, 'humidity': 93, 'dew_point': 5.52, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 119, 'wind_gust': 1.04, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 3.16}}, {'dt': 1644300000, 'temp': 5.82, 'feels_like': 5.82, 'pressure': 1018, 'humidity': 95, 'dew_point': 5.08, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 114, 'wind_gust': 0.79, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 2.73}}, {'dt': 1644303600, 'temp': 5.45, 'feels_like': 5.45, 'pressure': 1017, 'humidity': 94, 'dew_point': 4.56, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 99, 'wind_gust': 0.91, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 3.16}}, {'dt': 1644307200, 'temp': 5.32, 'feels_like': 5.32, 'pressure': 1017, 'humidity': 94, 'dew_point': 4.43, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 109, 'wind_gust': 0.94, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.78}}, {'dt': 1644310800, 'temp': 5.15, 'feels_like': 5.15, 'pressure': 1017, 'humidity': 94, 'dew_point': 4.27, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 111, 'wind_gust': 1.04, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 2.05}}, {'dt': 1644314400, 'temp': 5.17, 'feels_like': 4.23, 'pressure': 1017, 'humidity': 94, 'dew_point': 4.28, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 111, 'wind_gust': 1.27, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644318000, 'temp': 5.16, 'feels_like': 4.16, 'pressure': 1018, 'humidity': 93, 'dew_point': 4.12, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.48, 'wind_deg': 110, 'wind_gust': 1.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644321600, 'temp': 5.88, 'feels_like': 4.94, 'pressure': 1019, 'humidity': 92, 'dew_point': 4.68, 'uvi': 0.07, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 110, 'wind_gust': 1.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644325200, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1019, 'humidity': 89, 'dew_point': 5.68, 'uvi': 1.41, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 108, 'wind_gust': 1.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644328800, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1019, 'humidity': 86, 'dew_point': 6.36, 'uvi': 3.32, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 122, 'wind_gust': 1.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644332400, 'temp': 8.69, 'feels_like': 8.69, 'pressure': 1019, 'humidity': 87, 'dew_point': 6.65, 'uvi': 5.57, 'clouds': 95, 'visibility': 8638, 'wind_speed': 0.22, 'wind_deg': 115, 'wind_gust': 1.72, 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'}], 'rain': {'1h': 8.65}}, {'dt': 1644336000, 'temp': 8.53, 'feels_like': 8.53, 'pressure': 1018, 'humidity': 89, 'dew_point': 6.82, 'uvi': 5.67, 'clouds': 97, 'visibility': 6895, 'wind_speed': 0.25, 'wind_deg': 136, 'wind_gust': 1.52, 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'}], 'rain': {'1h': 5.62}}, {'dt': 1644339600, 'temp': 8.8, 'feels_like': 8.8, 'pressure': 1017, 'humidity': 88, 'dew_point': 6.92, 'uvi': 6.17, 'clouds': 97, 'visibility': 6293, 'wind_speed': 0.13, 'wind_deg': 101, 'wind_gust': 1.54, 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'}], 'rain': {'1h': 15.38}}, {'dt': 1644343200, 'temp': 8.48, 'feels_like': 8.48, 'pressure': 1016, 'humidity': 89, 'dew_point': 6.77, 'uvi': 5.61, 'clouds': 100, 'visibility': 6117, 'wind_speed': 0.1, 'wind_deg': 359, 'wind_gust': 1.16, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.15}}, {'dt': 1644346800, 'temp': 7.96, 'feels_like': 7.96, 'pressure': 1016, 'humidity': 92, 'dew_point': 6.74, 'uvi': 5.44, 'clouds': 100, 'visibility': 7217, 'wind_speed': 0.04, 'wind_deg': 188, 'wind_gust': 1.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.75}}, {'dt': 1644350400, 'temp': 7.44, 'feels_like': 7.44, 'pressure': 1015, 'humidity': 93, 'dew_point': 6.38, 'uvi': 3.18, 'clouds': 100, 'visibility': 4078, 'wind_speed': 0.26, 'wind_deg': 84, 'wind_gust': 1.37, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644354000, 'temp': 7.01, 'feels_like': 7.01, 'pressure': 1015, 'humidity': 93, 'dew_point': 5.96, 'uvi': 1.31, 'clouds': 100, 'visibility': 4806, 'wind_speed': 0.58, 'wind_deg': 85, 'wind_gust': 1.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644357600, 'temp': 6.77, 'feels_like': 6.77, 'pressure': 1016, 'humidity': 95, 'dew_point': 6.03, 'uvi': 0.5, 'clouds': 100, 'visibility': 4957, 'wind_speed': 0.96, 'wind_deg': 102, 'wind_gust': 1.64, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644361200, 'temp': 6.53, 'feels_like': 6.53, 'pressure': 1017, 'humidity': 95, 'dew_point': 5.79, 'uvi': 0, 'clouds': 99, 'visibility': 3827, 'wind_speed': 0.92, 'wind_deg': 116, 'wind_gust': 1.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 00:00:00 | 100.000000 | 5.670000 | 5.170000 | 94.000000 | 1017.000000 |  | 6.570000 | 0.000000 | 10000.000000 | 112.000000 | 2.41 | 2.030000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 01:00:00 | 100.000000 | 5.400000 | 5.340000 | 92.000000 | 1018.000000 |  | 6.600000 | 0.000000 | 10000.000000 | 115.000000 | 2.18 | 1.890000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 02:00:00 | 100.000000 | 5.090000 | 4.750000 | 93.000000 | 1019.000000 | 0.65 | 6.140000 | 0.000000 | 10000.000000 | 106.000000 | 2.23 | 1.950000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 03:00:00 | 100.000000 | 5.600000 | 5.220000 | 94.000000 | 1019.000000 | 1.15 | 6.490000 | 0.000000 | 3493.000000 | 109.000000 | 2.23 | 1.880000 | 501 | Rain | moderate rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 04:00:00 | 100.000000 | 5.460000 | 5.700000 | 92.000000 | 1019.000000 | 1 | 6.670000 | 0.000000 | 9631.000000 | 120.000000 | 1.79 | 1.630000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 05:00:00 | 100.000000 | 5.520000 | 6.570000 | 93.000000 | 1019.000000 | 3.16 | 6.570000 | 0.000000 | 10000.000000 | 119.000000 | 1.04 | 0.960000 | 501 | Rain | moderate rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 06:00:00 | 100.000000 | 5.080000 | 5.820000 | 95.000000 | 1018.000000 | 2.73 | 5.820000 | 0.000000 | 10000.000000 | 114.000000 | 0.79 | 0.690000 | 501 | Rain | moderate rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 07:00:00 | 100.000000 | 4.560000 | 5.450000 | 94.000000 | 1017.000000 | 3.16 | 5.450000 | 0.000000 | 10000.000000 | 99.000000 | 0.91 | 0.810000 | 501 | Rain | moderate rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 08:00:00 | 100.000000 | 4.430000 | 5.320000 | 94.000000 | 1017.000000 | 1.78 | 5.320000 | 0.000000 | 10000.000000 | 109.000000 | 0.94 | 0.830000 | 501 | Rain | moderate rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 09:00:00 | 100.000000 | 4.270000 | 5.150000 | 94.000000 | 1017.000000 | 2.05 | 5.150000 | 0.000000 | 10000.000000 | 111.000000 | 1.04 | 1.070000 | 501 | Rain | moderate rain | 10n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 10:00:00 | 100.000000 | 4.280000 | 4.230000 | 94.000000 | 1017.000000 |  | 5.170000 | 0.000000 | 10000.000000 | 111.000000 | 1.27 | 1.430000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 11:00:00 | 100.000000 | 4.120000 | 4.160000 | 93.000000 | 1018.000000 |  | 5.160000 | 0.000000 | 10000.000000 | 110.000000 | 1.38 | 1.480000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 12:00:00 | 90.000000 | 4.680000 | 4.940000 | 92.000000 | 1019.000000 |  | 5.880000 | 0.070000 | 10000.000000 | 110.000000 | 1.78 | 1.510000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 13:00:00 | 96.000000 | 5.680000 | 7.370000 | 89.000000 | 1019.000000 |  | 7.370000 | 1.410000 | 10000.000000 | 108.000000 | 1.92 | 0.860000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 14:00:00 | 93.000000 | 6.360000 | 8.570000 | 86.000000 | 1019.000000 |  | 8.570000 | 3.320000 | 10000.000000 | 122.000000 | 1.89 | 0.300000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 15:00:00 | 95.000000 | 6.650000 | 8.690000 | 87.000000 | 1019.000000 | 8.65 | 8.690000 | 5.570000 | 8638.000000 | 115.000000 | 1.72 | 0.220000 | 502 | Rain | heavy intensity rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 16:00:00 | 97.000000 | 6.820000 | 8.530000 | 89.000000 | 1018.000000 | 5.62 | 8.530000 | 5.670000 | 6895.000000 | 136.000000 | 1.52 | 0.250000 | 502 | Rain | heavy intensity rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 17:00:00 | 97.000000 | 6.920000 | 8.800000 | 88.000000 | 1017.000000 | 15.38 | 8.800000 | 6.170000 | 6293.000000 | 101.000000 | 1.54 | 0.130000 | 502 | Rain | heavy intensity rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 18:00:00 | 100.000000 | 6.770000 | 8.480000 | 89.000000 | 1016.000000 | 1.15 | 8.480000 | 5.610000 | 6117.000000 | 359.000000 | 1.16 | 0.100000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 19:00:00 | 100.000000 | 6.740000 | 7.960000 | 92.000000 | 1016.000000 | 0.75 | 7.960000 | 5.440000 | 7217.000000 | 188.000000 | 1.18 | 0.040000 | 500 | Rain | light rain | 10d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 20:00:00 | 100.000000 | 6.380000 | 7.440000 | 93.000000 | 1015.000000 |  | 7.440000 | 3.180000 | 4078.000000 | 84.000000 | 1.37 | 0.260000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 21:00:00 | 100.000000 | 5.960000 | 7.010000 | 93.000000 | 1015.000000 |  | 7.010000 | 1.310000 | 4806.000000 | 85.000000 | 1.29 | 0.580000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 22:00:00 | 100.000000 | 6.030000 | 6.770000 | 95.000000 | 1016.000000 |  | 6.770000 | 0.500000 | 4957.000000 | 102.000000 | 1.64 | 0.960000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-08 23:00:00 | 99.000000 | 5.790000 | 6.530000 | 95.000000 | 1017.000000 |  | 6.530000 | 0.000000 | 3827.000000 | 116.000000 | 1.16 | 0.920000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21190270_OWM_Clouds_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Clouds_20220210.png)
![CNE_IDEAM_Station21190270_OWM_Dewpoint_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Dewpoint_20220210.png)
![CNE_IDEAM_Station21190270_OWM_Feelslike_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Feelslike_20220210.png)
![CNE_IDEAM_Station21190270_OWM_Humidity_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Humidity_20220210.png)
![CNE_IDEAM_Station21190270_OWM_Pressure_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Pressure_20220210.png)
![CNE_IDEAM_Station21190270_OWM_Rain_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Rain_20220210.png)
![CNE_IDEAM_Station21190270_OWM_Temp_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Temp_20220210.png)
![CNE_IDEAM_Station21190270_OWM_UVI_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_UVI_20220210.png)
![CNE_IDEAM_Station21190270_OWM_Visibility_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Visibility_20220210.png)
![CNE_IDEAM_Station21190270_OWM_Winddeg_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Winddeg_20220210.png)
![CNE_IDEAM_Station21190270_OWM_Windgust_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Windgust_20220210.png)
![CNE_IDEAM_Station21190270_OWM_Windspeed_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Windspeed_20220210.png)

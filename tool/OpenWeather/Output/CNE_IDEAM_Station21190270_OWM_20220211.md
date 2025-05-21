
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21190270_OWM_20220211.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220211.csv)

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
{'lat': 4.031, 'lon': -74.3112, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644427498, 'sunrise': 1644405137, 'sunset': 1644448245, 'temp': 8.86, 'feels_like': 8.86, 'pressure': 1017, 'humidity': 90, 'dew_point': 7.31, 'uvi': 12.94, 'clouds': 99, 'visibility': 2021, 'wind_speed': 0.23, 'wind_deg': 101, 'wind_gust': 1.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644364800, 'temp': 6.71, 'feels_like': 6.71, 'pressure': 1017, 'humidity': 95, 'dew_point': 5.97, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 106, 'wind_gust': 1.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644368400, 'temp': 6.65, 'feels_like': 6.65, 'pressure': 1018, 'humidity': 94, 'dew_point': 5.75, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.1, 'wind_deg': 115, 'wind_gust': 1.27, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644372000, 'temp': 6.55, 'feels_like': 6.55, 'pressure': 1019, 'humidity': 94, 'dew_point': 5.66, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 109, 'wind_gust': 1.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644375600, 'temp': 6.5, 'feels_like': 6.5, 'pressure': 1019, 'humidity': 93, 'dew_point': 5.45, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 112, 'wind_gust': 1.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644379200, 'temp': 6.4, 'feels_like': 5.62, 'pressure': 1019, 'humidity': 92, 'dew_point': 5.2, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 117, 'wind_gust': 1.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644382800, 'temp': 6.01, 'feels_like': 6.01, 'pressure': 1019, 'humidity': 92, 'dew_point': 4.81, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 118, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644386400, 'temp': 5.49, 'feels_like': 5.49, 'pressure': 1018, 'humidity': 93, 'dew_point': 4.45, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 106, 'wind_gust': 1.33, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644390000, 'temp': 5.35, 'feels_like': 5.35, 'pressure': 1017, 'humidity': 94, 'dew_point': 4.46, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 108, 'wind_gust': 1.26, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644393600, 'temp': 5.44, 'feels_like': 5.44, 'pressure': 1016, 'humidity': 94, 'dew_point': 4.55, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 107, 'wind_gust': 1.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644397200, 'temp': 5.46, 'feels_like': 5.46, 'pressure': 1016, 'humidity': 93, 'dew_point': 4.42, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.21, 'wind_deg': 111, 'wind_gust': 1.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644400800, 'temp': 5.69, 'feels_like': 5.69, 'pressure': 1017, 'humidity': 93, 'dew_point': 4.65, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 108, 'wind_gust': 1.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644404400, 'temp': 5.67, 'feels_like': 5.67, 'pressure': 1017, 'humidity': 93, 'dew_point': 4.63, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 104, 'wind_gust': 1.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644408000, 'temp': 6.27, 'feels_like': 6.27, 'pressure': 1018, 'humidity': 90, 'dew_point': 4.75, 'uvi': 0.15, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 92, 'wind_gust': 1.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644411600, 'temp': 7.61, 'feels_like': 7.61, 'pressure': 1018, 'humidity': 86, 'dew_point': 5.42, 'uvi': 2.26, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 80, 'wind_gust': 1.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644415200, 'temp': 8.84, 'feels_like': 8.84, 'pressure': 1018, 'humidity': 84, 'dew_point': 6.29, 'uvi': 5.32, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 75, 'wind_gust': 1.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644418800, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1018, 'humidity': 84, 'dew_point': 6.81, 'uvi': 8.92, 'clouds': 99, 'visibility': 5315, 'wind_speed': 0.17, 'wind_deg': 30, 'wind_gust': 1.62, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644422400, 'temp': 9, 'feels_like': 9, 'pressure': 1018, 'humidity': 88, 'dew_point': 7.12, 'uvi': 11.89, 'clouds': 99, 'visibility': 1748, 'wind_speed': 0.16, 'wind_deg': 39, 'wind_gust': 1.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644426000, 'temp': 8.86, 'feels_like': 8.86, 'pressure': 1017, 'humidity': 90, 'dew_point': 7.31, 'uvi': 12.94, 'clouds': 99, 'visibility': 2021, 'wind_speed': 0.23, 'wind_deg': 101, 'wind_gust': 1.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644429600, 'temp': 8.62, 'feels_like': 8.62, 'pressure': 1016, 'humidity': 92, 'dew_point': 7.4, 'uvi': 11.76, 'clouds': 97, 'visibility': 936, 'wind_speed': 0.33, 'wind_deg': 138, 'wind_gust': 1.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644433200, 'temp': 8.27, 'feels_like': 8.27, 'pressure': 1015, 'humidity': 93, 'dew_point': 7.21, 'uvi': 8.13, 'clouds': 99, 'visibility': 1080, 'wind_speed': 0.42, 'wind_deg': 118, 'wind_gust': 1.64, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1644436800, 'temp': 8.14, 'feels_like': 8.14, 'pressure': 1014, 'humidity': 92, 'dew_point': 6.92, 'uvi': 4.75, 'clouds': 99, 'visibility': 1232, 'wind_speed': 0.63, 'wind_deg': 101, 'wind_gust': 1.62, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.73}}, {'dt': 1644440400, 'temp': 7.95, 'feels_like': 7.95, 'pressure': 1014, 'humidity': 92, 'dew_point': 6.73, 'uvi': 1.96, 'clouds': 99, 'visibility': 4693, 'wind_speed': 0.74, 'wind_deg': 85, 'wind_gust': 1.49, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.73}}, {'dt': 1644444000, 'temp': 8.01, 'feels_like': 8.01, 'pressure': 1014, 'humidity': 91, 'dew_point': 6.63, 'uvi': 0.4, 'clouds': 98, 'visibility': 3060, 'wind_speed': 0.68, 'wind_deg': 90, 'wind_gust': 1.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644447600, 'temp': 7.41, 'feels_like': 7.41, 'pressure': 1015, 'humidity': 96, 'dew_point': 6.81, 'uvi': 0, 'clouds': 98, 'visibility': 1969, 'wind_speed': 1.1, 'wind_deg': 92, 'wind_gust': 1.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 00:00:00 | 99.000000 | 5.970000 | 6.710000 | 95.000000 | 1017.000000 |  | 6.710000 | 0.000000 | 10000.000000 | 106.000000 | 1.09 | 0.820000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 01:00:00 | 99.000000 | 5.750000 | 6.650000 | 94.000000 | 1018.000000 |  | 6.650000 | 0.000000 | 10000.000000 | 115.000000 | 1.27 | 1.100000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 02:00:00 | 100.000000 | 5.660000 | 6.550000 | 94.000000 | 1019.000000 |  | 6.550000 | 0.000000 | 10000.000000 | 109.000000 | 1.39 | 1.240000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 03:00:00 | 99.000000 | 5.450000 | 6.500000 | 93.000000 | 1019.000000 |  | 6.500000 | 0.000000 | 10000.000000 | 112.000000 | 1.36 | 1.310000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 04:00:00 | 98.000000 | 5.200000 | 5.620000 | 92.000000 | 1019.000000 |  | 6.400000 | 0.000000 | 10000.000000 | 117.000000 | 1.4 | 1.440000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 05:00:00 | 98.000000 | 4.810000 | 6.010000 | 92.000000 | 1019.000000 |  | 6.010000 | 0.000000 | 10000.000000 | 118.000000 | 1.18 | 1.180000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 06:00:00 | 74.000000 | 4.450000 | 5.490000 | 93.000000 | 1018.000000 |  | 5.490000 | 0.000000 | 10000.000000 | 106.000000 | 1.33 | 1.190000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 07:00:00 | 88.000000 | 4.460000 | 5.350000 | 94.000000 | 1017.000000 |  | 5.350000 | 0.000000 | 10000.000000 | 108.000000 | 1.26 | 1.180000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 08:00:00 | 91.000000 | 4.550000 | 5.440000 | 94.000000 | 1016.000000 |  | 5.440000 | 0.000000 | 10000.000000 | 107.000000 | 1.22 | 1.120000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 09:00:00 | 92.000000 | 4.420000 | 5.460000 | 93.000000 | 1016.000000 |  | 5.460000 | 0.000000 | 10000.000000 | 111.000000 | 1.17 | 1.210000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 10:00:00 | 93.000000 | 4.650000 | 5.690000 | 93.000000 | 1017.000000 |  | 5.690000 | 0.000000 | 10000.000000 | 108.000000 | 1.21 | 1.190000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 11:00:00 | 93.000000 | 4.630000 | 5.670000 | 93.000000 | 1017.000000 |  | 5.670000 | 0.000000 | 10000.000000 | 104.000000 | 1.24 | 1.240000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 12:00:00 | 92.000000 | 4.750000 | 6.270000 | 90.000000 | 1018.000000 |  | 6.270000 | 0.150000 | 10000.000000 | 92.000000 | 1.51 | 1.270000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 13:00:00 | 97.000000 | 5.420000 | 7.610000 | 86.000000 | 1018.000000 |  | 7.610000 | 2.260000 | 10000.000000 | 80.000000 | 1.48 | 0.660000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 14:00:00 | 98.000000 | 6.290000 | 8.840000 | 84.000000 | 1018.000000 |  | 8.840000 | 5.320000 | 10000.000000 | 75.000000 | 1.61 | 0.300000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 15:00:00 | 99.000000 | 6.810000 | 9.370000 | 84.000000 | 1018.000000 |  | 9.370000 | 8.920000 | 5315.000000 | 30.000000 | 1.62 | 0.170000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 16:00:00 | 99.000000 | 7.120000 | 9.000000 | 88.000000 | 1018.000000 |  | 9.000000 | 11.890000 | 1748.000000 | 39.000000 | 1.52 | 0.160000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 17:00:00 | 99.000000 | 7.310000 | 8.860000 | 90.000000 | 1017.000000 |  | 8.860000 | 12.940000 | 2021.000000 | 101.000000 | 1.5 | 0.230000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 18:00:00 | 97.000000 | 7.400000 | 8.620000 | 92.000000 | 1016.000000 |  | 8.620000 | 11.760000 | 936.000000 | 138.000000 | 1.68 | 0.330000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 19:00:00 | 99.000000 | 7.210000 | 8.270000 | 93.000000 | 1015.000000 | 0.36 | 8.270000 | 8.130000 | 1080.000000 | 118.000000 | 1.64 | 0.420000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 20:00:00 | 99.000000 | 6.920000 | 8.140000 | 92.000000 | 1014.000000 | 2.73 | 8.140000 | 4.750000 | 1232.000000 | 101.000000 | 1.62 | 0.630000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 21:00:00 | 99.000000 | 6.730000 | 7.950000 | 92.000000 | 1014.000000 | 2.73 | 7.950000 | 1.960000 | 4693.000000 | 85.000000 | 1.49 | 0.740000 | 501 | Rain | moderate rain | 10d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 22:00:00 | 98.000000 | 6.630000 | 8.010000 | 91.000000 | 1014.000000 |  | 8.010000 | 0.400000 | 3060.000000 | 90.000000 | 1.34 | 0.680000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-09 23:00:00 | 98.000000 | 6.810000 | 7.410000 | 96.000000 | 1015.000000 |  | 7.410000 | 0.000000 | 1969.000000 | 92.000000 | 1.67 | 1.100000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21190270_OWM_Clouds_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Clouds_20220211.png)
![CNE_IDEAM_Station21190270_OWM_Dewpoint_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Dewpoint_20220211.png)
![CNE_IDEAM_Station21190270_OWM_Feelslike_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Feelslike_20220211.png)
![CNE_IDEAM_Station21190270_OWM_Humidity_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Humidity_20220211.png)
![CNE_IDEAM_Station21190270_OWM_Pressure_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Pressure_20220211.png)
![CNE_IDEAM_Station21190270_OWM_Rain_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Rain_20220211.png)
![CNE_IDEAM_Station21190270_OWM_Temp_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Temp_20220211.png)
![CNE_IDEAM_Station21190270_OWM_UVI_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_UVI_20220211.png)
![CNE_IDEAM_Station21190270_OWM_Visibility_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Visibility_20220211.png)
![CNE_IDEAM_Station21190270_OWM_Winddeg_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Winddeg_20220211.png)
![CNE_IDEAM_Station21190270_OWM_Windgust_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Windgust_20220211.png)
![CNE_IDEAM_Station21190270_OWM_Windspeed_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Windspeed_20220211.png)

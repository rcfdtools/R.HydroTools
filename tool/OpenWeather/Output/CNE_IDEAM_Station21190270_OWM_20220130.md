
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

* Current date time: 2022-01-30 14:37:17.220329
* Unix time to eval: 1643467037
* Days before (for historical data): 1
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220130.xls
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21190270_OWM_20220130.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220130.csv)

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
| Latitude | latitud | lat | Geolocalization latitude degrees |
| Longitude | longitud | lon | Geolocalization longitude degrees |
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

### (CNE index 1323) Open Weather values for station 21190270 - SAN JUAN [21190270]

JSON data from API OWM:

```
{'lat': 4.031, 'lon': -74.3112, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643467037, 'sunrise': 1643454720, 'sunset': 1643497714, 'temp': 10.91, 'feels_like': 9.78, 'pressure': 1017, 'humidity': 66, 'dew_point': 4.81, 'uvi': 9.42, 'clouds': 18, 'visibility': 10000, 'wind_speed': 2.92, 'wind_deg': 310, 'wind_gust': 2.85, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, 'hourly': [{'dt': 1643414400, 'temp': 7.14, 'feels_like': 7.14, 'pressure': 1016, 'humidity': 94, 'dew_point': 6.24, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 69, 'wind_gust': 1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.53}}, {'dt': 1643418000, 'temp': 6.93, 'feels_like': 6.93, 'pressure': 1017, 'humidity': 93, 'dew_point': 5.88, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 41, 'wind_gust': 1.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.63}}, {'dt': 1643421600, 'temp': 7.24, 'feels_like': 7.24, 'pressure': 1018, 'humidity': 94, 'dew_point': 6.34, 'uvi': 0, 'clouds': 92, 'visibility': 3565, 'wind_speed': 0.46, 'wind_deg': 351, 'wind_gust': 1.78, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1643425200, 'temp': 7.27, 'feels_like': 7.27, 'pressure': 1018, 'humidity': 93, 'dew_point': 6.21, 'uvi': 0, 'clouds': 93, 'visibility': 8526, 'wind_speed': 0.73, 'wind_deg': 308, 'wind_gust': 1.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.97}}, {'dt': 1643428800, 'temp': 7.14, 'feels_like': 7.14, 'pressure': 1018, 'humidity': 93, 'dew_point': 6.09, 'uvi': 0, 'clouds': 93, 'visibility': 9867, 'wind_speed': 0.67, 'wind_deg': 299, 'wind_gust': 1.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643432400, 'temp': 6.91, 'feels_like': 6.91, 'pressure': 1018, 'humidity': 94, 'dew_point': 6.01, 'uvi': 0, 'clouds': 94, 'visibility': 5996, 'wind_speed': 0.53, 'wind_deg': 298, 'wind_gust': 1.62, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.21}}, {'dt': 1643436000, 'temp': 6.35, 'feels_like': 6.35, 'pressure': 1017, 'humidity': 94, 'dew_point': 5.46, 'uvi': 0, 'clouds': 93, 'visibility': 8190, 'wind_speed': 0.16, 'wind_deg': 82, 'wind_gust': 1.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643439600, 'temp': 5.6, 'feels_like': 5.6, 'pressure': 1017, 'humidity': 90, 'dew_point': 4.09, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 314, 'wind_gust': 2.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643443200, 'temp': 4.47, 'feels_like': 4.47, 'pressure': 1017, 'humidity': 94, 'dew_point': 3.59, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 316, 'wind_gust': 1.81, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643446800, 'temp': 4.61, 'feels_like': 4.61, 'pressure': 1017, 'humidity': 91, 'dew_point': 3.27, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 21, 'wind_gust': 1.88, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643450400, 'temp': 3.75, 'feels_like': 3.75, 'pressure': 1018, 'humidity': 94, 'dew_point': 2.88, 'uvi': 0, 'clouds': 47, 'visibility': 9466, 'wind_speed': 0.71, 'wind_deg': 342, 'wind_gust': 1.9, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643454000, 'temp': 3.58, 'feels_like': 3.58, 'pressure': 1019, 'humidity': 93, 'dew_point': 2.56, 'uvi': 0, 'clouds': 46, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 351, 'wind_gust': 1.85, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643457600, 'temp': 4.81, 'feels_like': 4.81, 'pressure': 1019, 'humidity': 89, 'dew_point': 3.15, 'uvi': 0.55, 'clouds': 30, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 353, 'wind_gust': 1.98, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643461200, 'temp': 7.6, 'feels_like': 6.58, 'pressure': 1019, 'humidity': 77, 'dew_point': 3.83, 'uvi': 2.37, 'clouds': 39, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 319, 'wind_gust': 2.38, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643464800, 'temp': 9.29, 'feels_like': 8.08, 'pressure': 1018, 'humidity': 72, 'dew_point': 4.51, 'uvi': 5.6, 'clouds': 22, 'visibility': 10000, 'wind_speed': 2.36, 'wind_deg': 310, 'wind_gust': 2.64, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643468400, 'temp': 10.91, 'feels_like': 9.78, 'pressure': 1017, 'humidity': 66, 'dew_point': 4.81, 'uvi': 9.42, 'clouds': 18, 'visibility': 10000, 'wind_speed': 2.92, 'wind_deg': 310, 'wind_gust': 2.85, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643472000, 'temp': 12.34, 'feels_like': 11.2, 'pressure': 1016, 'humidity': 60, 'dew_point': 4.8, 'uvi': 12.55, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.05, 'wind_deg': 306, 'wind_gust': 2.83, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643475600, 'temp': 13.18, 'feels_like': 12.04, 'pressure': 1015, 'humidity': 57, 'dew_point': 4.86, 'uvi': 13.66, 'clouds': 23, 'visibility': 10000, 'wind_speed': 3.24, 'wind_deg': 304, 'wind_gust': 3.09, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643479200, 'temp': 13.35, 'feels_like': 12.28, 'pressure': 1013, 'humidity': 59, 'dew_point': 5.51, 'uvi': 12.4, 'clouds': 97, 'visibility': 10000, 'wind_speed': 3.31, 'wind_deg': 303, 'wind_gust': 3.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}, {'dt': 1643482800, 'temp': 12.28, 'feels_like': 11.29, 'pressure': 1013, 'humidity': 66, 'dew_point': 6.12, 'uvi': 9.06, 'clouds': 98, 'visibility': 10000, 'wind_speed': 2.86, 'wind_deg': 304, 'wind_gust': 2.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1643486400, 'temp': 10.97, 'feels_like': 10.05, 'pressure': 1013, 'humidity': 74, 'dew_point': 6.52, 'uvi': 5.28, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.61, 'wind_deg': 304, 'wind_gust': 2.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.4}}, {'dt': 1643490000, 'temp': 10.09, 'feels_like': 9.22, 'pressure': 1013, 'humidity': 79, 'dew_point': 6.62, 'uvi': 2.16, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.39, 'wind_deg': 305, 'wind_gust': 2.35, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.41}}, {'dt': 1643493600, 'temp': 9.32, 'feels_like': 8.32, 'pressure': 1014, 'humidity': 84, 'dew_point': 6.76, 'uvi': 0.45, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.1, 'wind_deg': 304, 'wind_gust': 2.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.25}}, {'dt': 1643497200, 'temp': 7.76, 'feels_like': 7.13, 'pressure': 1015, 'humidity': 92, 'dew_point': 6.54, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.47, 'wind_deg': 313, 'wind_gust': 2.13, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 00:00:00 | 95.000000 | 6.240000 | 7.140000 | 94.000000 | 1016.000000 | 0.53 | 7.140000 | 0.000000 | 10000.000000 | 69.000000 | 1 | 0.760000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 01:00:00 | 81.000000 | 5.880000 | 6.930000 | 93.000000 | 1017.000000 | 0.63 | 6.930000 | 0.000000 | 10000.000000 | 41.000000 | 1.24 | 0.360000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 02:00:00 | 92.000000 | 6.340000 | 7.240000 | 94.000000 | 1018.000000 | 0.13 | 7.240000 | 0.000000 | 3565.000000 | 351.000000 | 1.78 | 0.460000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 03:00:00 | 93.000000 | 6.210000 | 7.270000 | 93.000000 | 1018.000000 | 0.97 | 7.270000 | 0.000000 | 8526.000000 | 308.000000 | 1.71 | 0.730000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 04:00:00 | 93.000000 | 6.090000 | 7.140000 | 93.000000 | 1018.000000 |  | 7.140000 | 0.000000 | 9867.000000 | 299.000000 | 1.7 | 0.670000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 05:00:00 | 94.000000 | 6.010000 | 6.910000 | 94.000000 | 1018.000000 | 1.21 | 6.910000 | 0.000000 | 5996.000000 | 298.000000 | 1.62 | 0.530000 | 501 | Rain | moderate rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 06:00:00 | 93.000000 | 5.460000 | 6.350000 | 94.000000 | 1017.000000 |  | 6.350000 | 0.000000 | 8190.000000 | 82.000000 | 1.16 | 0.160000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 07:00:00 | 68.000000 | 4.090000 | 5.600000 | 90.000000 | 1017.000000 |  | 5.600000 | 0.000000 | 10000.000000 | 314.000000 | 2.03 | 0.680000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 08:00:00 | 54.000000 | 3.590000 | 4.470000 | 94.000000 | 1017.000000 |  | 4.470000 | 0.000000 | 10000.000000 | 316.000000 | 1.81 | 0.660000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 09:00:00 | 57.000000 | 3.270000 | 4.610000 | 91.000000 | 1017.000000 |  | 4.610000 | 0.000000 | 10000.000000 | 21.000000 | 1.88 | 0.520000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 10:00:00 | 47.000000 | 2.880000 | 3.750000 | 94.000000 | 1018.000000 |  | 3.750000 | 0.000000 | 9466.000000 | 342.000000 | 1.9 | 0.710000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 11:00:00 | 46.000000 | 2.560000 | 3.580000 | 93.000000 | 1019.000000 |  | 3.580000 | 0.000000 | 10000.000000 | 351.000000 | 1.85 | 0.540000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 12:00:00 | 30.000000 | 3.150000 | 4.810000 | 89.000000 | 1019.000000 |  | 4.810000 | 0.550000 | 10000.000000 | 353.000000 | 1.98 | 0.540000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 13:00:00 | 39.000000 | 3.830000 | 6.580000 | 77.000000 | 1019.000000 |  | 7.600000 | 2.370000 | 10000.000000 | 319.000000 | 2.38 | 1.810000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 14:00:00 | 22.000000 | 4.510000 | 8.080000 | 72.000000 | 1018.000000 |  | 9.290000 | 5.600000 | 10000.000000 | 310.000000 | 2.64 | 2.360000 | 801 | Clouds | few clouds | 02d | 14 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 15:00:00 | 18.000000 | 4.810000 | 9.780000 | 66.000000 | 1017.000000 |  | 10.910000 | 9.420000 | 10000.000000 | 310.000000 | 2.85 | 2.920000 | 801 | Clouds | few clouds | 02d | 15 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 16:00:00 | 20.000000 | 4.800000 | 11.200000 | 60.000000 | 1016.000000 |  | 12.340000 | 12.550000 | 10000.000000 | 306.000000 | 2.83 | 3.050000 | 801 | Clouds | few clouds | 02d | 16 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 17:00:00 | 23.000000 | 4.860000 | 12.040000 | 57.000000 | 1015.000000 |  | 13.180000 | 13.660000 | 10000.000000 | 304.000000 | 3.09 | 3.240000 | 801 | Clouds | few clouds | 02d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 18:00:00 | 97.000000 | 5.510000 | 12.280000 | 59.000000 | 1013.000000 | 0.1 | 13.350000 | 12.400000 | 10000.000000 | 303.000000 | 3.1 | 3.310000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 19:00:00 | 98.000000 | 6.120000 | 11.290000 | 66.000000 | 1013.000000 | 0.29 | 12.280000 | 9.060000 | 10000.000000 | 304.000000 | 2.63 | 2.860000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 20:00:00 | 99.000000 | 6.520000 | 10.050000 | 74.000000 | 1013.000000 | 0.4 | 10.970000 | 5.280000 | 10000.000000 | 304.000000 | 2.54 | 2.610000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 21:00:00 | 99.000000 | 6.620000 | 9.220000 | 79.000000 | 1013.000000 | 0.41 | 10.090000 | 2.160000 | 10000.000000 | 305.000000 | 2.35 | 2.390000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 22:00:00 | 100.000000 | 6.760000 | 8.320000 | 84.000000 | 1014.000000 | 0.25 | 9.320000 | 0.450000 | 10000.000000 | 304.000000 | 2.19 | 2.100000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-29 23:00:00 | 98.000000 | 6.540000 | 7.130000 | 92.000000 | 1015.000000 | 0.14 | 7.760000 | 0.000000 | 10000.000000 | 313.000000 | 2.13 | 1.470000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21190270_OWM_Clouds_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Clouds_20220130.png)
![CNE_IDEAM_Station21190270_OWM_Dewpoint_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Dewpoint_20220130.png)
![CNE_IDEAM_Station21190270_OWM_Feelslike_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Feelslike_20220130.png)
![CNE_IDEAM_Station21190270_OWM_Humidity_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Humidity_20220130.png)
![CNE_IDEAM_Station21190270_OWM_Pressure_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Pressure_20220130.png)
![CNE_IDEAM_Station21190270_OWM_Rain_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Rain_20220130.png)
![CNE_IDEAM_Station21190270_OWM_Temp_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Temp_20220130.png)
![CNE_IDEAM_Station21190270_OWM_UVI_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_UVI_20220130.png)
![CNE_IDEAM_Station21190270_OWM_Visibility_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Visibility_20220130.png)
![CNE_IDEAM_Station21190270_OWM_Winddeg_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Winddeg_20220130.png)
![CNE_IDEAM_Station21190270_OWM_Windgust_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Windgust_20220130.png)
![CNE_IDEAM_Station21190270_OWM_Windspeed_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Windspeed_20220130.png)

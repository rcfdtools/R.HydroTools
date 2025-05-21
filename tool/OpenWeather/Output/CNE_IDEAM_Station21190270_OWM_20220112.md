
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SAN JUAN [21190270] - Historical

Study case: Weather evaluation from historical openweathermap data for the CNE IDEAM network stations in Bogotá - Colombia - Suramérica

### GitHub repository and system information

* Python version: 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
* Python path: ['D:\\R.GISPython\\OpenWeather', 'D:\\R.GISPython', 'D:\\R.GISPython.wiki', 'C:\\Python310\\python310.zip', 'C:\\Python310\\DLLs']
* matplotlib version: 3.5.0
* Repository: https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather
* License and conditions: https://github.com/rcfdtools/R.GISPython/wiki/License
* Credits: r.cfdtools@gmail.com

### General parameters

* Current date time: 2022-01-12 11:11:05.365344
* Unix time to eval: 1641899465
* Days before (for historical data): 1
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220112.xls
* CNE IDEAM file downloaded and updated: No
* CNE IDEAM stations: 4494
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21190270_OWM_20220112.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220112.csv)

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
{'lat': 4.031, 'lon': -74.3112, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641899465, 'sunrise': 1641899270, 'sunset': 1641942126, 'temp': 5.84, 'feels_like': 5.84, 'pressure': 1018, 'humidity': 94, 'dew_point': 4.95, 'uvi': 0, 'clouds': 99, 'visibility': 8344, 'wind_speed': 0.48, 'wind_deg': 325, 'wind_gust': 1.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641859200, 'temp': 6.68, 'feels_like': 6.68, 'pressure': 1017, 'humidity': 91, 'dew_point': 5.32, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 341, 'wind_gust': 1.15, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641862800, 'temp': 5.82, 'feels_like': 5.82, 'pressure': 1018, 'humidity': 91, 'dew_point': 4.47, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 44, 'wind_gust': 1.11, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641866400, 'temp': 5.34, 'feels_like': 5.34, 'pressure': 1019, 'humidity': 91, 'dew_point': 3.99, 'uvi': 0, 'clouds': 38, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 60, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641870000, 'temp': 5.06, 'feels_like': 5.06, 'pressure': 1020, 'humidity': 91, 'dew_point': 3.71, 'uvi': 0, 'clouds': 38, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 39, 'wind_gust': 1.4, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641873600, 'temp': 5.57, 'feels_like': 5.57, 'pressure': 1019, 'humidity': 91, 'dew_point': 4.22, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 345, 'wind_gust': 1.57, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641877200, 'temp': 5.87, 'feels_like': 5.87, 'pressure': 1019, 'humidity': 93, 'dew_point': 4.83, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 360, 'wind_gust': 1.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641880800, 'temp': 6.18, 'feels_like': 6.18, 'pressure': 1018, 'humidity': 95, 'dew_point': 5.44, 'uvi': 0, 'clouds': 91, 'visibility': 6380, 'wind_speed': 0.58, 'wind_deg': 332, 'wind_gust': 1.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641884400, 'temp': 6.41, 'feels_like': 6.41, 'pressure': 1017, 'humidity': 95, 'dew_point': 5.67, 'uvi': 0, 'clouds': 99, 'visibility': 6051, 'wind_speed': 0.66, 'wind_deg': 318, 'wind_gust': 1.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641888000, 'temp': 6.42, 'feels_like': 6.42, 'pressure': 1016, 'humidity': 95, 'dew_point': 5.68, 'uvi': 0, 'clouds': 99, 'visibility': 6169, 'wind_speed': 0.72, 'wind_deg': 310, 'wind_gust': 1.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641891600, 'temp': 6.39, 'feels_like': 6.39, 'pressure': 1016, 'humidity': 96, 'dew_point': 5.8, 'uvi': 0, 'clouds': 100, 'visibility': 4985, 'wind_speed': 0.93, 'wind_deg': 304, 'wind_gust': 1.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641895200, 'temp': 6.35, 'feels_like': 6.35, 'pressure': 1017, 'humidity': 95, 'dew_point': 5.61, 'uvi': 0, 'clouds': 100, 'visibility': 4593, 'wind_speed': 0.63, 'wind_deg': 311, 'wind_gust': 1.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641898800, 'temp': 5.84, 'feels_like': 5.84, 'pressure': 1018, 'humidity': 94, 'dew_point': 4.95, 'uvi': 0, 'clouds': 99, 'visibility': 8344, 'wind_speed': 0.48, 'wind_deg': 325, 'wind_gust': 1.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641902400, 'temp': 6.24, 'feels_like': 6.24, 'pressure': 1018, 'humidity': 93, 'dew_point': 5.19, 'uvi': 0.41, 'clouds': 81, 'visibility': 5086, 'wind_speed': 0.69, 'wind_deg': 339, 'wind_gust': 1.21, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641906000, 'temp': 7.08, 'feels_like': 7.08, 'pressure': 1019, 'humidity': 90, 'dew_point': 5.55, 'uvi': 1.88, 'clouds': 90, 'visibility': 6671, 'wind_speed': 1.21, 'wind_deg': 319, 'wind_gust': 1.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641909600, 'temp': 8.12, 'feels_like': 8.12, 'pressure': 1019, 'humidity': 87, 'dew_point': 6.09, 'uvi': 4.49, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 321, 'wind_gust': 1.56, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641913200, 'temp': 9.2, 'feels_like': 8.5, 'pressure': 1019, 'humidity': 82, 'dew_point': 6.29, 'uvi': 7.58, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 310, 'wind_gust': 1.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641916800, 'temp': 9.82, 'feels_like': 9.2, 'pressure': 1018, 'humidity': 81, 'dew_point': 6.72, 'uvi': 11.73, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.75, 'wind_deg': 308, 'wind_gust': 1.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.25}}, {'dt': 1641920400, 'temp': 10.27, 'feels_like': 9.44, 'pressure': 1017, 'humidity': 80, 'dew_point': 6.98, 'uvi': 12.76, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.79, 'wind_deg': 303, 'wind_gust': 1.86, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1641924000, 'temp': 10.09, 'feels_like': 9.27, 'pressure': 1016, 'humidity': 81, 'dew_point': 6.98, 'uvi': 11.59, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.93, 'wind_deg': 299, 'wind_gust': 1.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.41}}, {'dt': 1641927600, 'temp': 10.02, 'feels_like': 9.19, 'pressure': 1015, 'humidity': 81, 'dew_point': 6.91, 'uvi': 8.33, 'clouds': 91, 'visibility': 10000, 'wind_speed': 2.18, 'wind_deg': 300, 'wind_gust': 2.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.37}}, {'dt': 1641931200, 'temp': 9.31, 'feels_like': 8.46, 'pressure': 1014, 'humidity': 84, 'dew_point': 6.75, 'uvi': 4.85, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.92, 'wind_deg': 302, 'wind_gust': 1.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.27}}, {'dt': 1641934800, 'temp': 8.8, 'feels_like': 8.28, 'pressure': 1015, 'humidity': 87, 'dew_point': 6.76, 'uvi': 1.96, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 307, 'wind_gust': 1.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641938400, 'temp': 8.6, 'feels_like': 8.6, 'pressure': 1015, 'humidity': 87, 'dew_point': 6.56, 'uvi': 0.46, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 305, 'wind_gust': 1.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641942000, 'temp': 6.92, 'feels_like': 6.92, 'pressure': 1017, 'humidity': 94, 'dew_point': 6.02, 'uvi': 0, 'clouds': 88, 'visibility': 6032, 'wind_speed': 0.87, 'wind_deg': 305, 'wind_gust': 1.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 00:00:00 | 34.000000 | 5.320000 | 6.680000 | 91.000000 | 1017.000000 |  | 6.680000 | 0.000000 | 10000.000000 | 341.000000 | 1.15 | 0.710000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 01:00:00 | 40.000000 | 4.470000 | 5.820000 | 91.000000 | 1018.000000 |  | 5.820000 | 0.000000 | 10000.000000 | 44.000000 | 1.11 | 0.440000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 02:00:00 | 38.000000 | 3.990000 | 5.340000 | 91.000000 | 1019.000000 | 0.14 | 5.340000 | 0.000000 | 10000.000000 | 60.000000 | 1.25 | 0.640000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 03:00:00 | 38.000000 | 3.710000 | 5.060000 | 91.000000 | 1020.000000 | 0.14 | 5.060000 | 0.000000 | 10000.000000 | 39.000000 | 1.4 | 0.450000 | 500 | Rain | light rain | 10n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 04:00:00 | 47.000000 | 4.220000 | 5.570000 | 91.000000 | 1019.000000 |  | 5.570000 | 0.000000 | 10000.000000 | 345.000000 | 1.57 | 0.490000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 05:00:00 | 55.000000 | 4.830000 | 5.870000 | 93.000000 | 1019.000000 | 0.15 | 5.870000 | 0.000000 | 10000.000000 | 360.000000 | 1.53 | 0.350000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 06:00:00 | 91.000000 | 5.440000 | 6.180000 | 95.000000 | 1018.000000 | 0.17 | 6.180000 | 0.000000 | 6380.000000 | 332.000000 | 1.57 | 0.580000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 07:00:00 | 99.000000 | 5.670000 | 6.410000 | 95.000000 | 1017.000000 |  | 6.410000 | 0.000000 | 6051.000000 | 318.000000 | 1.86 | 0.660000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 08:00:00 | 99.000000 | 5.680000 | 6.420000 | 95.000000 | 1016.000000 |  | 6.420000 | 0.000000 | 6169.000000 | 310.000000 | 1.67 | 0.720000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 09:00:00 | 100.000000 | 5.800000 | 6.390000 | 96.000000 | 1016.000000 |  | 6.390000 | 0.000000 | 4985.000000 | 304.000000 | 1.88 | 0.930000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 10:00:00 | 100.000000 | 5.610000 | 6.350000 | 95.000000 | 1017.000000 | 0.12 | 6.350000 | 0.000000 | 4593.000000 | 311.000000 | 1.43 | 0.630000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 11:00:00 | 99.000000 | 4.950000 | 5.840000 | 94.000000 | 1018.000000 |  | 5.840000 | 0.000000 | 8344.000000 | 325.000000 | 1.05 | 0.480000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 12:00:00 | 81.000000 | 5.190000 | 6.240000 | 93.000000 | 1018.000000 |  | 6.240000 | 0.410000 | 5086.000000 | 339.000000 | 1.21 | 0.690000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 13:00:00 | 90.000000 | 5.550000 | 7.080000 | 90.000000 | 1019.000000 |  | 7.080000 | 1.880000 | 6671.000000 | 319.000000 | 1.79 | 1.210000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 14:00:00 | 94.000000 | 6.090000 | 8.120000 | 87.000000 | 1019.000000 | 0.12 | 8.120000 | 4.490000 | 10000.000000 | 321.000000 | 1.56 | 1.290000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 15:00:00 | 96.000000 | 6.290000 | 8.500000 | 82.000000 | 1019.000000 | 0.11 | 9.200000 | 7.580000 | 10000.000000 | 310.000000 | 1.81 | 1.730000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 16:00:00 | 96.000000 | 6.720000 | 9.200000 | 81.000000 | 1018.000000 | 0.25 | 9.820000 | 11.730000 | 10000.000000 | 308.000000 | 1.92 | 1.750000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 17:00:00 | 95.000000 | 6.980000 | 9.440000 | 80.000000 | 1017.000000 | 0.36 | 10.270000 | 12.760000 | 10000.000000 | 303.000000 | 1.86 | 1.790000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 18:00:00 | 82.000000 | 6.980000 | 9.270000 | 81.000000 | 1016.000000 | 0.41 | 10.090000 | 11.590000 | 10000.000000 | 299.000000 | 1.87 | 1.930000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 19:00:00 | 91.000000 | 6.910000 | 9.190000 | 81.000000 | 1015.000000 | 0.37 | 10.020000 | 8.330000 | 10000.000000 | 300.000000 | 2.18 | 2.180000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 20:00:00 | 92.000000 | 6.750000 | 8.460000 | 84.000000 | 1014.000000 | 0.27 | 9.310000 | 4.850000 | 10000.000000 | 302.000000 | 1.99 | 1.920000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 21:00:00 | 94.000000 | 6.760000 | 8.280000 | 87.000000 | 1015.000000 | 0.16 | 8.800000 | 1.960000 | 10000.000000 | 307.000000 | 1.59 | 1.500000 | 500 | Rain | light rain | 10d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 22:00:00 | 91.000000 | 6.560000 | 8.600000 | 87.000000 | 1015.000000 |  | 8.600000 | 0.460000 | 10000.000000 | 305.000000 | 1.42 | 1.180000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-11 23:00:00 | 88.000000 | 6.020000 | 6.920000 | 94.000000 | 1017.000000 | 0.13 | 6.920000 | 0.000000 | 6032.000000 | 305.000000 | 1.44 | 0.870000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21190270_OWM_Clouds_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Clouds_20220112.png)
![CNE_IDEAM_Station21190270_OWM_Dewpoint_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Dewpoint_20220112.png)
![CNE_IDEAM_Station21190270_OWM_Feelslike_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Feelslike_20220112.png)
![CNE_IDEAM_Station21190270_OWM_Humidity_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Humidity_20220112.png)
![CNE_IDEAM_Station21190270_OWM_Pressure_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Pressure_20220112.png)
![CNE_IDEAM_Station21190270_OWM_Rain_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Rain_20220112.png)
![CNE_IDEAM_Station21190270_OWM_Temp_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Temp_20220112.png)
![CNE_IDEAM_Station21190270_OWM_UVI_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_UVI_20220112.png)
![CNE_IDEAM_Station21190270_OWM_Visibility_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Visibility_20220112.png)
![CNE_IDEAM_Station21190270_OWM_Windgust_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Windgust_20220112.png)
![CNE_IDEAM_Station21190270_OWM_Windspeed_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Windspeed_20220112.png)

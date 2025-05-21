
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

* Current date time: 2022-02-03 15:08:03.237034
* Unix time to eval: 1643814483
* Days before (for historical data): 1
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220203.xls
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21190270_OWM_20220203.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220203.csv)

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

### (CNE index 1322) Open Weather values for station 21190270 - SAN JUAN [21190270]

JSON data from API OWM:

```
{'lat': 4.031, 'lon': -74.3112, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643814483, 'sunrise': 1643800339, 'sunset': 1643843372, 'temp': 9.63, 'feels_like': 9.63, 'pressure': 1018, 'humidity': 70, 'dew_point': 4.43, 'uvi': 6.83, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 150, 'wind_gust': 1.97, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, 'hourly': [{'dt': 1643760000, 'temp': 6.48, 'feels_like': 5.34, 'pressure': 1016, 'humidity': 94, 'dew_point': 5.59, 'uvi': 0, 'clouds': 88, 'visibility': 5321, 'wind_speed': 1.76, 'wind_deg': 104, 'wind_gust': 1.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1643763600, 'temp': 6.3, 'feels_like': 6.3, 'pressure': 1017, 'humidity': 91, 'dew_point': 4.94, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 103, 'wind_gust': 1.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.25}}, {'dt': 1643767200, 'temp': 6.43, 'feels_like': 6.43, 'pressure': 1018, 'humidity': 91, 'dew_point': 5.07, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 110, 'wind_gust': 1.15, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1643770800, 'temp': 6.43, 'feels_like': 6.43, 'pressure': 1018, 'humidity': 92, 'dew_point': 5.23, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 109, 'wind_gust': 0.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1643774400, 'temp': 6.32, 'feels_like': 6.32, 'pressure': 1018, 'humidity': 93, 'dew_point': 5.27, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 113, 'wind_gust': 0.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1643778000, 'temp': 5.97, 'feels_like': 5.97, 'pressure': 1017, 'humidity': 94, 'dew_point': 5.08, 'uvi': 0, 'clouds': 98, 'visibility': 5657, 'wind_speed': 1.08, 'wind_deg': 117, 'wind_gust': 1.08, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1643781600, 'temp': 6.15, 'feels_like': 6.15, 'pressure': 1016, 'humidity': 92, 'dew_point': 4.95, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 136, 'wind_gust': 1.13, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1643785200, 'temp': 6.05, 'feels_like': 6.05, 'pressure': 1016, 'humidity': 90, 'dew_point': 4.54, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 136, 'wind_gust': 1.14, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1643788800, 'temp': 5.59, 'feels_like': 4.79, 'pressure': 1016, 'humidity': 92, 'dew_point': 4.39, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 129, 'wind_gust': 1.48, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1643792400, 'temp': 5.25, 'feels_like': 4.05, 'pressure': 1016, 'humidity': 94, 'dew_point': 4.36, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 123, 'wind_gust': 1.89, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1643796000, 'temp': 5.11, 'feels_like': 3.76, 'pressure': 1017, 'humidity': 93, 'dew_point': 4.07, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.76, 'wind_deg': 123, 'wind_gust': 2.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1643799600, 'temp': 4.87, 'feels_like': 3.48, 'pressure': 1018, 'humidity': 93, 'dew_point': 3.84, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.76, 'wind_deg': 121, 'wind_gust': 2.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643803200, 'temp': 5.17, 'feels_like': 3.75, 'pressure': 1018, 'humidity': 91, 'dew_point': 3.82, 'uvi': 0.53, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.83, 'wind_deg': 119, 'wind_gust': 2.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643806800, 'temp': 5.81, 'feels_like': 4.92, 'pressure': 1019, 'humidity': 87, 'dew_point': 3.82, 'uvi': 1.72, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 118, 'wind_gust': 1.98, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643810400, 'temp': 7.58, 'feels_like': 7.58, 'pressure': 1019, 'humidity': 79, 'dew_point': 4.18, 'uvi': 4.07, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 124, 'wind_gust': 1.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1643814000, 'temp': 9.63, 'feels_like': 9.63, 'pressure': 1018, 'humidity': 70, 'dew_point': 4.43, 'uvi': 6.83, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 150, 'wind_gust': 1.97, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1643817600, 'temp': 11.12, 'feels_like': 9.96, 'pressure': 1017, 'humidity': 64, 'dew_point': 4.57, 'uvi': 12.64, 'clouds': 69, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 178, 'wind_gust': 2.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1643821200, 'temp': 11.53, 'feels_like': 10.38, 'pressure': 1016, 'humidity': 63, 'dew_point': 4.74, 'uvi': 13.74, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 191, 'wind_gust': 2.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1643824800, 'temp': 11.5, 'feels_like': 10.4, 'pressure': 1015, 'humidity': 65, 'dew_point': 5.16, 'uvi': 12.47, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 198, 'wind_gust': 2.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1643828400, 'temp': 10.75, 'feels_like': 9.76, 'pressure': 1014, 'humidity': 72, 'dew_point': 5.91, 'uvi': 9.05, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 162, 'wind_gust': 2.33, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1643832000, 'temp': 9.52, 'feels_like': 9.27, 'pressure': 1014, 'humidity': 78, 'dew_point': 5.88, 'uvi': 5.27, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 127, 'wind_gust': 2.37, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.35}}, {'dt': 1643835600, 'temp': 8.91, 'feels_like': 8.22, 'pressure': 1014, 'humidity': 80, 'dew_point': 5.65, 'uvi': 2.17, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 121, 'wind_gust': 2.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1643839200, 'temp': 8.17, 'feels_like': 7.17, 'pressure': 1015, 'humidity': 82, 'dew_point': 5.29, 'uvi': 0.39, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.88, 'wind_deg': 121, 'wind_gust': 2.32, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1643842800, 'temp': 6.88, 'feels_like': 5.49, 'pressure': 1016, 'humidity': 89, 'dew_point': 5.2, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.07, 'wind_deg': 114, 'wind_gust': 2.48, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 00:00:00 | 88.000000 | 5.590000 | 5.340000 | 94.000000 | 1016.000000 | 0.2 | 6.480000 | 0.000000 | 5321.000000 | 104.000000 | 1.77 | 1.760000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 01:00:00 | 95.000000 | 4.940000 | 6.300000 | 91.000000 | 1017.000000 | 0.25 | 6.300000 | 0.000000 | 10000.000000 | 103.000000 | 1.2 | 1.310000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 02:00:00 | 97.000000 | 5.070000 | 6.430000 | 91.000000 | 1018.000000 | 0.15 | 6.430000 | 0.000000 | 10000.000000 | 110.000000 | 1.15 | 1.050000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 03:00:00 | 98.000000 | 5.230000 | 6.430000 | 92.000000 | 1018.000000 | 0.17 | 6.430000 | 0.000000 | 10000.000000 | 109.000000 | 0.93 | 0.810000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 04:00:00 | 98.000000 | 5.270000 | 6.320000 | 93.000000 | 1018.000000 | 0.17 | 6.320000 | 0.000000 | 10000.000000 | 113.000000 | 0.72 | 0.700000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 05:00:00 | 98.000000 | 5.080000 | 5.970000 | 94.000000 | 1017.000000 | 0.1 | 5.970000 | 0.000000 | 5657.000000 | 117.000000 | 1.08 | 1.080000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 06:00:00 | 100.000000 | 4.950000 | 6.150000 | 92.000000 | 1016.000000 | 0.12 | 6.150000 | 0.000000 | 10000.000000 | 136.000000 | 1.13 | 0.930000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 07:00:00 | 100.000000 | 4.540000 | 6.050000 | 90.000000 | 1016.000000 | 0.16 | 6.050000 | 0.000000 | 10000.000000 | 136.000000 | 1.14 | 0.980000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 08:00:00 | 100.000000 | 4.390000 | 4.790000 | 92.000000 | 1016.000000 | 0.16 | 5.590000 | 0.000000 | 10000.000000 | 129.000000 | 1.48 | 1.370000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 09:00:00 | 100.000000 | 4.360000 | 4.050000 | 94.000000 | 1016.000000 | 0.24 | 5.250000 | 0.000000 | 10000.000000 | 123.000000 | 1.89 | 1.650000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 10:00:00 | 100.000000 | 4.070000 | 3.760000 | 93.000000 | 1017.000000 | 0.17 | 5.110000 | 0.000000 | 10000.000000 | 123.000000 | 2.03 | 1.760000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 11:00:00 | 100.000000 | 3.840000 | 3.480000 | 93.000000 | 1018.000000 |  | 4.870000 | 0.000000 | 10000.000000 | 121.000000 | 2.25 | 1.760000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 12:00:00 | 90.000000 | 3.820000 | 3.750000 | 91.000000 | 1018.000000 |  | 5.170000 | 0.530000 | 10000.000000 | 119.000000 | 2.25 | 1.830000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 13:00:00 | 98.000000 | 3.820000 | 4.920000 | 87.000000 | 1019.000000 |  | 5.810000 | 1.720000 | 10000.000000 | 118.000000 | 1.98 | 1.460000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 14:00:00 | 85.000000 | 4.180000 | 7.580000 | 79.000000 | 1019.000000 | 0.18 | 7.580000 | 4.070000 | 10000.000000 | 124.000000 | 1.81 | 0.960000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 15:00:00 | 77.000000 | 4.430000 | 9.630000 | 70.000000 | 1018.000000 | 0.19 | 9.630000 | 6.830000 | 10000.000000 | 150.000000 | 1.97 | 0.720000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 16:00:00 | 69.000000 | 4.570000 | 9.960000 | 64.000000 | 1017.000000 | 0.12 | 11.120000 | 12.640000 | 10000.000000 | 178.000000 | 2.01 | 0.580000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 17:00:00 | 70.000000 | 4.740000 | 10.380000 | 63.000000 | 1016.000000 | 0.2 | 11.530000 | 13.740000 | 10000.000000 | 191.000000 | 2.25 | 0.570000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 18:00:00 | 100.000000 | 5.160000 | 10.400000 | 65.000000 | 1015.000000 | 0.19 | 11.500000 | 12.470000 | 10000.000000 | 198.000000 | 2.71 | 0.750000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 19:00:00 | 100.000000 | 5.910000 | 9.760000 | 72.000000 | 1014.000000 | 0.26 | 10.750000 | 9.050000 | 10000.000000 | 162.000000 | 2.33 | 0.970000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 20:00:00 | 100.000000 | 5.880000 | 9.270000 | 78.000000 | 1014.000000 | 0.35 | 9.520000 | 5.270000 | 10000.000000 | 127.000000 | 2.37 | 1.350000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 21:00:00 | 100.000000 | 5.650000 | 8.220000 | 80.000000 | 1014.000000 | 0.26 | 8.910000 | 2.170000 | 10000.000000 | 121.000000 | 2.43 | 1.680000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 22:00:00 | 100.000000 | 5.290000 | 7.170000 | 82.000000 | 1015.000000 | 0.16 | 8.170000 | 0.390000 | 10000.000000 | 121.000000 | 2.32 | 1.880000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21190270 | "SAN JUAN [21190270]" | 4.031028 | -74.311167 | 2900.000000 | Pluviométrica | Convencional | Activa | 1972-06-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-02-02 23:00:00 | 99.000000 | 5.200000 | 5.490000 | 89.000000 | 1016.000000 | 0.17 | 6.880000 | 0.000000 | 10000.000000 | 114.000000 | 2.48 | 2.070000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21190270_OWM_Clouds_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Clouds_20220203.png)
![CNE_IDEAM_Station21190270_OWM_Dewpoint_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Dewpoint_20220203.png)
![CNE_IDEAM_Station21190270_OWM_Feelslike_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Feelslike_20220203.png)
![CNE_IDEAM_Station21190270_OWM_Humidity_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Humidity_20220203.png)
![CNE_IDEAM_Station21190270_OWM_Pressure_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Pressure_20220203.png)
![CNE_IDEAM_Station21190270_OWM_Rain_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Rain_20220203.png)
![CNE_IDEAM_Station21190270_OWM_Temp_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Temp_20220203.png)
![CNE_IDEAM_Station21190270_OWM_UVI_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_UVI_20220203.png)
![CNE_IDEAM_Station21190270_OWM_Visibility_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Visibility_20220203.png)
![CNE_IDEAM_Station21190270_OWM_Winddeg_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Winddeg_20220203.png)
![CNE_IDEAM_Station21190270_OWM_Windgust_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Windgust_20220203.png)
![CNE_IDEAM_Station21190270_OWM_Windspeed_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21190270_OWM_Windspeed_20220203.png)

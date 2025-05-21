
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35025070_OWM_20220203.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220203.csv)

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

### (CNE index 1865) Open Weather values for station 35025070 - TAQUES LOS [35025070]

JSON data from API OWM:

```
{'lat': 4.1967, 'lon': -74.1909, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643814483, 'sunrise': 1643800322, 'sunset': 1643843331, 'temp': 12.57, 'feels_like': 11.53, 'pressure': 1018, 'humidity': 63, 'dew_point': 5.72, 'uvi': 6.83, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 68, 'wind_gust': 1.98, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1643760000, 'temp': 9.57, 'feels_like': 9.14, 'pressure': 1017, 'humidity': 90, 'dew_point': 8.01, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.52, 'wind_deg': 100, 'wind_gust': 1.84, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643763600, 'temp': 8.57, 'feels_like': 8.19, 'pressure': 1018, 'humidity': 89, 'dew_point': 6.86, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 103, 'wind_gust': 1.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643767200, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1018, 'humidity': 89, 'dew_point': 6.86, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 108, 'wind_gust': 1.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643770800, 'temp': 6.57, 'feels_like': 6.57, 'pressure': 1018, 'humidity': 88, 'dew_point': 4.73, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 125, 'wind_gust': 1.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643774400, 'temp': 6.57, 'feels_like': 6.57, 'pressure': 1018, 'humidity': 88, 'dew_point': 4.73, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 117, 'wind_gust': 1.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643778000, 'temp': 4.57, 'feels_like': 4.57, 'pressure': 1018, 'humidity': 89, 'dew_point': 2.92, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 103, 'wind_gust': 1.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643781600, 'temp': 4.57, 'feels_like': 4.57, 'pressure': 1017, 'humidity': 87, 'dew_point': 2.6, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 103, 'wind_gust': 1.1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643785200, 'temp': 5.57, 'feels_like': 5.57, 'pressure': 1016, 'humidity': 87, 'dew_point': 3.58, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 94, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643788800, 'temp': 6.57, 'feels_like': 6.57, 'pressure': 1016, 'humidity': 89, 'dew_point': 4.89, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 95, 'wind_gust': 1.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643792400, 'temp': 5.57, 'feels_like': 5.57, 'pressure': 1017, 'humidity': 89, 'dew_point': 3.9, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.1, 'wind_deg': 102, 'wind_gust': 1.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643796000, 'temp': 4.57, 'feels_like': 4.57, 'pressure': 1017, 'humidity': 90, 'dew_point': 3.07, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 106, 'wind_gust': 1.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1643799600, 'temp': 5.57, 'feels_like': 5.57, 'pressure': 1018, 'humidity': 89, 'dew_point': 3.9, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 106, 'wind_gust': 2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643803200, 'temp': 5.57, 'feels_like': 4.77, 'pressure': 1018, 'humidity': 86, 'dew_point': 3.42, 'uvi': 0.53, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 98, 'wind_gust': 2.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643806800, 'temp': 7.57, 'feels_like': 6.76, 'pressure': 1019, 'humidity': 80, 'dew_point': 4.35, 'uvi': 1.72, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.6, 'wind_deg': 101, 'wind_gust': 2.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643810400, 'temp': 10.57, 'feels_like': 9.51, 'pressure': 1019, 'humidity': 70, 'dew_point': 5.33, 'uvi': 4.07, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 100, 'wind_gust': 1.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643814000, 'temp': 12.57, 'feels_like': 11.53, 'pressure': 1018, 'humidity': 63, 'dew_point': 5.72, 'uvi': 6.83, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 68, 'wind_gust': 1.98, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643817600, 'temp': 14.57, 'feels_like': 13.75, 'pressure': 1017, 'humidity': 64, 'dew_point': 7.85, 'uvi': 12.64, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 4, 'wind_gust': 2.19, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643821200, 'temp': 14.57, 'feels_like': 13.83, 'pressure': 1016, 'humidity': 67, 'dew_point': 8.52, 'uvi': 13.74, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 33, 'wind_gust': 2.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1643824800, 'temp': 13.57, 'feels_like': 12.71, 'pressure': 1015, 'humidity': 66, 'dew_point': 7.35, 'uvi': 12.47, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 30, 'wind_gust': 2.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.32}}, {'dt': 1643828400, 'temp': 14.57, 'feels_like': 13.88, 'pressure': 1014, 'humidity': 69, 'dew_point': 8.95, 'uvi': 9.05, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 50, 'wind_gust': 2.49, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1643832000, 'temp': 14.57, 'feels_like': 13.99, 'pressure': 1014, 'humidity': 73, 'dew_point': 9.79, 'uvi': 5.27, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 101, 'wind_gust': 2.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.4}}, {'dt': 1643835600, 'temp': 13.57, 'feels_like': 12.94, 'pressure': 1014, 'humidity': 75, 'dew_point': 9.23, 'uvi': 2.17, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 107, 'wind_gust': 2.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1643839200, 'temp': 12.57, 'feels_like': 11.87, 'pressure': 1014, 'humidity': 76, 'dew_point': 8.46, 'uvi': 0.39, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 105, 'wind_gust': 2.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.28}}, {'dt': 1643842800, 'temp': 10.57, 'feels_like': 9.85, 'pressure': 1016, 'humidity': 83, 'dew_point': 7.81, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.77, 'wind_deg': 93, 'wind_gust': 2.42, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 00:00:00 | 76.000000 | 8.010000 | 9.140000 | 90.000000 | 1017.000000 |  | 9.570000 | 0.000000 | 10000.000000 | 100.000000 | 1.84 | 1.520000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 01:00:00 | 86.000000 | 6.860000 | 8.190000 | 89.000000 | 1018.000000 |  | 8.570000 | 0.000000 | 10000.000000 | 103.000000 | 1.66 | 1.350000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 02:00:00 | 88.000000 | 6.860000 | 8.570000 | 89.000000 | 1018.000000 |  | 8.570000 | 0.000000 | 10000.000000 | 108.000000 | 1.7 | 1.120000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 03:00:00 | 92.000000 | 4.730000 | 6.570000 | 88.000000 | 1018.000000 |  | 6.570000 | 0.000000 | 10000.000000 | 125.000000 | 1.36 | 0.770000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 04:00:00 | 94.000000 | 4.730000 | 6.570000 | 88.000000 | 1018.000000 |  | 6.570000 | 0.000000 | 10000.000000 | 117.000000 | 1.16 | 0.640000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 05:00:00 | 95.000000 | 2.920000 | 4.570000 | 89.000000 | 1018.000000 |  | 4.570000 | 0.000000 | 10000.000000 | 103.000000 | 1.36 | 1.040000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 06:00:00 | 94.000000 | 2.600000 | 4.570000 | 87.000000 | 1017.000000 |  | 4.570000 | 0.000000 | 10000.000000 | 103.000000 | 1.1 | 0.610000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 07:00:00 | 99.000000 | 3.580000 | 5.570000 | 87.000000 | 1016.000000 |  | 5.570000 | 0.000000 | 10000.000000 | 94.000000 | 1.18 | 0.650000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 08:00:00 | 100.000000 | 4.890000 | 6.570000 | 89.000000 | 1016.000000 |  | 6.570000 | 0.000000 | 10000.000000 | 95.000000 | 1.44 | 0.840000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 09:00:00 | 100.000000 | 3.900000 | 5.570000 | 89.000000 | 1017.000000 |  | 5.570000 | 0.000000 | 10000.000000 | 102.000000 | 1.67 | 1.100000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 10:00:00 | 100.000000 | 3.070000 | 4.570000 | 90.000000 | 1017.000000 | 0.11 | 4.570000 | 0.000000 | 10000.000000 | 106.000000 | 1.75 | 1.160000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 11:00:00 | 100.000000 | 3.900000 | 5.570000 | 89.000000 | 1018.000000 |  | 5.570000 | 0.000000 | 10000.000000 | 106.000000 | 2 | 1.220000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 12:00:00 | 96.000000 | 3.420000 | 4.770000 | 86.000000 | 1018.000000 |  | 5.570000 | 0.530000 | 10000.000000 | 98.000000 | 2.39 | 1.370000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 13:00:00 | 100.000000 | 4.350000 | 6.760000 | 80.000000 | 1019.000000 |  | 7.570000 | 1.720000 | 10000.000000 | 101.000000 | 2.3 | 1.600000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 14:00:00 | 91.000000 | 5.330000 | 9.510000 | 70.000000 | 1019.000000 |  | 10.570000 | 4.070000 | 10000.000000 | 100.000000 | 1.73 | 1.040000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 15:00:00 | 80.000000 | 5.720000 | 11.530000 | 63.000000 | 1018.000000 |  | 12.570000 | 6.830000 | 10000.000000 | 68.000000 | 1.98 | 0.370000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 16:00:00 | 79.000000 | 7.850000 | 13.750000 | 64.000000 | 1017.000000 |  | 14.570000 | 12.640000 | 10000.000000 | 4.000000 | 2.19 | 0.260000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 17:00:00 | 81.000000 | 8.520000 | 13.830000 | 67.000000 | 1016.000000 | 0.21 | 14.570000 | 13.740000 | 10000.000000 | 33.000000 | 2.19 | 0.660000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 18:00:00 | 99.000000 | 7.350000 | 12.710000 | 66.000000 | 1015.000000 | 0.32 | 13.570000 | 12.470000 | 10000.000000 | 30.000000 | 2.53 | 0.890000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 19:00:00 | 100.000000 | 8.950000 | 13.880000 | 69.000000 | 1014.000000 | 0.33 | 14.570000 | 9.050000 | 10000.000000 | 50.000000 | 2.49 | 0.730000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 20:00:00 | 100.000000 | 9.790000 | 13.990000 | 73.000000 | 1014.000000 | 0.4 | 14.570000 | 5.270000 | 10000.000000 | 101.000000 | 2.16 | 0.950000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 21:00:00 | 100.000000 | 9.230000 | 12.940000 | 75.000000 | 1014.000000 | 0.26 | 13.570000 | 2.170000 | 10000.000000 | 107.000000 | 2.27 | 1.140000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 22:00:00 | 100.000000 | 8.460000 | 11.870000 | 76.000000 | 1014.000000 | 0.28 | 12.570000 | 0.390000 | 10000.000000 | 105.000000 | 2.26 | 1.650000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 23:00:00 | 100.000000 | 7.810000 | 9.850000 | 83.000000 | 1016.000000 | 0.12 | 10.570000 | 0.000000 | 10000.000000 | 93.000000 | 2.42 | 1.770000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station35025070_OWM_Clouds_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Clouds_20220203.png)
![CNE_IDEAM_Station35025070_OWM_Dewpoint_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Dewpoint_20220203.png)
![CNE_IDEAM_Station35025070_OWM_Feelslike_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Feelslike_20220203.png)
![CNE_IDEAM_Station35025070_OWM_Humidity_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Humidity_20220203.png)
![CNE_IDEAM_Station35025070_OWM_Pressure_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Pressure_20220203.png)
![CNE_IDEAM_Station35025070_OWM_Rain_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Rain_20220203.png)
![CNE_IDEAM_Station35025070_OWM_Temp_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Temp_20220203.png)
![CNE_IDEAM_Station35025070_OWM_UVI_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_UVI_20220203.png)
![CNE_IDEAM_Station35025070_OWM_Visibility_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Visibility_20220203.png)
![CNE_IDEAM_Station35025070_OWM_Winddeg_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Winddeg_20220203.png)
![CNE_IDEAM_Station35025070_OWM_Windgust_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Windgust_20220203.png)
![CNE_IDEAM_Station35025070_OWM_Windspeed_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Windspeed_20220203.png)

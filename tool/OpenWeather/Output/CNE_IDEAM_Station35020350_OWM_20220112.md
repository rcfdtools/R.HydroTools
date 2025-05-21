
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BETANIA [35020350] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35020350_OWM_20220112.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220112.csv)

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

### (CNE index 1906) Open Weather values for station 35020350 - BETANIA [35020350]

JSON data from API OWM:

```
{'lat': 4.2189, 'lon': -74.1469, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641899465, 'sunrise': 1641899249, 'sunset': 1641942068, 'temp': 8.37, 'feels_like': 8.37, 'pressure': 1018, 'humidity': 97, 'dew_point': 7.92, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 297, 'wind_gust': 0.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641859200, 'temp': 11.37, 'feels_like': 11.04, 'pressure': 1017, 'humidity': 95, 'dew_point': 10.6, 'uvi': 0, 'clouds': 85, 'visibility': 9839, 'wind_speed': 0.32, 'wind_deg': 43, 'wind_gust': 0.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641862800, 'temp': 11.37, 'feels_like': 11.02, 'pressure': 1018, 'humidity': 94, 'dew_point': 10.44, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.16, 'wind_deg': 53, 'wind_gust': 0.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641866400, 'temp': 10.37, 'feels_like': 9.92, 'pressure': 1019, 'humidity': 94, 'dew_point': 9.45, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 77, 'wind_gust': 0.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641870000, 'temp': 10.37, 'feels_like': 9.92, 'pressure': 1020, 'humidity': 94, 'dew_point': 9.45, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 177, 'wind_gust': 0.93, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641873600, 'temp': 10.37, 'feels_like': 9.86, 'pressure': 1019, 'humidity': 92, 'dew_point': 9.13, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 263, 'wind_gust': 0.8, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641877200, 'temp': 10.37, 'feels_like': 9.89, 'pressure': 1019, 'humidity': 93, 'dew_point': 9.29, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.13, 'wind_deg': 337, 'wind_gust': 0.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641880800, 'temp': 10.37, 'feels_like': 9.92, 'pressure': 1018, 'humidity': 94, 'dew_point': 9.45, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 290, 'wind_gust': 0.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641884400, 'temp': 10.37, 'feels_like': 9.92, 'pressure': 1017, 'humidity': 94, 'dew_point': 9.45, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 294, 'wind_gust': 1.14, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641888000, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1016, 'humidity': 94, 'dew_point': 8.45, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 309, 'wind_gust': 0.94, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641891600, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1017, 'humidity': 96, 'dew_point': 8.77, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 307, 'wind_gust': 1.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641895200, 'temp': 8.37, 'feels_like': 8.37, 'pressure': 1017, 'humidity': 96, 'dew_point': 7.77, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 314, 'wind_gust': 0.83, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641898800, 'temp': 8.37, 'feels_like': 8.37, 'pressure': 1018, 'humidity': 97, 'dew_point': 7.92, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 297, 'wind_gust': 0.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641902400, 'temp': 8.37, 'feels_like': 8.37, 'pressure': 1018, 'humidity': 96, 'dew_point': 7.77, 'uvi': 0.41, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 305, 'wind_gust': 1.09, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641906000, 'temp': 10.37, 'feels_like': 9.86, 'pressure': 1019, 'humidity': 92, 'dew_point': 9.13, 'uvi': 1.88, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 338, 'wind_gust': 1.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641909600, 'temp': 11.37, 'feels_like': 10.91, 'pressure': 1019, 'humidity': 90, 'dew_point': 9.79, 'uvi': 4.49, 'clouds': 95, 'visibility': 9557, 'wind_speed': 0.5, 'wind_deg': 9, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641913200, 'temp': 11.37, 'feels_like': 10.76, 'pressure': 1019, 'humidity': 84, 'dew_point': 8.77, 'uvi': 7.58, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 15, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641916800, 'temp': 12.37, 'feels_like': 11.8, 'pressure': 1018, 'humidity': 82, 'dew_point': 9.39, 'uvi': 11.73, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 322, 'wind_gust': 1.51, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641920400, 'temp': 14.37, 'feels_like': 14.06, 'pressure': 1017, 'humidity': 84, 'dew_point': 11.7, 'uvi': 12.76, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 317, 'wind_gust': 1.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.34}}, {'dt': 1641924000, 'temp': 15.37, 'feels_like': 15.18, 'pressure': 1016, 'humidity': 85, 'dew_point': 12.86, 'uvi': 11.59, 'clouds': 94, 'visibility': 6242, 'wind_speed': 0.65, 'wind_deg': 317, 'wind_gust': 1.86, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.49}}, {'dt': 1641927600, 'temp': 16.37, 'feels_like': 16.41, 'pressure': 1015, 'humidity': 90, 'dew_point': 14.73, 'uvi': 8.33, 'clouds': 100, 'visibility': 7792, 'wind_speed': 0.65, 'wind_deg': 316, 'wind_gust': 2.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1641931200, 'temp': 15.37, 'feels_like': 15.36, 'pressure': 1015, 'humidity': 92, 'dew_point': 14.08, 'uvi': 4.85, 'clouds': 99, 'visibility': 3325, 'wind_speed': 0.48, 'wind_deg': 305, 'wind_gust': 1.7, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}, {'dt': 1641934800, 'temp': 14.37, 'feels_like': 14.26, 'pressure': 1015, 'humidity': 92, 'dew_point': 13.09, 'uvi': 1.96, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.05, 'wind_deg': 257, 'wind_gust': 1.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1641938400, 'temp': 14.37, 'feels_like': 14.29, 'pressure': 1016, 'humidity': 93, 'dew_point': 13.25, 'uvi': 0.46, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.1, 'wind_deg': 330, 'wind_gust': 1.26, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641942000, 'temp': 12.37, 'feels_like': 12.22, 'pressure': 1017, 'humidity': 98, 'dew_point': 12.06, 'uvi': 0, 'clouds': 95, 'visibility': 4828, 'wind_speed': 0.35, 'wind_deg': 309, 'wind_gust': 1.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 00:00:00 | 85.000000 | 10.600000 | 11.040000 | 95.000000 | 1017.000000 |  | 11.370000 | 0.000000 | 9839.000000 | 43.000000 | 0.73 | 0.320000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 01:00:00 | 93.000000 | 10.440000 | 11.020000 | 94.000000 | 1018.000000 |  | 11.370000 | 0.000000 | 10000.000000 | 53.000000 | 0.77 | 0.160000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 02:00:00 | 89.000000 | 9.450000 | 9.920000 | 94.000000 | 1019.000000 |  | 10.370000 | 0.000000 | 10000.000000 | 77.000000 | 0.83 | 0.270000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 03:00:00 | 78.000000 | 9.450000 | 9.920000 | 94.000000 | 1020.000000 |  | 10.370000 | 0.000000 | 10000.000000 | 177.000000 | 0.93 | 0.340000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 04:00:00 | 77.000000 | 9.130000 | 9.860000 | 92.000000 | 1019.000000 |  | 10.370000 | 0.000000 | 10000.000000 | 263.000000 | 0.8 | 0.230000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 05:00:00 | 78.000000 | 9.290000 | 9.890000 | 93.000000 | 1019.000000 | 0.2 | 10.370000 | 0.000000 | 10000.000000 | 337.000000 | 0.98 | 0.130000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 06:00:00 | 83.000000 | 9.450000 | 9.920000 | 94.000000 | 1018.000000 | 0.2 | 10.370000 | 0.000000 | 10000.000000 | 290.000000 | 0.93 | 0.560000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 07:00:00 | 91.000000 | 9.450000 | 9.920000 | 94.000000 | 1017.000000 | 0.1 | 10.370000 | 0.000000 | 10000.000000 | 294.000000 | 1.14 | 0.670000 | 500 | Rain | light rain | 10n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 08:00:00 | 95.000000 | 8.450000 | 9.370000 | 94.000000 | 1016.000000 |  | 9.370000 | 0.000000 | 10000.000000 | 309.000000 | 0.94 | 0.530000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 09:00:00 | 97.000000 | 8.770000 | 9.370000 | 96.000000 | 1017.000000 |  | 9.370000 | 0.000000 | 10000.000000 | 307.000000 | 1.14 | 0.780000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 10:00:00 | 97.000000 | 7.770000 | 8.370000 | 96.000000 | 1017.000000 | 0.11 | 8.370000 | 0.000000 | 10000.000000 | 314.000000 | 0.83 | 0.350000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 11:00:00 | 97.000000 | 7.920000 | 8.370000 | 97.000000 | 1018.000000 |  | 8.370000 | 0.000000 | 10000.000000 | 297.000000 | 0.89 | 0.300000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 12:00:00 | 82.000000 | 7.770000 | 8.370000 | 96.000000 | 1018.000000 |  | 8.370000 | 0.410000 | 10000.000000 | 305.000000 | 1.09 | 0.660000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 13:00:00 | 91.000000 | 9.130000 | 9.860000 | 92.000000 | 1019.000000 |  | 10.370000 | 1.880000 | 10000.000000 | 338.000000 | 1.39 | 0.510000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 14:00:00 | 95.000000 | 9.790000 | 10.910000 | 90.000000 | 1019.000000 | 0.13 | 11.370000 | 4.490000 | 9557.000000 | 9.000000 | 1.27 | 0.500000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 15:00:00 | 96.000000 | 8.770000 | 10.760000 | 84.000000 | 1019.000000 | 0.12 | 11.370000 | 7.580000 | 10000.000000 | 15.000000 | 1.27 | 0.540000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 16:00:00 | 97.000000 | 9.390000 | 11.800000 | 82.000000 | 1018.000000 | 0.17 | 12.370000 | 11.730000 | 10000.000000 | 322.000000 | 1.51 | 0.490000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 17:00:00 | 96.000000 | 11.700000 | 14.060000 | 84.000000 | 1017.000000 | 0.34 | 14.370000 | 12.760000 | 10000.000000 | 317.000000 | 1.73 | 0.640000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 18:00:00 | 94.000000 | 12.860000 | 15.180000 | 85.000000 | 1016.000000 | 0.49 | 15.370000 | 11.590000 | 6242.000000 | 317.000000 | 1.86 | 0.650000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 19:00:00 | 100.000000 | 14.730000 | 16.410000 | 90.000000 | 1015.000000 | 0.38 | 16.370000 | 8.330000 | 7792.000000 | 316.000000 | 2.01 | 0.650000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 20:00:00 | 99.000000 | 14.080000 | 15.360000 | 92.000000 | 1015.000000 | 0.44 | 15.370000 | 4.850000 | 3325.000000 | 305.000000 | 1.7 | 0.480000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 21:00:00 | 99.000000 | 13.090000 | 14.260000 | 92.000000 | 1015.000000 | 0.22 | 14.370000 | 1.960000 | 10000.000000 | 257.000000 | 1.53 | 0.050000 | 500 | Rain | light rain | 10d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 22:00:00 | 98.000000 | 13.250000 | 14.290000 | 93.000000 | 1016.000000 |  | 14.370000 | 0.460000 | 10000.000000 | 330.000000 | 1.26 | 0.100000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 23:00:00 | 95.000000 | 12.060000 | 12.220000 | 98.000000 | 1017.000000 |  | 12.370000 | 0.000000 | 4828.000000 | 309.000000 | 1.21 | 0.350000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35020350_OWM_Clouds_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Clouds_20220112.png)
![CNE_IDEAM_Station35020350_OWM_Dewpoint_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Dewpoint_20220112.png)
![CNE_IDEAM_Station35020350_OWM_Feelslike_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Feelslike_20220112.png)
![CNE_IDEAM_Station35020350_OWM_Humidity_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Humidity_20220112.png)
![CNE_IDEAM_Station35020350_OWM_Pressure_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Pressure_20220112.png)
![CNE_IDEAM_Station35020350_OWM_Rain_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Rain_20220112.png)
![CNE_IDEAM_Station35020350_OWM_Temp_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Temp_20220112.png)
![CNE_IDEAM_Station35020350_OWM_UVI_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_UVI_20220112.png)
![CNE_IDEAM_Station35020350_OWM_Visibility_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Visibility_20220112.png)
![CNE_IDEAM_Station35020350_OWM_Windgust_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Windgust_20220112.png)
![CNE_IDEAM_Station35020350_OWM_Windspeed_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Windspeed_20220112.png)

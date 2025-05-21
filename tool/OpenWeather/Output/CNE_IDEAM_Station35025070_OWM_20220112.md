
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - TAQUES LOS [35025070] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35025070_OWM_20220112.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220112.csv)

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

### (CNE index 1868) Open Weather values for station 35025070 - TAQUES LOS [35025070]

JSON data from API OWM:

```
{'lat': 4.1967, 'lon': -74.1909, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641899465, 'sunrise': 1641899257, 'sunset': 1641942081, 'temp': 6.57, 'feels_like': 6.57, 'pressure': 1018, 'humidity': 97, 'dew_point': 6.13, 'uvi': 0, 'clouds': 98, 'visibility': 6487, 'wind_speed': 0.44, 'wind_deg': 293, 'wind_gust': 0.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641859200, 'temp': 9.57, 'feels_like': 9.57, 'pressure': 1017, 'humidity': 94, 'dew_point': 8.65, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 16, 'wind_gust': 0.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641862800, 'temp': 9.57, 'feels_like': 9.57, 'pressure': 1018, 'humidity': 94, 'dew_point': 8.65, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 30, 'wind_gust': 0.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641866400, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1019, 'humidity': 93, 'dew_point': 7.5, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 67, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641870000, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1020, 'humidity': 93, 'dew_point': 7.5, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 141, 'wind_gust': 0.97, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641873600, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1019, 'humidity': 92, 'dew_point': 7.35, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 307, 'wind_gust': 0.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641877200, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1019, 'humidity': 93, 'dew_point': 7.5, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 25, 'wind_gust': 1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1641880800, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1018, 'humidity': 94, 'dew_point': 7.66, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 315, 'wind_gust': 0.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.25}}, {'dt': 1641884400, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1017, 'humidity': 95, 'dew_point': 7.82, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 306, 'wind_gust': 1.17, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641888000, 'temp': 7.57, 'feels_like': 7.57, 'pressure': 1016, 'humidity': 95, 'dew_point': 6.82, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 314, 'wind_gust': 1.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641891600, 'temp': 7.57, 'feels_like': 7.57, 'pressure': 1017, 'humidity': 97, 'dew_point': 7.13, 'uvi': 0, 'clouds': 98, 'visibility': 8057, 'wind_speed': 0.92, 'wind_deg': 306, 'wind_gust': 1.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641895200, 'temp': 6.57, 'feels_like': 6.57, 'pressure': 1017, 'humidity': 97, 'dew_point': 6.13, 'uvi': 0, 'clouds': 98, 'visibility': 5990, 'wind_speed': 0.48, 'wind_deg': 310, 'wind_gust': 0.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641898800, 'temp': 6.57, 'feels_like': 6.57, 'pressure': 1018, 'humidity': 97, 'dew_point': 6.13, 'uvi': 0, 'clouds': 98, 'visibility': 6487, 'wind_speed': 0.44, 'wind_deg': 293, 'wind_gust': 0.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641902400, 'temp': 6.57, 'feels_like': 6.57, 'pressure': 1018, 'humidity': 97, 'dew_point': 6.13, 'uvi': 0.41, 'clouds': 86, 'visibility': 5896, 'wind_speed': 0.78, 'wind_deg': 304, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641906000, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1019, 'humidity': 94, 'dew_point': 7.66, 'uvi': 1.88, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 317, 'wind_gust': 1.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641909600, 'temp': 9.57, 'feels_like': 9.57, 'pressure': 1020, 'humidity': 92, 'dew_point': 8.34, 'uvi': 4.49, 'clouds': 96, 'visibility': 6251, 'wind_speed': 0.71, 'wind_deg': 332, 'wind_gust': 1.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641913200, 'temp': 9.57, 'feels_like': 9.57, 'pressure': 1019, 'humidity': 86, 'dew_point': 7.35, 'uvi': 7.58, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 329, 'wind_gust': 1.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641916800, 'temp': 10.57, 'feels_like': 9.82, 'pressure': 1018, 'humidity': 82, 'dew_point': 7.63, 'uvi': 11.73, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 306, 'wind_gust': 1.48, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1641920400, 'temp': 12.57, 'feels_like': 12.05, 'pressure': 1017, 'humidity': 83, 'dew_point': 9.76, 'uvi': 12.76, 'clouds': 96, 'visibility': 9587, 'wind_speed': 1.26, 'wind_deg': 306, 'wind_gust': 1.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1641924000, 'temp': 13.57, 'feels_like': 13.2, 'pressure': 1016, 'humidity': 85, 'dew_point': 11.1, 'uvi': 11.59, 'clouds': 94, 'visibility': 8369, 'wind_speed': 1.31, 'wind_deg': 299, 'wind_gust': 1.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.51}}, {'dt': 1641927600, 'temp': 14.57, 'feels_like': 14.41, 'pressure': 1015, 'humidity': 89, 'dew_point': 12.78, 'uvi': 8.33, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 300, 'wind_gust': 2.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.41}}, {'dt': 1641931200, 'temp': 13.57, 'feels_like': 13.36, 'pressure': 1015, 'humidity': 91, 'dew_point': 12.13, 'uvi': 4.85, 'clouds': 98, 'visibility': 5427, 'wind_speed': 1.04, 'wind_deg': 294, 'wind_gust': 1.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.46}}, {'dt': 1641934800, 'temp': 12.57, 'feels_like': 12.28, 'pressure': 1015, 'humidity': 92, 'dew_point': 11.31, 'uvi': 1.96, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 281, 'wind_gust': 1.52, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1641938400, 'temp': 12.57, 'feels_like': 12.28, 'pressure': 1016, 'humidity': 92, 'dew_point': 11.31, 'uvi': 0.46, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 295, 'wind_gust': 1.28, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}, {'dt': 1641942000, 'temp': 10.57, 'feels_like': 10.22, 'pressure': 1017, 'humidity': 97, 'dew_point': 10.11, 'uvi': 0, 'clouds': 93, 'visibility': 5653, 'wind_speed': 0.6, 'wind_deg': 297, 'wind_gust': 1.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 00:00:00 | 78.000000 | 8.650000 | 9.570000 | 94.000000 | 1017.000000 |  | 9.570000 | 0.000000 | 10000.000000 | 16.000000 | 0.74 | 0.340000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 01:00:00 | 88.000000 | 8.650000 | 9.570000 | 94.000000 | 1018.000000 |  | 9.570000 | 0.000000 | 10000.000000 | 30.000000 | 0.78 | 0.190000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 02:00:00 | 85.000000 | 7.500000 | 8.570000 | 93.000000 | 1019.000000 |  | 8.570000 | 0.000000 | 10000.000000 | 67.000000 | 0.88 | 0.400000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 03:00:00 | 74.000000 | 7.500000 | 8.570000 | 93.000000 | 1020.000000 |  | 8.570000 | 0.000000 | 10000.000000 | 141.000000 | 0.97 | 0.240000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 04:00:00 | 74.000000 | 7.350000 | 8.570000 | 92.000000 | 1019.000000 |  | 8.570000 | 0.000000 | 10000.000000 | 307.000000 | 0.83 | 0.200000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 05:00:00 | 77.000000 | 7.500000 | 8.570000 | 93.000000 | 1019.000000 | 0.24 | 8.570000 | 0.000000 | 10000.000000 | 25.000000 | 1 | 0.260000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 06:00:00 | 88.000000 | 7.660000 | 8.570000 | 94.000000 | 1018.000000 | 0.25 | 8.570000 | 0.000000 | 10000.000000 | 315.000000 | 0.93 | 0.470000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 07:00:00 | 94.000000 | 7.820000 | 8.570000 | 95.000000 | 1017.000000 | 0.12 | 8.570000 | 0.000000 | 10000.000000 | 306.000000 | 1.17 | 0.670000 | 500 | Rain | light rain | 10n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 08:00:00 | 97.000000 | 6.820000 | 7.570000 | 95.000000 | 1016.000000 |  | 7.570000 | 0.000000 | 10000.000000 | 314.000000 | 1.06 | 0.630000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 09:00:00 | 98.000000 | 7.130000 | 7.570000 | 97.000000 | 1017.000000 |  | 7.570000 | 0.000000 | 8057.000000 | 306.000000 | 1.34 | 0.920000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 10:00:00 | 98.000000 | 6.130000 | 6.570000 | 97.000000 | 1017.000000 | 0.13 | 6.570000 | 0.000000 | 5990.000000 | 310.000000 | 0.93 | 0.480000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 11:00:00 | 98.000000 | 6.130000 | 6.570000 | 97.000000 | 1018.000000 |  | 6.570000 | 0.000000 | 6487.000000 | 293.000000 | 0.96 | 0.440000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 12:00:00 | 86.000000 | 6.130000 | 6.570000 | 97.000000 | 1018.000000 |  | 6.570000 | 0.410000 | 5896.000000 | 304.000000 | 1.18 | 0.780000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 13:00:00 | 93.000000 | 7.660000 | 8.570000 | 94.000000 | 1019.000000 |  | 8.570000 | 1.880000 | 10000.000000 | 317.000000 | 1.49 | 0.790000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 14:00:00 | 96.000000 | 8.340000 | 9.570000 | 92.000000 | 1020.000000 | 0.15 | 9.570000 | 4.490000 | 6251.000000 | 332.000000 | 1.24 | 0.710000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 15:00:00 | 97.000000 | 7.350000 | 9.570000 | 86.000000 | 1019.000000 | 0.12 | 9.570000 | 7.580000 | 10000.000000 | 329.000000 | 1.21 | 0.780000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 16:00:00 | 98.000000 | 7.630000 | 9.820000 | 82.000000 | 1018.000000 | 0.19 | 10.570000 | 11.730000 | 10000.000000 | 306.000000 | 1.48 | 1.080000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 17:00:00 | 96.000000 | 9.760000 | 12.050000 | 83.000000 | 1017.000000 | 0.38 | 12.570000 | 12.760000 | 9587.000000 | 306.000000 | 1.75 | 1.260000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 18:00:00 | 94.000000 | 11.100000 | 13.200000 | 85.000000 | 1016.000000 | 0.51 | 13.570000 | 11.590000 | 8369.000000 | 299.000000 | 1.79 | 1.310000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 19:00:00 | 99.000000 | 12.780000 | 14.410000 | 89.000000 | 1015.000000 | 0.41 | 14.570000 | 8.330000 | 10000.000000 | 300.000000 | 2.1 | 1.290000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 20:00:00 | 98.000000 | 12.130000 | 13.360000 | 91.000000 | 1015.000000 | 0.46 | 13.570000 | 4.850000 | 5427.000000 | 294.000000 | 1.77 | 1.040000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 21:00:00 | 99.000000 | 11.310000 | 12.280000 | 92.000000 | 1015.000000 | 0.2 | 12.570000 | 1.960000 | 10000.000000 | 281.000000 | 1.52 | 0.520000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 22:00:00 | 97.000000 | 11.310000 | 12.280000 | 92.000000 | 1016.000000 | 0.1 | 12.570000 | 0.460000 | 10000.000000 | 295.000000 | 1.28 | 0.420000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 23:00:00 | 93.000000 | 10.110000 | 10.220000 | 97.000000 | 1017.000000 | 0.11 | 10.570000 | 0.000000 | 5653.000000 | 297.000000 | 1.3 | 0.600000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station35025070_OWM_Clouds_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Clouds_20220112.png)
![CNE_IDEAM_Station35025070_OWM_Dewpoint_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Dewpoint_20220112.png)
![CNE_IDEAM_Station35025070_OWM_Feelslike_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Feelslike_20220112.png)
![CNE_IDEAM_Station35025070_OWM_Humidity_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Humidity_20220112.png)
![CNE_IDEAM_Station35025070_OWM_Pressure_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Pressure_20220112.png)
![CNE_IDEAM_Station35025070_OWM_Rain_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Rain_20220112.png)
![CNE_IDEAM_Station35025070_OWM_Temp_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Temp_20220112.png)
![CNE_IDEAM_Station35025070_OWM_UVI_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_UVI_20220112.png)
![CNE_IDEAM_Station35025070_OWM_Visibility_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Visibility_20220112.png)
![CNE_IDEAM_Station35025070_OWM_Windgust_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Windgust_20220112.png)
![CNE_IDEAM_Station35025070_OWM_Windspeed_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Windspeed_20220112.png)

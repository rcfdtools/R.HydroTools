
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ANIMAS LAS [35027150] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35027150_OWM_20220112.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220112.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.13797222,-74.17380556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.13797222&lon=-74.17380556)

| Parameter | Value |
|---|---|
| Code | 35027150 |
| Name | ANIMAS LAS [35027150] |
| Latitude, ° | 4.13797222 |
| Longitude, ° | -74.17380556 |
| Elevation, m | 2840 |
| Category | Limnigráfica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1985-01-15 00:00:00 |
| Suspension date | NaT |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Chochal |
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

### (CNE index 1625) Open Weather values for station 35027150 - ANIMAS LAS [35027150]

JSON data from API OWM:

```
{'lat': 4.138, 'lon': -74.1738, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641899465, 'sunrise': 1641899247, 'sunset': 1641942083, 'temp': 8.46, 'feels_like': 8.46, 'pressure': 1018, 'humidity': 97, 'dew_point': 8.01, 'uvi': 0, 'clouds': 96, 'visibility': 8624, 'wind_speed': 0.48, 'wind_deg': 303, 'wind_gust': 0.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641859200, 'temp': 11.46, 'feels_like': 11.12, 'pressure': 1017, 'humidity': 94, 'dew_point': 10.53, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 357, 'wind_gust': 0.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641862800, 'temp': 11.46, 'feels_like': 11.09, 'pressure': 1018, 'humidity': 93, 'dew_point': 10.37, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 2, 'wind_gust': 0.84, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641866400, 'temp': 10.46, 'feels_like': 9.99, 'pressure': 1020, 'humidity': 93, 'dew_point': 9.38, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 35, 'wind_gust': 0.89, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641870000, 'temp': 10.46, 'feels_like': 9.99, 'pressure': 1020, 'humidity': 93, 'dew_point': 9.38, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.14, 'wind_deg': 323, 'wind_gust': 1.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641873600, 'temp': 10.46, 'feels_like': 9.96, 'pressure': 1020, 'humidity': 92, 'dew_point': 9.22, 'uvi': 0, 'clouds': 69, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 313, 'wind_gust': 0.99, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641877200, 'temp': 10.46, 'feels_like': 9.99, 'pressure': 1019, 'humidity': 93, 'dew_point': 9.38, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 330, 'wind_gust': 1.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641880800, 'temp': 10.46, 'feels_like': 10.04, 'pressure': 1018, 'humidity': 95, 'dew_point': 9.69, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 310, 'wind_gust': 1.14, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641884400, 'temp': 10.46, 'feels_like': 10.04, 'pressure': 1017, 'humidity': 95, 'dew_point': 9.69, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 305, 'wind_gust': 1.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641888000, 'temp': 9.46, 'feels_like': 9.46, 'pressure': 1016, 'humidity': 95, 'dew_point': 8.7, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 313, 'wind_gust': 1.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641891600, 'temp': 9.46, 'feels_like': 9.46, 'pressure': 1017, 'humidity': 96, 'dew_point': 8.85, 'uvi': 0, 'clouds': 96, 'visibility': 8880, 'wind_speed': 1, 'wind_deg': 306, 'wind_gust': 1.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641895200, 'temp': 8.46, 'feels_like': 8.46, 'pressure': 1017, 'humidity': 97, 'dew_point': 8.01, 'uvi': 0, 'clouds': 97, 'visibility': 7578, 'wind_speed': 0.64, 'wind_deg': 311, 'wind_gust': 1.06, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641898800, 'temp': 8.46, 'feels_like': 8.46, 'pressure': 1018, 'humidity': 97, 'dew_point': 8.01, 'uvi': 0, 'clouds': 96, 'visibility': 8624, 'wind_speed': 0.48, 'wind_deg': 303, 'wind_gust': 0.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641902400, 'temp': 8.46, 'feels_like': 8.46, 'pressure': 1019, 'humidity': 95, 'dew_point': 7.71, 'uvi': 0.41, 'clouds': 79, 'visibility': 7604, 'wind_speed': 0.73, 'wind_deg': 313, 'wind_gust': 1.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641906000, 'temp': 10.46, 'feels_like': 9.96, 'pressure': 1019, 'humidity': 92, 'dew_point': 9.22, 'uvi': 1.88, 'clouds': 87, 'visibility': 9041, 'wind_speed': 0.67, 'wind_deg': 331, 'wind_gust': 1.55, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641909600, 'temp': 11.46, 'feels_like': 11.01, 'pressure': 1020, 'humidity': 90, 'dew_point': 9.88, 'uvi': 4.49, 'clouds': 93, 'visibility': 7317, 'wind_speed': 0.63, 'wind_deg': 347, 'wind_gust': 1.4, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641913200, 'temp': 11.46, 'feels_like': 10.88, 'pressure': 1019, 'humidity': 85, 'dew_point': 9.03, 'uvi': 7.58, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 344, 'wind_gust': 1.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641916800, 'temp': 12.46, 'feels_like': 11.93, 'pressure': 1018, 'humidity': 83, 'dew_point': 9.66, 'uvi': 11.73, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 319, 'wind_gust': 1.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1641920400, 'temp': 14.46, 'feels_like': 14.13, 'pressure': 1018, 'humidity': 83, 'dew_point': 11.61, 'uvi': 12.76, 'clouds': 95, 'visibility': 9668, 'wind_speed': 0.82, 'wind_deg': 316, 'wind_gust': 1.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.37}}, {'dt': 1641924000, 'temp': 15.46, 'feels_like': 15.28, 'pressure': 1016, 'humidity': 85, 'dew_point': 12.95, 'uvi': 11.59, 'clouds': 91, 'visibility': 9766, 'wind_speed': 0.91, 'wind_deg': 305, 'wind_gust': 1.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}, {'dt': 1641927600, 'temp': 16.46, 'feels_like': 16.46, 'pressure': 1015, 'humidity': 88, 'dew_point': 14.47, 'uvi': 8.33, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 305, 'wind_gust': 2.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.37}}, {'dt': 1641931200, 'temp': 15.46, 'feels_like': 15.39, 'pressure': 1015, 'humidity': 89, 'dew_point': 13.66, 'uvi': 4.85, 'clouds': 96, 'visibility': 7810, 'wind_speed': 0.88, 'wind_deg': 303, 'wind_gust': 1.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.37}}, {'dt': 1641934800, 'temp': 14.46, 'feels_like': 14.34, 'pressure': 1015, 'humidity': 91, 'dew_point': 13.01, 'uvi': 1.96, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 305, 'wind_gust': 1.56, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641938400, 'temp': 14.46, 'feels_like': 14.34, 'pressure': 1016, 'humidity': 91, 'dew_point': 13.01, 'uvi': 0.46, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 313, 'wind_gust': 1.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641942000, 'temp': 12.46, 'feels_like': 12.27, 'pressure': 1017, 'humidity': 96, 'dew_point': 11.84, 'uvi': 0, 'clouds': 92, 'visibility': 3777, 'wind_speed': 0.61, 'wind_deg': 308, 'wind_gust': 1.33, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 00:00:00 | 70.000000 | 10.530000 | 11.120000 | 94.000000 | 1017.000000 |  | 11.460000 | 0.000000 | 10000.000000 | 357.000000 | 0.9 | 0.480000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 01:00:00 | 78.000000 | 10.370000 | 11.090000 | 93.000000 | 1018.000000 |  | 11.460000 | 0.000000 | 10000.000000 | 2.000000 | 0.84 | 0.300000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 02:00:00 | 75.000000 | 9.380000 | 9.990000 | 93.000000 | 1020.000000 |  | 10.460000 | 0.000000 | 10000.000000 | 35.000000 | 0.89 | 0.390000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 03:00:00 | 68.000000 | 9.380000 | 9.990000 | 93.000000 | 1020.000000 |  | 10.460000 | 0.000000 | 10000.000000 | 323.000000 | 1.01 | 0.140000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 04:00:00 | 69.000000 | 9.220000 | 9.960000 | 92.000000 | 1020.000000 |  | 10.460000 | 0.000000 | 10000.000000 | 313.000000 | 0.99 | 0.540000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 05:00:00 | 72.000000 | 9.380000 | 9.990000 | 93.000000 | 1019.000000 | 0.16 | 10.460000 | 0.000000 | 10000.000000 | 330.000000 | 1.1 | 0.440000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 06:00:00 | 83.000000 | 9.690000 | 10.040000 | 95.000000 | 1018.000000 | 0.18 | 10.460000 | 0.000000 | 10000.000000 | 310.000000 | 1.14 | 0.770000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 07:00:00 | 90.000000 | 9.690000 | 10.040000 | 95.000000 | 1017.000000 |  | 10.460000 | 0.000000 | 10000.000000 | 305.000000 | 1.41 | 0.900000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 08:00:00 | 95.000000 | 8.700000 | 9.460000 | 95.000000 | 1016.000000 |  | 9.460000 | 0.000000 | 10000.000000 | 313.000000 | 1.22 | 0.750000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 09:00:00 | 96.000000 | 8.850000 | 9.460000 | 96.000000 | 1017.000000 |  | 9.460000 | 0.000000 | 8880.000000 | 306.000000 | 1.44 | 1.000000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 10:00:00 | 97.000000 | 8.010000 | 8.460000 | 97.000000 | 1017.000000 | 0.11 | 8.460000 | 0.000000 | 7578.000000 | 311.000000 | 1.06 | 0.640000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 11:00:00 | 96.000000 | 8.010000 | 8.460000 | 97.000000 | 1018.000000 |  | 8.460000 | 0.000000 | 8624.000000 | 303.000000 | 0.97 | 0.480000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 12:00:00 | 79.000000 | 7.710000 | 8.460000 | 95.000000 | 1019.000000 |  | 8.460000 | 0.410000 | 7604.000000 | 313.000000 | 1.15 | 0.730000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 13:00:00 | 87.000000 | 9.220000 | 9.960000 | 92.000000 | 1019.000000 |  | 10.460000 | 1.880000 | 9041.000000 | 331.000000 | 1.55 | 0.670000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 14:00:00 | 93.000000 | 9.880000 | 11.010000 | 90.000000 | 1020.000000 | 0.13 | 11.460000 | 4.490000 | 7317.000000 | 347.000000 | 1.4 | 0.630000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 15:00:00 | 95.000000 | 9.030000 | 10.880000 | 85.000000 | 1019.000000 | 0.13 | 11.460000 | 7.580000 | 10000.000000 | 344.000000 | 1.43 | 0.650000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 16:00:00 | 96.000000 | 9.660000 | 11.930000 | 83.000000 | 1018.000000 | 0.21 | 12.460000 | 11.730000 | 10000.000000 | 319.000000 | 1.63 | 0.700000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 17:00:00 | 95.000000 | 11.610000 | 14.130000 | 83.000000 | 1018.000000 | 0.37 | 14.460000 | 12.760000 | 9668.000000 | 316.000000 | 1.79 | 0.820000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 18:00:00 | 91.000000 | 12.950000 | 15.280000 | 85.000000 | 1016.000000 | 0.44 | 15.460000 | 11.590000 | 9766.000000 | 305.000000 | 1.75 | 0.910000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 19:00:00 | 98.000000 | 14.470000 | 16.460000 | 88.000000 | 1015.000000 | 0.37 | 16.460000 | 8.330000 | 10000.000000 | 305.000000 | 2.03 | 1.030000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 20:00:00 | 96.000000 | 13.660000 | 15.390000 | 89.000000 | 1015.000000 | 0.37 | 15.460000 | 4.850000 | 7810.000000 | 303.000000 | 1.82 | 0.880000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 21:00:00 | 97.000000 | 13.010000 | 14.340000 | 91.000000 | 1015.000000 | 0.18 | 14.460000 | 1.960000 | 10000.000000 | 305.000000 | 1.56 | 0.490000 | 500 | Rain | light rain | 10d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 22:00:00 | 95.000000 | 13.010000 | 14.340000 | 91.000000 | 1016.000000 |  | 14.460000 | 0.460000 | 10000.000000 | 313.000000 | 1.3 | 0.430000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 23:00:00 | 92.000000 | 11.840000 | 12.270000 | 96.000000 | 1017.000000 | 0.11 | 12.460000 | 0.000000 | 3777.000000 | 308.000000 | 1.33 | 0.610000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station35027150_OWM_Clouds_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Clouds_20220112.png)
![CNE_IDEAM_Station35027150_OWM_Dewpoint_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Dewpoint_20220112.png)
![CNE_IDEAM_Station35027150_OWM_Feelslike_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Feelslike_20220112.png)
![CNE_IDEAM_Station35027150_OWM_Humidity_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Humidity_20220112.png)
![CNE_IDEAM_Station35027150_OWM_Pressure_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Pressure_20220112.png)
![CNE_IDEAM_Station35027150_OWM_Rain_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Rain_20220112.png)
![CNE_IDEAM_Station35027150_OWM_Temp_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Temp_20220112.png)
![CNE_IDEAM_Station35027150_OWM_UVI_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_UVI_20220112.png)
![CNE_IDEAM_Station35027150_OWM_Visibility_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Visibility_20220112.png)
![CNE_IDEAM_Station35027150_OWM_Windgust_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Windgust_20220112.png)
![CNE_IDEAM_Station35027150_OWM_Windspeed_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Windspeed_20220112.png)

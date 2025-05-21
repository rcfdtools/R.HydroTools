
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - NAZARETH [35020310] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35020310_OWM_20220112.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220112.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.17225,-74.146) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.17225&lon=-74.146)

| Parameter | Value |
|---|---|
| Code | 35020310 |
| Name | NAZARETH [35020310] |
| Latitude, ° | 4.17225 |
| Longitude, ° | -74.146 |
| Elevation, m | 2800 |
| Category | Pluviográfica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1984-07-15 00:00:00 |
| Suspension date | NaT |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Ceibas |
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

### (CNE index 1858) Open Weather values for station 35020310 - NAZARETH [35020310]

JSON data from API OWM:

```
{'lat': 4.1723, 'lon': -74.146, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641899465, 'sunrise': 1641899244, 'sunset': 1641942073, 'temp': 10.9, 'feels_like': 10.55, 'pressure': 1018, 'humidity': 96, 'dew_point': 10.29, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 303, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641859200, 'temp': 13.9, 'feels_like': 13.83, 'pressure': 1017, 'humidity': 95, 'dew_point': 13.11, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 18, 'wind_gust': 0.84, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641862800, 'temp': 13.9, 'feels_like': 13.8, 'pressure': 1018, 'humidity': 94, 'dew_point': 12.95, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 16, 'wind_gust': 0.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641866400, 'temp': 12.9, 'feels_like': 12.7, 'pressure': 1019, 'humidity': 94, 'dew_point': 11.96, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 49, 'wind_gust': 0.84, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641870000, 'temp': 12.9, 'feels_like': 12.67, 'pressure': 1020, 'humidity': 93, 'dew_point': 11.8, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.13, 'wind_deg': 220, 'wind_gust': 0.96, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641873600, 'temp': 12.9, 'feels_like': 12.65, 'pressure': 1019, 'humidity': 92, 'dew_point': 11.63, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 296, 'wind_gust': 0.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641877200, 'temp': 12.9, 'feels_like': 12.67, 'pressure': 1019, 'humidity': 93, 'dew_point': 11.8, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 320, 'wind_gust': 1.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641880800, 'temp': 12.9, 'feels_like': 12.7, 'pressure': 1018, 'humidity': 94, 'dew_point': 11.96, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 298, 'wind_gust': 1.06, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641884400, 'temp': 12.9, 'feels_like': 12.7, 'pressure': 1017, 'humidity': 94, 'dew_point': 11.96, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 299, 'wind_gust': 1.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641888000, 'temp': 11.9, 'feels_like': 11.6, 'pressure': 1016, 'humidity': 94, 'dew_point': 10.97, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 312, 'wind_gust': 1.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641891600, 'temp': 11.9, 'feels_like': 11.65, 'pressure': 1017, 'humidity': 96, 'dew_point': 11.28, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 307, 'wind_gust': 1.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641895200, 'temp': 10.9, 'feels_like': 10.55, 'pressure': 1017, 'humidity': 96, 'dew_point': 10.29, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 314, 'wind_gust': 0.93, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641898800, 'temp': 10.9, 'feels_like': 10.55, 'pressure': 1018, 'humidity': 96, 'dew_point': 10.29, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 303, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641902400, 'temp': 10.9, 'feels_like': 10.53, 'pressure': 1018, 'humidity': 95, 'dew_point': 10.13, 'uvi': 0.41, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 312, 'wind_gust': 1.09, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641906000, 'temp': 12.9, 'feels_like': 12.65, 'pressure': 1019, 'humidity': 92, 'dew_point': 11.63, 'uvi': 1.88, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 346, 'wind_gust': 1.45, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641909600, 'temp': 13.9, 'feels_like': 13.67, 'pressure': 1020, 'humidity': 89, 'dew_point': 12.12, 'uvi': 4.49, 'clouds': 93, 'visibility': 8875, 'wind_speed': 0.53, 'wind_deg': 13, 'wind_gust': 1.36, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641913200, 'temp': 13.9, 'feels_like': 13.54, 'pressure': 1019, 'humidity': 84, 'dew_point': 11.24, 'uvi': 7.58, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 18, 'wind_gust': 1.39, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641916800, 'temp': 14.9, 'feels_like': 14.61, 'pressure': 1018, 'humidity': 83, 'dew_point': 12.04, 'uvi': 11.73, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 335, 'wind_gust': 1.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641920400, 'temp': 16.9, 'feels_like': 16.84, 'pressure': 1018, 'humidity': 84, 'dew_point': 14.18, 'uvi': 12.76, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 327, 'wind_gust': 1.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.34}}, {'dt': 1641924000, 'temp': 17.9, 'feels_like': 17.97, 'pressure': 1016, 'humidity': 85, 'dew_point': 15.34, 'uvi': 11.59, 'clouds': 92, 'visibility': 7478, 'wind_speed': 0.58, 'wind_deg': 319, 'wind_gust': 1.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}, {'dt': 1641927600, 'temp': 18.9, 'feels_like': 19.14, 'pressure': 1015, 'humidity': 88, 'dew_point': 16.87, 'uvi': 8.33, 'clouds': 99, 'visibility': 8641, 'wind_speed': 0.64, 'wind_deg': 317, 'wind_gust': 1.97, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1641931200, 'temp': 17.9, 'feels_like': 18.1, 'pressure': 1015, 'humidity': 90, 'dew_point': 16.24, 'uvi': 4.85, 'clouds': 97, 'visibility': 5205, 'wind_speed': 0.51, 'wind_deg': 313, 'wind_gust': 1.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1641934800, 'temp': 16.9, 'feels_like': 17.05, 'pressure': 1015, 'humidity': 92, 'dew_point': 15.59, 'uvi': 1.96, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.15, 'wind_deg': 323, 'wind_gust': 1.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1641938400, 'temp': 16.9, 'feels_like': 17.05, 'pressure': 1016, 'humidity': 92, 'dew_point': 15.59, 'uvi': 0.46, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 334, 'wind_gust': 1.26, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641942000, 'temp': 14.9, 'feels_like': 14.98, 'pressure': 1017, 'humidity': 97, 'dew_point': 14.43, 'uvi': 0, 'clouds': 93, 'visibility': 3875, 'wind_speed': 0.42, 'wind_deg': 315, 'wind_gust': 1.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 00:00:00 | 79.000000 | 13.110000 | 13.830000 | 95.000000 | 1017.000000 |  | 13.900000 | 0.000000 | 10000.000000 | 18.000000 | 0.84 | 0.370000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 01:00:00 | 86.000000 | 12.950000 | 13.800000 | 94.000000 | 1018.000000 |  | 13.900000 | 0.000000 | 10000.000000 | 16.000000 | 0.8 | 0.210000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 02:00:00 | 83.000000 | 11.960000 | 12.700000 | 94.000000 | 1019.000000 |  | 12.900000 | 0.000000 | 10000.000000 | 49.000000 | 0.84 | 0.280000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 03:00:00 | 73.000000 | 11.800000 | 12.670000 | 93.000000 | 1020.000000 |  | 12.900000 | 0.000000 | 10000.000000 | 220.000000 | 0.96 | 0.130000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 04:00:00 | 73.000000 | 11.630000 | 12.650000 | 92.000000 | 1019.000000 |  | 12.900000 | 0.000000 | 10000.000000 | 296.000000 | 0.9 | 0.380000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 05:00:00 | 75.000000 | 11.800000 | 12.670000 | 93.000000 | 1019.000000 | 0.16 | 12.900000 | 0.000000 | 10000.000000 | 320.000000 | 1.03 | 0.320000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 06:00:00 | 80.000000 | 11.960000 | 12.700000 | 94.000000 | 1018.000000 | 0.17 | 12.900000 | 0.000000 | 10000.000000 | 298.000000 | 1.06 | 0.720000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 07:00:00 | 89.000000 | 11.960000 | 12.700000 | 94.000000 | 1017.000000 |  | 12.900000 | 0.000000 | 10000.000000 | 299.000000 | 1.28 | 0.820000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 08:00:00 | 94.000000 | 10.970000 | 11.600000 | 94.000000 | 1016.000000 |  | 11.900000 | 0.000000 | 10000.000000 | 312.000000 | 1.05 | 0.620000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 09:00:00 | 96.000000 | 11.280000 | 11.650000 | 96.000000 | 1017.000000 |  | 11.900000 | 0.000000 | 10000.000000 | 307.000000 | 1.24 | 0.860000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 10:00:00 | 96.000000 | 10.290000 | 10.550000 | 96.000000 | 1017.000000 |  | 10.900000 | 0.000000 | 10000.000000 | 314.000000 | 0.93 | 0.490000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 11:00:00 | 96.000000 | 10.290000 | 10.550000 | 96.000000 | 1018.000000 |  | 10.900000 | 0.000000 | 10000.000000 | 303.000000 | 0.91 | 0.370000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 12:00:00 | 78.000000 | 10.130000 | 10.530000 | 95.000000 | 1018.000000 |  | 10.900000 | 0.410000 | 10000.000000 | 312.000000 | 1.09 | 0.660000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 13:00:00 | 88.000000 | 11.630000 | 12.650000 | 92.000000 | 1019.000000 |  | 12.900000 | 1.880000 | 10000.000000 | 346.000000 | 1.45 | 0.510000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 14:00:00 | 93.000000 | 12.120000 | 13.670000 | 89.000000 | 1020.000000 | 0.12 | 13.900000 | 4.490000 | 8875.000000 | 13.000000 | 1.36 | 0.530000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 15:00:00 | 95.000000 | 11.240000 | 13.540000 | 84.000000 | 1019.000000 | 0.13 | 13.900000 | 7.580000 | 10000.000000 | 18.000000 | 1.39 | 0.540000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 16:00:00 | 96.000000 | 12.040000 | 14.610000 | 83.000000 | 1018.000000 | 0.18 | 14.900000 | 11.730000 | 10000.000000 | 335.000000 | 1.59 | 0.410000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 17:00:00 | 95.000000 | 14.180000 | 16.840000 | 84.000000 | 1018.000000 | 0.34 | 16.900000 | 12.760000 | 10000.000000 | 327.000000 | 1.77 | 0.530000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 18:00:00 | 92.000000 | 15.340000 | 17.970000 | 85.000000 | 1016.000000 | 0.44 | 17.900000 | 11.590000 | 7478.000000 | 319.000000 | 1.79 | 0.580000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 19:00:00 | 99.000000 | 16.870000 | 19.140000 | 88.000000 | 1015.000000 | 0.36 | 18.900000 | 8.330000 | 8641.000000 | 317.000000 | 1.97 | 0.640000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 20:00:00 | 97.000000 | 16.240000 | 18.100000 | 90.000000 | 1015.000000 | 0.38 | 17.900000 | 4.850000 | 5205.000000 | 313.000000 | 1.74 | 0.510000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 21:00:00 | 98.000000 | 15.590000 | 17.050000 | 92.000000 | 1015.000000 | 0.2 | 16.900000 | 1.960000 | 10000.000000 | 323.000000 | 1.53 | 0.150000 | 500 | Rain | light rain | 10d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 22:00:00 | 96.000000 | 15.590000 | 17.050000 | 92.000000 | 1016.000000 |  | 16.900000 | 0.460000 | 10000.000000 | 334.000000 | 1.26 | 0.200000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-11 23:00:00 | 93.000000 | 14.430000 | 14.980000 | 97.000000 | 1017.000000 |  | 14.900000 | 0.000000 | 3875.000000 | 315.000000 | 1.25 | 0.420000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35020310_OWM_Clouds_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Clouds_20220112.png)
![CNE_IDEAM_Station35020310_OWM_Dewpoint_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Dewpoint_20220112.png)
![CNE_IDEAM_Station35020310_OWM_Feelslike_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Feelslike_20220112.png)
![CNE_IDEAM_Station35020310_OWM_Humidity_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Humidity_20220112.png)
![CNE_IDEAM_Station35020310_OWM_Pressure_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Pressure_20220112.png)
![CNE_IDEAM_Station35020310_OWM_Rain_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Rain_20220112.png)
![CNE_IDEAM_Station35020310_OWM_Temp_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Temp_20220112.png)
![CNE_IDEAM_Station35020310_OWM_UVI_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_UVI_20220112.png)
![CNE_IDEAM_Station35020310_OWM_Visibility_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Visibility_20220112.png)
![CNE_IDEAM_Station35020310_OWM_Windgust_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Windgust_20220112.png)
![CNE_IDEAM_Station35020310_OWM_Windspeed_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Windspeed_20220112.png)

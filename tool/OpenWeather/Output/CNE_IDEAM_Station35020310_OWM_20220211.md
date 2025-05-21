
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - NAZARETH [35020310] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35020310_OWM_20220211.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220211.csv)

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

### (CNE index 1854) Open Weather values for station 35020310 - NAZARETH [35020310]

JSON data from API OWM:

```
{'lat': 4.1723, 'lon': -74.146, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644427498, 'sunrise': 1644405107, 'sunset': 1644448196, 'temp': 18.9, 'feels_like': 19.04, 'pressure': 1016, 'humidity': 84, 'dew_point': 16.14, 'uvi': 12.94, 'clouds': 100, 'visibility': 7302, 'wind_speed': 0.92, 'wind_deg': 107, 'wind_gust': 1.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644364800, 'temp': 11.9, 'feels_like': 11.63, 'pressure': 1017, 'humidity': 95, 'dew_point': 11.13, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.22, 'wind_deg': 185, 'wind_gust': 1.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644368400, 'temp': 10.9, 'feels_like': 10.5, 'pressure': 1018, 'humidity': 94, 'dew_point': 9.97, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 171, 'wind_gust': 1.15, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644372000, 'temp': 10.9, 'feels_like': 10.47, 'pressure': 1019, 'humidity': 93, 'dew_point': 9.81, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 141, 'wind_gust': 1.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644375600, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1020, 'humidity': 92, 'dew_point': 7.67, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 135, 'wind_gust': 1.47, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644379200, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1020, 'humidity': 91, 'dew_point': 7.51, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 135, 'wind_gust': 1.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644382800, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1019, 'humidity': 91, 'dew_point': 7.51, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 144, 'wind_gust': 1.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644386400, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1018, 'humidity': 91, 'dew_point': 6.52, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 144, 'wind_gust': 1.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644390000, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1017, 'humidity': 92, 'dew_point': 6.68, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 146, 'wind_gust': 1.09, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644393600, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1017, 'humidity': 92, 'dew_point': 7.67, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 146, 'wind_gust': 1.14, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644397200, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1017, 'humidity': 92, 'dew_point': 7.67, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 135, 'wind_gust': 1.16, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644400800, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1017, 'humidity': 92, 'dew_point': 7.67, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 120, 'wind_gust': 1.31, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644404400, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1017, 'humidity': 91, 'dew_point': 8.5, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 119, 'wind_gust': 1.28, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644408000, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1018, 'humidity': 89, 'dew_point': 8.17, 'uvi': 0.15, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 92, 'wind_gust': 1.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644411600, 'temp': 12.9, 'feels_like': 12.41, 'pressure': 1018, 'humidity': 83, 'dew_point': 10.09, 'uvi': 2.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 88, 'wind_gust': 1.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644415200, 'temp': 14.9, 'feels_like': 14.56, 'pressure': 1018, 'humidity': 81, 'dew_point': 11.67, 'uvi': 5.32, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 88, 'wind_gust': 1.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644418800, 'temp': 16.9, 'feels_like': 16.73, 'pressure': 1018, 'humidity': 80, 'dew_point': 13.43, 'uvi': 8.92, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 87, 'wind_gust': 1.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644422400, 'temp': 17.9, 'feels_like': 17.91, 'pressure': 1018, 'humidity': 83, 'dew_point': 14.97, 'uvi': 11.89, 'clouds': 100, 'visibility': 9123, 'wind_speed': 0.86, 'wind_deg': 96, 'wind_gust': 1.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644426000, 'temp': 18.9, 'feels_like': 19.04, 'pressure': 1016, 'humidity': 84, 'dew_point': 16.14, 'uvi': 12.94, 'clouds': 100, 'visibility': 7302, 'wind_speed': 0.92, 'wind_deg': 107, 'wind_gust': 1.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644429600, 'temp': 18.9, 'feels_like': 19.17, 'pressure': 1016, 'humidity': 89, 'dew_point': 17.05, 'uvi': 11.76, 'clouds': 91, 'visibility': 5882, 'wind_speed': 0.69, 'wind_deg': 125, 'wind_gust': 1.94, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644433200, 'temp': 15.9, 'feels_like': 15.9, 'pressure': 1015, 'humidity': 90, 'dew_point': 14.26, 'uvi': 8.13, 'clouds': 99, 'visibility': 6002, 'wind_speed': 0.68, 'wind_deg': 118, 'wind_gust': 1.66, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.54}}, {'dt': 1644436800, 'temp': 15.9, 'feels_like': 15.95, 'pressure': 1014, 'humidity': 92, 'dew_point': 14.6, 'uvi': 4.75, 'clouds': 99, 'visibility': 4634, 'wind_speed': 0.74, 'wind_deg': 110, 'wind_gust': 1.57, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 3.16}}, {'dt': 1644440400, 'temp': 12.9, 'feels_like': 12.67, 'pressure': 1014, 'humidity': 93, 'dew_point': 11.8, 'uvi': 1.96, 'clouds': 100, 'visibility': 3320, 'wind_speed': 0.71, 'wind_deg': 95, 'wind_gust': 1.44, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.05}}, {'dt': 1644444000, 'temp': 12.9, 'feels_like': 12.67, 'pressure': 1014, 'humidity': 93, 'dew_point': 11.8, 'uvi': 0.4, 'clouds': 98, 'visibility': 3306, 'wind_speed': 0.63, 'wind_deg': 80, 'wind_gust': 1.27, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644447600, 'temp': 12.9, 'feels_like': 12.8, 'pressure': 1015, 'humidity': 98, 'dew_point': 12.59, 'uvi': 0, 'clouds': 98, 'visibility': 1108, 'wind_speed': 0.7, 'wind_deg': 82, 'wind_gust': 1.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 00:00:00 | 100.000000 | 11.130000 | 11.630000 | 95.000000 | 1017.000000 |  | 11.900000 | 0.000000 | 10000.000000 | 185.000000 | 1.11 | 0.220000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 01:00:00 | 100.000000 | 9.970000 | 10.500000 | 94.000000 | 1018.000000 |  | 10.900000 | 0.000000 | 10000.000000 | 171.000000 | 1.15 | 0.360000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 02:00:00 | 100.000000 | 9.810000 | 10.470000 | 93.000000 | 1019.000000 |  | 10.900000 | 0.000000 | 10000.000000 | 141.000000 | 1.39 | 0.440000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 03:00:00 | 98.000000 | 7.670000 | 8.900000 | 92.000000 | 1020.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 135.000000 | 1.47 | 0.530000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 04:00:00 | 94.000000 | 7.510000 | 8.900000 | 91.000000 | 1020.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 135.000000 | 1.49 | 0.630000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 05:00:00 | 94.000000 | 7.510000 | 8.900000 | 91.000000 | 1019.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 144.000000 | 1.44 | 0.510000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 06:00:00 | 74.000000 | 6.520000 | 7.900000 | 91.000000 | 1018.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 144.000000 | 1.07 | 0.420000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 07:00:00 | 84.000000 | 6.680000 | 7.900000 | 92.000000 | 1017.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 146.000000 | 1.09 | 0.450000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 08:00:00 | 82.000000 | 7.670000 | 8.900000 | 92.000000 | 1017.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 146.000000 | 1.14 | 0.340000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 09:00:00 | 83.000000 | 7.670000 | 8.900000 | 92.000000 | 1017.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 135.000000 | 1.16 | 0.410000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 10:00:00 | 82.000000 | 7.670000 | 8.900000 | 92.000000 | 1017.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 120.000000 | 1.31 | 0.340000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 11:00:00 | 82.000000 | 8.500000 | 9.900000 | 91.000000 | 1017.000000 |  | 9.900000 | 0.000000 | 10000.000000 | 119.000000 | 1.28 | 0.440000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 12:00:00 | 100.000000 | 8.170000 | 9.900000 | 89.000000 | 1018.000000 |  | 9.900000 | 0.150000 | 10000.000000 | 92.000000 | 1.33 | 0.420000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 13:00:00 | 100.000000 | 10.090000 | 12.410000 | 83.000000 | 1018.000000 |  | 12.900000 | 2.260000 | 10000.000000 | 88.000000 | 1.7 | 0.910000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 14:00:00 | 100.000000 | 11.670000 | 14.560000 | 81.000000 | 1018.000000 |  | 14.900000 | 5.320000 | 10000.000000 | 88.000000 | 1.77 | 0.780000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 15:00:00 | 100.000000 | 13.430000 | 16.730000 | 80.000000 | 1018.000000 |  | 16.900000 | 8.920000 | 10000.000000 | 87.000000 | 1.78 | 0.680000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 16:00:00 | 100.000000 | 14.970000 | 17.910000 | 83.000000 | 1018.000000 |  | 17.900000 | 11.890000 | 9123.000000 | 96.000000 | 1.81 | 0.860000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 17:00:00 | 100.000000 | 16.140000 | 19.040000 | 84.000000 | 1016.000000 |  | 18.900000 | 12.940000 | 7302.000000 | 107.000000 | 1.81 | 0.920000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 18:00:00 | 91.000000 | 17.050000 | 19.170000 | 89.000000 | 1016.000000 |  | 18.900000 | 11.760000 | 5882.000000 | 125.000000 | 1.94 | 0.690000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 19:00:00 | 99.000000 | 14.260000 | 15.900000 | 90.000000 | 1015.000000 | 1.54 | 15.900000 | 8.130000 | 6002.000000 | 118.000000 | 1.66 | 0.680000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 20:00:00 | 99.000000 | 14.600000 | 15.950000 | 92.000000 | 1014.000000 | 3.16 | 15.900000 | 4.750000 | 4634.000000 | 110.000000 | 1.57 | 0.740000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 21:00:00 | 100.000000 | 11.800000 | 12.670000 | 93.000000 | 1014.000000 | 2.05 | 12.900000 | 1.960000 | 3320.000000 | 95.000000 | 1.44 | 0.710000 | 501 | Rain | moderate rain | 10d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 22:00:00 | 98.000000 | 11.800000 | 12.670000 | 93.000000 | 1014.000000 |  | 12.900000 | 0.400000 | 3306.000000 | 80.000000 | 1.27 | 0.630000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 23:00:00 | 98.000000 | 12.590000 | 12.800000 | 98.000000 | 1015.000000 |  | 12.900000 | 0.000000 | 1108.000000 | 82.000000 | 1.24 | 0.700000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35020310_OWM_Clouds_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Clouds_20220211.png)
![CNE_IDEAM_Station35020310_OWM_Dewpoint_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Dewpoint_20220211.png)
![CNE_IDEAM_Station35020310_OWM_Feelslike_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Feelslike_20220211.png)
![CNE_IDEAM_Station35020310_OWM_Humidity_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Humidity_20220211.png)
![CNE_IDEAM_Station35020310_OWM_Pressure_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Pressure_20220211.png)
![CNE_IDEAM_Station35020310_OWM_Rain_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Rain_20220211.png)
![CNE_IDEAM_Station35020310_OWM_Temp_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Temp_20220211.png)
![CNE_IDEAM_Station35020310_OWM_UVI_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_UVI_20220211.png)
![CNE_IDEAM_Station35020310_OWM_Visibility_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Visibility_20220211.png)
![CNE_IDEAM_Station35020310_OWM_Winddeg_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Winddeg_20220211.png)
![CNE_IDEAM_Station35020310_OWM_Windgust_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Windgust_20220211.png)
![CNE_IDEAM_Station35020310_OWM_Windspeed_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Windspeed_20220211.png)

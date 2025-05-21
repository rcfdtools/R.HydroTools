
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - VILLA TERESA - AUT [21206920] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206920_OWM_20220211.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220211.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.35,-74.15) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.35&lon=-74.15)

| Parameter | Value |
|---|---|
| Code | 21206920 |
| Name | VILLA TERESA - AUT [21206920] |
| Latitude, ° | 4.35 |
| Longitude, ° | -74.15 |
| Elevation, m | 3624 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-07-19 00:00:00 |
| Suspension date | NaT |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Guatiquia |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Bogotá |

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

### (CNE index 86) Open Weather values for station 21206920 - VILLA TERESA - AUT [21206920]

JSON data from API OWM:

```
{'lat': 4.35, 'lon': -74.15, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644427498, 'sunrise': 1644405119, 'sunset': 1644448186, 'temp': 13.9, 'feels_like': 13.41, 'pressure': 1015, 'humidity': 79, 'dew_point': 10.32, 'uvi': 12.94, 'clouds': 98, 'visibility': 9941, 'wind_speed': 0.25, 'wind_deg': 181, 'wind_gust': 1.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644364800, 'temp': 6.9, 'feels_like': 6.9, 'pressure': 1017, 'humidity': 96, 'dew_point': 6.31, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 179, 'wind_gust': 0.93, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644368400, 'temp': 5.9, 'feels_like': 5.9, 'pressure': 1018, 'humidity': 93, 'dew_point': 4.86, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 157, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644372000, 'temp': 5.9, 'feels_like': 5.9, 'pressure': 1019, 'humidity': 92, 'dew_point': 4.7, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 137, 'wind_gust': 1.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644375600, 'temp': 3.9, 'feels_like': 3.9, 'pressure': 1019, 'humidity': 90, 'dew_point': 2.41, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 118, 'wind_gust': 1.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644379200, 'temp': 3.9, 'feels_like': 3.9, 'pressure': 1019, 'humidity': 89, 'dew_point': 2.26, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 123, 'wind_gust': 1.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644382800, 'temp': 3.9, 'feels_like': 3.9, 'pressure': 1019, 'humidity': 89, 'dew_point': 2.26, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 127, 'wind_gust': 1.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644386400, 'temp': 2.9, 'feels_like': 2.9, 'pressure': 1018, 'humidity': 89, 'dew_point': 1.27, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 128, 'wind_gust': 1.05, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644390000, 'temp': 2.9, 'feels_like': 2.9, 'pressure': 1017, 'humidity': 89, 'dew_point': 1.27, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 130, 'wind_gust': 1.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644393600, 'temp': 3.9, 'feels_like': 3.9, 'pressure': 1016, 'humidity': 90, 'dew_point': 2.41, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 120, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644397200, 'temp': 3.9, 'feels_like': 3.9, 'pressure': 1016, 'humidity': 89, 'dew_point': 2.26, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 119, 'wind_gust': 1.26, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644400800, 'temp': 3.9, 'feels_like': 3.9, 'pressure': 1017, 'humidity': 89, 'dew_point': 2.26, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 116, 'wind_gust': 1.47, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644404400, 'temp': 4.9, 'feels_like': 4.9, 'pressure': 1017, 'humidity': 89, 'dew_point': 3.24, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 123, 'wind_gust': 1.42, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644408000, 'temp': 4.9, 'feels_like': 4.9, 'pressure': 1017, 'humidity': 86, 'dew_point': 2.76, 'uvi': 0.15, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 114, 'wind_gust': 1.26, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644411600, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1017, 'humidity': 79, 'dew_point': 4.49, 'uvi': 2.26, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 79, 'wind_gust': 1.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644415200, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1018, 'humidity': 75, 'dew_point': 5.68, 'uvi': 5.32, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 76, 'wind_gust': 1.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644418800, 'temp': 11.9, 'feels_like': 11.05, 'pressure': 1017, 'humidity': 73, 'dew_point': 7.22, 'uvi': 8.92, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 19, 'wind_gust': 1.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644422400, 'temp': 12.9, 'feels_like': 12.2, 'pressure': 1016, 'humidity': 75, 'dew_point': 8.58, 'uvi': 11.89, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.05, 'wind_deg': 127, 'wind_gust': 1.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644426000, 'temp': 13.9, 'feels_like': 13.41, 'pressure': 1015, 'humidity': 79, 'dew_point': 10.32, 'uvi': 12.94, 'clouds': 98, 'visibility': 9941, 'wind_speed': 0.25, 'wind_deg': 181, 'wind_gust': 1.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644429600, 'temp': 13.9, 'feels_like': 13.57, 'pressure': 1015, 'humidity': 85, 'dew_point': 11.42, 'uvi': 11.76, 'clouds': 84, 'visibility': 7809, 'wind_speed': 0.22, 'wind_deg': 211, 'wind_gust': 1.93, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644433200, 'temp': 10.9, 'feels_like': 10.29, 'pressure': 1014, 'humidity': 86, 'dew_point': 8.65, 'uvi': 8.13, 'clouds': 94, 'visibility': 7379, 'wind_speed': 0.19, 'wind_deg': 165, 'wind_gust': 1.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1644436800, 'temp': 10.9, 'feels_like': 10.37, 'pressure': 1013, 'humidity': 89, 'dew_point': 9.16, 'uvi': 4.75, 'clouds': 96, 'visibility': 6632, 'wind_speed': 0.31, 'wind_deg': 138, 'wind_gust': 1.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1644440400, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1013, 'humidity': 92, 'dew_point': 6.68, 'uvi': 1.96, 'clouds': 98, 'visibility': 5511, 'wind_speed': 0.38, 'wind_deg': 108, 'wind_gust': 1.49, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.33}}, {'dt': 1644444000, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1013, 'humidity': 92, 'dew_point': 6.68, 'uvi': 0.4, 'clouds': 97, 'visibility': 6309, 'wind_speed': 0.35, 'wind_deg': 77, 'wind_gust': 1.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644447600, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1014, 'humidity': 97, 'dew_point': 7.45, 'uvi': 0, 'clouds': 97, 'visibility': 4571, 'wind_speed': 0.62, 'wind_deg': 87, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 00:00:00 | 100.000000 | 6.310000 | 6.900000 | 96.000000 | 1017.000000 |  | 6.900000 | 0.000000 | 10000.000000 | 179.000000 | 0.93 | 0.240000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 01:00:00 | 100.000000 | 4.860000 | 5.900000 | 93.000000 | 1018.000000 |  | 5.900000 | 0.000000 | 10000.000000 | 157.000000 | 0.95 | 0.380000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 02:00:00 | 100.000000 | 4.700000 | 5.900000 | 92.000000 | 1019.000000 |  | 5.900000 | 0.000000 | 10000.000000 | 137.000000 | 1.17 | 0.510000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 03:00:00 | 98.000000 | 2.410000 | 3.900000 | 90.000000 | 1019.000000 |  | 3.900000 | 0.000000 | 10000.000000 | 118.000000 | 1.46 | 0.730000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 04:00:00 | 92.000000 | 2.260000 | 3.900000 | 89.000000 | 1019.000000 |  | 3.900000 | 0.000000 | 10000.000000 | 123.000000 | 1.5 | 0.860000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 05:00:00 | 92.000000 | 2.260000 | 3.900000 | 89.000000 | 1019.000000 |  | 3.900000 | 0.000000 | 10000.000000 | 127.000000 | 1.41 | 0.680000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 06:00:00 | 80.000000 | 1.270000 | 2.900000 | 89.000000 | 1018.000000 |  | 2.900000 | 0.000000 | 10000.000000 | 128.000000 | 1.05 | 0.550000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 07:00:00 | 88.000000 | 1.270000 | 2.900000 | 89.000000 | 1017.000000 |  | 2.900000 | 0.000000 | 10000.000000 | 130.000000 | 1.17 | 0.660000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 08:00:00 | 85.000000 | 2.410000 | 3.900000 | 90.000000 | 1016.000000 |  | 3.900000 | 0.000000 | 10000.000000 | 120.000000 | 1.18 | 0.650000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 09:00:00 | 84.000000 | 2.260000 | 3.900000 | 89.000000 | 1016.000000 |  | 3.900000 | 0.000000 | 10000.000000 | 119.000000 | 1.26 | 0.800000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 10:00:00 | 81.000000 | 2.260000 | 3.900000 | 89.000000 | 1017.000000 |  | 3.900000 | 0.000000 | 10000.000000 | 116.000000 | 1.47 | 0.780000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 11:00:00 | 79.000000 | 3.240000 | 4.900000 | 89.000000 | 1017.000000 |  | 4.900000 | 0.000000 | 10000.000000 | 123.000000 | 1.42 | 0.840000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 12:00:00 | 91.000000 | 2.760000 | 4.900000 | 86.000000 | 1017.000000 |  | 4.900000 | 0.150000 | 10000.000000 | 114.000000 | 1.26 | 0.570000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 13:00:00 | 95.000000 | 4.490000 | 7.900000 | 79.000000 | 1017.000000 |  | 7.900000 | 2.260000 | 10000.000000 | 79.000000 | 1.57 | 0.530000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 14:00:00 | 97.000000 | 5.680000 | 9.900000 | 75.000000 | 1018.000000 |  | 9.900000 | 5.320000 | 10000.000000 | 76.000000 | 1.75 | 0.310000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 15:00:00 | 98.000000 | 7.220000 | 11.050000 | 73.000000 | 1017.000000 |  | 11.900000 | 8.920000 | 10000.000000 | 19.000000 | 1.95 | 0.190000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 16:00:00 | 98.000000 | 8.580000 | 12.200000 | 75.000000 | 1016.000000 |  | 12.900000 | 11.890000 | 10000.000000 | 127.000000 | 1.92 | 0.050000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 17:00:00 | 98.000000 | 10.320000 | 13.410000 | 79.000000 | 1015.000000 |  | 13.900000 | 12.940000 | 9941.000000 | 181.000000 | 1.95 | 0.250000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 18:00:00 | 84.000000 | 11.420000 | 13.570000 | 85.000000 | 1015.000000 |  | 13.900000 | 11.760000 | 7809.000000 | 211.000000 | 1.93 | 0.220000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 19:00:00 | 94.000000 | 8.650000 | 10.290000 | 86.000000 | 1014.000000 | 0.13 | 10.900000 | 8.130000 | 7379.000000 | 165.000000 | 1.69 | 0.190000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 20:00:00 | 96.000000 | 9.160000 | 10.370000 | 89.000000 | 1013.000000 | 0.36 | 10.900000 | 4.750000 | 6632.000000 | 138.000000 | 1.61 | 0.310000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 21:00:00 | 98.000000 | 6.680000 | 7.900000 | 92.000000 | 1013.000000 | 1.33 | 7.900000 | 1.960000 | 5511.000000 | 108.000000 | 1.49 | 0.380000 | 501 | Rain | moderate rain | 10d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 22:00:00 | 97.000000 | 6.680000 | 7.900000 | 92.000000 | 1013.000000 |  | 7.900000 | 0.400000 | 6309.000000 | 77.000000 | 1.36 | 0.350000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 23:00:00 | 97.000000 | 7.450000 | 7.900000 | 97.000000 | 1014.000000 |  | 7.900000 | 0.000000 | 4571.000000 | 87.000000 | 1.18 | 0.620000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21206920_OWM_Clouds_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Clouds_20220211.png)
![CNE_IDEAM_Station21206920_OWM_Dewpoint_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Dewpoint_20220211.png)
![CNE_IDEAM_Station21206920_OWM_Feelslike_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Feelslike_20220211.png)
![CNE_IDEAM_Station21206920_OWM_Humidity_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Humidity_20220211.png)
![CNE_IDEAM_Station21206920_OWM_Pressure_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Pressure_20220211.png)
![CNE_IDEAM_Station21206920_OWM_Rain_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Rain_20220211.png)
![CNE_IDEAM_Station21206920_OWM_Temp_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Temp_20220211.png)
![CNE_IDEAM_Station21206920_OWM_UVI_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_UVI_20220211.png)
![CNE_IDEAM_Station21206920_OWM_Visibility_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Visibility_20220211.png)
![CNE_IDEAM_Station21206920_OWM_Winddeg_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Winddeg_20220211.png)
![CNE_IDEAM_Station21206920_OWM_Windgust_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Windgust_20220211.png)
![CNE_IDEAM_Station21206920_OWM_Windspeed_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Windspeed_20220211.png)

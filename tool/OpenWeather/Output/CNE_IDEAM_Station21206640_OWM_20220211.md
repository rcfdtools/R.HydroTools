
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SAN JOSE [21206640] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206640_OWM_20220211.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220211.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.50155556,-74.11930556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.50155556&lon=-74.11930556)

| Parameter | Value |
|---|---|
| Code | 21206640 |
| Name | SAN JOSE [21206640] |
| Latitude, ° | 4.50155556 |
| Longitude, ° | -74.11930556 |
| Elevation, m | 2700 |
| Category | Climática Ordinaria |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 2001-11-15 00:00:00 |
| Suspension date | 2011-05-10 00:00:00 |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Guaviare |
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

### (CNE index 2376) Open Weather values for station 21206640 - SAN JOSE [21206640]

JSON data from API OWM:

```
{'lat': 4.5016, 'lon': -74.1193, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644427498, 'sunrise': 1644405121, 'sunset': 1644448169, 'temp': 18.03, 'feels_like': 17.77, 'pressure': 1015, 'humidity': 72, 'dew_point': 12.91, 'uvi': 10.55, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 195, 'wind_gust': 2.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644364800, 'temp': 11.03, 'feels_like': 10.67, 'pressure': 1016, 'humidity': 95, 'dew_point': 10.26, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 181, 'wind_gust': 0.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644368400, 'temp': 10.03, 'feels_like': 9.54, 'pressure': 1017, 'humidity': 94, 'dew_point': 9.11, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 143, 'wind_gust': 0.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644372000, 'temp': 10.03, 'feels_like': 9.52, 'pressure': 1018, 'humidity': 93, 'dew_point': 8.95, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 144, 'wind_gust': 0.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644375600, 'temp': 8.03, 'feels_like': 8.03, 'pressure': 1019, 'humidity': 91, 'dew_point': 6.65, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 100, 'wind_gust': 1.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644379200, 'temp': 8.03, 'feels_like': 8.03, 'pressure': 1019, 'humidity': 90, 'dew_point': 6.49, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 120, 'wind_gust': 1.35, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644382800, 'temp': 8.03, 'feels_like': 8.03, 'pressure': 1018, 'humidity': 90, 'dew_point': 6.49, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 125, 'wind_gust': 1.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644386400, 'temp': 7.03, 'feels_like': 7.03, 'pressure': 1017, 'humidity': 88, 'dew_point': 5.18, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 117, 'wind_gust': 1.08, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644390000, 'temp': 7.03, 'feels_like': 7.03, 'pressure': 1016, 'humidity': 88, 'dew_point': 5.18, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 124, 'wind_gust': 1.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644393600, 'temp': 8.03, 'feels_like': 8.03, 'pressure': 1016, 'humidity': 88, 'dew_point': 6.17, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 112, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644397200, 'temp': 8.03, 'feels_like': 8.03, 'pressure': 1016, 'humidity': 88, 'dew_point': 6.17, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 117, 'wind_gust': 1.27, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644400800, 'temp': 8.03, 'feels_like': 8.03, 'pressure': 1016, 'humidity': 88, 'dew_point': 6.17, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 123, 'wind_gust': 1.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644404400, 'temp': 9.03, 'feels_like': 9.03, 'pressure': 1017, 'humidity': 88, 'dew_point': 7.15, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 130, 'wind_gust': 1.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644408000, 'temp': 9.03, 'feels_like': 9.03, 'pressure': 1017, 'humidity': 83, 'dew_point': 6.3, 'uvi': 0.11, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 126, 'wind_gust': 1.2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644411600, 'temp': 12.03, 'feels_like': 11.25, 'pressure': 1017, 'humidity': 75, 'dew_point': 7.74, 'uvi': 2.36, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 113, 'wind_gust': 1.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644415200, 'temp': 14.03, 'feels_like': 13.26, 'pressure': 1017, 'humidity': 68, 'dew_point': 8.22, 'uvi': 5.59, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 150, 'wind_gust': 1.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644418800, 'temp': 16.03, 'feels_like': 15.36, 'pressure': 1016, 'humidity': 64, 'dew_point': 9.23, 'uvi': 9.38, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.29, 'wind_deg': 192, 'wind_gust': 2.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644422400, 'temp': 17.03, 'feels_like': 16.49, 'pressure': 1015, 'humidity': 65, 'dew_point': 10.41, 'uvi': 9.69, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 201, 'wind_gust': 2.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644426000, 'temp': 18.03, 'feels_like': 17.77, 'pressure': 1015, 'humidity': 72, 'dew_point': 12.91, 'uvi': 10.55, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 195, 'wind_gust': 2.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644429600, 'temp': 18.03, 'feels_like': 17.98, 'pressure': 1014, 'humidity': 80, 'dew_point': 14.53, 'uvi': 9.58, 'clouds': 78, 'visibility': 8409, 'wind_speed': 0.4, 'wind_deg': 179, 'wind_gust': 2.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644433200, 'temp': 15.03, 'feels_like': 14.7, 'pressure': 1013, 'humidity': 81, 'dew_point': 11.8, 'uvi': 6.76, 'clouds': 90, 'visibility': 6898, 'wind_speed': 0.5, 'wind_deg': 151, 'wind_gust': 1.9, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.78}}, {'dt': 1644436800, 'temp': 15.03, 'feels_like': 14.81, 'pressure': 1012, 'humidity': 85, 'dew_point': 12.53, 'uvi': 3.95, 'clouds': 93, 'visibility': 8715, 'wind_speed': 0.65, 'wind_deg': 146, 'wind_gust': 2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.75}}, {'dt': 1644440400, 'temp': 12.03, 'feels_like': 11.61, 'pressure': 1012, 'humidity': 89, 'dew_point': 10.27, 'uvi': 1.62, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 131, 'wind_gust': 1.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644444000, 'temp': 12.03, 'feels_like': 11.66, 'pressure': 1013, 'humidity': 91, 'dew_point': 10.61, 'uvi': 0.49, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 126, 'wind_gust': 1.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644447600, 'temp': 12.03, 'feels_like': 11.77, 'pressure': 1014, 'humidity': 95, 'dew_point': 11.25, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 116, 'wind_gust': 1.53, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 00:00:00 | 100.000000 | 10.260000 | 10.670000 | 95.000000 | 1016.000000 |  | 11.030000 | 0.000000 | 10000.000000 | 181.000000 | 0.71 | 0.170000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 01:00:00 | 100.000000 | 9.110000 | 9.540000 | 94.000000 | 1017.000000 |  | 10.030000 | 0.000000 | 10000.000000 | 143.000000 | 0.81 | 0.370000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 02:00:00 | 100.000000 | 8.950000 | 9.520000 | 93.000000 | 1018.000000 |  | 10.030000 | 0.000000 | 10000.000000 | 144.000000 | 0.87 | 0.380000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 03:00:00 | 100.000000 | 6.650000 | 8.030000 | 91.000000 | 1019.000000 |  | 8.030000 | 0.000000 | 10000.000000 | 100.000000 | 1.29 | 0.650000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 04:00:00 | 94.000000 | 6.490000 | 8.030000 | 90.000000 | 1019.000000 |  | 8.030000 | 0.000000 | 10000.000000 | 120.000000 | 1.35 | 0.730000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 05:00:00 | 95.000000 | 6.490000 | 8.030000 | 90.000000 | 1018.000000 |  | 8.030000 | 0.000000 | 10000.000000 | 125.000000 | 1.25 | 0.480000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 06:00:00 | 91.000000 | 5.180000 | 7.030000 | 88.000000 | 1017.000000 |  | 7.030000 | 0.000000 | 10000.000000 | 117.000000 | 1.08 | 0.570000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 07:00:00 | 98.000000 | 5.180000 | 7.030000 | 88.000000 | 1016.000000 |  | 7.030000 | 0.000000 | 10000.000000 | 124.000000 | 1.28 | 0.730000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 08:00:00 | 97.000000 | 6.170000 | 8.030000 | 88.000000 | 1016.000000 |  | 8.030000 | 0.000000 | 10000.000000 | 112.000000 | 1.18 | 0.810000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 09:00:00 | 95.000000 | 6.170000 | 8.030000 | 88.000000 | 1016.000000 |  | 8.030000 | 0.000000 | 10000.000000 | 117.000000 | 1.27 | 0.960000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 10:00:00 | 92.000000 | 6.170000 | 8.030000 | 88.000000 | 1016.000000 |  | 8.030000 | 0.000000 | 10000.000000 | 123.000000 | 1.48 | 0.960000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 11:00:00 | 88.000000 | 7.150000 | 9.030000 | 88.000000 | 1017.000000 |  | 9.030000 | 0.000000 | 10000.000000 | 130.000000 | 1.44 | 0.980000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 12:00:00 | 83.000000 | 6.300000 | 9.030000 | 83.000000 | 1017.000000 |  | 9.030000 | 0.110000 | 10000.000000 | 126.000000 | 1.2 | 0.750000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 13:00:00 | 89.000000 | 7.740000 | 11.250000 | 75.000000 | 1017.000000 |  | 12.030000 | 2.360000 | 10000.000000 | 113.000000 | 1.52 | 0.490000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 14:00:00 | 95.000000 | 8.220000 | 13.260000 | 68.000000 | 1017.000000 |  | 14.030000 | 5.590000 | 10000.000000 | 150.000000 | 1.77 | 0.450000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 15:00:00 | 96.000000 | 9.230000 | 15.360000 | 64.000000 | 1016.000000 |  | 16.030000 | 9.380000 | 10000.000000 | 192.000000 | 2.11 | 0.290000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 16:00:00 | 96.000000 | 10.410000 | 16.490000 | 65.000000 | 1015.000000 |  | 17.030000 | 9.690000 | 10000.000000 | 201.000000 | 2.06 | 0.520000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 17:00:00 | 97.000000 | 12.910000 | 17.770000 | 72.000000 | 1015.000000 |  | 18.030000 | 10.550000 | 10000.000000 | 195.000000 | 2.16 | 0.710000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 18:00:00 | 78.000000 | 14.530000 | 17.980000 | 80.000000 | 1014.000000 |  | 18.030000 | 9.580000 | 8409.000000 | 179.000000 | 2.03 | 0.400000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 19:00:00 | 90.000000 | 11.800000 | 14.700000 | 81.000000 | 1013.000000 | 1.78 | 15.030000 | 6.760000 | 6898.000000 | 151.000000 | 1.9 | 0.500000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 20:00:00 | 93.000000 | 12.530000 | 14.810000 | 85.000000 | 1012.000000 | 0.75 | 15.030000 | 3.950000 | 8715.000000 | 146.000000 | 2 | 0.650000 | 500 | Rain | light rain | 10d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 21:00:00 | 95.000000 | 10.270000 | 11.610000 | 89.000000 | 1012.000000 |  | 12.030000 | 1.620000 | 10000.000000 | 131.000000 | 1.97 | 0.780000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 22:00:00 | 96.000000 | 10.610000 | 11.660000 | 91.000000 | 1013.000000 |  | 12.030000 | 0.490000 | 10000.000000 | 126.000000 | 1.78 | 0.650000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 23:00:00 | 95.000000 | 11.250000 | 11.770000 | 95.000000 | 1014.000000 |  | 12.030000 | 0.000000 | 10000.000000 | 116.000000 | 1.53 | 0.870000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21206640_OWM_Clouds_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Clouds_20220211.png)
![CNE_IDEAM_Station21206640_OWM_Dewpoint_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Dewpoint_20220211.png)
![CNE_IDEAM_Station21206640_OWM_Feelslike_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Feelslike_20220211.png)
![CNE_IDEAM_Station21206640_OWM_Humidity_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Humidity_20220211.png)
![CNE_IDEAM_Station21206640_OWM_Pressure_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Pressure_20220211.png)
![CNE_IDEAM_Station21206640_OWM_Rain_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Rain_20220211.png)
![CNE_IDEAM_Station21206640_OWM_Temp_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Temp_20220211.png)
![CNE_IDEAM_Station21206640_OWM_UVI_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_UVI_20220211.png)
![CNE_IDEAM_Station21206640_OWM_Visibility_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Visibility_20220211.png)
![CNE_IDEAM_Station21206640_OWM_Winddeg_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Winddeg_20220211.png)
![CNE_IDEAM_Station21206640_OWM_Windgust_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Windgust_20220211.png)
![CNE_IDEAM_Station21206640_OWM_Windspeed_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Windspeed_20220211.png)

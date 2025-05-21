
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - EFRAIN CA#AVERAL [21206610] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206610_OWM_20220211.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220211.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.58333333,-74.06666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.58333333&lon=-74.06666667)

| Parameter | Value |
|---|---|
| Code | 21206610 |
| Name | EFRAIN CA#AVERAL [21206610] |
| Latitude, ° | 4.58333333 |
| Longitude, ° | -74.06666667 |
| Elevation, m | 2804 |
| Category | Climática Ordinaria |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 2001-11-15 00:00:00 |
| Suspension date | 2009-08-05 00:00:00 |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Cauca |
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

### (CNE index 2318) Open Weather values for station 21206610 - EFRAIN CA#AVERAL [21206610]

JSON data from API OWM:

```
{'lat': 4.5833, 'lon': -74.0667, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644427498, 'sunrise': 1644405113, 'sunset': 1644448151, 'temp': 16.67, 'feels_like': 15.65, 'pressure': 1026, 'humidity': 48, 'dew_point': 5.62, 'uvi': 10.55, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 150, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, 'hourly': [{'dt': 1644364800, 'temp': 9.67, 'feels_like': 9.23, 'pressure': 1025, 'humidity': 87, 'dew_point': 7.61, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 210, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644368400, 'temp': 8.67, 'feels_like': 7.59, 'pressure': 1026, 'humidity': 100, 'dew_point': 8.67, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 320, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644372000, 'temp': 8.67, 'feels_like': 8.09, 'pressure': 1027, 'humidity': 100, 'dew_point': 8.67, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 330, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644375600, 'temp': 6.67, 'feels_like': 6.67, 'pressure': 1027, 'humidity': 100, 'dew_point': 6.67, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644379200, 'temp': 6.67, 'feels_like': 6.67, 'pressure': 1027, 'humidity': 100, 'dew_point': 6.67, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644382800, 'temp': 6.67, 'feels_like': 6.67, 'pressure': 1027, 'humidity': 100, 'dew_point': 6.67, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644386400, 'temp': 5.67, 'feels_like': 5.67, 'pressure': 1026, 'humidity': 93, 'dew_point': 4.63, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644390000, 'temp': 5.67, 'feels_like': 4.66, 'pressure': 1026, 'humidity': 100, 'dew_point': 5.67, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 360, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1644393600, 'temp': 6.67, 'feels_like': 6.67, 'pressure': 1025, 'humidity': 100, 'dew_point': 6.67, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1644397200, 'temp': 6.67, 'feels_like': 5.8, 'pressure': 1025, 'humidity': 100, 'dew_point': 6.67, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 320, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1644400800, 'temp': 6.67, 'feels_like': 6.67, 'pressure': 1025, 'humidity': 100, 'dew_point': 6.67, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644404400, 'temp': 7.67, 'feels_like': 7.67, 'pressure': 1025, 'humidity': 93, 'dew_point': 6.61, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644408000, 'temp': 7.67, 'feels_like': 7.67, 'pressure': 1026, 'humidity': 100, 'dew_point': 7.67, 'uvi': 0.11, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644411600, 'temp': 10.67, 'feels_like': 10.09, 'pressure': 1027, 'humidity': 88, 'dew_point': 8.77, 'uvi': 2.36, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644415200, 'temp': 12.67, 'feels_like': 11.87, 'pressure': 1027, 'humidity': 72, 'dew_point': 7.76, 'uvi': 5.59, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 60, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1644418800, 'temp': 14.67, 'feels_like': 13.73, 'pressure': 1027, 'humidity': 59, 'dew_point': 6.75, 'uvi': 9.38, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 40, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1644422400, 'temp': 15.67, 'feels_like': 14.55, 'pressure': 1027, 'humidity': 48, 'dew_point': 4.7, 'uvi': 9.69, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 70, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644426000, 'temp': 16.67, 'feels_like': 15.65, 'pressure': 1026, 'humidity': 48, 'dew_point': 5.62, 'uvi': 10.55, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 150, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1644429600, 'temp': 16.67, 'feels_like': 15.65, 'pressure': 1025, 'humidity': 48, 'dew_point': 5.62, 'uvi': 9.58, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 250, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644433200, 'temp': 13.67, 'feels_like': 12.97, 'pressure': 1024, 'humidity': 72, 'dew_point': 8.72, 'uvi': 6.76, 'clouds': 75, 'visibility': 9000, 'wind_speed': 5.14, 'wind_deg': 290, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}, {'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.05}}, {'dt': 1644436800, 'temp': 13.67, 'feels_like': 12.97, 'pressure': 1023, 'humidity': 72, 'dew_point': 8.72, 'uvi': 3.95, 'clouds': 75, 'visibility': 9000, 'wind_speed': 3.09, 'wind_deg': 290, 'weather': [{'id': 211, 'main': 'Thunderstorm', 'description': 'thunderstorm', 'icon': '11d'}, {'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}]}, {'dt': 1644440400, 'temp': 10.67, 'feels_like': 9.93, 'pressure': 1023, 'humidity': 82, 'dew_point': 7.73, 'uvi': 1.62, 'clouds': 75, 'visibility': 7000, 'wind_speed': 3.09, 'wind_deg': 130, 'weather': [{'id': 301, 'main': 'Drizzle', 'description': 'drizzle', 'icon': '09d'}]}, {'dt': 1644444000, 'temp': 10.67, 'feels_like': 10.4, 'pressure': 1023, 'humidity': 100, 'dew_point': 10.67, 'uvi': 0.49, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 30, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644447600, 'temp': 10.67, 'feels_like': 10.25, 'pressure': 1024, 'humidity': 94, 'dew_point': 9.75, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 350, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 00:00:00 | 100.000000 | 7.610000 | 9.230000 | 87.000000 | 1025.000000 |  | 9.670000 | 0.000000 | 10000.000000 | 210.000000 |  | 1.540000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 01:00:00 | 100.000000 | 8.670000 | 7.590000 | 100.000000 | 1026.000000 |  | 8.670000 | 0.000000 | 10000.000000 | 320.000000 |  | 2.060000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 02:00:00 | 100.000000 | 8.670000 | 8.090000 | 100.000000 | 1027.000000 |  | 8.670000 | 0.000000 | 10000.000000 | 330.000000 |  | 1.540000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 03:00:00 | 98.000000 | 6.670000 | 6.670000 | 100.000000 | 1027.000000 |  | 6.670000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 04:00:00 | 95.000000 | 6.670000 | 6.670000 | 100.000000 | 1027.000000 |  | 6.670000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 05:00:00 | 96.000000 | 6.670000 | 6.670000 | 100.000000 | 1027.000000 |  | 6.670000 | 0.000000 | 10000.000000 | 0.000000 |  | 0.000000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 06:00:00 | 94.000000 | 4.630000 | 5.670000 | 93.000000 | 1026.000000 |  | 5.670000 | 0.000000 | 10000.000000 | 0.000000 |  | 0.000000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 07:00:00 | 99.000000 | 5.670000 | 4.660000 | 100.000000 | 1026.000000 |  | 5.670000 | 0.000000 | 10000.000000 | 360.000000 |  | 1.540000 | 741 | Fog | fog | 50n | 07 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 08:00:00 | 99.000000 | 6.670000 | 6.670000 | 100.000000 | 1025.000000 |  | 6.670000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 741 | Fog | fog | 50n | 08 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 09:00:00 | 97.000000 | 6.670000 | 5.800000 | 100.000000 | 1025.000000 |  | 6.670000 | 0.000000 | 10000.000000 | 320.000000 |  | 1.540000 | 741 | Fog | fog | 50n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 10:00:00 | 75.000000 | 6.670000 | 6.670000 | 100.000000 | 1025.000000 |  | 6.670000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 11:00:00 | 75.000000 | 6.610000 | 7.670000 | 93.000000 | 1025.000000 |  | 7.670000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 12:00:00 | 75.000000 | 7.670000 | 7.670000 | 100.000000 | 1026.000000 |  | 7.670000 | 0.110000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 13:00:00 | 75.000000 | 8.770000 | 10.090000 | 88.000000 | 1027.000000 |  | 10.670000 | 2.360000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 14:00:00 | 40.000000 | 7.760000 | 11.870000 | 72.000000 | 1027.000000 |  | 12.670000 | 5.590000 | 10000.000000 | 60.000000 |  | 3.090000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 15:00:00 | 40.000000 | 6.750000 | 13.730000 | 59.000000 | 1027.000000 |  | 14.670000 | 9.380000 | 10000.000000 | 40.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 16:00:00 | 75.000000 | 4.700000 | 14.550000 | 48.000000 | 1027.000000 |  | 15.670000 | 9.690000 | 10000.000000 | 70.000000 |  | 4.120000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 17:00:00 | 40.000000 | 5.620000 | 15.650000 | 48.000000 | 1026.000000 |  | 16.670000 | 10.550000 | 10000.000000 | 150.000000 |  | 4.630000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 18:00:00 | 75.000000 | 5.620000 | 15.650000 | 48.000000 | 1025.000000 |  | 16.670000 | 9.580000 | 10000.000000 | 250.000000 |  | 3.090000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 19:00:00 | 75.000000 | 8.720000 | 12.970000 | 72.000000 | 1024.000000 | 2.05 | 13.670000 | 6.760000 | 9000.000000 | 290.000000 |  | 5.140000 | 721 | Haze | haze | 50d | 19 |
| ![11d.png](http://openweathermap.org/img/w/11d.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 20:00:00 | 75.000000 | 8.720000 | 12.970000 | 72.000000 | 1023.000000 |  | 13.670000 | 3.950000 | 9000.000000 | 290.000000 |  | 3.090000 | 211 | Thunderstorm | thunderstorm | 11d | 20 |
| ![09d.png](http://openweathermap.org/img/w/09d.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 21:00:00 | 75.000000 | 7.730000 | 9.930000 | 82.000000 | 1023.000000 |  | 10.670000 | 1.620000 | 7000.000000 | 130.000000 |  | 3.090000 | 301 | Drizzle | drizzle | 09d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 22:00:00 | 75.000000 | 10.670000 | 10.400000 | 100.000000 | 1023.000000 |  | 10.670000 | 0.490000 | 10000.000000 | 30.000000 |  | 2.060000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206610 | "EFRAIN CA#AVERAL [21206610]" | 4.583333 | -74.066667 | 2804.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2009-08-05 00:00:00 | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 23:00:00 | 75.000000 | 9.750000 | 10.250000 | 94.000000 | 1024.000000 |  | 10.670000 | 0.000000 | 10000.000000 | 350.000000 |  | 1.540000 | 803 | Clouds | broken clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21206610_OWM_Clouds_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206610_OWM_Clouds_20220211.png)
![CNE_IDEAM_Station21206610_OWM_Dewpoint_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206610_OWM_Dewpoint_20220211.png)
![CNE_IDEAM_Station21206610_OWM_Feelslike_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206610_OWM_Feelslike_20220211.png)
![CNE_IDEAM_Station21206610_OWM_Humidity_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206610_OWM_Humidity_20220211.png)
![CNE_IDEAM_Station21206610_OWM_Pressure_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206610_OWM_Pressure_20220211.png)
![CNE_IDEAM_Station21206610_OWM_Rain_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206610_OWM_Rain_20220211.png)
![CNE_IDEAM_Station21206610_OWM_Temp_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206610_OWM_Temp_20220211.png)
![CNE_IDEAM_Station21206610_OWM_UVI_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206610_OWM_UVI_20220211.png)
![CNE_IDEAM_Station21206610_OWM_Visibility_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206610_OWM_Visibility_20220211.png)
![CNE_IDEAM_Station21206610_OWM_Winddeg_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206610_OWM_Winddeg_20220211.png)
![CNE_IDEAM_Station21206610_OWM_Windgust_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206610_OWM_Windgust_20220211.png)
![CNE_IDEAM_Station21206610_OWM_Windspeed_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206610_OWM_Windspeed_20220211.png)

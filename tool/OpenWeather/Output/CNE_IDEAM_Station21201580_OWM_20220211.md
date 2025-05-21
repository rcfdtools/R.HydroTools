
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PASQUILLA [21201580] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201580_OWM_20220211.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220211.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.4465,-74.15483333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.4465&lon=-74.15483333)

| Parameter | Value |
|---|---|
| Code | 21201580 |
| Name | PASQUILLA [21201580] |
| Latitude, ° | 4.4465 |
| Longitude, ° | -74.15483333 |
| Elevation, m | 30 |
| Category | Pluviométrica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1981-11-14 19:00:00 |
| Suspension date | NaT |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | 0 |
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

### (CNE index 2173) Open Weather values for station 21201580 - PASQUILLA [21201580]

JSON data from API OWM:

```
{'lat': 4.4465, 'lon': -74.1548, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644427498, 'sunrise': 1644405126, 'sunset': 1644448181, 'temp': 16.81, 'feels_like': 16.53, 'pressure': 1015, 'humidity': 76, 'dew_point': 12.56, 'uvi': 12.94, 'clouds': 97, 'visibility': 9685, 'wind_speed': 0.68, 'wind_deg': 235, 'wind_gust': 2.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644364800, 'temp': 9.81, 'feels_like': 9.81, 'pressure': 1016, 'humidity': 95, 'dew_point': 9.05, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.16, 'wind_deg': 170, 'wind_gust': 0.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644368400, 'temp': 8.81, 'feels_like': 8.81, 'pressure': 1017, 'humidity': 93, 'dew_point': 7.74, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 135, 'wind_gust': 0.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644372000, 'temp': 8.81, 'feels_like': 8.81, 'pressure': 1018, 'humidity': 92, 'dew_point': 7.58, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 129, 'wind_gust': 0.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644375600, 'temp': 6.81, 'feels_like': 6.81, 'pressure': 1019, 'humidity': 90, 'dew_point': 5.29, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 102, 'wind_gust': 1.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644379200, 'temp': 6.81, 'feels_like': 6.81, 'pressure': 1019, 'humidity': 89, 'dew_point': 5.13, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 114, 'wind_gust': 1.45, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644382800, 'temp': 6.81, 'feels_like': 6.81, 'pressure': 1018, 'humidity': 89, 'dew_point': 5.13, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 116, 'wind_gust': 1.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644386400, 'temp': 5.81, 'feels_like': 5.81, 'pressure': 1017, 'humidity': 88, 'dew_point': 3.98, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 112, 'wind_gust': 1.13, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644390000, 'temp': 5.81, 'feels_like': 5.81, 'pressure': 1016, 'humidity': 88, 'dew_point': 3.98, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 116, 'wind_gust': 1.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644393600, 'temp': 6.81, 'feels_like': 6.81, 'pressure': 1016, 'humidity': 88, 'dew_point': 4.96, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 108, 'wind_gust': 1.27, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644397200, 'temp': 6.81, 'feels_like': 6.81, 'pressure': 1016, 'humidity': 88, 'dew_point': 4.96, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.1, 'wind_deg': 111, 'wind_gust': 1.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644400800, 'temp': 6.81, 'feels_like': 6.81, 'pressure': 1016, 'humidity': 88, 'dew_point': 4.96, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 113, 'wind_gust': 1.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644404400, 'temp': 7.81, 'feels_like': 7.81, 'pressure': 1017, 'humidity': 87, 'dew_point': 5.78, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.1, 'wind_deg': 120, 'wind_gust': 1.5, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644408000, 'temp': 7.81, 'feels_like': 7.81, 'pressure': 1017, 'humidity': 83, 'dew_point': 5.11, 'uvi': 0.15, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 115, 'wind_gust': 1.22, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644411600, 'temp': 10.81, 'feels_like': 9.96, 'pressure': 1017, 'humidity': 77, 'dew_point': 6.94, 'uvi': 2.26, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 80, 'wind_gust': 1.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644415200, 'temp': 12.81, 'feels_like': 12, 'pressure': 1017, 'humidity': 71, 'dew_point': 7.69, 'uvi': 5.32, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.06, 'wind_deg': 96, 'wind_gust': 1.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644418800, 'temp': 14.81, 'feels_like': 14.12, 'pressure': 1017, 'humidity': 68, 'dew_point': 8.97, 'uvi': 8.92, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 298, 'wind_gust': 2.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644422400, 'temp': 15.81, 'feels_like': 15.27, 'pressure': 1016, 'humidity': 70, 'dew_point': 10.36, 'uvi': 11.89, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 257, 'wind_gust': 1.98, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644426000, 'temp': 16.81, 'feels_like': 16.53, 'pressure': 1015, 'humidity': 76, 'dew_point': 12.56, 'uvi': 12.94, 'clouds': 97, 'visibility': 9685, 'wind_speed': 0.68, 'wind_deg': 235, 'wind_gust': 2.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644429600, 'temp': 16.81, 'feels_like': 16.71, 'pressure': 1014, 'humidity': 83, 'dew_point': 13.91, 'uvi': 11.76, 'clouds': 81, 'visibility': 7132, 'wind_speed': 0.41, 'wind_deg': 254, 'wind_gust': 1.94, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644433200, 'temp': 13.81, 'feels_like': 13.44, 'pressure': 1013, 'humidity': 84, 'dew_point': 11.16, 'uvi': 8.13, 'clouds': 91, 'visibility': 6161, 'wind_speed': 0.2, 'wind_deg': 223, 'wind_gust': 1.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.65}}, {'dt': 1644436800, 'temp': 13.81, 'feels_like': 13.54, 'pressure': 1012, 'humidity': 88, 'dew_point': 11.86, 'uvi': 4.75, 'clouds': 94, 'visibility': 6511, 'wind_speed': 0.24, 'wind_deg': 174, 'wind_gust': 1.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 1}}, {'dt': 1644440400, 'temp': 10.81, 'feels_like': 10.3, 'pressure': 1012, 'humidity': 90, 'dew_point': 9.24, 'uvi': 1.96, 'clouds': 96, 'visibility': 7249, 'wind_speed': 0.36, 'wind_deg': 124, 'wind_gust': 1.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644444000, 'temp': 10.81, 'feels_like': 10.35, 'pressure': 1013, 'humidity': 92, 'dew_point': 9.56, 'uvi': 0.4, 'clouds': 96, 'visibility': 7963, 'wind_speed': 0.29, 'wind_deg': 101, 'wind_gust': 1.56, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644447600, 'temp': 10.81, 'feels_like': 10.43, 'pressure': 1014, 'humidity': 95, 'dew_point': 10.04, 'uvi': 0, 'clouds': 96, 'visibility': 7465, 'wind_speed': 0.7, 'wind_deg': 99, 'wind_gust': 1.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 00:00:00 | 100.000000 | 9.050000 | 9.810000 | 95.000000 | 1016.000000 |  | 9.810000 | 0.000000 | 10000.000000 | 170.000000 | 0.78 | 0.160000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 01:00:00 | 100.000000 | 7.740000 | 8.810000 | 93.000000 | 1017.000000 |  | 8.810000 | 0.000000 | 10000.000000 | 135.000000 | 0.84 | 0.410000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 02:00:00 | 100.000000 | 7.580000 | 8.810000 | 92.000000 | 1018.000000 |  | 8.810000 | 0.000000 | 10000.000000 | 129.000000 | 0.96 | 0.480000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 03:00:00 | 99.000000 | 5.290000 | 6.810000 | 90.000000 | 1019.000000 |  | 6.810000 | 0.000000 | 10000.000000 | 102.000000 | 1.41 | 0.860000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 04:00:00 | 92.000000 | 5.130000 | 6.810000 | 89.000000 | 1019.000000 |  | 6.810000 | 0.000000 | 10000.000000 | 114.000000 | 1.45 | 0.960000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 05:00:00 | 93.000000 | 5.130000 | 6.810000 | 89.000000 | 1018.000000 |  | 6.810000 | 0.000000 | 10000.000000 | 116.000000 | 1.34 | 0.720000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 06:00:00 | 86.000000 | 3.980000 | 5.810000 | 88.000000 | 1017.000000 |  | 5.810000 | 0.000000 | 10000.000000 | 112.000000 | 1.13 | 0.700000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 07:00:00 | 94.000000 | 3.980000 | 5.810000 | 88.000000 | 1016.000000 |  | 5.810000 | 0.000000 | 10000.000000 | 116.000000 | 1.3 | 0.840000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 08:00:00 | 92.000000 | 4.960000 | 6.810000 | 88.000000 | 1016.000000 |  | 6.810000 | 0.000000 | 10000.000000 | 108.000000 | 1.27 | 0.930000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 09:00:00 | 91.000000 | 4.960000 | 6.810000 | 88.000000 | 1016.000000 |  | 6.810000 | 0.000000 | 10000.000000 | 111.000000 | 1.38 | 1.100000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 10:00:00 | 87.000000 | 4.960000 | 6.810000 | 88.000000 | 1016.000000 |  | 6.810000 | 0.000000 | 10000.000000 | 113.000000 | 1.57 | 1.120000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 11:00:00 | 83.000000 | 5.780000 | 7.810000 | 87.000000 | 1017.000000 |  | 7.810000 | 0.000000 | 10000.000000 | 120.000000 | 1.5 | 1.100000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 12:00:00 | 83.000000 | 5.110000 | 7.810000 | 83.000000 | 1017.000000 |  | 7.810000 | 0.150000 | 10000.000000 | 115.000000 | 1.22 | 0.730000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 13:00:00 | 89.000000 | 6.940000 | 9.960000 | 77.000000 | 1017.000000 |  | 10.810000 | 2.260000 | 10000.000000 | 80.000000 | 1.48 | 0.400000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 14:00:00 | 95.000000 | 7.690000 | 12.000000 | 71.000000 | 1017.000000 |  | 12.810000 | 5.320000 | 10000.000000 | 96.000000 | 1.7 | 0.060000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 15:00:00 | 96.000000 | 8.970000 | 14.120000 | 68.000000 | 1017.000000 |  | 14.810000 | 8.920000 | 10000.000000 | 298.000000 | 2.05 | 0.330000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 16:00:00 | 97.000000 | 10.360000 | 15.270000 | 70.000000 | 1016.000000 |  | 15.810000 | 11.890000 | 10000.000000 | 257.000000 | 1.98 | 0.530000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 17:00:00 | 97.000000 | 12.560000 | 16.530000 | 76.000000 | 1015.000000 |  | 16.810000 | 12.940000 | 9685.000000 | 235.000000 | 2.07 | 0.680000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 18:00:00 | 81.000000 | 13.910000 | 16.710000 | 83.000000 | 1014.000000 |  | 16.810000 | 11.760000 | 7132.000000 | 254.000000 | 1.94 | 0.410000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 19:00:00 | 91.000000 | 11.160000 | 13.440000 | 84.000000 | 1013.000000 | 0.65 | 13.810000 | 8.130000 | 6161.000000 | 223.000000 | 1.74 | 0.200000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 20:00:00 | 94.000000 | 11.860000 | 13.540000 | 88.000000 | 1012.000000 | 1 | 13.810000 | 4.750000 | 6511.000000 | 174.000000 | 1.77 | 0.240000 | 500 | Rain | light rain | 10d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 21:00:00 | 96.000000 | 9.240000 | 10.300000 | 90.000000 | 1012.000000 |  | 10.810000 | 1.960000 | 7249.000000 | 124.000000 | 1.71 | 0.360000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 22:00:00 | 96.000000 | 9.560000 | 10.350000 | 92.000000 | 1013.000000 |  | 10.810000 | 0.400000 | 7963.000000 | 101.000000 | 1.56 | 0.290000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 23:00:00 | 96.000000 | 10.040000 | 10.430000 | 95.000000 | 1014.000000 |  | 10.810000 | 0.000000 | 7465.000000 | 99.000000 | 1.32 | 0.700000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21201580_OWM_Clouds_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Clouds_20220211.png)
![CNE_IDEAM_Station21201580_OWM_Dewpoint_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Dewpoint_20220211.png)
![CNE_IDEAM_Station21201580_OWM_Feelslike_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Feelslike_20220211.png)
![CNE_IDEAM_Station21201580_OWM_Humidity_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Humidity_20220211.png)
![CNE_IDEAM_Station21201580_OWM_Pressure_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Pressure_20220211.png)
![CNE_IDEAM_Station21201580_OWM_Rain_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Rain_20220211.png)
![CNE_IDEAM_Station21201580_OWM_Temp_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Temp_20220211.png)
![CNE_IDEAM_Station21201580_OWM_UVI_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_UVI_20220211.png)
![CNE_IDEAM_Station21201580_OWM_Visibility_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Visibility_20220211.png)
![CNE_IDEAM_Station21201580_OWM_Winddeg_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Winddeg_20220211.png)
![CNE_IDEAM_Station21201580_OWM_Windgust_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Windgust_20220211.png)
![CNE_IDEAM_Station21201580_OWM_Windspeed_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Windspeed_20220211.png)

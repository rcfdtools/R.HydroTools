
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ESCUELA LA UNION [21201200] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201200_OWM_20220211.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220211.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.34294444,-74.18388889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.34294444&lon=-74.18388889)

| Parameter | Value |
|---|---|
| Code | 21201200 |
| Name | ESCUELA LA UNION [21201200] |
| Latitude, ° | 4.34294444 |
| Longitude, ° | -74.18388889 |
| Elevation, m | 3320 |
| Category | Pluviométrica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1985-03-14 19:00:00 |
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

### (CNE index 3317) Open Weather values for station 21201200 - ESCUELA LA UNION [21201200]

JSON data from API OWM:

```
{'lat': 4.3429, 'lon': -74.1839, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644427498, 'sunrise': 1644405126, 'sunset': 1644448195, 'temp': 13.98, 'feels_like': 13.55, 'pressure': 1015, 'humidity': 81, 'dew_point': 10.78, 'uvi': 12.94, 'clouds': 98, 'visibility': 8145, 'wind_speed': 0.49, 'wind_deg': 268, 'wind_gust': 1.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644364800, 'temp': 6.98, 'feels_like': 6.98, 'pressure': 1017, 'humidity': 96, 'dew_point': 6.39, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.29, 'wind_deg': 139, 'wind_gust': 0.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644368400, 'temp': 5.98, 'feels_like': 5.98, 'pressure': 1018, 'humidity': 93, 'dew_point': 4.94, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 129, 'wind_gust': 0.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644372000, 'temp': 5.98, 'feels_like': 5.98, 'pressure': 1019, 'humidity': 92, 'dew_point': 4.78, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 116, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644375600, 'temp': 3.98, 'feels_like': 3.98, 'pressure': 1019, 'humidity': 90, 'dew_point': 2.49, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 108, 'wind_gust': 1.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644379200, 'temp': 3.98, 'feels_like': 3.98, 'pressure': 1019, 'humidity': 89, 'dew_point': 2.33, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 112, 'wind_gust': 1.56, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644382800, 'temp': 3.98, 'feels_like': 3.98, 'pressure': 1019, 'humidity': 89, 'dew_point': 2.33, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 114, 'wind_gust': 1.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644386400, 'temp': 2.98, 'feels_like': 2.98, 'pressure': 1018, 'humidity': 89, 'dew_point': 1.35, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 114, 'wind_gust': 1.06, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644390000, 'temp': 2.98, 'feels_like': 2.98, 'pressure': 1017, 'humidity': 89, 'dew_point': 1.35, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 116, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644393600, 'temp': 3.98, 'feels_like': 3.98, 'pressure': 1016, 'humidity': 89, 'dew_point': 2.33, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 109, 'wind_gust': 1.23, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644397200, 'temp': 3.98, 'feels_like': 3.98, 'pressure': 1016, 'humidity': 89, 'dew_point': 2.33, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 109, 'wind_gust': 1.33, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644400800, 'temp': 3.98, 'feels_like': 3.98, 'pressure': 1017, 'humidity': 89, 'dew_point': 2.33, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 105, 'wind_gust': 1.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644404400, 'temp': 4.98, 'feels_like': 4.98, 'pressure': 1017, 'humidity': 89, 'dew_point': 3.32, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 111, 'wind_gust': 1.48, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644408000, 'temp': 4.98, 'feels_like': 4.98, 'pressure': 1017, 'humidity': 86, 'dew_point': 2.84, 'uvi': 0.15, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 101, 'wind_gust': 1.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644411600, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1017, 'humidity': 79, 'dew_point': 4.57, 'uvi': 2.26, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 52, 'wind_gust': 1.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644415200, 'temp': 9.98, 'feels_like': 9.98, 'pressure': 1018, 'humidity': 76, 'dew_point': 5.95, 'uvi': 5.32, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 1, 'wind_gust': 1.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644418800, 'temp': 11.98, 'feels_like': 11.17, 'pressure': 1017, 'humidity': 74, 'dew_point': 7.5, 'uvi': 8.92, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 327, 'wind_gust': 1.94, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644422400, 'temp': 12.98, 'feels_like': 12.34, 'pressure': 1017, 'humidity': 77, 'dew_point': 9.05, 'uvi': 11.89, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 301, 'wind_gust': 1.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644426000, 'temp': 13.98, 'feels_like': 13.55, 'pressure': 1015, 'humidity': 81, 'dew_point': 10.78, 'uvi': 12.94, 'clouds': 98, 'visibility': 8145, 'wind_speed': 0.49, 'wind_deg': 268, 'wind_gust': 1.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644429600, 'temp': 13.98, 'feels_like': 13.68, 'pressure': 1015, 'humidity': 86, 'dew_point': 11.68, 'uvi': 11.76, 'clouds': 86, 'visibility': 6568, 'wind_speed': 0.57, 'wind_deg': 275, 'wind_gust': 1.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644433200, 'temp': 10.98, 'feels_like': 10.43, 'pressure': 1013, 'humidity': 88, 'dew_point': 9.07, 'uvi': 8.13, 'clouds': 95, 'visibility': 6078, 'wind_speed': 0.35, 'wind_deg': 277, 'wind_gust': 1.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644436800, 'temp': 10.98, 'feels_like': 10.48, 'pressure': 1013, 'humidity': 90, 'dew_point': 9.41, 'uvi': 4.75, 'clouds': 97, 'visibility': 5411, 'wind_speed': 0.12, 'wind_deg': 261, 'wind_gust': 1.51, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.65}}, {'dt': 1644440400, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1013, 'humidity': 92, 'dew_point': 6.76, 'uvi': 1.96, 'clouds': 98, 'visibility': 4804, 'wind_speed': 0.12, 'wind_deg': 65, 'wind_gust': 1.42, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.78}}, {'dt': 1644444000, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1013, 'humidity': 93, 'dew_point': 6.92, 'uvi': 0.4, 'clouds': 98, 'visibility': 5667, 'wind_speed': 0.26, 'wind_deg': 24, 'wind_gust': 1.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644447600, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1014, 'humidity': 97, 'dew_point': 7.53, 'uvi': 0, 'clouds': 97, 'visibility': 3429, 'wind_speed': 0.6, 'wind_deg': 74, 'wind_gust': 1.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 00:00:00 | 100.000000 | 6.390000 | 6.980000 | 96.000000 | 1017.000000 |  | 6.980000 | 0.000000 | 10000.000000 | 139.000000 | 0.92 | 0.290000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 01:00:00 | 100.000000 | 4.940000 | 5.980000 | 93.000000 | 1018.000000 |  | 5.980000 | 0.000000 | 10000.000000 | 129.000000 | 0.92 | 0.490000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 02:00:00 | 100.000000 | 4.780000 | 5.980000 | 92.000000 | 1019.000000 |  | 5.980000 | 0.000000 | 10000.000000 | 116.000000 | 1.18 | 0.740000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 03:00:00 | 99.000000 | 2.490000 | 3.980000 | 90.000000 | 1019.000000 |  | 3.980000 | 0.000000 | 10000.000000 | 108.000000 | 1.51 | 1.080000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 04:00:00 | 91.000000 | 2.330000 | 3.980000 | 89.000000 | 1019.000000 |  | 3.980000 | 0.000000 | 10000.000000 | 112.000000 | 1.56 | 1.200000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 05:00:00 | 92.000000 | 2.330000 | 3.980000 | 89.000000 | 1019.000000 |  | 3.980000 | 0.000000 | 10000.000000 | 114.000000 | 1.46 | 1.000000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 06:00:00 | 77.000000 | 1.350000 | 2.980000 | 89.000000 | 1018.000000 |  | 2.980000 | 0.000000 | 10000.000000 | 114.000000 | 1.06 | 0.760000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 07:00:00 | 86.000000 | 1.350000 | 2.980000 | 89.000000 | 1017.000000 |  | 2.980000 | 0.000000 | 10000.000000 | 116.000000 | 1.18 | 0.870000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 08:00:00 | 82.000000 | 2.330000 | 3.980000 | 89.000000 | 1016.000000 |  | 3.980000 | 0.000000 | 10000.000000 | 109.000000 | 1.23 | 0.900000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 09:00:00 | 82.000000 | 2.330000 | 3.980000 | 89.000000 | 1016.000000 |  | 3.980000 | 0.000000 | 10000.000000 | 109.000000 | 1.33 | 1.070000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 10:00:00 | 79.000000 | 2.330000 | 3.980000 | 89.000000 | 1017.000000 |  | 3.980000 | 0.000000 | 10000.000000 | 105.000000 | 1.54 | 1.120000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 11:00:00 | 76.000000 | 3.320000 | 4.980000 | 89.000000 | 1017.000000 |  | 4.980000 | 0.000000 | 10000.000000 | 111.000000 | 1.48 | 1.110000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 12:00:00 | 90.000000 | 2.840000 | 4.980000 | 86.000000 | 1017.000000 |  | 4.980000 | 0.150000 | 10000.000000 | 101.000000 | 1.31 | 0.730000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 13:00:00 | 94.000000 | 4.570000 | 7.980000 | 79.000000 | 1017.000000 |  | 7.980000 | 2.260000 | 10000.000000 | 52.000000 | 1.52 | 0.480000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 14:00:00 | 97.000000 | 5.950000 | 9.980000 | 76.000000 | 1018.000000 |  | 9.980000 | 5.320000 | 10000.000000 | 1.000000 | 1.7 | 0.320000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 15:00:00 | 98.000000 | 7.500000 | 11.170000 | 74.000000 | 1017.000000 |  | 11.980000 | 8.920000 | 10000.000000 | 327.000000 | 1.94 | 0.570000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 16:00:00 | 98.000000 | 9.050000 | 12.340000 | 77.000000 | 1017.000000 |  | 12.980000 | 11.890000 | 10000.000000 | 301.000000 | 1.85 | 0.470000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 17:00:00 | 98.000000 | 10.780000 | 13.550000 | 81.000000 | 1015.000000 |  | 13.980000 | 12.940000 | 8145.000000 | 268.000000 | 1.87 | 0.490000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 18:00:00 | 86.000000 | 11.680000 | 13.680000 | 86.000000 | 1015.000000 |  | 13.980000 | 11.760000 | 6568.000000 | 275.000000 | 1.86 | 0.570000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 19:00:00 | 95.000000 | 9.070000 | 10.430000 | 88.000000 | 1013.000000 |  | 10.980000 | 8.130000 | 6078.000000 | 277.000000 | 1.6 | 0.350000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 20:00:00 | 97.000000 | 9.410000 | 10.480000 | 90.000000 | 1013.000000 | 0.65 | 10.980000 | 4.750000 | 5411.000000 | 261.000000 | 1.51 | 0.120000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 21:00:00 | 98.000000 | 6.760000 | 7.980000 | 92.000000 | 1013.000000 | 1.78 | 7.980000 | 1.960000 | 4804.000000 | 65.000000 | 1.42 | 0.120000 | 501 | Rain | moderate rain | 10d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 22:00:00 | 98.000000 | 6.920000 | 7.980000 | 93.000000 | 1013.000000 |  | 7.980000 | 0.400000 | 5667.000000 | 24.000000 | 1.31 | 0.260000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 23:00:00 | 97.000000 | 7.530000 | 7.980000 | 97.000000 | 1014.000000 |  | 7.980000 | 0.000000 | 3429.000000 | 74.000000 | 1.14 | 0.600000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21201200_OWM_Clouds_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Clouds_20220211.png)
![CNE_IDEAM_Station21201200_OWM_Dewpoint_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Dewpoint_20220211.png)
![CNE_IDEAM_Station21201200_OWM_Feelslike_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Feelslike_20220211.png)
![CNE_IDEAM_Station21201200_OWM_Humidity_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Humidity_20220211.png)
![CNE_IDEAM_Station21201200_OWM_Pressure_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Pressure_20220211.png)
![CNE_IDEAM_Station21201200_OWM_Rain_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Rain_20220211.png)
![CNE_IDEAM_Station21201200_OWM_Temp_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Temp_20220211.png)
![CNE_IDEAM_Station21201200_OWM_UVI_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_UVI_20220211.png)
![CNE_IDEAM_Station21201200_OWM_Visibility_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Visibility_20220211.png)
![CNE_IDEAM_Station21201200_OWM_Winddeg_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Winddeg_20220211.png)
![CNE_IDEAM_Station21201200_OWM_Windgust_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Windgust_20220211.png)
![CNE_IDEAM_Station21201200_OWM_Windspeed_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Windspeed_20220211.png)

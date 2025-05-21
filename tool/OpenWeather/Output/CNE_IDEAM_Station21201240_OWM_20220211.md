
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SANTA MARIA DE USME [21201240] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201240_OWM_20220211.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220211.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.48130556,-74.12627778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.48130556&lon=-74.12627778)

| Parameter | Value |
|---|---|
| Code | 21201240 |
| Name | SANTA MARIA DE USME [21201240] |
| Latitude, ° | 4.48130556 |
| Longitude, ° | -74.12627778 |
| Elevation, m | 2800 |
| Category | Pluviométrica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1977-12-15 00:00:00 |
| Suspension date | NaT |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Bogota |
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

### (CNE index 2076) Open Weather values for station 21201240 - SANTA MARIA DE USME [21201240]

JSON data from API OWM:

```
{'lat': 4.4813, 'lon': -74.1263, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644427498, 'sunrise': 1644405121, 'sunset': 1644448172, 'temp': 18.14, 'feels_like': 17.92, 'pressure': 1015, 'humidity': 73, 'dew_point': 13.23, 'uvi': 12.94, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 200, 'wind_gust': 2.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644364800, 'temp': 11.14, 'feels_like': 10.79, 'pressure': 1016, 'humidity': 95, 'dew_point': 10.37, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 184, 'wind_gust': 0.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644368400, 'temp': 10.14, 'feels_like': 9.66, 'pressure': 1017, 'humidity': 94, 'dew_point': 9.22, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 144, 'wind_gust': 0.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644372000, 'temp': 10.14, 'feels_like': 9.61, 'pressure': 1018, 'humidity': 92, 'dew_point': 8.9, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 143, 'wind_gust': 0.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644375600, 'temp': 8.14, 'feels_like': 8.14, 'pressure': 1019, 'humidity': 91, 'dew_point': 6.76, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 102, 'wind_gust': 1.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644379200, 'temp': 8.14, 'feels_like': 8.14, 'pressure': 1019, 'humidity': 90, 'dew_point': 6.6, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 120, 'wind_gust': 1.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644382800, 'temp': 8.14, 'feels_like': 8.14, 'pressure': 1018, 'humidity': 90, 'dew_point': 6.6, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 124, 'wind_gust': 1.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644386400, 'temp': 7.14, 'feels_like': 7.14, 'pressure': 1017, 'humidity': 88, 'dew_point': 5.29, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 117, 'wind_gust': 1.1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644390000, 'temp': 7.14, 'feels_like': 7.14, 'pressure': 1016, 'humidity': 88, 'dew_point': 5.29, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 124, 'wind_gust': 1.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644393600, 'temp': 8.14, 'feels_like': 8.14, 'pressure': 1016, 'humidity': 88, 'dew_point': 6.27, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 112, 'wind_gust': 1.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644397200, 'temp': 8.14, 'feels_like': 8.14, 'pressure': 1016, 'humidity': 88, 'dew_point': 6.27, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 116, 'wind_gust': 1.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644400800, 'temp': 8.14, 'feels_like': 8.14, 'pressure': 1016, 'humidity': 88, 'dew_point': 6.27, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 121, 'wind_gust': 1.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644404400, 'temp': 9.14, 'feels_like': 9.14, 'pressure': 1017, 'humidity': 88, 'dew_point': 7.26, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 129, 'wind_gust': 1.45, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644408000, 'temp': 9.14, 'feels_like': 9.14, 'pressure': 1017, 'humidity': 83, 'dew_point': 6.41, 'uvi': 0.15, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 125, 'wind_gust': 1.2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644411600, 'temp': 12.14, 'feels_like': 11.39, 'pressure': 1017, 'humidity': 76, 'dew_point': 8.04, 'uvi': 2.26, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 107, 'wind_gust': 1.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644415200, 'temp': 14.14, 'feels_like': 13.41, 'pressure': 1017, 'humidity': 69, 'dew_point': 8.54, 'uvi': 5.32, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 144, 'wind_gust': 1.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644418800, 'temp': 16.14, 'feels_like': 15.51, 'pressure': 1016, 'humidity': 65, 'dew_point': 9.56, 'uvi': 8.92, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 203, 'wind_gust': 2.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644422400, 'temp': 17.14, 'feels_like': 16.63, 'pressure': 1016, 'humidity': 66, 'dew_point': 10.74, 'uvi': 11.89, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 208, 'wind_gust': 2.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644426000, 'temp': 18.14, 'feels_like': 17.92, 'pressure': 1015, 'humidity': 73, 'dew_point': 13.23, 'uvi': 12.94, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 200, 'wind_gust': 2.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644429600, 'temp': 18.14, 'feels_like': 18.1, 'pressure': 1014, 'humidity': 80, 'dew_point': 14.64, 'uvi': 11.76, 'clouds': 79, 'visibility': 8150, 'wind_speed': 0.34, 'wind_deg': 189, 'wind_gust': 2.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644433200, 'temp': 15.14, 'feels_like': 14.85, 'pressure': 1013, 'humidity': 82, 'dew_point': 12.09, 'uvi': 8.13, 'clouds': 91, 'visibility': 6835, 'wind_speed': 0.41, 'wind_deg': 154, 'wind_gust': 1.86, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.54}}, {'dt': 1644436800, 'temp': 15.14, 'feels_like': 14.96, 'pressure': 1012, 'humidity': 86, 'dew_point': 12.82, 'uvi': 4.75, 'clouds': 93, 'visibility': 8182, 'wind_speed': 0.56, 'wind_deg': 147, 'wind_gust': 1.93, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.15}}, {'dt': 1644440400, 'temp': 12.14, 'feels_like': 11.73, 'pressure': 1012, 'humidity': 89, 'dew_point': 10.38, 'uvi': 1.96, 'clouds': 95, 'visibility': 9953, 'wind_speed': 0.69, 'wind_deg': 129, 'wind_gust': 1.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644444000, 'temp': 12.14, 'feels_like': 11.79, 'pressure': 1013, 'humidity': 91, 'dew_point': 10.72, 'uvi': 0.4, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 121, 'wind_gust': 1.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644447600, 'temp': 12.14, 'feels_like': 11.89, 'pressure': 1014, 'humidity': 95, 'dew_point': 11.36, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 112, 'wind_gust': 1.47, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 00:00:00 | 100.000000 | 10.370000 | 10.790000 | 95.000000 | 1016.000000 |  | 11.140000 | 0.000000 | 10000.000000 | 184.000000 | 0.73 | 0.170000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 01:00:00 | 100.000000 | 9.220000 | 9.660000 | 94.000000 | 1017.000000 |  | 10.140000 | 0.000000 | 10000.000000 | 144.000000 | 0.83 | 0.370000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 02:00:00 | 100.000000 | 8.900000 | 9.610000 | 92.000000 | 1018.000000 |  | 10.140000 | 0.000000 | 10000.000000 | 143.000000 | 0.9 | 0.390000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 03:00:00 | 100.000000 | 6.760000 | 8.140000 | 91.000000 | 1019.000000 |  | 8.140000 | 0.000000 | 10000.000000 | 102.000000 | 1.32 | 0.670000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 04:00:00 | 94.000000 | 6.600000 | 8.140000 | 90.000000 | 1019.000000 |  | 8.140000 | 0.000000 | 10000.000000 | 120.000000 | 1.38 | 0.760000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 05:00:00 | 94.000000 | 6.600000 | 8.140000 | 90.000000 | 1018.000000 |  | 8.140000 | 0.000000 | 10000.000000 | 124.000000 | 1.28 | 0.510000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 06:00:00 | 90.000000 | 5.290000 | 7.140000 | 88.000000 | 1017.000000 |  | 7.140000 | 0.000000 | 10000.000000 | 117.000000 | 1.1 | 0.580000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 07:00:00 | 97.000000 | 5.290000 | 7.140000 | 88.000000 | 1016.000000 |  | 7.140000 | 0.000000 | 10000.000000 | 124.000000 | 1.28 | 0.730000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 08:00:00 | 96.000000 | 6.270000 | 8.140000 | 88.000000 | 1016.000000 |  | 8.140000 | 0.000000 | 10000.000000 | 112.000000 | 1.2 | 0.810000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 09:00:00 | 94.000000 | 6.270000 | 8.140000 | 88.000000 | 1016.000000 |  | 8.140000 | 0.000000 | 10000.000000 | 116.000000 | 1.29 | 0.960000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 10:00:00 | 90.000000 | 6.270000 | 8.140000 | 88.000000 | 1016.000000 |  | 8.140000 | 0.000000 | 10000.000000 | 121.000000 | 1.49 | 0.960000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 11:00:00 | 86.000000 | 7.260000 | 9.140000 | 88.000000 | 1017.000000 |  | 9.140000 | 0.000000 | 10000.000000 | 129.000000 | 1.45 | 0.980000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 12:00:00 | 84.000000 | 6.410000 | 9.140000 | 83.000000 | 1017.000000 |  | 9.140000 | 0.150000 | 10000.000000 | 125.000000 | 1.2 | 0.720000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 13:00:00 | 90.000000 | 8.040000 | 11.390000 | 76.000000 | 1017.000000 |  | 12.140000 | 2.260000 | 10000.000000 | 107.000000 | 1.51 | 0.470000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 14:00:00 | 95.000000 | 8.540000 | 13.410000 | 69.000000 | 1017.000000 |  | 14.140000 | 5.320000 | 10000.000000 | 144.000000 | 1.76 | 0.370000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 15:00:00 | 96.000000 | 9.560000 | 15.510000 | 65.000000 | 1016.000000 |  | 16.140000 | 8.920000 | 10000.000000 | 203.000000 | 2.09 | 0.190000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 16:00:00 | 96.000000 | 10.740000 | 16.630000 | 66.000000 | 1016.000000 |  | 17.140000 | 11.890000 | 10000.000000 | 208.000000 | 2.05 | 0.450000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 17:00:00 | 97.000000 | 13.230000 | 17.920000 | 73.000000 | 1015.000000 |  | 18.140000 | 12.940000 | 10000.000000 | 200.000000 | 2.14 | 0.650000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 18:00:00 | 79.000000 | 14.640000 | 18.100000 | 80.000000 | 1014.000000 |  | 18.140000 | 11.760000 | 8150.000000 | 189.000000 | 2.01 | 0.340000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 19:00:00 | 91.000000 | 12.090000 | 14.850000 | 82.000000 | 1013.000000 | 1.54 | 15.140000 | 8.130000 | 6835.000000 | 154.000000 | 1.86 | 0.410000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 20:00:00 | 93.000000 | 12.820000 | 14.960000 | 86.000000 | 1012.000000 | 1.15 | 15.140000 | 4.750000 | 8182.000000 | 147.000000 | 1.93 | 0.560000 | 501 | Rain | moderate rain | 10d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 21:00:00 | 95.000000 | 10.380000 | 11.730000 | 89.000000 | 1012.000000 |  | 12.140000 | 1.960000 | 9953.000000 | 129.000000 | 1.89 | 0.690000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 22:00:00 | 96.000000 | 10.720000 | 11.790000 | 91.000000 | 1013.000000 |  | 12.140000 | 0.400000 | 10000.000000 | 121.000000 | 1.71 | 0.560000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 23:00:00 | 96.000000 | 11.360000 | 11.890000 | 95.000000 | 1014.000000 |  | 12.140000 | 0.000000 | 10000.000000 | 112.000000 | 1.47 | 0.820000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21201240_OWM_Clouds_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Clouds_20220211.png)
![CNE_IDEAM_Station21201240_OWM_Dewpoint_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Dewpoint_20220211.png)
![CNE_IDEAM_Station21201240_OWM_Feelslike_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Feelslike_20220211.png)
![CNE_IDEAM_Station21201240_OWM_Humidity_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Humidity_20220211.png)
![CNE_IDEAM_Station21201240_OWM_Pressure_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Pressure_20220211.png)
![CNE_IDEAM_Station21201240_OWM_Rain_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Rain_20220211.png)
![CNE_IDEAM_Station21201240_OWM_Temp_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Temp_20220211.png)
![CNE_IDEAM_Station21201240_OWM_UVI_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_UVI_20220211.png)
![CNE_IDEAM_Station21201240_OWM_Visibility_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Visibility_20220211.png)
![CNE_IDEAM_Station21201240_OWM_Winddeg_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Winddeg_20220211.png)
![CNE_IDEAM_Station21201240_OWM_Windgust_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Windgust_20220211.png)
![CNE_IDEAM_Station21201240_OWM_Windspeed_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Windspeed_20220211.png)

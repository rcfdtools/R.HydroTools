
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ANIMAS LAS [35027150] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35027150_OWM_20220211.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220211.csv)

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

### (CNE index 1622) Open Weather values for station 35027150 - ANIMAS LAS [35027150]

JSON data from API OWM:

```
{'lat': 4.138, 'lon': -74.1738, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644427498, 'sunrise': 1644405111, 'sunset': 1644448205, 'temp': 16.46, 'feels_like': 16.41, 'pressure': 1017, 'humidity': 86, 'dew_point': 14.11, 'uvi': 12.94, 'clouds': 100, 'visibility': 5392, 'wind_speed': 0.8, 'wind_deg': 105, 'wind_gust': 1.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644364800, 'temp': 9.46, 'feels_like': 9.46, 'pressure': 1017, 'humidity': 95, 'dew_point': 8.7, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 130, 'wind_gust': 1.13, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644368400, 'temp': 8.46, 'feels_like': 8.46, 'pressure': 1018, 'humidity': 94, 'dew_point': 7.55, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 135, 'wind_gust': 1.19, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644372000, 'temp': 8.46, 'feels_like': 8.46, 'pressure': 1019, 'humidity': 93, 'dew_point': 7.39, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 119, 'wind_gust': 1.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644375600, 'temp': 6.46, 'feels_like': 6.46, 'pressure': 1020, 'humidity': 92, 'dew_point': 5.26, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 117, 'wind_gust': 1.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644379200, 'temp': 6.46, 'feels_like': 6.46, 'pressure': 1020, 'humidity': 91, 'dew_point': 5.1, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 121, 'wind_gust': 1.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644382800, 'temp': 6.46, 'feels_like': 6.46, 'pressure': 1019, 'humidity': 91, 'dew_point': 5.1, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 126, 'wind_gust': 1.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644386400, 'temp': 5.46, 'feels_like': 5.46, 'pressure': 1018, 'humidity': 92, 'dew_point': 4.27, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 122, 'wind_gust': 1.14, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644390000, 'temp': 5.46, 'feels_like': 5.46, 'pressure': 1017, 'humidity': 92, 'dew_point': 4.27, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 123, 'wind_gust': 1.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644393600, 'temp': 6.46, 'feels_like': 6.46, 'pressure': 1017, 'humidity': 92, 'dew_point': 5.26, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 120, 'wind_gust': 1.18, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644397200, 'temp': 6.46, 'feels_like': 6.46, 'pressure': 1017, 'humidity': 92, 'dew_point': 5.26, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 117, 'wind_gust': 1.19, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644400800, 'temp': 6.46, 'feels_like': 6.46, 'pressure': 1017, 'humidity': 92, 'dew_point': 5.26, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 105, 'wind_gust': 1.32, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644404400, 'temp': 7.46, 'feels_like': 7.46, 'pressure': 1018, 'humidity': 92, 'dew_point': 6.25, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 104, 'wind_gust': 1.29, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644408000, 'temp': 7.46, 'feels_like': 7.46, 'pressure': 1018, 'humidity': 90, 'dew_point': 5.93, 'uvi': 0.15, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 84, 'wind_gust': 1.43, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644411600, 'temp': 10.46, 'feels_like': 9.75, 'pressure': 1018, 'humidity': 84, 'dew_point': 7.88, 'uvi': 2.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 85, 'wind_gust': 1.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644415200, 'temp': 12.46, 'feels_like': 11.9, 'pressure': 1018, 'humidity': 82, 'dew_point': 9.48, 'uvi': 5.32, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 85, 'wind_gust': 1.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644418800, 'temp': 14.46, 'feels_like': 14.08, 'pressure': 1018, 'humidity': 81, 'dew_point': 11.24, 'uvi': 8.92, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 83, 'wind_gust': 1.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644422400, 'temp': 15.46, 'feels_like': 15.28, 'pressure': 1018, 'humidity': 85, 'dew_point': 12.95, 'uvi': 11.89, 'clouds': 100, 'visibility': 6984, 'wind_speed': 0.74, 'wind_deg': 92, 'wind_gust': 1.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644426000, 'temp': 16.46, 'feels_like': 16.41, 'pressure': 1017, 'humidity': 86, 'dew_point': 14.11, 'uvi': 12.94, 'clouds': 100, 'visibility': 5392, 'wind_speed': 0.8, 'wind_deg': 105, 'wind_gust': 1.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644429600, 'temp': 16.46, 'feels_like': 16.51, 'pressure': 1016, 'humidity': 90, 'dew_point': 14.82, 'uvi': 11.76, 'clouds': 94, 'visibility': 4225, 'wind_speed': 0.64, 'wind_deg': 125, 'wind_gust': 1.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644433200, 'temp': 13.46, 'feels_like': 13.24, 'pressure': 1015, 'humidity': 91, 'dew_point': 12.02, 'uvi': 8.13, 'clouds': 99, 'visibility': 4185, 'wind_speed': 0.64, 'wind_deg': 116, 'wind_gust': 1.63, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.15}}, {'dt': 1644436800, 'temp': 13.46, 'feels_like': 13.26, 'pressure': 1014, 'humidity': 92, 'dew_point': 12.19, 'uvi': 4.75, 'clouds': 100, 'visibility': 3478, 'wind_speed': 0.73, 'wind_deg': 105, 'wind_gust': 1.59, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 3.65}}, {'dt': 1644440400, 'temp': 10.46, 'feels_like': 9.99, 'pressure': 1014, 'humidity': 93, 'dew_point': 9.38, 'uvi': 1.96, 'clouds': 100, 'visibility': 3901, 'wind_speed': 0.72, 'wind_deg': 91, 'wind_gust': 1.51, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.37}}, {'dt': 1644444000, 'temp': 10.46, 'feels_like': 9.99, 'pressure': 1014, 'humidity': 93, 'dew_point': 9.38, 'uvi': 0.4, 'clouds': 98, 'visibility': 3450, 'wind_speed': 0.63, 'wind_deg': 78, 'wind_gust': 1.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644447600, 'temp': 10.46, 'feels_like': 10.12, 'pressure': 1015, 'humidity': 98, 'dew_point': 10.16, 'uvi': 0, 'clouds': 98, 'visibility': 1228, 'wind_speed': 0.78, 'wind_deg': 81, 'wind_gust': 1.37, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 00:00:00 | 100.000000 | 8.700000 | 9.460000 | 95.000000 | 1017.000000 |  | 9.460000 | 0.000000 | 10000.000000 | 130.000000 | 1.13 | 0.300000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 01:00:00 | 100.000000 | 7.550000 | 8.460000 | 94.000000 | 1018.000000 |  | 8.460000 | 0.000000 | 10000.000000 | 135.000000 | 1.19 | 0.490000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 02:00:00 | 100.000000 | 7.390000 | 8.460000 | 93.000000 | 1019.000000 |  | 8.460000 | 0.000000 | 10000.000000 | 119.000000 | 1.44 | 0.680000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 03:00:00 | 99.000000 | 5.260000 | 6.460000 | 92.000000 | 1020.000000 |  | 6.460000 | 0.000000 | 10000.000000 | 117.000000 | 1.49 | 0.790000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 04:00:00 | 95.000000 | 5.100000 | 6.460000 | 91.000000 | 1020.000000 |  | 6.460000 | 0.000000 | 10000.000000 | 121.000000 | 1.52 | 0.880000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 05:00:00 | 95.000000 | 5.100000 | 6.460000 | 91.000000 | 1019.000000 |  | 6.460000 | 0.000000 | 10000.000000 | 126.000000 | 1.44 | 0.710000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 06:00:00 | 71.000000 | 4.270000 | 5.460000 | 92.000000 | 1018.000000 |  | 5.460000 | 0.000000 | 10000.000000 | 122.000000 | 1.14 | 0.600000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 07:00:00 | 84.000000 | 4.270000 | 5.460000 | 92.000000 | 1017.000000 |  | 5.460000 | 0.000000 | 10000.000000 | 123.000000 | 1.15 | 0.610000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 08:00:00 | 83.000000 | 5.260000 | 6.460000 | 92.000000 | 1017.000000 |  | 6.460000 | 0.000000 | 10000.000000 | 120.000000 | 1.18 | 0.510000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 09:00:00 | 84.000000 | 5.260000 | 6.460000 | 92.000000 | 1017.000000 |  | 6.460000 | 0.000000 | 10000.000000 | 117.000000 | 1.19 | 0.610000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 10:00:00 | 83.000000 | 5.260000 | 6.460000 | 92.000000 | 1017.000000 |  | 6.460000 | 0.000000 | 10000.000000 | 105.000000 | 1.32 | 0.580000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 11:00:00 | 83.000000 | 6.250000 | 7.460000 | 92.000000 | 1018.000000 |  | 7.460000 | 0.000000 | 10000.000000 | 104.000000 | 1.29 | 0.670000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 12:00:00 | 100.000000 | 5.930000 | 7.460000 | 90.000000 | 1018.000000 |  | 7.460000 | 0.150000 | 10000.000000 | 84.000000 | 1.43 | 0.690000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 13:00:00 | 100.000000 | 7.880000 | 9.750000 | 84.000000 | 1018.000000 |  | 10.460000 | 2.260000 | 10000.000000 | 85.000000 | 1.69 | 0.920000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 14:00:00 | 100.000000 | 9.480000 | 11.900000 | 82.000000 | 1018.000000 |  | 12.460000 | 5.320000 | 10000.000000 | 85.000000 | 1.76 | 0.710000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 15:00:00 | 100.000000 | 11.240000 | 14.080000 | 81.000000 | 1018.000000 |  | 14.460000 | 8.920000 | 10000.000000 | 83.000000 | 1.74 | 0.590000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 16:00:00 | 100.000000 | 12.950000 | 15.280000 | 85.000000 | 1018.000000 |  | 15.460000 | 11.890000 | 6984.000000 | 92.000000 | 1.73 | 0.740000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 17:00:00 | 100.000000 | 14.110000 | 16.410000 | 86.000000 | 1017.000000 |  | 16.460000 | 12.940000 | 5392.000000 | 105.000000 | 1.72 | 0.800000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 18:00:00 | 94.000000 | 14.820000 | 16.510000 | 90.000000 | 1016.000000 |  | 16.460000 | 11.760000 | 4225.000000 | 125.000000 | 1.88 | 0.640000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 19:00:00 | 99.000000 | 12.020000 | 13.240000 | 91.000000 | 1015.000000 | 1.15 | 13.460000 | 8.130000 | 4185.000000 | 116.000000 | 1.63 | 0.640000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 20:00:00 | 100.000000 | 12.190000 | 13.260000 | 92.000000 | 1014.000000 | 3.65 | 13.460000 | 4.750000 | 3478.000000 | 105.000000 | 1.59 | 0.730000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 21:00:00 | 100.000000 | 9.380000 | 9.990000 | 93.000000 | 1014.000000 | 2.37 | 10.460000 | 1.960000 | 3901.000000 | 91.000000 | 1.51 | 0.720000 | 501 | Rain | moderate rain | 10d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 22:00:00 | 98.000000 | 9.380000 | 9.990000 | 93.000000 | 1014.000000 |  | 10.460000 | 0.400000 | 3450.000000 | 78.000000 | 1.32 | 0.630000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-09 23:00:00 | 98.000000 | 10.160000 | 10.120000 | 98.000000 | 1015.000000 |  | 10.460000 | 0.000000 | 1228.000000 | 81.000000 | 1.37 | 0.780000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35027150_OWM_Clouds_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Clouds_20220211.png)
![CNE_IDEAM_Station35027150_OWM_Dewpoint_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Dewpoint_20220211.png)
![CNE_IDEAM_Station35027150_OWM_Feelslike_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Feelslike_20220211.png)
![CNE_IDEAM_Station35027150_OWM_Humidity_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Humidity_20220211.png)
![CNE_IDEAM_Station35027150_OWM_Pressure_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Pressure_20220211.png)
![CNE_IDEAM_Station35027150_OWM_Rain_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Rain_20220211.png)
![CNE_IDEAM_Station35027150_OWM_Temp_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Temp_20220211.png)
![CNE_IDEAM_Station35027150_OWM_UVI_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_UVI_20220211.png)
![CNE_IDEAM_Station35027150_OWM_Visibility_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Visibility_20220211.png)
![CNE_IDEAM_Station35027150_OWM_Winddeg_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Winddeg_20220211.png)
![CNE_IDEAM_Station35027150_OWM_Windgust_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Windgust_20220211.png)
![CNE_IDEAM_Station35027150_OWM_Windspeed_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Windspeed_20220211.png)

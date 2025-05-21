
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

* Current date time: 2022-02-13 07:30:06.495901
* Unix time to eval: 1644564606
* Days before (for historical data): 2
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220213.xls
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35027150_OWM_20220213.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220213.csv)

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
{'lat': 4.138, 'lon': -74.1738, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644564606, 'sunrise': 1644577903, 'sunset': 1644621019, 'temp': 7.46, 'feels_like': 7.46, 'pressure': 1015, 'humidity': 96, 'dew_point': 6.86, 'uvi': 0, 'clouds': 100, 'visibility': 8416, 'wind_speed': 0.6, 'wind_deg': 292, 'wind_gust': 0.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, 'hourly': [{'dt': 1644537600, 'temp': 10.46, 'feels_like': 10.04, 'pressure': 1015, 'humidity': 95, 'dew_point': 9.69, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.1, 'wind_deg': 65, 'wind_gust': 1.45, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644541200, 'temp': 9.46, 'feels_like': 9.46, 'pressure': 1016, 'humidity': 92, 'dew_point': 8.23, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 78, 'wind_gust': 1.25, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644544800, 'temp': 9.46, 'feels_like': 9.46, 'pressure': 1017, 'humidity': 93, 'dew_point': 8.39, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 78, 'wind_gust': 0.78, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644548400, 'temp': 9.46, 'feels_like': 9.46, 'pressure': 1017, 'humidity': 94, 'dew_point': 8.54, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 65, 'wind_gust': 0.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644552000, 'temp': 9.46, 'feels_like': 9.46, 'pressure': 1017, 'humidity': 94, 'dew_point': 8.54, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 42, 'wind_gust': 0.87, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644555600, 'temp': 8.46, 'feels_like': 8.46, 'pressure': 1016, 'humidity': 95, 'dew_point': 7.71, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 27, 'wind_gust': 0.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644559200, 'temp': 8.46, 'feels_like': 8.46, 'pressure': 1016, 'humidity': 95, 'dew_point': 7.71, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 10, 'wind_gust': 0.64, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644562800, 'temp': 7.46, 'feels_like': 7.46, 'pressure': 1015, 'humidity': 95, 'dew_point': 6.71, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 308, 'wind_gust': 0.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644566400, 'temp': 7.46, 'feels_like': 7.46, 'pressure': 1015, 'humidity': 96, 'dew_point': 6.86, 'uvi': 0, 'clouds': 100, 'visibility': 8416, 'wind_speed': 0.6, 'wind_deg': 292, 'wind_gust': 0.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644570000, 'temp': 7.46, 'feels_like': 7.46, 'pressure': 1015, 'humidity': 97, 'dew_point': 7.02, 'uvi': 0, 'clouds': 100, 'visibility': 7528, 'wind_speed': 0.64, 'wind_deg': 310, 'wind_gust': 1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644573600, 'temp': 6.46, 'feels_like': 6.46, 'pressure': 1015, 'humidity': 96, 'dew_point': 5.87, 'uvi': 0, 'clouds': 100, 'visibility': 6595, 'wind_speed': 0.57, 'wind_deg': 311, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644577200, 'temp': 6.46, 'feels_like': 6.46, 'pressure': 1016, 'humidity': 95, 'dew_point': 5.72, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 305, 'wind_gust': 0.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644580800, 'temp': 7.46, 'feels_like': 7.46, 'pressure': 1017, 'humidity': 93, 'dew_point': 6.4, 'uvi': 0.44, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 1, 'wind_gust': 0.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644584400, 'temp': 11.46, 'feels_like': 10.99, 'pressure': 1017, 'humidity': 89, 'dew_point': 9.71, 'uvi': 2.45, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 48, 'wind_gust': 1.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644588000, 'temp': 13.46, 'feels_like': 13.05, 'pressure': 1017, 'humidity': 84, 'dew_point': 10.81, 'uvi': 5.78, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 44, 'wind_gust': 1.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644591600, 'temp': 14.46, 'feels_like': 14, 'pressure': 1016, 'humidity': 78, 'dew_point': 10.68, 'uvi': 9.69, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 38, 'wind_gust': 1.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644595200, 'temp': 15.46, 'feels_like': 14.99, 'pressure': 1015, 'humidity': 74, 'dew_point': 10.85, 'uvi': 12.74, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 21, 'wind_gust': 2.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644598800, 'temp': 17.46, 'feels_like': 17.22, 'pressure': 1014, 'humidity': 75, 'dew_point': 12.99, 'uvi': 13.86, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 20, 'wind_gust': 2.41, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644602400, 'temp': 16.46, 'feels_like': 16.2, 'pressure': 1013, 'humidity': 78, 'dew_point': 12.62, 'uvi': 12.6, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 11, 'wind_gust': 2.24, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644606000, 'temp': 17.46, 'feels_like': 17.45, 'pressure': 1012, 'humidity': 84, 'dew_point': 14.73, 'uvi': 8.92, 'clouds': 93, 'visibility': 6171, 'wind_speed': 0.48, 'wind_deg': 10, 'wind_gust': 2.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644609600, 'temp': 17.46, 'feels_like': 17.69, 'pressure': 1012, 'humidity': 93, 'dew_point': 16.32, 'uvi': 5.22, 'clouds': 97, 'visibility': 4020, 'wind_speed': 0.32, 'wind_deg': 337, 'wind_gust': 1.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644613200, 'temp': 14.46, 'feels_like': 14.47, 'pressure': 1012, 'humidity': 96, 'dew_point': 13.83, 'uvi': 2.15, 'clouds': 98, 'visibility': 835, 'wind_speed': 0.32, 'wind_deg': 332, 'wind_gust': 1.62, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644616800, 'temp': 14.46, 'feels_like': 14.49, 'pressure': 1013, 'humidity': 97, 'dew_point': 13.99, 'uvi': 0.5, 'clouds': 98, 'visibility': 153, 'wind_speed': 0.3, 'wind_deg': 28, 'wind_gust': 1.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644620400, 'temp': 13.46, 'feels_like': 13.42, 'pressure': 1014, 'humidity': 98, 'dew_point': 13.15, 'uvi': 0, 'clouds': 99, 'visibility': 145, 'wind_speed': 0.49, 'wind_deg': 62, 'wind_gust': 1.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 00:00:00 | 72.000000 | 9.690000 | 10.040000 | 95.000000 | 1015.000000 |  | 10.460000 | 0.000000 | 10000.000000 | 65.000000 | 1.45 | 1.100000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 01:00:00 | 84.000000 | 8.230000 | 9.460000 | 92.000000 | 1016.000000 |  | 9.460000 | 0.000000 | 10000.000000 | 78.000000 | 1.25 | 0.920000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 02:00:00 | 83.000000 | 8.390000 | 9.460000 | 93.000000 | 1017.000000 |  | 9.460000 | 0.000000 | 10000.000000 | 78.000000 | 0.78 | 0.560000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 03:00:00 | 79.000000 | 8.540000 | 9.460000 | 94.000000 | 1017.000000 |  | 9.460000 | 0.000000 | 10000.000000 | 65.000000 | 0.76 | 0.550000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 04:00:00 | 82.000000 | 8.540000 | 9.460000 | 94.000000 | 1017.000000 |  | 9.460000 | 0.000000 | 10000.000000 | 42.000000 | 0.87 | 0.610000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 05:00:00 | 85.000000 | 7.710000 | 8.460000 | 95.000000 | 1016.000000 |  | 8.460000 | 0.000000 | 10000.000000 | 27.000000 | 0.79 | 0.510000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 06:00:00 | 98.000000 | 7.710000 | 8.460000 | 95.000000 | 1016.000000 |  | 8.460000 | 0.000000 | 10000.000000 | 10.000000 | 0.64 | 0.240000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 07:00:00 | 100.000000 | 6.710000 | 7.460000 | 95.000000 | 1015.000000 |  | 7.460000 | 0.000000 | 10000.000000 | 308.000000 | 0.69 | 0.230000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 08:00:00 | 100.000000 | 6.860000 | 7.460000 | 96.000000 | 1015.000000 |  | 7.460000 | 0.000000 | 8416.000000 | 292.000000 | 0.82 | 0.600000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 09:00:00 | 100.000000 | 7.020000 | 7.460000 | 97.000000 | 1015.000000 |  | 7.460000 | 0.000000 | 7528.000000 | 310.000000 | 1 | 0.640000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 10:00:00 | 100.000000 | 5.870000 | 6.460000 | 96.000000 | 1015.000000 |  | 6.460000 | 0.000000 | 6595.000000 | 311.000000 | 0.95 | 0.570000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 11:00:00 | 99.000000 | 5.720000 | 6.460000 | 95.000000 | 1016.000000 |  | 6.460000 | 0.000000 | 10000.000000 | 305.000000 | 0.78 | 0.530000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 12:00:00 | 97.000000 | 6.400000 | 7.460000 | 93.000000 | 1017.000000 |  | 7.460000 | 0.440000 | 10000.000000 | 1.000000 | 0.92 | 0.470000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 13:00:00 | 100.000000 | 9.710000 | 10.990000 | 89.000000 | 1017.000000 |  | 11.460000 | 2.450000 | 10000.000000 | 48.000000 | 1.2 | 0.710000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 14:00:00 | 95.000000 | 10.810000 | 13.050000 | 84.000000 | 1017.000000 |  | 13.460000 | 5.780000 | 10000.000000 | 44.000000 | 1.44 | 0.820000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 15:00:00 | 88.000000 | 10.680000 | 14.000000 | 78.000000 | 1016.000000 |  | 14.460000 | 9.690000 | 10000.000000 | 38.000000 | 1.84 | 0.880000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 16:00:00 | 86.000000 | 10.850000 | 14.990000 | 74.000000 | 1015.000000 |  | 15.460000 | 12.740000 | 10000.000000 | 21.000000 | 2.11 | 0.890000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 17:00:00 | 84.000000 | 12.990000 | 17.220000 | 75.000000 | 1014.000000 |  | 17.460000 | 13.860000 | 10000.000000 | 20.000000 | 2.41 | 0.930000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 18:00:00 | 81.000000 | 12.620000 | 16.200000 | 78.000000 | 1013.000000 |  | 16.460000 | 12.600000 | 10000.000000 | 11.000000 | 2.24 | 0.690000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 19:00:00 | 93.000000 | 14.730000 | 17.450000 | 84.000000 | 1012.000000 |  | 17.460000 | 8.920000 | 6171.000000 | 10.000000 | 2.07 | 0.480000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 20:00:00 | 97.000000 | 16.320000 | 17.690000 | 93.000000 | 1012.000000 |  | 17.460000 | 5.220000 | 4020.000000 | 337.000000 | 1.84 | 0.320000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 21:00:00 | 98.000000 | 13.830000 | 14.470000 | 96.000000 | 1012.000000 |  | 14.460000 | 2.150000 | 835.000000 | 332.000000 | 1.62 | 0.320000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 22:00:00 | 98.000000 | 13.990000 | 14.490000 | 97.000000 | 1013.000000 |  | 14.460000 | 0.500000 | 153.000000 | 28.000000 | 1.5 | 0.300000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 23:00:00 | 99.000000 | 13.150000 | 13.420000 | 98.000000 | 1014.000000 |  | 13.460000 | 0.000000 | 145.000000 | 62.000000 | 1.11 | 0.490000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35027150_OWM_Clouds_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Clouds_20220213.png)
![CNE_IDEAM_Station35027150_OWM_Dewpoint_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Dewpoint_20220213.png)
![CNE_IDEAM_Station35027150_OWM_Feelslike_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Feelslike_20220213.png)
![CNE_IDEAM_Station35027150_OWM_Humidity_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Humidity_20220213.png)
![CNE_IDEAM_Station35027150_OWM_Pressure_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Pressure_20220213.png)
![CNE_IDEAM_Station35027150_OWM_Rain_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Rain_20220213.png)
![CNE_IDEAM_Station35027150_OWM_Temp_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Temp_20220213.png)
![CNE_IDEAM_Station35027150_OWM_UVI_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_UVI_20220213.png)
![CNE_IDEAM_Station35027150_OWM_Visibility_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Visibility_20220213.png)
![CNE_IDEAM_Station35027150_OWM_Winddeg_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Winddeg_20220213.png)
![CNE_IDEAM_Station35027150_OWM_Windgust_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Windgust_20220213.png)
![CNE_IDEAM_Station35027150_OWM_Windspeed_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Windspeed_20220213.png)

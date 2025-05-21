
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201240_OWM_20220213.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220213.csv)

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
{'lat': 4.4813, 'lon': -74.1263, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644564606, 'sunrise': 1644577912, 'sunset': 1644620987, 'temp': 9.14, 'feels_like': 9.14, 'pressure': 1014, 'humidity': 91, 'dew_point': 7.75, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 217, 'wind_gust': 0.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, 'hourly': [{'dt': 1644537600, 'temp': 11.4, 'feels_like': 11.02, 'pressure': 1014, 'humidity': 93, 'dew_point': 10.31, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 107, 'wind_gust': 1.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644541200, 'temp': 11.16, 'feels_like': 10.71, 'pressure': 1015, 'humidity': 91, 'dew_point': 9.75, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 111, 'wind_gust': 1.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644544800, 'temp': 11.14, 'feels_like': 10.66, 'pressure': 1016, 'humidity': 90, 'dew_point': 9.56, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 110, 'wind_gust': 1.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644548400, 'temp': 10.45, 'feels_like': 9.93, 'pressure': 1016, 'humidity': 91, 'dew_point': 9.05, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 115, 'wind_gust': 1.43, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644552000, 'temp': 10.09, 'feels_like': 9.53, 'pressure': 1016, 'humidity': 91, 'dew_point': 8.69, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 121, 'wind_gust': 1.39, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644555600, 'temp': 9.99, 'feels_like': 9.99, 'pressure': 1016, 'humidity': 91, 'dew_point': 8.59, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 118, 'wind_gust': 1.26, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644559200, 'temp': 9.83, 'feels_like': 9.83, 'pressure': 1015, 'humidity': 91, 'dew_point': 8.43, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 140, 'wind_gust': 1.2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644562800, 'temp': 9.14, 'feels_like': 9.14, 'pressure': 1014, 'humidity': 90, 'dew_point': 7.59, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 158, 'wind_gust': 1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644566400, 'temp': 9.14, 'feels_like': 9.14, 'pressure': 1014, 'humidity': 91, 'dew_point': 7.75, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 217, 'wind_gust': 0.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644570000, 'temp': 9.14, 'feels_like': 9.14, 'pressure': 1014, 'humidity': 91, 'dew_point': 7.75, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 246, 'wind_gust': 0.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644573600, 'temp': 8.14, 'feels_like': 8.14, 'pressure': 1014, 'humidity': 91, 'dew_point': 6.76, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 276, 'wind_gust': 0.53, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644577200, 'temp': 8.14, 'feels_like': 8.14, 'pressure': 1015, 'humidity': 90, 'dew_point': 6.6, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 258, 'wind_gust': 0.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644580800, 'temp': 9.14, 'feels_like': 9.14, 'pressure': 1015, 'humidity': 86, 'dew_point': 6.92, 'uvi': 0.44, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 49, 'wind_gust': 0.67, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644584400, 'temp': 13.14, 'feels_like': 12.65, 'pressure': 1016, 'humidity': 82, 'dew_point': 10.14, 'uvi': 2.45, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 115, 'wind_gust': 1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644588000, 'temp': 15.14, 'feels_like': 14.69, 'pressure': 1016, 'humidity': 76, 'dew_point': 10.94, 'uvi': 5.78, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 134, 'wind_gust': 1.26, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644591600, 'temp': 16.14, 'feels_like': 15.59, 'pressure': 1015, 'humidity': 68, 'dew_point': 10.24, 'uvi': 9.69, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 131, 'wind_gust': 1.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644595200, 'temp': 17.14, 'feels_like': 16.55, 'pressure': 1013, 'humidity': 63, 'dew_point': 10.05, 'uvi': 12.74, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 324, 'wind_gust': 1.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644598800, 'temp': 19.14, 'feels_like': 18.78, 'pressure': 1012, 'humidity': 64, 'dew_point': 12.18, 'uvi': 13.86, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 340, 'wind_gust': 2.48, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644602400, 'temp': 18.14, 'feels_like': 17.84, 'pressure': 1012, 'humidity': 70, 'dew_point': 12.59, 'uvi': 12.6, 'clouds': 66, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 328, 'wind_gust': 2.46, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644606000, 'temp': 19.14, 'feels_like': 19.04, 'pressure': 1011, 'humidity': 74, 'dew_point': 14.4, 'uvi': 8.92, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 316, 'wind_gust': 2.12, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644609600, 'temp': 19.14, 'feels_like': 19.15, 'pressure': 1010, 'humidity': 78, 'dew_point': 15.22, 'uvi': 5.22, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 235, 'wind_gust': 1.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644613200, 'temp': 16.14, 'feels_like': 15.95, 'pressure': 1011, 'humidity': 82, 'dew_point': 13.07, 'uvi': 2.15, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 205, 'wind_gust': 1.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644616800, 'temp': 16.14, 'feels_like': 16.16, 'pressure': 1012, 'humidity': 90, 'dew_point': 14.5, 'uvi': 0.5, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 182, 'wind_gust': 1.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644620400, 'temp': 15.14, 'feels_like': 15.22, 'pressure': 1013, 'humidity': 96, 'dew_point': 14.51, 'uvi': 0, 'clouds': 89, 'visibility': 1786, 'wind_speed': 0.58, 'wind_deg': 128, 'wind_gust': 1.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 00:00:00 | 80.000000 | 10.310000 | 11.020000 | 93.000000 | 1014.000000 |  | 11.400000 | 0.000000 | 10000.000000 | 107.000000 | 1.61 | 1.300000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 01:00:00 | 96.000000 | 9.750000 | 10.710000 | 91.000000 | 1015.000000 |  | 11.160000 | 0.000000 | 10000.000000 | 111.000000 | 1.69 | 1.220000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 02:00:00 | 93.000000 | 9.560000 | 10.660000 | 90.000000 | 1016.000000 |  | 11.140000 | 0.000000 | 10000.000000 | 110.000000 | 1.3 | 0.880000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 03:00:00 | 89.000000 | 9.050000 | 9.930000 | 91.000000 | 1016.000000 |  | 10.450000 | 0.000000 | 10000.000000 | 115.000000 | 1.43 | 0.950000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 04:00:00 | 79.000000 | 8.690000 | 9.530000 | 91.000000 | 1016.000000 |  | 10.090000 | 0.000000 | 10000.000000 | 121.000000 | 1.39 | 0.960000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 05:00:00 | 78.000000 | 8.590000 | 9.990000 | 91.000000 | 1016.000000 |  | 9.990000 | 0.000000 | 10000.000000 | 118.000000 | 1.26 | 0.950000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 06:00:00 | 72.000000 | 8.430000 | 9.830000 | 91.000000 | 1015.000000 |  | 9.830000 | 0.000000 | 10000.000000 | 140.000000 | 1.2 | 0.780000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 07:00:00 | 90.000000 | 7.590000 | 9.140000 | 90.000000 | 1014.000000 |  | 9.140000 | 0.000000 | 10000.000000 | 158.000000 | 1 | 0.650000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 08:00:00 | 95.000000 | 7.750000 | 9.140000 | 91.000000 | 1014.000000 |  | 9.140000 | 0.000000 | 10000.000000 | 217.000000 | 0.66 | 0.270000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 09:00:00 | 97.000000 | 7.750000 | 9.140000 | 91.000000 | 1014.000000 |  | 9.140000 | 0.000000 | 10000.000000 | 246.000000 | 0.72 | 0.240000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 10:00:00 | 97.000000 | 6.760000 | 8.140000 | 91.000000 | 1014.000000 |  | 8.140000 | 0.000000 | 10000.000000 | 276.000000 | 0.53 | 0.250000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 11:00:00 | 97.000000 | 6.600000 | 8.140000 | 90.000000 | 1015.000000 |  | 8.140000 | 0.000000 | 10000.000000 | 258.000000 | 0.48 | 0.360000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 12:00:00 | 79.000000 | 6.920000 | 9.140000 | 86.000000 | 1015.000000 |  | 9.140000 | 0.440000 | 10000.000000 | 49.000000 | 0.67 | 0.240000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 13:00:00 | 92.000000 | 10.140000 | 12.650000 | 82.000000 | 1016.000000 |  | 13.140000 | 2.450000 | 10000.000000 | 115.000000 | 1 | 0.370000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 14:00:00 | 91.000000 | 10.940000 | 14.690000 | 76.000000 | 1016.000000 |  | 15.140000 | 5.780000 | 10000.000000 | 134.000000 | 1.26 | 0.570000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 15:00:00 | 91.000000 | 10.240000 | 15.590000 | 68.000000 | 1015.000000 |  | 16.140000 | 9.690000 | 10000.000000 | 131.000000 | 1.74 | 0.210000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 16:00:00 | 87.000000 | 10.050000 | 16.550000 | 63.000000 | 1013.000000 |  | 17.140000 | 12.740000 | 10000.000000 | 324.000000 | 1.85 | 0.340000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 17:00:00 | 80.000000 | 12.180000 | 18.780000 | 64.000000 | 1012.000000 |  | 19.140000 | 13.860000 | 10000.000000 | 340.000000 | 2.48 | 0.460000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 18:00:00 | 66.000000 | 12.590000 | 17.840000 | 70.000000 | 1012.000000 |  | 18.140000 | 12.600000 | 10000.000000 | 328.000000 | 2.46 | 0.600000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 19:00:00 | 81.000000 | 14.400000 | 19.040000 | 74.000000 | 1011.000000 |  | 19.140000 | 8.920000 | 10000.000000 | 316.000000 | 2.12 | 0.320000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 20:00:00 | 85.000000 | 15.220000 | 19.150000 | 78.000000 | 1010.000000 |  | 19.140000 | 5.220000 | 10000.000000 | 235.000000 | 1.87 | 0.420000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 21:00:00 | 87.000000 | 13.070000 | 15.950000 | 82.000000 | 1011.000000 |  | 16.140000 | 2.150000 | 10000.000000 | 205.000000 | 1.58 | 0.570000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 22:00:00 | 89.000000 | 14.500000 | 16.160000 | 90.000000 | 1012.000000 |  | 16.140000 | 0.500000 | 10000.000000 | 182.000000 | 1.84 | 0.400000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 23:00:00 | 89.000000 | 14.510000 | 15.220000 | 96.000000 | 1013.000000 |  | 15.140000 | 0.000000 | 1786.000000 | 128.000000 | 1.39 | 0.580000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21201240_OWM_Clouds_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Clouds_20220213.png)
![CNE_IDEAM_Station21201240_OWM_Dewpoint_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Dewpoint_20220213.png)
![CNE_IDEAM_Station21201240_OWM_Feelslike_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Feelslike_20220213.png)
![CNE_IDEAM_Station21201240_OWM_Humidity_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Humidity_20220213.png)
![CNE_IDEAM_Station21201240_OWM_Pressure_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Pressure_20220213.png)
![CNE_IDEAM_Station21201240_OWM_Rain_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Rain_20220213.png)
![CNE_IDEAM_Station21201240_OWM_Temp_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Temp_20220213.png)
![CNE_IDEAM_Station21201240_OWM_UVI_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_UVI_20220213.png)
![CNE_IDEAM_Station21201240_OWM_Visibility_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Visibility_20220213.png)
![CNE_IDEAM_Station21201240_OWM_Winddeg_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Winddeg_20220213.png)
![CNE_IDEAM_Station21201240_OWM_Windgust_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Windgust_20220213.png)
![CNE_IDEAM_Station21201240_OWM_Windspeed_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Windspeed_20220213.png)

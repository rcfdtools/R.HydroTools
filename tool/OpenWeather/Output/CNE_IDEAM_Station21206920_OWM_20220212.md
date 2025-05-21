
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

* Current date time: 2022-02-12 11:35:00.628114
* Unix time to eval: 1644579300
* Days before (for historical data): 1
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220212.xls
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206920_OWM_20220212.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220212.csv)

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
{'lat': 4.35, 'lon': -74.15, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644579300, 'sunrise': 1644577910, 'sunset': 1644621001, 'temp': 3.9, 'feels_like': 3.9, 'pressure': 1016, 'humidity': 88, 'dew_point': 2.1, 'uvi': 0.44, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 11, 'wind_gust': 0.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644537600, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1014, 'humidity': 93, 'dew_point': 6.31, 'uvi': 0, 'clouds': 69, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 91, 'wind_gust': 1.41, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644541200, 'temp': 7.12, 'feels_like': 7.12, 'pressure': 1015, 'humidity': 91, 'dew_point': 5.75, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 104, 'wind_gust': 1.32, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644544800, 'temp': 6.88, 'feels_like': 6.88, 'pressure': 1016, 'humidity': 90, 'dew_point': 5.36, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 111, 'wind_gust': 0.92, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644548400, 'temp': 6.47, 'feels_like': 6.47, 'pressure': 1017, 'humidity': 91, 'dew_point': 5.11, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 109, 'wind_gust': 0.91, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644552000, 'temp': 6.26, 'feels_like': 6.26, 'pressure': 1017, 'humidity': 92, 'dew_point': 5.06, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 108, 'wind_gust': 0.97, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644555600, 'temp': 6.21, 'feels_like': 6.21, 'pressure': 1016, 'humidity': 92, 'dew_point': 5.01, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 109, 'wind_gust': 0.89, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644559200, 'temp': 5.96, 'feels_like': 5.96, 'pressure': 1015, 'humidity': 92, 'dew_point': 4.76, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 139, 'wind_gust': 0.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644562800, 'temp': 4.9, 'feels_like': 4.9, 'pressure': 1014, 'humidity': 92, 'dew_point': 3.71, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 179, 'wind_gust': 0.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644566400, 'temp': 4.9, 'feels_like': 4.9, 'pressure': 1014, 'humidity': 93, 'dew_point': 3.86, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 254, 'wind_gust': 0.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644570000, 'temp': 4.9, 'feels_like': 4.9, 'pressure': 1014, 'humidity': 94, 'dew_point': 4.02, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 272, 'wind_gust': 0.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644573600, 'temp': 3.9, 'feels_like': 3.9, 'pressure': 1015, 'humidity': 93, 'dew_point': 2.87, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 276, 'wind_gust': 0.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644577200, 'temp': 3.9, 'feels_like': 3.9, 'pressure': 1015, 'humidity': 92, 'dew_point': 2.72, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 270, 'wind_gust': 0.64, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644580800, 'temp': 4.9, 'feels_like': 4.9, 'pressure': 1016, 'humidity': 88, 'dew_point': 3.08, 'uvi': 0.44, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 11, 'wind_gust': 0.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644584400, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1016, 'humidity': 84, 'dew_point': 6.35, 'uvi': 2.45, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 70, 'wind_gust': 1.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644588000, 'temp': 10.9, 'feels_like': 10.11, 'pressure': 1016, 'humidity': 79, 'dew_point': 7.41, 'uvi': 5.78, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 63, 'wind_gust': 1.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644591600, 'temp': 11.9, 'feels_like': 11.03, 'pressure': 1016, 'humidity': 72, 'dew_point': 7.02, 'uvi': 9.69, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 28, 'wind_gust': 1.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644595200, 'temp': 12.9, 'feels_like': 12.05, 'pressure': 1014, 'humidity': 69, 'dew_point': 7.36, 'uvi': 12.74, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 356, 'wind_gust': 2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644598800, 'temp': 14.9, 'feels_like': 14.3, 'pressure': 1013, 'humidity': 71, 'dew_point': 9.7, 'uvi': 13.86, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 355, 'wind_gust': 2.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644602400, 'temp': 13.9, 'feels_like': 13.33, 'pressure': 1012, 'humidity': 76, 'dew_point': 9.74, 'uvi': 12.6, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 338, 'wind_gust': 2.49, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644606000, 'temp': 14.9, 'feels_like': 14.56, 'pressure': 1011, 'humidity': 81, 'dew_point': 11.67, 'uvi': 8.92, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 332, 'wind_gust': 2.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644609600, 'temp': 14.9, 'feels_like': 14.77, 'pressure': 1011, 'humidity': 89, 'dew_point': 13.1, 'uvi': 5.22, 'clouds': 93, 'visibility': 9537, 'wind_speed': 0.46, 'wind_deg': 283, 'wind_gust': 1.93, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644613200, 'temp': 11.9, 'feels_like': 11.52, 'pressure': 1012, 'humidity': 91, 'dew_point': 10.48, 'uvi': 2.15, 'clouds': 94, 'visibility': 4491, 'wind_speed': 0.32, 'wind_deg': 261, 'wind_gust': 1.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644616800, 'temp': 11.9, 'feels_like': 11.63, 'pressure': 1012, 'humidity': 95, 'dew_point': 11.13, 'uvi': 0.5, 'clouds': 95, 'visibility': 3751, 'wind_speed': 0.04, 'wind_deg': 166, 'wind_gust': 1.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644620400, 'temp': 10.9, 'feels_like': 10.6, 'pressure': 1014, 'humidity': 98, 'dew_point': 10.6, 'uvi': 0, 'clouds': 95, 'visibility': 958, 'wind_speed': 0.44, 'wind_deg': 93, 'wind_gust': 1.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 00:00:00 | 69.000000 | 6.310000 | 7.370000 | 93.000000 | 1014.000000 |  | 7.370000 | 0.000000 | 10000.000000 | 91.000000 | 1.41 | 1.140000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 01:00:00 | 84.000000 | 5.750000 | 7.120000 | 91.000000 | 1015.000000 |  | 7.120000 | 0.000000 | 10000.000000 | 104.000000 | 1.32 | 1.000000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 02:00:00 | 84.000000 | 5.360000 | 6.880000 | 90.000000 | 1016.000000 |  | 6.880000 | 0.000000 | 10000.000000 | 111.000000 | 0.92 | 0.590000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 03:00:00 | 80.000000 | 5.110000 | 6.470000 | 91.000000 | 1017.000000 |  | 6.470000 | 0.000000 | 10000.000000 | 109.000000 | 0.91 | 0.520000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 04:00:00 | 78.000000 | 5.060000 | 6.260000 | 92.000000 | 1017.000000 |  | 6.260000 | 0.000000 | 10000.000000 | 108.000000 | 0.97 | 0.530000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 05:00:00 | 80.000000 | 5.010000 | 6.210000 | 92.000000 | 1016.000000 |  | 6.210000 | 0.000000 | 10000.000000 | 109.000000 | 0.89 | 0.480000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 06:00:00 | 86.000000 | 4.760000 | 5.960000 | 92.000000 | 1015.000000 |  | 5.960000 | 0.000000 | 10000.000000 | 139.000000 | 0.79 | 0.360000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 07:00:00 | 95.000000 | 3.710000 | 4.900000 | 92.000000 | 1014.000000 |  | 4.900000 | 0.000000 | 10000.000000 | 179.000000 | 0.78 | 0.370000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 08:00:00 | 98.000000 | 3.860000 | 4.900000 | 93.000000 | 1014.000000 |  | 4.900000 | 0.000000 | 10000.000000 | 254.000000 | 0.66 | 0.400000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 09:00:00 | 98.000000 | 4.020000 | 4.900000 | 94.000000 | 1014.000000 |  | 4.900000 | 0.000000 | 10000.000000 | 272.000000 | 0.82 | 0.430000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 10:00:00 | 99.000000 | 2.870000 | 3.900000 | 93.000000 | 1015.000000 |  | 3.900000 | 0.000000 | 10000.000000 | 276.000000 | 0.7 | 0.450000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 11:00:00 | 98.000000 | 2.720000 | 3.900000 | 92.000000 | 1015.000000 |  | 3.900000 | 0.000000 | 10000.000000 | 270.000000 | 0.64 | 0.510000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 12:00:00 | 89.000000 | 3.080000 | 4.900000 | 88.000000 | 1016.000000 |  | 4.900000 | 0.440000 | 10000.000000 | 11.000000 | 0.78 | 0.270000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 13:00:00 | 97.000000 | 6.350000 | 8.900000 | 84.000000 | 1016.000000 |  | 8.900000 | 2.450000 | 10000.000000 | 70.000000 | 1.03 | 0.460000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 14:00:00 | 95.000000 | 7.410000 | 10.110000 | 79.000000 | 1016.000000 |  | 10.900000 | 5.780000 | 10000.000000 | 63.000000 | 1.32 | 0.440000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 15:00:00 | 90.000000 | 7.020000 | 11.030000 | 72.000000 | 1016.000000 |  | 11.900000 | 9.690000 | 10000.000000 | 28.000000 | 1.83 | 0.520000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 16:00:00 | 86.000000 | 7.360000 | 12.050000 | 69.000000 | 1014.000000 |  | 12.900000 | 12.740000 | 10000.000000 | 356.000000 | 2 | 0.720000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 17:00:00 | 83.000000 | 9.700000 | 14.300000 | 71.000000 | 1013.000000 |  | 14.900000 | 13.860000 | 10000.000000 | 355.000000 | 2.56 | 0.810000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 18:00:00 | 77.000000 | 9.740000 | 13.330000 | 76.000000 | 1012.000000 |  | 13.900000 | 12.600000 | 10000.000000 | 338.000000 | 2.49 | 0.790000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 19:00:00 | 90.000000 | 11.670000 | 14.560000 | 81.000000 | 1011.000000 |  | 14.900000 | 8.920000 | 10000.000000 | 332.000000 | 2.24 | 0.550000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 20:00:00 | 93.000000 | 13.100000 | 14.770000 | 89.000000 | 1011.000000 |  | 14.900000 | 5.220000 | 9537.000000 | 283.000000 | 1.93 | 0.460000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 21:00:00 | 94.000000 | 10.480000 | 11.520000 | 91.000000 | 1012.000000 |  | 11.900000 | 2.150000 | 4491.000000 | 261.000000 | 1.68 | 0.320000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 22:00:00 | 95.000000 | 11.130000 | 11.630000 | 95.000000 | 1012.000000 |  | 11.900000 | 0.500000 | 3751.000000 | 166.000000 | 1.7 | 0.040000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 23:00:00 | 95.000000 | 10.600000 | 10.600000 | 98.000000 | 1014.000000 |  | 10.900000 | 0.000000 | 958.000000 | 93.000000 | 1.21 | 0.440000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21206920_OWM_Clouds_20220212.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Clouds_20220212.png)
![CNE_IDEAM_Station21206920_OWM_Dewpoint_20220212.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Dewpoint_20220212.png)
![CNE_IDEAM_Station21206920_OWM_Feelslike_20220212.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Feelslike_20220212.png)
![CNE_IDEAM_Station21206920_OWM_Humidity_20220212.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Humidity_20220212.png)
![CNE_IDEAM_Station21206920_OWM_Pressure_20220212.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Pressure_20220212.png)
![CNE_IDEAM_Station21206920_OWM_Rain_20220212.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Rain_20220212.png)
![CNE_IDEAM_Station21206920_OWM_Temp_20220212.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Temp_20220212.png)
![CNE_IDEAM_Station21206920_OWM_UVI_20220212.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_UVI_20220212.png)
![CNE_IDEAM_Station21206920_OWM_Visibility_20220212.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Visibility_20220212.png)
![CNE_IDEAM_Station21206920_OWM_Winddeg_20220212.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Winddeg_20220212.png)
![CNE_IDEAM_Station21206920_OWM_Windgust_20220212.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Windgust_20220212.png)
![CNE_IDEAM_Station21206920_OWM_Windspeed_20220212.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Windspeed_20220212.png)

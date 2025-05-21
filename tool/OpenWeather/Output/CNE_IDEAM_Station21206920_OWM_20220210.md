
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

* Current date time: 2022-02-10 14:08:04.180886
* Unix time to eval: 1644329284
* Days before (for historical data): 2
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220210.xls
* CNE IDEAM file downloaded and updated: No
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206920_OWM_20220210.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220210.csv)

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
{'lat': 4.35, 'lon': -74.15, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644329284, 'sunrise': 1644318722, 'sunset': 1644361777, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1019, 'humidity': 87, 'dew_point': 6.86, 'uvi': 3.32, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 127, 'wind_gust': 1.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644278400, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1017, 'humidity': 93, 'dew_point': 7.83, 'uvi': 0, 'clouds': 100, 'visibility': 7680, 'wind_speed': 1.09, 'wind_deg': 119, 'wind_gust': 1.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644282000, 'temp': 8.9, 'feels_like': 8.54, 'pressure': 1017, 'humidity': 93, 'dew_point': 7.83, 'uvi': 0, 'clouds': 100, 'visibility': 9140, 'wind_speed': 1.37, 'wind_deg': 114, 'wind_gust': 2.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644285600, 'temp': 7.9, 'feels_like': 7.2, 'pressure': 1018, 'humidity': 93, 'dew_point': 6.84, 'uvi': 0, 'clouds': 100, 'visibility': 4488, 'wind_speed': 1.55, 'wind_deg': 105, 'wind_gust': 2.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644289200, 'temp': 7.9, 'feels_like': 7.34, 'pressure': 1019, 'humidity': 93, 'dew_point': 6.84, 'uvi': 0, 'clouds': 100, 'visibility': 3674, 'wind_speed': 1.43, 'wind_deg': 100, 'wind_gust': 2.17, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 3.16}}, {'dt': 1644292800, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1019, 'humidity': 94, 'dew_point': 7, 'uvi': 0, 'clouds': 100, 'visibility': 1852, 'wind_speed': 0.78, 'wind_deg': 116, 'wind_gust': 1.51, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.54}}, {'dt': 1644296400, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1018, 'humidity': 93, 'dew_point': 6.84, 'uvi': 0, 'clouds': 100, 'visibility': 7466, 'wind_speed': 0.27, 'wind_deg': 133, 'wind_gust': 1.14, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 2.37}}, {'dt': 1644300000, 'temp': 6.9, 'feels_like': 6.9, 'pressure': 1018, 'humidity': 95, 'dew_point': 6.16, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.07, 'wind_deg': 189, 'wind_gust': 0.88, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.78}}, {'dt': 1644303600, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1017, 'humidity': 94, 'dew_point': 7, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.18, 'wind_deg': 123, 'wind_gust': 0.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 1}}, {'dt': 1644307200, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1016, 'humidity': 93, 'dew_point': 6.84, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 225, 'wind_gust': 0.76, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.54}}, {'dt': 1644310800, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1016, 'humidity': 92, 'dew_point': 6.68, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 202, 'wind_gust': 0.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644314400, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1017, 'humidity': 92, 'dew_point': 6.68, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 129, 'wind_gust': 0.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644318000, 'temp': 6.9, 'feels_like': 6.9, 'pressure': 1017, 'humidity': 92, 'dew_point': 5.69, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 120, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644321600, 'temp': 6.9, 'feels_like': 6.9, 'pressure': 1018, 'humidity': 92, 'dew_point': 5.69, 'uvi': 0.07, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 116, 'wind_gust': 1.15, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644325200, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1018, 'humidity': 89, 'dew_point': 7.19, 'uvi': 1.41, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 95, 'wind_gust': 1.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644328800, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1019, 'humidity': 87, 'dew_point': 6.86, 'uvi': 3.32, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 127, 'wind_gust': 1.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644332400, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1018, 'humidity': 82, 'dew_point': 6.98, 'uvi': 5.57, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.12, 'wind_deg': 120, 'wind_gust': 1.75, 'weather': [{'id': 503, 'main': 'Rain', 'description': 'very heavy rain', 'icon': '10d'}], 'rain': {'1h': 20.5}}, {'dt': 1644336000, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1017, 'humidity': 85, 'dew_point': 5.54, 'uvi': 5.67, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 220, 'wind_gust': 1.8, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.73}}, {'dt': 1644339600, 'temp': 6.9, 'feels_like': 6.9, 'pressure': 1016, 'humidity': 89, 'dew_point': 5.22, 'uvi': 6.17, 'clouds': 98, 'visibility': 8511, 'wind_speed': 0.21, 'wind_deg': 112, 'wind_gust': 1.66, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 3.16}}, {'dt': 1644343200, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1016, 'humidity': 90, 'dew_point': 7.35, 'uvi': 5.61, 'clouds': 99, 'visibility': 6338, 'wind_speed': 0.23, 'wind_deg': 49, 'wind_gust': 1.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 1}}, {'dt': 1644346800, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1015, 'humidity': 91, 'dew_point': 8.5, 'uvi': 5.44, 'clouds': 100, 'visibility': 5685, 'wind_speed': 0.25, 'wind_deg': 26, 'wind_gust': 1.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644350400, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1015, 'humidity': 93, 'dew_point': 8.82, 'uvi': 3.18, 'clouds': 100, 'visibility': 4599, 'wind_speed': 0.15, 'wind_deg': 12, 'wind_gust': 1.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644354000, 'temp': 10.9, 'feels_like': 10.47, 'pressure': 1015, 'humidity': 93, 'dew_point': 9.81, 'uvi': 1.31, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 102, 'wind_gust': 1.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644357600, 'temp': 10.9, 'feels_like': 10.42, 'pressure': 1015, 'humidity': 91, 'dew_point': 9.49, 'uvi': 0.5, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 114, 'wind_gust': 1.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644361200, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1016, 'humidity': 95, 'dew_point': 9.14, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 129, 'wind_gust': 1.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 00:00:00 | 100.000000 | 7.830000 | 8.900000 | 93.000000 | 1017.000000 |  | 8.900000 | 0.000000 | 7680.000000 | 119.000000 | 1.85 | 1.090000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 01:00:00 | 100.000000 | 7.830000 | 8.540000 | 93.000000 | 1017.000000 |  | 8.900000 | 0.000000 | 9140.000000 | 114.000000 | 2.06 | 1.370000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 02:00:00 | 100.000000 | 6.840000 | 7.200000 | 93.000000 | 1018.000000 |  | 7.900000 | 0.000000 | 4488.000000 | 105.000000 | 2.34 | 1.550000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 03:00:00 | 100.000000 | 6.840000 | 7.340000 | 93.000000 | 1019.000000 | 3.16 | 7.900000 | 0.000000 | 3674.000000 | 100.000000 | 2.17 | 1.430000 | 501 | Rain | moderate rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 04:00:00 | 100.000000 | 7.000000 | 7.900000 | 94.000000 | 1019.000000 | 1.54 | 7.900000 | 0.000000 | 1852.000000 | 116.000000 | 1.51 | 0.780000 | 501 | Rain | moderate rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 05:00:00 | 100.000000 | 6.840000 | 7.900000 | 93.000000 | 1018.000000 | 2.37 | 7.900000 | 0.000000 | 7466.000000 | 133.000000 | 1.14 | 0.270000 | 501 | Rain | moderate rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 06:00:00 | 100.000000 | 6.160000 | 6.900000 | 95.000000 | 1018.000000 | 1.78 | 6.900000 | 0.000000 | 10000.000000 | 189.000000 | 0.88 | 0.070000 | 501 | Rain | moderate rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 07:00:00 | 100.000000 | 7.000000 | 7.900000 | 94.000000 | 1017.000000 | 1 | 7.900000 | 0.000000 | 10000.000000 | 123.000000 | 0.94 | 0.180000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 08:00:00 | 100.000000 | 6.840000 | 7.900000 | 93.000000 | 1016.000000 | 1.54 | 7.900000 | 0.000000 | 10000.000000 | 225.000000 | 0.76 | 0.200000 | 501 | Rain | moderate rain | 10n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 09:00:00 | 100.000000 | 6.680000 | 7.900000 | 92.000000 | 1016.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 202.000000 | 0.68 | 0.200000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 10:00:00 | 100.000000 | 6.680000 | 7.900000 | 92.000000 | 1017.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 129.000000 | 0.73 | 0.520000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 11:00:00 | 100.000000 | 5.690000 | 6.900000 | 92.000000 | 1017.000000 |  | 6.900000 | 0.000000 | 10000.000000 | 120.000000 | 0.95 | 0.570000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 12:00:00 | 100.000000 | 5.690000 | 6.900000 | 92.000000 | 1018.000000 |  | 6.900000 | 0.070000 | 10000.000000 | 116.000000 | 1.15 | 0.630000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 13:00:00 | 100.000000 | 7.190000 | 8.900000 | 89.000000 | 1018.000000 |  | 8.900000 | 1.410000 | 10000.000000 | 95.000000 | 1.5 | 0.670000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 14:00:00 | 96.000000 | 6.860000 | 8.900000 | 87.000000 | 1019.000000 |  | 8.900000 | 3.320000 | 10000.000000 | 127.000000 | 1.52 | 0.250000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 15:00:00 | 97.000000 | 6.980000 | 9.900000 | 82.000000 | 1018.000000 | 20.5 | 9.900000 | 5.570000 | 10000.000000 | 120.000000 | 1.75 | 0.120000 | 503 | Rain | very heavy rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 16:00:00 | 98.000000 | 5.540000 | 7.900000 | 85.000000 | 1017.000000 | 2.73 | 7.900000 | 5.670000 | 10000.000000 | 220.000000 | 1.8 | 0.240000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 17:00:00 | 98.000000 | 5.220000 | 6.900000 | 89.000000 | 1016.000000 | 3.16 | 6.900000 | 6.170000 | 8511.000000 | 112.000000 | 1.66 | 0.210000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 18:00:00 | 99.000000 | 7.350000 | 8.900000 | 90.000000 | 1016.000000 | 1 | 8.900000 | 5.610000 | 6338.000000 | 49.000000 | 1.34 | 0.230000 | 500 | Rain | light rain | 10d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 19:00:00 | 100.000000 | 8.500000 | 9.900000 | 91.000000 | 1015.000000 |  | 9.900000 | 5.440000 | 5685.000000 | 26.000000 | 1.21 | 0.250000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 20:00:00 | 100.000000 | 8.820000 | 9.900000 | 93.000000 | 1015.000000 |  | 9.900000 | 3.180000 | 4599.000000 | 12.000000 | 1.2 | 0.150000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 21:00:00 | 100.000000 | 9.810000 | 10.470000 | 93.000000 | 1015.000000 |  | 10.900000 | 1.310000 | 10000.000000 | 102.000000 | 1.34 | 0.270000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 22:00:00 | 100.000000 | 9.490000 | 10.420000 | 91.000000 | 1015.000000 |  | 10.900000 | 0.500000 | 10000.000000 | 114.000000 | 1.54 | 0.530000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 23:00:00 | 100.000000 | 9.140000 | 9.900000 | 95.000000 | 1016.000000 |  | 9.900000 | 0.000000 | 10000.000000 | 129.000000 | 1.2 | 0.320000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21206920_OWM_Clouds_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Clouds_20220210.png)
![CNE_IDEAM_Station21206920_OWM_Dewpoint_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Dewpoint_20220210.png)
![CNE_IDEAM_Station21206920_OWM_Feelslike_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Feelslike_20220210.png)
![CNE_IDEAM_Station21206920_OWM_Humidity_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Humidity_20220210.png)
![CNE_IDEAM_Station21206920_OWM_Pressure_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Pressure_20220210.png)
![CNE_IDEAM_Station21206920_OWM_Rain_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Rain_20220210.png)
![CNE_IDEAM_Station21206920_OWM_Temp_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Temp_20220210.png)
![CNE_IDEAM_Station21206920_OWM_UVI_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_UVI_20220210.png)
![CNE_IDEAM_Station21206920_OWM_Visibility_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Visibility_20220210.png)
![CNE_IDEAM_Station21206920_OWM_Winddeg_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Winddeg_20220210.png)
![CNE_IDEAM_Station21206920_OWM_Windgust_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Windgust_20220210.png)
![CNE_IDEAM_Station21206920_OWM_Windspeed_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Windspeed_20220210.png)

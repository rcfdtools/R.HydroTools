
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - COLEGIO SAN CAYETANO [21206650] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206650_OWM_20220210.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220210.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.51675278,-74.08822222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.51675278&lon=-74.08822222)

| Parameter | Value |
|---|---|
| Code | 21206650 |
| Name | COLEGIO SAN CAYETANO [21206650] |
| Latitude, ° | 4.51675278 |
| Longitude, ° | -74.08822222 |
| Elevation, m | 3100 |
| Category | Climática Ordinaria |
| Technology | Convencional |
| Status | Activa |
| Installation date | 2001-11-15 00:00:00 |
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

### (CNE index 3786) Open Weather values for station 21206650 - COLEGIO SAN CAYETANO [21206650]

JSON data from API OWM:

```
{'lat': 4.5168, 'lon': -74.0882, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644329284, 'sunrise': 1644318718, 'sunset': 1644361752, 'temp': 9.65, 'feels_like': 9.65, 'pressure': 1018, 'humidity': 83, 'dew_point': 6.91, 'uvi': 3.22, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 147, 'wind_gust': 1.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644278400, 'temp': 9.97, 'feels_like': 9.97, 'pressure': 1016, 'humidity': 93, 'dew_point': 8.89, 'uvi': 0, 'clouds': 100, 'visibility': 6821, 'wind_speed': 0.9, 'wind_deg': 138, 'wind_gust': 1.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644282000, 'temp': 9.97, 'feels_like': 9.97, 'pressure': 1017, 'humidity': 93, 'dew_point': 8.89, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 132, 'wind_gust': 2.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644285600, 'temp': 8.97, 'feels_like': 8.47, 'pressure': 1018, 'humidity': 94, 'dew_point': 8.06, 'uvi': 0, 'clouds': 100, 'visibility': 6131, 'wind_speed': 1.5, 'wind_deg': 127, 'wind_gust': 2.43, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.54}}, {'dt': 1644289200, 'temp': 8.97, 'feels_like': 8.32, 'pressure': 1019, 'humidity': 94, 'dew_point': 8.06, 'uvi': 0, 'clouds': 100, 'visibility': 5659, 'wind_speed': 1.65, 'wind_deg': 123, 'wind_gust': 2.59, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644292800, 'temp': 8.97, 'feels_like': 8.97, 'pressure': 1019, 'humidity': 95, 'dew_point': 8.21, 'uvi': 0, 'clouds': 100, 'visibility': 2963, 'wind_speed': 1.27, 'wind_deg': 134, 'wind_gust': 1.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.65}}, {'dt': 1644296400, 'temp': 8.97, 'feels_like': 8.97, 'pressure': 1019, 'humidity': 94, 'dew_point': 8.06, 'uvi': 0, 'clouds': 100, 'visibility': 6661, 'wind_speed': 0.65, 'wind_deg': 150, 'wind_gust': 1.26, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.54}}, {'dt': 1644300000, 'temp': 7.97, 'feels_like': 7.97, 'pressure': 1018, 'humidity': 95, 'dew_point': 7.22, 'uvi': 0, 'clouds': 100, 'visibility': 7983, 'wind_speed': 0.29, 'wind_deg': 160, 'wind_gust': 0.87, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.33}}, {'dt': 1644303600, 'temp': 8.97, 'feels_like': 8.97, 'pressure': 1017, 'humidity': 94, 'dew_point': 8.06, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 130, 'wind_gust': 0.88, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.75}}, {'dt': 1644307200, 'temp': 8.97, 'feels_like': 8.97, 'pressure': 1016, 'humidity': 93, 'dew_point': 7.9, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 182, 'wind_gust': 0.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1644310800, 'temp': 8.97, 'feels_like': 8.97, 'pressure': 1016, 'humidity': 93, 'dew_point': 7.9, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 199, 'wind_gust': 0.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644314400, 'temp': 8.97, 'feels_like': 8.97, 'pressure': 1016, 'humidity': 92, 'dew_point': 7.74, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 138, 'wind_gust': 0.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644318000, 'temp': 7.97, 'feels_like': 7.97, 'pressure': 1017, 'humidity': 92, 'dew_point': 6.75, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 140, 'wind_gust': 0.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644321600, 'temp': 7.97, 'feels_like': 7.97, 'pressure': 1018, 'humidity': 91, 'dew_point': 6.59, 'uvi': 0.28, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 139, 'wind_gust': 1.02, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644325200, 'temp': 9.97, 'feels_like': 9.97, 'pressure': 1018, 'humidity': 89, 'dew_point': 8.24, 'uvi': 1.36, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 126, 'wind_gust': 1.37, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644328800, 'temp': 9.97, 'feels_like': 9.97, 'pressure': 1018, 'humidity': 83, 'dew_point': 7.22, 'uvi': 3.22, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 147, 'wind_gust': 1.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644332400, 'temp': 10.97, 'feels_like': 10.05, 'pressure': 1017, 'humidity': 74, 'dew_point': 6.52, 'uvi': 5.42, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 147, 'wind_gust': 2.08, 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'}], 'rain': {'1h': 7.49}}, {'dt': 1644336000, 'temp': 8.97, 'feels_like': 8.97, 'pressure': 1016, 'humidity': 73, 'dew_point': 4.4, 'uvi': 9.18, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 146, 'wind_gust': 2.35, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.78}}, {'dt': 1644339600, 'temp': 7.97, 'feels_like': 7.97, 'pressure': 1016, 'humidity': 81, 'dew_point': 4.91, 'uvi': 9.99, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 145, 'wind_gust': 1.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644343200, 'temp': 9.97, 'feels_like': 9.97, 'pressure': 1015, 'humidity': 84, 'dew_point': 7.4, 'uvi': 9.07, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 125, 'wind_gust': 1.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644346800, 'temp': 10.97, 'feels_like': 10.37, 'pressure': 1015, 'humidity': 86, 'dew_point': 8.72, 'uvi': 3.65, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 105, 'wind_gust': 1.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644350400, 'temp': 10.97, 'feels_like': 10.39, 'pressure': 1014, 'humidity': 87, 'dew_point': 8.89, 'uvi': 2.13, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 120, 'wind_gust': 1.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644354000, 'temp': 11.97, 'feels_like': 11.49, 'pressure': 1014, 'humidity': 87, 'dew_point': 9.88, 'uvi': 0.87, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 138, 'wind_gust': 1.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644357600, 'temp': 11.97, 'feels_like': 11.47, 'pressure': 1015, 'humidity': 86, 'dew_point': 9.7, 'uvi': 0.14, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 139, 'wind_gust': 1.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644361200, 'temp': 10.97, 'feels_like': 10.52, 'pressure': 1016, 'humidity': 92, 'dew_point': 9.72, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 154, 'wind_gust': 1.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 00:00:00 | 100.000000 | 8.890000 | 9.970000 | 93.000000 | 1016.000000 |  | 9.970000 | 0.000000 | 6821.000000 | 138.000000 | 1.72 | 0.900000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 01:00:00 | 100.000000 | 8.890000 | 9.970000 | 93.000000 | 1017.000000 |  | 9.970000 | 0.000000 | 10000.000000 | 132.000000 | 2.03 | 1.240000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 02:00:00 | 100.000000 | 8.060000 | 8.470000 | 94.000000 | 1018.000000 | 1.54 | 8.970000 | 0.000000 | 6131.000000 | 127.000000 | 2.43 | 1.500000 | 501 | Rain | moderate rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 03:00:00 | 100.000000 | 8.060000 | 8.320000 | 94.000000 | 1019.000000 |  | 8.970000 | 0.000000 | 5659.000000 | 123.000000 | 2.59 | 1.650000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 04:00:00 | 100.000000 | 8.210000 | 8.970000 | 95.000000 | 1019.000000 | 0.65 | 8.970000 | 0.000000 | 2963.000000 | 134.000000 | 1.99 | 1.270000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 05:00:00 | 100.000000 | 8.060000 | 8.970000 | 94.000000 | 1019.000000 | 1.54 | 8.970000 | 0.000000 | 6661.000000 | 150.000000 | 1.26 | 0.650000 | 501 | Rain | moderate rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 06:00:00 | 100.000000 | 7.220000 | 7.970000 | 95.000000 | 1018.000000 | 1.33 | 7.970000 | 0.000000 | 7983.000000 | 160.000000 | 0.87 | 0.290000 | 501 | Rain | moderate rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 07:00:00 | 100.000000 | 8.060000 | 8.970000 | 94.000000 | 1017.000000 | 0.75 | 8.970000 | 0.000000 | 10000.000000 | 130.000000 | 0.88 | 0.390000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 08:00:00 | 100.000000 | 7.900000 | 8.970000 | 93.000000 | 1016.000000 | 0.24 | 8.970000 | 0.000000 | 10000.000000 | 182.000000 | 0.76 | 0.210000 | 500 | Rain | light rain | 10n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 09:00:00 | 100.000000 | 7.900000 | 8.970000 | 93.000000 | 1016.000000 |  | 8.970000 | 0.000000 | 10000.000000 | 199.000000 | 0.66 | 0.260000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 10:00:00 | 100.000000 | 7.740000 | 8.970000 | 92.000000 | 1016.000000 |  | 8.970000 | 0.000000 | 10000.000000 | 138.000000 | 0.61 | 0.510000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 11:00:00 | 100.000000 | 6.750000 | 7.970000 | 92.000000 | 1017.000000 |  | 7.970000 | 0.000000 | 10000.000000 | 140.000000 | 0.9 | 0.650000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 12:00:00 | 100.000000 | 6.590000 | 7.970000 | 91.000000 | 1018.000000 |  | 7.970000 | 0.280000 | 10000.000000 | 139.000000 | 1.02 | 0.620000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 13:00:00 | 100.000000 | 8.240000 | 9.970000 | 89.000000 | 1018.000000 |  | 9.970000 | 1.360000 | 10000.000000 | 126.000000 | 1.37 | 0.770000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 14:00:00 | 100.000000 | 7.220000 | 9.970000 | 83.000000 | 1018.000000 |  | 9.970000 | 3.220000 | 10000.000000 | 147.000000 | 1.89 | 1.010000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 15:00:00 | 100.000000 | 6.520000 | 10.050000 | 74.000000 | 1017.000000 | 7.49 | 10.970000 | 5.420000 | 10000.000000 | 147.000000 | 2.08 | 1.020000 | 502 | Rain | heavy intensity rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 16:00:00 | 100.000000 | 4.400000 | 8.970000 | 73.000000 | 1016.000000 | 1.78 | 8.970000 | 9.180000 | 10000.000000 | 146.000000 | 2.35 | 0.960000 | 501 | Rain | moderate rain | 10d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 17:00:00 | 100.000000 | 4.910000 | 7.970000 | 81.000000 | 1016.000000 |  | 7.970000 | 9.990000 | 10000.000000 | 145.000000 | 1.96 | 1.010000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 18:00:00 | 97.000000 | 7.400000 | 9.970000 | 84.000000 | 1015.000000 |  | 9.970000 | 9.070000 | 10000.000000 | 125.000000 | 1.66 | 0.870000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 19:00:00 | 100.000000 | 8.720000 | 10.370000 | 86.000000 | 1015.000000 |  | 10.970000 | 3.650000 | 10000.000000 | 105.000000 | 1.61 | 0.760000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 20:00:00 | 100.000000 | 8.890000 | 10.390000 | 87.000000 | 1014.000000 |  | 10.970000 | 2.130000 | 10000.000000 | 120.000000 | 1.52 | 0.740000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 21:00:00 | 100.000000 | 9.880000 | 11.490000 | 87.000000 | 1014.000000 |  | 11.970000 | 0.870000 | 10000.000000 | 138.000000 | 1.48 | 0.870000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 22:00:00 | 100.000000 | 9.700000 | 11.470000 | 86.000000 | 1015.000000 |  | 11.970000 | 0.140000 | 10000.000000 | 139.000000 | 1.73 | 0.950000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 23:00:00 | 100.000000 | 9.720000 | 10.520000 | 92.000000 | 1016.000000 |  | 10.970000 | 0.000000 | 10000.000000 | 154.000000 | 1.42 | 0.680000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21206650_OWM_Clouds_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Clouds_20220210.png)
![CNE_IDEAM_Station21206650_OWM_Dewpoint_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Dewpoint_20220210.png)
![CNE_IDEAM_Station21206650_OWM_Feelslike_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Feelslike_20220210.png)
![CNE_IDEAM_Station21206650_OWM_Humidity_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Humidity_20220210.png)
![CNE_IDEAM_Station21206650_OWM_Pressure_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Pressure_20220210.png)
![CNE_IDEAM_Station21206650_OWM_Rain_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Rain_20220210.png)
![CNE_IDEAM_Station21206650_OWM_Temp_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Temp_20220210.png)
![CNE_IDEAM_Station21206650_OWM_UVI_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_UVI_20220210.png)
![CNE_IDEAM_Station21206650_OWM_Visibility_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Visibility_20220210.png)
![CNE_IDEAM_Station21206650_OWM_Winddeg_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Winddeg_20220210.png)
![CNE_IDEAM_Station21206650_OWM_Windgust_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Windgust_20220210.png)
![CNE_IDEAM_Station21206650_OWM_Windspeed_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Windspeed_20220210.png)


## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BETANIA [35020350] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35020350_OWM_20220210.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220210.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.21888889,-74.14686111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.21888889&lon=-74.14686111)

| Parameter | Value |
|---|---|
| Code | 35020350 |
| Name | BETANIA [35020350] |
| Latitude, ° | 4.21888889 |
| Longitude, ° | -74.14686111 |
| Elevation, m | 3150 |
| Category | Pluviométrica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1986-01-15 00:00:00 |
| Suspension date | NaT |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Blanco |
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

### (CNE index 1901) Open Weather values for station 35020350 - BETANIA [35020350]

JSON data from API OWM:

```
{'lat': 4.2189, 'lon': -74.1469, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644329284, 'sunrise': 1644318713, 'sunset': 1644361785, 'temp': 11.37, 'feels_like': 10.89, 'pressure': 1019, 'humidity': 89, 'dew_point': 9.62, 'uvi': 3.32, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 84, 'wind_gust': 1.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, 'hourly': [{'dt': 1644278400, 'temp': 11.37, 'feels_like': 11.04, 'pressure': 1017, 'humidity': 95, 'dew_point': 10.6, 'uvi': 0, 'clouds': 100, 'visibility': 6872, 'wind_speed': 1.17, 'wind_deg': 122, 'wind_gust': 1.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644282000, 'temp': 11.37, 'feels_like': 11.04, 'pressure': 1018, 'humidity': 95, 'dew_point': 10.6, 'uvi': 0, 'clouds': 100, 'visibility': 5077, 'wind_speed': 1.35, 'wind_deg': 111, 'wind_gust': 2.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644285600, 'temp': 10.37, 'feels_like': 9.94, 'pressure': 1019, 'humidity': 95, 'dew_point': 9.6, 'uvi': 0, 'clouds': 100, 'visibility': 1733, 'wind_speed': 1.49, 'wind_deg': 98, 'wind_gust': 2.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644289200, 'temp': 10.37, 'feels_like': 9.94, 'pressure': 1019, 'humidity': 95, 'dew_point': 9.6, 'uvi': 0, 'clouds': 100, 'visibility': 609, 'wind_speed': 1.19, 'wind_deg': 93, 'wind_gust': 1.94, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 2.73}}, {'dt': 1644292800, 'temp': 10.37, 'feels_like': 9.94, 'pressure': 1019, 'humidity': 95, 'dew_point': 9.6, 'uvi': 0, 'clouds': 100, 'visibility': 1456, 'wind_speed': 0.41, 'wind_deg': 106, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.75}}, {'dt': 1644296400, 'temp': 10.37, 'feels_like': 9.94, 'pressure': 1019, 'humidity': 95, 'dew_point': 9.6, 'uvi': 0, 'clouds': 100, 'visibility': 7059, 'wind_speed': 0.03, 'wind_deg': 321, 'wind_gust': 1.05, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 2.73}}, {'dt': 1644300000, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1018, 'humidity': 96, 'dew_point': 8.77, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 280, 'wind_gust': 0.95, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.33}}, {'dt': 1644303600, 'temp': 10.37, 'feels_like': 9.92, 'pressure': 1017, 'humidity': 94, 'dew_point': 9.45, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.14, 'wind_deg': 272, 'wind_gust': 0.96, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.33}}, {'dt': 1644307200, 'temp': 10.37, 'feels_like': 9.92, 'pressure': 1017, 'humidity': 94, 'dew_point': 9.45, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 249, 'wind_gust': 0.82, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.78}}, {'dt': 1644310800, 'temp': 10.37, 'feels_like': 9.89, 'pressure': 1017, 'humidity': 93, 'dew_point': 9.29, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 206, 'wind_gust': 0.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644314400, 'temp': 10.37, 'feels_like': 9.89, 'pressure': 1017, 'humidity': 93, 'dew_point': 9.29, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 129, 'wind_gust': 0.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644318000, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1018, 'humidity': 94, 'dew_point': 8.45, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 113, 'wind_gust': 1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644321600, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1018, 'humidity': 93, 'dew_point': 8.3, 'uvi': 0.07, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 109, 'wind_gust': 1.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644325200, 'temp': 11.37, 'feels_like': 10.94, 'pressure': 1019, 'humidity': 91, 'dew_point': 9.96, 'uvi': 1.41, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 91, 'wind_gust': 1.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644328800, 'temp': 11.37, 'feels_like': 10.89, 'pressure': 1019, 'humidity': 89, 'dew_point': 9.62, 'uvi': 3.32, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 84, 'wind_gust': 1.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644332400, 'temp': 12.37, 'feels_like': 11.93, 'pressure': 1019, 'humidity': 87, 'dew_point': 10.27, 'uvi': 5.57, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 84, 'wind_gust': 1.67, 'weather': [{'id': 503, 'main': 'Rain', 'description': 'very heavy rain', 'icon': '10d'}], 'rain': {'1h': 23.68}}, {'dt': 1644336000, 'temp': 10.37, 'feels_like': 9.84, 'pressure': 1018, 'humidity': 91, 'dew_point': 8.97, 'uvi': 5.67, 'clouds': 96, 'visibility': 9363, 'wind_speed': 0.28, 'wind_deg': 124, 'wind_gust': 1.54, 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'}], 'rain': {'1h': 8.65}}, {'dt': 1644339600, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1017, 'humidity': 92, 'dew_point': 8.14, 'uvi': 6.17, 'clouds': 97, 'visibility': 7749, 'wind_speed': 0.59, 'wind_deg': 82, 'wind_gust': 1.62, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.37}}, {'dt': 1644343200, 'temp': 11.37, 'feels_like': 10.96, 'pressure': 1016, 'humidity': 92, 'dew_point': 10.12, 'uvi': 5.61, 'clouds': 100, 'visibility': 3821, 'wind_speed': 0.39, 'wind_deg': 53, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.27}}, {'dt': 1644346800, 'temp': 12.37, 'feels_like': 12.12, 'pressure': 1016, 'humidity': 94, 'dew_point': 11.43, 'uvi': 5.44, 'clouds': 100, 'visibility': 3280, 'wind_speed': 0.22, 'wind_deg': 59, 'wind_gust': 1.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644350400, 'temp': 12.37, 'feels_like': 12.17, 'pressure': 1015, 'humidity': 96, 'dew_point': 11.75, 'uvi': 3.18, 'clouds': 100, 'visibility': 669, 'wind_speed': 0.18, 'wind_deg': 33, 'wind_gust': 1.15, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644354000, 'temp': 13.37, 'feels_like': 13.27, 'pressure': 1015, 'humidity': 96, 'dew_point': 12.75, 'uvi': 1.31, 'clouds': 100, 'visibility': 4316, 'wind_speed': 0.36, 'wind_deg': 69, 'wind_gust': 1.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644357600, 'temp': 13.37, 'feels_like': 13.24, 'pressure': 1016, 'humidity': 95, 'dew_point': 12.59, 'uvi': 0.5, 'clouds': 100, 'visibility': 6119, 'wind_speed': 0.65, 'wind_deg': 98, 'wind_gust': 1.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644361200, 'temp': 12.37, 'feels_like': 12.2, 'pressure': 1017, 'humidity': 97, 'dew_point': 11.91, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 107, 'wind_gust': 1.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 00:00:00 | 100.000000 | 10.600000 | 11.040000 | 95.000000 | 1017.000000 |  | 11.370000 | 0.000000 | 6872.000000 | 122.000000 | 1.97 | 1.170000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 01:00:00 | 100.000000 | 10.600000 | 11.040000 | 95.000000 | 1018.000000 |  | 11.370000 | 0.000000 | 5077.000000 | 111.000000 | 2.12 | 1.350000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 02:00:00 | 100.000000 | 9.600000 | 9.940000 | 95.000000 | 1019.000000 |  | 10.370000 | 0.000000 | 1733.000000 | 98.000000 | 2.32 | 1.490000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 03:00:00 | 100.000000 | 9.600000 | 9.940000 | 95.000000 | 1019.000000 | 2.73 | 10.370000 | 0.000000 | 609.000000 | 93.000000 | 1.94 | 1.190000 | 501 | Rain | moderate rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 04:00:00 | 100.000000 | 9.600000 | 9.940000 | 95.000000 | 1019.000000 | 0.75 | 10.370000 | 0.000000 | 1456.000000 | 106.000000 | 1.27 | 0.410000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 05:00:00 | 100.000000 | 9.600000 | 9.940000 | 95.000000 | 1019.000000 | 2.73 | 10.370000 | 0.000000 | 7059.000000 | 321.000000 | 1.05 | 0.030000 | 501 | Rain | moderate rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 06:00:00 | 100.000000 | 8.770000 | 9.370000 | 96.000000 | 1018.000000 | 1.33 | 9.370000 | 0.000000 | 10000.000000 | 280.000000 | 0.95 | 0.210000 | 501 | Rain | moderate rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 07:00:00 | 100.000000 | 9.450000 | 9.920000 | 94.000000 | 1017.000000 | 1.33 | 10.370000 | 0.000000 | 10000.000000 | 272.000000 | 0.96 | 0.140000 | 501 | Rain | moderate rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 08:00:00 | 100.000000 | 9.450000 | 9.920000 | 94.000000 | 1017.000000 | 1.78 | 10.370000 | 0.000000 | 10000.000000 | 249.000000 | 0.82 | 0.370000 | 501 | Rain | moderate rain | 10n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 09:00:00 | 100.000000 | 9.290000 | 9.890000 | 93.000000 | 1017.000000 |  | 10.370000 | 0.000000 | 10000.000000 | 206.000000 | 0.75 | 0.210000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 10:00:00 | 100.000000 | 9.290000 | 9.890000 | 93.000000 | 1017.000000 |  | 10.370000 | 0.000000 | 10000.000000 | 129.000000 | 0.86 | 0.520000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 11:00:00 | 100.000000 | 8.450000 | 9.370000 | 94.000000 | 1018.000000 |  | 9.370000 | 0.000000 | 10000.000000 | 113.000000 | 1 | 0.510000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 12:00:00 | 99.000000 | 8.300000 | 9.370000 | 93.000000 | 1018.000000 |  | 9.370000 | 0.070000 | 10000.000000 | 109.000000 | 1.32 | 0.710000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 13:00:00 | 100.000000 | 9.960000 | 10.940000 | 91.000000 | 1019.000000 |  | 11.370000 | 1.410000 | 10000.000000 | 91.000000 | 1.73 | 0.830000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 14:00:00 | 94.000000 | 9.620000 | 10.890000 | 89.000000 | 1019.000000 |  | 11.370000 | 3.320000 | 10000.000000 | 84.000000 | 1.46 | 0.350000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 15:00:00 | 95.000000 | 10.270000 | 11.930000 | 87.000000 | 1019.000000 | 23.68 | 12.370000 | 5.570000 | 10000.000000 | 84.000000 | 1.67 | 0.360000 | 503 | Rain | very heavy rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 16:00:00 | 96.000000 | 8.970000 | 9.840000 | 91.000000 | 1018.000000 | 8.65 | 10.370000 | 5.670000 | 9363.000000 | 124.000000 | 1.54 | 0.280000 | 502 | Rain | heavy intensity rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 17:00:00 | 97.000000 | 8.140000 | 9.370000 | 92.000000 | 1017.000000 | 2.37 | 9.370000 | 6.170000 | 7749.000000 | 82.000000 | 1.62 | 0.590000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 18:00:00 | 100.000000 | 10.120000 | 10.960000 | 92.000000 | 1016.000000 | 0.27 | 11.370000 | 5.610000 | 3821.000000 | 53.000000 | 1.25 | 0.390000 | 500 | Rain | light rain | 10d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 19:00:00 | 100.000000 | 11.430000 | 12.120000 | 94.000000 | 1016.000000 |  | 12.370000 | 5.440000 | 3280.000000 | 59.000000 | 1.05 | 0.220000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 20:00:00 | 100.000000 | 11.750000 | 12.170000 | 96.000000 | 1015.000000 |  | 12.370000 | 3.180000 | 669.000000 | 33.000000 | 1.15 | 0.180000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 21:00:00 | 100.000000 | 12.750000 | 13.270000 | 96.000000 | 1015.000000 |  | 13.370000 | 1.310000 | 4316.000000 | 69.000000 | 1.32 | 0.360000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 22:00:00 | 100.000000 | 12.590000 | 13.240000 | 95.000000 | 1016.000000 |  | 13.370000 | 0.500000 | 6119.000000 | 98.000000 | 1.49 | 0.650000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 23:00:00 | 100.000000 | 11.910000 | 12.200000 | 97.000000 | 1017.000000 |  | 12.370000 | 0.000000 | 10000.000000 | 107.000000 | 1.12 | 0.390000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35020350_OWM_Clouds_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Clouds_20220210.png)
![CNE_IDEAM_Station35020350_OWM_Dewpoint_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Dewpoint_20220210.png)
![CNE_IDEAM_Station35020350_OWM_Feelslike_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Feelslike_20220210.png)
![CNE_IDEAM_Station35020350_OWM_Humidity_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Humidity_20220210.png)
![CNE_IDEAM_Station35020350_OWM_Pressure_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Pressure_20220210.png)
![CNE_IDEAM_Station35020350_OWM_Rain_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Rain_20220210.png)
![CNE_IDEAM_Station35020350_OWM_Temp_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Temp_20220210.png)
![CNE_IDEAM_Station35020350_OWM_UVI_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_UVI_20220210.png)
![CNE_IDEAM_Station35020350_OWM_Visibility_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Visibility_20220210.png)
![CNE_IDEAM_Station35020350_OWM_Winddeg_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Winddeg_20220210.png)
![CNE_IDEAM_Station35020350_OWM_Windgust_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Windgust_20220210.png)
![CNE_IDEAM_Station35020350_OWM_Windspeed_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Windspeed_20220210.png)

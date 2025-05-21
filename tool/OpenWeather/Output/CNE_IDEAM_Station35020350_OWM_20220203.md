
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

* Current date time: 2022-02-03 15:08:03.237034
* Unix time to eval: 1643814483
* Days before (for historical data): 1
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220203.xls
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35020350_OWM_20220203.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220203.csv)

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

### (CNE index 1903) Open Weather values for station 35020350 - BETANIA [35020350]

JSON data from API OWM:

```
{'lat': 4.2189, 'lon': -74.1469, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643814483, 'sunrise': 1643800313, 'sunset': 1643843319, 'temp': 14.37, 'feels_like': 13.51, 'pressure': 1018, 'humidity': 63, 'dew_point': 7.43, 'uvi': 6.83, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 85, 'wind_gust': 2.04, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1643760000, 'temp': 11.37, 'feels_like': 10.89, 'pressure': 1017, 'humidity': 89, 'dew_point': 9.62, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 106, 'wind_gust': 1.75, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643763600, 'temp': 10.37, 'feels_like': 9.76, 'pressure': 1018, 'humidity': 88, 'dew_point': 8.47, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 110, 'wind_gust': 1.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643767200, 'temp': 10.37, 'feels_like': 9.79, 'pressure': 1018, 'humidity': 89, 'dew_point': 8.64, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 120, 'wind_gust': 1.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643770800, 'temp': 8.37, 'feels_like': 8.37, 'pressure': 1019, 'humidity': 89, 'dew_point': 6.67, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 149, 'wind_gust': 1.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643774400, 'temp': 8.37, 'feels_like': 8.37, 'pressure': 1018, 'humidity': 88, 'dew_point': 6.5, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 138, 'wind_gust': 1.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643778000, 'temp': 6.37, 'feels_like': 6.37, 'pressure': 1018, 'humidity': 88, 'dew_point': 4.53, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 112, 'wind_gust': 1.35, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643781600, 'temp': 6.37, 'feels_like': 6.37, 'pressure': 1017, 'humidity': 88, 'dew_point': 4.53, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 120, 'wind_gust': 1.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643785200, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1017, 'humidity': 88, 'dew_point': 5.52, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 103, 'wind_gust': 1.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643788800, 'temp': 8.37, 'feels_like': 8.37, 'pressure': 1016, 'humidity': 89, 'dew_point': 6.67, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 102, 'wind_gust': 1.47, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643792400, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1017, 'humidity': 89, 'dew_point': 5.68, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 107, 'wind_gust': 1.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643796000, 'temp': 6.37, 'feels_like': 6.37, 'pressure': 1017, 'humidity': 90, 'dew_point': 4.85, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 111, 'wind_gust': 1.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643799600, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1018, 'humidity': 89, 'dew_point': 5.68, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 111, 'wind_gust': 1.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643803200, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1018, 'humidity': 85, 'dew_point': 5.02, 'uvi': 0.53, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 100, 'wind_gust': 2.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643806800, 'temp': 9.37, 'feels_like': 8.88, 'pressure': 1019, 'humidity': 78, 'dew_point': 5.73, 'uvi': 1.72, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 104, 'wind_gust': 2.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643810400, 'temp': 12.37, 'feels_like': 11.44, 'pressure': 1019, 'humidity': 68, 'dew_point': 6.64, 'uvi': 4.07, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 100, 'wind_gust': 1.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643814000, 'temp': 14.37, 'feels_like': 13.51, 'pressure': 1018, 'humidity': 63, 'dew_point': 7.43, 'uvi': 6.83, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 85, 'wind_gust': 2.04, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643817600, 'temp': 16.37, 'feels_like': 15.71, 'pressure': 1017, 'humidity': 63, 'dew_point': 9.32, 'uvi': 12.64, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 76, 'wind_gust': 2.2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643821200, 'temp': 16.37, 'feels_like': 15.79, 'pressure': 1016, 'humidity': 66, 'dew_point': 10.01, 'uvi': 13.74, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 64, 'wind_gust': 2.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1643824800, 'temp': 15.37, 'feels_like': 14.66, 'pressure': 1015, 'humidity': 65, 'dew_point': 8.83, 'uvi': 12.47, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 57, 'wind_gust': 2.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.27}}, {'dt': 1643828400, 'temp': 16.37, 'feels_like': 15.79, 'pressure': 1014, 'humidity': 66, 'dew_point': 10.01, 'uvi': 9.05, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 71, 'wind_gust': 2.51, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.27}}, {'dt': 1643832000, 'temp': 16.37, 'feels_like': 15.86, 'pressure': 1014, 'humidity': 69, 'dew_point': 10.68, 'uvi': 5.27, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 105, 'wind_gust': 2.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.34}}, {'dt': 1643835600, 'temp': 15.37, 'feels_like': 14.84, 'pressure': 1014, 'humidity': 72, 'dew_point': 10.36, 'uvi': 2.17, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 112, 'wind_gust': 2.29, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1643839200, 'temp': 14.37, 'feels_like': 13.79, 'pressure': 1014, 'humidity': 74, 'dew_point': 9.8, 'uvi': 0.39, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.67, 'wind_deg': 108, 'wind_gust': 2.31, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.23}}, {'dt': 1643842800, 'temp': 12.37, 'feels_like': 11.78, 'pressure': 1016, 'humidity': 81, 'dew_point': 9.21, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 97, 'wind_gust': 2.35, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 00:00:00 | 77.000000 | 9.620000 | 10.890000 | 89.000000 | 1017.000000 |  | 11.370000 | 0.000000 | 10000.000000 | 106.000000 | 1.75 | 1.280000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 01:00:00 | 88.000000 | 8.470000 | 9.760000 | 88.000000 | 1018.000000 |  | 10.370000 | 0.000000 | 10000.000000 | 110.000000 | 1.58 | 1.090000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 02:00:00 | 89.000000 | 8.640000 | 9.790000 | 89.000000 | 1018.000000 |  | 10.370000 | 0.000000 | 10000.000000 | 120.000000 | 1.61 | 0.780000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 03:00:00 | 93.000000 | 6.670000 | 8.370000 | 89.000000 | 1019.000000 |  | 8.370000 | 0.000000 | 10000.000000 | 149.000000 | 1.36 | 0.550000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 04:00:00 | 95.000000 | 6.500000 | 8.370000 | 88.000000 | 1018.000000 |  | 8.370000 | 0.000000 | 10000.000000 | 138.000000 | 1.2 | 0.480000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 05:00:00 | 96.000000 | 4.530000 | 6.370000 | 88.000000 | 1018.000000 |  | 6.370000 | 0.000000 | 10000.000000 | 112.000000 | 1.35 | 0.830000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 06:00:00 | 90.000000 | 4.530000 | 6.370000 | 88.000000 | 1017.000000 |  | 6.370000 | 0.000000 | 10000.000000 | 120.000000 | 1.17 | 0.490000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 07:00:00 | 99.000000 | 5.520000 | 7.370000 | 88.000000 | 1017.000000 |  | 7.370000 | 0.000000 | 10000.000000 | 103.000000 | 1.22 | 0.560000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 08:00:00 | 99.000000 | 6.670000 | 8.370000 | 89.000000 | 1016.000000 |  | 8.370000 | 0.000000 | 10000.000000 | 102.000000 | 1.47 | 0.720000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 09:00:00 | 100.000000 | 5.680000 | 7.370000 | 89.000000 | 1017.000000 |  | 7.370000 | 0.000000 | 10000.000000 | 107.000000 | 1.65 | 0.910000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 10:00:00 | 100.000000 | 4.850000 | 6.370000 | 90.000000 | 1017.000000 |  | 6.370000 | 0.000000 | 10000.000000 | 111.000000 | 1.68 | 0.890000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 11:00:00 | 100.000000 | 5.680000 | 7.370000 | 89.000000 | 1018.000000 |  | 7.370000 | 0.000000 | 10000.000000 | 111.000000 | 1.89 | 0.960000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 12:00:00 | 96.000000 | 5.020000 | 7.370000 | 85.000000 | 1018.000000 |  | 7.370000 | 0.530000 | 10000.000000 | 100.000000 | 2.25 | 1.170000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 13:00:00 | 100.000000 | 5.730000 | 8.880000 | 78.000000 | 1019.000000 |  | 9.370000 | 1.720000 | 10000.000000 | 104.000000 | 2.24 | 1.550000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 14:00:00 | 90.000000 | 6.640000 | 11.440000 | 68.000000 | 1019.000000 |  | 12.370000 | 4.070000 | 10000.000000 | 100.000000 | 1.81 | 1.220000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 15:00:00 | 79.000000 | 7.430000 | 13.510000 | 63.000000 | 1018.000000 |  | 14.370000 | 6.830000 | 10000.000000 | 85.000000 | 2.04 | 0.750000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 16:00:00 | 79.000000 | 9.320000 | 15.710000 | 63.000000 | 1017.000000 |  | 16.370000 | 12.640000 | 10000.000000 | 76.000000 | 2.2 | 0.540000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 17:00:00 | 82.000000 | 10.010000 | 15.790000 | 66.000000 | 1016.000000 | 0.17 | 16.370000 | 13.740000 | 10000.000000 | 64.000000 | 2.18 | 0.930000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 18:00:00 | 99.000000 | 8.830000 | 14.660000 | 65.000000 | 1015.000000 | 0.27 | 15.370000 | 12.470000 | 10000.000000 | 57.000000 | 2.45 | 1.130000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 19:00:00 | 100.000000 | 10.010000 | 15.790000 | 66.000000 | 1014.000000 | 0.27 | 16.370000 | 9.050000 | 10000.000000 | 71.000000 | 2.51 | 1.060000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 20:00:00 | 100.000000 | 10.680000 | 15.860000 | 69.000000 | 1014.000000 | 0.34 | 16.370000 | 5.270000 | 10000.000000 | 105.000000 | 2.2 | 1.180000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 21:00:00 | 100.000000 | 10.360000 | 14.840000 | 72.000000 | 1014.000000 | 0.21 | 15.370000 | 2.170000 | 10000.000000 | 112.000000 | 2.29 | 1.280000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 22:00:00 | 100.000000 | 9.800000 | 13.790000 | 74.000000 | 1014.000000 | 0.23 | 14.370000 | 0.390000 | 10000.000000 | 108.000000 | 2.31 | 1.670000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 23:00:00 | 100.000000 | 9.210000 | 11.780000 | 81.000000 | 1016.000000 | 0.1 | 12.370000 | 0.000000 | 10000.000000 | 97.000000 | 2.35 | 1.610000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station35020350_OWM_Clouds_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Clouds_20220203.png)
![CNE_IDEAM_Station35020350_OWM_Dewpoint_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Dewpoint_20220203.png)
![CNE_IDEAM_Station35020350_OWM_Feelslike_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Feelslike_20220203.png)
![CNE_IDEAM_Station35020350_OWM_Humidity_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Humidity_20220203.png)
![CNE_IDEAM_Station35020350_OWM_Pressure_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Pressure_20220203.png)
![CNE_IDEAM_Station35020350_OWM_Rain_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Rain_20220203.png)
![CNE_IDEAM_Station35020350_OWM_Temp_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Temp_20220203.png)
![CNE_IDEAM_Station35020350_OWM_UVI_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_UVI_20220203.png)
![CNE_IDEAM_Station35020350_OWM_Visibility_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Visibility_20220203.png)
![CNE_IDEAM_Station35020350_OWM_Winddeg_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Winddeg_20220203.png)
![CNE_IDEAM_Station35020350_OWM_Windgust_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Windgust_20220203.png)
![CNE_IDEAM_Station35020350_OWM_Windspeed_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Windspeed_20220203.png)

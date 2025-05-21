
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - NAZARETH [35020310] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35020310_OWM_20220203.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220203.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.17225,-74.146) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.17225&lon=-74.146)

| Parameter | Value |
|---|---|
| Code | 35020310 |
| Name | NAZARETH [35020310] |
| Latitude, ° | 4.17225 |
| Longitude, ° | -74.146 |
| Elevation, m | 2800 |
| Category | Pluviográfica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1984-07-15 00:00:00 |
| Suspension date | NaT |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Ceibas |
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

### (CNE index 1855) Open Weather values for station 35020310 - NAZARETH [35020310]

JSON data from API OWM:

```
{'lat': 4.1723, 'lon': -74.146, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643814483, 'sunrise': 1643800309, 'sunset': 1643843322, 'temp': 16.9, 'feels_like': 16.32, 'pressure': 1018, 'humidity': 64, 'dew_point': 10.05, 'uvi': 6.83, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 101, 'wind_gust': 2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1643760000, 'temp': 13.9, 'feels_like': 13.7, 'pressure': 1017, 'humidity': 90, 'dew_point': 12.29, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 104, 'wind_gust': 1.73, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643763600, 'temp': 12.9, 'feels_like': 12.54, 'pressure': 1018, 'humidity': 88, 'dew_point': 10.96, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 106, 'wind_gust': 1.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643767200, 'temp': 12.9, 'feels_like': 12.57, 'pressure': 1018, 'humidity': 89, 'dew_point': 11.13, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 117, 'wind_gust': 1.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643770800, 'temp': 10.9, 'feels_like': 10.37, 'pressure': 1019, 'humidity': 89, 'dew_point': 9.16, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 142, 'wind_gust': 1.23, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643774400, 'temp': 10.9, 'feels_like': 10.37, 'pressure': 1018, 'humidity': 89, 'dew_point': 9.16, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 134, 'wind_gust': 1.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643778000, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1018, 'humidity': 90, 'dew_point': 7.35, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 115, 'wind_gust': 1.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643781600, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1017, 'humidity': 88, 'dew_point': 7.02, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 127, 'wind_gust': 1.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643785200, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1017, 'humidity': 88, 'dew_point': 8.01, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 113, 'wind_gust': 1.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643788800, 'temp': 10.9, 'feels_like': 10.37, 'pressure': 1017, 'humidity': 89, 'dew_point': 9.16, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 111, 'wind_gust': 1.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643792400, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1017, 'humidity': 90, 'dew_point': 8.34, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 113, 'wind_gust': 1.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643796000, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1018, 'humidity': 91, 'dew_point': 7.51, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 117, 'wind_gust': 1.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643799600, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1018, 'humidity': 90, 'dew_point': 8.34, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 116, 'wind_gust': 1.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643803200, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1019, 'humidity': 86, 'dew_point': 7.67, 'uvi': 0.53, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 105, 'wind_gust': 2.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643806800, 'temp': 11.9, 'feels_like': 11.18, 'pressure': 1019, 'humidity': 78, 'dew_point': 8.19, 'uvi': 1.72, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.58, 'wind_deg': 106, 'wind_gust': 2.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643810400, 'temp': 14.9, 'feels_like': 14.25, 'pressure': 1019, 'humidity': 69, 'dew_point': 9.27, 'uvi': 4.07, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 105, 'wind_gust': 1.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643814000, 'temp': 16.9, 'feels_like': 16.32, 'pressure': 1018, 'humidity': 64, 'dew_point': 10.05, 'uvi': 6.83, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 101, 'wind_gust': 2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643817600, 'temp': 18.9, 'feels_like': 18.49, 'pressure': 1017, 'humidity': 63, 'dew_point': 11.71, 'uvi': 12.64, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 102, 'wind_gust': 2.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643821200, 'temp': 18.9, 'feels_like': 18.54, 'pressure': 1016, 'humidity': 65, 'dew_point': 12.18, 'uvi': 13.74, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 86, 'wind_gust': 2.13, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1643824800, 'temp': 17.9, 'feels_like': 17.42, 'pressure': 1015, 'humidity': 64, 'dew_point': 11, 'uvi': 12.47, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 79, 'wind_gust': 2.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1643828400, 'temp': 18.9, 'feels_like': 18.57, 'pressure': 1014, 'humidity': 66, 'dew_point': 12.42, 'uvi': 9.05, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 92, 'wind_gust': 2.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1643832000, 'temp': 18.9, 'feels_like': 18.65, 'pressure': 1014, 'humidity': 69, 'dew_point': 13.09, 'uvi': 5.27, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 110, 'wind_gust': 2.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1643835600, 'temp': 17.9, 'feels_like': 17.63, 'pressure': 1014, 'humidity': 72, 'dew_point': 12.79, 'uvi': 2.17, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.6, 'wind_deg': 114, 'wind_gust': 2.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1643839200, 'temp': 16.9, 'feels_like': 16.58, 'pressure': 1015, 'humidity': 74, 'dew_point': 12.24, 'uvi': 0.39, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.84, 'wind_deg': 111, 'wind_gust': 2.35, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1643842800, 'temp': 14.9, 'feels_like': 14.59, 'pressure': 1016, 'humidity': 82, 'dew_point': 11.86, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.6, 'wind_deg': 101, 'wind_gust': 2.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 00:00:00 | 81.000000 | 12.290000 | 13.700000 | 90.000000 | 1017.000000 |  | 13.900000 | 0.000000 | 10000.000000 | 104.000000 | 1.73 | 1.200000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 01:00:00 | 91.000000 | 10.960000 | 12.540000 | 88.000000 | 1018.000000 |  | 12.900000 | 0.000000 | 10000.000000 | 106.000000 | 1.5 | 0.960000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 02:00:00 | 92.000000 | 11.130000 | 12.570000 | 89.000000 | 1018.000000 |  | 12.900000 | 0.000000 | 10000.000000 | 117.000000 | 1.48 | 0.730000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 03:00:00 | 94.000000 | 9.160000 | 10.370000 | 89.000000 | 1019.000000 |  | 10.900000 | 0.000000 | 10000.000000 | 142.000000 | 1.23 | 0.510000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 04:00:00 | 96.000000 | 9.160000 | 10.370000 | 89.000000 | 1018.000000 |  | 10.900000 | 0.000000 | 10000.000000 | 134.000000 | 1.12 | 0.470000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 05:00:00 | 96.000000 | 7.350000 | 8.900000 | 90.000000 | 1018.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 115.000000 | 1.28 | 0.790000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 06:00:00 | 91.000000 | 7.020000 | 8.900000 | 88.000000 | 1017.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 127.000000 | 1.16 | 0.550000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 07:00:00 | 99.000000 | 8.010000 | 9.900000 | 88.000000 | 1017.000000 |  | 9.900000 | 0.000000 | 10000.000000 | 113.000000 | 1.22 | 0.550000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 08:00:00 | 99.000000 | 9.160000 | 10.370000 | 89.000000 | 1017.000000 |  | 10.900000 | 0.000000 | 10000.000000 | 111.000000 | 1.48 | 0.750000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 09:00:00 | 100.000000 | 8.340000 | 9.900000 | 90.000000 | 1017.000000 |  | 9.900000 | 0.000000 | 10000.000000 | 113.000000 | 1.68 | 0.910000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 10:00:00 | 100.000000 | 7.510000 | 8.900000 | 91.000000 | 1018.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 117.000000 | 1.74 | 0.870000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 11:00:00 | 100.000000 | 8.340000 | 9.900000 | 90.000000 | 1018.000000 |  | 9.900000 | 0.000000 | 10000.000000 | 116.000000 | 1.95 | 0.900000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 12:00:00 | 95.000000 | 7.670000 | 9.900000 | 86.000000 | 1019.000000 |  | 9.900000 | 0.530000 | 10000.000000 | 105.000000 | 2.25 | 1.150000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 13:00:00 | 100.000000 | 8.190000 | 11.180000 | 78.000000 | 1019.000000 |  | 11.900000 | 1.720000 | 10000.000000 | 106.000000 | 2.18 | 1.580000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 14:00:00 | 91.000000 | 9.270000 | 14.250000 | 69.000000 | 1019.000000 |  | 14.900000 | 4.070000 | 10000.000000 | 105.000000 | 1.84 | 1.360000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 15:00:00 | 82.000000 | 10.050000 | 16.320000 | 64.000000 | 1018.000000 |  | 16.900000 | 6.830000 | 10000.000000 | 101.000000 | 2 | 1.000000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 16:00:00 | 81.000000 | 11.710000 | 18.490000 | 63.000000 | 1017.000000 |  | 18.900000 | 12.640000 | 10000.000000 | 102.000000 | 2.11 | 0.780000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 17:00:00 | 83.000000 | 12.180000 | 18.540000 | 65.000000 | 1016.000000 | 0.15 | 18.900000 | 13.740000 | 10000.000000 | 86.000000 | 2.13 | 0.980000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 18:00:00 | 100.000000 | 11.000000 | 17.420000 | 64.000000 | 1015.000000 | 0.22 | 17.900000 | 12.470000 | 10000.000000 | 79.000000 | 2.47 | 1.090000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 19:00:00 | 100.000000 | 12.420000 | 18.570000 | 66.000000 | 1014.000000 | 0.24 | 18.900000 | 9.050000 | 10000.000000 | 92.000000 | 2.47 | 1.190000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 20:00:00 | 100.000000 | 13.090000 | 18.650000 | 69.000000 | 1014.000000 | 0.31 | 18.900000 | 5.270000 | 10000.000000 | 110.000000 | 2.24 | 1.500000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 21:00:00 | 100.000000 | 12.790000 | 17.630000 | 72.000000 | 1014.000000 | 0.18 | 17.900000 | 2.170000 | 10000.000000 | 114.000000 | 2.34 | 1.600000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 22:00:00 | 100.000000 | 12.240000 | 16.580000 | 74.000000 | 1015.000000 | 0.2 | 16.900000 | 0.390000 | 10000.000000 | 111.000000 | 2.35 | 1.840000 | 500 | Rain | light rain | 10d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 23:00:00 | 100.000000 | 11.860000 | 14.590000 | 82.000000 | 1016.000000 |  | 14.900000 | 0.000000 | 10000.000000 | 101.000000 | 2.32 | 1.600000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35020310_OWM_Clouds_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Clouds_20220203.png)
![CNE_IDEAM_Station35020310_OWM_Dewpoint_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Dewpoint_20220203.png)
![CNE_IDEAM_Station35020310_OWM_Feelslike_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Feelslike_20220203.png)
![CNE_IDEAM_Station35020310_OWM_Humidity_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Humidity_20220203.png)
![CNE_IDEAM_Station35020310_OWM_Pressure_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Pressure_20220203.png)
![CNE_IDEAM_Station35020310_OWM_Rain_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Rain_20220203.png)
![CNE_IDEAM_Station35020310_OWM_Temp_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Temp_20220203.png)
![CNE_IDEAM_Station35020310_OWM_UVI_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_UVI_20220203.png)
![CNE_IDEAM_Station35020310_OWM_Visibility_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Visibility_20220203.png)
![CNE_IDEAM_Station35020310_OWM_Winddeg_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Winddeg_20220203.png)
![CNE_IDEAM_Station35020310_OWM_Windgust_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Windgust_20220203.png)
![CNE_IDEAM_Station35020310_OWM_Windspeed_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Windspeed_20220203.png)

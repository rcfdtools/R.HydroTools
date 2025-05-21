
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35027150_OWM_20220203.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220203.csv)

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

### (CNE index 1623) Open Weather values for station 35027150 - ANIMAS LAS [35027150]

JSON data from API OWM:

```
{'lat': 4.138, 'lon': -74.1738, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643814483, 'sunrise': 1643800314, 'sunset': 1643843331, 'temp': 14.46, 'feels_like': 13.66, 'pressure': 1018, 'humidity': 65, 'dew_point': 7.97, 'uvi': 6.83, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 109, 'wind_gust': 1.96, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1643760000, 'temp': 11.46, 'feels_like': 11.04, 'pressure': 1017, 'humidity': 91, 'dew_point': 10.04, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 101, 'wind_gust': 1.79, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643763600, 'temp': 10.46, 'feels_like': 9.89, 'pressure': 1018, 'humidity': 89, 'dew_point': 8.73, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 101, 'wind_gust': 1.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643767200, 'temp': 10.46, 'feels_like': 9.89, 'pressure': 1018, 'humidity': 89, 'dew_point': 8.73, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 110, 'wind_gust': 1.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643770800, 'temp': 8.46, 'feels_like': 8.46, 'pressure': 1019, 'humidity': 90, 'dew_point': 6.92, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 125, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643774400, 'temp': 8.46, 'feels_like': 8.46, 'pressure': 1018, 'humidity': 90, 'dew_point': 6.92, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 121, 'wind_gust': 1.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643778000, 'temp': 6.46, 'feels_like': 6.46, 'pressure': 1018, 'humidity': 91, 'dew_point': 5.1, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 111, 'wind_gust': 1.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643781600, 'temp': 6.46, 'feels_like': 6.46, 'pressure': 1017, 'humidity': 89, 'dew_point': 4.78, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 122, 'wind_gust': 1.13, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643785200, 'temp': 7.46, 'feels_like': 7.46, 'pressure': 1017, 'humidity': 88, 'dew_point': 5.6, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 114, 'wind_gust': 1.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643788800, 'temp': 8.46, 'feels_like': 8.46, 'pressure': 1017, 'humidity': 90, 'dew_point': 6.92, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 112, 'wind_gust': 1.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643792400, 'temp': 7.46, 'feels_like': 7.46, 'pressure': 1017, 'humidity': 91, 'dew_point': 6.09, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 113, 'wind_gust': 1.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643796000, 'temp': 6.46, 'feels_like': 6.46, 'pressure': 1018, 'humidity': 91, 'dew_point': 5.1, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 117, 'wind_gust': 1.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1643799600, 'temp': 7.46, 'feels_like': 7.46, 'pressure': 1018, 'humidity': 91, 'dew_point': 6.09, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.1, 'wind_deg': 115, 'wind_gust': 2.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643803200, 'temp': 7.46, 'feels_like': 7.46, 'pressure': 1019, 'humidity': 87, 'dew_point': 5.44, 'uvi': 0.53, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 107, 'wind_gust': 2.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643806800, 'temp': 9.46, 'feels_like': 8.89, 'pressure': 1019, 'humidity': 80, 'dew_point': 6.19, 'uvi': 1.72, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.64, 'wind_deg': 107, 'wind_gust': 2.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643810400, 'temp': 12.46, 'feels_like': 11.62, 'pressure': 1019, 'humidity': 71, 'dew_point': 7.35, 'uvi': 4.07, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 108, 'wind_gust': 1.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643814000, 'temp': 14.46, 'feels_like': 13.66, 'pressure': 1018, 'humidity': 65, 'dew_point': 7.97, 'uvi': 6.83, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 109, 'wind_gust': 1.96, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643817600, 'temp': 16.46, 'feels_like': 15.81, 'pressure': 1017, 'humidity': 63, 'dew_point': 9.4, 'uvi': 12.64, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 114, 'wind_gust': 2.08, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643821200, 'temp': 16.46, 'feels_like': 15.83, 'pressure': 1016, 'humidity': 64, 'dew_point': 9.64, 'uvi': 13.74, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 95, 'wind_gust': 2.14, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1643824800, 'temp': 15.46, 'feels_like': 14.73, 'pressure': 1015, 'humidity': 64, 'dew_point': 8.69, 'uvi': 12.47, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 87, 'wind_gust': 2.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.23}}, {'dt': 1643828400, 'temp': 16.46, 'feels_like': 15.91, 'pressure': 1014, 'humidity': 67, 'dew_point': 10.32, 'uvi': 9.05, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 102, 'wind_gust': 2.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.25}}, {'dt': 1643832000, 'temp': 16.46, 'feels_like': 16.02, 'pressure': 1014, 'humidity': 71, 'dew_point': 11.19, 'uvi': 5.27, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 111, 'wind_gust': 2.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1643835600, 'temp': 15.46, 'feels_like': 14.99, 'pressure': 1014, 'humidity': 74, 'dew_point': 10.85, 'uvi': 2.17, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.71, 'wind_deg': 114, 'wind_gust': 2.4, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1643839200, 'temp': 14.46, 'feels_like': 13.95, 'pressure': 1015, 'humidity': 76, 'dew_point': 10.29, 'uvi': 0.39, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.95, 'wind_deg': 112, 'wind_gust': 2.37, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1643842800, 'temp': 12.46, 'feels_like': 11.95, 'pressure': 1016, 'humidity': 84, 'dew_point': 9.83, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.75, 'wind_deg': 101, 'wind_gust': 2.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 00:00:00 | 82.000000 | 10.040000 | 11.040000 | 91.000000 | 1017.000000 |  | 11.460000 | 0.000000 | 10000.000000 | 101.000000 | 1.79 | 1.330000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 01:00:00 | 91.000000 | 8.730000 | 9.890000 | 89.000000 | 1018.000000 |  | 10.460000 | 0.000000 | 10000.000000 | 101.000000 | 1.49 | 1.060000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 02:00:00 | 92.000000 | 8.730000 | 9.890000 | 89.000000 | 1018.000000 |  | 10.460000 | 0.000000 | 10000.000000 | 110.000000 | 1.46 | 0.900000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 03:00:00 | 95.000000 | 6.920000 | 8.460000 | 90.000000 | 1019.000000 |  | 8.460000 | 0.000000 | 10000.000000 | 125.000000 | 1.18 | 0.640000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 04:00:00 | 96.000000 | 6.920000 | 8.460000 | 90.000000 | 1018.000000 |  | 8.460000 | 0.000000 | 10000.000000 | 121.000000 | 1.04 | 0.560000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 05:00:00 | 96.000000 | 5.100000 | 6.460000 | 91.000000 | 1018.000000 |  | 6.460000 | 0.000000 | 10000.000000 | 111.000000 | 1.25 | 0.900000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 06:00:00 | 94.000000 | 4.780000 | 6.460000 | 89.000000 | 1017.000000 |  | 6.460000 | 0.000000 | 10000.000000 | 122.000000 | 1.13 | 0.620000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 07:00:00 | 99.000000 | 5.600000 | 7.460000 | 88.000000 | 1017.000000 |  | 7.460000 | 0.000000 | 10000.000000 | 114.000000 | 1.2 | 0.610000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 08:00:00 | 100.000000 | 6.920000 | 8.460000 | 90.000000 | 1017.000000 |  | 8.460000 | 0.000000 | 10000.000000 | 112.000000 | 1.48 | 0.870000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 09:00:00 | 100.000000 | 6.090000 | 7.460000 | 91.000000 | 1017.000000 |  | 7.460000 | 0.000000 | 10000.000000 | 113.000000 | 1.75 | 1.070000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 10:00:00 | 100.000000 | 5.100000 | 6.460000 | 91.000000 | 1018.000000 | 0.11 | 6.460000 | 0.000000 | 10000.000000 | 117.000000 | 1.85 | 1.080000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 11:00:00 | 100.000000 | 6.090000 | 7.460000 | 91.000000 | 1018.000000 |  | 7.460000 | 0.000000 | 10000.000000 | 115.000000 | 2.09 | 1.100000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 12:00:00 | 95.000000 | 5.440000 | 7.460000 | 87.000000 | 1019.000000 |  | 7.460000 | 0.530000 | 10000.000000 | 107.000000 | 2.36 | 1.330000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 13:00:00 | 100.000000 | 6.190000 | 8.890000 | 80.000000 | 1019.000000 |  | 9.460000 | 1.720000 | 10000.000000 | 107.000000 | 2.21 | 1.640000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 14:00:00 | 92.000000 | 7.350000 | 11.620000 | 71.000000 | 1019.000000 |  | 12.460000 | 4.070000 | 10000.000000 | 108.000000 | 1.82 | 1.360000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 15:00:00 | 83.000000 | 7.970000 | 13.660000 | 65.000000 | 1018.000000 |  | 14.460000 | 6.830000 | 10000.000000 | 109.000000 | 1.96 | 0.950000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 16:00:00 | 81.000000 | 9.400000 | 15.810000 | 63.000000 | 1017.000000 |  | 16.460000 | 12.640000 | 10000.000000 | 114.000000 | 2.08 | 0.680000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 17:00:00 | 82.000000 | 9.640000 | 15.830000 | 64.000000 | 1016.000000 | 0.16 | 16.460000 | 13.740000 | 10000.000000 | 95.000000 | 2.14 | 0.790000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 18:00:00 | 100.000000 | 8.690000 | 14.730000 | 64.000000 | 1015.000000 | 0.23 | 15.460000 | 12.470000 | 10000.000000 | 87.000000 | 2.55 | 0.840000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 19:00:00 | 100.000000 | 10.320000 | 15.910000 | 67.000000 | 1014.000000 | 0.25 | 16.460000 | 9.050000 | 10000.000000 | 102.000000 | 2.45 | 1.070000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 20:00:00 | 100.000000 | 11.190000 | 16.020000 | 71.000000 | 1014.000000 | 0.33 | 16.460000 | 5.270000 | 10000.000000 | 111.000000 | 2.27 | 1.560000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 21:00:00 | 100.000000 | 10.850000 | 14.990000 | 74.000000 | 1014.000000 | 0.2 | 15.460000 | 2.170000 | 10000.000000 | 114.000000 | 2.4 | 1.710000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 22:00:00 | 100.000000 | 10.290000 | 13.950000 | 76.000000 | 1015.000000 | 0.2 | 14.460000 | 0.390000 | 10000.000000 | 112.000000 | 2.37 | 1.950000 | 500 | Rain | light rain | 10d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-02 23:00:00 | 100.000000 | 9.830000 | 11.950000 | 84.000000 | 1016.000000 |  | 12.460000 | 0.000000 | 10000.000000 | 101.000000 | 2.4 | 1.750000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35027150_OWM_Clouds_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Clouds_20220203.png)
![CNE_IDEAM_Station35027150_OWM_Dewpoint_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Dewpoint_20220203.png)
![CNE_IDEAM_Station35027150_OWM_Feelslike_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Feelslike_20220203.png)
![CNE_IDEAM_Station35027150_OWM_Humidity_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Humidity_20220203.png)
![CNE_IDEAM_Station35027150_OWM_Pressure_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Pressure_20220203.png)
![CNE_IDEAM_Station35027150_OWM_Rain_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Rain_20220203.png)
![CNE_IDEAM_Station35027150_OWM_Temp_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Temp_20220203.png)
![CNE_IDEAM_Station35027150_OWM_UVI_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_UVI_20220203.png)
![CNE_IDEAM_Station35027150_OWM_Visibility_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Visibility_20220203.png)
![CNE_IDEAM_Station35027150_OWM_Winddeg_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Winddeg_20220203.png)
![CNE_IDEAM_Station35027150_OWM_Windgust_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Windgust_20220203.png)
![CNE_IDEAM_Station35027150_OWM_Windspeed_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Windspeed_20220203.png)

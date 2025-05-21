
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ESCUELA LA UNION [21201200] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201200_OWM_20220203.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220203.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.34294444,-74.18388889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.34294444&lon=-74.18388889)

| Parameter | Value |
|---|---|
| Code | 21201200 |
| Name | ESCUELA LA UNION [21201200] |
| Latitude, ° | 4.34294444 |
| Longitude, ° | -74.18388889 |
| Elevation, m | 3320 |
| Category | Pluviométrica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1985-03-14 19:00:00 |
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

### (CNE index 3319) Open Weather values for station 21201200 - ESCUELA LA UNION [21201200]

JSON data from API OWM:

```
{'lat': 4.3429, 'lon': -74.1839, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643814483, 'sunrise': 1643800331, 'sunset': 1643843319, 'temp': 11.98, 'feels_like': 10.83, 'pressure': 1017, 'humidity': 61, 'dew_point': 4.7, 'uvi': 6.83, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.22, 'wind_deg': 35, 'wind_gust': 1.94, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1643760000, 'temp': 8.98, 'feels_like': 8.5, 'pressure': 1016, 'humidity': 87, 'dew_point': 6.94, 'uvi': 0, 'clouds': 64, 'visibility': 10000, 'wind_speed': 1.49, 'wind_deg': 113, 'wind_gust': 1.86, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643763600, 'temp': 7.98, 'feels_like': 7.28, 'pressure': 1017, 'humidity': 87, 'dew_point': 5.95, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 117, 'wind_gust': 1.86, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643767200, 'temp': 7.98, 'feels_like': 7.28, 'pressure': 1018, 'humidity': 87, 'dew_point': 5.95, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 121, 'wind_gust': 2.08, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643770800, 'temp': 5.98, 'feels_like': 5.23, 'pressure': 1018, 'humidity': 87, 'dew_point': 3.98, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 128, 'wind_gust': 1.91, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643774400, 'temp': 5.98, 'feels_like': 5.98, 'pressure': 1018, 'humidity': 86, 'dew_point': 3.82, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 122, 'wind_gust': 1.69, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643778000, 'temp': 3.98, 'feels_like': 2.76, 'pressure': 1018, 'humidity': 86, 'dew_point': 1.85, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.52, 'wind_deg': 112, 'wind_gust': 1.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643781600, 'temp': 3.98, 'feels_like': 3.98, 'pressure': 1017, 'humidity': 84, 'dew_point': 1.53, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 106, 'wind_gust': 1.43, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643785200, 'temp': 4.98, 'feels_like': 4.98, 'pressure': 1016, 'humidity': 85, 'dew_point': 2.67, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.26, 'wind_deg': 102, 'wind_gust': 1.62, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643788800, 'temp': 5.98, 'feels_like': 5.19, 'pressure': 1016, 'humidity': 86, 'dew_point': 3.82, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.4, 'wind_deg': 101, 'wind_gust': 1.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643792400, 'temp': 4.98, 'feels_like': 3.7, 'pressure': 1017, 'humidity': 86, 'dew_point': 2.84, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 103, 'wind_gust': 2.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643796000, 'temp': 3.98, 'feels_like': 2.46, 'pressure': 1017, 'humidity': 87, 'dew_point': 2.02, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.75, 'wind_deg': 105, 'wind_gust': 2.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643799600, 'temp': 4.98, 'feels_like': 3.55, 'pressure': 1017, 'humidity': 86, 'dew_point': 2.84, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 105, 'wind_gust': 2.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643803200, 'temp': 4.98, 'feels_like': 3.58, 'pressure': 1018, 'humidity': 83, 'dew_point': 2.34, 'uvi': 0.53, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.78, 'wind_deg': 99, 'wind_gust': 2.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643806800, 'temp': 6.98, 'feels_like': 5.96, 'pressure': 1018, 'humidity': 77, 'dew_point': 3.23, 'uvi': 1.72, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 103, 'wind_gust': 2.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643810400, 'temp': 9.98, 'feels_like': 9.98, 'pressure': 1018, 'humidity': 67, 'dew_point': 4.14, 'uvi': 4.07, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 102, 'wind_gust': 1.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643814000, 'temp': 11.98, 'feels_like': 10.83, 'pressure': 1017, 'humidity': 61, 'dew_point': 4.7, 'uvi': 6.83, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.22, 'wind_deg': 35, 'wind_gust': 1.94, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643817600, 'temp': 13.98, 'feels_like': 13, 'pressure': 1016, 'humidity': 60, 'dew_point': 6.35, 'uvi': 12.64, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 327, 'wind_gust': 2.39, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643821200, 'temp': 13.98, 'feels_like': 13.08, 'pressure': 1015, 'humidity': 63, 'dew_point': 7.06, 'uvi': 13.74, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 336, 'wind_gust': 2.32, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1643824800, 'temp': 12.98, 'feels_like': 12, 'pressure': 1014, 'humidity': 64, 'dew_point': 6.34, 'uvi': 12.47, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 333, 'wind_gust': 2.29, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.32}}, {'dt': 1643828400, 'temp': 13.98, 'feels_like': 13.13, 'pressure': 1013, 'humidity': 65, 'dew_point': 7.51, 'uvi': 9.05, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 337, 'wind_gust': 2.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.35}}, {'dt': 1643832000, 'temp': 13.98, 'feels_like': 13.21, 'pressure': 1013, 'humidity': 68, 'dew_point': 8.18, 'uvi': 5.27, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.16, 'wind_deg': 192, 'wind_gust': 2.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.39}}, {'dt': 1643835600, 'temp': 12.98, 'feels_like': 12.19, 'pressure': 1013, 'humidity': 71, 'dew_point': 7.85, 'uvi': 2.17, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 151, 'wind_gust': 2.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1643839200, 'temp': 11.98, 'feels_like': 11.14, 'pressure': 1013, 'humidity': 73, 'dew_point': 7.3, 'uvi': 0.39, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 110, 'wind_gust': 1.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1643842800, 'temp': 9.98, 'feels_like': 9.62, 'pressure': 1015, 'humidity': 80, 'dew_point': 6.69, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 100, 'wind_gust': 2.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 00:00:00 | 64.000000 | 6.940000 | 8.500000 | 87.000000 | 1016.000000 |  | 8.980000 | 0.000000 | 10000.000000 | 113.000000 | 1.86 | 1.490000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 01:00:00 | 76.000000 | 5.950000 | 7.280000 | 87.000000 | 1017.000000 |  | 7.980000 | 0.000000 | 10000.000000 | 117.000000 | 1.86 | 1.560000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 02:00:00 | 71.000000 | 5.950000 | 7.280000 | 87.000000 | 1018.000000 |  | 7.980000 | 0.000000 | 10000.000000 | 121.000000 | 2.08 | 1.560000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 03:00:00 | 72.000000 | 3.980000 | 5.230000 | 87.000000 | 1018.000000 |  | 5.980000 | 0.000000 | 10000.000000 | 128.000000 | 1.91 | 1.370000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 04:00:00 | 72.000000 | 3.820000 | 5.980000 | 86.000000 | 1018.000000 |  | 5.980000 | 0.000000 | 10000.000000 | 122.000000 | 1.69 | 1.280000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 05:00:00 | 73.000000 | 1.850000 | 2.760000 | 86.000000 | 1018.000000 |  | 3.980000 | 0.000000 | 10000.000000 | 112.000000 | 1.76 | 1.520000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 06:00:00 | 94.000000 | 1.530000 | 3.980000 | 84.000000 | 1017.000000 |  | 3.980000 | 0.000000 | 10000.000000 | 106.000000 | 1.43 | 1.170000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 07:00:00 | 99.000000 | 2.670000 | 4.980000 | 85.000000 | 1016.000000 |  | 4.980000 | 0.000000 | 10000.000000 | 102.000000 | 1.62 | 1.260000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 08:00:00 | 100.000000 | 3.820000 | 5.190000 | 86.000000 | 1016.000000 |  | 5.980000 | 0.000000 | 10000.000000 | 101.000000 | 1.81 | 1.400000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 09:00:00 | 99.000000 | 2.840000 | 3.700000 | 86.000000 | 1017.000000 |  | 4.980000 | 0.000000 | 10000.000000 | 103.000000 | 2.01 | 1.680000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 10:00:00 | 100.000000 | 2.020000 | 2.460000 | 87.000000 | 1017.000000 |  | 3.980000 | 0.000000 | 10000.000000 | 105.000000 | 2.11 | 1.750000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 11:00:00 | 100.000000 | 2.840000 | 3.550000 | 86.000000 | 1017.000000 |  | 4.980000 | 0.000000 | 10000.000000 | 105.000000 | 2.33 | 1.810000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 12:00:00 | 95.000000 | 2.340000 | 3.580000 | 83.000000 | 1018.000000 |  | 4.980000 | 0.530000 | 10000.000000 | 99.000000 | 2.58 | 1.780000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 13:00:00 | 100.000000 | 3.230000 | 5.960000 | 77.000000 | 1018.000000 |  | 6.980000 | 1.720000 | 10000.000000 | 103.000000 | 2.42 | 1.720000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 14:00:00 | 94.000000 | 4.140000 | 9.980000 | 67.000000 | 1018.000000 |  | 9.980000 | 4.070000 | 10000.000000 | 102.000000 | 1.82 | 0.910000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 15:00:00 | 84.000000 | 4.700000 | 10.830000 | 61.000000 | 1017.000000 |  | 11.980000 | 6.830000 | 10000.000000 | 35.000000 | 1.94 | 0.220000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 16:00:00 | 81.000000 | 6.350000 | 13.000000 | 60.000000 | 1016.000000 |  | 13.980000 | 12.640000 | 10000.000000 | 327.000000 | 2.39 | 0.600000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 17:00:00 | 82.000000 | 7.060000 | 13.080000 | 63.000000 | 1015.000000 | 0.18 | 13.980000 | 13.740000 | 10000.000000 | 336.000000 | 2.32 | 0.670000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 18:00:00 | 99.000000 | 6.340000 | 12.000000 | 64.000000 | 1014.000000 | 0.32 | 12.980000 | 12.470000 | 10000.000000 | 333.000000 | 2.29 | 0.480000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 19:00:00 | 100.000000 | 7.510000 | 13.130000 | 65.000000 | 1013.000000 | 0.35 | 13.980000 | 9.050000 | 10000.000000 | 337.000000 | 2.38 | 0.360000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 20:00:00 | 95.000000 | 8.180000 | 13.210000 | 68.000000 | 1013.000000 | 0.39 | 13.980000 | 5.270000 | 10000.000000 | 192.000000 | 2.21 | 0.160000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 21:00:00 | 97.000000 | 7.850000 | 12.190000 | 71.000000 | 1013.000000 | 0.26 | 12.980000 | 2.170000 | 10000.000000 | 151.000000 | 2.21 | 0.360000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 22:00:00 | 97.000000 | 7.300000 | 11.140000 | 73.000000 | 1013.000000 | 0.29 | 11.980000 | 0.390000 | 10000.000000 | 110.000000 | 1.99 | 1.040000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 23:00:00 | 98.000000 | 6.690000 | 9.620000 | 80.000000 | 1015.000000 | 0.17 | 9.980000 | 0.000000 | 10000.000000 | 100.000000 | 2.24 | 1.510000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21201200_OWM_Clouds_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Clouds_20220203.png)
![CNE_IDEAM_Station21201200_OWM_Dewpoint_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Dewpoint_20220203.png)
![CNE_IDEAM_Station21201200_OWM_Feelslike_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Feelslike_20220203.png)
![CNE_IDEAM_Station21201200_OWM_Humidity_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Humidity_20220203.png)
![CNE_IDEAM_Station21201200_OWM_Pressure_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Pressure_20220203.png)
![CNE_IDEAM_Station21201200_OWM_Rain_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Rain_20220203.png)
![CNE_IDEAM_Station21201200_OWM_Temp_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Temp_20220203.png)
![CNE_IDEAM_Station21201200_OWM_UVI_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_UVI_20220203.png)
![CNE_IDEAM_Station21201200_OWM_Visibility_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Visibility_20220203.png)
![CNE_IDEAM_Station21201200_OWM_Winddeg_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Winddeg_20220203.png)
![CNE_IDEAM_Station21201200_OWM_Windgust_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Windgust_20220203.png)
![CNE_IDEAM_Station21201200_OWM_Windspeed_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Windspeed_20220203.png)

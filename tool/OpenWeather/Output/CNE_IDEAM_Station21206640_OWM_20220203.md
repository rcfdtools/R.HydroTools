
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SAN JOSE [21206640] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206640_OWM_20220203.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220203.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.50155556,-74.11930556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.50155556&lon=-74.11930556)

| Parameter | Value |
|---|---|
| Code | 21206640 |
| Name | SAN JOSE [21206640] |
| Latitude, ° | 4.50155556 |
| Longitude, ° | -74.11930556 |
| Elevation, m | 2700 |
| Category | Climática Ordinaria |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 2001-11-15 00:00:00 |
| Suspension date | 2011-05-10 00:00:00 |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Guaviare |
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

### (CNE index 2378) Open Weather values for station 21206640 - SAN JOSE [21206640]

JSON data from API OWM:

```
{'lat': 4.5016, 'lon': -74.1193, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643814483, 'sunrise': 1643800327, 'sunset': 1643843292, 'temp': 16.03, 'feels_like': 15.15, 'pressure': 1017, 'humidity': 56, 'dew_point': 7.26, 'uvi': 9.17, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.1, 'wind_deg': 137, 'wind_gust': 2.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1643760000, 'temp': 13.03, 'feels_like': 12.58, 'pressure': 1016, 'humidity': 84, 'dew_point': 10.39, 'uvi': 0, 'clouds': 56, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 140, 'wind_gust': 2.18, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643763600, 'temp': 12.03, 'feels_like': 11.53, 'pressure': 1017, 'humidity': 86, 'dew_point': 9.76, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.63, 'wind_deg': 142, 'wind_gust': 2.06, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643767200, 'temp': 12.03, 'feels_like': 11.56, 'pressure': 1018, 'humidity': 87, 'dew_point': 9.94, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1.84, 'wind_deg': 142, 'wind_gust': 2.35, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643770800, 'temp': 10.03, 'feels_like': 9.39, 'pressure': 1018, 'humidity': 88, 'dew_point': 8.14, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 1.8, 'wind_deg': 139, 'wind_gust': 2.43, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643774400, 'temp': 10.03, 'feels_like': 9.36, 'pressure': 1018, 'humidity': 87, 'dew_point': 7.97, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 134, 'wind_gust': 2.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643778000, 'temp': 8.03, 'feels_like': 7.13, 'pressure': 1018, 'humidity': 86, 'dew_point': 5.83, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.75, 'wind_deg': 129, 'wind_gust': 1.99, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643781600, 'temp': 8.03, 'feels_like': 7.18, 'pressure': 1017, 'humidity': 86, 'dew_point': 5.83, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.71, 'wind_deg': 117, 'wind_gust': 1.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643785200, 'temp': 9.03, 'feels_like': 8.18, 'pressure': 1017, 'humidity': 85, 'dew_point': 6.65, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.87, 'wind_deg': 118, 'wind_gust': 2.13, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643788800, 'temp': 10.03, 'feels_like': 9.31, 'pressure': 1016, 'humidity': 85, 'dew_point': 7.63, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.03, 'wind_deg': 117, 'wind_gust': 2.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643792400, 'temp': 9.03, 'feels_like': 7.9, 'pressure': 1017, 'humidity': 85, 'dew_point': 6.65, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.2, 'wind_deg': 115, 'wind_gust': 2.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643796000, 'temp': 8.03, 'feels_like': 6.64, 'pressure': 1017, 'humidity': 86, 'dew_point': 5.83, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.31, 'wind_deg': 115, 'wind_gust': 2.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643799600, 'temp': 9.03, 'feels_like': 7.79, 'pressure': 1017, 'humidity': 86, 'dew_point': 6.82, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.34, 'wind_deg': 114, 'wind_gust': 2.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643803200, 'temp': 9.03, 'feels_like': 7.88, 'pressure': 1018, 'humidity': 83, 'dew_point': 6.3, 'uvi': 0.54, 'clouds': 94, 'visibility': 10000, 'wind_speed': 2.22, 'wind_deg': 113, 'wind_gust': 2.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643806800, 'temp': 11.03, 'feels_like': 10.09, 'pressure': 1018, 'humidity': 73, 'dew_point': 6.38, 'uvi': 2.3, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.01, 'wind_deg': 119, 'wind_gust': 2.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643810400, 'temp': 14.03, 'feels_like': 13.11, 'pressure': 1018, 'humidity': 62, 'dew_point': 6.87, 'uvi': 5.45, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 127, 'wind_gust': 2.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643814000, 'temp': 16.03, 'feels_like': 15.15, 'pressure': 1017, 'humidity': 56, 'dew_point': 7.26, 'uvi': 9.17, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.1, 'wind_deg': 137, 'wind_gust': 2.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643817600, 'temp': 18.03, 'feels_like': 17.19, 'pressure': 1015, 'humidity': 50, 'dew_point': 7.46, 'uvi': 12.18, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 150, 'wind_gust': 2.66, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643821200, 'temp': 18.03, 'feels_like': 17.17, 'pressure': 1014, 'humidity': 49, 'dew_point': 7.17, 'uvi': 13.25, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 187, 'wind_gust': 2.62, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643824800, 'temp': 17.03, 'feels_like': 16.17, 'pressure': 1013, 'humidity': 53, 'dew_point': 7.39, 'uvi': 12.02, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 189, 'wind_gust': 2.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1643828400, 'temp': 18.03, 'feels_like': 17.25, 'pressure': 1012, 'humidity': 52, 'dew_point': 8.04, 'uvi': 7.48, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 179, 'wind_gust': 2.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1643832000, 'temp': 18.03, 'feels_like': 17.27, 'pressure': 1011, 'humidity': 53, 'dew_point': 8.32, 'uvi': 4.35, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 180, 'wind_gust': 2.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1643835600, 'temp': 17.03, 'feels_like': 16.33, 'pressure': 1011, 'humidity': 59, 'dew_point': 8.97, 'uvi': 1.78, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 174, 'wind_gust': 2.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1643839200, 'temp': 16.03, 'feels_like': 15.33, 'pressure': 1012, 'humidity': 63, 'dew_point': 9, 'uvi': 0.42, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 148, 'wind_gust': 2.04, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1643842800, 'temp': 14.03, 'feels_like': 13.45, 'pressure': 1014, 'humidity': 75, 'dew_point': 9.67, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.63, 'wind_deg': 136, 'wind_gust': 2.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 00:00:00 | 56.000000 | 10.390000 | 12.580000 | 84.000000 | 1016.000000 |  | 13.030000 | 0.000000 | 10000.000000 | 140.000000 | 2.18 | 1.570000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 01:00:00 | 70.000000 | 9.760000 | 11.530000 | 86.000000 | 1017.000000 |  | 12.030000 | 0.000000 | 10000.000000 | 142.000000 | 2.06 | 1.630000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 02:00:00 | 63.000000 | 9.940000 | 11.560000 | 87.000000 | 1018.000000 |  | 12.030000 | 0.000000 | 10000.000000 | 142.000000 | 2.35 | 1.840000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 03:00:00 | 60.000000 | 8.140000 | 9.390000 | 88.000000 | 1018.000000 |  | 10.030000 | 0.000000 | 10000.000000 | 139.000000 | 2.43 | 1.800000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 04:00:00 | 58.000000 | 7.970000 | 9.360000 | 87.000000 | 1018.000000 |  | 10.030000 | 0.000000 | 10000.000000 | 134.000000 | 2.07 | 1.730000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 05:00:00 | 57.000000 | 5.830000 | 7.130000 | 86.000000 | 1018.000000 |  | 8.030000 | 0.000000 | 10000.000000 | 129.000000 | 1.99 | 1.750000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 06:00:00 | 92.000000 | 5.830000 | 7.180000 | 86.000000 | 1017.000000 |  | 8.030000 | 0.000000 | 10000.000000 | 117.000000 | 1.67 | 1.710000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 07:00:00 | 100.000000 | 6.650000 | 8.180000 | 85.000000 | 1017.000000 |  | 9.030000 | 0.000000 | 10000.000000 | 118.000000 | 2.13 | 1.870000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 08:00:00 | 100.000000 | 7.630000 | 9.310000 | 85.000000 | 1016.000000 |  | 10.030000 | 0.000000 | 10000.000000 | 117.000000 | 2.29 | 2.030000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 09:00:00 | 99.000000 | 6.650000 | 7.900000 | 85.000000 | 1017.000000 |  | 9.030000 | 0.000000 | 10000.000000 | 115.000000 | 2.48 | 2.200000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 10:00:00 | 99.000000 | 5.830000 | 6.640000 | 86.000000 | 1017.000000 |  | 8.030000 | 0.000000 | 10000.000000 | 115.000000 | 2.63 | 2.310000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 11:00:00 | 99.000000 | 6.820000 | 7.790000 | 86.000000 | 1017.000000 |  | 9.030000 | 0.000000 | 10000.000000 | 114.000000 | 2.8 | 2.340000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 12:00:00 | 94.000000 | 6.300000 | 7.880000 | 83.000000 | 1018.000000 |  | 9.030000 | 0.540000 | 10000.000000 | 113.000000 | 2.78 | 2.220000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 13:00:00 | 100.000000 | 6.380000 | 10.090000 | 73.000000 | 1018.000000 |  | 11.030000 | 2.300000 | 10000.000000 | 119.000000 | 2.67 | 2.010000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 14:00:00 | 99.000000 | 6.870000 | 13.110000 | 62.000000 | 1018.000000 |  | 14.030000 | 5.450000 | 10000.000000 | 127.000000 | 2.29 | 1.420000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 15:00:00 | 91.000000 | 7.260000 | 15.150000 | 56.000000 | 1017.000000 |  | 16.030000 | 9.170000 | 10000.000000 | 137.000000 | 2.14 | 1.100000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 16:00:00 | 79.000000 | 7.460000 | 17.190000 | 50.000000 | 1015.000000 |  | 18.030000 | 12.180000 | 10000.000000 | 150.000000 | 2.66 | 0.620000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 17:00:00 | 76.000000 | 7.170000 | 17.170000 | 49.000000 | 1014.000000 |  | 18.030000 | 13.250000 | 10000.000000 | 187.000000 | 2.62 | 0.820000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 18:00:00 | 98.000000 | 7.390000 | 16.170000 | 53.000000 | 1013.000000 | 0.18 | 17.030000 | 12.020000 | 10000.000000 | 189.000000 | 2.18 | 1.620000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 19:00:00 | 100.000000 | 8.040000 | 17.250000 | 52.000000 | 1012.000000 | 0.21 | 18.030000 | 7.480000 | 10000.000000 | 179.000000 | 2.27 | 1.370000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 20:00:00 | 83.000000 | 8.320000 | 17.270000 | 53.000000 | 1011.000000 | 0.21 | 18.030000 | 4.350000 | 10000.000000 | 180.000000 | 2.53 | 1.200000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 21:00:00 | 88.000000 | 8.970000 | 16.330000 | 59.000000 | 1011.000000 | 0.15 | 17.030000 | 1.780000 | 10000.000000 | 174.000000 | 2.41 | 1.230000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 22:00:00 | 90.000000 | 9.000000 | 15.330000 | 63.000000 | 1012.000000 | 0.18 | 16.030000 | 0.420000 | 10000.000000 | 148.000000 | 2.04 | 1.370000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 23:00:00 | 92.000000 | 9.670000 | 13.450000 | 75.000000 | 1014.000000 | 0.15 | 14.030000 | 0.000000 | 10000.000000 | 136.000000 | 2.61 | 1.630000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21206640_OWM_Clouds_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Clouds_20220203.png)
![CNE_IDEAM_Station21206640_OWM_Dewpoint_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Dewpoint_20220203.png)
![CNE_IDEAM_Station21206640_OWM_Feelslike_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Feelslike_20220203.png)
![CNE_IDEAM_Station21206640_OWM_Humidity_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Humidity_20220203.png)
![CNE_IDEAM_Station21206640_OWM_Pressure_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Pressure_20220203.png)
![CNE_IDEAM_Station21206640_OWM_Rain_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Rain_20220203.png)
![CNE_IDEAM_Station21206640_OWM_Temp_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Temp_20220203.png)
![CNE_IDEAM_Station21206640_OWM_UVI_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_UVI_20220203.png)
![CNE_IDEAM_Station21206640_OWM_Visibility_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Visibility_20220203.png)
![CNE_IDEAM_Station21206640_OWM_Winddeg_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Winddeg_20220203.png)
![CNE_IDEAM_Station21206640_OWM_Windgust_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Windgust_20220203.png)
![CNE_IDEAM_Station21206640_OWM_Windspeed_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Windspeed_20220203.png)

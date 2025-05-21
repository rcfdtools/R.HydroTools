
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201240_OWM_20220203.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220203.csv)

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

### (CNE index 2078) Open Weather values for station 21201240 - SANTA MARIA DE USME [21201240]

JSON data from API OWM:

```
{'lat': 4.4813, 'lon': -74.1263, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643814483, 'sunrise': 1643800327, 'sunset': 1643843295, 'temp': 16.14, 'feels_like': 15.27, 'pressure': 1017, 'humidity': 56, 'dew_point': 7.37, 'uvi': 6.83, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 134, 'wind_gust': 2.1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1643760000, 'temp': 13.14, 'feels_like': 12.7, 'pressure': 1016, 'humidity': 84, 'dew_point': 10.5, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 137, 'wind_gust': 2.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643763600, 'temp': 12.14, 'feels_like': 11.66, 'pressure': 1017, 'humidity': 86, 'dew_point': 9.87, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 140, 'wind_gust': 2.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643767200, 'temp': 12.14, 'feels_like': 11.68, 'pressure': 1018, 'humidity': 87, 'dew_point': 10.04, 'uvi': 0, 'clouds': 64, 'visibility': 10000, 'wind_speed': 1.8, 'wind_deg': 140, 'wind_gust': 2.3, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643770800, 'temp': 10.14, 'feels_like': 9.51, 'pressure': 1018, 'humidity': 88, 'dew_point': 8.24, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 1.76, 'wind_deg': 138, 'wind_gust': 2.38, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643774400, 'temp': 10.14, 'feels_like': 9.48, 'pressure': 1018, 'humidity': 87, 'dew_point': 8.08, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 133, 'wind_gust': 2.04, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643778000, 'temp': 8.14, 'feels_like': 7.28, 'pressure': 1018, 'humidity': 86, 'dew_point': 5.94, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 127, 'wind_gust': 1.98, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643781600, 'temp': 8.14, 'feels_like': 7.34, 'pressure': 1017, 'humidity': 85, 'dew_point': 5.77, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.67, 'wind_deg': 117, 'wind_gust': 1.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643785200, 'temp': 9.14, 'feels_like': 8.36, 'pressure': 1017, 'humidity': 85, 'dew_point': 6.75, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 117, 'wind_gust': 2.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643788800, 'temp': 10.14, 'feels_like': 9.43, 'pressure': 1016, 'humidity': 85, 'dew_point': 7.74, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.97, 'wind_deg': 116, 'wind_gust': 2.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643792400, 'temp': 9.14, 'feels_like': 8.06, 'pressure': 1017, 'humidity': 85, 'dew_point': 6.75, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.16, 'wind_deg': 114, 'wind_gust': 2.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643796000, 'temp': 8.14, 'feels_like': 6.81, 'pressure': 1017, 'humidity': 86, 'dew_point': 5.94, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.25, 'wind_deg': 114, 'wind_gust': 2.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643799600, 'temp': 9.14, 'feels_like': 7.97, 'pressure': 1017, 'humidity': 86, 'dew_point': 6.92, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.28, 'wind_deg': 114, 'wind_gust': 2.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643803200, 'temp': 9.14, 'feels_like': 8.05, 'pressure': 1018, 'humidity': 83, 'dew_point': 6.41, 'uvi': 0.53, 'clouds': 94, 'visibility': 10000, 'wind_speed': 2.17, 'wind_deg': 111, 'wind_gust': 2.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643806800, 'temp': 11.14, 'feels_like': 10.24, 'pressure': 1018, 'humidity': 74, 'dew_point': 6.69, 'uvi': 1.72, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.98, 'wind_deg': 117, 'wind_gust': 2.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643810400, 'temp': 14.14, 'feels_like': 13.25, 'pressure': 1018, 'humidity': 63, 'dew_point': 7.21, 'uvi': 4.07, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 124, 'wind_gust': 2.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643814000, 'temp': 16.14, 'feels_like': 15.27, 'pressure': 1017, 'humidity': 56, 'dew_point': 7.37, 'uvi': 6.83, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 134, 'wind_gust': 2.1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643817600, 'temp': 18.14, 'feels_like': 17.37, 'pressure': 1015, 'humidity': 52, 'dew_point': 8.14, 'uvi': 12.64, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 146, 'wind_gust': 2.62, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643821200, 'temp': 18.14, 'feels_like': 17.34, 'pressure': 1014, 'humidity': 51, 'dew_point': 7.85, 'uvi': 13.74, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 190, 'wind_gust': 2.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643824800, 'temp': 17.14, 'feels_like': 16.32, 'pressure': 1013, 'humidity': 54, 'dew_point': 7.77, 'uvi': 12.47, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.39, 'wind_deg': 189, 'wind_gust': 2.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1643828400, 'temp': 18.14, 'feels_like': 17.39, 'pressure': 1012, 'humidity': 53, 'dew_point': 8.42, 'uvi': 9.05, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 179, 'wind_gust': 2.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1643832000, 'temp': 18.14, 'feels_like': 17.42, 'pressure': 1011, 'humidity': 54, 'dew_point': 8.69, 'uvi': 5.27, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 181, 'wind_gust': 2.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.23}}, {'dt': 1643835600, 'temp': 17.14, 'feels_like': 16.48, 'pressure': 1012, 'humidity': 60, 'dew_point': 9.32, 'uvi': 2.17, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 174, 'wind_gust': 2.39, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1643839200, 'temp': 16.14, 'feels_like': 15.48, 'pressure': 1012, 'humidity': 64, 'dew_point': 9.33, 'uvi': 0.39, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 144, 'wind_gust': 2.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1643842800, 'temp': 14.14, 'feels_like': 13.57, 'pressure': 1014, 'humidity': 75, 'dew_point': 9.78, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.58, 'wind_deg': 132, 'wind_gust': 2.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 00:00:00 | 57.000000 | 10.500000 | 12.700000 | 84.000000 | 1016.000000 |  | 13.140000 | 0.000000 | 10000.000000 | 137.000000 | 2.11 | 1.540000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 01:00:00 | 70.000000 | 9.870000 | 11.660000 | 86.000000 | 1017.000000 |  | 12.140000 | 0.000000 | 10000.000000 | 140.000000 | 2.01 | 1.610000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 02:00:00 | 64.000000 | 10.040000 | 11.680000 | 87.000000 | 1018.000000 |  | 12.140000 | 0.000000 | 10000.000000 | 140.000000 | 2.3 | 1.800000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 03:00:00 | 60.000000 | 8.240000 | 9.510000 | 88.000000 | 1018.000000 |  | 10.140000 | 0.000000 | 10000.000000 | 138.000000 | 2.38 | 1.760000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 04:00:00 | 58.000000 | 8.080000 | 9.480000 | 87.000000 | 1018.000000 |  | 10.140000 | 0.000000 | 10000.000000 | 133.000000 | 2.04 | 1.700000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 05:00:00 | 58.000000 | 5.940000 | 7.280000 | 86.000000 | 1018.000000 |  | 8.140000 | 0.000000 | 10000.000000 | 127.000000 | 1.98 | 1.730000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 06:00:00 | 92.000000 | 5.770000 | 7.340000 | 85.000000 | 1017.000000 |  | 8.140000 | 0.000000 | 10000.000000 | 117.000000 | 1.67 | 1.670000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 07:00:00 | 100.000000 | 6.750000 | 8.360000 | 85.000000 | 1017.000000 |  | 9.140000 | 0.000000 | 10000.000000 | 117.000000 | 2.09 | 1.810000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 08:00:00 | 100.000000 | 7.740000 | 9.430000 | 85.000000 | 1016.000000 |  | 10.140000 | 0.000000 | 10000.000000 | 116.000000 | 2.25 | 1.970000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 09:00:00 | 99.000000 | 6.750000 | 8.060000 | 85.000000 | 1017.000000 |  | 9.140000 | 0.000000 | 10000.000000 | 114.000000 | 2.44 | 2.160000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 10:00:00 | 99.000000 | 5.940000 | 6.810000 | 86.000000 | 1017.000000 |  | 8.140000 | 0.000000 | 10000.000000 | 114.000000 | 2.58 | 2.250000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 11:00:00 | 100.000000 | 6.920000 | 7.970000 | 86.000000 | 1017.000000 |  | 9.140000 | 0.000000 | 10000.000000 | 114.000000 | 2.75 | 2.280000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 12:00:00 | 94.000000 | 6.410000 | 8.050000 | 83.000000 | 1018.000000 |  | 9.140000 | 0.530000 | 10000.000000 | 111.000000 | 2.76 | 2.170000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 13:00:00 | 100.000000 | 6.690000 | 10.240000 | 74.000000 | 1018.000000 |  | 11.140000 | 1.720000 | 10000.000000 | 117.000000 | 2.63 | 1.980000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 14:00:00 | 98.000000 | 7.210000 | 13.250000 | 63.000000 | 1018.000000 |  | 14.140000 | 4.070000 | 10000.000000 | 124.000000 | 2.22 | 1.350000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 15:00:00 | 91.000000 | 7.370000 | 15.270000 | 56.000000 | 1017.000000 |  | 16.140000 | 6.830000 | 10000.000000 | 134.000000 | 2.1 | 0.980000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 16:00:00 | 80.000000 | 8.140000 | 17.370000 | 52.000000 | 1015.000000 |  | 18.140000 | 12.640000 | 10000.000000 | 146.000000 | 2.62 | 0.480000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 17:00:00 | 78.000000 | 7.850000 | 17.340000 | 51.000000 | 1014.000000 |  | 18.140000 | 13.740000 | 10000.000000 | 190.000000 | 2.57 | 0.640000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 18:00:00 | 99.000000 | 7.770000 | 16.320000 | 54.000000 | 1013.000000 | 0.19 | 17.140000 | 12.470000 | 10000.000000 | 189.000000 | 2.18 | 1.390000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 19:00:00 | 100.000000 | 8.420000 | 17.390000 | 53.000000 | 1012.000000 | 0.22 | 18.140000 | 9.050000 | 10000.000000 | 179.000000 | 2.27 | 1.170000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 20:00:00 | 85.000000 | 8.690000 | 17.420000 | 54.000000 | 1011.000000 | 0.23 | 18.140000 | 5.270000 | 10000.000000 | 181.000000 | 2.5 | 1.070000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 21:00:00 | 89.000000 | 9.320000 | 16.480000 | 60.000000 | 1012.000000 | 0.16 | 17.140000 | 2.170000 | 10000.000000 | 174.000000 | 2.39 | 1.120000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 22:00:00 | 91.000000 | 9.330000 | 15.480000 | 64.000000 | 1012.000000 | 0.19 | 16.140000 | 0.390000 | 10000.000000 | 144.000000 | 2.02 | 1.300000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 23:00:00 | 93.000000 | 9.780000 | 13.570000 | 75.000000 | 1014.000000 | 0.15 | 14.140000 | 0.000000 | 10000.000000 | 132.000000 | 2.53 | 1.580000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21201240_OWM_Clouds_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Clouds_20220203.png)
![CNE_IDEAM_Station21201240_OWM_Dewpoint_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Dewpoint_20220203.png)
![CNE_IDEAM_Station21201240_OWM_Feelslike_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Feelslike_20220203.png)
![CNE_IDEAM_Station21201240_OWM_Humidity_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Humidity_20220203.png)
![CNE_IDEAM_Station21201240_OWM_Pressure_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Pressure_20220203.png)
![CNE_IDEAM_Station21201240_OWM_Rain_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Rain_20220203.png)
![CNE_IDEAM_Station21201240_OWM_Temp_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Temp_20220203.png)
![CNE_IDEAM_Station21201240_OWM_UVI_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_UVI_20220203.png)
![CNE_IDEAM_Station21201240_OWM_Visibility_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Visibility_20220203.png)
![CNE_IDEAM_Station21201240_OWM_Winddeg_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Winddeg_20220203.png)
![CNE_IDEAM_Station21201240_OWM_Windgust_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Windgust_20220203.png)
![CNE_IDEAM_Station21201240_OWM_Windspeed_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Windspeed_20220203.png)

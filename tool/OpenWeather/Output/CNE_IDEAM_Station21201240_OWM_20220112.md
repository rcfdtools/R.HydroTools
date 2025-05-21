
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SANTA MARIA DE USME [21201240] - Historical

Study case: Weather evaluation from historical openweathermap data for the CNE IDEAM network stations in Bogotá - Colombia - Suramérica

### GitHub repository and system information

* Python version: 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
* Python path: ['D:\\R.GISPython\\OpenWeather', 'D:\\R.GISPython', 'D:\\R.GISPython.wiki', 'C:\\Python310\\python310.zip', 'C:\\Python310\\DLLs']
* matplotlib version: 3.5.0
* Repository: https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather
* License and conditions: https://github.com/rcfdtools/R.GISPython/wiki/License
* Credits: r.cfdtools@gmail.com

### General parameters

* Current date time: 2022-01-12 11:11:05.365344
* Unix time to eval: 1641899465
* Days before (for historical data): 1
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220112.xls
* CNE IDEAM file downloaded and updated: No
* CNE IDEAM stations: 4494
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201240_OWM_20220112.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220112.csv)

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
| Latitude | latitud | lat | Geolocalization latitude degrees |
| Longitude | longitud | lon | Geolocalization longitude degrees |
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

### (CNE index 2081) Open Weather values for station 21201240 - SANTA MARIA DE USME [21201240]

JSON data from API OWM:

```
{'lat': 4.4813, 'lon': -74.1263, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641899465, 'sunrise': 1641899269, 'sunset': 1641942038, 'temp': 10.14, 'feels_like': 9.61, 'pressure': 1017, 'humidity': 92, 'dew_point': 8.9, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 346, 'wind_gust': 0.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641859200, 'temp': 13.14, 'feels_like': 12.89, 'pressure': 1016, 'humidity': 91, 'dew_point': 11.71, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 127, 'wind_gust': 0.97, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641862800, 'temp': 13.14, 'feels_like': 12.89, 'pressure': 1017, 'humidity': 91, 'dew_point': 11.71, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 30, 'wind_gust': 1.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641866400, 'temp': 12.14, 'feels_like': 11.81, 'pressure': 1018, 'humidity': 92, 'dew_point': 10.88, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 49, 'wind_gust': 0.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641870000, 'temp': 12.14, 'feels_like': 11.81, 'pressure': 1018, 'humidity': 92, 'dew_point': 10.88, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.22, 'wind_deg': 161, 'wind_gust': 0.87, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641873600, 'temp': 12.14, 'feels_like': 11.73, 'pressure': 1018, 'humidity': 89, 'dew_point': 10.38, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.07, 'wind_deg': 15, 'wind_gust': 0.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641877200, 'temp': 12.14, 'feels_like': 11.73, 'pressure': 1017, 'humidity': 89, 'dew_point': 10.38, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.1, 'wind_deg': 7, 'wind_gust': 0.73, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641880800, 'temp': 12.14, 'feels_like': 11.73, 'pressure': 1017, 'humidity': 89, 'dew_point': 10.38, 'uvi': 0, 'clouds': 56, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 296, 'wind_gust': 0.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641884400, 'temp': 12.14, 'feels_like': 11.79, 'pressure': 1016, 'humidity': 91, 'dew_point': 10.72, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 306, 'wind_gust': 1.1, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641888000, 'temp': 11.14, 'feels_like': 10.71, 'pressure': 1016, 'humidity': 92, 'dew_point': 9.89, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 316, 'wind_gust': 0.94, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641891600, 'temp': 11.14, 'feels_like': 10.74, 'pressure': 1016, 'humidity': 93, 'dew_point': 10.05, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 303, 'wind_gust': 1.25, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641895200, 'temp': 10.14, 'feels_like': 9.64, 'pressure': 1016, 'humidity': 93, 'dew_point': 9.06, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 321, 'wind_gust': 0.94, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641898800, 'temp': 10.14, 'feels_like': 9.61, 'pressure': 1017, 'humidity': 92, 'dew_point': 8.9, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 346, 'wind_gust': 0.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641902400, 'temp': 10.14, 'feels_like': 9.53, 'pressure': 1017, 'humidity': 89, 'dew_point': 8.41, 'uvi': 0.41, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 326, 'wind_gust': 0.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641906000, 'temp': 12.14, 'feels_like': 11.58, 'pressure': 1018, 'humidity': 83, 'dew_point': 9.34, 'uvi': 1.88, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 321, 'wind_gust': 0.94, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641909600, 'temp': 13.14, 'feels_like': 12.55, 'pressure': 1018, 'humidity': 78, 'dew_point': 9.39, 'uvi': 4.49, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 318, 'wind_gust': 0.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641913200, 'temp': 13.14, 'feels_like': 12.36, 'pressure': 1018, 'humidity': 71, 'dew_point': 8.01, 'uvi': 7.58, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 317, 'wind_gust': 1.26, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641916800, 'temp': 14.14, 'feels_like': 13.36, 'pressure': 1016, 'humidity': 67, 'dew_point': 8.11, 'uvi': 11.73, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 270, 'wind_gust': 1.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641920400, 'temp': 16.14, 'feels_like': 15.59, 'pressure': 1015, 'humidity': 68, 'dew_point': 10.24, 'uvi': 12.76, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 258, 'wind_gust': 1.89, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.28}}, {'dt': 1641924000, 'temp': 17.14, 'feels_like': 16.82, 'pressure': 1015, 'humidity': 73, 'dew_point': 12.27, 'uvi': 11.59, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 254, 'wind_gust': 1.95, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, {'dt': 1641927600, 'temp': 18.14, 'feels_like': 18.2, 'pressure': 1014, 'humidity': 84, 'dew_point': 15.4, 'uvi': 8.33, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 260, 'wind_gust': 1.86, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.46}}, {'dt': 1641931200, 'temp': 17.14, 'feels_like': 17.1, 'pressure': 1014, 'humidity': 84, 'dew_point': 14.42, 'uvi': 4.85, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 262, 'wind_gust': 1.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, {'dt': 1641934800, 'temp': 16.14, 'feels_like': 16.03, 'pressure': 1014, 'humidity': 85, 'dew_point': 13.62, 'uvi': 1.96, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 272, 'wind_gust': 1.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.4}}, {'dt': 1641938400, 'temp': 16.14, 'feels_like': 16.11, 'pressure': 1015, 'humidity': 88, 'dew_point': 14.15, 'uvi': 0.46, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 232, 'wind_gust': 1.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641942000, 'temp': 14.14, 'feels_like': 14.06, 'pressure': 1016, 'humidity': 94, 'dew_point': 13.19, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.11, 'wind_deg': 144, 'wind_gust': 1.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 00:00:00 | 73.000000 | 11.710000 | 12.890000 | 91.000000 | 1016.000000 |  | 13.140000 | 0.000000 | 10000.000000 | 127.000000 | 0.97 | 0.240000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 01:00:00 | 78.000000 | 11.710000 | 12.890000 | 91.000000 | 1017.000000 |  | 13.140000 | 0.000000 | 10000.000000 | 30.000000 | 1.03 | 0.490000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 02:00:00 | 84.000000 | 10.880000 | 11.810000 | 92.000000 | 1018.000000 |  | 12.140000 | 0.000000 | 10000.000000 | 49.000000 | 0.9 | 0.310000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 03:00:00 | 79.000000 | 10.880000 | 11.810000 | 92.000000 | 1018.000000 |  | 12.140000 | 0.000000 | 10000.000000 | 161.000000 | 0.87 | 0.220000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 04:00:00 | 80.000000 | 10.380000 | 11.730000 | 89.000000 | 1018.000000 |  | 12.140000 | 0.000000 | 10000.000000 | 15.000000 | 0.85 | 0.070000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 05:00:00 | 84.000000 | 10.380000 | 11.730000 | 89.000000 | 1017.000000 |  | 12.140000 | 0.000000 | 10000.000000 | 7.000000 | 0.73 | 0.100000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 06:00:00 | 56.000000 | 10.380000 | 11.730000 | 89.000000 | 1017.000000 | 0.13 | 12.140000 | 0.000000 | 10000.000000 | 296.000000 | 0.76 | 0.440000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 07:00:00 | 70.000000 | 10.720000 | 11.790000 | 91.000000 | 1016.000000 |  | 12.140000 | 0.000000 | 10000.000000 | 306.000000 | 1.1 | 0.570000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 08:00:00 | 68.000000 | 9.890000 | 10.710000 | 92.000000 | 1016.000000 |  | 11.140000 | 0.000000 | 10000.000000 | 316.000000 | 0.94 | 0.730000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 09:00:00 | 79.000000 | 10.050000 | 10.740000 | 93.000000 | 1016.000000 |  | 11.140000 | 0.000000 | 10000.000000 | 303.000000 | 1.25 | 1.030000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 10:00:00 | 84.000000 | 9.060000 | 9.640000 | 93.000000 | 1016.000000 |  | 10.140000 | 0.000000 | 10000.000000 | 321.000000 | 0.94 | 0.580000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 11:00:00 | 87.000000 | 8.900000 | 9.610000 | 92.000000 | 1017.000000 |  | 10.140000 | 0.000000 | 10000.000000 | 346.000000 | 0.67 | 0.440000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 12:00:00 | 86.000000 | 8.410000 | 9.530000 | 89.000000 | 1017.000000 |  | 10.140000 | 0.410000 | 10000.000000 | 326.000000 | 0.87 | 0.480000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 13:00:00 | 95.000000 | 9.340000 | 11.580000 | 83.000000 | 1018.000000 |  | 12.140000 | 1.880000 | 10000.000000 | 321.000000 | 0.94 | 0.700000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 14:00:00 | 97.000000 | 9.390000 | 12.550000 | 78.000000 | 1018.000000 |  | 13.140000 | 4.490000 | 10000.000000 | 318.000000 | 0.97 | 0.620000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 15:00:00 | 97.000000 | 8.010000 | 12.360000 | 71.000000 | 1018.000000 |  | 13.140000 | 7.580000 | 10000.000000 | 317.000000 | 1.26 | 0.940000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 16:00:00 | 96.000000 | 8.110000 | 13.360000 | 67.000000 | 1016.000000 | 0.16 | 14.140000 | 11.730000 | 10000.000000 | 270.000000 | 1.65 | 1.060000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 17:00:00 | 94.000000 | 10.240000 | 15.590000 | 68.000000 | 1015.000000 | 0.28 | 16.140000 | 12.760000 | 10000.000000 | 258.000000 | 1.89 | 1.150000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 18:00:00 | 91.000000 | 12.270000 | 16.820000 | 73.000000 | 1015.000000 | 0.53 | 17.140000 | 11.590000 | 10000.000000 | 254.000000 | 1.95 | 0.830000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 19:00:00 | 100.000000 | 15.400000 | 18.200000 | 84.000000 | 1014.000000 | 0.46 | 18.140000 | 8.330000 | 10000.000000 | 260.000000 | 1.86 | 0.760000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 20:00:00 | 99.000000 | 14.420000 | 17.100000 | 84.000000 | 1014.000000 | 0.56 | 17.140000 | 4.850000 | 10000.000000 | 262.000000 | 1.71 | 0.820000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 21:00:00 | 95.000000 | 13.620000 | 16.030000 | 85.000000 | 1014.000000 | 0.4 | 16.140000 | 1.960000 | 10000.000000 | 272.000000 | 1.65 | 0.530000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 22:00:00 | 95.000000 | 14.150000 | 16.110000 | 88.000000 | 1015.000000 | 0.18 | 16.140000 | 0.460000 | 10000.000000 | 232.000000 | 1.21 | 0.190000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 23:00:00 | 91.000000 | 13.190000 | 14.060000 | 94.000000 | 1016.000000 | 0.15 | 14.140000 | 0.000000 | 10000.000000 | 144.000000 | 1.02 | 0.110000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21201240_OWM_Clouds_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Clouds_20220112.png)
![CNE_IDEAM_Station21201240_OWM_Dewpoint_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Dewpoint_20220112.png)
![CNE_IDEAM_Station21201240_OWM_Feelslike_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Feelslike_20220112.png)
![CNE_IDEAM_Station21201240_OWM_Humidity_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Humidity_20220112.png)
![CNE_IDEAM_Station21201240_OWM_Pressure_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Pressure_20220112.png)
![CNE_IDEAM_Station21201240_OWM_Rain_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Rain_20220112.png)
![CNE_IDEAM_Station21201240_OWM_Temp_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Temp_20220112.png)
![CNE_IDEAM_Station21201240_OWM_UVI_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_UVI_20220112.png)
![CNE_IDEAM_Station21201240_OWM_Visibility_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Visibility_20220112.png)
![CNE_IDEAM_Station21201240_OWM_Windgust_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Windgust_20220112.png)
![CNE_IDEAM_Station21201240_OWM_Windspeed_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Windspeed_20220112.png)

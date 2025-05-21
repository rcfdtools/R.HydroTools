
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

* Current date time: 2022-01-30 14:37:17.220329
* Unix time to eval: 1643467037
* Days before (for historical data): 1
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220130.xls
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201240_OWM_20220130.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220130.csv)

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

### (CNE index 2079) Open Weather values for station 21201240 - SANTA MARIA DE USME [21201240]

JSON data from API OWM:

```
{'lat': 4.4813, 'lon': -74.1263, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643467037, 'sunrise': 1643454711, 'sunset': 1643497635, 'temp': 13.14, 'feels_like': 11.89, 'pressure': 1016, 'humidity': 53, 'dew_point': 3.78, 'uvi': 9.42, 'clouds': 5, 'visibility': 10000, 'wind_speed': 2.34, 'wind_deg': 308, 'wind_gust': 2.31, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, 'hourly': [{'dt': 1643414400, 'temp': 13.14, 'feels_like': 12.76, 'pressure': 1015, 'humidity': 86, 'dew_point': 10.85, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 93, 'wind_gust': 1.4, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.93}}, {'dt': 1643418000, 'temp': 13.14, 'feels_like': 12.78, 'pressure': 1016, 'humidity': 87, 'dew_point': 11.03, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 61, 'wind_gust': 1.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.63}}, {'dt': 1643421600, 'temp': 12.14, 'feels_like': 11.79, 'pressure': 1017, 'humidity': 91, 'dew_point': 10.72, 'uvi': 0, 'clouds': 53, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 346, 'wind_gust': 1.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1643425200, 'temp': 11.14, 'feels_like': 10.58, 'pressure': 1017, 'humidity': 87, 'dew_point': 9.06, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 355, 'wind_gust': 0.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.44}}, {'dt': 1643428800, 'temp': 10.14, 'feels_like': 9.53, 'pressure': 1017, 'humidity': 89, 'dew_point': 8.41, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 289, 'wind_gust': 1.24, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643432400, 'temp': 10.14, 'feels_like': 9.53, 'pressure': 1017, 'humidity': 89, 'dew_point': 8.41, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 298, 'wind_gust': 1.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1643436000, 'temp': 9.14, 'feels_like': 9.14, 'pressure': 1016, 'humidity': 89, 'dew_point': 7.42, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 280, 'wind_gust': 0.92, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643439600, 'temp': 9.14, 'feels_like': 9.14, 'pressure': 1016, 'humidity': 92, 'dew_point': 7.91, 'uvi': 0, 'clouds': 27, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 250, 'wind_gust': 1.61, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643443200, 'temp': 7.14, 'feels_like': 7.14, 'pressure': 1016, 'humidity': 92, 'dew_point': 5.93, 'uvi': 0, 'clouds': 22, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 279, 'wind_gust': 1.86, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643446800, 'temp': 6.14, 'feels_like': 6.14, 'pressure': 1016, 'humidity': 92, 'dew_point': 4.94, 'uvi': 0, 'clouds': 29, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 288, 'wind_gust': 1.23, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643450400, 'temp': 5.14, 'feels_like': 5.14, 'pressure': 1017, 'humidity': 93, 'dew_point': 4.1, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 280, 'wind_gust': 1.88, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643454000, 'temp': 4.14, 'feels_like': 4.14, 'pressure': 1017, 'humidity': 92, 'dew_point': 2.96, 'uvi': 0, 'clouds': 17, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 282, 'wind_gust': 1.84, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643457600, 'temp': 5.14, 'feels_like': 5.14, 'pressure': 1018, 'humidity': 88, 'dew_point': 3.32, 'uvi': 0.55, 'clouds': 5, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 292, 'wind_gust': 2.11, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643461200, 'temp': 9.14, 'feels_like': 8.75, 'pressure': 1017, 'humidity': 74, 'dew_point': 4.76, 'uvi': 2.37, 'clouds': 9, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 296, 'wind_gust': 1.92, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643464800, 'temp': 13.14, 'feels_like': 12.15, 'pressure': 1017, 'humidity': 63, 'dew_point': 6.26, 'uvi': 5.6, 'clouds': 6, 'visibility': 10000, 'wind_speed': 2.1, 'wind_deg': 306, 'wind_gust': 2.26, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643468400, 'temp': 16.14, 'feels_like': 15.19, 'pressure': 1016, 'humidity': 53, 'dew_point': 6.57, 'uvi': 9.42, 'clouds': 5, 'visibility': 10000, 'wind_speed': 2.34, 'wind_deg': 308, 'wind_gust': 2.31, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643472000, 'temp': 17.14, 'feels_like': 16.16, 'pressure': 1015, 'humidity': 48, 'dew_point': 6.05, 'uvi': 12.55, 'clouds': 4, 'visibility': 10000, 'wind_speed': 2.54, 'wind_deg': 312, 'wind_gust': 2.5, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643475600, 'temp': 19.14, 'feels_like': 18.31, 'pressure': 1013, 'humidity': 46, 'dew_point': 7.26, 'uvi': 13.66, 'clouds': 10, 'visibility': 10000, 'wind_speed': 2.81, 'wind_deg': 313, 'wind_gust': 2.74, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643479200, 'temp': 18.14, 'feels_like': 17.18, 'pressure': 1012, 'humidity': 45, 'dew_point': 6.03, 'uvi': 12.4, 'clouds': 28, 'visibility': 10000, 'wind_speed': 2.84, 'wind_deg': 309, 'wind_gust': 2.75, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643482800, 'temp': 19.14, 'feels_like': 18.31, 'pressure': 1011, 'humidity': 46, 'dew_point': 7.26, 'uvi': 9.06, 'clouds': 26, 'visibility': 10000, 'wind_speed': 2.63, 'wind_deg': 307, 'wind_gust': 2.77, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643486400, 'temp': 18.14, 'feels_like': 17.29, 'pressure': 1010, 'humidity': 49, 'dew_point': 7.27, 'uvi': 5.28, 'clouds': 23, 'visibility': 10000, 'wind_speed': 2.1, 'wind_deg': 296, 'wind_gust': 2.83, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643490000, 'temp': 18.14, 'feels_like': 17.5, 'pressure': 1011, 'humidity': 57, 'dew_point': 9.5, 'uvi': 2.16, 'clouds': 42, 'visibility': 10000, 'wind_speed': 1.75, 'wind_deg': 288, 'wind_gust': 2.72, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643493600, 'temp': 17.14, 'feels_like': 16.76, 'pressure': 1012, 'humidity': 71, 'dew_point': 11.84, 'uvi': 0.45, 'clouds': 56, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 285, 'wind_gust': 2.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1643497200, 'temp': 15.14, 'feels_like': 14.98, 'pressure': 1014, 'humidity': 87, 'dew_point': 12.99, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 303, 'wind_gust': 1.52, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 00:00:00 | 97.000000 | 10.850000 | 12.760000 | 86.000000 | 1015.000000 | 0.93 | 13.140000 | 0.000000 | 10000.000000 | 93.000000 | 1.4 | 0.570000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 01:00:00 | 100.000000 | 11.030000 | 12.780000 | 87.000000 | 1016.000000 | 0.63 | 13.140000 | 0.000000 | 10000.000000 | 61.000000 | 1.59 | 0.730000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 02:00:00 | 53.000000 | 10.720000 | 11.790000 | 91.000000 | 1017.000000 | 0.12 | 12.140000 | 0.000000 | 10000.000000 | 346.000000 | 1.03 | 0.360000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 03:00:00 | 83.000000 | 9.060000 | 10.580000 | 87.000000 | 1017.000000 | 0.44 | 11.140000 | 0.000000 | 10000.000000 | 355.000000 | 0.87 | 0.230000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 04:00:00 | 62.000000 | 8.410000 | 9.530000 | 89.000000 | 1017.000000 |  | 10.140000 | 0.000000 | 10000.000000 | 289.000000 | 1.24 | 0.490000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 05:00:00 | 86.000000 | 8.410000 | 9.530000 | 89.000000 | 1017.000000 | 0.29 | 10.140000 | 0.000000 | 10000.000000 | 298.000000 | 1.3 | 0.660000 | 500 | Rain | light rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 06:00:00 | 82.000000 | 7.420000 | 9.140000 | 89.000000 | 1016.000000 |  | 9.140000 | 0.000000 | 10000.000000 | 280.000000 | 0.92 | 0.420000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 07:00:00 | 27.000000 | 7.910000 | 9.140000 | 92.000000 | 1016.000000 |  | 9.140000 | 0.000000 | 10000.000000 | 250.000000 | 1.61 | 0.650000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 08:00:00 | 22.000000 | 5.930000 | 7.140000 | 92.000000 | 1016.000000 |  | 7.140000 | 0.000000 | 10000.000000 | 279.000000 | 1.86 | 0.700000 | 801 | Clouds | few clouds | 02n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 09:00:00 | 29.000000 | 4.940000 | 6.140000 | 92.000000 | 1016.000000 |  | 6.140000 | 0.000000 | 10000.000000 | 288.000000 | 1.23 | 0.520000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 10:00:00 | 20.000000 | 4.100000 | 5.140000 | 93.000000 | 1017.000000 |  | 5.140000 | 0.000000 | 10000.000000 | 280.000000 | 1.88 | 0.850000 | 801 | Clouds | few clouds | 02n | 10 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 11:00:00 | 17.000000 | 2.960000 | 4.140000 | 92.000000 | 1017.000000 |  | 4.140000 | 0.000000 | 10000.000000 | 282.000000 | 1.84 | 0.940000 | 801 | Clouds | few clouds | 02n | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 12:00:00 | 5.000000 | 3.320000 | 5.140000 | 88.000000 | 1018.000000 |  | 5.140000 | 0.550000 | 10000.000000 | 292.000000 | 2.11 | 0.740000 | 800 | Clear | clear sky | 01d | 12 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 13:00:00 | 9.000000 | 4.760000 | 8.750000 | 74.000000 | 1017.000000 |  | 9.140000 | 2.370000 | 10000.000000 | 296.000000 | 1.92 | 1.430000 | 800 | Clear | clear sky | 01d | 13 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 14:00:00 | 6.000000 | 6.260000 | 12.150000 | 63.000000 | 1017.000000 |  | 13.140000 | 5.600000 | 10000.000000 | 306.000000 | 2.26 | 2.100000 | 800 | Clear | clear sky | 01d | 14 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 15:00:00 | 5.000000 | 6.570000 | 15.190000 | 53.000000 | 1016.000000 |  | 16.140000 | 9.420000 | 10000.000000 | 308.000000 | 2.31 | 2.340000 | 800 | Clear | clear sky | 01d | 15 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 16:00:00 | 4.000000 | 6.050000 | 16.160000 | 48.000000 | 1015.000000 |  | 17.140000 | 12.550000 | 10000.000000 | 312.000000 | 2.5 | 2.540000 | 800 | Clear | clear sky | 01d | 16 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 17:00:00 | 10.000000 | 7.260000 | 18.310000 | 46.000000 | 1013.000000 |  | 19.140000 | 13.660000 | 10000.000000 | 313.000000 | 2.74 | 2.810000 | 800 | Clear | clear sky | 01d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 18:00:00 | 28.000000 | 6.030000 | 17.180000 | 45.000000 | 1012.000000 |  | 18.140000 | 12.400000 | 10000.000000 | 309.000000 | 2.75 | 2.840000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 19:00:00 | 26.000000 | 7.260000 | 18.310000 | 46.000000 | 1011.000000 |  | 19.140000 | 9.060000 | 10000.000000 | 307.000000 | 2.77 | 2.630000 | 802 | Clouds | scattered clouds | 03d | 19 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 20:00:00 | 23.000000 | 7.270000 | 17.290000 | 49.000000 | 1010.000000 |  | 18.140000 | 5.280000 | 10000.000000 | 296.000000 | 2.83 | 2.100000 | 801 | Clouds | few clouds | 02d | 20 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 21:00:00 | 42.000000 | 9.500000 | 17.500000 | 57.000000 | 1011.000000 |  | 18.140000 | 2.160000 | 10000.000000 | 288.000000 | 2.72 | 1.750000 | 802 | Clouds | scattered clouds | 03d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 22:00:00 | 56.000000 | 11.840000 | 16.760000 | 71.000000 | 1012.000000 | 0.16 | 17.140000 | 0.450000 | 10000.000000 | 285.000000 | 2.01 | 0.980000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201240 | "SANTA MARIA DE USME [21201240]" | 4.481306 | -74.126278 | 2800.000000 | Pluviométrica | Convencional | Activa | 1977-12-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 23:00:00 | 65.000000 | 12.990000 | 14.980000 | 87.000000 | 1014.000000 | 0.15 | 15.140000 | 0.000000 | 10000.000000 | 303.000000 | 1.52 | 0.490000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21201240_OWM_Clouds_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Clouds_20220130.png)
![CNE_IDEAM_Station21201240_OWM_Dewpoint_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Dewpoint_20220130.png)
![CNE_IDEAM_Station21201240_OWM_Feelslike_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Feelslike_20220130.png)
![CNE_IDEAM_Station21201240_OWM_Humidity_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Humidity_20220130.png)
![CNE_IDEAM_Station21201240_OWM_Pressure_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Pressure_20220130.png)
![CNE_IDEAM_Station21201240_OWM_Rain_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Rain_20220130.png)
![CNE_IDEAM_Station21201240_OWM_Temp_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Temp_20220130.png)
![CNE_IDEAM_Station21201240_OWM_UVI_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_UVI_20220130.png)
![CNE_IDEAM_Station21201240_OWM_Visibility_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Visibility_20220130.png)
![CNE_IDEAM_Station21201240_OWM_Winddeg_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Winddeg_20220130.png)
![CNE_IDEAM_Station21201240_OWM_Windgust_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Windgust_20220130.png)
![CNE_IDEAM_Station21201240_OWM_Windspeed_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201240_OWM_Windspeed_20220130.png)

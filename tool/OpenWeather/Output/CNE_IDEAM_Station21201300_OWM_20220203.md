
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AUSTRALIA [21201300] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201300_OWM_20220203.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220203.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.39425,-74.132) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.39425&lon=-74.132)

| Parameter | Value |
|---|---|
| Code | 21201300 |
| Name | AUSTRALIA [21201300] |
| Latitude, ° | 4.39425 |
| Longitude, ° | -74.132 |
| Elevation, m | 3050 |
| Category | Pluviométrica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1985-03-15 00:00:00 |
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

### (CNE index 1516) Open Weather values for station 21201300 - AUSTRALIA [21201300]

JSON data from API OWM:

```
{'lat': 4.3943, 'lon': -74.132, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643814483, 'sunrise': 1643800322, 'sunset': 1643843303, 'temp': 13.38, 'feels_like': 12.31, 'pressure': 1017, 'humidity': 59, 'dew_point': 5.54, 'uvi': 6.83, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 116, 'wind_gust': 2.08, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1643760000, 'temp': 10.38, 'feels_like': 9.72, 'pressure': 1016, 'humidity': 86, 'dew_point': 8.14, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1.4, 'wind_deg': 128, 'wind_gust': 1.95, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643763600, 'temp': 9.38, 'feels_like': 9.06, 'pressure': 1017, 'humidity': 86, 'dew_point': 7.16, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.39, 'wind_deg': 132, 'wind_gust': 1.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643767200, 'temp': 9.38, 'feels_like': 9.04, 'pressure': 1018, 'humidity': 87, 'dew_point': 7.33, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.41, 'wind_deg': 137, 'wind_gust': 2.06, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643770800, 'temp': 7.38, 'feels_like': 7.38, 'pressure': 1018, 'humidity': 88, 'dew_point': 5.53, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 141, 'wind_gust': 2.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643774400, 'temp': 7.38, 'feels_like': 7.38, 'pressure': 1018, 'humidity': 87, 'dew_point': 5.36, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 134, 'wind_gust': 1.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643778000, 'temp': 5.38, 'feels_like': 4.51, 'pressure': 1018, 'humidity': 86, 'dew_point': 3.23, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.4, 'wind_deg': 124, 'wind_gust': 1.77, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643781600, 'temp': 5.38, 'feels_like': 5.38, 'pressure': 1017, 'humidity': 86, 'dew_point': 3.23, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 117, 'wind_gust': 1.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643785200, 'temp': 6.38, 'feels_like': 5.7, 'pressure': 1017, 'humidity': 86, 'dew_point': 4.21, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 114, 'wind_gust': 1.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643788800, 'temp': 7.38, 'feels_like': 6.65, 'pressure': 1016, 'humidity': 86, 'dew_point': 5.2, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 113, 'wind_gust': 1.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643792400, 'temp': 6.38, 'feels_like': 5.29, 'pressure': 1017, 'humidity': 87, 'dew_point': 4.38, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 112, 'wind_gust': 2.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643796000, 'temp': 5.38, 'feels_like': 4.08, 'pressure': 1017, 'humidity': 87, 'dew_point': 3.39, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.75, 'wind_deg': 113, 'wind_gust': 2.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643799600, 'temp': 6.38, 'feels_like': 5.17, 'pressure': 1018, 'humidity': 87, 'dew_point': 4.38, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 113, 'wind_gust': 2.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643803200, 'temp': 6.38, 'feels_like': 5.18, 'pressure': 1018, 'humidity': 84, 'dew_point': 3.88, 'uvi': 0.53, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.8, 'wind_deg': 108, 'wind_gust': 2.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643806800, 'temp': 8.38, 'feels_like': 7.49, 'pressure': 1018, 'humidity': 75, 'dew_point': 4.21, 'uvi': 1.72, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.8, 'wind_deg': 112, 'wind_gust': 2.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643810400, 'temp': 11.38, 'feels_like': 10.27, 'pressure': 1018, 'humidity': 65, 'dew_point': 5.04, 'uvi': 4.07, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.26, 'wind_deg': 115, 'wind_gust': 2.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643814000, 'temp': 13.38, 'feels_like': 12.31, 'pressure': 1017, 'humidity': 59, 'dew_point': 5.54, 'uvi': 6.83, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 116, 'wind_gust': 2.08, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643817600, 'temp': 15.38, 'feels_like': 14.44, 'pressure': 1016, 'humidity': 56, 'dew_point': 6.66, 'uvi': 12.64, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 110, 'wind_gust': 2.48, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643821200, 'temp': 15.38, 'feels_like': 14.46, 'pressure': 1015, 'humidity': 57, 'dew_point': 6.92, 'uvi': 13.74, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 125, 'wind_gust': 2.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1643824800, 'temp': 14.38, 'feels_like': 13.39, 'pressure': 1014, 'humidity': 58, 'dew_point': 6.23, 'uvi': 12.47, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 159, 'wind_gust': 2.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1643828400, 'temp': 15.38, 'feels_like': 14.49, 'pressure': 1013, 'humidity': 58, 'dew_point': 7.17, 'uvi': 9.05, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 145, 'wind_gust': 2.37, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1643832000, 'temp': 15.38, 'feels_like': 14.54, 'pressure': 1012, 'humidity': 60, 'dew_point': 7.67, 'uvi': 5.27, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 156, 'wind_gust': 2.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.27}}, {'dt': 1643835600, 'temp': 14.38, 'feels_like': 13.57, 'pressure': 1012, 'humidity': 65, 'dew_point': 7.89, 'uvi': 2.17, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 152, 'wind_gust': 2.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1643839200, 'temp': 13.38, 'feels_like': 12.55, 'pressure': 1013, 'humidity': 68, 'dew_point': 7.6, 'uvi': 0.39, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 129, 'wind_gust': 2.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1643842800, 'temp': 11.38, 'feels_like': 10.58, 'pressure': 1015, 'humidity': 77, 'dew_point': 7.5, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 118, 'wind_gust': 2.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 00:00:00 | 63.000000 | 8.140000 | 9.720000 | 86.000000 | 1016.000000 |  | 10.380000 | 0.000000 | 10000.000000 | 128.000000 | 1.95 | 1.400000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 01:00:00 | 76.000000 | 7.160000 | 9.060000 | 86.000000 | 1017.000000 |  | 9.380000 | 0.000000 | 10000.000000 | 132.000000 | 1.85 | 1.390000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 02:00:00 | 72.000000 | 7.330000 | 9.040000 | 87.000000 | 1018.000000 |  | 9.380000 | 0.000000 | 10000.000000 | 137.000000 | 2.06 | 1.410000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 03:00:00 | 71.000000 | 5.530000 | 7.380000 | 88.000000 | 1018.000000 |  | 7.380000 | 0.000000 | 10000.000000 | 141.000000 | 2.02 | 1.310000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 04:00:00 | 71.000000 | 5.360000 | 7.380000 | 87.000000 | 1018.000000 |  | 7.380000 | 0.000000 | 10000.000000 | 134.000000 | 1.76 | 1.250000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 05:00:00 | 71.000000 | 3.230000 | 4.510000 | 86.000000 | 1018.000000 |  | 5.380000 | 0.000000 | 10000.000000 | 124.000000 | 1.77 | 1.400000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 06:00:00 | 91.000000 | 3.230000 | 5.380000 | 86.000000 | 1017.000000 |  | 5.380000 | 0.000000 | 10000.000000 | 117.000000 | 1.51 | 1.230000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 07:00:00 | 99.000000 | 4.210000 | 5.700000 | 86.000000 | 1017.000000 |  | 6.380000 | 0.000000 | 10000.000000 | 114.000000 | 1.78 | 1.360000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 08:00:00 | 100.000000 | 5.200000 | 6.650000 | 86.000000 | 1016.000000 |  | 7.380000 | 0.000000 | 10000.000000 | 113.000000 | 1.97 | 1.510000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 09:00:00 | 99.000000 | 4.380000 | 5.290000 | 87.000000 | 1017.000000 |  | 6.380000 | 0.000000 | 10000.000000 | 112.000000 | 2.16 | 1.700000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 10:00:00 | 99.000000 | 3.390000 | 4.080000 | 87.000000 | 1017.000000 |  | 5.380000 | 0.000000 | 10000.000000 | 113.000000 | 2.25 | 1.750000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 11:00:00 | 100.000000 | 4.380000 | 5.170000 | 87.000000 | 1018.000000 |  | 6.380000 | 0.000000 | 10000.000000 | 113.000000 | 2.42 | 1.810000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 12:00:00 | 95.000000 | 3.880000 | 5.180000 | 84.000000 | 1018.000000 |  | 6.380000 | 0.530000 | 10000.000000 | 108.000000 | 2.57 | 1.800000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 13:00:00 | 100.000000 | 4.210000 | 7.490000 | 75.000000 | 1018.000000 |  | 8.380000 | 1.720000 | 10000.000000 | 112.000000 | 2.49 | 1.800000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 14:00:00 | 95.000000 | 5.040000 | 10.270000 | 65.000000 | 1018.000000 |  | 11.380000 | 4.070000 | 10000.000000 | 115.000000 | 2.06 | 1.260000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 15:00:00 | 86.000000 | 5.540000 | 12.310000 | 59.000000 | 1017.000000 |  | 13.380000 | 6.830000 | 10000.000000 | 116.000000 | 2.08 | 0.790000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 16:00:00 | 80.000000 | 6.660000 | 14.440000 | 56.000000 | 1016.000000 |  | 15.380000 | 12.640000 | 10000.000000 | 110.000000 | 2.48 | 0.380000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 17:00:00 | 80.000000 | 6.920000 | 14.460000 | 57.000000 | 1015.000000 | 0.11 | 15.380000 | 13.740000 | 10000.000000 | 125.000000 | 2.43 | 0.300000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 18:00:00 | 99.000000 | 6.230000 | 13.390000 | 58.000000 | 1014.000000 | 0.22 | 14.380000 | 12.470000 | 10000.000000 | 159.000000 | 2.26 | 0.600000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 19:00:00 | 100.000000 | 7.170000 | 14.490000 | 58.000000 | 1013.000000 | 0.24 | 15.380000 | 9.050000 | 10000.000000 | 145.000000 | 2.37 | 0.630000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 20:00:00 | 91.000000 | 7.670000 | 14.540000 | 60.000000 | 1012.000000 | 0.27 | 15.380000 | 5.270000 | 10000.000000 | 156.000000 | 2.38 | 0.810000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 21:00:00 | 93.000000 | 7.890000 | 13.570000 | 65.000000 | 1012.000000 | 0.18 | 14.380000 | 2.170000 | 10000.000000 | 152.000000 | 2.34 | 0.950000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 22:00:00 | 95.000000 | 7.600000 | 12.550000 | 68.000000 | 1013.000000 | 0.21 | 13.380000 | 0.390000 | 10000.000000 | 129.000000 | 2.12 | 1.310000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 23:00:00 | 96.000000 | 7.500000 | 10.580000 | 77.000000 | 1015.000000 | 0.14 | 11.380000 | 0.000000 | 10000.000000 | 118.000000 | 2.44 | 1.500000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21201300_OWM_Clouds_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Clouds_20220203.png)
![CNE_IDEAM_Station21201300_OWM_Dewpoint_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Dewpoint_20220203.png)
![CNE_IDEAM_Station21201300_OWM_Feelslike_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Feelslike_20220203.png)
![CNE_IDEAM_Station21201300_OWM_Humidity_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Humidity_20220203.png)
![CNE_IDEAM_Station21201300_OWM_Pressure_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Pressure_20220203.png)
![CNE_IDEAM_Station21201300_OWM_Rain_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Rain_20220203.png)
![CNE_IDEAM_Station21201300_OWM_Temp_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Temp_20220203.png)
![CNE_IDEAM_Station21201300_OWM_UVI_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_UVI_20220203.png)
![CNE_IDEAM_Station21201300_OWM_Visibility_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Visibility_20220203.png)
![CNE_IDEAM_Station21201300_OWM_Winddeg_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Winddeg_20220203.png)
![CNE_IDEAM_Station21201300_OWM_Windgust_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Windgust_20220203.png)
![CNE_IDEAM_Station21201300_OWM_Windspeed_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Windspeed_20220203.png)

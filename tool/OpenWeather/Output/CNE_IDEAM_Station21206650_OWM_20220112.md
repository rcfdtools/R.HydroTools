
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - COLEGIO SAN CAYETANO [21206650] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206650_OWM_20220112.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220112.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.51675278,-74.08822222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.51675278&lon=-74.08822222)

| Parameter | Value |
|---|---|
| Code | 21206650 |
| Name | COLEGIO SAN CAYETANO [21206650] |
| Latitude, ° | 4.51675278 |
| Longitude, ° | -74.08822222 |
| Elevation, m | 3100 |
| Category | Climática Ordinaria |
| Technology | Convencional |
| Status | Activa |
| Installation date | 2001-11-15 00:00:00 |
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

### (CNE index 3792) Open Weather values for station 21206650 - COLEGIO SAN CAYETANO [21206650]

JSON data from API OWM:

```
{'lat': 4.5168, 'lon': -74.0882, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641899465, 'sunrise': 1641899263, 'sunset': 1641942026, 'temp': 6.97, 'feels_like': 6.97, 'pressure': 1017, 'humidity': 91, 'dew_point': 5.6, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 346, 'wind_gust': 0.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641859200, 'temp': 9.97, 'feels_like': 9.97, 'pressure': 1016, 'humidity': 93, 'dew_point': 8.89, 'uvi': 0, 'clouds': 76, 'visibility': 9068, 'wind_speed': 0.4, 'wind_deg': 137, 'wind_gust': 1.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641862800, 'temp': 9.97, 'feels_like': 9.97, 'pressure': 1017, 'humidity': 93, 'dew_point': 8.89, 'uvi': 0, 'clouds': 81, 'visibility': 9189, 'wind_speed': 0.42, 'wind_deg': 50, 'wind_gust': 1.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641866400, 'temp': 8.97, 'feels_like': 8.97, 'pressure': 1018, 'humidity': 93, 'dew_point': 7.9, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 74, 'wind_gust': 0.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641870000, 'temp': 8.97, 'feels_like': 8.97, 'pressure': 1018, 'humidity': 93, 'dew_point': 7.9, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 162, 'wind_gust': 0.86, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641873600, 'temp': 8.97, 'feels_like': 8.97, 'pressure': 1018, 'humidity': 91, 'dew_point': 7.58, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.04, 'wind_deg': 41, 'wind_gust': 0.82, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641877200, 'temp': 8.97, 'feels_like': 8.97, 'pressure': 1017, 'humidity': 90, 'dew_point': 7.42, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.11, 'wind_deg': 29, 'wind_gust': 0.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641880800, 'temp': 8.97, 'feels_like': 8.97, 'pressure': 1017, 'humidity': 90, 'dew_point': 7.42, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 294, 'wind_gust': 0.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641884400, 'temp': 8.97, 'feels_like': 8.97, 'pressure': 1016, 'humidity': 93, 'dew_point': 7.9, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 295, 'wind_gust': 1.13, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641888000, 'temp': 7.97, 'feels_like': 7.97, 'pressure': 1016, 'humidity': 93, 'dew_point': 6.91, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 311, 'wind_gust': 0.95, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641891600, 'temp': 7.97, 'feels_like': 7.97, 'pressure': 1016, 'humidity': 94, 'dew_point': 7.06, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 300, 'wind_gust': 1.23, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641895200, 'temp': 6.97, 'feels_like': 6.97, 'pressure': 1017, 'humidity': 93, 'dew_point': 5.92, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 311, 'wind_gust': 0.93, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641898800, 'temp': 6.97, 'feels_like': 6.97, 'pressure': 1017, 'humidity': 91, 'dew_point': 5.6, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 346, 'wind_gust': 0.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641902400, 'temp': 6.97, 'feels_like': 6.97, 'pressure': 1017, 'humidity': 89, 'dew_point': 5.28, 'uvi': 0.47, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 318, 'wind_gust': 0.84, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641906000, 'temp': 8.97, 'feels_like': 8.97, 'pressure': 1018, 'humidity': 82, 'dew_point': 6.07, 'uvi': 1.89, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 324, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641909600, 'temp': 9.97, 'feels_like': 9.97, 'pressure': 1018, 'humidity': 76, 'dew_point': 5.94, 'uvi': 4.54, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 323, 'wind_gust': 0.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641913200, 'temp': 9.97, 'feels_like': 9.97, 'pressure': 1017, 'humidity': 68, 'dew_point': 4.34, 'uvi': 7.68, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 324, 'wind_gust': 1.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641916800, 'temp': 10.97, 'feels_like': 9.74, 'pressure': 1016, 'humidity': 62, 'dew_point': 3.98, 'uvi': 11.23, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 258, 'wind_gust': 1.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641920400, 'temp': 12.97, 'feels_like': 11.97, 'pressure': 1015, 'humidity': 63, 'dew_point': 6.1, 'uvi': 12.22, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 236, 'wind_gust': 1.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.28}}, {'dt': 1641924000, 'temp': 13.97, 'feels_like': 13.25, 'pressure': 1014, 'humidity': 70, 'dew_point': 8.59, 'uvi': 11.09, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 221, 'wind_gust': 1.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.51}}, {'dt': 1641927600, 'temp': 14.97, 'feels_like': 14.64, 'pressure': 1014, 'humidity': 81, 'dew_point': 11.74, 'uvi': 5.75, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 235, 'wind_gust': 1.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.4}}, {'dt': 1641931200, 'temp': 13.97, 'feels_like': 13.56, 'pressure': 1013, 'humidity': 82, 'dew_point': 10.95, 'uvi': 3.34, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 246, 'wind_gust': 1.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.49}}, {'dt': 1641934800, 'temp': 12.97, 'feels_like': 12.49, 'pressure': 1014, 'humidity': 83, 'dew_point': 10.15, 'uvi': 1.34, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 261, 'wind_gust': 1.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1641938400, 'temp': 12.97, 'feels_like': 12.62, 'pressure': 1014, 'humidity': 88, 'dew_point': 11.03, 'uvi': 0.44, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 181, 'wind_gust': 1.36, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641942000, 'temp': 10.97, 'feels_like': 10.58, 'pressure': 1016, 'humidity': 94, 'dew_point': 10.04, 'uvi': 0, 'clouds': 91, 'visibility': 9452, 'wind_speed': 0.26, 'wind_deg': 140, 'wind_gust': 1.15, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 00:00:00 | 76.000000 | 8.890000 | 9.970000 | 93.000000 | 1016.000000 |  | 9.970000 | 0.000000 | 9068.000000 | 137.000000 | 1.11 | 0.400000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 01:00:00 | 81.000000 | 8.890000 | 9.970000 | 93.000000 | 1017.000000 |  | 9.970000 | 0.000000 | 9189.000000 | 50.000000 | 1.02 | 0.420000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 02:00:00 | 86.000000 | 7.900000 | 8.970000 | 93.000000 | 1018.000000 |  | 8.970000 | 0.000000 | 10000.000000 | 74.000000 | 0.87 | 0.240000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 03:00:00 | 82.000000 | 7.900000 | 8.970000 | 93.000000 | 1018.000000 |  | 8.970000 | 0.000000 | 10000.000000 | 162.000000 | 0.86 | 0.260000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 04:00:00 | 84.000000 | 7.580000 | 8.970000 | 91.000000 | 1018.000000 |  | 8.970000 | 0.000000 | 10000.000000 | 41.000000 | 0.82 | 0.040000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 05:00:00 | 87.000000 | 7.420000 | 8.970000 | 90.000000 | 1017.000000 |  | 8.970000 | 0.000000 | 10000.000000 | 29.000000 | 0.69 | 0.110000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 06:00:00 | 47.000000 | 7.420000 | 8.970000 | 90.000000 | 1017.000000 | 0.1 | 8.970000 | 0.000000 | 10000.000000 | 294.000000 | 0.79 | 0.480000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 07:00:00 | 60.000000 | 7.900000 | 8.970000 | 93.000000 | 1016.000000 |  | 8.970000 | 0.000000 | 10000.000000 | 295.000000 | 1.13 | 0.660000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 08:00:00 | 58.000000 | 6.910000 | 7.970000 | 93.000000 | 1016.000000 |  | 7.970000 | 0.000000 | 10000.000000 | 311.000000 | 0.95 | 0.740000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 09:00:00 | 72.000000 | 7.060000 | 7.970000 | 94.000000 | 1016.000000 |  | 7.970000 | 0.000000 | 10000.000000 | 300.000000 | 1.23 | 1.010000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 10:00:00 | 79.000000 | 5.920000 | 6.970000 | 93.000000 | 1017.000000 |  | 6.970000 | 0.000000 | 10000.000000 | 311.000000 | 0.93 | 0.560000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 11:00:00 | 83.000000 | 5.600000 | 6.970000 | 91.000000 | 1017.000000 |  | 6.970000 | 0.000000 | 10000.000000 | 346.000000 | 0.57 | 0.310000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 12:00:00 | 83.000000 | 5.280000 | 6.970000 | 89.000000 | 1017.000000 |  | 6.970000 | 0.470000 | 10000.000000 | 318.000000 | 0.84 | 0.400000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 13:00:00 | 94.000000 | 6.070000 | 8.970000 | 82.000000 | 1018.000000 |  | 8.970000 | 1.890000 | 10000.000000 | 324.000000 | 0.88 | 0.540000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 14:00:00 | 97.000000 | 5.940000 | 9.970000 | 76.000000 | 1018.000000 |  | 9.970000 | 4.540000 | 10000.000000 | 323.000000 | 0.96 | 0.480000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 15:00:00 | 96.000000 | 4.340000 | 9.970000 | 68.000000 | 1017.000000 |  | 9.970000 | 7.680000 | 10000.000000 | 324.000000 | 1.31 | 0.770000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 16:00:00 | 94.000000 | 3.980000 | 9.740000 | 62.000000 | 1016.000000 | 0.15 | 10.970000 | 11.230000 | 10000.000000 | 258.000000 | 1.75 | 0.800000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 17:00:00 | 92.000000 | 6.100000 | 11.970000 | 63.000000 | 1015.000000 | 0.28 | 12.970000 | 12.220000 | 10000.000000 | 236.000000 | 1.98 | 0.980000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 18:00:00 | 90.000000 | 8.590000 | 13.250000 | 70.000000 | 1014.000000 | 0.51 | 13.970000 | 11.090000 | 10000.000000 | 221.000000 | 1.99 | 0.710000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 19:00:00 | 100.000000 | 11.740000 | 14.640000 | 81.000000 | 1014.000000 | 0.4 | 14.970000 | 5.750000 | 10000.000000 | 235.000000 | 1.87 | 0.580000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 20:00:00 | 99.000000 | 10.950000 | 13.560000 | 82.000000 | 1013.000000 | 0.49 | 13.970000 | 3.340000 | 10000.000000 | 246.000000 | 1.8 | 0.650000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 21:00:00 | 96.000000 | 10.150000 | 12.490000 | 83.000000 | 1014.000000 | 0.36 | 12.970000 | 1.340000 | 10000.000000 | 261.000000 | 1.79 | 0.310000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 22:00:00 | 94.000000 | 11.030000 | 12.620000 | 88.000000 | 1014.000000 | 0.17 | 12.970000 | 0.440000 | 10000.000000 | 181.000000 | 1.36 | 0.250000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 23:00:00 | 91.000000 | 10.040000 | 10.580000 | 94.000000 | 1016.000000 | 0.15 | 10.970000 | 0.000000 | 9452.000000 | 140.000000 | 1.15 | 0.260000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21206650_OWM_Clouds_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Clouds_20220112.png)
![CNE_IDEAM_Station21206650_OWM_Dewpoint_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Dewpoint_20220112.png)
![CNE_IDEAM_Station21206650_OWM_Feelslike_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Feelslike_20220112.png)
![CNE_IDEAM_Station21206650_OWM_Humidity_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Humidity_20220112.png)
![CNE_IDEAM_Station21206650_OWM_Pressure_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Pressure_20220112.png)
![CNE_IDEAM_Station21206650_OWM_Rain_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Rain_20220112.png)
![CNE_IDEAM_Station21206650_OWM_Temp_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Temp_20220112.png)
![CNE_IDEAM_Station21206650_OWM_UVI_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_UVI_20220112.png)
![CNE_IDEAM_Station21206650_OWM_Visibility_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Visibility_20220112.png)
![CNE_IDEAM_Station21206650_OWM_Windgust_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Windgust_20220112.png)
![CNE_IDEAM_Station21206650_OWM_Windspeed_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Windspeed_20220112.png)

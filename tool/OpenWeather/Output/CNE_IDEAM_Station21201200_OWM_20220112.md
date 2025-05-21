
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ESCUELA LA UNION [21201200] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201200_OWM_20220112.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220112.csv)

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

### (CNE index 3322) Open Weather values for station 21201200 - ESCUELA LA UNION [21201200]

JSON data from API OWM:

```
{'lat': 4.3429, 'lon': -74.1839, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641899465, 'sunrise': 1641899269, 'sunset': 1641942065, 'temp': 5.98, 'feels_like': 5.98, 'pressure': 1017, 'humidity': 95, 'dew_point': 5.24, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 317, 'wind_gust': 0.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641859200, 'temp': 8.98, 'feels_like': 8.98, 'pressure': 1016, 'humidity': 93, 'dew_point': 7.91, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.18, 'wind_deg': 53, 'wind_gust': 0.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641862800, 'temp': 8.98, 'feels_like': 8.98, 'pressure': 1017, 'humidity': 92, 'dew_point': 7.75, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 27, 'wind_gust': 0.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641866400, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1019, 'humidity': 92, 'dew_point': 6.76, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 64, 'wind_gust': 0.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641870000, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1019, 'humidity': 92, 'dew_point': 6.76, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 148, 'wind_gust': 0.91, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641873600, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1019, 'humidity': 90, 'dew_point': 6.44, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.01, 'wind_deg': 116, 'wind_gust': 0.77, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641877200, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1018, 'humidity': 91, 'dew_point': 6.6, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 60, 'wind_gust': 0.84, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641880800, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1017, 'humidity': 91, 'dew_point': 6.6, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 311, 'wind_gust': 0.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641884400, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1017, 'humidity': 92, 'dew_point': 6.76, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 314, 'wind_gust': 0.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641888000, 'temp': 6.98, 'feels_like': 6.98, 'pressure': 1016, 'humidity': 93, 'dew_point': 5.93, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 320, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641891600, 'temp': 6.98, 'feels_like': 6.98, 'pressure': 1016, 'humidity': 95, 'dew_point': 6.24, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 308, 'wind_gust': 1.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641895200, 'temp': 5.98, 'feels_like': 5.98, 'pressure': 1017, 'humidity': 95, 'dew_point': 5.24, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 325, 'wind_gust': 0.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641898800, 'temp': 5.98, 'feels_like': 5.98, 'pressure': 1017, 'humidity': 95, 'dew_point': 5.24, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 317, 'wind_gust': 0.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641902400, 'temp': 5.98, 'feels_like': 5.98, 'pressure': 1018, 'humidity': 94, 'dew_point': 5.09, 'uvi': 0.41, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 310, 'wind_gust': 1.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641906000, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1019, 'humidity': 91, 'dew_point': 6.6, 'uvi': 1.88, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 315, 'wind_gust': 1.23, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641909600, 'temp': 8.98, 'feels_like': 8.98, 'pressure': 1019, 'humidity': 88, 'dew_point': 7.1, 'uvi': 4.49, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 320, 'wind_gust': 1.06, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641913200, 'temp': 8.98, 'feels_like': 8.98, 'pressure': 1019, 'humidity': 82, 'dew_point': 6.08, 'uvi': 7.58, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 315, 'wind_gust': 1.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641916800, 'temp': 9.98, 'feels_like': 9.8, 'pressure': 1018, 'humidity': 78, 'dew_point': 6.33, 'uvi': 11.73, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 289, 'wind_gust': 1.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641920400, 'temp': 11.98, 'feels_like': 11.27, 'pressure': 1016, 'humidity': 78, 'dew_point': 8.27, 'uvi': 12.76, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 290, 'wind_gust': 1.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.34}}, {'dt': 1641924000, 'temp': 12.98, 'feels_like': 12.45, 'pressure': 1015, 'humidity': 81, 'dew_point': 9.8, 'uvi': 11.59, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 290, 'wind_gust': 1.88, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.57}}, {'dt': 1641927600, 'temp': 13.98, 'feels_like': 13.76, 'pressure': 1015, 'humidity': 89, 'dew_point': 12.2, 'uvi': 8.33, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 290, 'wind_gust': 2.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.49}}, {'dt': 1641931200, 'temp': 12.98, 'feels_like': 12.68, 'pressure': 1014, 'humidity': 90, 'dew_point': 11.38, 'uvi': 4.85, 'clouds': 100, 'visibility': 7272, 'wind_speed': 1.14, 'wind_deg': 282, 'wind_gust': 1.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.58}}, {'dt': 1641934800, 'temp': 11.98, 'feels_like': 11.58, 'pressure': 1014, 'humidity': 90, 'dew_point': 10.39, 'uvi': 1.96, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 271, 'wind_gust': 1.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.32}}, {'dt': 1641938400, 'temp': 11.98, 'feels_like': 11.61, 'pressure': 1015, 'humidity': 91, 'dew_point': 10.56, 'uvi': 0.46, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 279, 'wind_gust': 1.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641942000, 'temp': 9.98, 'feels_like': 9.98, 'pressure': 1016, 'humidity': 96, 'dew_point': 9.37, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 288, 'wind_gust': 1.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 00:00:00 | 78.000000 | 7.910000 | 8.980000 | 93.000000 | 1016.000000 |  | 8.980000 | 0.000000 | 10000.000000 | 53.000000 | 0.7 | 0.180000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 01:00:00 | 86.000000 | 7.750000 | 8.980000 | 92.000000 | 1017.000000 |  | 8.980000 | 0.000000 | 10000.000000 | 27.000000 | 0.87 | 0.320000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 02:00:00 | 88.000000 | 6.760000 | 7.980000 | 92.000000 | 1019.000000 |  | 7.980000 | 0.000000 | 10000.000000 | 64.000000 | 0.9 | 0.390000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 03:00:00 | 77.000000 | 6.760000 | 7.980000 | 92.000000 | 1019.000000 |  | 7.980000 | 0.000000 | 10000.000000 | 148.000000 | 0.91 | 0.360000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 04:00:00 | 77.000000 | 6.440000 | 7.980000 | 90.000000 | 1019.000000 |  | 7.980000 | 0.000000 | 10000.000000 | 116.000000 | 0.77 | 0.010000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 05:00:00 | 80.000000 | 6.600000 | 7.980000 | 91.000000 | 1018.000000 | 0.19 | 7.980000 | 0.000000 | 10000.000000 | 60.000000 | 0.84 | 0.210000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 06:00:00 | 81.000000 | 6.600000 | 7.980000 | 91.000000 | 1017.000000 | 0.23 | 7.980000 | 0.000000 | 10000.000000 | 311.000000 | 0.75 | 0.300000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 07:00:00 | 91.000000 | 6.760000 | 7.980000 | 92.000000 | 1017.000000 | 0.1 | 7.980000 | 0.000000 | 10000.000000 | 314.000000 | 0.98 | 0.470000 | 500 | Rain | light rain | 10n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 08:00:00 | 92.000000 | 5.930000 | 6.980000 | 93.000000 | 1016.000000 |  | 6.980000 | 0.000000 | 10000.000000 | 320.000000 | 0.88 | 0.590000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 09:00:00 | 94.000000 | 6.240000 | 6.980000 | 95.000000 | 1016.000000 |  | 6.980000 | 0.000000 | 10000.000000 | 308.000000 | 1.21 | 0.910000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 10:00:00 | 96.000000 | 5.240000 | 5.980000 | 95.000000 | 1017.000000 | 0.1 | 5.980000 | 0.000000 | 10000.000000 | 325.000000 | 0.85 | 0.450000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 11:00:00 | 96.000000 | 5.240000 | 5.980000 | 95.000000 | 1017.000000 |  | 5.980000 | 0.000000 | 10000.000000 | 317.000000 | 0.86 | 0.410000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 12:00:00 | 90.000000 | 5.090000 | 5.980000 | 94.000000 | 1018.000000 |  | 5.980000 | 0.410000 | 10000.000000 | 310.000000 | 1.06 | 0.680000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 13:00:00 | 96.000000 | 6.600000 | 7.980000 | 91.000000 | 1019.000000 |  | 7.980000 | 1.880000 | 10000.000000 | 315.000000 | 1.23 | 0.860000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 14:00:00 | 98.000000 | 7.100000 | 8.980000 | 88.000000 | 1019.000000 | 0.14 | 8.980000 | 4.490000 | 10000.000000 | 320.000000 | 1.06 | 0.740000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 15:00:00 | 98.000000 | 6.080000 | 8.980000 | 82.000000 | 1019.000000 | 0.12 | 8.980000 | 7.580000 | 10000.000000 | 315.000000 | 1.11 | 0.940000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 16:00:00 | 98.000000 | 6.330000 | 9.800000 | 78.000000 | 1018.000000 | 0.17 | 9.980000 | 11.730000 | 10000.000000 | 289.000000 | 1.44 | 1.340000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 17:00:00 | 96.000000 | 8.270000 | 11.270000 | 78.000000 | 1016.000000 | 0.34 | 11.980000 | 12.760000 | 10000.000000 | 290.000000 | 1.76 | 1.550000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 18:00:00 | 94.000000 | 9.800000 | 12.450000 | 81.000000 | 1015.000000 | 0.57 | 12.980000 | 11.590000 | 10000.000000 | 290.000000 | 1.88 | 1.460000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 19:00:00 | 100.000000 | 12.200000 | 13.760000 | 89.000000 | 1015.000000 | 0.49 | 13.980000 | 8.330000 | 10000.000000 | 290.000000 | 2.05 | 1.310000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 20:00:00 | 100.000000 | 11.380000 | 12.680000 | 90.000000 | 1014.000000 | 0.58 | 12.980000 | 4.850000 | 7272.000000 | 282.000000 | 1.71 | 1.140000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 21:00:00 | 97.000000 | 10.390000 | 11.580000 | 90.000000 | 1014.000000 | 0.32 | 11.980000 | 1.960000 | 10000.000000 | 271.000000 | 1.54 | 0.720000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 22:00:00 | 97.000000 | 10.560000 | 11.610000 | 91.000000 | 1015.000000 | 0.15 | 11.980000 | 0.460000 | 10000.000000 | 279.000000 | 1.19 | 0.420000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 23:00:00 | 93.000000 | 9.370000 | 9.980000 | 96.000000 | 1016.000000 | 0.13 | 9.980000 | 0.000000 | 10000.000000 | 288.000000 | 1.1 | 0.370000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21201200_OWM_Clouds_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Clouds_20220112.png)
![CNE_IDEAM_Station21201200_OWM_Dewpoint_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Dewpoint_20220112.png)
![CNE_IDEAM_Station21201200_OWM_Feelslike_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Feelslike_20220112.png)
![CNE_IDEAM_Station21201200_OWM_Humidity_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Humidity_20220112.png)
![CNE_IDEAM_Station21201200_OWM_Pressure_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Pressure_20220112.png)
![CNE_IDEAM_Station21201200_OWM_Rain_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Rain_20220112.png)
![CNE_IDEAM_Station21201200_OWM_Temp_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Temp_20220112.png)
![CNE_IDEAM_Station21201200_OWM_UVI_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_UVI_20220112.png)
![CNE_IDEAM_Station21201200_OWM_Visibility_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Visibility_20220112.png)
![CNE_IDEAM_Station21201200_OWM_Windgust_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Windgust_20220112.png)
![CNE_IDEAM_Station21201200_OWM_Windspeed_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Windspeed_20220112.png)


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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201200_OWM_20220130.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220130.csv)

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

### (CNE index 3320) Open Weather values for station 21201200 - ESCUELA LA UNION [21201200]

JSON data from API OWM:

```
{'lat': 4.3429, 'lon': -74.1839, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643467037, 'sunrise': 1643454714, 'sunset': 1643497660, 'temp': 8.98, 'feels_like': 7.9, 'pressure': 1017, 'humidity': 59, 'dew_point': 1.41, 'uvi': 9.42, 'clouds': 8, 'visibility': 10000, 'wind_speed': 2.12, 'wind_deg': 304, 'wind_gust': 2.29, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, 'hourly': [{'dt': 1643414400, 'temp': 8.98, 'feels_like': 8.98, 'pressure': 1015, 'humidity': 91, 'dew_point': 7.59, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 68, 'wind_gust': 1.38, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.13}}, {'dt': 1643418000, 'temp': 8.98, 'feels_like': 8.98, 'pressure': 1016, 'humidity': 90, 'dew_point': 7.43, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 41, 'wind_gust': 1.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.91}}, {'dt': 1643421600, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1017, 'humidity': 92, 'dew_point': 6.76, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 330, 'wind_gust': 1.35, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643425200, 'temp': 6.98, 'feels_like': 6.98, 'pressure': 1018, 'humidity': 90, 'dew_point': 5.45, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 321, 'wind_gust': 1.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.86}}, {'dt': 1643428800, 'temp': 5.98, 'feels_like': 5.98, 'pressure': 1018, 'humidity': 91, 'dew_point': 4.62, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 259, 'wind_gust': 1.21, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643432400, 'temp': 5.98, 'feels_like': 5.98, 'pressure': 1017, 'humidity': 92, 'dew_point': 4.78, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 276, 'wind_gust': 1.17, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.77}}, {'dt': 1643436000, 'temp': 4.98, 'feels_like': 4.98, 'pressure': 1017, 'humidity': 92, 'dew_point': 3.79, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 181, 'wind_gust': 1.05, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643439600, 'temp': 4.98, 'feels_like': 4.98, 'pressure': 1017, 'humidity': 93, 'dew_point': 3.94, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 195, 'wind_gust': 1.53, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643443200, 'temp': 2.98, 'feels_like': 2.98, 'pressure': 1017, 'humidity': 93, 'dew_point': 1.96, 'uvi': 0, 'clouds': 32, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 221, 'wind_gust': 1.66, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643446800, 'temp': 1.98, 'feels_like': 1.98, 'pressure': 1017, 'humidity': 91, 'dew_point': 0.67, 'uvi': 0, 'clouds': 31, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 213, 'wind_gust': 1.3, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643450400, 'temp': 0.98, 'feels_like': 0.98, 'pressure': 1017, 'humidity': 92, 'dew_point': -0.15, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 226, 'wind_gust': 1.77, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643454000, 'temp': -0.02, 'feels_like': -0.02, 'pressure': 1018, 'humidity': 91, 'dew_point': -1.16, 'uvi': 0, 'clouds': 30, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 221, 'wind_gust': 1.82, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643457600, 'temp': 0.98, 'feels_like': 0.98, 'pressure': 1018, 'humidity': 87, 'dew_point': -0.83, 'uvi': 0.55, 'clouds': 7, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 216, 'wind_gust': 1.94, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643461200, 'temp': 4.98, 'feels_like': 4.98, 'pressure': 1018, 'humidity': 75, 'dew_point': 0.92, 'uvi': 2.37, 'clouds': 13, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 285, 'wind_gust': 1.42, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643464800, 'temp': 8.98, 'feels_like': 8.16, 'pressure': 1017, 'humidity': 67, 'dew_point': 3.19, 'uvi': 5.6, 'clouds': 7, 'visibility': 10000, 'wind_speed': 1.83, 'wind_deg': 300, 'wind_gust': 2.01, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643468400, 'temp': 11.98, 'feels_like': 10.77, 'pressure': 1017, 'humidity': 59, 'dew_point': 4.23, 'uvi': 9.42, 'clouds': 8, 'visibility': 10000, 'wind_speed': 2.12, 'wind_deg': 304, 'wind_gust': 2.29, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643472000, 'temp': 12.98, 'feels_like': 11.8, 'pressure': 1015, 'humidity': 56, 'dew_point': 4.42, 'uvi': 12.55, 'clouds': 9, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 308, 'wind_gust': 2.67, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643475600, 'temp': 14.98, 'feels_like': 13.97, 'pressure': 1014, 'humidity': 55, 'dew_point': 6.02, 'uvi': 13.66, 'clouds': 11, 'visibility': 10000, 'wind_speed': 2.51, 'wind_deg': 308, 'wind_gust': 2.95, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643479200, 'temp': 13.98, 'feels_like': 12.97, 'pressure': 1013, 'humidity': 59, 'dew_point': 6.1, 'uvi': 12.4, 'clouds': 44, 'visibility': 10000, 'wind_speed': 2.54, 'wind_deg': 307, 'wind_gust': 2.91, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643482800, 'temp': 14.98, 'feels_like': 14.15, 'pressure': 1012, 'humidity': 62, 'dew_point': 7.77, 'uvi': 9.06, 'clouds': 54, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 305, 'wind_gust': 2.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1643486400, 'temp': 13.98, 'feels_like': 13.24, 'pressure': 1012, 'humidity': 69, 'dew_point': 8.39, 'uvi': 5.28, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.8, 'wind_deg': 302, 'wind_gust': 2.78, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.27}}, {'dt': 1643490000, 'temp': 13.98, 'feels_like': 13.42, 'pressure': 1012, 'humidity': 76, 'dew_point': 9.82, 'uvi': 2.16, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 297, 'wind_gust': 2.48, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.23}}, {'dt': 1643493600, 'temp': 12.98, 'feels_like': 12.53, 'pressure': 1013, 'humidity': 84, 'dew_point': 10.34, 'uvi': 0.45, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 295, 'wind_gust': 2.09, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1643497200, 'temp': 10.98, 'feels_like': 10.54, 'pressure': 1015, 'humidity': 92, 'dew_point': 9.73, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 299, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 00:00:00 | 94.000000 | 7.590000 | 8.980000 | 91.000000 | 1015.000000 | 1.13 | 8.980000 | 0.000000 | 10000.000000 | 68.000000 | 1.38 | 0.820000 | 501 | Rain | moderate rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 01:00:00 | 99.000000 | 7.430000 | 8.980000 | 90.000000 | 1016.000000 | 0.91 | 8.980000 | 0.000000 | 10000.000000 | 41.000000 | 1.57 | 0.910000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 02:00:00 | 77.000000 | 6.760000 | 7.980000 | 92.000000 | 1017.000000 |  | 7.980000 | 0.000000 | 10000.000000 | 330.000000 | 1.35 | 0.650000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 03:00:00 | 89.000000 | 5.450000 | 6.980000 | 90.000000 | 1018.000000 | 0.86 | 6.980000 | 0.000000 | 10000.000000 | 321.000000 | 1.24 | 0.570000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 04:00:00 | 83.000000 | 4.620000 | 5.980000 | 91.000000 | 1018.000000 |  | 5.980000 | 0.000000 | 10000.000000 | 259.000000 | 1.21 | 0.190000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 05:00:00 | 85.000000 | 4.780000 | 5.980000 | 92.000000 | 1017.000000 | 0.77 | 5.980000 | 0.000000 | 10000.000000 | 276.000000 | 1.17 | 0.310000 | 500 | Rain | light rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 06:00:00 | 80.000000 | 3.790000 | 4.980000 | 92.000000 | 1017.000000 |  | 4.980000 | 0.000000 | 10000.000000 | 181.000000 | 1.05 | 0.200000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 07:00:00 | 33.000000 | 3.940000 | 4.980000 | 93.000000 | 1017.000000 |  | 4.980000 | 0.000000 | 10000.000000 | 195.000000 | 1.53 | 0.520000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 08:00:00 | 32.000000 | 1.960000 | 2.980000 | 93.000000 | 1017.000000 |  | 2.980000 | 0.000000 | 10000.000000 | 221.000000 | 1.66 | 0.520000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 09:00:00 | 31.000000 | 0.670000 | 1.980000 | 91.000000 | 1017.000000 |  | 1.980000 | 0.000000 | 10000.000000 | 213.000000 | 1.3 | 0.300000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 10:00:00 | 33.000000 | -0.150000 | 0.980000 | 92.000000 | 1017.000000 |  | 0.980000 | 0.000000 | 10000.000000 | 226.000000 | 1.77 | 0.600000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 11:00:00 | 30.000000 | -1.160000 | -0.020000 | 91.000000 | 1018.000000 |  | -0.020000 | 0.000000 | 10000.000000 | 221.000000 | 1.82 | 0.570000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 12:00:00 | 7.000000 | -0.830000 | 0.980000 | 87.000000 | 1018.000000 |  | 0.980000 | 0.550000 | 10000.000000 | 216.000000 | 1.94 | 0.380000 | 800 | Clear | clear sky | 01d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 13:00:00 | 13.000000 | 0.920000 | 4.980000 | 75.000000 | 1018.000000 |  | 4.980000 | 2.370000 | 10000.000000 | 285.000000 | 1.42 | 1.010000 | 801 | Clouds | few clouds | 02d | 13 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 14:00:00 | 7.000000 | 3.190000 | 8.160000 | 67.000000 | 1017.000000 |  | 8.980000 | 5.600000 | 10000.000000 | 300.000000 | 2.01 | 1.830000 | 800 | Clear | clear sky | 01d | 14 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 15:00:00 | 8.000000 | 4.230000 | 10.770000 | 59.000000 | 1017.000000 |  | 11.980000 | 9.420000 | 10000.000000 | 304.000000 | 2.29 | 2.120000 | 800 | Clear | clear sky | 01d | 15 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 16:00:00 | 9.000000 | 4.420000 | 11.800000 | 56.000000 | 1015.000000 |  | 12.980000 | 12.550000 | 10000.000000 | 308.000000 | 2.67 | 2.260000 | 800 | Clear | clear sky | 01d | 16 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 17:00:00 | 11.000000 | 6.020000 | 13.970000 | 55.000000 | 1014.000000 |  | 14.980000 | 13.660000 | 10000.000000 | 308.000000 | 2.95 | 2.510000 | 801 | Clouds | few clouds | 02d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 18:00:00 | 44.000000 | 6.100000 | 12.970000 | 59.000000 | 1013.000000 |  | 13.980000 | 12.400000 | 10000.000000 | 307.000000 | 2.91 | 2.540000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 19:00:00 | 54.000000 | 7.770000 | 14.150000 | 62.000000 | 1012.000000 | 0.2 | 14.980000 | 9.060000 | 10000.000000 | 305.000000 | 2.87 | 2.260000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 20:00:00 | 61.000000 | 8.390000 | 13.240000 | 69.000000 | 1012.000000 | 0.27 | 13.980000 | 5.280000 | 10000.000000 | 302.000000 | 2.78 | 1.800000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 21:00:00 | 72.000000 | 9.820000 | 13.420000 | 76.000000 | 1012.000000 | 0.23 | 13.980000 | 2.160000 | 10000.000000 | 297.000000 | 2.48 | 1.550000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 22:00:00 | 79.000000 | 10.340000 | 12.530000 | 84.000000 | 1013.000000 | 0.26 | 12.980000 | 0.450000 | 10000.000000 | 295.000000 | 2.09 | 1.060000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 23:00:00 | 83.000000 | 9.730000 | 10.540000 | 92.000000 | 1015.000000 | 0.14 | 10.980000 | 0.000000 | 10000.000000 | 299.000000 | 1.25 | 0.570000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21201200_OWM_Clouds_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Clouds_20220130.png)
![CNE_IDEAM_Station21201200_OWM_Dewpoint_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Dewpoint_20220130.png)
![CNE_IDEAM_Station21201200_OWM_Feelslike_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Feelslike_20220130.png)
![CNE_IDEAM_Station21201200_OWM_Humidity_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Humidity_20220130.png)
![CNE_IDEAM_Station21201200_OWM_Pressure_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Pressure_20220130.png)
![CNE_IDEAM_Station21201200_OWM_Rain_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Rain_20220130.png)
![CNE_IDEAM_Station21201200_OWM_Temp_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Temp_20220130.png)
![CNE_IDEAM_Station21201200_OWM_UVI_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_UVI_20220130.png)
![CNE_IDEAM_Station21201200_OWM_Visibility_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Visibility_20220130.png)
![CNE_IDEAM_Station21201200_OWM_Winddeg_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Winddeg_20220130.png)
![CNE_IDEAM_Station21201200_OWM_Windgust_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Windgust_20220130.png)
![CNE_IDEAM_Station21201200_OWM_Windspeed_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Windspeed_20220130.png)

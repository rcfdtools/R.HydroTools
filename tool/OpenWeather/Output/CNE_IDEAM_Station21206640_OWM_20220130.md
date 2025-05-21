
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206640_OWM_20220130.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220130.csv)

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

### (CNE index 2379) Open Weather values for station 21206640 - SAN JOSE [21206640]

JSON data from API OWM:

```
{'lat': 4.5016, 'lon': -74.1193, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643467037, 'sunrise': 1643454710, 'sunset': 1643497632, 'temp': 13.03, 'feels_like': 11.77, 'pressure': 1016, 'humidity': 53, 'dew_point': 3.68, 'uvi': 9.24, 'clouds': 4, 'visibility': 10000, 'wind_speed': 2.42, 'wind_deg': 308, 'wind_gust': 2.3, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, 'hourly': [{'dt': 1643414400, 'temp': 13.03, 'feels_like': 12.63, 'pressure': 1015, 'humidity': 86, 'dew_point': 10.75, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 97, 'wind_gust': 1.42, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.91}}, {'dt': 1643418000, 'temp': 13.03, 'feels_like': 12.66, 'pressure': 1016, 'humidity': 87, 'dew_point': 10.92, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 66, 'wind_gust': 1.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.6}}, {'dt': 1643421600, 'temp': 12.03, 'feels_like': 11.66, 'pressure': 1017, 'humidity': 91, 'dew_point': 10.61, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 349, 'wind_gust': 0.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1643425200, 'temp': 11.03, 'feels_like': 10.46, 'pressure': 1017, 'humidity': 87, 'dew_point': 8.95, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 12, 'wind_gust': 0.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.39}}, {'dt': 1643428800, 'temp': 10.03, 'feels_like': 9.44, 'pressure': 1017, 'humidity': 90, 'dew_point': 8.47, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 292, 'wind_gust': 1.25, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643432400, 'temp': 10.03, 'feels_like': 9.41, 'pressure': 1017, 'humidity': 89, 'dew_point': 8.3, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 301, 'wind_gust': 1.33, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1643436000, 'temp': 9.03, 'feels_like': 9.03, 'pressure': 1016, 'humidity': 89, 'dew_point': 7.32, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 286, 'wind_gust': 0.92, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643439600, 'temp': 9.03, 'feels_like': 9.03, 'pressure': 1016, 'humidity': 92, 'dew_point': 7.8, 'uvi': 0, 'clouds': 27, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 255, 'wind_gust': 1.61, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643443200, 'temp': 7.03, 'feels_like': 7.03, 'pressure': 1016, 'humidity': 92, 'dew_point': 5.82, 'uvi': 0, 'clouds': 21, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 285, 'wind_gust': 1.87, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643446800, 'temp': 6.03, 'feels_like': 6.03, 'pressure': 1016, 'humidity': 92, 'dew_point': 4.83, 'uvi': 0, 'clouds': 30, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 295, 'wind_gust': 1.21, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643450400, 'temp': 5.03, 'feels_like': 5.03, 'pressure': 1017, 'humidity': 93, 'dew_point': 3.99, 'uvi': 0, 'clouds': 19, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 286, 'wind_gust': 1.87, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643454000, 'temp': 4.03, 'feels_like': 4.03, 'pressure': 1017, 'humidity': 93, 'dew_point': 3, 'uvi': 0, 'clouds': 16, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 288, 'wind_gust': 1.83, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643457600, 'temp': 5.03, 'feels_like': 5.03, 'pressure': 1018, 'humidity': 88, 'dew_point': 3.21, 'uvi': 0.54, 'clouds': 5, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 298, 'wind_gust': 2.14, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643461200, 'temp': 9.03, 'feels_like': 8.55, 'pressure': 1017, 'humidity': 75, 'dew_point': 4.84, 'uvi': 2.31, 'clouds': 9, 'visibility': 10000, 'wind_speed': 1.49, 'wind_deg': 298, 'wind_gust': 1.99, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643464800, 'temp': 13.03, 'feels_like': 12.03, 'pressure': 1017, 'humidity': 63, 'dew_point': 6.16, 'uvi': 5.48, 'clouds': 6, 'visibility': 10000, 'wind_speed': 2.16, 'wind_deg': 306, 'wind_gust': 2.29, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643468400, 'temp': 16.03, 'feels_like': 15.07, 'pressure': 1016, 'humidity': 53, 'dew_point': 6.46, 'uvi': 9.24, 'clouds': 4, 'visibility': 10000, 'wind_speed': 2.42, 'wind_deg': 308, 'wind_gust': 2.3, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643472000, 'temp': 17.03, 'feels_like': 16.02, 'pressure': 1015, 'humidity': 47, 'dew_point': 5.65, 'uvi': 12.35, 'clouds': 4, 'visibility': 10000, 'wind_speed': 2.65, 'wind_deg': 312, 'wind_gust': 2.45, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643475600, 'temp': 19.03, 'feels_like': 18.14, 'pressure': 1013, 'humidity': 44, 'dew_point': 6.51, 'uvi': 13.45, 'clouds': 10, 'visibility': 10000, 'wind_speed': 2.93, 'wind_deg': 313, 'wind_gust': 2.69, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643479200, 'temp': 18.03, 'feels_like': 17.04, 'pressure': 1012, 'humidity': 44, 'dew_point': 5.61, 'uvi': 12.2, 'clouds': 27, 'visibility': 10000, 'wind_speed': 2.96, 'wind_deg': 308, 'wind_gust': 2.7, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643482800, 'temp': 19.03, 'feels_like': 18.14, 'pressure': 1011, 'humidity': 44, 'dew_point': 6.51, 'uvi': 9.16, 'clouds': 23, 'visibility': 10000, 'wind_speed': 2.75, 'wind_deg': 307, 'wind_gust': 2.72, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643486400, 'temp': 18.03, 'feels_like': 17.09, 'pressure': 1010, 'humidity': 46, 'dew_point': 6.25, 'uvi': 5.33, 'clouds': 18, 'visibility': 10000, 'wind_speed': 2.19, 'wind_deg': 295, 'wind_gust': 2.83, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643490000, 'temp': 18.03, 'feels_like': 17.32, 'pressure': 1010, 'humidity': 55, 'dew_point': 8.86, 'uvi': 2.17, 'clouds': 37, 'visibility': 10000, 'wind_speed': 1.82, 'wind_deg': 287, 'wind_gust': 2.74, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643493600, 'temp': 17.03, 'feels_like': 16.59, 'pressure': 1012, 'humidity': 69, 'dew_point': 11.31, 'uvi': 0.46, 'clouds': 53, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 283, 'wind_gust': 2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1643497200, 'temp': 15.03, 'feels_like': 14.86, 'pressure': 1014, 'humidity': 87, 'dew_point': 12.89, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 301, 'wind_gust': 1.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 00:00:00 | 98.000000 | 10.750000 | 12.630000 | 86.000000 | 1015.000000 | 0.91 | 13.030000 | 0.000000 | 10000.000000 | 97.000000 | 1.42 | 0.590000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 01:00:00 | 100.000000 | 10.920000 | 12.660000 | 87.000000 | 1016.000000 | 0.6 | 13.030000 | 0.000000 | 10000.000000 | 66.000000 | 1.59 | 0.720000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 02:00:00 | 51.000000 | 10.610000 | 11.660000 | 91.000000 | 1017.000000 | 0.12 | 12.030000 | 0.000000 | 10000.000000 | 349.000000 | 0.98 | 0.330000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 03:00:00 | 83.000000 | 8.950000 | 10.460000 | 87.000000 | 1017.000000 | 0.39 | 11.030000 | 0.000000 | 10000.000000 | 12.000000 | 0.81 | 0.200000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 04:00:00 | 60.000000 | 8.470000 | 9.440000 | 90.000000 | 1017.000000 |  | 10.030000 | 0.000000 | 10000.000000 | 292.000000 | 1.25 | 0.540000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 05:00:00 | 87.000000 | 8.300000 | 9.410000 | 89.000000 | 1017.000000 | 0.24 | 10.030000 | 0.000000 | 10000.000000 | 301.000000 | 1.33 | 0.710000 | 500 | Rain | light rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 06:00:00 | 83.000000 | 7.320000 | 9.030000 | 89.000000 | 1016.000000 |  | 9.030000 | 0.000000 | 10000.000000 | 286.000000 | 0.92 | 0.460000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 07:00:00 | 27.000000 | 7.800000 | 9.030000 | 92.000000 | 1016.000000 |  | 9.030000 | 0.000000 | 10000.000000 | 255.000000 | 1.61 | 0.670000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 08:00:00 | 21.000000 | 5.820000 | 7.030000 | 92.000000 | 1016.000000 |  | 7.030000 | 0.000000 | 10000.000000 | 285.000000 | 1.87 | 0.730000 | 801 | Clouds | few clouds | 02n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 09:00:00 | 30.000000 | 4.830000 | 6.030000 | 92.000000 | 1016.000000 |  | 6.030000 | 0.000000 | 10000.000000 | 295.000000 | 1.21 | 0.560000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 10:00:00 | 19.000000 | 3.990000 | 5.030000 | 93.000000 | 1017.000000 |  | 5.030000 | 0.000000 | 10000.000000 | 286.000000 | 1.87 | 0.890000 | 801 | Clouds | few clouds | 02n | 10 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 11:00:00 | 16.000000 | 3.000000 | 4.030000 | 93.000000 | 1017.000000 |  | 4.030000 | 0.000000 | 10000.000000 | 288.000000 | 1.83 | 0.980000 | 801 | Clouds | few clouds | 02n | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 12:00:00 | 5.000000 | 3.210000 | 5.030000 | 88.000000 | 1018.000000 |  | 5.030000 | 0.540000 | 10000.000000 | 298.000000 | 2.14 | 0.800000 | 800 | Clear | clear sky | 01d | 12 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 13:00:00 | 9.000000 | 4.840000 | 8.550000 | 75.000000 | 1017.000000 |  | 9.030000 | 2.310000 | 10000.000000 | 298.000000 | 1.99 | 1.490000 | 800 | Clear | clear sky | 01d | 13 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 14:00:00 | 6.000000 | 6.160000 | 12.030000 | 63.000000 | 1017.000000 |  | 13.030000 | 5.480000 | 10000.000000 | 306.000000 | 2.29 | 2.160000 | 800 | Clear | clear sky | 01d | 14 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 15:00:00 | 4.000000 | 6.460000 | 15.070000 | 53.000000 | 1016.000000 |  | 16.030000 | 9.240000 | 10000.000000 | 308.000000 | 2.3 | 2.420000 | 800 | Clear | clear sky | 01d | 15 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 16:00:00 | 4.000000 | 5.650000 | 16.020000 | 47.000000 | 1015.000000 |  | 17.030000 | 12.350000 | 10000.000000 | 312.000000 | 2.45 | 2.650000 | 800 | Clear | clear sky | 01d | 16 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 17:00:00 | 10.000000 | 6.510000 | 18.140000 | 44.000000 | 1013.000000 |  | 19.030000 | 13.450000 | 10000.000000 | 313.000000 | 2.69 | 2.930000 | 800 | Clear | clear sky | 01d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 18:00:00 | 27.000000 | 5.610000 | 17.040000 | 44.000000 | 1012.000000 |  | 18.030000 | 12.200000 | 10000.000000 | 308.000000 | 2.7 | 2.960000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 19:00:00 | 23.000000 | 6.510000 | 18.140000 | 44.000000 | 1011.000000 |  | 19.030000 | 9.160000 | 10000.000000 | 307.000000 | 2.72 | 2.750000 | 801 | Clouds | few clouds | 02d | 19 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 20:00:00 | 18.000000 | 6.250000 | 17.090000 | 46.000000 | 1010.000000 |  | 18.030000 | 5.330000 | 10000.000000 | 295.000000 | 2.83 | 2.190000 | 801 | Clouds | few clouds | 02d | 20 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 21:00:00 | 37.000000 | 8.860000 | 17.320000 | 55.000000 | 1010.000000 |  | 18.030000 | 2.170000 | 10000.000000 | 287.000000 | 2.74 | 1.820000 | 802 | Clouds | scattered clouds | 03d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 22:00:00 | 53.000000 | 11.310000 | 16.590000 | 69.000000 | 1012.000000 | 0.15 | 17.030000 | 0.460000 | 10000.000000 | 283.000000 | 2 | 1.010000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 23:00:00 | 62.000000 | 12.890000 | 14.860000 | 87.000000 | 1014.000000 | 0.15 | 15.030000 | 0.000000 | 10000.000000 | 301.000000 | 1.57 | 0.490000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21206640_OWM_Clouds_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Clouds_20220130.png)
![CNE_IDEAM_Station21206640_OWM_Dewpoint_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Dewpoint_20220130.png)
![CNE_IDEAM_Station21206640_OWM_Feelslike_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Feelslike_20220130.png)
![CNE_IDEAM_Station21206640_OWM_Humidity_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Humidity_20220130.png)
![CNE_IDEAM_Station21206640_OWM_Pressure_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Pressure_20220130.png)
![CNE_IDEAM_Station21206640_OWM_Rain_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Rain_20220130.png)
![CNE_IDEAM_Station21206640_OWM_Temp_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Temp_20220130.png)
![CNE_IDEAM_Station21206640_OWM_UVI_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_UVI_20220130.png)
![CNE_IDEAM_Station21206640_OWM_Visibility_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Visibility_20220130.png)
![CNE_IDEAM_Station21206640_OWM_Winddeg_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Winddeg_20220130.png)
![CNE_IDEAM_Station21206640_OWM_Windgust_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Windgust_20220130.png)
![CNE_IDEAM_Station21206640_OWM_Windspeed_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Windspeed_20220130.png)

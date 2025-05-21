
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SAN JOSE [21206640] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206640_OWM_20220112.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220112.csv)

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

### (CNE index 2381) Open Weather values for station 21206640 - SAN JOSE [21206640]

JSON data from API OWM:

```
{'lat': 4.5016, 'lon': -74.1193, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641899465, 'sunrise': 1641899269, 'sunset': 1641942035, 'temp': 10.03, 'feels_like': 9.46, 'pressure': 1017, 'humidity': 91, 'dew_point': 8.63, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 347, 'wind_gust': 0.64, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641859200, 'temp': 13.03, 'feels_like': 12.76, 'pressure': 1016, 'humidity': 91, 'dew_point': 11.6, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 133, 'wind_gust': 1.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641862800, 'temp': 13.03, 'feels_like': 12.76, 'pressure': 1017, 'humidity': 91, 'dew_point': 11.6, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 33, 'wind_gust': 1.04, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641866400, 'temp': 12.03, 'feels_like': 11.69, 'pressure': 1018, 'humidity': 92, 'dew_point': 10.77, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 51, 'wind_gust': 0.89, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641870000, 'temp': 12.03, 'feels_like': 11.69, 'pressure': 1018, 'humidity': 92, 'dew_point': 10.77, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 157, 'wind_gust': 0.86, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641873600, 'temp': 12.03, 'feels_like': 11.61, 'pressure': 1018, 'humidity': 89, 'dew_point': 10.27, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.09, 'wind_deg': 27, 'wind_gust': 0.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641877200, 'temp': 12.03, 'feels_like': 11.61, 'pressure': 1017, 'humidity': 89, 'dew_point': 10.27, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.11, 'wind_deg': 15, 'wind_gust': 0.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641880800, 'temp': 12.03, 'feels_like': 11.61, 'pressure': 1017, 'humidity': 89, 'dew_point': 10.27, 'uvi': 0, 'clouds': 53, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 297, 'wind_gust': 0.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641884400, 'temp': 12.03, 'feels_like': 11.66, 'pressure': 1016, 'humidity': 91, 'dew_point': 10.61, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 305, 'wind_gust': 1.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641888000, 'temp': 11.03, 'feels_like': 10.59, 'pressure': 1016, 'humidity': 92, 'dew_point': 9.78, 'uvi': 0, 'clouds': 64, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 316, 'wind_gust': 0.95, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641891600, 'temp': 11.03, 'feels_like': 10.62, 'pressure': 1016, 'humidity': 93, 'dew_point': 9.94, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 302, 'wind_gust': 1.27, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641895200, 'temp': 10.03, 'feels_like': 9.52, 'pressure': 1016, 'humidity': 93, 'dew_point': 8.95, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 319, 'wind_gust': 0.95, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641898800, 'temp': 10.03, 'feels_like': 9.46, 'pressure': 1017, 'humidity': 91, 'dew_point': 8.63, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 347, 'wind_gust': 0.64, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641902400, 'temp': 10.03, 'feels_like': 9.41, 'pressure': 1017, 'humidity': 89, 'dew_point': 8.3, 'uvi': 0.47, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 326, 'wind_gust': 0.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641906000, 'temp': 12.03, 'feels_like': 11.43, 'pressure': 1018, 'humidity': 82, 'dew_point': 9.06, 'uvi': 1.89, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 320, 'wind_gust': 0.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641909600, 'temp': 13.03, 'feels_like': 12.4, 'pressure': 1018, 'humidity': 77, 'dew_point': 9.1, 'uvi': 4.54, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 316, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641913200, 'temp': 13.03, 'feels_like': 12.22, 'pressure': 1018, 'humidity': 70, 'dew_point': 7.69, 'uvi': 7.68, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 316, 'wind_gust': 1.27, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641916800, 'temp': 14.03, 'feels_like': 13.19, 'pressure': 1016, 'humidity': 65, 'dew_point': 7.56, 'uvi': 11.23, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 267, 'wind_gust': 1.68, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641920400, 'temp': 16.03, 'feels_like': 15.41, 'pressure': 1015, 'humidity': 66, 'dew_point': 9.69, 'uvi': 12.22, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 253, 'wind_gust': 1.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.28}}, {'dt': 1641924000, 'temp': 17.03, 'feels_like': 16.67, 'pressure': 1014, 'humidity': 72, 'dew_point': 11.95, 'uvi': 11.09, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 246, 'wind_gust': 1.95, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, {'dt': 1641927600, 'temp': 18.03, 'feels_like': 18.06, 'pressure': 1014, 'humidity': 83, 'dew_point': 15.1, 'uvi': 5.75, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 254, 'wind_gust': 1.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.46}}, {'dt': 1641931200, 'temp': 17.03, 'feels_like': 16.96, 'pressure': 1013, 'humidity': 83, 'dew_point': 14.12, 'uvi': 3.34, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 258, 'wind_gust': 1.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.55}}, {'dt': 1641934800, 'temp': 16.03, 'feels_like': 15.88, 'pressure': 1014, 'humidity': 84, 'dew_point': 13.33, 'uvi': 1.34, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 271, 'wind_gust': 1.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.4}}, {'dt': 1641938400, 'temp': 16.03, 'feels_like': 15.99, 'pressure': 1014, 'humidity': 88, 'dew_point': 14.04, 'uvi': 0.44, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 220, 'wind_gust': 1.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641942000, 'temp': 14.03, 'feels_like': 13.94, 'pressure': 1016, 'humidity': 94, 'dew_point': 13.08, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 140, 'wind_gust': 1.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 00:00:00 | 73.000000 | 11.600000 | 12.760000 | 91.000000 | 1016.000000 |  | 13.030000 | 0.000000 | 10000.000000 | 133.000000 | 1.02 | 0.280000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 01:00:00 | 78.000000 | 11.600000 | 12.760000 | 91.000000 | 1017.000000 |  | 13.030000 | 0.000000 | 10000.000000 | 33.000000 | 1.04 | 0.500000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 02:00:00 | 84.000000 | 10.770000 | 11.690000 | 92.000000 | 1018.000000 |  | 12.030000 | 0.000000 | 10000.000000 | 51.000000 | 0.89 | 0.300000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 03:00:00 | 79.000000 | 10.770000 | 11.690000 | 92.000000 | 1018.000000 |  | 12.030000 | 0.000000 | 10000.000000 | 157.000000 | 0.86 | 0.210000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 04:00:00 | 81.000000 | 10.270000 | 11.610000 | 89.000000 | 1018.000000 |  | 12.030000 | 0.000000 | 10000.000000 | 27.000000 | 0.85 | 0.090000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 05:00:00 | 85.000000 | 10.270000 | 11.610000 | 89.000000 | 1017.000000 |  | 12.030000 | 0.000000 | 10000.000000 | 15.000000 | 0.71 | 0.110000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 06:00:00 | 53.000000 | 10.270000 | 11.610000 | 89.000000 | 1017.000000 | 0.12 | 12.030000 | 0.000000 | 10000.000000 | 297.000000 | 0.76 | 0.440000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 07:00:00 | 66.000000 | 10.610000 | 11.660000 | 91.000000 | 1016.000000 |  | 12.030000 | 0.000000 | 10000.000000 | 305.000000 | 1.11 | 0.590000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 08:00:00 | 64.000000 | 9.780000 | 10.590000 | 92.000000 | 1016.000000 |  | 11.030000 | 0.000000 | 10000.000000 | 316.000000 | 0.95 | 0.760000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 09:00:00 | 76.000000 | 9.940000 | 10.620000 | 93.000000 | 1016.000000 |  | 11.030000 | 0.000000 | 10000.000000 | 302.000000 | 1.27 | 1.050000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 10:00:00 | 82.000000 | 8.950000 | 9.520000 | 93.000000 | 1016.000000 |  | 10.030000 | 0.000000 | 10000.000000 | 319.000000 | 0.95 | 0.600000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 11:00:00 | 86.000000 | 8.630000 | 9.460000 | 91.000000 | 1017.000000 |  | 10.030000 | 0.000000 | 10000.000000 | 347.000000 | 0.64 | 0.440000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 12:00:00 | 85.000000 | 8.300000 | 9.410000 | 89.000000 | 1017.000000 |  | 10.030000 | 0.470000 | 10000.000000 | 326.000000 | 0.85 | 0.460000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 13:00:00 | 95.000000 | 9.060000 | 11.430000 | 82.000000 | 1018.000000 |  | 12.030000 | 1.890000 | 10000.000000 | 320.000000 | 0.9 | 0.690000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 14:00:00 | 97.000000 | 9.100000 | 12.400000 | 77.000000 | 1018.000000 |  | 13.030000 | 4.540000 | 10000.000000 | 316.000000 | 0.95 | 0.630000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 15:00:00 | 96.000000 | 7.690000 | 12.220000 | 70.000000 | 1018.000000 |  | 13.030000 | 7.680000 | 10000.000000 | 316.000000 | 1.27 | 0.960000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 16:00:00 | 95.000000 | 7.560000 | 13.190000 | 65.000000 | 1016.000000 | 0.16 | 14.030000 | 11.230000 | 10000.000000 | 267.000000 | 1.68 | 1.060000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 17:00:00 | 94.000000 | 9.690000 | 15.410000 | 66.000000 | 1015.000000 | 0.28 | 16.030000 | 12.220000 | 10000.000000 | 253.000000 | 1.91 | 1.170000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 18:00:00 | 91.000000 | 11.950000 | 16.670000 | 72.000000 | 1014.000000 | 0.53 | 17.030000 | 11.090000 | 10000.000000 | 246.000000 | 1.95 | 0.830000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 19:00:00 | 100.000000 | 15.100000 | 18.060000 | 83.000000 | 1014.000000 | 0.46 | 18.030000 | 5.750000 | 10000.000000 | 254.000000 | 1.85 | 0.750000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 20:00:00 | 99.000000 | 14.120000 | 16.960000 | 83.000000 | 1013.000000 | 0.55 | 17.030000 | 3.340000 | 10000.000000 | 258.000000 | 1.72 | 0.820000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 21:00:00 | 95.000000 | 13.330000 | 15.880000 | 84.000000 | 1014.000000 | 0.4 | 16.030000 | 1.340000 | 10000.000000 | 271.000000 | 1.67 | 0.520000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 22:00:00 | 94.000000 | 14.040000 | 15.990000 | 88.000000 | 1014.000000 | 0.18 | 16.030000 | 0.440000 | 10000.000000 | 220.000000 | 1.23 | 0.200000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 23:00:00 | 91.000000 | 13.080000 | 13.940000 | 94.000000 | 1016.000000 | 0.16 | 14.030000 | 0.000000 | 10000.000000 | 140.000000 | 1.03 | 0.170000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21206640_OWM_Clouds_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Clouds_20220112.png)
![CNE_IDEAM_Station21206640_OWM_Dewpoint_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Dewpoint_20220112.png)
![CNE_IDEAM_Station21206640_OWM_Feelslike_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Feelslike_20220112.png)
![CNE_IDEAM_Station21206640_OWM_Humidity_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Humidity_20220112.png)
![CNE_IDEAM_Station21206640_OWM_Pressure_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Pressure_20220112.png)
![CNE_IDEAM_Station21206640_OWM_Rain_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Rain_20220112.png)
![CNE_IDEAM_Station21206640_OWM_Temp_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Temp_20220112.png)
![CNE_IDEAM_Station21206640_OWM_UVI_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_UVI_20220112.png)
![CNE_IDEAM_Station21206640_OWM_Visibility_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Visibility_20220112.png)
![CNE_IDEAM_Station21206640_OWM_Windgust_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Windgust_20220112.png)
![CNE_IDEAM_Station21206640_OWM_Windspeed_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Windspeed_20220112.png)

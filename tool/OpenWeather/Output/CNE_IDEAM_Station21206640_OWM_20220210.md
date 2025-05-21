
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

* Current date time: 2022-02-10 14:08:04.180886
* Unix time to eval: 1644329284
* Days before (for historical data): 2
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220210.xls
* CNE IDEAM file downloaded and updated: No
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206640_OWM_20220210.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220210.csv)

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

### (CNE index 2376) Open Weather values for station 21206640 - SAN JOSE [21206640]

JSON data from API OWM:

```
{'lat': 4.5016, 'lon': -74.1193, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644329284, 'sunrise': 1644318724, 'sunset': 1644361760, 'temp': 13.03, 'feels_like': 12.56, 'pressure': 1018, 'humidity': 83, 'dew_point': 10.21, 'uvi': 3.22, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 153, 'wind_gust': 1.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644278400, 'temp': 13.03, 'feels_like': 12.79, 'pressure': 1016, 'humidity': 92, 'dew_point': 11.76, 'uvi': 0, 'clouds': 100, 'visibility': 7467, 'wind_speed': 0.93, 'wind_deg': 126, 'wind_gust': 1.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644282000, 'temp': 13.03, 'feels_like': 12.79, 'pressure': 1017, 'humidity': 92, 'dew_point': 11.76, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 126, 'wind_gust': 2.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644285600, 'temp': 12.03, 'feels_like': 11.69, 'pressure': 1018, 'humidity': 92, 'dew_point': 10.77, 'uvi': 0, 'clouds': 100, 'visibility': 7601, 'wind_speed': 1.58, 'wind_deg': 121, 'wind_gust': 2.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.42}}, {'dt': 1644289200, 'temp': 12.03, 'feels_like': 11.72, 'pressure': 1019, 'humidity': 93, 'dew_point': 10.93, 'uvi': 0, 'clouds': 100, 'visibility': 6649, 'wind_speed': 1.75, 'wind_deg': 115, 'wind_gust': 2.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.49}}, {'dt': 1644292800, 'temp': 12.03, 'feels_like': 11.72, 'pressure': 1019, 'humidity': 93, 'dew_point': 10.93, 'uvi': 0, 'clouds': 100, 'visibility': 2803, 'wind_speed': 1.36, 'wind_deg': 128, 'wind_gust': 2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.65}}, {'dt': 1644296400, 'temp': 12.03, 'feels_like': 11.72, 'pressure': 1018, 'humidity': 93, 'dew_point': 10.93, 'uvi': 0, 'clouds': 100, 'visibility': 7959, 'wind_speed': 0.7, 'wind_deg': 141, 'wind_gust': 1.25, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.15}}, {'dt': 1644300000, 'temp': 11.03, 'feels_like': 10.64, 'pressure': 1018, 'humidity': 94, 'dew_point': 10.1, 'uvi': 0, 'clouds': 100, 'visibility': 9339, 'wind_speed': 0.29, 'wind_deg': 142, 'wind_gust': 0.81, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.54}}, {'dt': 1644303600, 'temp': 12.03, 'feels_like': 11.72, 'pressure': 1017, 'humidity': 93, 'dew_point': 10.93, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 118, 'wind_gust': 0.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 1}}, {'dt': 1644307200, 'temp': 12.03, 'feels_like': 11.69, 'pressure': 1016, 'humidity': 92, 'dew_point': 10.77, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 149, 'wind_gust': 0.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.56}}, {'dt': 1644310800, 'temp': 12.03, 'feels_like': 11.69, 'pressure': 1016, 'humidity': 92, 'dew_point': 10.77, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 200, 'wind_gust': 0.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644314400, 'temp': 12.03, 'feels_like': 11.66, 'pressure': 1016, 'humidity': 91, 'dew_point': 10.61, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 136, 'wind_gust': 0.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644318000, 'temp': 11.03, 'feels_like': 10.56, 'pressure': 1017, 'humidity': 91, 'dew_point': 9.62, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 135, 'wind_gust': 0.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644321600, 'temp': 11.03, 'feels_like': 10.54, 'pressure': 1018, 'humidity': 90, 'dew_point': 9.45, 'uvi': 0.28, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 135, 'wind_gust': 0.98, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644325200, 'temp': 13.03, 'feels_like': 12.71, 'pressure': 1018, 'humidity': 89, 'dew_point': 11.26, 'uvi': 1.36, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 121, 'wind_gust': 1.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644328800, 'temp': 13.03, 'feels_like': 12.56, 'pressure': 1018, 'humidity': 83, 'dew_point': 10.21, 'uvi': 3.22, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 153, 'wind_gust': 1.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644332400, 'temp': 14.03, 'feels_like': 13.45, 'pressure': 1017, 'humidity': 75, 'dew_point': 9.67, 'uvi': 5.42, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 157, 'wind_gust': 1.97, 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'}], 'rain': {'1h': 9.99}}, {'dt': 1644336000, 'temp': 12.03, 'feels_like': 11.25, 'pressure': 1016, 'humidity': 75, 'dew_point': 7.74, 'uvi': 9.18, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 178, 'wind_gust': 2.28, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.37}}, {'dt': 1644339600, 'temp': 11.03, 'feels_like': 10.33, 'pressure': 1016, 'humidity': 82, 'dew_point': 8.08, 'uvi': 9.99, 'clouds': 100, 'visibility': 9975, 'wind_speed': 0.7, 'wind_deg': 165, 'wind_gust': 1.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644343200, 'temp': 13.03, 'feels_like': 12.61, 'pressure': 1015, 'humidity': 85, 'dew_point': 10.57, 'uvi': 9.07, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 126, 'wind_gust': 1.55, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644346800, 'temp': 14.03, 'feels_like': 13.73, 'pressure': 1015, 'humidity': 86, 'dew_point': 11.73, 'uvi': 3.65, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 86, 'wind_gust': 1.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644350400, 'temp': 14.03, 'feels_like': 13.79, 'pressure': 1014, 'humidity': 88, 'dew_point': 12.08, 'uvi': 2.13, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 112, 'wind_gust': 1.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644354000, 'temp': 15.03, 'feels_like': 14.89, 'pressure': 1014, 'humidity': 88, 'dew_point': 13.06, 'uvi': 0.87, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 139, 'wind_gust': 1.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644357600, 'temp': 15.03, 'feels_like': 14.83, 'pressure': 1015, 'humidity': 86, 'dew_point': 12.71, 'uvi': 0.14, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 139, 'wind_gust': 1.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644361200, 'temp': 14.03, 'feels_like': 13.89, 'pressure': 1016, 'humidity': 92, 'dew_point': 12.75, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 158, 'wind_gust': 1.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 00:00:00 | 100.000000 | 11.760000 | 12.790000 | 92.000000 | 1016.000000 |  | 13.030000 | 0.000000 | 7467.000000 | 126.000000 | 1.7 | 0.930000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 01:00:00 | 100.000000 | 11.760000 | 12.790000 | 92.000000 | 1017.000000 |  | 13.030000 | 0.000000 | 10000.000000 | 126.000000 | 2.01 | 1.330000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 02:00:00 | 100.000000 | 10.770000 | 11.690000 | 92.000000 | 1018.000000 | 0.42 | 12.030000 | 0.000000 | 7601.000000 | 121.000000 | 2.41 | 1.580000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 03:00:00 | 100.000000 | 10.930000 | 11.720000 | 93.000000 | 1019.000000 | 0.49 | 12.030000 | 0.000000 | 6649.000000 | 115.000000 | 2.61 | 1.750000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 04:00:00 | 100.000000 | 10.930000 | 11.720000 | 93.000000 | 1019.000000 | 0.65 | 12.030000 | 0.000000 | 2803.000000 | 128.000000 | 2 | 1.360000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 05:00:00 | 100.000000 | 10.930000 | 11.720000 | 93.000000 | 1018.000000 | 1.15 | 12.030000 | 0.000000 | 7959.000000 | 141.000000 | 1.25 | 0.700000 | 501 | Rain | moderate rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 06:00:00 | 100.000000 | 10.100000 | 10.640000 | 94.000000 | 1018.000000 | 1.54 | 11.030000 | 0.000000 | 9339.000000 | 142.000000 | 0.81 | 0.290000 | 501 | Rain | moderate rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 07:00:00 | 100.000000 | 10.930000 | 11.720000 | 93.000000 | 1017.000000 | 1 | 12.030000 | 0.000000 | 10000.000000 | 118.000000 | 0.9 | 0.470000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 08:00:00 | 100.000000 | 10.770000 | 11.690000 | 92.000000 | 1016.000000 | 0.56 | 12.030000 | 0.000000 | 10000.000000 | 149.000000 | 0.75 | 0.170000 | 500 | Rain | light rain | 10n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 09:00:00 | 100.000000 | 10.770000 | 11.690000 | 92.000000 | 1016.000000 |  | 12.030000 | 0.000000 | 10000.000000 | 200.000000 | 0.65 | 0.210000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 10:00:00 | 100.000000 | 10.610000 | 11.660000 | 91.000000 | 1016.000000 |  | 12.030000 | 0.000000 | 10000.000000 | 136.000000 | 0.61 | 0.500000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 11:00:00 | 100.000000 | 9.620000 | 10.560000 | 91.000000 | 1017.000000 |  | 11.030000 | 0.000000 | 10000.000000 | 135.000000 | 0.9 | 0.680000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 12:00:00 | 100.000000 | 9.450000 | 10.540000 | 90.000000 | 1018.000000 |  | 11.030000 | 0.280000 | 10000.000000 | 135.000000 | 0.98 | 0.610000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 13:00:00 | 100.000000 | 11.260000 | 12.710000 | 89.000000 | 1018.000000 |  | 13.030000 | 1.360000 | 10000.000000 | 121.000000 | 1.28 | 0.660000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 14:00:00 | 100.000000 | 10.210000 | 12.560000 | 83.000000 | 1018.000000 |  | 13.030000 | 3.220000 | 10000.000000 | 153.000000 | 1.77 | 0.790000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 15:00:00 | 100.000000 | 9.670000 | 13.450000 | 75.000000 | 1017.000000 | 9.99 | 14.030000 | 5.420000 | 10000.000000 | 157.000000 | 1.97 | 0.650000 | 502 | Rain | heavy intensity rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 16:00:00 | 100.000000 | 7.740000 | 11.250000 | 75.000000 | 1016.000000 | 2.37 | 12.030000 | 9.180000 | 10000.000000 | 178.000000 | 2.28 | 0.590000 | 501 | Rain | moderate rain | 10d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 17:00:00 | 100.000000 | 8.080000 | 10.330000 | 82.000000 | 1016.000000 |  | 11.030000 | 9.990000 | 9975.000000 | 165.000000 | 1.83 | 0.700000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 18:00:00 | 97.000000 | 10.570000 | 12.610000 | 85.000000 | 1015.000000 |  | 13.030000 | 9.070000 | 10000.000000 | 126.000000 | 1.55 | 0.530000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 19:00:00 | 100.000000 | 11.730000 | 13.730000 | 86.000000 | 1015.000000 |  | 14.030000 | 3.650000 | 10000.000000 | 86.000000 | 1.52 | 0.450000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 20:00:00 | 100.000000 | 12.080000 | 13.790000 | 88.000000 | 1014.000000 |  | 14.030000 | 2.130000 | 10000.000000 | 112.000000 | 1.38 | 0.410000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 21:00:00 | 100.000000 | 13.060000 | 14.890000 | 88.000000 | 1014.000000 |  | 15.030000 | 0.870000 | 10000.000000 | 139.000000 | 1.39 | 0.680000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 22:00:00 | 100.000000 | 12.710000 | 14.830000 | 86.000000 | 1015.000000 |  | 15.030000 | 0.140000 | 10000.000000 | 139.000000 | 1.66 | 0.730000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206640 | "SAN JOSE [21206640]" | 4.501556 | -74.119306 | 2700.000000 | Climática Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2011-05-10 00:00:00 | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 23:00:00 | 100.000000 | 12.750000 | 13.890000 | 92.000000 | 1016.000000 |  | 14.030000 | 0.000000 | 10000.000000 | 158.000000 | 1.32 | 0.500000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21206640_OWM_Clouds_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Clouds_20220210.png)
![CNE_IDEAM_Station21206640_OWM_Dewpoint_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Dewpoint_20220210.png)
![CNE_IDEAM_Station21206640_OWM_Feelslike_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Feelslike_20220210.png)
![CNE_IDEAM_Station21206640_OWM_Humidity_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Humidity_20220210.png)
![CNE_IDEAM_Station21206640_OWM_Pressure_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Pressure_20220210.png)
![CNE_IDEAM_Station21206640_OWM_Rain_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Rain_20220210.png)
![CNE_IDEAM_Station21206640_OWM_Temp_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Temp_20220210.png)
![CNE_IDEAM_Station21206640_OWM_UVI_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_UVI_20220210.png)
![CNE_IDEAM_Station21206640_OWM_Visibility_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Visibility_20220210.png)
![CNE_IDEAM_Station21206640_OWM_Winddeg_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Winddeg_20220210.png)
![CNE_IDEAM_Station21206640_OWM_Windgust_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Windgust_20220210.png)
![CNE_IDEAM_Station21206640_OWM_Windspeed_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206640_OWM_Windspeed_20220210.png)

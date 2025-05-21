
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - NAZARETH [35020310] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35020310_OWM_20220210.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220210.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.17225,-74.146) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.17225&lon=-74.146)

| Parameter | Value |
|---|---|
| Code | 35020310 |
| Name | NAZARETH [35020310] |
| Latitude, ° | 4.17225 |
| Longitude, ° | -74.146 |
| Elevation, m | 2800 |
| Category | Pluviográfica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1984-07-15 00:00:00 |
| Suspension date | NaT |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Ceibas |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Río Guayuriba |

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

### (CNE index 1854) Open Weather values for station 35020310 - NAZARETH [35020310]

JSON data from API OWM:

```
{'lat': 4.1723, 'lon': -74.146, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644329284, 'sunrise': 1644318710, 'sunset': 1644361788, 'temp': 13.9, 'feels_like': 13.67, 'pressure': 1019, 'humidity': 89, 'dew_point': 12.12, 'uvi': 3.32, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 97, 'wind_gust': 1.52, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.65}}, 'hourly': [{'dt': 1644278400, 'temp': 13.9, 'feels_like': 13.83, 'pressure': 1017, 'humidity': 95, 'dew_point': 13.11, 'uvi': 0, 'clouds': 100, 'visibility': 6523, 'wind_speed': 1.22, 'wind_deg': 123, 'wind_gust': 2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644282000, 'temp': 13.9, 'feels_like': 13.83, 'pressure': 1018, 'humidity': 95, 'dew_point': 13.11, 'uvi': 0, 'clouds': 100, 'visibility': 5919, 'wind_speed': 1.36, 'wind_deg': 113, 'wind_gust': 2.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644285600, 'temp': 12.9, 'feels_like': 12.73, 'pressure': 1019, 'humidity': 95, 'dew_point': 12.12, 'uvi': 0, 'clouds': 100, 'visibility': 2571, 'wind_speed': 1.46, 'wind_deg': 99, 'wind_gust': 2.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644289200, 'temp': 12.9, 'feels_like': 12.73, 'pressure': 1020, 'humidity': 95, 'dew_point': 12.12, 'uvi': 0, 'clouds': 100, 'visibility': 546, 'wind_speed': 1.22, 'wind_deg': 95, 'wind_gust': 2.02, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 2.73}}, {'dt': 1644292800, 'temp': 12.9, 'feels_like': 12.73, 'pressure': 1019, 'humidity': 95, 'dew_point': 12.12, 'uvi': 0, 'clouds': 100, 'visibility': 2360, 'wind_speed': 0.51, 'wind_deg': 108, 'wind_gust': 1.39, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.86}}, {'dt': 1644296400, 'temp': 12.9, 'feels_like': 12.73, 'pressure': 1019, 'humidity': 95, 'dew_point': 12.12, 'uvi': 0, 'clouds': 100, 'visibility': 8644, 'wind_speed': 0.06, 'wind_deg': 95, 'wind_gust': 1.03, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 2.73}}, {'dt': 1644300000, 'temp': 11.9, 'feels_like': 11.65, 'pressure': 1018, 'humidity': 96, 'dew_point': 11.28, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 286, 'wind_gust': 0.93, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.33}}, {'dt': 1644303600, 'temp': 12.9, 'feels_like': 12.7, 'pressure': 1017, 'humidity': 94, 'dew_point': 11.96, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.15, 'wind_deg': 296, 'wind_gust': 0.97, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.78}}, {'dt': 1644307200, 'temp': 12.9, 'feels_like': 12.7, 'pressure': 1017, 'humidity': 94, 'dew_point': 11.96, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.29, 'wind_deg': 254, 'wind_gust': 0.87, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.78}}, {'dt': 1644310800, 'temp': 12.9, 'feels_like': 12.67, 'pressure': 1017, 'humidity': 93, 'dew_point': 11.8, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 192, 'wind_gust': 0.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644314400, 'temp': 12.9, 'feels_like': 12.67, 'pressure': 1017, 'humidity': 93, 'dew_point': 11.8, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 125, 'wind_gust': 0.93, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644318000, 'temp': 11.9, 'feels_like': 11.6, 'pressure': 1018, 'humidity': 94, 'dew_point': 10.97, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 112, 'wind_gust': 1.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644321600, 'temp': 11.9, 'feels_like': 11.57, 'pressure': 1018, 'humidity': 93, 'dew_point': 10.81, 'uvi': 0.07, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 111, 'wind_gust': 1.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644325200, 'temp': 13.9, 'feels_like': 13.72, 'pressure': 1019, 'humidity': 91, 'dew_point': 12.46, 'uvi': 1.41, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 98, 'wind_gust': 1.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644328800, 'temp': 13.9, 'feels_like': 13.67, 'pressure': 1019, 'humidity': 89, 'dew_point': 12.12, 'uvi': 3.32, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 97, 'wind_gust': 1.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644332400, 'temp': 14.9, 'feels_like': 14.72, 'pressure': 1019, 'humidity': 87, 'dew_point': 12.76, 'uvi': 5.57, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 97, 'wind_gust': 1.65, 'weather': [{'id': 503, 'main': 'Rain', 'description': 'very heavy rain', 'icon': '10d'}], 'rain': {'1h': 27.34}}, {'dt': 1644336000, 'temp': 12.9, 'feels_like': 12.62, 'pressure': 1018, 'humidity': 91, 'dew_point': 11.47, 'uvi': 5.67, 'clouds': 97, 'visibility': 8625, 'wind_speed': 0.52, 'wind_deg': 119, 'wind_gust': 1.52, 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'}], 'rain': {'1h': 11.53}}, {'dt': 1644339600, 'temp': 11.9, 'feels_like': 11.55, 'pressure': 1017, 'humidity': 92, 'dew_point': 10.64, 'uvi': 6.17, 'clouds': 97, 'visibility': 7217, 'wind_speed': 0.72, 'wind_deg': 94, 'wind_gust': 1.59, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.73}}, {'dt': 1644343200, 'temp': 13.9, 'feels_like': 13.75, 'pressure': 1016, 'humidity': 92, 'dew_point': 12.62, 'uvi': 5.61, 'clouds': 100, 'visibility': 4040, 'wind_speed': 0.44, 'wind_deg': 76, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644346800, 'temp': 14.9, 'feels_like': 14.9, 'pressure': 1016, 'humidity': 94, 'dew_point': 13.94, 'uvi': 5.44, 'clouds': 100, 'visibility': 3818, 'wind_speed': 0.31, 'wind_deg': 90, 'wind_gust': 1.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644350400, 'temp': 14.9, 'feels_like': 14.93, 'pressure': 1015, 'humidity': 95, 'dew_point': 14.11, 'uvi': 3.18, 'clouds': 100, 'visibility': 1258, 'wind_speed': 0.25, 'wind_deg': 74, 'wind_gust': 1.13, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644354000, 'temp': 15.9, 'feels_like': 16.05, 'pressure': 1015, 'humidity': 96, 'dew_point': 15.26, 'uvi': 1.31, 'clouds': 100, 'visibility': 4276, 'wind_speed': 0.43, 'wind_deg': 78, 'wind_gust': 1.26, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644357600, 'temp': 15.9, 'feels_like': 16.03, 'pressure': 1016, 'humidity': 95, 'dew_point': 15.1, 'uvi': 0.5, 'clouds': 100, 'visibility': 6828, 'wind_speed': 0.7, 'wind_deg': 99, 'wind_gust': 1.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644361200, 'temp': 14.9, 'feels_like': 14.98, 'pressure': 1017, 'humidity': 97, 'dew_point': 14.43, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 111, 'wind_gust': 1.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 00:00:00 | 100.000000 | 13.110000 | 13.830000 | 95.000000 | 1017.000000 |  | 13.900000 | 0.000000 | 6523.000000 | 123.000000 | 2 | 1.220000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 01:00:00 | 100.000000 | 13.110000 | 13.830000 | 95.000000 | 1018.000000 |  | 13.900000 | 0.000000 | 5919.000000 | 113.000000 | 2.11 | 1.360000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 02:00:00 | 100.000000 | 12.120000 | 12.730000 | 95.000000 | 1019.000000 |  | 12.900000 | 0.000000 | 2571.000000 | 99.000000 | 2.29 | 1.460000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 03:00:00 | 100.000000 | 12.120000 | 12.730000 | 95.000000 | 1020.000000 | 2.73 | 12.900000 | 0.000000 | 546.000000 | 95.000000 | 2.02 | 1.220000 | 501 | Rain | moderate rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 04:00:00 | 100.000000 | 12.120000 | 12.730000 | 95.000000 | 1019.000000 | 0.86 | 12.900000 | 0.000000 | 2360.000000 | 108.000000 | 1.39 | 0.510000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 05:00:00 | 100.000000 | 12.120000 | 12.730000 | 95.000000 | 1019.000000 | 2.73 | 12.900000 | 0.000000 | 8644.000000 | 95.000000 | 1.03 | 0.060000 | 501 | Rain | moderate rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 06:00:00 | 100.000000 | 11.280000 | 11.650000 | 96.000000 | 1018.000000 | 1.33 | 11.900000 | 0.000000 | 10000.000000 | 286.000000 | 0.93 | 0.200000 | 501 | Rain | moderate rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 07:00:00 | 100.000000 | 11.960000 | 12.700000 | 94.000000 | 1017.000000 | 1.78 | 12.900000 | 0.000000 | 10000.000000 | 296.000000 | 0.97 | 0.150000 | 501 | Rain | moderate rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 08:00:00 | 100.000000 | 11.960000 | 12.700000 | 94.000000 | 1017.000000 | 1.78 | 12.900000 | 0.000000 | 10000.000000 | 254.000000 | 0.87 | 0.290000 | 501 | Rain | moderate rain | 10n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 09:00:00 | 100.000000 | 11.800000 | 12.670000 | 93.000000 | 1017.000000 |  | 12.900000 | 0.000000 | 10000.000000 | 192.000000 | 0.82 | 0.170000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 10:00:00 | 100.000000 | 11.800000 | 12.670000 | 93.000000 | 1017.000000 |  | 12.900000 | 0.000000 | 10000.000000 | 125.000000 | 0.93 | 0.510000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 11:00:00 | 100.000000 | 10.970000 | 11.600000 | 94.000000 | 1018.000000 |  | 11.900000 | 0.000000 | 10000.000000 | 112.000000 | 1.04 | 0.590000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 12:00:00 | 98.000000 | 10.810000 | 11.570000 | 93.000000 | 1018.000000 |  | 11.900000 | 0.070000 | 10000.000000 | 111.000000 | 1.36 | 0.790000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 13:00:00 | 99.000000 | 12.460000 | 13.720000 | 91.000000 | 1019.000000 |  | 13.900000 | 1.410000 | 10000.000000 | 98.000000 | 1.77 | 0.920000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 14:00:00 | 95.000000 | 12.120000 | 13.670000 | 89.000000 | 1019.000000 |  | 13.900000 | 3.320000 | 10000.000000 | 97.000000 | 1.52 | 0.520000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 15:00:00 | 96.000000 | 12.760000 | 14.720000 | 87.000000 | 1019.000000 | 27.34 | 14.900000 | 5.570000 | 10000.000000 | 97.000000 | 1.65 | 0.560000 | 503 | Rain | very heavy rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 16:00:00 | 97.000000 | 11.470000 | 12.620000 | 91.000000 | 1018.000000 | 11.53 | 12.900000 | 5.670000 | 8625.000000 | 119.000000 | 1.52 | 0.520000 | 502 | Rain | heavy intensity rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 17:00:00 | 97.000000 | 10.640000 | 11.550000 | 92.000000 | 1017.000000 | 2.73 | 11.900000 | 6.170000 | 7217.000000 | 94.000000 | 1.59 | 0.720000 | 501 | Rain | moderate rain | 10d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 18:00:00 | 100.000000 | 12.620000 | 13.750000 | 92.000000 | 1016.000000 |  | 13.900000 | 5.610000 | 4040.000000 | 76.000000 | 1.18 | 0.440000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 19:00:00 | 100.000000 | 13.940000 | 14.900000 | 94.000000 | 1016.000000 |  | 14.900000 | 5.440000 | 3818.000000 | 90.000000 | 1.03 | 0.310000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 20:00:00 | 100.000000 | 14.110000 | 14.930000 | 95.000000 | 1015.000000 |  | 14.900000 | 3.180000 | 1258.000000 | 74.000000 | 1.13 | 0.250000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 21:00:00 | 100.000000 | 15.260000 | 16.050000 | 96.000000 | 1015.000000 |  | 15.900000 | 1.310000 | 4276.000000 | 78.000000 | 1.26 | 0.430000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 22:00:00 | 100.000000 | 15.100000 | 16.030000 | 95.000000 | 1016.000000 |  | 15.900000 | 0.500000 | 6828.000000 | 99.000000 | 1.46 | 0.700000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 23:00:00 | 100.000000 | 14.430000 | 14.980000 | 97.000000 | 1017.000000 |  | 14.900000 | 0.000000 | 10000.000000 | 111.000000 | 1.09 | 0.410000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35020310_OWM_Clouds_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Clouds_20220210.png)
![CNE_IDEAM_Station35020310_OWM_Dewpoint_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Dewpoint_20220210.png)
![CNE_IDEAM_Station35020310_OWM_Feelslike_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Feelslike_20220210.png)
![CNE_IDEAM_Station35020310_OWM_Humidity_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Humidity_20220210.png)
![CNE_IDEAM_Station35020310_OWM_Pressure_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Pressure_20220210.png)
![CNE_IDEAM_Station35020310_OWM_Rain_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Rain_20220210.png)
![CNE_IDEAM_Station35020310_OWM_Temp_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Temp_20220210.png)
![CNE_IDEAM_Station35020310_OWM_UVI_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_UVI_20220210.png)
![CNE_IDEAM_Station35020310_OWM_Visibility_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Visibility_20220210.png)
![CNE_IDEAM_Station35020310_OWM_Winddeg_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Winddeg_20220210.png)
![CNE_IDEAM_Station35020310_OWM_Windgust_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Windgust_20220210.png)
![CNE_IDEAM_Station35020310_OWM_Windspeed_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Windspeed_20220210.png)

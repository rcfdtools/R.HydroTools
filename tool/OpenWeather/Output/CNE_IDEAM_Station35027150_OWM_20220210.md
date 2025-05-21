
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ANIMAS LAS [35027150] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35027150_OWM_20220210.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220210.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.13797222,-74.17380556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.13797222&lon=-74.17380556)

| Parameter | Value |
|---|---|
| Code | 35027150 |
| Name | ANIMAS LAS [35027150] |
| Latitude, ° | 4.13797222 |
| Longitude, ° | -74.17380556 |
| Elevation, m | 2840 |
| Category | Limnigráfica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1985-01-15 00:00:00 |
| Suspension date | NaT |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Chochal |
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

### (CNE index 1622) Open Weather values for station 35027150 - ANIMAS LAS [35027150]

JSON data from API OWM:

```
{'lat': 4.138, 'lon': -74.1738, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644329284, 'sunrise': 1644318714, 'sunset': 1644361797, 'temp': 11.46, 'feels_like': 10.96, 'pressure': 1019, 'humidity': 88, 'dew_point': 9.54, 'uvi': 3.32, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 99, 'wind_gust': 1.6, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, 'hourly': [{'dt': 1644278400, 'temp': 11.46, 'feels_like': 11.14, 'pressure': 1017, 'humidity': 95, 'dew_point': 10.69, 'uvi': 0, 'clouds': 100, 'visibility': 7444, 'wind_speed': 1.41, 'wind_deg': 119, 'wind_gust': 2.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644282000, 'temp': 11.46, 'feels_like': 11.12, 'pressure': 1018, 'humidity': 94, 'dew_point': 10.53, 'uvi': 0, 'clouds': 100, 'visibility': 7703, 'wind_speed': 1.46, 'wind_deg': 113, 'wind_gust': 2.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644285600, 'temp': 10.46, 'feels_like': 10.04, 'pressure': 1019, 'humidity': 95, 'dew_point': 9.69, 'uvi': 0, 'clouds': 100, 'visibility': 3740, 'wind_speed': 1.56, 'wind_deg': 100, 'wind_gust': 2.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644289200, 'temp': 10.46, 'feels_like': 10.04, 'pressure': 1020, 'humidity': 95, 'dew_point': 9.69, 'uvi': 0, 'clouds': 100, 'visibility': 456, 'wind_speed': 1.35, 'wind_deg': 97, 'wind_gust': 2.13, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 2.37}}, {'dt': 1644292800, 'temp': 10.46, 'feels_like': 10.02, 'pressure': 1019, 'humidity': 94, 'dew_point': 9.54, 'uvi': 0, 'clouds': 100, 'visibility': 3469, 'wind_speed': 0.74, 'wind_deg': 110, 'wind_gust': 1.48, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.86}}, {'dt': 1644296400, 'temp': 10.46, 'feels_like': 10.04, 'pressure': 1019, 'humidity': 95, 'dew_point': 9.69, 'uvi': 0, 'clouds': 100, 'visibility': 9174, 'wind_speed': 0.26, 'wind_deg': 96, 'wind_gust': 1.01, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 3.16}}, {'dt': 1644300000, 'temp': 9.46, 'feels_like': 9.46, 'pressure': 1018, 'humidity': 96, 'dew_point': 8.85, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.08, 'wind_deg': 346, 'wind_gust': 0.84, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.54}}, {'dt': 1644303600, 'temp': 10.46, 'feels_like': 10.02, 'pressure': 1018, 'humidity': 94, 'dew_point': 9.54, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.14, 'wind_deg': 45, 'wind_gust': 0.92, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 2.05}}, {'dt': 1644307200, 'temp': 10.46, 'feels_like': 10.02, 'pressure': 1017, 'humidity': 94, 'dew_point': 9.54, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.07, 'wind_deg': 184, 'wind_gust': 0.87, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.54}}, {'dt': 1644310800, 'temp': 10.46, 'feels_like': 9.99, 'pressure': 1017, 'humidity': 93, 'dew_point': 9.38, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.29, 'wind_deg': 127, 'wind_gust': 0.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644314400, 'temp': 10.46, 'feels_like': 10.02, 'pressure': 1017, 'humidity': 94, 'dew_point': 9.54, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 115, 'wind_gust': 1.02, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644318000, 'temp': 9.46, 'feels_like': 9.46, 'pressure': 1018, 'humidity': 94, 'dew_point': 8.54, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 108, 'wind_gust': 1.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644321600, 'temp': 9.46, 'feels_like': 9.46, 'pressure': 1018, 'humidity': 93, 'dew_point': 8.39, 'uvi': 0.07, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 108, 'wind_gust': 1.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644325200, 'temp': 11.46, 'feels_like': 11.01, 'pressure': 1019, 'humidity': 90, 'dew_point': 9.88, 'uvi': 1.41, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 99, 'wind_gust': 1.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644328800, 'temp': 11.46, 'feels_like': 10.96, 'pressure': 1019, 'humidity': 88, 'dew_point': 9.54, 'uvi': 3.32, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 99, 'wind_gust': 1.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644332400, 'temp': 12.46, 'feels_like': 12.03, 'pressure': 1019, 'humidity': 87, 'dew_point': 10.36, 'uvi': 5.57, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 98, 'wind_gust': 1.7, 'weather': [{'id': 503, 'main': 'Rain', 'description': 'very heavy rain', 'icon': '10d'}], 'rain': {'1h': 27.34}}, {'dt': 1644336000, 'temp': 10.46, 'feels_like': 9.91, 'pressure': 1018, 'humidity': 90, 'dew_point': 8.89, 'uvi': 5.67, 'clouds': 97, 'visibility': 7584, 'wind_speed': 0.53, 'wind_deg': 119, 'wind_gust': 1.48, 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'}], 'rain': {'1h': 13.32}}, {'dt': 1644339600, 'temp': 9.46, 'feels_like': 9.46, 'pressure': 1017, 'humidity': 91, 'dew_point': 8.07, 'uvi': 6.17, 'clouds': 97, 'visibility': 6739, 'wind_speed': 0.63, 'wind_deg': 97, 'wind_gust': 1.54, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.73}}, {'dt': 1644343200, 'temp': 11.46, 'feels_like': 11.04, 'pressure': 1017, 'humidity': 91, 'dew_point': 10.04, 'uvi': 5.61, 'clouds': 100, 'visibility': 4983, 'wind_speed': 0.36, 'wind_deg': 76, 'wind_gust': 1.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644346800, 'temp': 12.46, 'feels_like': 12.19, 'pressure': 1016, 'humidity': 93, 'dew_point': 11.36, 'uvi': 5.44, 'clouds': 100, 'visibility': 4991, 'wind_speed': 0.26, 'wind_deg': 95, 'wind_gust': 0.99, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644350400, 'temp': 12.46, 'feels_like': 12.24, 'pressure': 1015, 'humidity': 95, 'dew_point': 11.68, 'uvi': 3.18, 'clouds': 100, 'visibility': 1971, 'wind_speed': 0.26, 'wind_deg': 74, 'wind_gust': 1.13, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644354000, 'temp': 13.46, 'feels_like': 13.34, 'pressure': 1016, 'humidity': 95, 'dew_point': 12.68, 'uvi': 1.31, 'clouds': 100, 'visibility': 3915, 'wind_speed': 0.48, 'wind_deg': 74, 'wind_gust': 1.26, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644357600, 'temp': 13.46, 'feels_like': 13.34, 'pressure': 1016, 'humidity': 95, 'dew_point': 12.68, 'uvi': 0.5, 'clouds': 100, 'visibility': 6227, 'wind_speed': 0.73, 'wind_deg': 95, 'wind_gust': 1.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644361200, 'temp': 12.46, 'feels_like': 12.29, 'pressure': 1017, 'humidity': 97, 'dew_point': 12, 'uvi': 0, 'clouds': 100, 'visibility': 9304, 'wind_speed': 0.49, 'wind_deg': 110, 'wind_gust': 1.13, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 00:00:00 | 100.000000 | 10.690000 | 11.140000 | 95.000000 | 1017.000000 |  | 11.460000 | 0.000000 | 7444.000000 | 119.000000 | 2.11 | 1.410000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 01:00:00 | 100.000000 | 10.530000 | 11.120000 | 94.000000 | 1018.000000 |  | 11.460000 | 0.000000 | 7703.000000 | 113.000000 | 2.12 | 1.460000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 02:00:00 | 100.000000 | 9.690000 | 10.040000 | 95.000000 | 1019.000000 |  | 10.460000 | 0.000000 | 3740.000000 | 100.000000 | 2.3 | 1.560000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 03:00:00 | 100.000000 | 9.690000 | 10.040000 | 95.000000 | 1020.000000 | 2.37 | 10.460000 | 0.000000 | 456.000000 | 97.000000 | 2.13 | 1.350000 | 501 | Rain | moderate rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 04:00:00 | 100.000000 | 9.540000 | 10.020000 | 94.000000 | 1019.000000 | 0.86 | 10.460000 | 0.000000 | 3469.000000 | 110.000000 | 1.48 | 0.740000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 05:00:00 | 100.000000 | 9.690000 | 10.040000 | 95.000000 | 1019.000000 | 3.16 | 10.460000 | 0.000000 | 9174.000000 | 96.000000 | 1.01 | 0.260000 | 501 | Rain | moderate rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 06:00:00 | 100.000000 | 8.850000 | 9.460000 | 96.000000 | 1018.000000 | 1.54 | 9.460000 | 0.000000 | 10000.000000 | 346.000000 | 0.84 | 0.080000 | 501 | Rain | moderate rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 07:00:00 | 100.000000 | 9.540000 | 10.020000 | 94.000000 | 1018.000000 | 2.05 | 10.460000 | 0.000000 | 10000.000000 | 45.000000 | 0.92 | 0.140000 | 501 | Rain | moderate rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 08:00:00 | 100.000000 | 9.540000 | 10.020000 | 94.000000 | 1017.000000 | 1.54 | 10.460000 | 0.000000 | 10000.000000 | 184.000000 | 0.87 | 0.070000 | 501 | Rain | moderate rain | 10n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 09:00:00 | 100.000000 | 9.380000 | 9.990000 | 93.000000 | 1017.000000 |  | 10.460000 | 0.000000 | 10000.000000 | 127.000000 | 0.86 | 0.290000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 10:00:00 | 100.000000 | 9.540000 | 10.020000 | 94.000000 | 1017.000000 |  | 10.460000 | 0.000000 | 10000.000000 | 115.000000 | 1.02 | 0.720000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 11:00:00 | 100.000000 | 8.540000 | 9.460000 | 94.000000 | 1018.000000 |  | 9.460000 | 0.000000 | 10000.000000 | 108.000000 | 1.14 | 0.860000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 12:00:00 | 96.000000 | 8.390000 | 9.460000 | 93.000000 | 1018.000000 |  | 9.460000 | 0.070000 | 10000.000000 | 108.000000 | 1.49 | 0.980000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 13:00:00 | 98.000000 | 9.880000 | 11.010000 | 90.000000 | 1019.000000 |  | 11.460000 | 1.410000 | 10000.000000 | 99.000000 | 1.85 | 1.000000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 14:00:00 | 94.000000 | 9.540000 | 10.960000 | 88.000000 | 1019.000000 |  | 11.460000 | 3.320000 | 10000.000000 | 99.000000 | 1.6 | 0.540000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 15:00:00 | 95.000000 | 10.360000 | 12.030000 | 87.000000 | 1019.000000 | 27.34 | 12.460000 | 5.570000 | 10000.000000 | 98.000000 | 1.7 | 0.590000 | 503 | Rain | very heavy rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 16:00:00 | 97.000000 | 8.890000 | 9.910000 | 90.000000 | 1018.000000 | 13.32 | 10.460000 | 5.670000 | 7584.000000 | 119.000000 | 1.48 | 0.530000 | 502 | Rain | heavy intensity rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 17:00:00 | 97.000000 | 8.070000 | 9.460000 | 91.000000 | 1017.000000 | 2.73 | 9.460000 | 6.170000 | 6739.000000 | 97.000000 | 1.54 | 0.630000 | 501 | Rain | moderate rain | 10d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 18:00:00 | 100.000000 | 10.040000 | 11.040000 | 91.000000 | 1017.000000 |  | 11.460000 | 5.610000 | 4983.000000 | 76.000000 | 1.12 | 0.360000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 19:00:00 | 100.000000 | 11.360000 | 12.190000 | 93.000000 | 1016.000000 |  | 12.460000 | 5.440000 | 4991.000000 | 95.000000 | 0.99 | 0.260000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 20:00:00 | 100.000000 | 11.680000 | 12.240000 | 95.000000 | 1015.000000 |  | 12.460000 | 3.180000 | 1971.000000 | 74.000000 | 1.13 | 0.260000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 21:00:00 | 100.000000 | 12.680000 | 13.340000 | 95.000000 | 1016.000000 |  | 13.460000 | 1.310000 | 3915.000000 | 74.000000 | 1.26 | 0.480000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 22:00:00 | 100.000000 | 12.680000 | 13.340000 | 95.000000 | 1016.000000 |  | 13.460000 | 0.500000 | 6227.000000 | 95.000000 | 1.5 | 0.730000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35027150 | "ANIMAS LAS [35027150]" | 4.137972 | -74.173806 | 2840.000000 | Limnigráfica | Convencional | Activa | 1985-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-08 23:00:00 | 100.000000 | 12.000000 | 12.290000 | 97.000000 | 1017.000000 |  | 12.460000 | 0.000000 | 9304.000000 | 110.000000 | 1.13 | 0.490000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35027150_OWM_Clouds_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Clouds_20220210.png)
![CNE_IDEAM_Station35027150_OWM_Dewpoint_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Dewpoint_20220210.png)
![CNE_IDEAM_Station35027150_OWM_Feelslike_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Feelslike_20220210.png)
![CNE_IDEAM_Station35027150_OWM_Humidity_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Humidity_20220210.png)
![CNE_IDEAM_Station35027150_OWM_Pressure_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Pressure_20220210.png)
![CNE_IDEAM_Station35027150_OWM_Rain_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Rain_20220210.png)
![CNE_IDEAM_Station35027150_OWM_Temp_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Temp_20220210.png)
![CNE_IDEAM_Station35027150_OWM_UVI_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_UVI_20220210.png)
![CNE_IDEAM_Station35027150_OWM_Visibility_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Visibility_20220210.png)
![CNE_IDEAM_Station35027150_OWM_Winddeg_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Winddeg_20220210.png)
![CNE_IDEAM_Station35027150_OWM_Windgust_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Windgust_20220210.png)
![CNE_IDEAM_Station35027150_OWM_Windspeed_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35027150_OWM_Windspeed_20220210.png)

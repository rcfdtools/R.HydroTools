
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

* Current date time: 2022-02-13 07:30:06.495901
* Unix time to eval: 1644564606
* Days before (for historical data): 2
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220213.xls
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35020310_OWM_20220213.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220213.csv)

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
{'lat': 4.1723, 'lon': -74.146, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644564606, 'sunrise': 1644577898, 'sunset': 1644621011, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1015, 'humidity': 96, 'dew_point': 9.29, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 281, 'wind_gust': 0.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, 'hourly': [{'dt': 1644537600, 'temp': 12.9, 'feels_like': 12.73, 'pressure': 1015, 'humidity': 95, 'dew_point': 12.12, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 67, 'wind_gust': 1.29, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644541200, 'temp': 11.9, 'feels_like': 11.57, 'pressure': 1016, 'humidity': 93, 'dew_point': 10.81, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 83, 'wind_gust': 1.08, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644544800, 'temp': 11.9, 'feels_like': 11.57, 'pressure': 1017, 'humidity': 93, 'dew_point': 10.81, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 92, 'wind_gust': 0.69, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644548400, 'temp': 11.9, 'feels_like': 11.6, 'pressure': 1017, 'humidity': 94, 'dew_point': 10.97, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 71, 'wind_gust': 0.66, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644552000, 'temp': 11.9, 'feels_like': 11.6, 'pressure': 1017, 'humidity': 94, 'dew_point': 10.97, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 39, 'wind_gust': 0.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644555600, 'temp': 10.9, 'feels_like': 10.5, 'pressure': 1016, 'humidity': 94, 'dew_point': 9.97, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 20, 'wind_gust': 0.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644559200, 'temp': 10.9, 'feels_like': 10.53, 'pressure': 1016, 'humidity': 95, 'dew_point': 10.13, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.11, 'wind_deg': 343, 'wind_gust': 0.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644562800, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1015, 'humidity': 95, 'dew_point': 9.14, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 271, 'wind_gust': 0.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644566400, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1015, 'humidity': 96, 'dew_point': 9.29, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 281, 'wind_gust': 0.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644570000, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1015, 'humidity': 96, 'dew_point': 9.29, 'uvi': 0, 'clouds': 100, 'visibility': 9350, 'wind_speed': 0.64, 'wind_deg': 296, 'wind_gust': 0.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644573600, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1015, 'humidity': 96, 'dew_point': 8.3, 'uvi': 0, 'clouds': 100, 'visibility': 9403, 'wind_speed': 0.59, 'wind_deg': 293, 'wind_gust': 0.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644577200, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1016, 'humidity': 95, 'dew_point': 8.14, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 288, 'wind_gust': 0.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644580800, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1017, 'humidity': 92, 'dew_point': 8.66, 'uvi': 0.44, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 347, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644584400, 'temp': 13.9, 'feels_like': 13.64, 'pressure': 1017, 'humidity': 88, 'dew_point': 11.95, 'uvi': 2.45, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 60, 'wind_gust': 1.15, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644588000, 'temp': 15.9, 'feels_like': 15.71, 'pressure': 1017, 'humidity': 83, 'dew_point': 13.02, 'uvi': 5.78, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 54, 'wind_gust': 1.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644591600, 'temp': 16.9, 'feels_like': 16.68, 'pressure': 1016, 'humidity': 78, 'dew_point': 13.04, 'uvi': 9.69, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 50, 'wind_gust': 1.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644595200, 'temp': 17.9, 'feels_like': 17.7, 'pressure': 1015, 'humidity': 75, 'dew_point': 13.41, 'uvi': 12.74, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 40, 'wind_gust': 2.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644598800, 'temp': 19.9, 'feels_like': 19.93, 'pressure': 1014, 'humidity': 76, 'dew_point': 15.55, 'uvi': 13.86, 'clouds': 85, 'visibility': 9621, 'wind_speed': 0.95, 'wind_deg': 39, 'wind_gust': 2.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644602400, 'temp': 18.9, 'feels_like': 18.91, 'pressure': 1013, 'humidity': 79, 'dew_point': 15.18, 'uvi': 12.6, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 37, 'wind_gust': 2.34, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644606000, 'temp': 19.9, 'feels_like': 20.17, 'pressure': 1012, 'humidity': 85, 'dew_point': 17.3, 'uvi': 8.92, 'clouds': 93, 'visibility': 5656, 'wind_speed': 0.53, 'wind_deg': 44, 'wind_gust': 2.19, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644609600, 'temp': 19.9, 'feels_like': 20.4, 'pressure': 1012, 'humidity': 94, 'dew_point': 18.91, 'uvi': 5.22, 'clouds': 97, 'visibility': 3011, 'wind_speed': 0.19, 'wind_deg': 19, 'wind_gust': 1.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644613200, 'temp': 16.9, 'feels_like': 17.15, 'pressure': 1012, 'humidity': 96, 'dew_point': 16.26, 'uvi': 2.15, 'clouds': 98, 'visibility': 556, 'wind_speed': 0.17, 'wind_deg': 14, 'wind_gust': 1.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644616800, 'temp': 16.9, 'feels_like': 17.18, 'pressure': 1013, 'humidity': 97, 'dew_point': 16.42, 'uvi': 0.5, 'clouds': 98, 'visibility': 137, 'wind_speed': 0.34, 'wind_deg': 63, 'wind_gust': 1.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644620400, 'temp': 15.9, 'feels_like': 16.13, 'pressure': 1014, 'humidity': 99, 'dew_point': 15.74, 'uvi': 0, 'clouds': 98, 'visibility': 132, 'wind_speed': 0.56, 'wind_deg': 73, 'wind_gust': 1.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 00:00:00 | 71.000000 | 12.120000 | 12.730000 | 95.000000 | 1015.000000 |  | 12.900000 | 0.000000 | 10000.000000 | 67.000000 | 1.29 | 0.920000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 01:00:00 | 83.000000 | 10.810000 | 11.570000 | 93.000000 | 1016.000000 |  | 11.900000 | 0.000000 | 10000.000000 | 83.000000 | 1.08 | 0.720000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 02:00:00 | 83.000000 | 10.810000 | 11.570000 | 93.000000 | 1017.000000 |  | 11.900000 | 0.000000 | 10000.000000 | 92.000000 | 0.69 | 0.370000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 03:00:00 | 79.000000 | 10.970000 | 11.600000 | 94.000000 | 1017.000000 |  | 11.900000 | 0.000000 | 10000.000000 | 71.000000 | 0.66 | 0.320000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 04:00:00 | 83.000000 | 10.970000 | 11.600000 | 94.000000 | 1017.000000 |  | 11.900000 | 0.000000 | 10000.000000 | 39.000000 | 0.76 | 0.380000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 05:00:00 | 86.000000 | 9.970000 | 10.500000 | 94.000000 | 1016.000000 |  | 10.900000 | 0.000000 | 10000.000000 | 20.000000 | 0.7 | 0.300000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 06:00:00 | 98.000000 | 10.130000 | 10.530000 | 95.000000 | 1016.000000 |  | 10.900000 | 0.000000 | 10000.000000 | 343.000000 | 0.61 | 0.110000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 07:00:00 | 100.000000 | 9.140000 | 9.900000 | 95.000000 | 1015.000000 |  | 9.900000 | 0.000000 | 10000.000000 | 271.000000 | 0.68 | 0.240000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 08:00:00 | 100.000000 | 9.290000 | 9.900000 | 96.000000 | 1015.000000 |  | 9.900000 | 0.000000 | 10000.000000 | 281.000000 | 0.76 | 0.580000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 09:00:00 | 100.000000 | 9.290000 | 9.900000 | 96.000000 | 1015.000000 |  | 9.900000 | 0.000000 | 9350.000000 | 296.000000 | 0.97 | 0.640000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 10:00:00 | 100.000000 | 8.300000 | 8.900000 | 96.000000 | 1015.000000 |  | 8.900000 | 0.000000 | 9403.000000 | 293.000000 | 0.92 | 0.590000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 11:00:00 | 99.000000 | 8.140000 | 8.900000 | 95.000000 | 1016.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 288.000000 | 0.81 | 0.590000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 12:00:00 | 95.000000 | 8.660000 | 9.900000 | 92.000000 | 1017.000000 |  | 9.900000 | 0.440000 | 10000.000000 | 347.000000 | 0.88 | 0.370000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 13:00:00 | 100.000000 | 11.950000 | 13.640000 | 88.000000 | 1017.000000 |  | 13.900000 | 2.450000 | 10000.000000 | 60.000000 | 1.15 | 0.710000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 14:00:00 | 96.000000 | 13.020000 | 15.710000 | 83.000000 | 1017.000000 |  | 15.900000 | 5.780000 | 10000.000000 | 54.000000 | 1.4 | 0.820000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 15:00:00 | 89.000000 | 13.040000 | 16.680000 | 78.000000 | 1016.000000 |  | 16.900000 | 9.690000 | 10000.000000 | 50.000000 | 1.82 | 0.920000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 16:00:00 | 87.000000 | 13.410000 | 17.700000 | 75.000000 | 1015.000000 |  | 17.900000 | 12.740000 | 10000.000000 | 40.000000 | 2.09 | 0.920000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 17:00:00 | 85.000000 | 15.550000 | 19.930000 | 76.000000 | 1014.000000 |  | 19.900000 | 13.860000 | 9621.000000 | 39.000000 | 2.44 | 0.950000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 18:00:00 | 81.000000 | 15.180000 | 18.910000 | 79.000000 | 1013.000000 |  | 18.900000 | 12.600000 | 10000.000000 | 37.000000 | 2.34 | 0.710000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 19:00:00 | 93.000000 | 17.300000 | 20.170000 | 85.000000 | 1012.000000 |  | 19.900000 | 8.920000 | 5656.000000 | 44.000000 | 2.19 | 0.530000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 20:00:00 | 97.000000 | 18.910000 | 20.400000 | 94.000000 | 1012.000000 |  | 19.900000 | 5.220000 | 3011.000000 | 19.000000 | 1.88 | 0.190000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 21:00:00 | 98.000000 | 16.260000 | 17.150000 | 96.000000 | 1012.000000 |  | 16.900000 | 2.150000 | 556.000000 | 14.000000 | 1.69 | 0.170000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 22:00:00 | 98.000000 | 16.420000 | 17.180000 | 97.000000 | 1013.000000 |  | 16.900000 | 0.500000 | 137.000000 | 63.000000 | 1.6 | 0.340000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-02-11 23:00:00 | 98.000000 | 15.740000 | 16.130000 | 99.000000 | 1014.000000 |  | 15.900000 | 0.000000 | 132.000000 | 73.000000 | 1.22 | 0.560000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35020310_OWM_Clouds_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Clouds_20220213.png)
![CNE_IDEAM_Station35020310_OWM_Dewpoint_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Dewpoint_20220213.png)
![CNE_IDEAM_Station35020310_OWM_Feelslike_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Feelslike_20220213.png)
![CNE_IDEAM_Station35020310_OWM_Humidity_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Humidity_20220213.png)
![CNE_IDEAM_Station35020310_OWM_Pressure_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Pressure_20220213.png)
![CNE_IDEAM_Station35020310_OWM_Rain_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Rain_20220213.png)
![CNE_IDEAM_Station35020310_OWM_Temp_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Temp_20220213.png)
![CNE_IDEAM_Station35020310_OWM_UVI_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_UVI_20220213.png)
![CNE_IDEAM_Station35020310_OWM_Visibility_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Visibility_20220213.png)
![CNE_IDEAM_Station35020310_OWM_Winddeg_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Winddeg_20220213.png)
![CNE_IDEAM_Station35020310_OWM_Windgust_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Windgust_20220213.png)
![CNE_IDEAM_Station35020310_OWM_Windspeed_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Windspeed_20220213.png)

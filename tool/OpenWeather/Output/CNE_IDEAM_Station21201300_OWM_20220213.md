
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201300_OWM_20220213.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220213.csv)

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

### (CNE index 1515) Open Weather values for station 21201300 - AUSTRALIA [21201300]

JSON data from API OWM:

```
{'lat': 4.3943, 'lon': -74.132, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644564606, 'sunrise': 1644577908, 'sunset': 1644620994, 'temp': 6.38, 'feels_like': 6.38, 'pressure': 1014, 'humidity': 92, 'dew_point': 5.18, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 246, 'wind_gust': 0.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, 'hourly': [{'dt': 1644537600, 'temp': 9.38, 'feels_like': 9.38, 'pressure': 1014, 'humidity': 93, 'dew_point': 8.31, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 99, 'wind_gust': 1.44, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644541200, 'temp': 8.38, 'feels_like': 8.38, 'pressure': 1015, 'humidity': 92, 'dew_point': 7.16, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 108, 'wind_gust': 1.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644544800, 'temp': 8.38, 'feels_like': 8.38, 'pressure': 1016, 'humidity': 90, 'dew_point': 6.84, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 114, 'wind_gust': 1.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644548400, 'temp': 8.38, 'feels_like': 8.38, 'pressure': 1017, 'humidity': 91, 'dew_point': 7, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 116, 'wind_gust': 1.09, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644552000, 'temp': 8.38, 'feels_like': 8.38, 'pressure': 1017, 'humidity': 92, 'dew_point': 7.16, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 118, 'wind_gust': 1.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644555600, 'temp': 7.38, 'feels_like': 7.38, 'pressure': 1016, 'humidity': 92, 'dew_point': 6.17, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 117, 'wind_gust': 1.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644559200, 'temp': 7.38, 'feels_like': 7.38, 'pressure': 1015, 'humidity': 92, 'dew_point': 6.17, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 145, 'wind_gust': 0.94, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644562800, 'temp': 6.38, 'feels_like': 6.38, 'pressure': 1014, 'humidity': 91, 'dew_point': 5.02, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 175, 'wind_gust': 0.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644566400, 'temp': 6.38, 'feels_like': 6.38, 'pressure': 1014, 'humidity': 92, 'dew_point': 5.18, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 246, 'wind_gust': 0.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644570000, 'temp': 6.38, 'feels_like': 6.38, 'pressure': 1014, 'humidity': 93, 'dew_point': 5.33, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 265, 'wind_gust': 0.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644573600, 'temp': 5.38, 'feels_like': 5.38, 'pressure': 1015, 'humidity': 92, 'dew_point': 4.19, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 274, 'wind_gust': 0.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644577200, 'temp': 5.38, 'feels_like': 5.38, 'pressure': 1015, 'humidity': 91, 'dew_point': 4.03, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 266, 'wind_gust': 0.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644580800, 'temp': 6.38, 'feels_like': 6.38, 'pressure': 1016, 'humidity': 87, 'dew_point': 4.38, 'uvi': 0.44, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 15, 'wind_gust': 0.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644584400, 'temp': 10.38, 'feels_like': 9.64, 'pressure': 1016, 'humidity': 83, 'dew_point': 7.62, 'uvi': 2.45, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 87, 'wind_gust': 1.02, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644588000, 'temp': 12.38, 'feels_like': 11.71, 'pressure': 1016, 'humidity': 78, 'dew_point': 8.66, 'uvi': 5.78, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 96, 'wind_gust': 1.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644591600, 'temp': 13.38, 'feels_like': 12.63, 'pressure': 1015, 'humidity': 71, 'dew_point': 8.24, 'uvi': 9.69, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 61, 'wind_gust': 1.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644595200, 'temp': 14.38, 'feels_like': 13.62, 'pressure': 1014, 'humidity': 67, 'dew_point': 8.34, 'uvi': 12.74, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 7, 'wind_gust': 1.94, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644598800, 'temp': 16.38, 'feels_like': 15.85, 'pressure': 1013, 'humidity': 68, 'dew_point': 10.47, 'uvi': 13.86, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 8, 'wind_gust': 2.52, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644602400, 'temp': 15.38, 'feels_like': 14.88, 'pressure': 1012, 'humidity': 73, 'dew_point': 10.57, 'uvi': 12.6, 'clouds': 72, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 349, 'wind_gust': 2.49, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644606000, 'temp': 16.38, 'feels_like': 16.11, 'pressure': 1011, 'humidity': 78, 'dew_point': 12.54, 'uvi': 8.92, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 348, 'wind_gust': 2.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644609600, 'temp': 16.38, 'feels_like': 16.29, 'pressure': 1011, 'humidity': 85, 'dew_point': 13.85, 'uvi': 5.22, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 256, 'wind_gust': 1.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644613200, 'temp': 13.38, 'feels_like': 13.07, 'pressure': 1011, 'humidity': 88, 'dew_point': 11.44, 'uvi': 2.15, 'clouds': 91, 'visibility': 7166, 'wind_speed': 0.32, 'wind_deg': 214, 'wind_gust': 1.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644616800, 'temp': 13.38, 'feels_like': 13.2, 'pressure': 1012, 'humidity': 93, 'dew_point': 12.27, 'uvi': 0.5, 'clouds': 93, 'visibility': 6100, 'wind_speed': 0.23, 'wind_deg': 157, 'wind_gust': 1.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644620400, 'temp': 12.38, 'feels_like': 12.21, 'pressure': 1013, 'humidity': 97, 'dew_point': 11.92, 'uvi': 0, 'clouds': 93, 'visibility': 1200, 'wind_speed': 0.52, 'wind_deg': 109, 'wind_gust': 1.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 00:00:00 | 74.000000 | 8.310000 | 9.380000 | 93.000000 | 1014.000000 |  | 9.380000 | 0.000000 | 10000.000000 | 99.000000 | 1.44 | 1.120000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 01:00:00 | 89.000000 | 7.160000 | 8.380000 | 92.000000 | 1015.000000 |  | 8.380000 | 0.000000 | 10000.000000 | 108.000000 | 1.42 | 1.010000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 02:00:00 | 88.000000 | 6.840000 | 8.380000 | 90.000000 | 1016.000000 |  | 8.380000 | 0.000000 | 10000.000000 | 114.000000 | 1.04 | 0.650000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 03:00:00 | 84.000000 | 7.000000 | 8.380000 | 91.000000 | 1017.000000 |  | 8.380000 | 0.000000 | 10000.000000 | 116.000000 | 1.09 | 0.640000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 04:00:00 | 79.000000 | 7.160000 | 8.380000 | 92.000000 | 1017.000000 |  | 8.380000 | 0.000000 | 10000.000000 | 118.000000 | 1.11 | 0.630000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 05:00:00 | 80.000000 | 6.170000 | 7.380000 | 92.000000 | 1016.000000 |  | 7.380000 | 0.000000 | 10000.000000 | 117.000000 | 1.01 | 0.600000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 06:00:00 | 81.000000 | 6.170000 | 7.380000 | 92.000000 | 1015.000000 |  | 7.380000 | 0.000000 | 10000.000000 | 145.000000 | 0.94 | 0.490000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 07:00:00 | 93.000000 | 5.020000 | 6.380000 | 91.000000 | 1014.000000 |  | 6.380000 | 0.000000 | 10000.000000 | 175.000000 | 0.87 | 0.460000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 08:00:00 | 97.000000 | 5.180000 | 6.380000 | 92.000000 | 1014.000000 |  | 6.380000 | 0.000000 | 10000.000000 | 246.000000 | 0.67 | 0.370000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 09:00:00 | 98.000000 | 5.330000 | 6.380000 | 93.000000 | 1014.000000 |  | 6.380000 | 0.000000 | 10000.000000 | 265.000000 | 0.8 | 0.400000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 10:00:00 | 98.000000 | 4.190000 | 5.380000 | 92.000000 | 1015.000000 |  | 5.380000 | 0.000000 | 10000.000000 | 274.000000 | 0.66 | 0.420000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 11:00:00 | 97.000000 | 4.030000 | 5.380000 | 91.000000 | 1015.000000 |  | 5.380000 | 0.000000 | 10000.000000 | 266.000000 | 0.61 | 0.500000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 12:00:00 | 85.000000 | 4.380000 | 6.380000 | 87.000000 | 1016.000000 |  | 6.380000 | 0.440000 | 10000.000000 | 15.000000 | 0.74 | 0.210000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 13:00:00 | 95.000000 | 7.620000 | 9.640000 | 83.000000 | 1016.000000 |  | 10.380000 | 2.450000 | 10000.000000 | 87.000000 | 1.02 | 0.440000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 14:00:00 | 94.000000 | 8.660000 | 11.710000 | 78.000000 | 1016.000000 |  | 12.380000 | 5.780000 | 10000.000000 | 96.000000 | 1.29 | 0.480000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 15:00:00 | 90.000000 | 8.240000 | 12.630000 | 71.000000 | 1015.000000 |  | 13.380000 | 9.690000 | 10000.000000 | 61.000000 | 1.78 | 0.380000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 16:00:00 | 86.000000 | 8.340000 | 13.620000 | 67.000000 | 1014.000000 |  | 14.380000 | 12.740000 | 10000.000000 | 7.000000 | 1.94 | 0.490000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 17:00:00 | 82.000000 | 10.470000 | 15.850000 | 68.000000 | 1013.000000 |  | 16.380000 | 13.860000 | 10000.000000 | 8.000000 | 2.52 | 0.590000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 18:00:00 | 72.000000 | 10.570000 | 14.880000 | 73.000000 | 1012.000000 |  | 15.380000 | 12.600000 | 10000.000000 | 349.000000 | 2.49 | 0.590000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 19:00:00 | 86.000000 | 12.540000 | 16.110000 | 78.000000 | 1011.000000 |  | 16.380000 | 8.920000 | 10000.000000 | 348.000000 | 2.22 | 0.340000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 20:00:00 | 90.000000 | 13.850000 | 16.290000 | 85.000000 | 1011.000000 |  | 16.380000 | 5.220000 | 10000.000000 | 256.000000 | 1.9 | 0.280000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 21:00:00 | 91.000000 | 11.440000 | 13.070000 | 88.000000 | 1011.000000 |  | 13.380000 | 2.150000 | 7166.000000 | 214.000000 | 1.66 | 0.320000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 22:00:00 | 93.000000 | 12.270000 | 13.200000 | 93.000000 | 1012.000000 |  | 13.380000 | 0.500000 | 6100.000000 | 157.000000 | 1.78 | 0.230000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 23:00:00 | 93.000000 | 11.920000 | 12.210000 | 97.000000 | 1013.000000 |  | 12.380000 | 0.000000 | 1200.000000 | 109.000000 | 1.32 | 0.520000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21201300_OWM_Clouds_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Clouds_20220213.png)
![CNE_IDEAM_Station21201300_OWM_Dewpoint_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Dewpoint_20220213.png)
![CNE_IDEAM_Station21201300_OWM_Feelslike_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Feelslike_20220213.png)
![CNE_IDEAM_Station21201300_OWM_Humidity_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Humidity_20220213.png)
![CNE_IDEAM_Station21201300_OWM_Pressure_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Pressure_20220213.png)
![CNE_IDEAM_Station21201300_OWM_Rain_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Rain_20220213.png)
![CNE_IDEAM_Station21201300_OWM_Temp_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Temp_20220213.png)
![CNE_IDEAM_Station21201300_OWM_UVI_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_UVI_20220213.png)
![CNE_IDEAM_Station21201300_OWM_Visibility_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Visibility_20220213.png)
![CNE_IDEAM_Station21201300_OWM_Winddeg_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Winddeg_20220213.png)
![CNE_IDEAM_Station21201300_OWM_Windgust_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Windgust_20220213.png)
![CNE_IDEAM_Station21201300_OWM_Windspeed_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Windspeed_20220213.png)

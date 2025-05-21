
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

* Current date time: 2022-02-11 17:24:58.576252
* Unix time to eval: 1644427498
* Days before (for historical data): 2
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220211.xls
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201300_OWM_20220211.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220211.csv)

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
{'lat': 4.3943, 'lon': -74.132, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644427498, 'sunrise': 1644405117, 'sunset': 1644448179, 'temp': 15.38, 'feels_like': 14.98, 'pressure': 1015, 'humidity': 77, 'dew_point': 11.37, 'uvi': 12.94, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 171, 'wind_gust': 2.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644364800, 'temp': 8.38, 'feels_like': 8.38, 'pressure': 1017, 'humidity': 96, 'dew_point': 7.78, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 195, 'wind_gust': 0.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644368400, 'temp': 7.38, 'feels_like': 7.38, 'pressure': 1018, 'humidity': 94, 'dew_point': 6.48, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 165, 'wind_gust': 0.93, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644372000, 'temp': 7.38, 'feels_like': 7.38, 'pressure': 1019, 'humidity': 92, 'dew_point': 6.17, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 149, 'wind_gust': 1.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644375600, 'temp': 5.38, 'feels_like': 5.38, 'pressure': 1019, 'humidity': 91, 'dew_point': 4.03, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 118, 'wind_gust': 1.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644379200, 'temp': 5.38, 'feels_like': 5.38, 'pressure': 1019, 'humidity': 90, 'dew_point': 3.87, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 127, 'wind_gust': 1.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644382800, 'temp': 5.38, 'feels_like': 5.38, 'pressure': 1019, 'humidity': 90, 'dew_point': 3.87, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 134, 'wind_gust': 1.35, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644386400, 'temp': 4.38, 'feels_like': 4.38, 'pressure': 1017, 'humidity': 89, 'dew_point': 2.73, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 131, 'wind_gust': 1.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644390000, 'temp': 4.38, 'feels_like': 4.38, 'pressure': 1017, 'humidity': 89, 'dew_point': 2.73, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 134, 'wind_gust': 1.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644393600, 'temp': 5.38, 'feels_like': 5.38, 'pressure': 1016, 'humidity': 89, 'dew_point': 3.72, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 122, 'wind_gust': 1.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644397200, 'temp': 5.38, 'feels_like': 5.38, 'pressure': 1016, 'humidity': 89, 'dew_point': 3.72, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 122, 'wind_gust': 1.26, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644400800, 'temp': 5.38, 'feels_like': 5.38, 'pressure': 1017, 'humidity': 89, 'dew_point': 3.72, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 123, 'wind_gust': 1.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644404400, 'temp': 6.38, 'feels_like': 6.38, 'pressure': 1017, 'humidity': 89, 'dew_point': 4.7, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 130, 'wind_gust': 1.41, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644408000, 'temp': 6.38, 'feels_like': 6.38, 'pressure': 1017, 'humidity': 85, 'dew_point': 4.05, 'uvi': 0.15, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 124, 'wind_gust': 1.23, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644411600, 'temp': 9.38, 'feels_like': 9.38, 'pressure': 1017, 'humidity': 78, 'dew_point': 5.74, 'uvi': 2.26, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 94, 'wind_gust': 1.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644415200, 'temp': 11.38, 'feels_like': 10.48, 'pressure': 1017, 'humidity': 73, 'dew_point': 6.72, 'uvi': 5.32, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 108, 'wind_gust': 1.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644418800, 'temp': 13.38, 'feels_like': 12.6, 'pressure': 1017, 'humidity': 70, 'dew_point': 8.03, 'uvi': 8.92, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.13, 'wind_deg': 101, 'wind_gust': 2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644422400, 'temp': 14.38, 'feels_like': 13.75, 'pressure': 1016, 'humidity': 72, 'dew_point': 9.4, 'uvi': 11.89, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 158, 'wind_gust': 1.98, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644426000, 'temp': 15.38, 'feels_like': 14.98, 'pressure': 1015, 'humidity': 77, 'dew_point': 11.37, 'uvi': 12.94, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 171, 'wind_gust': 2.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644429600, 'temp': 15.38, 'feels_like': 15.14, 'pressure': 1014, 'humidity': 83, 'dew_point': 12.51, 'uvi': 11.76, 'clouds': 82, 'visibility': 8295, 'wind_speed': 0.31, 'wind_deg': 172, 'wind_gust': 1.98, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644433200, 'temp': 12.38, 'feels_like': 11.89, 'pressure': 1013, 'humidity': 85, 'dew_point': 9.93, 'uvi': 8.13, 'clouds': 93, 'visibility': 7608, 'wind_speed': 0.38, 'wind_deg': 146, 'wind_gust': 1.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1644436800, 'temp': 12.38, 'feels_like': 11.97, 'pressure': 1013, 'humidity': 88, 'dew_point': 10.45, 'uvi': 4.75, 'clouds': 95, 'visibility': 7484, 'wind_speed': 0.5, 'wind_deg': 138, 'wind_gust': 1.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.42}}, {'dt': 1644440400, 'temp': 9.38, 'feels_like': 9.38, 'pressure': 1013, 'humidity': 91, 'dew_point': 7.99, 'uvi': 1.96, 'clouds': 97, 'visibility': 7103, 'wind_speed': 0.56, 'wind_deg': 118, 'wind_gust': 1.64, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.49}}, {'dt': 1644444000, 'temp': 9.38, 'feels_like': 9.38, 'pressure': 1013, 'humidity': 92, 'dew_point': 8.15, 'uvi': 0.4, 'clouds': 97, 'visibility': 7886, 'wind_speed': 0.47, 'wind_deg': 101, 'wind_gust': 1.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644447600, 'temp': 9.38, 'feels_like': 9.38, 'pressure': 1014, 'humidity': 96, 'dew_point': 8.78, 'uvi': 0, 'clouds': 96, 'visibility': 6856, 'wind_speed': 0.69, 'wind_deg': 99, 'wind_gust': 1.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 00:00:00 | 100.000000 | 7.780000 | 8.380000 | 96.000000 | 1017.000000 |  | 8.380000 | 0.000000 | 10000.000000 | 195.000000 | 0.87 | 0.230000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 01:00:00 | 100.000000 | 6.480000 | 7.380000 | 94.000000 | 1018.000000 |  | 7.380000 | 0.000000 | 10000.000000 | 165.000000 | 0.93 | 0.360000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 02:00:00 | 100.000000 | 6.170000 | 7.380000 | 92.000000 | 1019.000000 |  | 7.380000 | 0.000000 | 10000.000000 | 149.000000 | 1.07 | 0.430000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 03:00:00 | 99.000000 | 4.030000 | 5.380000 | 91.000000 | 1019.000000 |  | 5.380000 | 0.000000 | 10000.000000 | 118.000000 | 1.4 | 0.590000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 04:00:00 | 93.000000 | 3.870000 | 5.380000 | 90.000000 | 1019.000000 |  | 5.380000 | 0.000000 | 10000.000000 | 127.000000 | 1.44 | 0.730000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 05:00:00 | 93.000000 | 3.870000 | 5.380000 | 90.000000 | 1019.000000 |  | 5.380000 | 0.000000 | 10000.000000 | 134.000000 | 1.35 | 0.540000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 06:00:00 | 84.000000 | 2.730000 | 4.380000 | 89.000000 | 1017.000000 |  | 4.380000 | 0.000000 | 10000.000000 | 131.000000 | 1.07 | 0.500000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 07:00:00 | 92.000000 | 2.730000 | 4.380000 | 89.000000 | 1017.000000 |  | 4.380000 | 0.000000 | 10000.000000 | 134.000000 | 1.2 | 0.630000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 08:00:00 | 89.000000 | 3.720000 | 5.380000 | 89.000000 | 1016.000000 |  | 5.380000 | 0.000000 | 10000.000000 | 122.000000 | 1.17 | 0.630000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 09:00:00 | 88.000000 | 3.720000 | 5.380000 | 89.000000 | 1016.000000 |  | 5.380000 | 0.000000 | 10000.000000 | 122.000000 | 1.26 | 0.770000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 10:00:00 | 85.000000 | 3.720000 | 5.380000 | 89.000000 | 1017.000000 |  | 5.380000 | 0.000000 | 10000.000000 | 123.000000 | 1.46 | 0.750000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 11:00:00 | 82.000000 | 4.700000 | 6.380000 | 89.000000 | 1017.000000 |  | 6.380000 | 0.000000 | 10000.000000 | 130.000000 | 1.41 | 0.810000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 12:00:00 | 89.000000 | 4.050000 | 6.380000 | 85.000000 | 1017.000000 |  | 6.380000 | 0.150000 | 10000.000000 | 124.000000 | 1.23 | 0.570000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 13:00:00 | 93.000000 | 5.740000 | 9.380000 | 78.000000 | 1017.000000 |  | 9.380000 | 2.260000 | 10000.000000 | 94.000000 | 1.57 | 0.550000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 14:00:00 | 97.000000 | 6.720000 | 10.480000 | 73.000000 | 1017.000000 |  | 11.380000 | 5.320000 | 10000.000000 | 108.000000 | 1.77 | 0.390000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 15:00:00 | 98.000000 | 8.030000 | 12.600000 | 70.000000 | 1017.000000 |  | 13.380000 | 8.920000 | 10000.000000 | 101.000000 | 2 | 0.130000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 16:00:00 | 98.000000 | 9.400000 | 13.750000 | 72.000000 | 1016.000000 |  | 14.380000 | 11.890000 | 10000.000000 | 158.000000 | 1.98 | 0.250000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 17:00:00 | 98.000000 | 11.370000 | 14.980000 | 77.000000 | 1015.000000 |  | 15.380000 | 12.940000 | 10000.000000 | 171.000000 | 2.04 | 0.440000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 18:00:00 | 82.000000 | 12.510000 | 15.140000 | 83.000000 | 1014.000000 |  | 15.380000 | 11.760000 | 8295.000000 | 172.000000 | 1.98 | 0.310000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 19:00:00 | 93.000000 | 9.930000 | 11.890000 | 85.000000 | 1013.000000 | 0.21 | 12.380000 | 8.130000 | 7608.000000 | 146.000000 | 1.77 | 0.380000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 20:00:00 | 95.000000 | 10.450000 | 11.970000 | 88.000000 | 1013.000000 | 0.42 | 12.380000 | 4.750000 | 7484.000000 | 138.000000 | 1.74 | 0.500000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 21:00:00 | 97.000000 | 7.990000 | 9.380000 | 91.000000 | 1013.000000 | 0.49 | 9.380000 | 1.960000 | 7103.000000 | 118.000000 | 1.64 | 0.560000 | 500 | Rain | light rain | 10d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 22:00:00 | 97.000000 | 8.150000 | 9.380000 | 92.000000 | 1013.000000 |  | 9.380000 | 0.400000 | 7886.000000 | 101.000000 | 1.49 | 0.470000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-09 23:00:00 | 96.000000 | 8.780000 | 9.380000 | 96.000000 | 1014.000000 |  | 9.380000 | 0.000000 | 6856.000000 | 99.000000 | 1.29 | 0.690000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21201300_OWM_Clouds_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Clouds_20220211.png)
![CNE_IDEAM_Station21201300_OWM_Dewpoint_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Dewpoint_20220211.png)
![CNE_IDEAM_Station21201300_OWM_Feelslike_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Feelslike_20220211.png)
![CNE_IDEAM_Station21201300_OWM_Humidity_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Humidity_20220211.png)
![CNE_IDEAM_Station21201300_OWM_Pressure_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Pressure_20220211.png)
![CNE_IDEAM_Station21201300_OWM_Rain_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Rain_20220211.png)
![CNE_IDEAM_Station21201300_OWM_Temp_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Temp_20220211.png)
![CNE_IDEAM_Station21201300_OWM_UVI_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_UVI_20220211.png)
![CNE_IDEAM_Station21201300_OWM_Visibility_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Visibility_20220211.png)
![CNE_IDEAM_Station21201300_OWM_Winddeg_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Winddeg_20220211.png)
![CNE_IDEAM_Station21201300_OWM_Windgust_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Windgust_20220211.png)
![CNE_IDEAM_Station21201300_OWM_Windspeed_20220211.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Windspeed_20220211.png)

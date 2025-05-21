
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201200_OWM_20220213.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220213.csv)

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

### (CNE index 3317) Open Weather values for station 21201200 - ESCUELA LA UNION [21201200]

JSON data from API OWM:

```
{'lat': 4.3429, 'lon': -74.1839, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644564606, 'sunrise': 1644577917, 'sunset': 1644621009, 'temp': 4.98, 'feels_like': 4.98, 'pressure': 1014, 'humidity': 93, 'dew_point': 3.94, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 253, 'wind_gust': 0.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, 'hourly': [{'dt': 1644537600, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1014, 'humidity': 93, 'dew_point': 6.92, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 87, 'wind_gust': 1.53, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644541200, 'temp': 6.98, 'feels_like': 6.98, 'pressure': 1015, 'humidity': 91, 'dew_point': 5.61, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 99, 'wind_gust': 1.4, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644544800, 'temp': 6.98, 'feels_like': 6.98, 'pressure': 1016, 'humidity': 90, 'dew_point': 5.45, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 101, 'wind_gust': 0.92, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644548400, 'temp': 6.98, 'feels_like': 6.98, 'pressure': 1017, 'humidity': 91, 'dew_point': 5.61, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 94, 'wind_gust': 0.88, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644552000, 'temp': 6.98, 'feels_like': 6.98, 'pressure': 1016, 'humidity': 91, 'dew_point': 5.61, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 97, 'wind_gust': 0.98, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644555600, 'temp': 5.98, 'feels_like': 5.98, 'pressure': 1016, 'humidity': 91, 'dew_point': 4.62, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 97, 'wind_gust': 0.91, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644559200, 'temp': 5.98, 'feels_like': 5.98, 'pressure': 1015, 'humidity': 92, 'dew_point': 4.78, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 119, 'wind_gust': 0.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644562800, 'temp': 4.98, 'feels_like': 4.98, 'pressure': 1014, 'humidity': 92, 'dew_point': 3.79, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 158, 'wind_gust': 0.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644566400, 'temp': 4.98, 'feels_like': 4.98, 'pressure': 1014, 'humidity': 93, 'dew_point': 3.94, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 253, 'wind_gust': 0.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644570000, 'temp': 4.98, 'feels_like': 4.98, 'pressure': 1014, 'humidity': 94, 'dew_point': 4.1, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 277, 'wind_gust': 0.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644573600, 'temp': 3.98, 'feels_like': 3.98, 'pressure': 1015, 'humidity': 93, 'dew_point': 2.95, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 284, 'wind_gust': 0.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644577200, 'temp': 3.98, 'feels_like': 3.98, 'pressure': 1015, 'humidity': 91, 'dew_point': 2.65, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 275, 'wind_gust': 0.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644580800, 'temp': 4.98, 'feels_like': 4.98, 'pressure': 1016, 'humidity': 88, 'dew_point': 3.16, 'uvi': 0.44, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 26, 'wind_gust': 0.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644584400, 'temp': 8.98, 'feels_like': 8.98, 'pressure': 1016, 'humidity': 84, 'dew_point': 6.43, 'uvi': 2.45, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 48, 'wind_gust': 1.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644588000, 'temp': 10.98, 'feels_like': 10.2, 'pressure': 1016, 'humidity': 79, 'dew_point': 7.48, 'uvi': 5.78, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 20, 'wind_gust': 1.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644591600, 'temp': 11.98, 'feels_like': 11.11, 'pressure': 1015, 'humidity': 72, 'dew_point': 7.1, 'uvi': 9.69, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 350, 'wind_gust': 1.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644595200, 'temp': 12.98, 'feels_like': 12.16, 'pressure': 1014, 'humidity': 70, 'dew_point': 7.64, 'uvi': 12.74, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 331, 'wind_gust': 2.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644598800, 'temp': 14.98, 'feels_like': 14.39, 'pressure': 1013, 'humidity': 71, 'dew_point': 9.77, 'uvi': 13.86, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 329, 'wind_gust': 2.59, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644602400, 'temp': 13.98, 'feels_like': 13.44, 'pressure': 1012, 'humidity': 77, 'dew_point': 10.02, 'uvi': 12.6, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 317, 'wind_gust': 2.47, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644606000, 'temp': 14.98, 'feels_like': 14.67, 'pressure': 1011, 'humidity': 82, 'dew_point': 11.94, 'uvi': 8.92, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 310, 'wind_gust': 2.19, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644609600, 'temp': 14.98, 'feels_like': 14.88, 'pressure': 1011, 'humidity': 90, 'dew_point': 13.35, 'uvi': 5.22, 'clouds': 96, 'visibility': 9188, 'wind_speed': 0.94, 'wind_deg': 289, 'wind_gust': 1.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644613200, 'temp': 11.98, 'feels_like': 11.66, 'pressure': 1012, 'humidity': 93, 'dew_point': 10.88, 'uvi': 2.15, 'clouds': 96, 'visibility': 3261, 'wind_speed': 0.71, 'wind_deg': 284, 'wind_gust': 1.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644616800, 'temp': 11.98, 'feels_like': 11.71, 'pressure': 1012, 'humidity': 95, 'dew_point': 11.2, 'uvi': 0.5, 'clouds': 97, 'visibility': 2597, 'wind_speed': 0.33, 'wind_deg': 298, 'wind_gust': 1.59, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644620400, 'temp': 10.98, 'feels_like': 10.69, 'pressure': 1013, 'humidity': 98, 'dew_point': 10.68, 'uvi': 0, 'clouds': 96, 'visibility': 1058, 'wind_speed': 0.3, 'wind_deg': 65, 'wind_gust': 1.02, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 00:00:00 | 65.000000 | 6.920000 | 7.980000 | 93.000000 | 1014.000000 |  | 7.980000 | 0.000000 | 10000.000000 | 87.000000 | 1.53 | 1.330000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 01:00:00 | 80.000000 | 5.610000 | 6.980000 | 91.000000 | 1015.000000 |  | 6.980000 | 0.000000 | 10000.000000 | 99.000000 | 1.4 | 1.220000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 02:00:00 | 80.000000 | 5.450000 | 6.980000 | 90.000000 | 1016.000000 |  | 6.980000 | 0.000000 | 10000.000000 | 101.000000 | 0.92 | 0.710000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 03:00:00 | 77.000000 | 5.610000 | 6.980000 | 91.000000 | 1017.000000 |  | 6.980000 | 0.000000 | 10000.000000 | 94.000000 | 0.88 | 0.610000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 04:00:00 | 76.000000 | 5.610000 | 6.980000 | 91.000000 | 1016.000000 |  | 6.980000 | 0.000000 | 10000.000000 | 97.000000 | 0.98 | 0.680000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 05:00:00 | 78.000000 | 4.620000 | 5.980000 | 91.000000 | 1016.000000 |  | 5.980000 | 0.000000 | 10000.000000 | 97.000000 | 0.91 | 0.620000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 06:00:00 | 86.000000 | 4.780000 | 5.980000 | 92.000000 | 1015.000000 |  | 5.980000 | 0.000000 | 10000.000000 | 119.000000 | 0.75 | 0.440000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 07:00:00 | 95.000000 | 3.790000 | 4.980000 | 92.000000 | 1014.000000 |  | 4.980000 | 0.000000 | 10000.000000 | 158.000000 | 0.73 | 0.360000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 08:00:00 | 97.000000 | 3.940000 | 4.980000 | 93.000000 | 1014.000000 |  | 4.980000 | 0.000000 | 10000.000000 | 253.000000 | 0.63 | 0.320000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 09:00:00 | 98.000000 | 4.100000 | 4.980000 | 94.000000 | 1014.000000 |  | 4.980000 | 0.000000 | 10000.000000 | 277.000000 | 0.78 | 0.300000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 10:00:00 | 99.000000 | 2.950000 | 3.980000 | 93.000000 | 1015.000000 |  | 3.980000 | 0.000000 | 10000.000000 | 284.000000 | 0.66 | 0.330000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 11:00:00 | 98.000000 | 2.650000 | 3.980000 | 91.000000 | 1015.000000 |  | 3.980000 | 0.000000 | 10000.000000 | 275.000000 | 0.58 | 0.400000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 12:00:00 | 91.000000 | 3.160000 | 4.980000 | 88.000000 | 1016.000000 |  | 4.980000 | 0.440000 | 10000.000000 | 26.000000 | 0.79 | 0.390000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 13:00:00 | 98.000000 | 6.430000 | 8.980000 | 84.000000 | 1016.000000 |  | 8.980000 | 2.450000 | 10000.000000 | 48.000000 | 1.04 | 0.440000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 14:00:00 | 96.000000 | 7.480000 | 10.200000 | 79.000000 | 1016.000000 |  | 10.980000 | 5.780000 | 10000.000000 | 20.000000 | 1.34 | 0.430000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 15:00:00 | 89.000000 | 7.100000 | 11.110000 | 72.000000 | 1015.000000 |  | 11.980000 | 9.690000 | 10000.000000 | 350.000000 | 1.88 | 0.740000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 16:00:00 | 86.000000 | 7.640000 | 12.160000 | 70.000000 | 1014.000000 |  | 12.980000 | 12.740000 | 10000.000000 | 331.000000 | 2.03 | 1.170000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 17:00:00 | 83.000000 | 9.770000 | 14.390000 | 71.000000 | 1013.000000 |  | 14.980000 | 13.860000 | 10000.000000 | 329.000000 | 2.59 | 1.310000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 18:00:00 | 81.000000 | 10.020000 | 13.440000 | 77.000000 | 1012.000000 |  | 13.980000 | 12.600000 | 10000.000000 | 317.000000 | 2.47 | 1.370000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 19:00:00 | 93.000000 | 11.940000 | 14.670000 | 82.000000 | 1011.000000 |  | 14.980000 | 8.920000 | 10000.000000 | 310.000000 | 2.19 | 1.090000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 20:00:00 | 96.000000 | 13.350000 | 14.880000 | 90.000000 | 1011.000000 |  | 14.980000 | 5.220000 | 9188.000000 | 289.000000 | 1.95 | 0.940000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 21:00:00 | 96.000000 | 10.880000 | 11.660000 | 93.000000 | 1012.000000 |  | 11.980000 | 2.150000 | 3261.000000 | 284.000000 | 1.66 | 0.710000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 22:00:00 | 97.000000 | 11.200000 | 11.710000 | 95.000000 | 1012.000000 |  | 11.980000 | 0.500000 | 2597.000000 | 298.000000 | 1.59 | 0.330000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviométrica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 23:00:00 | 96.000000 | 10.680000 | 10.690000 | 98.000000 | 1013.000000 |  | 10.980000 | 0.000000 | 1058.000000 | 65.000000 | 1.02 | 0.300000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21201200_OWM_Clouds_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Clouds_20220213.png)
![CNE_IDEAM_Station21201200_OWM_Dewpoint_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Dewpoint_20220213.png)
![CNE_IDEAM_Station21201200_OWM_Feelslike_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Feelslike_20220213.png)
![CNE_IDEAM_Station21201200_OWM_Humidity_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Humidity_20220213.png)
![CNE_IDEAM_Station21201200_OWM_Pressure_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Pressure_20220213.png)
![CNE_IDEAM_Station21201200_OWM_Rain_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Rain_20220213.png)
![CNE_IDEAM_Station21201200_OWM_Temp_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Temp_20220213.png)
![CNE_IDEAM_Station21201200_OWM_UVI_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_UVI_20220213.png)
![CNE_IDEAM_Station21201200_OWM_Visibility_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Visibility_20220213.png)
![CNE_IDEAM_Station21201200_OWM_Winddeg_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Winddeg_20220213.png)
![CNE_IDEAM_Station21201200_OWM_Windgust_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Windgust_20220213.png)
![CNE_IDEAM_Station21201200_OWM_Windspeed_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Windspeed_20220213.png)


## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - COLEGIO SAN CAYETANO [21206650] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206650_OWM_20220213.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220213.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.51675278,-74.08822222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.51675278&lon=-74.08822222)

| Parameter | Value |
|---|---|
| Code | 21206650 |
| Name | COLEGIO SAN CAYETANO [21206650] |
| Latitude, ° | 4.51675278 |
| Longitude, ° | -74.08822222 |
| Elevation, m | 3100 |
| Category | Climática Ordinaria |
| Technology | Convencional |
| Status | Activa |
| Installation date | 2001-11-15 00:00:00 |
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

### (CNE index 3786) Open Weather values for station 21206650 - COLEGIO SAN CAYETANO [21206650]

JSON data from API OWM:

```
{'lat': 4.5168, 'lon': -74.0882, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644564606, 'sunrise': 1644577905, 'sunset': 1644620976, 'temp': 5.97, 'feels_like': 5.97, 'pressure': 1014, 'humidity': 92, 'dew_point': 4.77, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 219, 'wind_gust': 0.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, 'hourly': [{'dt': 1644537600, 'temp': 8.03, 'feels_like': 8.03, 'pressure': 1014, 'humidity': 94, 'dew_point': 7.12, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 118, 'wind_gust': 1.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644541200, 'temp': 7.91, 'feels_like': 7.91, 'pressure': 1015, 'humidity': 93, 'dew_point': 6.85, 'uvi': 0, 'clouds': 98, 'visibility': 8222, 'wind_speed': 1.02, 'wind_deg': 122, 'wind_gust': 1.62, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644544800, 'temp': 7.91, 'feels_like': 7.91, 'pressure': 1016, 'humidity': 91, 'dew_point': 6.53, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 123, 'wind_gust': 1.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644548400, 'temp': 7.21, 'feels_like': 7.21, 'pressure': 1016, 'humidity': 92, 'dew_point': 6, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 130, 'wind_gust': 1.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644552000, 'temp': 6.87, 'feels_like': 6.87, 'pressure': 1016, 'humidity': 92, 'dew_point': 5.66, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 137, 'wind_gust': 1.31, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644555600, 'temp': 6.77, 'feels_like': 6.77, 'pressure': 1016, 'humidity': 92, 'dew_point': 5.56, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 130, 'wind_gust': 1.13, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644559200, 'temp': 6.67, 'feels_like': 6.67, 'pressure': 1015, 'humidity': 92, 'dew_point': 5.46, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 155, 'wind_gust': 1.19, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644562800, 'temp': 5.97, 'feels_like': 5.97, 'pressure': 1014, 'humidity': 92, 'dew_point': 4.77, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 168, 'wind_gust': 1.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644566400, 'temp': 5.97, 'feels_like': 5.97, 'pressure': 1014, 'humidity': 92, 'dew_point': 4.77, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 219, 'wind_gust': 0.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644570000, 'temp': 5.97, 'feels_like': 5.97, 'pressure': 1014, 'humidity': 92, 'dew_point': 4.77, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 254, 'wind_gust': 0.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644573600, 'temp': 4.97, 'feels_like': 4.97, 'pressure': 1014, 'humidity': 91, 'dew_point': 3.63, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 275, 'wind_gust': 0.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644577200, 'temp': 4.97, 'feels_like': 4.97, 'pressure': 1015, 'humidity': 91, 'dew_point': 3.63, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 247, 'wind_gust': 0.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644580800, 'temp': 5.97, 'feels_like': 5.97, 'pressure': 1015, 'humidity': 87, 'dew_point': 3.97, 'uvi': 0.54, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.16, 'wind_deg': 96, 'wind_gust': 0.6, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644584400, 'temp': 9.97, 'feels_like': 9.97, 'pressure': 1016, 'humidity': 81, 'dew_point': 6.86, 'uvi': 2.47, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 133, 'wind_gust': 1.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644588000, 'temp': 11.97, 'feels_like': 11.18, 'pressure': 1016, 'humidity': 75, 'dew_point': 7.68, 'uvi': 5.83, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 141, 'wind_gust': 1.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644591600, 'temp': 12.97, 'feels_like': 12.05, 'pressure': 1015, 'humidity': 66, 'dew_point': 6.78, 'uvi': 9.79, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 142, 'wind_gust': 1.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644595200, 'temp': 13.97, 'feels_like': 13.02, 'pressure': 1013, 'humidity': 61, 'dew_point': 6.58, 'uvi': 12.22, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 124, 'wind_gust': 1.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644598800, 'temp': 15.97, 'feels_like': 15.19, 'pressure': 1012, 'humidity': 60, 'dew_point': 8.22, 'uvi': 13.3, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 91, 'wind_gust': 2.43, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644602400, 'temp': 14.97, 'feels_like': 14.25, 'pressure': 1011, 'humidity': 66, 'dew_point': 8.68, 'uvi': 12.08, 'clouds': 59, 'visibility': 10000, 'wind_speed': 0.29, 'wind_deg': 60, 'wind_gust': 2.41, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644606000, 'temp': 15.97, 'feels_like': 15.42, 'pressure': 1010, 'humidity': 69, 'dew_point': 10.29, 'uvi': 7.84, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 115, 'wind_gust': 2.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644609600, 'temp': 15.97, 'feels_like': 15.53, 'pressure': 1010, 'humidity': 73, 'dew_point': 11.14, 'uvi': 4.58, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 185, 'wind_gust': 1.91, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644613200, 'temp': 12.97, 'feels_like': 12.36, 'pressure': 1010, 'humidity': 78, 'dew_point': 9.23, 'uvi': 1.88, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 180, 'wind_gust': 1.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644616800, 'temp': 12.97, 'feels_like': 12.65, 'pressure': 1012, 'humidity': 89, 'dew_point': 11.2, 'uvi': 0.39, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 163, 'wind_gust': 2.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644620400, 'temp': 11.97, 'feels_like': 11.7, 'pressure': 1013, 'humidity': 95, 'dew_point': 11.19, 'uvi': 0, 'clouds': 86, 'visibility': 1967, 'wind_speed': 0.8, 'wind_deg': 137, 'wind_gust': 1.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 00:00:00 | 84.000000 | 7.120000 | 8.030000 | 94.000000 | 1014.000000 |  | 8.030000 | 0.000000 | 10000.000000 | 118.000000 | 1.56 | 1.170000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 01:00:00 | 98.000000 | 6.850000 | 7.910000 | 93.000000 | 1015.000000 |  | 7.910000 | 0.000000 | 8222.000000 | 122.000000 | 1.62 | 1.020000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 02:00:00 | 95.000000 | 6.530000 | 7.910000 | 91.000000 | 1016.000000 |  | 7.910000 | 0.000000 | 10000.000000 | 123.000000 | 1.25 | 0.760000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 03:00:00 | 91.000000 | 6.000000 | 7.210000 | 92.000000 | 1016.000000 |  | 7.210000 | 0.000000 | 10000.000000 | 130.000000 | 1.4 | 0.890000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 04:00:00 | 82.000000 | 5.660000 | 6.870000 | 92.000000 | 1016.000000 |  | 6.870000 | 0.000000 | 10000.000000 | 137.000000 | 1.31 | 0.860000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 05:00:00 | 82.000000 | 5.560000 | 6.770000 | 92.000000 | 1016.000000 |  | 6.770000 | 0.000000 | 10000.000000 | 130.000000 | 1.13 | 0.810000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 06:00:00 | 73.000000 | 5.460000 | 6.670000 | 92.000000 | 1015.000000 |  | 6.670000 | 0.000000 | 10000.000000 | 155.000000 | 1.19 | 0.750000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 07:00:00 | 92.000000 | 4.770000 | 5.970000 | 92.000000 | 1014.000000 |  | 5.970000 | 0.000000 | 10000.000000 | 168.000000 | 1.01 | 0.660000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 08:00:00 | 96.000000 | 4.770000 | 5.970000 | 92.000000 | 1014.000000 |  | 5.970000 | 0.000000 | 10000.000000 | 219.000000 | 0.65 | 0.300000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 09:00:00 | 97.000000 | 4.770000 | 5.970000 | 92.000000 | 1014.000000 |  | 5.970000 | 0.000000 | 10000.000000 | 254.000000 | 0.7 | 0.250000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 10:00:00 | 98.000000 | 3.630000 | 4.970000 | 91.000000 | 1014.000000 |  | 4.970000 | 0.000000 | 10000.000000 | 275.000000 | 0.5 | 0.210000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 11:00:00 | 97.000000 | 3.630000 | 4.970000 | 91.000000 | 1015.000000 |  | 4.970000 | 0.000000 | 10000.000000 | 247.000000 | 0.44 | 0.260000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 12:00:00 | 73.000000 | 3.970000 | 5.970000 | 87.000000 | 1015.000000 |  | 5.970000 | 0.540000 | 10000.000000 | 96.000000 | 0.6 | 0.160000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 13:00:00 | 89.000000 | 6.860000 | 9.970000 | 81.000000 | 1016.000000 |  | 9.970000 | 2.470000 | 10000.000000 | 133.000000 | 1.04 | 0.580000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 14:00:00 | 85.000000 | 7.680000 | 11.180000 | 75.000000 | 1016.000000 |  | 11.970000 | 5.830000 | 10000.000000 | 141.000000 | 1.31 | 0.880000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 15:00:00 | 88.000000 | 6.780000 | 12.050000 | 66.000000 | 1015.000000 |  | 12.970000 | 9.790000 | 10000.000000 | 142.000000 | 1.65 | 0.670000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 16:00:00 | 85.000000 | 6.580000 | 13.020000 | 61.000000 | 1013.000000 |  | 13.970000 | 12.220000 | 10000.000000 | 124.000000 | 1.74 | 0.300000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 17:00:00 | 78.000000 | 8.220000 | 15.190000 | 60.000000 | 1012.000000 |  | 15.970000 | 13.300000 | 10000.000000 | 91.000000 | 2.43 | 0.410000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 18:00:00 | 59.000000 | 8.680000 | 14.250000 | 66.000000 | 1011.000000 |  | 14.970000 | 12.080000 | 10000.000000 | 60.000000 | 2.41 | 0.290000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 19:00:00 | 75.000000 | 10.290000 | 15.420000 | 69.000000 | 1010.000000 |  | 15.970000 | 7.840000 | 10000.000000 | 115.000000 | 2.11 | 0.190000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 20:00:00 | 80.000000 | 11.140000 | 15.530000 | 73.000000 | 1010.000000 |  | 15.970000 | 4.580000 | 10000.000000 | 185.000000 | 1.91 | 0.570000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 21:00:00 | 82.000000 | 9.230000 | 12.360000 | 78.000000 | 1010.000000 |  | 12.970000 | 1.880000 | 10000.000000 | 180.000000 | 1.7 | 0.800000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 22:00:00 | 85.000000 | 11.200000 | 12.650000 | 89.000000 | 1012.000000 |  | 12.970000 | 0.390000 | 10000.000000 | 163.000000 | 2.05 | 0.710000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 23:00:00 | 86.000000 | 11.190000 | 11.700000 | 95.000000 | 1013.000000 |  | 11.970000 | 0.000000 | 1967.000000 | 137.000000 | 1.73 | 0.800000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21206650_OWM_Clouds_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Clouds_20220213.png)
![CNE_IDEAM_Station21206650_OWM_Dewpoint_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Dewpoint_20220213.png)
![CNE_IDEAM_Station21206650_OWM_Feelslike_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Feelslike_20220213.png)
![CNE_IDEAM_Station21206650_OWM_Humidity_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Humidity_20220213.png)
![CNE_IDEAM_Station21206650_OWM_Pressure_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Pressure_20220213.png)
![CNE_IDEAM_Station21206650_OWM_Rain_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Rain_20220213.png)
![CNE_IDEAM_Station21206650_OWM_Temp_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Temp_20220213.png)
![CNE_IDEAM_Station21206650_OWM_UVI_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_UVI_20220213.png)
![CNE_IDEAM_Station21206650_OWM_Visibility_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Visibility_20220213.png)
![CNE_IDEAM_Station21206650_OWM_Winddeg_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Winddeg_20220213.png)
![CNE_IDEAM_Station21206650_OWM_Windgust_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Windgust_20220213.png)
![CNE_IDEAM_Station21206650_OWM_Windspeed_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Windspeed_20220213.png)

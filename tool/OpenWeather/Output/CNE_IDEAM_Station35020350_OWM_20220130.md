
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BETANIA [35020350] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35020350_OWM_20220130.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220130.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.21888889,-74.14686111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.21888889&lon=-74.14686111)

| Parameter | Value |
|---|---|
| Code | 35020350 |
| Name | BETANIA [35020350] |
| Latitude, ° | 4.21888889 |
| Longitude, ° | -74.14686111 |
| Elevation, m | 3150 |
| Category | Pluviométrica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1986-01-15 00:00:00 |
| Suspension date | NaT |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Blanco |
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

### (CNE index 1904) Open Weather values for station 35020350 - BETANIA [35020350]

JSON data from API OWM:

```
{'lat': 4.2189, 'lon': -74.1469, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643467037, 'sunrise': 1643454695, 'sunset': 1643497660, 'temp': 11.37, 'feels_like': 10.05, 'pressure': 1016, 'humidity': 57, 'dew_point': 3.16, 'uvi': 9.42, 'clouds': 12, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 324, 'wind_gust': 2.49, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, 'hourly': [{'dt': 1643414400, 'temp': 11.37, 'feels_like': 11.02, 'pressure': 1016, 'humidity': 94, 'dew_point': 10.44, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 69, 'wind_gust': 1.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.78}}, {'dt': 1643418000, 'temp': 11.37, 'feels_like': 10.96, 'pressure': 1017, 'humidity': 92, 'dew_point': 10.12, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 19, 'wind_gust': 1.29, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.68}}, {'dt': 1643421600, 'temp': 10.37, 'feels_like': 9.89, 'pressure': 1018, 'humidity': 93, 'dew_point': 9.29, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 300, 'wind_gust': 1.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643425200, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1018, 'humidity': 93, 'dew_point': 8.3, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 299, 'wind_gust': 1.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.82}}, {'dt': 1643428800, 'temp': 8.37, 'feels_like': 8.37, 'pressure': 1018, 'humidity': 92, 'dew_point': 7.15, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 293, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643432400, 'temp': 8.37, 'feels_like': 8.37, 'pressure': 1018, 'humidity': 94, 'dew_point': 7.46, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 273, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.82}}, {'dt': 1643436000, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1018, 'humidity': 94, 'dew_point': 6.47, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 225, 'wind_gust': 1.2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643439600, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1018, 'humidity': 94, 'dew_point': 6.47, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 256, 'wind_gust': 1.7, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643443200, 'temp': 5.37, 'feels_like': 5.37, 'pressure': 1017, 'humidity': 93, 'dew_point': 4.33, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 258, 'wind_gust': 1.9, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643446800, 'temp': 4.37, 'feels_like': 4.37, 'pressure': 1017, 'humidity': 92, 'dew_point': 3.19, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 257, 'wind_gust': 1.54, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643450400, 'temp': 3.37, 'feels_like': 3.37, 'pressure': 1018, 'humidity': 92, 'dew_point': 2.2, 'uvi': 0, 'clouds': 36, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 255, 'wind_gust': 2.16, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643454000, 'temp': 2.37, 'feels_like': 2.37, 'pressure': 1019, 'humidity': 91, 'dew_point': 1.05, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 251, 'wind_gust': 2.24, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643457600, 'temp': 3.37, 'feels_like': 3.37, 'pressure': 1019, 'humidity': 86, 'dew_point': 1.25, 'uvi': 0.55, 'clouds': 15, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 251, 'wind_gust': 2.2, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643461200, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1018, 'humidity': 72, 'dew_point': 2.66, 'uvi': 2.37, 'clouds': 23, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 301, 'wind_gust': 1.66, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643464800, 'temp': 11.37, 'feels_like': 10.23, 'pressure': 1017, 'humidity': 64, 'dew_point': 4.81, 'uvi': 5.6, 'clouds': 12, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 315, 'wind_gust': 2.13, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643468400, 'temp': 14.37, 'feels_like': 13.35, 'pressure': 1016, 'humidity': 57, 'dew_point': 5.97, 'uvi': 9.42, 'clouds': 12, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 324, 'wind_gust': 2.49, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643472000, 'temp': 15.37, 'feels_like': 14.37, 'pressure': 1015, 'humidity': 54, 'dew_point': 6.12, 'uvi': 12.55, 'clouds': 13, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 333, 'wind_gust': 2.89, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643475600, 'temp': 17.37, 'feels_like': 16.6, 'pressure': 1014, 'humidity': 55, 'dew_point': 8.25, 'uvi': 13.66, 'clouds': 15, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 330, 'wind_gust': 3.14, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643479200, 'temp': 16.37, 'feels_like': 15.6, 'pressure': 1013, 'humidity': 59, 'dew_point': 8.35, 'uvi': 12.4, 'clouds': 49, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 331, 'wind_gust': 2.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1643482800, 'temp': 17.37, 'feels_like': 16.86, 'pressure': 1012, 'humidity': 65, 'dew_point': 10.73, 'uvi': 9.06, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 334, 'wind_gust': 2.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1643486400, 'temp': 16.37, 'feels_like': 15.99, 'pressure': 1012, 'humidity': 74, 'dew_point': 11.73, 'uvi': 5.28, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 344, 'wind_gust': 2.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1643490000, 'temp': 16.37, 'feels_like': 16.15, 'pressure': 1013, 'humidity': 80, 'dew_point': 12.92, 'uvi': 2.16, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 333, 'wind_gust': 2.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.3}}, {'dt': 1643493600, 'temp': 15.37, 'feels_like': 15.21, 'pressure': 1014, 'humidity': 86, 'dew_point': 13.04, 'uvi': 0.45, 'clouds': 90, 'visibility': 9086, 'wind_speed': 0.35, 'wind_deg': 332, 'wind_gust': 2.09, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.25}}, {'dt': 1643497200, 'temp': 13.37, 'feels_like': 13.19, 'pressure': 1015, 'humidity': 93, 'dew_point': 12.26, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 312, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 00:00:00 | 90.000000 | 10.440000 | 11.020000 | 94.000000 | 1016.000000 | 0.78 | 11.370000 | 0.000000 | 10000.000000 | 69.000000 | 1.3 | 0.540000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 01:00:00 | 98.000000 | 10.120000 | 10.960000 | 92.000000 | 1017.000000 | 0.68 | 11.370000 | 0.000000 | 10000.000000 | 19.000000 | 1.29 | 0.470000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 02:00:00 | 88.000000 | 9.290000 | 9.890000 | 93.000000 | 1018.000000 |  | 10.370000 | 0.000000 | 10000.000000 | 300.000000 | 1.38 | 0.830000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 03:00:00 | 95.000000 | 8.300000 | 9.370000 | 93.000000 | 1018.000000 | 0.82 | 9.370000 | 0.000000 | 10000.000000 | 299.000000 | 1.47 | 0.950000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 04:00:00 | 91.000000 | 7.150000 | 8.370000 | 92.000000 | 1018.000000 |  | 8.370000 | 0.000000 | 10000.000000 | 293.000000 | 1.18 | 0.360000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 05:00:00 | 85.000000 | 7.460000 | 8.370000 | 94.000000 | 1018.000000 | 0.82 | 8.370000 | 0.000000 | 10000.000000 | 273.000000 | 1.25 | 0.630000 | 500 | Rain | light rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 06:00:00 | 82.000000 | 6.470000 | 7.370000 | 94.000000 | 1018.000000 |  | 7.370000 | 0.000000 | 10000.000000 | 225.000000 | 1.2 | 0.420000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 07:00:00 | 34.000000 | 6.470000 | 7.370000 | 94.000000 | 1018.000000 |  | 7.370000 | 0.000000 | 10000.000000 | 256.000000 | 1.7 | 0.720000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 08:00:00 | 34.000000 | 4.330000 | 5.370000 | 93.000000 | 1017.000000 |  | 5.370000 | 0.000000 | 10000.000000 | 258.000000 | 1.9 | 0.950000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 09:00:00 | 40.000000 | 3.190000 | 4.370000 | 92.000000 | 1017.000000 |  | 4.370000 | 0.000000 | 10000.000000 | 257.000000 | 1.54 | 0.630000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 10:00:00 | 36.000000 | 2.200000 | 3.370000 | 92.000000 | 1018.000000 |  | 3.370000 | 0.000000 | 10000.000000 | 255.000000 | 2.16 | 0.980000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 11:00:00 | 33.000000 | 1.050000 | 2.370000 | 91.000000 | 1019.000000 |  | 2.370000 | 0.000000 | 10000.000000 | 251.000000 | 2.24 | 0.880000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 12:00:00 | 15.000000 | 1.250000 | 3.370000 | 86.000000 | 1019.000000 |  | 3.370000 | 0.550000 | 10000.000000 | 251.000000 | 2.2 | 0.620000 | 801 | Clouds | few clouds | 02d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 13:00:00 | 23.000000 | 2.660000 | 7.370000 | 72.000000 | 1018.000000 |  | 7.370000 | 2.370000 | 10000.000000 | 301.000000 | 1.66 | 0.880000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 14:00:00 | 12.000000 | 4.810000 | 10.230000 | 64.000000 | 1017.000000 |  | 11.370000 | 5.600000 | 10000.000000 | 315.000000 | 2.13 | 1.230000 | 801 | Clouds | few clouds | 02d | 14 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 15:00:00 | 12.000000 | 5.970000 | 13.350000 | 57.000000 | 1016.000000 |  | 14.370000 | 9.420000 | 10000.000000 | 324.000000 | 2.49 | 1.330000 | 801 | Clouds | few clouds | 02d | 15 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 16:00:00 | 13.000000 | 6.120000 | 14.370000 | 54.000000 | 1015.000000 |  | 15.370000 | 12.550000 | 10000.000000 | 333.000000 | 2.89 | 1.160000 | 801 | Clouds | few clouds | 02d | 16 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 17:00:00 | 15.000000 | 8.250000 | 16.600000 | 55.000000 | 1014.000000 |  | 17.370000 | 13.660000 | 10000.000000 | 330.000000 | 3.14 | 1.200000 | 801 | Clouds | few clouds | 02d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 18:00:00 | 49.000000 | 8.350000 | 15.600000 | 59.000000 | 1013.000000 | 0.12 | 16.370000 | 12.400000 | 10000.000000 | 331.000000 | 2.99 | 1.150000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 19:00:00 | 65.000000 | 10.730000 | 16.860000 | 65.000000 | 1012.000000 | 0.26 | 17.370000 | 9.060000 | 10000.000000 | 334.000000 | 2.79 | 0.800000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 20:00:00 | 80.000000 | 11.730000 | 15.990000 | 74.000000 | 1012.000000 | 0.36 | 16.370000 | 5.280000 | 10000.000000 | 344.000000 | 2.5 | 0.580000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 21:00:00 | 87.000000 | 12.920000 | 16.150000 | 80.000000 | 1013.000000 | 0.3 | 16.370000 | 2.160000 | 10000.000000 | 333.000000 | 2.24 | 0.470000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 22:00:00 | 90.000000 | 13.040000 | 15.210000 | 86.000000 | 1014.000000 | 0.25 | 15.370000 | 0.450000 | 9086.000000 | 332.000000 | 2.09 | 0.350000 | 500 | Rain | light rain | 10d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020350 | "BETANIA [35020350]" | 4.218889 | -74.146861 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 23:00:00 | 92.000000 | 12.260000 | 13.190000 | 93.000000 | 1015.000000 |  | 13.370000 | 0.000000 | 10000.000000 | 312.000000 | 1.18 | 0.360000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35020350_OWM_Clouds_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Clouds_20220130.png)
![CNE_IDEAM_Station35020350_OWM_Dewpoint_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Dewpoint_20220130.png)
![CNE_IDEAM_Station35020350_OWM_Feelslike_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Feelslike_20220130.png)
![CNE_IDEAM_Station35020350_OWM_Humidity_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Humidity_20220130.png)
![CNE_IDEAM_Station35020350_OWM_Pressure_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Pressure_20220130.png)
![CNE_IDEAM_Station35020350_OWM_Rain_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Rain_20220130.png)
![CNE_IDEAM_Station35020350_OWM_Temp_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Temp_20220130.png)
![CNE_IDEAM_Station35020350_OWM_UVI_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_UVI_20220130.png)
![CNE_IDEAM_Station35020350_OWM_Visibility_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Visibility_20220130.png)
![CNE_IDEAM_Station35020350_OWM_Winddeg_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Winddeg_20220130.png)
![CNE_IDEAM_Station35020350_OWM_Windgust_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Windgust_20220130.png)
![CNE_IDEAM_Station35020350_OWM_Windspeed_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020350_OWM_Windspeed_20220130.png)

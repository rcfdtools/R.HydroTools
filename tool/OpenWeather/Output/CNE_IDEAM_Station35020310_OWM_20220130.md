
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35020310_OWM_20220130.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220130.csv)

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

### (CNE index 1856) Open Weather values for station 35020310 - NAZARETH [35020310]

JSON data from API OWM:

```
{'lat': 4.1723, 'lon': -74.146, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643467037, 'sunrise': 1643454691, 'sunset': 1643497664, 'temp': 13.9, 'feels_like': 12.83, 'pressure': 1016, 'humidity': 57, 'dew_point': 5.53, 'uvi': 9.42, 'clouds': 15, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 328, 'wind_gust': 2.58, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, 'hourly': [{'dt': 1643414400, 'temp': 13.9, 'feels_like': 13.77, 'pressure': 1016, 'humidity': 93, 'dew_point': 12.79, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 57, 'wind_gust': 1.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.64}}, {'dt': 1643418000, 'temp': 13.9, 'feels_like': 13.75, 'pressure': 1017, 'humidity': 92, 'dew_point': 12.62, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 9, 'wind_gust': 1.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.56}}, {'dt': 1643421600, 'temp': 12.9, 'feels_like': 12.67, 'pressure': 1018, 'humidity': 93, 'dew_point': 11.8, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 305, 'wind_gust': 1.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643425200, 'temp': 11.9, 'feels_like': 11.57, 'pressure': 1018, 'humidity': 93, 'dew_point': 10.81, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 301, 'wind_gust': 1.48, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.74}}, {'dt': 1643428800, 'temp': 10.9, 'feels_like': 10.45, 'pressure': 1018, 'humidity': 92, 'dew_point': 9.65, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 294, 'wind_gust': 1.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643432400, 'temp': 10.9, 'feels_like': 10.5, 'pressure': 1018, 'humidity': 94, 'dew_point': 9.97, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 280, 'wind_gust': 1.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.78}}, {'dt': 1643436000, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1018, 'humidity': 94, 'dew_point': 8.98, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 246, 'wind_gust': 1.13, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643439600, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1017, 'humidity': 93, 'dew_point': 8.82, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 274, 'wind_gust': 1.73, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643443200, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1017, 'humidity': 93, 'dew_point': 6.84, 'uvi': 0, 'clouds': 37, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 273, 'wind_gust': 1.88, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643446800, 'temp': 6.9, 'feels_like': 6.9, 'pressure': 1017, 'humidity': 92, 'dew_point': 5.69, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 276, 'wind_gust': 1.55, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643450400, 'temp': 5.9, 'feels_like': 5.9, 'pressure': 1018, 'humidity': 92, 'dew_point': 4.7, 'uvi': 0, 'clouds': 37, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 273, 'wind_gust': 2.13, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643454000, 'temp': 4.9, 'feels_like': 4.9, 'pressure': 1019, 'humidity': 91, 'dew_point': 3.56, 'uvi': 0, 'clouds': 35, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 271, 'wind_gust': 2.2, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643457600, 'temp': 5.9, 'feels_like': 5.9, 'pressure': 1019, 'humidity': 86, 'dew_point': 3.74, 'uvi': 0.55, 'clouds': 24, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 272, 'wind_gust': 2.13, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643461200, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1018, 'humidity': 72, 'dew_point': 5.1, 'uvi': 2.37, 'clouds': 31, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 307, 'wind_gust': 1.79, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643464800, 'temp': 13.9, 'feels_like': 13.02, 'pressure': 1017, 'humidity': 64, 'dew_point': 7.21, 'uvi': 5.6, 'clouds': 17, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 319, 'wind_gust': 2.23, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643468400, 'temp': 16.9, 'feels_like': 16.13, 'pressure': 1016, 'humidity': 57, 'dew_point': 8.34, 'uvi': 9.42, 'clouds': 15, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 328, 'wind_gust': 2.58, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643472000, 'temp': 17.9, 'feels_like': 17.16, 'pressure': 1015, 'humidity': 54, 'dew_point': 8.47, 'uvi': 12.55, 'clouds': 17, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 337, 'wind_gust': 2.91, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643475600, 'temp': 19.9, 'feels_like': 19.38, 'pressure': 1014, 'humidity': 55, 'dew_point': 10.6, 'uvi': 13.66, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 334, 'wind_gust': 3.14, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643479200, 'temp': 18.9, 'feels_like': 18.39, 'pressure': 1013, 'humidity': 59, 'dew_point': 10.72, 'uvi': 12.4, 'clouds': 58, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 335, 'wind_gust': 3.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1643482800, 'temp': 19.9, 'feels_like': 19.64, 'pressure': 1012, 'humidity': 65, 'dew_point': 13.13, 'uvi': 9.06, 'clouds': 72, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 340, 'wind_gust': 2.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1643486400, 'temp': 18.9, 'feels_like': 18.75, 'pressure': 1012, 'humidity': 73, 'dew_point': 13.96, 'uvi': 5.28, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 343, 'wind_gust': 2.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1643490000, 'temp': 18.9, 'feels_like': 18.91, 'pressure': 1013, 'humidity': 79, 'dew_point': 15.18, 'uvi': 2.16, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 334, 'wind_gust': 2.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1643493600, 'temp': 17.9, 'feels_like': 17.97, 'pressure': 1014, 'humidity': 85, 'dew_point': 15.34, 'uvi': 0.45, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 331, 'wind_gust': 2.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.25}}, {'dt': 1643497200, 'temp': 15.9, 'feels_like': 15.97, 'pressure': 1015, 'humidity': 93, 'dew_point': 14.77, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 320, 'wind_gust': 1.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 00:00:00 | 91.000000 | 12.790000 | 13.770000 | 93.000000 | 1016.000000 | 0.64 | 13.900000 | 0.000000 | 10000.000000 | 57.000000 | 1.21 | 0.470000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 01:00:00 | 98.000000 | 12.620000 | 13.750000 | 92.000000 | 1017.000000 | 0.56 | 13.900000 | 0.000000 | 10000.000000 | 9.000000 | 1.23 | 0.480000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 02:00:00 | 90.000000 | 11.800000 | 12.670000 | 93.000000 | 1018.000000 |  | 12.900000 | 0.000000 | 10000.000000 | 305.000000 | 1.41 | 0.880000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 03:00:00 | 96.000000 | 10.810000 | 11.570000 | 93.000000 | 1018.000000 | 0.74 | 11.900000 | 0.000000 | 10000.000000 | 301.000000 | 1.48 | 1.060000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 04:00:00 | 91.000000 | 9.650000 | 10.450000 | 92.000000 | 1018.000000 |  | 10.900000 | 0.000000 | 10000.000000 | 294.000000 | 1.24 | 0.590000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 05:00:00 | 86.000000 | 9.970000 | 10.500000 | 94.000000 | 1018.000000 | 0.78 | 10.900000 | 0.000000 | 10000.000000 | 280.000000 | 1.26 | 0.730000 | 500 | Rain | light rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 06:00:00 | 83.000000 | 8.980000 | 9.900000 | 94.000000 | 1018.000000 |  | 9.900000 | 0.000000 | 10000.000000 | 246.000000 | 1.13 | 0.410000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 07:00:00 | 40.000000 | 8.820000 | 9.900000 | 93.000000 | 1017.000000 |  | 9.900000 | 0.000000 | 10000.000000 | 274.000000 | 1.73 | 0.920000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 08:00:00 | 37.000000 | 6.840000 | 7.900000 | 93.000000 | 1017.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 273.000000 | 1.88 | 1.120000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 09:00:00 | 44.000000 | 5.690000 | 6.900000 | 92.000000 | 1017.000000 |  | 6.900000 | 0.000000 | 10000.000000 | 276.000000 | 1.55 | 0.690000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 10:00:00 | 37.000000 | 4.700000 | 5.900000 | 92.000000 | 1018.000000 |  | 5.900000 | 0.000000 | 10000.000000 | 273.000000 | 2.13 | 1.130000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 11:00:00 | 35.000000 | 3.560000 | 4.900000 | 91.000000 | 1019.000000 |  | 4.900000 | 0.000000 | 10000.000000 | 271.000000 | 2.2 | 1.030000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 12:00:00 | 24.000000 | 3.740000 | 5.900000 | 86.000000 | 1019.000000 |  | 5.900000 | 0.550000 | 10000.000000 | 272.000000 | 2.13 | 0.720000 | 801 | Clouds | few clouds | 02d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 13:00:00 | 31.000000 | 5.100000 | 9.900000 | 72.000000 | 1018.000000 |  | 9.900000 | 2.370000 | 10000.000000 | 307.000000 | 1.79 | 0.960000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 14:00:00 | 17.000000 | 7.210000 | 13.020000 | 64.000000 | 1017.000000 |  | 13.900000 | 5.600000 | 10000.000000 | 319.000000 | 2.23 | 1.160000 | 801 | Clouds | few clouds | 02d | 14 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 15:00:00 | 15.000000 | 8.340000 | 16.130000 | 57.000000 | 1016.000000 |  | 16.900000 | 9.420000 | 10000.000000 | 328.000000 | 2.58 | 1.270000 | 801 | Clouds | few clouds | 02d | 15 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 16:00:00 | 17.000000 | 8.470000 | 17.160000 | 54.000000 | 1015.000000 |  | 17.900000 | 12.550000 | 10000.000000 | 337.000000 | 2.91 | 1.070000 | 801 | Clouds | few clouds | 02d | 16 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 17:00:00 | 20.000000 | 10.600000 | 19.380000 | 55.000000 | 1014.000000 |  | 19.900000 | 13.660000 | 10000.000000 | 334.000000 | 3.14 | 1.080000 | 801 | Clouds | few clouds | 02d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 18:00:00 | 58.000000 | 10.720000 | 18.390000 | 59.000000 | 1013.000000 | 0.12 | 18.900000 | 12.400000 | 10000.000000 | 335.000000 | 3.01 | 1.040000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 19:00:00 | 72.000000 | 13.130000 | 19.640000 | 65.000000 | 1012.000000 | 0.29 | 19.900000 | 9.060000 | 10000.000000 | 340.000000 | 2.75 | 0.740000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 20:00:00 | 85.000000 | 13.960000 | 18.750000 | 73.000000 | 1012.000000 | 0.38 | 18.900000 | 5.280000 | 10000.000000 | 343.000000 | 2.46 | 0.610000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 21:00:00 | 90.000000 | 15.180000 | 18.910000 | 79.000000 | 1013.000000 | 0.33 | 18.900000 | 2.160000 | 10000.000000 | 334.000000 | 2.23 | 0.570000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 22:00:00 | 92.000000 | 15.340000 | 17.970000 | 85.000000 | 1014.000000 | 0.25 | 17.900000 | 0.450000 | 10000.000000 | 331.000000 | 2.1 | 0.520000 | 500 | Rain | light rain | 10d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35020310 | "NAZARETH [35020310]" | 4.172250 | -74.146000 | 2800.000000 | Pluviográfica | Convencional | Activa | 1984-07-15 00:00:00 | NaT | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 23:00:00 | 94.000000 | 14.770000 | 15.970000 | 93.000000 | 1015.000000 |  | 15.900000 | 0.000000 | 10000.000000 | 320.000000 | 1.41 | 0.640000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station35020310_OWM_Clouds_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Clouds_20220130.png)
![CNE_IDEAM_Station35020310_OWM_Dewpoint_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Dewpoint_20220130.png)
![CNE_IDEAM_Station35020310_OWM_Feelslike_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Feelslike_20220130.png)
![CNE_IDEAM_Station35020310_OWM_Humidity_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Humidity_20220130.png)
![CNE_IDEAM_Station35020310_OWM_Pressure_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Pressure_20220130.png)
![CNE_IDEAM_Station35020310_OWM_Rain_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Rain_20220130.png)
![CNE_IDEAM_Station35020310_OWM_Temp_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Temp_20220130.png)
![CNE_IDEAM_Station35020310_OWM_UVI_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_UVI_20220130.png)
![CNE_IDEAM_Station35020310_OWM_Visibility_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Visibility_20220130.png)
![CNE_IDEAM_Station35020310_OWM_Winddeg_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Winddeg_20220130.png)
![CNE_IDEAM_Station35020310_OWM_Windgust_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Windgust_20220130.png)
![CNE_IDEAM_Station35020310_OWM_Windspeed_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35020310_OWM_Windspeed_20220130.png)

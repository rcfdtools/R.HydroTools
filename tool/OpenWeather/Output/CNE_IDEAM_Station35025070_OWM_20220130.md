
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - TAQUES LOS [35025070] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35025070_OWM_20220130.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220130.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.19666667,-74.19094444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.19666667&lon=-74.19094444)

| Parameter | Value |
|---|---|
| Code | 35025070 |
| Name | TAQUES LOS [35025070] |
| Latitude, ° | 4.19666667 |
| Longitude, ° | -74.19094444 |
| Elevation, m | 3150 |
| Category | Pluviométrica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1986-01-14 19:00:00 |
| Suspension date | NaT |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | 0 |
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

### (CNE index 1866) Open Weather values for station 35025070 - TAQUES LOS [35025070]

JSON data from API OWM:

```
{'lat': 4.1967, 'lon': -74.1909, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643467037, 'sunrise': 1643454704, 'sunset': 1643497673, 'temp': 9.57, 'feels_like': 8.78, 'pressure': 1017, 'humidity': 61, 'dew_point': 2.43, 'uvi': 9.42, 'clouds': 14, 'visibility': 10000, 'wind_speed': 1.89, 'wind_deg': 308, 'wind_gust': 2.43, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, 'hourly': [{'dt': 1643414400, 'temp': 9.57, 'feels_like': 9.57, 'pressure': 1016, 'humidity': 94, 'dew_point': 8.65, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 65, 'wind_gust': 1.33, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.92}}, {'dt': 1643418000, 'temp': 9.57, 'feels_like': 9.57, 'pressure': 1017, 'humidity': 92, 'dew_point': 8.34, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 29, 'wind_gust': 1.37, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.79}}, {'dt': 1643421600, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1018, 'humidity': 94, 'dew_point': 7.66, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 313, 'wind_gust': 1.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643425200, 'temp': 7.57, 'feels_like': 7.57, 'pressure': 1018, 'humidity': 93, 'dew_point': 6.51, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 308, 'wind_gust': 1.49, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.98}}, {'dt': 1643428800, 'temp': 6.57, 'feels_like': 6.57, 'pressure': 1018, 'humidity': 93, 'dew_point': 5.52, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 294, 'wind_gust': 1.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643432400, 'temp': 6.57, 'feels_like': 6.57, 'pressure': 1018, 'humidity': 94, 'dew_point': 5.67, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 280, 'wind_gust': 1.29, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.02}}, {'dt': 1643436000, 'temp': 5.57, 'feels_like': 5.57, 'pressure': 1018, 'humidity': 94, 'dew_point': 4.68, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 189, 'wind_gust': 1.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643439600, 'temp': 5.57, 'feels_like': 5.57, 'pressure': 1018, 'humidity': 94, 'dew_point': 4.68, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 251, 'wind_gust': 1.62, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643443200, 'temp': 3.57, 'feels_like': 3.57, 'pressure': 1017, 'humidity': 94, 'dew_point': 2.7, 'uvi': 0, 'clouds': 41, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 255, 'wind_gust': 1.69, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643446800, 'temp': 2.57, 'feels_like': 2.57, 'pressure': 1017, 'humidity': 92, 'dew_point': 1.4, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 258, 'wind_gust': 1.47, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643450400, 'temp': 1.57, 'feels_like': 1.57, 'pressure': 1018, 'humidity': 93, 'dew_point': 0.56, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 253, 'wind_gust': 1.88, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643454000, 'temp': 0.57, 'feels_like': 0.57, 'pressure': 1019, 'humidity': 92, 'dew_point': -0.51, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 242, 'wind_gust': 1.98, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643457600, 'temp': 1.57, 'feels_like': 1.57, 'pressure': 1019, 'humidity': 87, 'dew_point': -0.31, 'uvi': 0.55, 'clouds': 17, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 239, 'wind_gust': 2.03, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643461200, 'temp': 5.57, 'feels_like': 5.57, 'pressure': 1018, 'humidity': 75, 'dew_point': 1.5, 'uvi': 2.37, 'clouds': 25, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 297, 'wind_gust': 1.57, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643464800, 'temp': 9.57, 'feels_like': 9.04, 'pressure': 1018, 'humidity': 68, 'dew_point': 3.96, 'uvi': 5.6, 'clouds': 13, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 304, 'wind_gust': 2.12, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643468400, 'temp': 12.57, 'feels_like': 11.48, 'pressure': 1017, 'humidity': 61, 'dew_point': 5.26, 'uvi': 9.42, 'clouds': 14, 'visibility': 10000, 'wind_speed': 1.89, 'wind_deg': 308, 'wind_gust': 2.43, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643472000, 'temp': 13.57, 'feels_like': 12.47, 'pressure': 1016, 'humidity': 57, 'dew_point': 5.22, 'uvi': 12.55, 'clouds': 16, 'visibility': 10000, 'wind_speed': 1.9, 'wind_deg': 309, 'wind_gust': 2.77, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643475600, 'temp': 15.57, 'feels_like': 14.7, 'pressure': 1014, 'humidity': 58, 'dew_point': 7.35, 'uvi': 13.66, 'clouds': 18, 'visibility': 10000, 'wind_speed': 2.05, 'wind_deg': 308, 'wind_gust': 3.03, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643479200, 'temp': 14.57, 'feels_like': 13.7, 'pressure': 1013, 'humidity': 62, 'dew_point': 7.38, 'uvi': 12.4, 'clouds': 62, 'visibility': 10000, 'wind_speed': 2.02, 'wind_deg': 308, 'wind_gust': 2.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1643482800, 'temp': 15.57, 'feels_like': 14.98, 'pressure': 1013, 'humidity': 69, 'dew_point': 9.91, 'uvi': 9.06, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.63, 'wind_deg': 306, 'wind_gust': 2.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.32}}, {'dt': 1643486400, 'temp': 14.57, 'feels_like': 14.12, 'pressure': 1013, 'humidity': 78, 'dew_point': 10.78, 'uvi': 5.28, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 309, 'wind_gust': 2.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.45}}, {'dt': 1643490000, 'temp': 14.57, 'feels_like': 14.25, 'pressure': 1013, 'humidity': 83, 'dew_point': 11.72, 'uvi': 2.16, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 306, 'wind_gust': 2.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1643493600, 'temp': 13.57, 'feels_like': 13.31, 'pressure': 1014, 'humidity': 89, 'dew_point': 11.79, 'uvi': 0.45, 'clouds': 93, 'visibility': 7164, 'wind_speed': 0.94, 'wind_deg': 304, 'wind_gust': 2.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.3}}, {'dt': 1643497200, 'temp': 11.57, 'feels_like': 11.24, 'pressure': 1015, 'humidity': 94, 'dew_point': 10.64, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 305, 'wind_gust': 1.36, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 00:00:00 | 92.000000 | 8.650000 | 9.570000 | 94.000000 | 1016.000000 | 0.92 | 9.570000 | 0.000000 | 10000.000000 | 65.000000 | 1.33 | 0.860000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 01:00:00 | 97.000000 | 8.340000 | 9.570000 | 92.000000 | 1017.000000 | 0.79 | 9.570000 | 0.000000 | 10000.000000 | 29.000000 | 1.37 | 0.730000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 02:00:00 | 93.000000 | 7.660000 | 8.570000 | 94.000000 | 1018.000000 |  | 8.570000 | 0.000000 | 10000.000000 | 313.000000 | 1.5 | 0.890000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 03:00:00 | 97.000000 | 6.510000 | 7.570000 | 93.000000 | 1018.000000 | 0.98 | 7.570000 | 0.000000 | 10000.000000 | 308.000000 | 1.49 | 0.940000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 04:00:00 | 94.000000 | 5.520000 | 6.570000 | 93.000000 | 1018.000000 |  | 6.570000 | 0.000000 | 10000.000000 | 294.000000 | 1.3 | 0.410000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 05:00:00 | 89.000000 | 5.670000 | 6.570000 | 94.000000 | 1018.000000 | 1.02 | 6.570000 | 0.000000 | 10000.000000 | 280.000000 | 1.29 | 0.450000 | 501 | Rain | moderate rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 06:00:00 | 85.000000 | 4.680000 | 5.570000 | 94.000000 | 1018.000000 |  | 5.570000 | 0.000000 | 10000.000000 | 189.000000 | 1.16 | 0.210000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 07:00:00 | 43.000000 | 4.680000 | 5.570000 | 94.000000 | 1018.000000 |  | 5.570000 | 0.000000 | 10000.000000 | 251.000000 | 1.62 | 0.410000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 08:00:00 | 41.000000 | 2.700000 | 3.570000 | 94.000000 | 1017.000000 |  | 3.570000 | 0.000000 | 10000.000000 | 255.000000 | 1.69 | 0.630000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 09:00:00 | 43.000000 | 1.400000 | 2.570000 | 92.000000 | 1017.000000 |  | 2.570000 | 0.000000 | 10000.000000 | 258.000000 | 1.47 | 0.280000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 10:00:00 | 43.000000 | 0.560000 | 1.570000 | 93.000000 | 1018.000000 |  | 1.570000 | 0.000000 | 10000.000000 | 253.000000 | 1.88 | 0.600000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 11:00:00 | 40.000000 | -0.510000 | 0.570000 | 92.000000 | 1019.000000 |  | 0.570000 | 0.000000 | 10000.000000 | 242.000000 | 1.98 | 0.470000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 12:00:00 | 17.000000 | -0.310000 | 1.570000 | 87.000000 | 1019.000000 |  | 1.570000 | 0.550000 | 10000.000000 | 239.000000 | 2.03 | 0.300000 | 801 | Clouds | few clouds | 02d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 13:00:00 | 25.000000 | 1.500000 | 5.570000 | 75.000000 | 1018.000000 |  | 5.570000 | 2.370000 | 10000.000000 | 297.000000 | 1.57 | 0.950000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 14:00:00 | 13.000000 | 3.960000 | 9.040000 | 68.000000 | 1018.000000 |  | 9.570000 | 5.600000 | 10000.000000 | 304.000000 | 2.12 | 1.620000 | 801 | Clouds | few clouds | 02d | 14 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 15:00:00 | 14.000000 | 5.260000 | 11.480000 | 61.000000 | 1017.000000 |  | 12.570000 | 9.420000 | 10000.000000 | 308.000000 | 2.43 | 1.890000 | 801 | Clouds | few clouds | 02d | 15 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 16:00:00 | 16.000000 | 5.220000 | 12.470000 | 57.000000 | 1016.000000 |  | 13.570000 | 12.550000 | 10000.000000 | 309.000000 | 2.77 | 1.900000 | 801 | Clouds | few clouds | 02d | 16 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 17:00:00 | 18.000000 | 7.350000 | 14.700000 | 58.000000 | 1014.000000 |  | 15.570000 | 13.660000 | 10000.000000 | 308.000000 | 3.03 | 2.050000 | 801 | Clouds | few clouds | 02d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 18:00:00 | 62.000000 | 7.380000 | 13.700000 | 62.000000 | 1013.000000 | 0.14 | 14.570000 | 12.400000 | 10000.000000 | 308.000000 | 2.92 | 2.020000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 19:00:00 | 76.000000 | 9.910000 | 14.980000 | 69.000000 | 1013.000000 | 0.32 | 15.570000 | 9.060000 | 10000.000000 | 306.000000 | 2.71 | 1.630000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 20:00:00 | 87.000000 | 10.780000 | 14.120000 | 78.000000 | 1013.000000 | 0.45 | 14.570000 | 5.280000 | 10000.000000 | 309.000000 | 2.54 | 1.280000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 21:00:00 | 91.000000 | 11.720000 | 14.250000 | 83.000000 | 1013.000000 | 0.36 | 14.570000 | 2.160000 | 10000.000000 | 306.000000 | 2.27 | 1.170000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 22:00:00 | 93.000000 | 11.790000 | 13.310000 | 89.000000 | 1014.000000 | 0.3 | 13.570000 | 0.450000 | 7164.000000 | 304.000000 | 2.12 | 0.940000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025070 | "TAQUES LOS [35025070]" | 4.196667 | -74.190944 | 3150.000000 | Pluviométrica | Convencional | Activa | 1986-01-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-29 23:00:00 | 95.000000 | 10.640000 | 11.240000 | 94.000000 | 1015.000000 | 0.11 | 11.570000 | 0.000000 | 10000.000000 | 305.000000 | 1.36 | 0.710000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station35025070_OWM_Clouds_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Clouds_20220130.png)
![CNE_IDEAM_Station35025070_OWM_Dewpoint_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Dewpoint_20220130.png)
![CNE_IDEAM_Station35025070_OWM_Feelslike_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Feelslike_20220130.png)
![CNE_IDEAM_Station35025070_OWM_Humidity_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Humidity_20220130.png)
![CNE_IDEAM_Station35025070_OWM_Pressure_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Pressure_20220130.png)
![CNE_IDEAM_Station35025070_OWM_Rain_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Rain_20220130.png)
![CNE_IDEAM_Station35025070_OWM_Temp_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Temp_20220130.png)
![CNE_IDEAM_Station35025070_OWM_UVI_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_UVI_20220130.png)
![CNE_IDEAM_Station35025070_OWM_Visibility_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Visibility_20220130.png)
![CNE_IDEAM_Station35025070_OWM_Winddeg_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Winddeg_20220130.png)
![CNE_IDEAM_Station35025070_OWM_Windgust_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Windgust_20220130.png)
![CNE_IDEAM_Station35025070_OWM_Windspeed_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025070_OWM_Windspeed_20220130.png)

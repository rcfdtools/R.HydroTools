
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - VILLA TERESA - AUT [21206920] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206920_OWM_20220130.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220130.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.35,-74.15) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.35&lon=-74.15)

| Parameter | Value |
|---|---|
| Code | 21206920 |
| Name | VILLA TERESA - AUT [21206920] |
| Latitude, ° | 4.35 |
| Longitude, ° | -74.15 |
| Elevation, m | 3624 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-07-19 00:00:00 |
| Suspension date | NaT |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Guatiquia |
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

### (CNE index 86) Open Weather values for station 21206920 - VILLA TERESA - AUT [21206920]

JSON data from API OWM:

```
{'lat': 4.35, 'lon': -74.15, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643467037, 'sunrise': 1643454706, 'sunset': 1643497651, 'temp': 8.9, 'feels_like': 8.05, 'pressure': 1016, 'humidity': 56, 'dew_point': 0.61, 'uvi': 9.42, 'clouds': 8, 'visibility': 10000, 'wind_speed': 1.84, 'wind_deg': 312, 'wind_gust': 2.36, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, 'hourly': [{'dt': 1643414400, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1015, 'humidity': 91, 'dew_point': 7.51, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 76, 'wind_gust': 1.36, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.96}}, {'dt': 1643418000, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1016, 'humidity': 90, 'dew_point': 7.35, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 42, 'wind_gust': 1.48, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.76}}, {'dt': 1643421600, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1017, 'humidity': 92, 'dew_point': 6.68, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 316, 'wind_gust': 1.25, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643425200, 'temp': 6.9, 'feels_like': 6.9, 'pressure': 1018, 'humidity': 90, 'dew_point': 5.38, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 310, 'wind_gust': 1.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.71}}, {'dt': 1643428800, 'temp': 5.9, 'feels_like': 5.9, 'pressure': 1017, 'humidity': 91, 'dew_point': 4.55, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 281, 'wind_gust': 1.18, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643432400, 'temp': 5.9, 'feels_like': 5.9, 'pressure': 1017, 'humidity': 92, 'dew_point': 4.7, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 280, 'wind_gust': 1.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.63}}, {'dt': 1643436000, 'temp': 4.9, 'feels_like': 4.9, 'pressure': 1017, 'humidity': 92, 'dew_point': 3.71, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 233, 'wind_gust': 1.08, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643439600, 'temp': 4.9, 'feels_like': 4.9, 'pressure': 1017, 'humidity': 93, 'dew_point': 3.86, 'uvi': 0, 'clouds': 30, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 233, 'wind_gust': 1.62, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643443200, 'temp': 2.9, 'feels_like': 2.9, 'pressure': 1017, 'humidity': 93, 'dew_point': 1.88, 'uvi': 0, 'clouds': 28, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 251, 'wind_gust': 1.84, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643446800, 'temp': 1.9, 'feels_like': 1.9, 'pressure': 1016, 'humidity': 92, 'dew_point': 0.74, 'uvi': 0, 'clouds': 32, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 252, 'wind_gust': 1.38, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643450400, 'temp': 0.9, 'feels_like': 0.9, 'pressure': 1017, 'humidity': 92, 'dew_point': -0.22, 'uvi': 0, 'clouds': 29, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 251, 'wind_gust': 1.98, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643454000, 'temp': -0.1, 'feels_like': -0.1, 'pressure': 1018, 'humidity': 91, 'dew_point': -1.24, 'uvi': 0, 'clouds': 26, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 250, 'wind_gust': 2.01, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643457600, 'temp': 0.9, 'feels_like': 0.9, 'pressure': 1018, 'humidity': 86, 'dew_point': -1.03, 'uvi': 0.55, 'clouds': 7, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 253, 'wind_gust': 2.11, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643461200, 'temp': 4.9, 'feels_like': 4.9, 'pressure': 1018, 'humidity': 73, 'dew_point': 0.47, 'uvi': 2.37, 'clouds': 14, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 293, 'wind_gust': 1.64, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643464800, 'temp': 8.9, 'feels_like': 8.23, 'pressure': 1017, 'humidity': 64, 'dew_point': 2.47, 'uvi': 5.6, 'clouds': 7, 'visibility': 10000, 'wind_speed': 1.66, 'wind_deg': 307, 'wind_gust': 2.11, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643468400, 'temp': 11.9, 'feels_like': 10.61, 'pressure': 1016, 'humidity': 56, 'dew_point': 3.41, 'uvi': 9.42, 'clouds': 8, 'visibility': 10000, 'wind_speed': 1.84, 'wind_deg': 312, 'wind_gust': 2.36, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643472000, 'temp': 12.9, 'feels_like': 11.6, 'pressure': 1015, 'humidity': 52, 'dew_point': 3.29, 'uvi': 12.55, 'clouds': 8, 'visibility': 10000, 'wind_speed': 1.85, 'wind_deg': 317, 'wind_gust': 2.72, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643475600, 'temp': 14.9, 'feels_like': 13.8, 'pressure': 1014, 'humidity': 52, 'dew_point': 5.14, 'uvi': 13.66, 'clouds': 11, 'visibility': 10000, 'wind_speed': 2.03, 'wind_deg': 316, 'wind_gust': 2.98, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643479200, 'temp': 13.9, 'feels_like': 12.78, 'pressure': 1013, 'humidity': 55, 'dew_point': 5.02, 'uvi': 12.4, 'clouds': 38, 'visibility': 10000, 'wind_speed': 2.03, 'wind_deg': 314, 'wind_gust': 2.91, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643482800, 'temp': 14.9, 'feels_like': 13.96, 'pressure': 1012, 'humidity': 58, 'dew_point': 6.72, 'uvi': 9.06, 'clouds': 47, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 312, 'wind_gust': 2.84, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1643486400, 'temp': 13.9, 'feels_like': 13.02, 'pressure': 1011, 'humidity': 64, 'dew_point': 7.21, 'uvi': 5.28, 'clouds': 55, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 307, 'wind_gust': 2.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1643490000, 'temp': 13.9, 'feels_like': 13.2, 'pressure': 1012, 'humidity': 71, 'dew_point': 8.74, 'uvi': 2.16, 'clouds': 68, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 299, 'wind_gust': 2.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1643493600, 'temp': 12.9, 'feels_like': 12.36, 'pressure': 1013, 'humidity': 81, 'dew_point': 9.72, 'uvi': 0.45, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 297, 'wind_gust': 2.07, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1643497200, 'temp': 10.9, 'feels_like': 10.42, 'pressure': 1015, 'humidity': 91, 'dew_point': 9.49, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 301, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 00:00:00 | 93.000000 | 7.510000 | 8.900000 | 91.000000 | 1015.000000 | 0.96 | 8.900000 | 0.000000 | 10000.000000 | 76.000000 | 1.36 | 0.610000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 01:00:00 | 99.000000 | 7.350000 | 8.900000 | 90.000000 | 1016.000000 | 0.76 | 8.900000 | 0.000000 | 10000.000000 | 42.000000 | 1.48 | 0.650000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 02:00:00 | 73.000000 | 6.680000 | 7.900000 | 92.000000 | 1017.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 316.000000 | 1.25 | 0.570000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 03:00:00 | 89.000000 | 5.380000 | 6.900000 | 90.000000 | 1018.000000 | 0.71 | 6.900000 | 0.000000 | 10000.000000 | 310.000000 | 1.21 | 0.560000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 04:00:00 | 80.000000 | 4.550000 | 5.900000 | 91.000000 | 1017.000000 |  | 5.900000 | 0.000000 | 10000.000000 | 281.000000 | 1.18 | 0.280000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 05:00:00 | 85.000000 | 4.700000 | 5.900000 | 92.000000 | 1017.000000 | 0.63 | 5.900000 | 0.000000 | 10000.000000 | 280.000000 | 1.23 | 0.520000 | 500 | Rain | light rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 06:00:00 | 81.000000 | 3.710000 | 4.900000 | 92.000000 | 1017.000000 |  | 4.900000 | 0.000000 | 10000.000000 | 233.000000 | 1.08 | 0.320000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 07:00:00 | 30.000000 | 3.860000 | 4.900000 | 93.000000 | 1017.000000 |  | 4.900000 | 0.000000 | 10000.000000 | 233.000000 | 1.62 | 0.600000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 08:00:00 | 28.000000 | 1.880000 | 2.900000 | 93.000000 | 1017.000000 |  | 2.900000 | 0.000000 | 10000.000000 | 251.000000 | 1.84 | 0.700000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 09:00:00 | 32.000000 | 0.740000 | 1.900000 | 92.000000 | 1016.000000 |  | 1.900000 | 0.000000 | 10000.000000 | 252.000000 | 1.38 | 0.470000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 10:00:00 | 29.000000 | -0.220000 | 0.900000 | 92.000000 | 1017.000000 |  | 0.900000 | 0.000000 | 10000.000000 | 251.000000 | 1.98 | 0.800000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 11:00:00 | 26.000000 | -1.240000 | -0.100000 | 91.000000 | 1018.000000 |  | -0.100000 | 0.000000 | 10000.000000 | 250.000000 | 2.01 | 0.760000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 12:00:00 | 7.000000 | -1.030000 | 0.900000 | 86.000000 | 1018.000000 |  | 0.900000 | 0.550000 | 10000.000000 | 253.000000 | 2.11 | 0.530000 | 800 | Clear | clear sky | 01d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 13:00:00 | 14.000000 | 0.470000 | 4.900000 | 73.000000 | 1018.000000 |  | 4.900000 | 2.370000 | 10000.000000 | 293.000000 | 1.64 | 1.070000 | 801 | Clouds | few clouds | 02d | 13 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 14:00:00 | 7.000000 | 2.470000 | 8.230000 | 64.000000 | 1017.000000 |  | 8.900000 | 5.600000 | 10000.000000 | 307.000000 | 2.11 | 1.660000 | 800 | Clear | clear sky | 01d | 14 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 15:00:00 | 8.000000 | 3.410000 | 10.610000 | 56.000000 | 1016.000000 |  | 11.900000 | 9.420000 | 10000.000000 | 312.000000 | 2.36 | 1.840000 | 800 | Clear | clear sky | 01d | 15 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 16:00:00 | 8.000000 | 3.290000 | 11.600000 | 52.000000 | 1015.000000 |  | 12.900000 | 12.550000 | 10000.000000 | 317.000000 | 2.72 | 1.850000 | 800 | Clear | clear sky | 01d | 16 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 17:00:00 | 11.000000 | 5.140000 | 13.800000 | 52.000000 | 1014.000000 |  | 14.900000 | 13.660000 | 10000.000000 | 316.000000 | 2.98 | 2.030000 | 801 | Clouds | few clouds | 02d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 18:00:00 | 38.000000 | 5.020000 | 12.780000 | 55.000000 | 1013.000000 |  | 13.900000 | 12.400000 | 10000.000000 | 314.000000 | 2.91 | 2.030000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 19:00:00 | 47.000000 | 6.720000 | 13.960000 | 58.000000 | 1012.000000 | 0.17 | 14.900000 | 9.060000 | 10000.000000 | 312.000000 | 2.84 | 1.730000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 20:00:00 | 55.000000 | 7.210000 | 13.020000 | 64.000000 | 1011.000000 | 0.22 | 13.900000 | 5.280000 | 10000.000000 | 307.000000 | 2.71 | 1.310000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 21:00:00 | 68.000000 | 8.740000 | 13.200000 | 71.000000 | 1012.000000 | 0.19 | 13.900000 | 2.160000 | 10000.000000 | 299.000000 | 2.47 | 1.090000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 22:00:00 | 76.000000 | 9.720000 | 12.360000 | 81.000000 | 1013.000000 | 0.22 | 12.900000 | 0.450000 | 10000.000000 | 297.000000 | 2.07 | 0.670000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 23:00:00 | 81.000000 | 9.490000 | 10.420000 | 91.000000 | 1015.000000 | 0.13 | 10.900000 | 0.000000 | 10000.000000 | 301.000000 | 1.25 | 0.400000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21206920_OWM_Clouds_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Clouds_20220130.png)
![CNE_IDEAM_Station21206920_OWM_Dewpoint_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Dewpoint_20220130.png)
![CNE_IDEAM_Station21206920_OWM_Feelslike_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Feelslike_20220130.png)
![CNE_IDEAM_Station21206920_OWM_Humidity_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Humidity_20220130.png)
![CNE_IDEAM_Station21206920_OWM_Pressure_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Pressure_20220130.png)
![CNE_IDEAM_Station21206920_OWM_Rain_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Rain_20220130.png)
![CNE_IDEAM_Station21206920_OWM_Temp_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Temp_20220130.png)
![CNE_IDEAM_Station21206920_OWM_UVI_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_UVI_20220130.png)
![CNE_IDEAM_Station21206920_OWM_Visibility_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Visibility_20220130.png)
![CNE_IDEAM_Station21206920_OWM_Winddeg_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Winddeg_20220130.png)
![CNE_IDEAM_Station21206920_OWM_Windgust_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Windgust_20220130.png)
![CNE_IDEAM_Station21206920_OWM_Windspeed_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Windspeed_20220130.png)

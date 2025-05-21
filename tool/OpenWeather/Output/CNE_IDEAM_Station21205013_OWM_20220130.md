
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - UNISALLE NORTE [21205013] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21205013_OWM_20220130.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220130.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.79444444,-74.03055556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.79444444&lon=-74.03055556)

| Parameter | Value |
|---|---|
| Code | 21205013 |
| Name | UNISALLE NORTE [21205013] |
| Latitude, ° | 4.79444444 |
| Longitude, ° | -74.03055556 |
| Elevation, m | 2595 |
| Category | Climática Ordinaria |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 2009-12-14 00:00:00 |
| Suspension date | 2012-11-07 00:00:00 |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Guavio |
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

### (CNE index 1714) Open Weather values for station 21205013 - UNISALLE NORTE [21205013]

JSON data from API OWM:

```
{'lat': 4.7944, 'lon': -74.0306, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643467037, 'sunrise': 1643454712, 'sunset': 1643497588, 'temp': 12.9, 'feels_like': 12, 'pressure': 1028, 'humidity': 67, 'dew_point': 6.93, 'uvi': 9.24, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 220, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1643414400, 'temp': 12.9, 'feels_like': 12.26, 'pressure': 1025, 'humidity': 77, 'dew_point': 8.97, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 300, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.78}}, {'dt': 1643418000, 'temp': 12.9, 'feels_like': 12.39, 'pressure': 1025, 'humidity': 82, 'dew_point': 9.91, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 310, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.5}}, {'dt': 1643421600, 'temp': 11.9, 'feels_like': 11, 'pressure': 1026, 'humidity': 71, 'dew_point': 6.82, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 300, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1643425200, 'temp': 10.9, 'feels_like': 10.03, 'pressure': 1027, 'humidity': 76, 'dew_point': 6.84, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 320, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.37}}, {'dt': 1643428800, 'temp': 9.9, 'feels_like': 8.66, 'pressure': 1027, 'humidity': 87, 'dew_point': 7.84, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 310, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643432400, 'temp': 9.9, 'feels_like': 8.66, 'pressure': 1026, 'humidity': 87, 'dew_point': 7.84, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 320, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.36}}, {'dt': 1643436000, 'temp': 8.9, 'feels_like': 7.14, 'pressure': 1026, 'humidity': 87, 'dew_point': 6.86, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 340, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643439600, 'temp': 8.9, 'feels_like': 8.35, 'pressure': 1026, 'humidity': 87, 'dew_point': 6.86, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 320, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643443200, 'temp': 6.9, 'feels_like': 6.9, 'pressure': 1025, 'humidity': 93, 'dew_point': 5.85, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643446800, 'temp': 5.9, 'feels_like': 5.9, 'pressure': 1025, 'humidity': 93, 'dew_point': 4.86, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643450400, 'temp': 4.9, 'feels_like': 4.9, 'pressure': 1026, 'humidity': 100, 'dew_point': 4.9, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1643454000, 'temp': 3.9, 'feels_like': 3.9, 'pressure': 1026, 'humidity': 100, 'dew_point': 3.9, 'uvi': 0, 'clouds': 36, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1643457600, 'temp': 4.9, 'feels_like': 3.78, 'pressure': 1027, 'humidity': 100, 'dew_point': 4.9, 'uvi': 0.54, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 310, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1643461200, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1028, 'humidity': 93, 'dew_point': 7.83, 'uvi': 2.31, 'clouds': 9, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643464800, 'temp': 12.9, 'feels_like': 12, 'pressure': 1028, 'humidity': 67, 'dew_point': 6.93, 'uvi': 5.48, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 220, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643468400, 'temp': 15.9, 'feels_like': 14.88, 'pressure': 1028, 'humidity': 51, 'dew_point': 5.79, 'uvi': 9.24, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 230, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643472000, 'temp': 16.9, 'feels_like': 15.9, 'pressure': 1027, 'humidity': 48, 'dew_point': 5.83, 'uvi': 12.35, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643475600, 'temp': 18.9, 'feels_like': 17.89, 'pressure': 1026, 'humidity': 40, 'dew_point': 5.02, 'uvi': 13.45, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643479200, 'temp': 17.9, 'feels_like': 16.84, 'pressure': 1025, 'humidity': 42, 'dew_point': 4.82, 'uvi': 12.2, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643482800, 'temp': 18.9, 'feels_like': 17.94, 'pressure': 1024, 'humidity': 42, 'dew_point': 5.72, 'uvi': 9.16, 'clouds': 75, 'visibility': 10000, 'wind_speed': 7.2, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643486400, 'temp': 17.9, 'feels_like': 17.1, 'pressure': 1023, 'humidity': 52, 'dew_point': 7.92, 'uvi': 5.33, 'clouds': 75, 'visibility': 10000, 'wind_speed': 7.2, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643490000, 'temp': 17.9, 'feels_like': 17.1, 'pressure': 1023, 'humidity': 52, 'dew_point': 7.92, 'uvi': 2.17, 'clouds': 75, 'visibility': 10000, 'wind_speed': 6.69, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643493600, 'temp': 16.9, 'feels_like': 16.08, 'pressure': 1023, 'humidity': 55, 'dew_point': 7.81, 'uvi': 0.46, 'clouds': 40, 'visibility': 10000, 'wind_speed': 7.2, 'wind_deg': 300, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643497200, 'temp': 14.9, 'feels_like': 14.09, 'pressure': 1024, 'humidity': 63, 'dew_point': 7.93, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 6.69, 'wind_deg': 290, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.28}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 00:00:00 | 75.000000 | 8.970000 | 12.260000 | 77.000000 | 1025.000000 | 0.78 | 12.900000 | 0.000000 | 10000.000000 | 300.000000 |  | 4.120000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 01:00:00 | 75.000000 | 9.910000 | 12.390000 | 82.000000 | 1025.000000 | 0.5 | 12.900000 | 0.000000 | 10000.000000 | 310.000000 |  | 3.090000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 02:00:00 | 40.000000 | 6.820000 | 11.000000 | 71.000000 | 1026.000000 | 0.18 | 11.900000 | 0.000000 | 10000.000000 | 300.000000 |  | 3.600000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 03:00:00 | 40.000000 | 6.840000 | 10.030000 | 76.000000 | 1027.000000 | 0.37 | 10.900000 | 0.000000 | 10000.000000 | 320.000000 |  | 3.090000 | 500 | Rain | light rain | 10n | 03 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 04:00:00 | 20.000000 | 7.840000 | 8.660000 | 87.000000 | 1027.000000 |  | 9.900000 | 0.000000 | 10000.000000 | 310.000000 |  | 2.570000 | 801 | Clouds | few clouds | 02n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 05:00:00 | 20.000000 | 7.840000 | 8.660000 | 87.000000 | 1026.000000 | 0.36 | 9.900000 | 0.000000 | 10000.000000 | 320.000000 |  | 2.570000 | 500 | Rain | light rain | 10n | 05 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 06:00:00 | 20.000000 | 6.860000 | 7.140000 | 87.000000 | 1026.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 340.000000 |  | 3.090000 | 801 | Clouds | few clouds | 02n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 07:00:00 | 76.000000 | 6.860000 | 8.350000 | 87.000000 | 1026.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 320.000000 |  | 1.540000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 08:00:00 | 60.000000 | 5.850000 | 6.900000 | 93.000000 | 1025.000000 |  | 6.900000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 09:00:00 | 48.000000 | 4.860000 | 5.900000 | 93.000000 | 1025.000000 |  | 5.900000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 10:00:00 | 40.000000 | 4.900000 | 4.900000 | 100.000000 | 1026.000000 |  | 4.900000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 741 | Fog | fog | 50n | 10 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 11:00:00 | 36.000000 | 3.900000 | 3.900000 | 100.000000 | 1026.000000 |  | 3.900000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 741 | Fog | fog | 50n | 11 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 12:00:00 | 40.000000 | 4.900000 | 3.780000 | 100.000000 | 1027.000000 |  | 4.900000 | 0.540000 | 10000.000000 | 310.000000 |  | 1.540000 | 741 | Fog | fog | 50d | 12 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 13:00:00 | 9.000000 | 7.830000 | 8.900000 | 93.000000 | 1028.000000 |  | 8.900000 | 2.310000 | 10000.000000 | 0.000000 |  | 1.030000 | 800 | Clear | clear sky | 01d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 14:00:00 | 75.000000 | 6.930000 | 12.000000 | 67.000000 | 1028.000000 |  | 12.900000 | 5.480000 | 10000.000000 | 220.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 15:00:00 | 75.000000 | 5.790000 | 14.880000 | 51.000000 | 1028.000000 |  | 15.900000 | 9.240000 | 10000.000000 | 230.000000 |  | 1.540000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 16:00:00 | 75.000000 | 5.830000 | 15.900000 | 48.000000 | 1027.000000 |  | 16.900000 | 12.350000 | 10000.000000 | 310.000000 |  | 3.600000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 17:00:00 | 75.000000 | 5.020000 | 17.890000 | 40.000000 | 1026.000000 |  | 18.900000 | 13.450000 | 10000.000000 | 310.000000 |  | 5.660000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 18:00:00 | 75.000000 | 4.820000 | 16.840000 | 42.000000 | 1025.000000 |  | 17.900000 | 12.200000 | 10000.000000 | 310.000000 |  | 5.660000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 19:00:00 | 75.000000 | 5.720000 | 17.940000 | 42.000000 | 1024.000000 |  | 18.900000 | 9.160000 | 10000.000000 | 310.000000 |  | 7.200000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 20:00:00 | 75.000000 | 7.920000 | 17.100000 | 52.000000 | 1023.000000 |  | 17.900000 | 5.330000 | 10000.000000 | 310.000000 |  | 7.200000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 21:00:00 | 75.000000 | 7.920000 | 17.100000 | 52.000000 | 1023.000000 |  | 17.900000 | 2.170000 | 10000.000000 | 310.000000 |  | 6.690000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 22:00:00 | 40.000000 | 7.810000 | 16.080000 | 55.000000 | 1023.000000 |  | 16.900000 | 0.460000 | 10000.000000 | 300.000000 |  | 7.200000 | 802 | Clouds | scattered clouds | 03d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Climática Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 23:00:00 | 75.000000 | 7.930000 | 14.090000 | 63.000000 | 1024.000000 | 0.28 | 14.900000 | 0.000000 | 10000.000000 | 290.000000 |  | 6.690000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21205013_OWM_Clouds_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Clouds_20220130.png)
![CNE_IDEAM_Station21205013_OWM_Dewpoint_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Dewpoint_20220130.png)
![CNE_IDEAM_Station21205013_OWM_Feelslike_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Feelslike_20220130.png)
![CNE_IDEAM_Station21205013_OWM_Humidity_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Humidity_20220130.png)
![CNE_IDEAM_Station21205013_OWM_Pressure_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Pressure_20220130.png)
![CNE_IDEAM_Station21205013_OWM_Rain_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Rain_20220130.png)
![CNE_IDEAM_Station21205013_OWM_Temp_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Temp_20220130.png)
![CNE_IDEAM_Station21205013_OWM_UVI_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_UVI_20220130.png)
![CNE_IDEAM_Station21205013_OWM_Visibility_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Visibility_20220130.png)
![CNE_IDEAM_Station21205013_OWM_Winddeg_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Winddeg_20220130.png)
![CNE_IDEAM_Station21205013_OWM_Windgust_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Windgust_20220130.png)
![CNE_IDEAM_Station21205013_OWM_Windspeed_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Windspeed_20220130.png)


## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SOLMAFORO BOGOTA - [21205529] - Historical

Study case: Weather evaluation from historical openweathermap data for the CNE IDEAM network stations in Bogot� - Colombia - Suram�rica

### GitHub repository and system information

* Python version: 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
* Python path: ['D:\\R.GISPython\\OpenWeather', 'D:\\R.GISPython', 'D:\\R.GISPython.wiki', 'C:\\Python310\\python310.zip', 'C:\\Python310\\DLLs']
* matplotlib version: 3.5.0
* Repository: https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather
* License and conditions: https://github.com/rcfdtools/R.GISPython/wiki/License
* Credits: r.cfdtools@gmail.com

### General parameters

* Current date time: 2022-01-12 11:11:05.365344
* Unix time to eval: 1641899465
* Days before (for historical data): 1
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220112.xls
* CNE IDEAM file downloaded and updated: No
* CNE IDEAM stations: 4494
* CNE IDEAM attributes: 20
* CNE IDEAM station code filter: ['All', 26055120, 1508500053]
* CNE IDEAM category filter: ['All']
* CNE IDEAM technology filter: ['All', 'Autom�tica sin Telemetr�a']
* CNE IDEAM status filter: ['All', 'Activa', 'En Mantenimiento']
* CNE IDEAM state filter: ['Bogot�']
* CNE IDEAM county filter: ['All']
* CNE IDEAM stream filter: ['All']
* CNE IDEAM operator filter: ['All']
* CNE IDEAM hydro area filter: ['All']
* CNE IDEAM hydro zone filter: ['All']
* CNE IDEAM hydro subzone filter: ['All']
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21205529_OWM_20220112.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220112.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.66754167,-74.06044722) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.66754167&lon=-74.06044722)

| Parameter | Value |
|---|---|
| Code | 21205529 |
| Name | SOLMAFORO BOGOTA - [21205529] |
| Latitude, � | 4.66754167 |
| Longitude, � | -74.06044722 |
| Elevation, m | 2562 |
| Category | Meteorol�gica Especial |
| Technology | Autom�tica sin Telemetr�a |
| Status | Activa |
| Installation date | 2015-12-03 00:00:00 |
| Suspension date | NaT |
| State | Bogot� |
| County | Bogota, D.C |
| Stream | Murca |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | R�o Bogot� |

> For `Show historical`, `True` means that we are getting weather historic values with the `Time Machine` option from the openweathermap server, `False` means that we are getting the `Forecast` weather values.

#### Unit system (metric)

| Parameter | Unit metric system | Unit imperial system | openweathermap name |
|---|---|---|---|
| Temperature | �C | �F | temp |
| Dew Point | �C | �F | dew_point |
| Feels like | �C | �F | feels_like |
| Clouds | % | % | clouds |
| Humidity | % | % | humidity |
| Pressure | hPa | hPa | pressure |
| Wind Direction | � | � | wind_deg |
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

### (CNE index 1159) Open Weather values for station 21205529 - SOLMAFORO BOGOTA - [21205529]

JSON data from API OWM:

```
{'lat': 4.6675, 'lon': -74.0604, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641899465, 'sunrise': 1641899271, 'sunset': 1641942004, 'temp': 10.92, 'feels_like': 10.5, 'pressure': 1026, 'humidity': 93, 'dew_point': 9.83, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 280, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, 'hourly': [{'dt': 1641859200, 'temp': 13.92, 'feels_like': 13.67, 'pressure': 1025, 'humidity': 88, 'dew_point': 11.97, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 310, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641862800, 'temp': 13.92, 'feels_like': 13.67, 'pressure': 1026, 'humidity': 88, 'dew_point': 11.97, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 360, 'weather': [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09n'}]}, {'dt': 1641866400, 'temp': 12.92, 'feels_like': 12.72, 'pressure': 1027, 'humidity': 94, 'dew_point': 11.98, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 300, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641870000, 'temp': 12.92, 'feels_like': 12.57, 'pressure': 1027, 'humidity': 88, 'dew_point': 10.98, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 280, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641873600, 'temp': 12.92, 'feels_like': 12.57, 'pressure': 1027, 'humidity': 88, 'dew_point': 10.98, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 290, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641877200, 'temp': 12.92, 'feels_like': 12.57, 'pressure': 1026, 'humidity': 88, 'dew_point': 10.98, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641880800, 'temp': 12.92, 'feels_like': 12.41, 'pressure': 1026, 'humidity': 82, 'dew_point': 9.92, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 300, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641884400, 'temp': 12.92, 'feels_like': 12.41, 'pressure': 1025, 'humidity': 82, 'dew_point': 9.92, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 300, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641888000, 'temp': 11.92, 'feels_like': 11.44, 'pressure': 1024, 'humidity': 87, 'dew_point': 9.83, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641891600, 'temp': 11.92, 'feels_like': 11.78, 'pressure': 1024, 'humidity': 100, 'dew_point': 11.92, 'uvi': 0, 'clouds': 75, 'visibility': 8000, 'wind_speed': 3.09, 'wind_deg': 300, 'weather': [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09n'}]}, {'dt': 1641895200, 'temp': 10.92, 'feels_like': 10.5, 'pressure': 1025, 'humidity': 93, 'dew_point': 9.83, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 330, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641898800, 'temp': 10.92, 'feels_like': 10.5, 'pressure': 1026, 'humidity': 93, 'dew_point': 9.83, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 280, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641902400, 'temp': 10.92, 'feels_like': 10.5, 'pressure': 1027, 'humidity': 93, 'dew_point': 9.83, 'uvi': 0.47, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 290, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641906000, 'temp': 12.92, 'feels_like': 12.57, 'pressure': 1028, 'humidity': 88, 'dew_point': 10.98, 'uvi': 1.89, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641909600, 'temp': 13.92, 'feels_like': 13.51, 'pressure': 1028, 'humidity': 82, 'dew_point': 10.9, 'uvi': 4.54, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 290, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641913200, 'temp': 13.92, 'feels_like': 13.38, 'pressure': 1028, 'humidity': 77, 'dew_point': 9.96, 'uvi': 7.68, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 290, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641916800, 'temp': 14.92, 'feels_like': 14.22, 'pressure': 1028, 'humidity': 67, 'dew_point': 8.85, 'uvi': 11.23, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 310, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641920400, 'temp': 16.92, 'feels_like': 16.31, 'pressure': 1027, 'humidity': 63, 'dew_point': 9.84, 'uvi': 12.22, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 300, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1641924000, 'temp': 17.92, 'feels_like': 17.2, 'pressure': 1026, 'humidity': 55, 'dew_point': 8.76, 'uvi': 11.09, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 310, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.61}}, {'dt': 1641927600, 'temp': 18.92, 'feels_like': 18.3, 'pressure': 1025, 'humidity': 55, 'dew_point': 9.69, 'uvi': 5.75, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 280, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.32}}, {'dt': 1641931200, 'temp': 17.92, 'feels_like': 17.31, 'pressure': 1025, 'humidity': 59, 'dew_point': 9.8, 'uvi': 3.34, 'clouds': 40, 'visibility': 10000, 'wind_speed': 6.17, 'wind_deg': 290, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.45}}, {'dt': 1641934800, 'temp': 16.92, 'feels_like': 16.31, 'pressure': 1024, 'humidity': 63, 'dew_point': 9.84, 'uvi': 1.34, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 270, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.32}}, {'dt': 1641938400, 'temp': 16.92, 'feels_like': 16.31, 'pressure': 1024, 'humidity': 63, 'dew_point': 9.84, 'uvi': 0.44, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 290, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1641942000, 'temp': 14.92, 'feels_like': 14.48, 'pressure': 1025, 'humidity': 77, 'dew_point': 10.93, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 270, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.23}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 00:00:00 | 40.000000 | 11.970000 | 13.670000 | 88.000000 | 1025.000000 | 0.2 | 13.920000 | 0.000000 | 10000.000000 | 310.000000 |  | 2.060000 | 500 | Rain | light rain | 10n | 00 |
| ![09n.png](http://openweathermap.org/img/w/09n.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 01:00:00 | 75.000000 | 11.970000 | 13.670000 | 88.000000 | 1026.000000 |  | 13.920000 | 0.000000 | 10000.000000 | 360.000000 |  | 2.570000 | 300 | Drizzle | light intensity drizzle | 09n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 02:00:00 | 75.000000 | 11.980000 | 12.720000 | 94.000000 | 1027.000000 |  | 12.920000 | 0.000000 | 10000.000000 | 300.000000 |  | 4.120000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 03:00:00 | 75.000000 | 10.980000 | 12.570000 | 88.000000 | 1027.000000 |  | 12.920000 | 0.000000 | 10000.000000 | 280.000000 |  | 1.540000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 04:00:00 | 75.000000 | 10.980000 | 12.570000 | 88.000000 | 1027.000000 |  | 12.920000 | 0.000000 | 10000.000000 | 290.000000 |  | 3.090000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 05:00:00 | 75.000000 | 10.980000 | 12.570000 | 88.000000 | 1026.000000 |  | 12.920000 | 0.000000 | 10000.000000 | 310.000000 |  | 4.120000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 06:00:00 | 75.000000 | 9.920000 | 12.410000 | 82.000000 | 1026.000000 |  | 12.920000 | 0.000000 | 10000.000000 | 300.000000 |  | 3.600000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 07:00:00 | 75.000000 | 9.920000 | 12.410000 | 82.000000 | 1025.000000 |  | 12.920000 | 0.000000 | 10000.000000 | 300.000000 |  | 2.570000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 08:00:00 | 75.000000 | 9.830000 | 11.440000 | 87.000000 | 1024.000000 |  | 11.920000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![09n.png](http://openweathermap.org/img/w/09n.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 09:00:00 | 75.000000 | 11.920000 | 11.780000 | 100.000000 | 1024.000000 |  | 11.920000 | 0.000000 | 8000.000000 | 300.000000 |  | 3.090000 | 300 | Drizzle | light intensity drizzle | 09n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 10:00:00 | 40.000000 | 9.830000 | 10.500000 | 93.000000 | 1025.000000 |  | 10.920000 | 0.000000 | 10000.000000 | 330.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 11:00:00 | 40.000000 | 9.830000 | 10.500000 | 93.000000 | 1026.000000 |  | 10.920000 | 0.000000 | 10000.000000 | 280.000000 |  | 2.570000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 12:00:00 | 40.000000 | 9.830000 | 10.500000 | 93.000000 | 1027.000000 |  | 10.920000 | 0.470000 | 10000.000000 | 290.000000 |  | 3.090000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 13:00:00 | 75.000000 | 10.980000 | 12.570000 | 88.000000 | 1028.000000 |  | 12.920000 | 1.890000 | 10000.000000 | 310.000000 |  | 2.570000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 14:00:00 | 75.000000 | 10.900000 | 13.510000 | 82.000000 | 1028.000000 |  | 13.920000 | 4.540000 | 10000.000000 | 290.000000 |  | 1.540000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 15:00:00 | 75.000000 | 9.960000 | 13.380000 | 77.000000 | 1028.000000 | 0.11 | 13.920000 | 7.680000 | 10000.000000 | 290.000000 |  | 4.120000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 16:00:00 | 75.000000 | 8.850000 | 14.220000 | 67.000000 | 1028.000000 | 0.16 | 14.920000 | 11.230000 | 10000.000000 | 310.000000 |  | 4.630000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 17:00:00 | 20.000000 | 9.840000 | 16.310000 | 63.000000 | 1027.000000 | 0.33 | 16.920000 | 12.220000 | 10000.000000 | 300.000000 |  | 4.630000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 18:00:00 | 40.000000 | 8.760000 | 17.200000 | 55.000000 | 1026.000000 | 0.61 | 17.920000 | 11.090000 | 10000.000000 | 310.000000 |  | 3.600000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 19:00:00 | 40.000000 | 9.690000 | 18.300000 | 55.000000 | 1025.000000 | 0.32 | 18.920000 | 5.750000 | 10000.000000 | 280.000000 |  | 5.660000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 20:00:00 | 40.000000 | 9.800000 | 17.310000 | 59.000000 | 1025.000000 | 0.45 | 17.920000 | 3.340000 | 10000.000000 | 290.000000 |  | 6.170000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 21:00:00 | 40.000000 | 9.840000 | 16.310000 | 63.000000 | 1024.000000 | 0.32 | 16.920000 | 1.340000 | 10000.000000 | 270.000000 |  | 5.660000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 22:00:00 | 20.000000 | 9.840000 | 16.310000 | 63.000000 | 1024.000000 | 0.21 | 16.920000 | 0.440000 | 10000.000000 | 290.000000 |  | 4.630000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21205529 | "SOLMAFORO BOGOTA - [21205529]" | 4.667542 | -74.060447 | 2562.000000 | Meteorol�gica Especial | Autom�tica sin Telemetr�a | Activa | 2015-12-03 00:00:00 | NaT | Bogot� | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-11 23:00:00 | 40.000000 | 10.930000 | 14.480000 | 77.000000 | 1025.000000 | 0.23 | 14.920000 | 0.000000 | 10000.000000 | 270.000000 |  | 5.660000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21205529_OWM_Clouds_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205529_OWM_Clouds_20220112.png)
![CNE_IDEAM_Station21205529_OWM_Dewpoint_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205529_OWM_Dewpoint_20220112.png)
![CNE_IDEAM_Station21205529_OWM_Feelslike_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205529_OWM_Feelslike_20220112.png)
![CNE_IDEAM_Station21205529_OWM_Humidity_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205529_OWM_Humidity_20220112.png)
![CNE_IDEAM_Station21205529_OWM_Pressure_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205529_OWM_Pressure_20220112.png)
![CNE_IDEAM_Station21205529_OWM_Rain_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205529_OWM_Rain_20220112.png)
![CNE_IDEAM_Station21205529_OWM_Temp_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205529_OWM_Temp_20220112.png)
![CNE_IDEAM_Station21205529_OWM_UVI_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205529_OWM_UVI_20220112.png)
![CNE_IDEAM_Station21205529_OWM_Visibility_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205529_OWM_Visibility_20220112.png)
![CNE_IDEAM_Station21205529_OWM_Windgust_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205529_OWM_Windgust_20220112.png)
![CNE_IDEAM_Station21205529_OWM_Windspeed_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205529_OWM_Windspeed_20220112.png)

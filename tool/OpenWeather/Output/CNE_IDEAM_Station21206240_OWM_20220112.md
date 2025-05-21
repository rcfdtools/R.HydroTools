
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CENTRO GAVIOTAS [21206240] - Historical

Study case: Weather evaluation from historical openweathermap data for the CNE IDEAM network stations in Bogotá - Colombia - Suramérica

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
* CNE IDEAM technology filter: ['All', 'Automática sin Telemetría']
* CNE IDEAM status filter: ['All', 'Activa', 'En Mantenimiento']
* CNE IDEAM state filter: ['Bogotá']
* CNE IDEAM county filter: ['All']
* CNE IDEAM stream filter: ['All']
* CNE IDEAM operator filter: ['All']
* CNE IDEAM hydro area filter: ['All']
* CNE IDEAM hydro zone filter: ['All']
* CNE IDEAM hydro subzone filter: ['All']
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206240_OWM_20220112.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220112.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.6,-74.06666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.6&lon=-74.06666667)

| Parameter | Value |
|---|---|
| Code | 21206240 |
| Name | CENTRO GAVIOTAS [21206240] |
| Latitude, ° | 4.6 |
| Longitude, ° | -74.06666667 |
| Elevation, m | 2700 |
| Category | Meteorológica Especial |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1987-08-15 00:00:00 |
| Suspension date | 1992-09-15 00:00:00 |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Quebrada Perlas |
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

### (CNE index 2226) Open Weather values for station 21206240 - CENTRO GAVIOTAS [21206240]

JSON data from API OWM:

```
{'lat': 4.6, 'lon': -74.0667, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641899465, 'sunrise': 1641899266, 'sunset': 1641942012, 'temp': 9.94, 'feels_like': 8.71, 'pressure': 1026, 'humidity': 93, 'dew_point': 8.86, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 280, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, 'hourly': [{'dt': 1641859200, 'temp': 12.94, 'feels_like': 12.59, 'pressure': 1025, 'humidity': 88, 'dew_point': 11, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 310, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641862800, 'temp': 12.94, 'feels_like': 12.59, 'pressure': 1026, 'humidity': 88, 'dew_point': 11, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 360, 'weather': [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09n'}]}, {'dt': 1641866400, 'temp': 11.94, 'feels_like': 11.64, 'pressure': 1027, 'humidity': 94, 'dew_point': 11.01, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 300, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641870000, 'temp': 11.94, 'feels_like': 11.49, 'pressure': 1027, 'humidity': 88, 'dew_point': 10.02, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 280, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641873600, 'temp': 11.94, 'feels_like': 11.49, 'pressure': 1027, 'humidity': 88, 'dew_point': 10.02, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 290, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641877200, 'temp': 11.94, 'feels_like': 11.49, 'pressure': 1026, 'humidity': 88, 'dew_point': 10.02, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641880800, 'temp': 11.94, 'feels_like': 11.33, 'pressure': 1026, 'humidity': 82, 'dew_point': 8.97, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 300, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641884400, 'temp': 11.94, 'feels_like': 11.33, 'pressure': 1025, 'humidity': 82, 'dew_point': 8.97, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 300, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641888000, 'temp': 10.94, 'feels_like': 10.36, 'pressure': 1024, 'humidity': 87, 'dew_point': 8.86, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641891600, 'temp': 10.94, 'feels_like': 10.7, 'pressure': 1024, 'humidity': 100, 'dew_point': 10.94, 'uvi': 0, 'clouds': 75, 'visibility': 8000, 'wind_speed': 3.09, 'wind_deg': 300, 'weather': [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09n'}]}, {'dt': 1641895200, 'temp': 9.94, 'feels_like': 9.07, 'pressure': 1025, 'humidity': 93, 'dew_point': 8.86, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 330, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641898800, 'temp': 9.94, 'feels_like': 8.71, 'pressure': 1026, 'humidity': 93, 'dew_point': 8.86, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 280, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641902400, 'temp': 9.94, 'feels_like': 8.39, 'pressure': 1027, 'humidity': 93, 'dew_point': 8.86, 'uvi': 0.47, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 290, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641906000, 'temp': 11.94, 'feels_like': 11.49, 'pressure': 1028, 'humidity': 88, 'dew_point': 10.02, 'uvi': 1.89, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641909600, 'temp': 12.94, 'feels_like': 12.43, 'pressure': 1028, 'humidity': 82, 'dew_point': 9.94, 'uvi': 4.54, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 290, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641913200, 'temp': 12.94, 'feels_like': 12.3, 'pressure': 1028, 'humidity': 77, 'dew_point': 9.01, 'uvi': 7.68, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 290, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641916800, 'temp': 13.94, 'feels_like': 13.14, 'pressure': 1028, 'humidity': 67, 'dew_point': 7.92, 'uvi': 11.23, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 310, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641920400, 'temp': 15.94, 'feels_like': 15.23, 'pressure': 1027, 'humidity': 63, 'dew_point': 8.91, 'uvi': 12.22, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 300, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1641924000, 'temp': 16.94, 'feels_like': 16.13, 'pressure': 1026, 'humidity': 55, 'dew_point': 7.85, 'uvi': 11.09, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 310, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, {'dt': 1641927600, 'temp': 17.94, 'feels_like': 17.23, 'pressure': 1025, 'humidity': 55, 'dew_point': 8.78, 'uvi': 5.75, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 280, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.34}}, {'dt': 1641931200, 'temp': 16.94, 'feels_like': 16.23, 'pressure': 1025, 'humidity': 59, 'dew_point': 8.88, 'uvi': 3.34, 'clouds': 40, 'visibility': 10000, 'wind_speed': 6.17, 'wind_deg': 290, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.45}}, {'dt': 1641934800, 'temp': 15.94, 'feels_like': 15.23, 'pressure': 1024, 'humidity': 63, 'dew_point': 8.91, 'uvi': 1.34, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 270, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1641938400, 'temp': 15.94, 'feels_like': 15.23, 'pressure': 1024, 'humidity': 63, 'dew_point': 8.91, 'uvi': 0.44, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 290, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1641942000, 'temp': 13.94, 'feels_like': 13.4, 'pressure': 1025, 'humidity': 77, 'dew_point': 9.98, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 270, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 00:00:00 | 40.000000 | 11.000000 | 12.590000 | 88.000000 | 1025.000000 | 0.15 | 12.940000 | 0.000000 | 10000.000000 | 310.000000 |  | 2.060000 | 500 | Rain | light rain | 10n | 00 |
| ![09n.png](http://openweathermap.org/img/w/09n.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 01:00:00 | 75.000000 | 11.000000 | 12.590000 | 88.000000 | 1026.000000 |  | 12.940000 | 0.000000 | 10000.000000 | 360.000000 |  | 2.570000 | 300 | Drizzle | light intensity drizzle | 09n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 02:00:00 | 75.000000 | 11.010000 | 11.640000 | 94.000000 | 1027.000000 |  | 11.940000 | 0.000000 | 10000.000000 | 300.000000 |  | 4.120000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 03:00:00 | 75.000000 | 10.020000 | 11.490000 | 88.000000 | 1027.000000 |  | 11.940000 | 0.000000 | 10000.000000 | 280.000000 |  | 1.540000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 04:00:00 | 75.000000 | 10.020000 | 11.490000 | 88.000000 | 1027.000000 |  | 11.940000 | 0.000000 | 10000.000000 | 290.000000 |  | 3.090000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 05:00:00 | 75.000000 | 10.020000 | 11.490000 | 88.000000 | 1026.000000 |  | 11.940000 | 0.000000 | 10000.000000 | 310.000000 |  | 4.120000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 06:00:00 | 75.000000 | 8.970000 | 11.330000 | 82.000000 | 1026.000000 |  | 11.940000 | 0.000000 | 10000.000000 | 300.000000 |  | 3.600000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 07:00:00 | 75.000000 | 8.970000 | 11.330000 | 82.000000 | 1025.000000 |  | 11.940000 | 0.000000 | 10000.000000 | 300.000000 |  | 2.570000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 08:00:00 | 75.000000 | 8.860000 | 10.360000 | 87.000000 | 1024.000000 |  | 10.940000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![09n.png](http://openweathermap.org/img/w/09n.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 09:00:00 | 75.000000 | 10.940000 | 10.700000 | 100.000000 | 1024.000000 |  | 10.940000 | 0.000000 | 8000.000000 | 300.000000 |  | 3.090000 | 300 | Drizzle | light intensity drizzle | 09n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 10:00:00 | 40.000000 | 8.860000 | 9.070000 | 93.000000 | 1025.000000 |  | 9.940000 | 0.000000 | 10000.000000 | 330.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 11:00:00 | 40.000000 | 8.860000 | 8.710000 | 93.000000 | 1026.000000 |  | 9.940000 | 0.000000 | 10000.000000 | 280.000000 |  | 2.570000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 12:00:00 | 40.000000 | 8.860000 | 8.390000 | 93.000000 | 1027.000000 |  | 9.940000 | 0.470000 | 10000.000000 | 290.000000 |  | 3.090000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 13:00:00 | 75.000000 | 10.020000 | 11.490000 | 88.000000 | 1028.000000 |  | 11.940000 | 1.890000 | 10000.000000 | 310.000000 |  | 2.570000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 14:00:00 | 75.000000 | 9.940000 | 12.430000 | 82.000000 | 1028.000000 |  | 12.940000 | 4.540000 | 10000.000000 | 290.000000 |  | 1.540000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 15:00:00 | 75.000000 | 9.010000 | 12.300000 | 77.000000 | 1028.000000 |  | 12.940000 | 7.680000 | 10000.000000 | 290.000000 |  | 4.120000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 16:00:00 | 75.000000 | 7.920000 | 13.140000 | 67.000000 | 1028.000000 | 0.16 | 13.940000 | 11.230000 | 10000.000000 | 310.000000 |  | 4.630000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 17:00:00 | 20.000000 | 8.910000 | 15.230000 | 63.000000 | 1027.000000 | 0.31 | 15.940000 | 12.220000 | 10000.000000 | 300.000000 |  | 4.630000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 18:00:00 | 40.000000 | 7.850000 | 16.130000 | 55.000000 | 1026.000000 | 0.56 | 16.940000 | 11.090000 | 10000.000000 | 310.000000 |  | 3.600000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 19:00:00 | 40.000000 | 8.780000 | 17.230000 | 55.000000 | 1025.000000 | 0.34 | 17.940000 | 5.750000 | 10000.000000 | 280.000000 |  | 5.660000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 20:00:00 | 40.000000 | 8.880000 | 16.230000 | 59.000000 | 1025.000000 | 0.45 | 16.940000 | 3.340000 | 10000.000000 | 290.000000 |  | 6.170000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 21:00:00 | 40.000000 | 8.910000 | 15.230000 | 63.000000 | 1024.000000 | 0.33 | 15.940000 | 1.340000 | 10000.000000 | 270.000000 |  | 5.660000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 22:00:00 | 20.000000 | 8.910000 | 15.230000 | 63.000000 | 1024.000000 | 0.19 | 15.940000 | 0.440000 | 10000.000000 | 290.000000 |  | 4.630000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206240 | "CENTRO GAVIOTAS [21206240]" | 4.600000 | -74.066667 | 2700.000000 | Meteorológica Especial | Convencional | Suspendida | 1987-08-15 00:00:00 | 1992-09-15 00:00:00 | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 23:00:00 | 40.000000 | 9.980000 | 13.400000 | 77.000000 | 1025.000000 | 0.19 | 13.940000 | 0.000000 | 10000.000000 | 270.000000 |  | 5.660000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21206240_OWM_Clouds_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206240_OWM_Clouds_20220112.png)
![CNE_IDEAM_Station21206240_OWM_Dewpoint_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206240_OWM_Dewpoint_20220112.png)
![CNE_IDEAM_Station21206240_OWM_Feelslike_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206240_OWM_Feelslike_20220112.png)
![CNE_IDEAM_Station21206240_OWM_Humidity_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206240_OWM_Humidity_20220112.png)
![CNE_IDEAM_Station21206240_OWM_Pressure_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206240_OWM_Pressure_20220112.png)
![CNE_IDEAM_Station21206240_OWM_Rain_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206240_OWM_Rain_20220112.png)
![CNE_IDEAM_Station21206240_OWM_Temp_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206240_OWM_Temp_20220112.png)
![CNE_IDEAM_Station21206240_OWM_UVI_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206240_OWM_UVI_20220112.png)
![CNE_IDEAM_Station21206240_OWM_Visibility_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206240_OWM_Visibility_20220112.png)
![CNE_IDEAM_Station21206240_OWM_Windgust_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206240_OWM_Windgust_20220112.png)
![CNE_IDEAM_Station21206240_OWM_Windspeed_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206240_OWM_Windspeed_20220112.png)


## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AUSTRALIA [21201300] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201300_OWM_20220112.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220112.csv)

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

### (CNE index 1517) Open Weather values for station 21201300 - AUSTRALIA [21201300]

JSON data from API OWM:

```
{'lat': 4.3943, 'lon': -74.132, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641899465, 'sunrise': 1641899262, 'sunset': 1641942048, 'temp': 7.38, 'feels_like': 7.38, 'pressure': 1017, 'humidity': 94, 'dew_point': 6.48, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 336, 'wind_gust': 0.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641859200, 'temp': 10.38, 'feels_like': 9.9, 'pressure': 1016, 'humidity': 93, 'dew_point': 9.3, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.22, 'wind_deg': 97, 'wind_gust': 0.86, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641862800, 'temp': 10.38, 'feels_like': 9.9, 'pressure': 1017, 'humidity': 93, 'dew_point': 9.3, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 36, 'wind_gust': 0.93, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641866400, 'temp': 9.38, 'feels_like': 9.38, 'pressure': 1018, 'humidity': 93, 'dew_point': 8.31, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 61, 'wind_gust': 0.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641870000, 'temp': 9.38, 'feels_like': 9.38, 'pressure': 1019, 'humidity': 93, 'dew_point': 8.31, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 171, 'wind_gust': 0.89, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641873600, 'temp': 9.38, 'feels_like': 9.38, 'pressure': 1018, 'humidity': 90, 'dew_point': 7.83, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.07, 'wind_deg': 259, 'wind_gust': 0.81, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641877200, 'temp': 9.38, 'feels_like': 9.38, 'pressure': 1018, 'humidity': 90, 'dew_point': 7.83, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.07, 'wind_deg': 351, 'wind_gust': 0.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641880800, 'temp': 9.38, 'feels_like': 9.38, 'pressure': 1017, 'humidity': 91, 'dew_point': 7.99, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 289, 'wind_gust': 0.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641884400, 'temp': 9.38, 'feels_like': 9.38, 'pressure': 1016, 'humidity': 92, 'dew_point': 8.15, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 299, 'wind_gust': 1.09, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641888000, 'temp': 8.38, 'feels_like': 8.38, 'pressure': 1016, 'humidity': 93, 'dew_point': 7.32, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 314, 'wind_gust': 0.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641891600, 'temp': 8.38, 'feels_like': 8.38, 'pressure': 1016, 'humidity': 94, 'dew_point': 7.47, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 304, 'wind_gust': 1.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641895200, 'temp': 7.38, 'feels_like': 7.38, 'pressure': 1017, 'humidity': 94, 'dew_point': 6.48, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 320, 'wind_gust': 0.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641898800, 'temp': 7.38, 'feels_like': 7.38, 'pressure': 1017, 'humidity': 94, 'dew_point': 6.48, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 336, 'wind_gust': 0.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641902400, 'temp': 7.38, 'feels_like': 7.38, 'pressure': 1018, 'humidity': 92, 'dew_point': 6.17, 'uvi': 0.41, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 317, 'wind_gust': 0.94, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641906000, 'temp': 9.38, 'feels_like': 9.38, 'pressure': 1018, 'humidity': 86, 'dew_point': 7.16, 'uvi': 1.88, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 327, 'wind_gust': 1.08, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641909600, 'temp': 10.38, 'feels_like': 9.61, 'pressure': 1019, 'humidity': 82, 'dew_point': 7.44, 'uvi': 4.49, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 336, 'wind_gust': 1.07, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641913200, 'temp': 10.38, 'feels_like': 9.46, 'pressure': 1018, 'humidity': 76, 'dew_point': 6.34, 'uvi': 7.58, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 332, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641916800, 'temp': 11.38, 'feels_like': 10.48, 'pressure': 1017, 'humidity': 73, 'dew_point': 6.72, 'uvi': 11.73, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 280, 'wind_gust': 1.58, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641920400, 'temp': 13.38, 'feels_like': 12.71, 'pressure': 1016, 'humidity': 74, 'dew_point': 8.85, 'uvi': 12.76, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 271, 'wind_gust': 1.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.3}}, {'dt': 1641924000, 'temp': 14.38, 'feels_like': 13.91, 'pressure': 1015, 'humidity': 78, 'dew_point': 10.6, 'uvi': 11.59, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 275, 'wind_gust': 1.95, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.52}}, {'dt': 1641927600, 'temp': 15.38, 'feels_like': 15.22, 'pressure': 1015, 'humidity': 86, 'dew_point': 13.05, 'uvi': 8.33, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 279, 'wind_gust': 1.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}, {'dt': 1641931200, 'temp': 14.38, 'feels_like': 14.15, 'pressure': 1014, 'humidity': 87, 'dew_point': 12.25, 'uvi': 4.85, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 271, 'wind_gust': 1.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.52}}, {'dt': 1641934800, 'temp': 13.38, 'feels_like': 13.07, 'pressure': 1014, 'humidity': 88, 'dew_point': 11.44, 'uvi': 1.96, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 267, 'wind_gust': 1.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.34}}, {'dt': 1641938400, 'temp': 13.38, 'feels_like': 13.15, 'pressure': 1015, 'humidity': 91, 'dew_point': 11.94, 'uvi': 0.46, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.11, 'wind_deg': 242, 'wind_gust': 1.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641942000, 'temp': 11.38, 'feels_like': 11.08, 'pressure': 1016, 'humidity': 96, 'dew_point': 10.77, 'uvi': 0, 'clouds': 93, 'visibility': 9610, 'wind_speed': 0.04, 'wind_deg': 293, 'wind_gust': 1.07, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 00:00:00 | 79.000000 | 9.300000 | 9.900000 | 93.000000 | 1016.000000 |  | 10.380000 | 0.000000 | 10000.000000 | 97.000000 | 0.86 | 0.220000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 01:00:00 | 85.000000 | 9.300000 | 9.900000 | 93.000000 | 1017.000000 |  | 10.380000 | 0.000000 | 10000.000000 | 36.000000 | 0.93 | 0.360000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 02:00:00 | 87.000000 | 8.310000 | 9.380000 | 93.000000 | 1018.000000 |  | 9.380000 | 0.000000 | 10000.000000 | 61.000000 | 0.87 | 0.270000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 03:00:00 | 79.000000 | 8.310000 | 9.380000 | 93.000000 | 1019.000000 |  | 9.380000 | 0.000000 | 10000.000000 | 171.000000 | 0.89 | 0.310000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 04:00:00 | 79.000000 | 7.830000 | 9.380000 | 90.000000 | 1018.000000 |  | 9.380000 | 0.000000 | 10000.000000 | 259.000000 | 0.81 | 0.070000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 05:00:00 | 82.000000 | 7.830000 | 9.380000 | 90.000000 | 1018.000000 | 0.1 | 9.380000 | 0.000000 | 10000.000000 | 351.000000 | 0.82 | 0.070000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 06:00:00 | 67.000000 | 7.990000 | 9.380000 | 91.000000 | 1017.000000 | 0.16 | 9.380000 | 0.000000 | 10000.000000 | 289.000000 | 0.81 | 0.470000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 07:00:00 | 79.000000 | 8.150000 | 9.380000 | 92.000000 | 1016.000000 |  | 9.380000 | 0.000000 | 10000.000000 | 299.000000 | 1.09 | 0.570000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 08:00:00 | 79.000000 | 7.320000 | 8.380000 | 93.000000 | 1016.000000 |  | 8.380000 | 0.000000 | 10000.000000 | 314.000000 | 0.9 | 0.620000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 09:00:00 | 86.000000 | 7.470000 | 8.380000 | 94.000000 | 1016.000000 |  | 8.380000 | 0.000000 | 10000.000000 | 304.000000 | 1.17 | 0.910000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 10:00:00 | 89.000000 | 6.480000 | 7.380000 | 94.000000 | 1017.000000 |  | 7.380000 | 0.000000 | 10000.000000 | 320.000000 | 0.87 | 0.460000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 11:00:00 | 91.000000 | 6.480000 | 7.380000 | 94.000000 | 1017.000000 |  | 7.380000 | 0.000000 | 10000.000000 | 336.000000 | 0.75 | 0.340000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 12:00:00 | 85.000000 | 6.170000 | 7.380000 | 92.000000 | 1018.000000 |  | 7.380000 | 0.410000 | 10000.000000 | 317.000000 | 0.94 | 0.530000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 13:00:00 | 94.000000 | 7.160000 | 9.380000 | 86.000000 | 1018.000000 |  | 9.380000 | 1.880000 | 10000.000000 | 327.000000 | 1.08 | 0.610000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 14:00:00 | 96.000000 | 7.440000 | 9.610000 | 82.000000 | 1019.000000 | 0.11 | 10.380000 | 4.490000 | 10000.000000 | 336.000000 | 1.07 | 0.510000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 15:00:00 | 97.000000 | 6.340000 | 9.460000 | 76.000000 | 1018.000000 | 0.11 | 10.380000 | 7.580000 | 10000.000000 | 332.000000 | 1.25 | 0.690000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 16:00:00 | 96.000000 | 6.720000 | 10.480000 | 73.000000 | 1017.000000 | 0.16 | 11.380000 | 11.730000 | 10000.000000 | 280.000000 | 1.58 | 0.770000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 17:00:00 | 95.000000 | 8.850000 | 12.710000 | 74.000000 | 1016.000000 | 0.3 | 13.380000 | 12.760000 | 10000.000000 | 271.000000 | 1.82 | 0.870000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 18:00:00 | 92.000000 | 10.600000 | 13.910000 | 78.000000 | 1015.000000 | 0.52 | 14.380000 | 11.590000 | 10000.000000 | 275.000000 | 1.95 | 0.640000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 19:00:00 | 100.000000 | 13.050000 | 15.220000 | 86.000000 | 1015.000000 | 0.44 | 15.380000 | 8.330000 | 10000.000000 | 279.000000 | 1.93 | 0.600000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 20:00:00 | 99.000000 | 12.250000 | 14.150000 | 87.000000 | 1014.000000 | 0.52 | 14.380000 | 4.850000 | 10000.000000 | 271.000000 | 1.69 | 0.630000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 21:00:00 | 97.000000 | 11.440000 | 13.070000 | 88.000000 | 1014.000000 | 0.34 | 13.380000 | 1.960000 | 10000.000000 | 267.000000 | 1.61 | 0.330000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 22:00:00 | 96.000000 | 11.940000 | 13.150000 | 91.000000 | 1015.000000 | 0.15 | 13.380000 | 0.460000 | 10000.000000 | 242.000000 | 1.23 | 0.110000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-11 23:00:00 | 93.000000 | 10.770000 | 11.080000 | 96.000000 | 1016.000000 | 0.13 | 11.380000 | 0.000000 | 9610.000000 | 293.000000 | 1.07 | 0.040000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21201300_OWM_Clouds_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Clouds_20220112.png)
![CNE_IDEAM_Station21201300_OWM_Dewpoint_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Dewpoint_20220112.png)
![CNE_IDEAM_Station21201300_OWM_Feelslike_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Feelslike_20220112.png)
![CNE_IDEAM_Station21201300_OWM_Humidity_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Humidity_20220112.png)
![CNE_IDEAM_Station21201300_OWM_Pressure_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Pressure_20220112.png)
![CNE_IDEAM_Station21201300_OWM_Rain_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Rain_20220112.png)
![CNE_IDEAM_Station21201300_OWM_Temp_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Temp_20220112.png)
![CNE_IDEAM_Station21201300_OWM_UVI_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_UVI_20220112.png)
![CNE_IDEAM_Station21201300_OWM_Visibility_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Visibility_20220112.png)
![CNE_IDEAM_Station21201300_OWM_Windgust_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Windgust_20220112.png)
![CNE_IDEAM_Station21201300_OWM_Windspeed_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Windspeed_20220112.png)

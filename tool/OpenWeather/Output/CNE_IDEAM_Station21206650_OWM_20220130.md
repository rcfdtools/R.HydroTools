
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206650_OWM_20220130.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220130.csv)

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

### (CNE index 3790) Open Weather values for station 21206650 - COLEGIO SAN CAYETANO [21206650]

JSON data from API OWM:

```
{'lat': 4.5168, 'lon': -74.0882, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643467037, 'sunrise': 1643454704, 'sunset': 1643497623, 'temp': 9.97, 'feels_like': 8.93, 'pressure': 1016, 'humidity': 50, 'dew_point': 0.04, 'uvi': 9.24, 'clouds': 6, 'visibility': 10000, 'wind_speed': 2.29, 'wind_deg': 312, 'wind_gust': 2.31, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, 'hourly': [{'dt': 1643414400, 'temp': 9.97, 'feels_like': 9.97, 'pressure': 1015, 'humidity': 86, 'dew_point': 7.74, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 114, 'wind_gust': 1.48, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.76}}, {'dt': 1643418000, 'temp': 9.97, 'feels_like': 9.97, 'pressure': 1016, 'humidity': 87, 'dew_point': 7.91, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 87, 'wind_gust': 1.48, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.48}}, {'dt': 1643421600, 'temp': 8.97, 'feels_like': 8.97, 'pressure': 1017, 'humidity': 92, 'dew_point': 7.74, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 307, 'wind_gust': 0.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1643425200, 'temp': 7.97, 'feels_like': 7.97, 'pressure': 1017, 'humidity': 88, 'dew_point': 6.11, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.09, 'wind_deg': 0, 'wind_gust': 0.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.33}}, {'dt': 1643428800, 'temp': 6.97, 'feels_like': 6.97, 'pressure': 1017, 'humidity': 90, 'dew_point': 5.44, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 302, 'wind_gust': 1.25, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643432400, 'temp': 6.97, 'feels_like': 6.97, 'pressure': 1017, 'humidity': 90, 'dew_point': 5.44, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 304, 'wind_gust': 1.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1643436000, 'temp': 5.97, 'feels_like': 5.97, 'pressure': 1016, 'humidity': 90, 'dew_point': 4.46, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 289, 'wind_gust': 1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643439600, 'temp': 5.97, 'feels_like': 5.97, 'pressure': 1016, 'humidity': 93, 'dew_point': 4.93, 'uvi': 0, 'clouds': 27, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 275, 'wind_gust': 1.62, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643443200, 'temp': 3.97, 'feels_like': 3.97, 'pressure': 1016, 'humidity': 94, 'dew_point': 3.09, 'uvi': 0, 'clouds': 22, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 296, 'wind_gust': 1.96, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643446800, 'temp': 2.97, 'feels_like': 2.97, 'pressure': 1016, 'humidity': 94, 'dew_point': 2.1, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 303, 'wind_gust': 1.23, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643450400, 'temp': 1.97, 'feels_like': 1.97, 'pressure': 1017, 'humidity': 94, 'dew_point': 1.11, 'uvi': 0, 'clouds': 19, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 297, 'wind_gust': 1.97, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643454000, 'temp': 0.97, 'feels_like': 0.97, 'pressure': 1017, 'humidity': 94, 'dew_point': 0.11, 'uvi': 0, 'clouds': 17, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 298, 'wind_gust': 1.93, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643457600, 'temp': 1.97, 'feels_like': 1.97, 'pressure': 1018, 'humidity': 89, 'dew_point': 0.35, 'uvi': 0.54, 'clouds': 5, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 309, 'wind_gust': 2.29, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643461200, 'temp': 5.97, 'feels_like': 5.04, 'pressure': 1017, 'humidity': 75, 'dew_point': 1.88, 'uvi': 2.31, 'clouds': 10, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 305, 'wind_gust': 2.17, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643464800, 'temp': 9.97, 'feels_like': 9.1, 'pressure': 1017, 'humidity': 61, 'dew_point': 2.81, 'uvi': 5.48, 'clouds': 6, 'visibility': 10000, 'wind_speed': 2.07, 'wind_deg': 310, 'wind_gust': 2.36, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643468400, 'temp': 12.97, 'feels_like': 11.63, 'pressure': 1016, 'humidity': 50, 'dew_point': 2.8, 'uvi': 9.24, 'clouds': 6, 'visibility': 10000, 'wind_speed': 2.29, 'wind_deg': 312, 'wind_gust': 2.31, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643472000, 'temp': 13.97, 'feels_like': 12.57, 'pressure': 1014, 'humidity': 44, 'dew_point': 1.92, 'uvi': 12.35, 'clouds': 4, 'visibility': 10000, 'wind_speed': 2.5, 'wind_deg': 314, 'wind_gust': 2.43, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643475600, 'temp': 15.97, 'feels_like': 14.69, 'pressure': 1013, 'humidity': 41, 'dew_point': 2.74, 'uvi': 13.45, 'clouds': 12, 'visibility': 10000, 'wind_speed': 2.76, 'wind_deg': 314, 'wind_gust': 2.63, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643479200, 'temp': 14.97, 'feels_like': 13.57, 'pressure': 1012, 'humidity': 40, 'dew_point': 1.5, 'uvi': 12.2, 'clouds': 25, 'visibility': 10000, 'wind_speed': 2.75, 'wind_deg': 310, 'wind_gust': 2.62, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643482800, 'temp': 15.97, 'feels_like': 14.67, 'pressure': 1010, 'humidity': 40, 'dew_point': 2.39, 'uvi': 9.16, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.5, 'wind_deg': 307, 'wind_gust': 2.58, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643486400, 'temp': 14.97, 'feels_like': 13.65, 'pressure': 1010, 'humidity': 43, 'dew_point': 2.51, 'uvi': 5.33, 'clouds': 15, 'visibility': 10000, 'wind_speed': 1.93, 'wind_deg': 293, 'wind_gust': 2.7, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643490000, 'temp': 14.97, 'feels_like': 13.85, 'pressure': 1010, 'humidity': 51, 'dew_point': 4.93, 'uvi': 2.17, 'clouds': 33, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 283, 'wind_gust': 2.69, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643493600, 'temp': 13.97, 'feels_like': 13.17, 'pressure': 1012, 'humidity': 67, 'dew_point': 7.95, 'uvi': 0.46, 'clouds': 48, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 276, 'wind_gust': 2.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1643497200, 'temp': 11.97, 'feels_like': 11.47, 'pressure': 1014, 'humidity': 86, 'dew_point': 9.7, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 290, 'wind_gust': 1.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 00:00:00 | 97.000000 | 7.740000 | 9.970000 | 86.000000 | 1015.000000 | 0.76 | 9.970000 | 0.000000 | 10000.000000 | 114.000000 | 1.48 | 0.610000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 01:00:00 | 100.000000 | 7.910000 | 9.970000 | 87.000000 | 1016.000000 | 0.48 | 9.970000 | 0.000000 | 10000.000000 | 87.000000 | 1.48 | 0.530000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 02:00:00 | 52.000000 | 7.740000 | 8.970000 | 92.000000 | 1017.000000 | 0.11 | 8.970000 | 0.000000 | 10000.000000 | 307.000000 | 0.9 | 0.250000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 03:00:00 | 87.000000 | 6.110000 | 7.970000 | 88.000000 | 1017.000000 | 0.33 | 7.970000 | 0.000000 | 10000.000000 | 0.000000 | 0.8 | 0.090000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 04:00:00 | 60.000000 | 5.440000 | 6.970000 | 90.000000 | 1017.000000 |  | 6.970000 | 0.000000 | 10000.000000 | 302.000000 | 1.25 | 0.700000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 05:00:00 | 90.000000 | 5.440000 | 6.970000 | 90.000000 | 1017.000000 | 0.21 | 6.970000 | 0.000000 | 10000.000000 | 304.000000 | 1.43 | 0.870000 | 500 | Rain | light rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 06:00:00 | 87.000000 | 4.460000 | 5.970000 | 90.000000 | 1016.000000 |  | 5.970000 | 0.000000 | 10000.000000 | 289.000000 | 1 | 0.600000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 07:00:00 | 27.000000 | 4.930000 | 5.970000 | 93.000000 | 1016.000000 |  | 5.970000 | 0.000000 | 10000.000000 | 275.000000 | 1.62 | 0.860000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 08:00:00 | 22.000000 | 3.090000 | 3.970000 | 94.000000 | 1016.000000 |  | 3.970000 | 0.000000 | 10000.000000 | 296.000000 | 1.96 | 0.990000 | 801 | Clouds | few clouds | 02n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 09:00:00 | 34.000000 | 2.100000 | 2.970000 | 94.000000 | 1016.000000 |  | 2.970000 | 0.000000 | 10000.000000 | 303.000000 | 1.23 | 0.750000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 10:00:00 | 19.000000 | 1.110000 | 1.970000 | 94.000000 | 1017.000000 |  | 1.970000 | 0.000000 | 10000.000000 | 297.000000 | 1.97 | 1.060000 | 801 | Clouds | few clouds | 02n | 10 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 11:00:00 | 17.000000 | 0.110000 | 0.970000 | 94.000000 | 1017.000000 |  | 0.970000 | 0.000000 | 10000.000000 | 298.000000 | 1.93 | 1.140000 | 801 | Clouds | few clouds | 02n | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 12:00:00 | 5.000000 | 0.350000 | 1.970000 | 89.000000 | 1018.000000 |  | 1.970000 | 0.540000 | 10000.000000 | 309.000000 | 2.29 | 0.980000 | 800 | Clear | clear sky | 01d | 12 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 13:00:00 | 10.000000 | 1.880000 | 5.040000 | 75.000000 | 1017.000000 |  | 5.970000 | 2.310000 | 10000.000000 | 305.000000 | 2.17 | 1.510000 | 800 | Clear | clear sky | 01d | 13 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 14:00:00 | 6.000000 | 2.810000 | 9.100000 | 61.000000 | 1017.000000 |  | 9.970000 | 5.480000 | 10000.000000 | 310.000000 | 2.36 | 2.070000 | 800 | Clear | clear sky | 01d | 14 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 15:00:00 | 6.000000 | 2.800000 | 11.630000 | 50.000000 | 1016.000000 |  | 12.970000 | 9.240000 | 10000.000000 | 312.000000 | 2.31 | 2.290000 | 800 | Clear | clear sky | 01d | 15 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 16:00:00 | 4.000000 | 1.920000 | 12.570000 | 44.000000 | 1014.000000 |  | 13.970000 | 12.350000 | 10000.000000 | 314.000000 | 2.43 | 2.500000 | 800 | Clear | clear sky | 01d | 16 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 17:00:00 | 12.000000 | 2.740000 | 14.690000 | 41.000000 | 1013.000000 |  | 15.970000 | 13.450000 | 10000.000000 | 314.000000 | 2.63 | 2.760000 | 801 | Clouds | few clouds | 02d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 18:00:00 | 25.000000 | 1.500000 | 13.570000 | 40.000000 | 1012.000000 |  | 14.970000 | 12.200000 | 10000.000000 | 310.000000 | 2.62 | 2.750000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 19:00:00 | 20.000000 | 2.390000 | 14.670000 | 40.000000 | 1010.000000 |  | 15.970000 | 9.160000 | 10000.000000 | 307.000000 | 2.58 | 2.500000 | 801 | Clouds | few clouds | 02d | 19 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 20:00:00 | 15.000000 | 2.510000 | 13.650000 | 43.000000 | 1010.000000 |  | 14.970000 | 5.330000 | 10000.000000 | 293.000000 | 2.7 | 1.930000 | 801 | Clouds | few clouds | 02d | 20 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 21:00:00 | 33.000000 | 4.930000 | 13.850000 | 51.000000 | 1010.000000 |  | 14.970000 | 2.170000 | 10000.000000 | 283.000000 | 2.69 | 1.620000 | 802 | Clouds | scattered clouds | 03d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 22:00:00 | 48.000000 | 7.950000 | 13.170000 | 67.000000 | 1012.000000 | 0.13 | 13.970000 | 0.460000 | 10000.000000 | 276.000000 | 2.03 | 0.830000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206650 | "COLEGIO SAN CAYETANO [21206650]" | 4.516753 | -74.088222 | 3100.000000 | Climática Ordinaria | Convencional | Activa | 2001-11-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 23:00:00 | 59.000000 | 9.700000 | 11.470000 | 86.000000 | 1014.000000 | 0.14 | 11.970000 | 0.000000 | 10000.000000 | 290.000000 | 1.66 | 0.390000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21206650_OWM_Clouds_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Clouds_20220130.png)
![CNE_IDEAM_Station21206650_OWM_Dewpoint_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Dewpoint_20220130.png)
![CNE_IDEAM_Station21206650_OWM_Feelslike_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Feelslike_20220130.png)
![CNE_IDEAM_Station21206650_OWM_Humidity_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Humidity_20220130.png)
![CNE_IDEAM_Station21206650_OWM_Pressure_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Pressure_20220130.png)
![CNE_IDEAM_Station21206650_OWM_Rain_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Rain_20220130.png)
![CNE_IDEAM_Station21206650_OWM_Temp_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Temp_20220130.png)
![CNE_IDEAM_Station21206650_OWM_UVI_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_UVI_20220130.png)
![CNE_IDEAM_Station21206650_OWM_Visibility_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Visibility_20220130.png)
![CNE_IDEAM_Station21206650_OWM_Winddeg_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Winddeg_20220130.png)
![CNE_IDEAM_Station21206650_OWM_Windgust_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Windgust_20220130.png)
![CNE_IDEAM_Station21206650_OWM_Windspeed_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206650_OWM_Windspeed_20220130.png)

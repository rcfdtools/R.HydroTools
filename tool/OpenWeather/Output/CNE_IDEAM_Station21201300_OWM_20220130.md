
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AUSTRALIA [21201300] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201300_OWM_20220130.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220130.csv)

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
{'lat': 4.3943, 'lon': -74.132, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643467037, 'sunrise': 1643454705, 'sunset': 1643497643, 'temp': 10.38, 'feels_like': 8.88, 'pressure': 1016, 'humidity': 54, 'dew_point': 1.48, 'uvi': 9.42, 'clouds': 7, 'visibility': 10000, 'wind_speed': 1.91, 'wind_deg': 313, 'wind_gust': 2.37, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, 'hourly': [{'dt': 1643414400, 'temp': 10.38, 'feels_like': 9.8, 'pressure': 1015, 'humidity': 89, 'dew_point': 8.65, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 86, 'wind_gust': 1.36, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.89}}, {'dt': 1643418000, 'temp': 10.38, 'feels_like': 9.8, 'pressure': 1016, 'humidity': 89, 'dew_point': 8.65, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 49, 'wind_gust': 1.49, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.67}}, {'dt': 1643421600, 'temp': 9.38, 'feels_like': 9.38, 'pressure': 1017, 'humidity': 92, 'dew_point': 8.15, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 318, 'wind_gust': 1.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643425200, 'temp': 8.38, 'feels_like': 8.38, 'pressure': 1018, 'humidity': 89, 'dew_point': 6.67, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 313, 'wind_gust': 1.09, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.58}}, {'dt': 1643428800, 'temp': 7.38, 'feels_like': 7.38, 'pressure': 1017, 'humidity': 90, 'dew_point': 5.85, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 287, 'wind_gust': 1.19, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643432400, 'temp': 7.38, 'feels_like': 7.38, 'pressure': 1017, 'humidity': 91, 'dew_point': 6.01, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 287, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.47}}, {'dt': 1643436000, 'temp': 6.38, 'feels_like': 6.38, 'pressure': 1017, 'humidity': 91, 'dew_point': 5.02, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 255, 'wind_gust': 1.04, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643439600, 'temp': 6.38, 'feels_like': 6.38, 'pressure': 1017, 'humidity': 93, 'dew_point': 5.33, 'uvi': 0, 'clouds': 28, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 246, 'wind_gust': 1.65, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643443200, 'temp': 4.38, 'feels_like': 4.38, 'pressure': 1016, 'humidity': 93, 'dew_point': 3.35, 'uvi': 0, 'clouds': 25, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 264, 'wind_gust': 1.9, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643446800, 'temp': 3.38, 'feels_like': 3.38, 'pressure': 1016, 'humidity': 92, 'dew_point': 2.21, 'uvi': 0, 'clouds': 32, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 268, 'wind_gust': 1.35, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643450400, 'temp': 2.38, 'feels_like': 2.38, 'pressure': 1017, 'humidity': 92, 'dew_point': 1.22, 'uvi': 0, 'clouds': 25, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 264, 'wind_gust': 2.02, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643454000, 'temp': 1.38, 'feels_like': 1.38, 'pressure': 1018, 'humidity': 91, 'dew_point': 0.07, 'uvi': 0, 'clouds': 22, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 266, 'wind_gust': 2.01, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643457600, 'temp': 2.38, 'feels_like': 2.38, 'pressure': 1018, 'humidity': 87, 'dew_point': 0.44, 'uvi': 0.55, 'clouds': 7, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 273, 'wind_gust': 2.16, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643461200, 'temp': 6.38, 'feels_like': 6.38, 'pressure': 1018, 'humidity': 73, 'dew_point': 1.9, 'uvi': 2.37, 'clouds': 12, 'visibility': 10000, 'wind_speed': 1.21, 'wind_deg': 296, 'wind_gust': 1.8, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643464800, 'temp': 10.38, 'feels_like': 9.12, 'pressure': 1017, 'humidity': 63, 'dew_point': 3.65, 'uvi': 5.6, 'clouds': 7, 'visibility': 10000, 'wind_speed': 1.74, 'wind_deg': 308, 'wind_gust': 2.19, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643468400, 'temp': 13.38, 'feels_like': 12.18, 'pressure': 1016, 'humidity': 54, 'dew_point': 4.27, 'uvi': 9.42, 'clouds': 7, 'visibility': 10000, 'wind_speed': 1.91, 'wind_deg': 313, 'wind_gust': 2.37, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643472000, 'temp': 14.38, 'feels_like': 13.18, 'pressure': 1015, 'humidity': 50, 'dew_point': 4.1, 'uvi': 12.55, 'clouds': 6, 'visibility': 10000, 'wind_speed': 1.95, 'wind_deg': 318, 'wind_gust': 2.67, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643475600, 'temp': 16.38, 'feels_like': 15.35, 'pressure': 1014, 'humidity': 49, 'dew_point': 5.65, 'uvi': 13.66, 'clouds': 11, 'visibility': 10000, 'wind_speed': 2.14, 'wind_deg': 318, 'wind_gust': 2.92, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643479200, 'temp': 15.38, 'feels_like': 14.31, 'pressure': 1012, 'humidity': 51, 'dew_point': 5.31, 'uvi': 12.4, 'clouds': 33, 'visibility': 10000, 'wind_speed': 2.13, 'wind_deg': 315, 'wind_gust': 2.86, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643482800, 'temp': 16.38, 'feels_like': 15.46, 'pressure': 1011, 'humidity': 53, 'dew_point': 6.79, 'uvi': 9.06, 'clouds': 38, 'visibility': 10000, 'wind_speed': 1.86, 'wind_deg': 313, 'wind_gust': 2.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1643486400, 'temp': 15.38, 'feels_like': 14.49, 'pressure': 1011, 'humidity': 58, 'dew_point': 7.17, 'uvi': 5.28, 'clouds': 43, 'visibility': 10000, 'wind_speed': 1.4, 'wind_deg': 304, 'wind_gust': 2.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1643490000, 'temp': 15.38, 'feels_like': 14.67, 'pressure': 1011, 'humidity': 65, 'dew_point': 8.84, 'uvi': 2.16, 'clouds': 58, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 294, 'wind_gust': 2.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1643493600, 'temp': 14.38, 'feels_like': 13.86, 'pressure': 1012, 'humidity': 76, 'dew_point': 10.21, 'uvi': 0.45, 'clouds': 69, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 293, 'wind_gust': 2.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1643497200, 'temp': 12.38, 'feels_like': 12.02, 'pressure': 1014, 'humidity': 90, 'dew_point': 10.79, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 303, 'wind_gust': 1.33, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 00:00:00 | 94.000000 | 8.650000 | 9.800000 | 89.000000 | 1015.000000 | 0.89 | 10.380000 | 0.000000 | 10000.000000 | 86.000000 | 1.36 | 0.530000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 01:00:00 | 99.000000 | 8.650000 | 9.800000 | 89.000000 | 1016.000000 | 0.67 | 10.380000 | 0.000000 | 10000.000000 | 49.000000 | 1.49 | 0.580000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 02:00:00 | 65.000000 | 8.150000 | 9.380000 | 92.000000 | 1017.000000 |  | 9.380000 | 0.000000 | 10000.000000 | 318.000000 | 1.15 | 0.470000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 03:00:00 | 87.000000 | 6.670000 | 8.380000 | 89.000000 | 1018.000000 | 0.58 | 8.380000 | 0.000000 | 10000.000000 | 313.000000 | 1.09 | 0.440000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 04:00:00 | 73.000000 | 5.850000 | 7.380000 | 90.000000 | 1017.000000 |  | 7.380000 | 0.000000 | 10000.000000 | 287.000000 | 1.19 | 0.380000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 05:00:00 | 85.000000 | 6.010000 | 7.380000 | 91.000000 | 1017.000000 | 0.47 | 7.380000 | 0.000000 | 10000.000000 | 287.000000 | 1.27 | 0.630000 | 500 | Rain | light rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 06:00:00 | 81.000000 | 5.020000 | 6.380000 | 91.000000 | 1017.000000 |  | 6.380000 | 0.000000 | 10000.000000 | 255.000000 | 1.04 | 0.390000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 07:00:00 | 28.000000 | 5.330000 | 6.380000 | 93.000000 | 1017.000000 |  | 6.380000 | 0.000000 | 10000.000000 | 246.000000 | 1.65 | 0.690000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 08:00:00 | 25.000000 | 3.350000 | 4.380000 | 93.000000 | 1016.000000 |  | 4.380000 | 0.000000 | 10000.000000 | 264.000000 | 1.9 | 0.780000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 09:00:00 | 32.000000 | 2.210000 | 3.380000 | 92.000000 | 1016.000000 |  | 3.380000 | 0.000000 | 10000.000000 | 268.000000 | 1.35 | 0.560000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 10:00:00 | 25.000000 | 1.220000 | 2.380000 | 92.000000 | 1017.000000 |  | 2.380000 | 0.000000 | 10000.000000 | 264.000000 | 2.02 | 0.890000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 11:00:00 | 22.000000 | 0.070000 | 1.380000 | 91.000000 | 1018.000000 |  | 1.380000 | 0.000000 | 10000.000000 | 266.000000 | 2.01 | 0.890000 | 801 | Clouds | few clouds | 02n | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 12:00:00 | 7.000000 | 0.440000 | 2.380000 | 87.000000 | 1018.000000 |  | 2.380000 | 0.550000 | 10000.000000 | 273.000000 | 2.16 | 0.660000 | 800 | Clear | clear sky | 01d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 13:00:00 | 12.000000 | 1.900000 | 6.380000 | 73.000000 | 1018.000000 |  | 6.380000 | 2.370000 | 10000.000000 | 296.000000 | 1.8 | 1.210000 | 801 | Clouds | few clouds | 02d | 13 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 14:00:00 | 7.000000 | 3.650000 | 9.120000 | 63.000000 | 1017.000000 |  | 10.380000 | 5.600000 | 10000.000000 | 308.000000 | 2.19 | 1.740000 | 800 | Clear | clear sky | 01d | 14 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 15:00:00 | 7.000000 | 4.270000 | 12.180000 | 54.000000 | 1016.000000 |  | 13.380000 | 9.420000 | 10000.000000 | 313.000000 | 2.37 | 1.910000 | 800 | Clear | clear sky | 01d | 15 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 16:00:00 | 6.000000 | 4.100000 | 13.180000 | 50.000000 | 1015.000000 |  | 14.380000 | 12.550000 | 10000.000000 | 318.000000 | 2.67 | 1.950000 | 800 | Clear | clear sky | 01d | 16 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 17:00:00 | 11.000000 | 5.650000 | 15.350000 | 49.000000 | 1014.000000 |  | 16.380000 | 13.660000 | 10000.000000 | 318.000000 | 2.92 | 2.140000 | 801 | Clouds | few clouds | 02d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 18:00:00 | 33.000000 | 5.310000 | 14.310000 | 51.000000 | 1012.000000 |  | 15.380000 | 12.400000 | 10000.000000 | 315.000000 | 2.86 | 2.130000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 19:00:00 | 38.000000 | 6.790000 | 15.460000 | 53.000000 | 1011.000000 | 0.12 | 16.380000 | 9.060000 | 10000.000000 | 313.000000 | 2.82 | 1.860000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 20:00:00 | 43.000000 | 7.170000 | 14.490000 | 58.000000 | 1011.000000 | 0.14 | 15.380000 | 5.280000 | 10000.000000 | 304.000000 | 2.73 | 1.400000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 21:00:00 | 58.000000 | 8.840000 | 14.670000 | 65.000000 | 1011.000000 | 0.15 | 15.380000 | 2.160000 | 10000.000000 | 294.000000 | 2.55 | 1.150000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 22:00:00 | 69.000000 | 10.210000 | 13.860000 | 76.000000 | 1012.000000 | 0.19 | 14.380000 | 0.450000 | 10000.000000 | 293.000000 | 2.05 | 0.640000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201300 | "AUSTRALIA [21201300]" | 4.394250 | -74.132000 | 3050.000000 | Pluviométrica | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 23:00:00 | 75.000000 | 10.790000 | 12.020000 | 90.000000 | 1014.000000 | 0.13 | 12.380000 | 0.000000 | 10000.000000 | 303.000000 | 1.33 | 0.380000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21201300_OWM_Clouds_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Clouds_20220130.png)
![CNE_IDEAM_Station21201300_OWM_Dewpoint_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Dewpoint_20220130.png)
![CNE_IDEAM_Station21201300_OWM_Feelslike_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Feelslike_20220130.png)
![CNE_IDEAM_Station21201300_OWM_Humidity_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Humidity_20220130.png)
![CNE_IDEAM_Station21201300_OWM_Pressure_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Pressure_20220130.png)
![CNE_IDEAM_Station21201300_OWM_Rain_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Rain_20220130.png)
![CNE_IDEAM_Station21201300_OWM_Temp_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Temp_20220130.png)
![CNE_IDEAM_Station21201300_OWM_UVI_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_UVI_20220130.png)
![CNE_IDEAM_Station21201300_OWM_Visibility_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Visibility_20220130.png)
![CNE_IDEAM_Station21201300_OWM_Winddeg_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Winddeg_20220130.png)
![CNE_IDEAM_Station21201300_OWM_Windgust_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Windgust_20220130.png)
![CNE_IDEAM_Station21201300_OWM_Windspeed_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201300_OWM_Windspeed_20220130.png)

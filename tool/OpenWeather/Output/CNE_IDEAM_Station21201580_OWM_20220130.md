
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PASQUILLA [21201580] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201580_OWM_20220130.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220130.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.4465,-74.15483333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.4465&lon=-74.15483333)

| Parameter | Value |
|---|---|
| Code | 21201580 |
| Name | PASQUILLA [21201580] |
| Latitude, ° | 4.4465 |
| Longitude, ° | -74.15483333 |
| Elevation, m | 30 |
| Category | Pluviométrica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1981-11-14 19:00:00 |
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

### (CNE index 2176) Open Weather values for station 21201580 - PASQUILLA [21201580]

JSON data from API OWM:

```
{'lat': 4.4465, 'lon': -74.1548, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643467037, 'sunrise': 1643454715, 'sunset': 1643497645, 'temp': 11.81, 'feels_like': 10.51, 'pressure': 1016, 'humidity': 56, 'dew_point': 3.33, 'uvi': 9.42, 'clouds': 5, 'visibility': 10000, 'wind_speed': 2.3, 'wind_deg': 306, 'wind_gust': 2.3, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, 'hourly': [{'dt': 1643414400, 'temp': 11.81, 'feels_like': 11.32, 'pressure': 1015, 'humidity': 87, 'dew_point': 9.72, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 75, 'wind_gust': 1.34, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.05}}, {'dt': 1643418000, 'temp': 11.81, 'feels_like': 11.32, 'pressure': 1016, 'humidity': 87, 'dew_point': 9.72, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 49, 'wind_gust': 1.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.76}}, {'dt': 1643421600, 'temp': 10.81, 'feels_like': 10.32, 'pressure': 1017, 'humidity': 91, 'dew_point': 9.4, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 351, 'wind_gust': 1.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1643425200, 'temp': 9.81, 'feels_like': 9.81, 'pressure': 1017, 'humidity': 87, 'dew_point': 7.75, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 342, 'wind_gust': 0.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.56}}, {'dt': 1643428800, 'temp': 8.81, 'feels_like': 8.81, 'pressure': 1017, 'humidity': 89, 'dew_point': 7.1, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 274, 'wind_gust': 1.22, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643432400, 'temp': 8.81, 'feels_like': 8.81, 'pressure': 1017, 'humidity': 89, 'dew_point': 7.1, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 292, 'wind_gust': 1.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.42}}, {'dt': 1643436000, 'temp': 7.81, 'feels_like': 7.81, 'pressure': 1016, 'humidity': 89, 'dew_point': 6.11, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 267, 'wind_gust': 0.92, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643439600, 'temp': 7.81, 'feels_like': 7.81, 'pressure': 1017, 'humidity': 92, 'dew_point': 6.59, 'uvi': 0, 'clouds': 29, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 225, 'wind_gust': 1.57, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643443200, 'temp': 5.81, 'feels_like': 5.81, 'pressure': 1016, 'humidity': 92, 'dew_point': 4.61, 'uvi': 0, 'clouds': 25, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 255, 'wind_gust': 1.75, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643446800, 'temp': 4.81, 'feels_like': 4.81, 'pressure': 1016, 'humidity': 91, 'dew_point': 3.47, 'uvi': 0, 'clouds': 28, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 265, 'wind_gust': 1.23, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643450400, 'temp': 3.81, 'feels_like': 3.81, 'pressure': 1017, 'humidity': 92, 'dew_point': 2.63, 'uvi': 0, 'clouds': 23, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 261, 'wind_gust': 1.79, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643454000, 'temp': 2.81, 'feels_like': 2.81, 'pressure': 1017, 'humidity': 91, 'dew_point': 1.49, 'uvi': 0, 'clouds': 21, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 264, 'wind_gust': 1.76, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643457600, 'temp': 3.81, 'feels_like': 3.81, 'pressure': 1018, 'humidity': 87, 'dew_point': 1.85, 'uvi': 0.55, 'clouds': 6, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 272, 'wind_gust': 1.96, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643461200, 'temp': 7.81, 'feels_like': 7.81, 'pressure': 1018, 'humidity': 74, 'dew_point': 3.47, 'uvi': 2.37, 'clouds': 10, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 291, 'wind_gust': 1.68, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643464800, 'temp': 11.81, 'feels_like': 10.72, 'pressure': 1017, 'humidity': 64, 'dew_point': 5.23, 'uvi': 5.6, 'clouds': 6, 'visibility': 10000, 'wind_speed': 2.03, 'wind_deg': 303, 'wind_gust': 2.14, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643468400, 'temp': 14.81, 'feels_like': 13.81, 'pressure': 1016, 'humidity': 56, 'dew_point': 6.13, 'uvi': 9.42, 'clouds': 5, 'visibility': 10000, 'wind_speed': 2.3, 'wind_deg': 306, 'wind_gust': 2.3, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643472000, 'temp': 15.81, 'feels_like': 14.8, 'pressure': 1015, 'humidity': 52, 'dew_point': 5.98, 'uvi': 12.55, 'clouds': 5, 'visibility': 10000, 'wind_speed': 2.49, 'wind_deg': 311, 'wind_gust': 2.57, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643475600, 'temp': 17.81, 'feels_like': 16.95, 'pressure': 1014, 'humidity': 50, 'dew_point': 7.26, 'uvi': 13.66, 'clouds': 10, 'visibility': 10000, 'wind_speed': 2.78, 'wind_deg': 311, 'wind_gust': 2.85, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643479200, 'temp': 16.81, 'feels_like': 15.85, 'pressure': 1012, 'humidity': 50, 'dew_point': 6.34, 'uvi': 12.4, 'clouds': 33, 'visibility': 10000, 'wind_speed': 2.85, 'wind_deg': 308, 'wind_gust': 2.86, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643482800, 'temp': 17.81, 'feels_like': 16.98, 'pressure': 1011, 'humidity': 51, 'dew_point': 7.55, 'uvi': 9.06, 'clouds': 34, 'visibility': 10000, 'wind_speed': 2.66, 'wind_deg': 307, 'wind_gust': 2.9, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643486400, 'temp': 16.81, 'feels_like': 15.98, 'pressure': 1011, 'humidity': 55, 'dew_point': 7.73, 'uvi': 5.28, 'clouds': 33, 'visibility': 10000, 'wind_speed': 2.19, 'wind_deg': 299, 'wind_gust': 2.91, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643490000, 'temp': 16.81, 'feels_like': 16.19, 'pressure': 1011, 'humidity': 63, 'dew_point': 9.73, 'uvi': 2.16, 'clouds': 51, 'visibility': 10000, 'wind_speed': 1.85, 'wind_deg': 293, 'wind_gust': 2.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1643493600, 'temp': 15.81, 'feels_like': 15.43, 'pressure': 1012, 'humidity': 76, 'dew_point': 11.59, 'uvi': 0.45, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 291, 'wind_gust': 2.07, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1643497200, 'temp': 13.81, 'feels_like': 13.57, 'pressure': 1014, 'humidity': 89, 'dew_point': 12.03, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 305, 'wind_gust': 1.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 00:00:00 | 96.000000 | 9.720000 | 11.320000 | 87.000000 | 1015.000000 | 1.05 | 11.810000 | 0.000000 | 10000.000000 | 75.000000 | 1.34 | 0.600000 | 501 | Rain | moderate rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 01:00:00 | 99.000000 | 9.720000 | 11.320000 | 87.000000 | 1016.000000 | 0.76 | 11.810000 | 0.000000 | 10000.000000 | 49.000000 | 1.63 | 0.860000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 02:00:00 | 60.000000 | 9.400000 | 10.320000 | 91.000000 | 1017.000000 | 0.11 | 10.810000 | 0.000000 | 10000.000000 | 351.000000 | 1.16 | 0.490000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 03:00:00 | 82.000000 | 7.750000 | 9.810000 | 87.000000 | 1017.000000 | 0.56 | 9.810000 | 0.000000 | 10000.000000 | 342.000000 | 0.99 | 0.340000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 04:00:00 | 68.000000 | 7.100000 | 8.810000 | 89.000000 | 1017.000000 |  | 8.810000 | 0.000000 | 10000.000000 | 274.000000 | 1.22 | 0.350000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 05:00:00 | 84.000000 | 7.100000 | 8.810000 | 89.000000 | 1017.000000 | 0.42 | 8.810000 | 0.000000 | 10000.000000 | 292.000000 | 1.2 | 0.490000 | 500 | Rain | light rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 06:00:00 | 79.000000 | 6.110000 | 7.810000 | 89.000000 | 1016.000000 |  | 7.810000 | 0.000000 | 10000.000000 | 267.000000 | 0.92 | 0.250000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 07:00:00 | 29.000000 | 6.590000 | 7.810000 | 92.000000 | 1017.000000 |  | 7.810000 | 0.000000 | 10000.000000 | 225.000000 | 1.57 | 0.560000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 08:00:00 | 25.000000 | 4.610000 | 5.810000 | 92.000000 | 1016.000000 |  | 5.810000 | 0.000000 | 10000.000000 | 255.000000 | 1.75 | 0.530000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 09:00:00 | 28.000000 | 3.470000 | 4.810000 | 91.000000 | 1016.000000 |  | 4.810000 | 0.000000 | 10000.000000 | 265.000000 | 1.23 | 0.340000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 10:00:00 | 23.000000 | 2.630000 | 3.810000 | 92.000000 | 1017.000000 |  | 3.810000 | 0.000000 | 10000.000000 | 261.000000 | 1.79 | 0.680000 | 801 | Clouds | few clouds | 02n | 10 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 11:00:00 | 21.000000 | 1.490000 | 2.810000 | 91.000000 | 1017.000000 |  | 2.810000 | 0.000000 | 10000.000000 | 264.000000 | 1.76 | 0.740000 | 801 | Clouds | few clouds | 02n | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 12:00:00 | 6.000000 | 1.850000 | 3.810000 | 87.000000 | 1018.000000 |  | 3.810000 | 0.550000 | 10000.000000 | 272.000000 | 1.96 | 0.520000 | 800 | Clear | clear sky | 01d | 12 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 13:00:00 | 10.000000 | 3.470000 | 7.810000 | 74.000000 | 1018.000000 |  | 7.810000 | 2.370000 | 10000.000000 | 291.000000 | 1.68 | 1.290000 | 800 | Clear | clear sky | 01d | 13 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 14:00:00 | 6.000000 | 5.230000 | 10.720000 | 64.000000 | 1017.000000 |  | 11.810000 | 5.600000 | 10000.000000 | 303.000000 | 2.14 | 2.030000 | 800 | Clear | clear sky | 01d | 14 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 15:00:00 | 5.000000 | 6.130000 | 13.810000 | 56.000000 | 1016.000000 |  | 14.810000 | 9.420000 | 10000.000000 | 306.000000 | 2.3 | 2.300000 | 800 | Clear | clear sky | 01d | 15 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 16:00:00 | 5.000000 | 5.980000 | 14.800000 | 52.000000 | 1015.000000 |  | 15.810000 | 12.550000 | 10000.000000 | 311.000000 | 2.57 | 2.490000 | 800 | Clear | clear sky | 01d | 16 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 17:00:00 | 10.000000 | 7.260000 | 16.950000 | 50.000000 | 1014.000000 |  | 17.810000 | 13.660000 | 10000.000000 | 311.000000 | 2.85 | 2.780000 | 800 | Clear | clear sky | 01d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 18:00:00 | 33.000000 | 6.340000 | 15.850000 | 50.000000 | 1012.000000 |  | 16.810000 | 12.400000 | 10000.000000 | 308.000000 | 2.86 | 2.850000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 19:00:00 | 34.000000 | 7.550000 | 16.980000 | 51.000000 | 1011.000000 |  | 17.810000 | 9.060000 | 10000.000000 | 307.000000 | 2.9 | 2.660000 | 802 | Clouds | scattered clouds | 03d | 19 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 20:00:00 | 33.000000 | 7.730000 | 15.980000 | 55.000000 | 1011.000000 |  | 16.810000 | 5.280000 | 10000.000000 | 299.000000 | 2.91 | 2.190000 | 802 | Clouds | scattered clouds | 03d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 21:00:00 | 51.000000 | 9.730000 | 16.190000 | 63.000000 | 1011.000000 | 0.12 | 16.810000 | 2.160000 | 10000.000000 | 293.000000 | 2.71 | 1.850000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 22:00:00 | 63.000000 | 11.590000 | 15.430000 | 76.000000 | 1012.000000 | 0.2 | 15.810000 | 0.450000 | 10000.000000 | 291.000000 | 2.07 | 1.160000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-29 23:00:00 | 71.000000 | 12.030000 | 13.570000 | 89.000000 | 1014.000000 | 0.16 | 13.810000 | 0.000000 | 10000.000000 | 305.000000 | 1.46 | 0.620000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21201580_OWM_Clouds_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Clouds_20220130.png)
![CNE_IDEAM_Station21201580_OWM_Dewpoint_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Dewpoint_20220130.png)
![CNE_IDEAM_Station21201580_OWM_Feelslike_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Feelslike_20220130.png)
![CNE_IDEAM_Station21201580_OWM_Humidity_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Humidity_20220130.png)
![CNE_IDEAM_Station21201580_OWM_Pressure_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Pressure_20220130.png)
![CNE_IDEAM_Station21201580_OWM_Rain_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Rain_20220130.png)
![CNE_IDEAM_Station21201580_OWM_Temp_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Temp_20220130.png)
![CNE_IDEAM_Station21201580_OWM_UVI_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_UVI_20220130.png)
![CNE_IDEAM_Station21201580_OWM_Visibility_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Visibility_20220130.png)
![CNE_IDEAM_Station21201580_OWM_Winddeg_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Winddeg_20220130.png)
![CNE_IDEAM_Station21201580_OWM_Windgust_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Windgust_20220130.png)
![CNE_IDEAM_Station21201580_OWM_Windspeed_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Windspeed_20220130.png)

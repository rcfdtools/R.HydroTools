
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

* Current date time: 2022-02-03 15:08:03.237034
* Unix time to eval: 1643814483
* Days before (for historical data): 1
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220203.xls
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201580_OWM_20220203.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220203.csv)

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
| Latitude | latitud | lat | Geolocation latitude degrees |
| Longitude | longitud | lon | Geolocation longitude degrees |
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

### (CNE index 2175) Open Weather values for station 21201580 - PASQUILLA [21201580]

JSON data from API OWM:

```
{'lat': 4.4465, 'lon': -74.1548, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643814483, 'sunrise': 1643800331, 'sunset': 1643843304, 'temp': 14.81, 'feels_like': 13.89, 'pressure': 1017, 'humidity': 59, 'dew_point': 6.88, 'uvi': 6.83, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 128, 'wind_gust': 1.98, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1643760000, 'temp': 11.81, 'feels_like': 11.27, 'pressure': 1016, 'humidity': 85, 'dew_point': 9.37, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.49, 'wind_deg': 130, 'wind_gust': 1.97, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643763600, 'temp': 10.81, 'feels_like': 10.19, 'pressure': 1017, 'humidity': 86, 'dew_point': 8.56, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 133, 'wind_gust': 1.96, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643767200, 'temp': 10.81, 'feels_like': 10.22, 'pressure': 1018, 'humidity': 87, 'dew_point': 8.74, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 1.83, 'wind_deg': 133, 'wind_gust': 2.27, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643770800, 'temp': 8.81, 'feels_like': 8, 'pressure': 1018, 'humidity': 87, 'dew_point': 6.77, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.79, 'wind_deg': 132, 'wind_gust': 2.3, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643774400, 'temp': 8.81, 'feels_like': 8.04, 'pressure': 1018, 'humidity': 86, 'dew_point': 6.6, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.74, 'wind_deg': 128, 'wind_gust': 2.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643778000, 'temp': 6.81, 'feels_like': 5.65, 'pressure': 1018, 'humidity': 85, 'dew_point': 4.47, 'uvi': 0, 'clouds': 56, 'visibility': 10000, 'wind_speed': 1.82, 'wind_deg': 121, 'wind_gust': 2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643781600, 'temp': 6.81, 'feels_like': 5.83, 'pressure': 1017, 'humidity': 84, 'dew_point': 4.3, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.66, 'wind_deg': 114, 'wind_gust': 1.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643785200, 'temp': 7.81, 'feels_like': 6.84, 'pressure': 1016, 'humidity': 84, 'dew_point': 5.28, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.79, 'wind_deg': 112, 'wind_gust': 2.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643788800, 'temp': 8.81, 'feels_like': 7.84, 'pressure': 1016, 'humidity': 84, 'dew_point': 6.26, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.96, 'wind_deg': 112, 'wind_gust': 2.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643792400, 'temp': 7.81, 'feels_like': 6.48, 'pressure': 1017, 'humidity': 85, 'dew_point': 5.45, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.18, 'wind_deg': 110, 'wind_gust': 2.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643796000, 'temp': 6.81, 'feels_like': 5.24, 'pressure': 1017, 'humidity': 85, 'dew_point': 4.47, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 111, 'wind_gust': 2.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643799600, 'temp': 7.81, 'feels_like': 6.39, 'pressure': 1017, 'humidity': 86, 'dew_point': 5.62, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.29, 'wind_deg': 111, 'wind_gust': 2.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643803200, 'temp': 7.81, 'feels_like': 6.49, 'pressure': 1018, 'humidity': 83, 'dew_point': 5.11, 'uvi': 0.53, 'clouds': 94, 'visibility': 10000, 'wind_speed': 2.17, 'wind_deg': 107, 'wind_gust': 2.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643806800, 'temp': 9.81, 'feels_like': 9.04, 'pressure': 1018, 'humidity': 75, 'dew_point': 5.6, 'uvi': 1.72, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.92, 'wind_deg': 112, 'wind_gust': 2.55, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643810400, 'temp': 12.81, 'feels_like': 11.84, 'pressure': 1018, 'humidity': 65, 'dew_point': 6.4, 'uvi': 4.07, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 118, 'wind_gust': 2.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643814000, 'temp': 14.81, 'feels_like': 13.89, 'pressure': 1017, 'humidity': 59, 'dew_point': 6.88, 'uvi': 6.83, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 128, 'wind_gust': 1.98, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1643817600, 'temp': 16.81, 'feels_like': 15.98, 'pressure': 1016, 'humidity': 55, 'dew_point': 7.73, 'uvi': 12.64, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.04, 'wind_deg': 291, 'wind_gust': 2.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643821200, 'temp': 16.81, 'feels_like': 15.98, 'pressure': 1014, 'humidity': 55, 'dew_point': 7.73, 'uvi': 13.74, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 248, 'wind_gust': 2.48, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}, {'dt': 1643824800, 'temp': 15.81, 'feels_like': 14.96, 'pressure': 1014, 'humidity': 58, 'dew_point': 7.57, 'uvi': 12.47, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 208, 'wind_gust': 2.15, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1643828400, 'temp': 16.81, 'feels_like': 16.06, 'pressure': 1012, 'humidity': 58, 'dew_point': 8.51, 'uvi': 9.05, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 201, 'wind_gust': 2.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.28}}, {'dt': 1643832000, 'temp': 16.81, 'feels_like': 16.09, 'pressure': 1012, 'humidity': 59, 'dew_point': 8.76, 'uvi': 5.27, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 203, 'wind_gust': 2.4, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1643835600, 'temp': 15.81, 'feels_like': 15.14, 'pressure': 1012, 'humidity': 65, 'dew_point': 9.25, 'uvi': 2.17, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 187, 'wind_gust': 2.33, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1643839200, 'temp': 14.81, 'feels_like': 14.12, 'pressure': 1013, 'humidity': 68, 'dew_point': 8.97, 'uvi': 0.39, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 137, 'wind_gust': 1.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.23}}, {'dt': 1643842800, 'temp': 12.81, 'feels_like': 12.16, 'pressure': 1014, 'humidity': 77, 'dew_point': 8.88, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 122, 'wind_gust': 2.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 00:00:00 | 57.000000 | 9.370000 | 11.270000 | 85.000000 | 1016.000000 |  | 11.810000 | 0.000000 | 10000.000000 | 130.000000 | 1.97 | 1.490000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 01:00:00 | 70.000000 | 8.560000 | 10.190000 | 86.000000 | 1017.000000 |  | 10.810000 | 0.000000 | 10000.000000 | 133.000000 | 1.96 | 1.620000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 02:00:00 | 62.000000 | 8.740000 | 10.220000 | 87.000000 | 1018.000000 |  | 10.810000 | 0.000000 | 10000.000000 | 133.000000 | 2.27 | 1.830000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 03:00:00 | 59.000000 | 6.770000 | 8.000000 | 87.000000 | 1018.000000 |  | 8.810000 | 0.000000 | 10000.000000 | 132.000000 | 2.3 | 1.790000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 04:00:00 | 57.000000 | 6.600000 | 8.040000 | 86.000000 | 1018.000000 |  | 8.810000 | 0.000000 | 10000.000000 | 128.000000 | 2.03 | 1.740000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 05:00:00 | 56.000000 | 4.470000 | 5.650000 | 85.000000 | 1018.000000 |  | 6.810000 | 0.000000 | 10000.000000 | 121.000000 | 2 | 1.820000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 06:00:00 | 93.000000 | 4.300000 | 5.830000 | 84.000000 | 1017.000000 |  | 6.810000 | 0.000000 | 10000.000000 | 114.000000 | 1.7 | 1.660000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 07:00:00 | 100.000000 | 5.280000 | 6.840000 | 84.000000 | 1016.000000 |  | 7.810000 | 0.000000 | 10000.000000 | 112.000000 | 2.03 | 1.790000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 08:00:00 | 100.000000 | 6.260000 | 7.840000 | 84.000000 | 1016.000000 |  | 8.810000 | 0.000000 | 10000.000000 | 112.000000 | 2.2 | 1.960000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 09:00:00 | 99.000000 | 5.450000 | 6.480000 | 85.000000 | 1017.000000 |  | 7.810000 | 0.000000 | 10000.000000 | 110.000000 | 2.41 | 2.180000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 10:00:00 | 99.000000 | 4.470000 | 5.240000 | 85.000000 | 1017.000000 |  | 6.810000 | 0.000000 | 10000.000000 | 111.000000 | 2.54 | 2.260000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 11:00:00 | 99.000000 | 5.620000 | 6.390000 | 86.000000 | 1017.000000 |  | 7.810000 | 0.000000 | 10000.000000 | 111.000000 | 2.73 | 2.290000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 12:00:00 | 94.000000 | 5.110000 | 6.490000 | 83.000000 | 1018.000000 |  | 7.810000 | 0.530000 | 10000.000000 | 107.000000 | 2.76 | 2.170000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 13:00:00 | 100.000000 | 5.600000 | 9.040000 | 75.000000 | 1018.000000 |  | 9.810000 | 1.720000 | 10000.000000 | 112.000000 | 2.55 | 1.920000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 14:00:00 | 97.000000 | 6.400000 | 11.840000 | 65.000000 | 1018.000000 |  | 12.810000 | 4.070000 | 10000.000000 | 118.000000 | 2.07 | 1.150000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 15:00:00 | 90.000000 | 6.880000 | 13.890000 | 59.000000 | 1017.000000 |  | 14.810000 | 6.830000 | 10000.000000 | 128.000000 | 1.98 | 0.580000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 16:00:00 | 82.000000 | 7.730000 | 15.980000 | 55.000000 | 1016.000000 |  | 16.810000 | 12.640000 | 10000.000000 | 291.000000 | 2.54 | 0.040000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 17:00:00 | 81.000000 | 7.730000 | 15.980000 | 55.000000 | 1014.000000 | 0.1 | 16.810000 | 13.740000 | 10000.000000 | 248.000000 | 2.48 | 0.400000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 18:00:00 | 98.000000 | 7.570000 | 14.960000 | 58.000000 | 1014.000000 | 0.24 | 15.810000 | 12.470000 | 10000.000000 | 208.000000 | 2.15 | 0.910000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 19:00:00 | 100.000000 | 8.510000 | 16.060000 | 58.000000 | 1012.000000 | 0.28 | 16.810000 | 9.050000 | 10000.000000 | 201.000000 | 2.27 | 0.700000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 20:00:00 | 88.000000 | 8.760000 | 16.090000 | 59.000000 | 1012.000000 | 0.29 | 16.810000 | 5.270000 | 10000.000000 | 203.000000 | 2.4 | 0.760000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 21:00:00 | 92.000000 | 9.250000 | 15.140000 | 65.000000 | 1012.000000 | 0.2 | 15.810000 | 2.170000 | 10000.000000 | 187.000000 | 2.33 | 0.800000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 22:00:00 | 93.000000 | 8.970000 | 14.120000 | 68.000000 | 1013.000000 | 0.23 | 14.810000 | 0.390000 | 10000.000000 | 137.000000 | 1.93 | 1.010000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-02 23:00:00 | 95.000000 | 8.880000 | 12.160000 | 77.000000 | 1014.000000 | 0.18 | 12.810000 | 0.000000 | 10000.000000 | 122.000000 | 2.3 | 1.460000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21201580_OWM_Clouds_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Clouds_20220203.png)
![CNE_IDEAM_Station21201580_OWM_Dewpoint_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Dewpoint_20220203.png)
![CNE_IDEAM_Station21201580_OWM_Feelslike_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Feelslike_20220203.png)
![CNE_IDEAM_Station21201580_OWM_Humidity_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Humidity_20220203.png)
![CNE_IDEAM_Station21201580_OWM_Pressure_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Pressure_20220203.png)
![CNE_IDEAM_Station21201580_OWM_Rain_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Rain_20220203.png)
![CNE_IDEAM_Station21201580_OWM_Temp_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Temp_20220203.png)
![CNE_IDEAM_Station21201580_OWM_UVI_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_UVI_20220203.png)
![CNE_IDEAM_Station21201580_OWM_Visibility_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Visibility_20220203.png)
![CNE_IDEAM_Station21201580_OWM_Winddeg_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Winddeg_20220203.png)
![CNE_IDEAM_Station21201580_OWM_Windgust_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Windgust_20220203.png)
![CNE_IDEAM_Station21201580_OWM_Windspeed_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Windspeed_20220203.png)

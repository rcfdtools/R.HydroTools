
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

* Current date time: 2022-02-10 14:08:04.180886
* Unix time to eval: 1644329284
* Days before (for historical data): 2
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220210.xls
* CNE IDEAM file downloaded and updated: No
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201580_OWM_20220210.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220210.csv)

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

### (CNE index 2173) Open Weather values for station 21201580 - PASQUILLA [21201580]

JSON data from API OWM:

```
{'lat': 4.4465, 'lon': -74.1548, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644329284, 'sunrise': 1644318729, 'sunset': 1644361772, 'temp': 11.81, 'feels_like': 11.24, 'pressure': 1018, 'humidity': 84, 'dew_point': 9.2, 'uvi': 3.32, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 158, 'wind_gust': 1.59, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644278400, 'temp': 11.81, 'feels_like': 11.45, 'pressure': 1016, 'humidity': 92, 'dew_point': 10.55, 'uvi': 0, 'clouds': 100, 'visibility': 8281, 'wind_speed': 1.05, 'wind_deg': 116, 'wind_gust': 1.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644282000, 'temp': 11.81, 'feels_like': 11.42, 'pressure': 1017, 'humidity': 91, 'dew_point': 10.39, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.41, 'wind_deg': 117, 'wind_gust': 1.99, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644285600, 'temp': 10.81, 'feels_like': 10.32, 'pressure': 1018, 'humidity': 91, 'dew_point': 9.4, 'uvi': 0, 'clouds': 100, 'visibility': 7916, 'wind_speed': 1.63, 'wind_deg': 111, 'wind_gust': 2.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644289200, 'temp': 10.81, 'feels_like': 10.35, 'pressure': 1018, 'humidity': 92, 'dew_point': 9.56, 'uvi': 0, 'clouds': 100, 'visibility': 6796, 'wind_speed': 1.72, 'wind_deg': 105, 'wind_gust': 2.43, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 2.73}}, {'dt': 1644292800, 'temp': 10.81, 'feels_like': 10.37, 'pressure': 1019, 'humidity': 93, 'dew_point': 9.72, 'uvi': 0, 'clouds': 100, 'visibility': 2905, 'wind_speed': 1.23, 'wind_deg': 119, 'wind_gust': 1.83, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.15}}, {'dt': 1644296400, 'temp': 10.81, 'feels_like': 10.35, 'pressure': 1018, 'humidity': 92, 'dew_point': 9.56, 'uvi': 0, 'clouds': 100, 'visibility': 9196, 'wind_speed': 0.61, 'wind_deg': 131, 'wind_gust': 1.22, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.33}}, {'dt': 1644300000, 'temp': 9.81, 'feels_like': 9.81, 'pressure': 1018, 'humidity': 94, 'dew_point': 8.89, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 127, 'wind_gust': 0.79, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.78}}, {'dt': 1644303600, 'temp': 10.81, 'feels_like': 10.37, 'pressure': 1017, 'humidity': 93, 'dew_point': 9.72, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 109, 'wind_gust': 0.93, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.15}}, {'dt': 1644307200, 'temp': 10.81, 'feels_like': 10.35, 'pressure': 1016, 'humidity': 92, 'dew_point': 9.56, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.15, 'wind_deg': 132, 'wind_gust': 0.74, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.33}}, {'dt': 1644310800, 'temp': 10.81, 'feels_like': 10.35, 'pressure': 1016, 'humidity': 92, 'dew_point': 9.56, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.15, 'wind_deg': 187, 'wind_gust': 0.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644314400, 'temp': 10.81, 'feels_like': 10.32, 'pressure': 1016, 'humidity': 91, 'dew_point': 9.4, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 128, 'wind_gust': 0.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644318000, 'temp': 9.81, 'feels_like': 9.81, 'pressure': 1017, 'humidity': 91, 'dew_point': 8.41, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 124, 'wind_gust': 0.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644321600, 'temp': 9.81, 'feels_like': 9.81, 'pressure': 1018, 'humidity': 90, 'dew_point': 8.25, 'uvi': 0.07, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 123, 'wind_gust': 1.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644325200, 'temp': 11.81, 'feels_like': 11.34, 'pressure': 1018, 'humidity': 88, 'dew_point': 9.89, 'uvi': 1.41, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 105, 'wind_gust': 1.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644328800, 'temp': 11.81, 'feels_like': 11.24, 'pressure': 1018, 'humidity': 84, 'dew_point': 9.2, 'uvi': 3.32, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 158, 'wind_gust': 1.59, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644332400, 'temp': 12.81, 'feels_like': 12.18, 'pressure': 1018, 'humidity': 78, 'dew_point': 9.07, 'uvi': 5.57, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 190, 'wind_gust': 1.81, 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'}], 'rain': {'1h': 15.38}}, {'dt': 1644336000, 'temp': 10.81, 'feels_like': 10.01, 'pressure': 1016, 'humidity': 79, 'dew_point': 7.32, 'uvi': 5.67, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 240, 'wind_gust': 2.04, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 3.16}}, {'dt': 1644339600, 'temp': 9.81, 'feels_like': 9.81, 'pressure': 1016, 'humidity': 86, 'dew_point': 7.58, 'uvi': 6.17, 'clouds': 99, 'visibility': 8872, 'wind_speed': 0.32, 'wind_deg': 203, 'wind_gust': 1.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 1}}, {'dt': 1644343200, 'temp': 11.81, 'feels_like': 11.34, 'pressure': 1015, 'humidity': 88, 'dew_point': 9.89, 'uvi': 5.61, 'clouds': 98, 'visibility': 8547, 'wind_speed': 0.1, 'wind_deg': 83, 'wind_gust': 1.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1644346800, 'temp': 12.81, 'feels_like': 12.44, 'pressure': 1015, 'humidity': 88, 'dew_point': 10.87, 'uvi': 5.44, 'clouds': 100, 'visibility': 8009, 'wind_speed': 0.29, 'wind_deg': 17, 'wind_gust': 1.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644350400, 'temp': 12.81, 'feels_like': 12.5, 'pressure': 1014, 'humidity': 90, 'dew_point': 11.21, 'uvi': 3.18, 'clouds': 100, 'visibility': 8545, 'wind_speed': 0.13, 'wind_deg': 18, 'wind_gust': 1.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644354000, 'temp': 13.81, 'feels_like': 13.6, 'pressure': 1014, 'humidity': 90, 'dew_point': 12.2, 'uvi': 1.31, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 136, 'wind_gust': 1.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644357600, 'temp': 13.81, 'feels_like': 13.54, 'pressure': 1015, 'humidity': 88, 'dew_point': 11.86, 'uvi': 0.5, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 134, 'wind_gust': 1.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644361200, 'temp': 12.81, 'feels_like': 12.57, 'pressure': 1016, 'humidity': 93, 'dew_point': 11.71, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 158, 'wind_gust': 1.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 00:00:00 | 100.000000 | 10.550000 | 11.450000 | 92.000000 | 1016.000000 |  | 11.810000 | 0.000000 | 8281.000000 | 116.000000 | 1.75 | 1.050000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 01:00:00 | 100.000000 | 10.390000 | 11.420000 | 91.000000 | 1017.000000 |  | 11.810000 | 0.000000 | 10000.000000 | 117.000000 | 1.99 | 1.410000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 02:00:00 | 100.000000 | 9.400000 | 10.320000 | 91.000000 | 1018.000000 |  | 10.810000 | 0.000000 | 7916.000000 | 111.000000 | 2.33 | 1.630000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 03:00:00 | 100.000000 | 9.560000 | 10.350000 | 92.000000 | 1018.000000 | 2.73 | 10.810000 | 0.000000 | 6796.000000 | 105.000000 | 2.43 | 1.720000 | 501 | Rain | moderate rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 04:00:00 | 100.000000 | 9.720000 | 10.370000 | 93.000000 | 1019.000000 | 1.15 | 10.810000 | 0.000000 | 2905.000000 | 119.000000 | 1.83 | 1.230000 | 501 | Rain | moderate rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 05:00:00 | 100.000000 | 9.560000 | 10.350000 | 92.000000 | 1018.000000 | 1.33 | 10.810000 | 0.000000 | 9196.000000 | 131.000000 | 1.22 | 0.610000 | 501 | Rain | moderate rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 06:00:00 | 100.000000 | 8.890000 | 9.810000 | 94.000000 | 1018.000000 | 1.78 | 9.810000 | 0.000000 | 10000.000000 | 127.000000 | 0.79 | 0.250000 | 501 | Rain | moderate rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 07:00:00 | 100.000000 | 9.720000 | 10.370000 | 93.000000 | 1017.000000 | 1.15 | 10.810000 | 0.000000 | 10000.000000 | 109.000000 | 0.93 | 0.460000 | 501 | Rain | moderate rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 08:00:00 | 100.000000 | 9.560000 | 10.350000 | 92.000000 | 1016.000000 | 1.33 | 10.810000 | 0.000000 | 10000.000000 | 132.000000 | 0.74 | 0.150000 | 501 | Rain | moderate rain | 10n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 09:00:00 | 100.000000 | 9.560000 | 10.350000 | 92.000000 | 1016.000000 |  | 10.810000 | 0.000000 | 10000.000000 | 187.000000 | 0.65 | 0.150000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 10:00:00 | 100.000000 | 9.400000 | 10.320000 | 91.000000 | 1016.000000 |  | 10.810000 | 0.000000 | 10000.000000 | 128.000000 | 0.65 | 0.510000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 11:00:00 | 100.000000 | 8.410000 | 9.810000 | 91.000000 | 1017.000000 |  | 9.810000 | 0.000000 | 10000.000000 | 124.000000 | 0.92 | 0.680000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 12:00:00 | 100.000000 | 8.250000 | 9.810000 | 90.000000 | 1018.000000 |  | 9.810000 | 0.070000 | 10000.000000 | 123.000000 | 1.01 | 0.620000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 13:00:00 | 100.000000 | 9.890000 | 11.340000 | 88.000000 | 1018.000000 |  | 11.810000 | 1.410000 | 10000.000000 | 105.000000 | 1.29 | 0.580000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 14:00:00 | 99.000000 | 9.200000 | 11.240000 | 84.000000 | 1018.000000 |  | 11.810000 | 3.320000 | 10000.000000 | 158.000000 | 1.59 | 0.420000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 15:00:00 | 99.000000 | 9.070000 | 12.180000 | 78.000000 | 1018.000000 | 15.38 | 12.810000 | 5.570000 | 10000.000000 | 190.000000 | 1.81 | 0.200000 | 502 | Rain | heavy intensity rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 16:00:00 | 99.000000 | 7.320000 | 10.010000 | 79.000000 | 1016.000000 | 3.16 | 10.810000 | 5.670000 | 10000.000000 | 240.000000 | 2.04 | 0.490000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 17:00:00 | 99.000000 | 7.580000 | 9.810000 | 86.000000 | 1016.000000 | 1 | 9.810000 | 6.170000 | 8872.000000 | 203.000000 | 1.67 | 0.320000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 18:00:00 | 98.000000 | 9.890000 | 11.340000 | 88.000000 | 1015.000000 | 0.36 | 11.810000 | 5.610000 | 8547.000000 | 83.000000 | 1.38 | 0.100000 | 500 | Rain | light rain | 10d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 19:00:00 | 100.000000 | 10.870000 | 12.440000 | 88.000000 | 1015.000000 |  | 12.810000 | 5.440000 | 8009.000000 | 17.000000 | 1.34 | 0.290000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 20:00:00 | 100.000000 | 11.210000 | 12.500000 | 90.000000 | 1014.000000 |  | 12.810000 | 3.180000 | 8545.000000 | 18.000000 | 1.21 | 0.130000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 21:00:00 | 100.000000 | 12.200000 | 13.600000 | 90.000000 | 1014.000000 |  | 13.810000 | 1.310000 | 10000.000000 | 136.000000 | 1.3 | 0.360000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 22:00:00 | 100.000000 | 11.860000 | 13.540000 | 88.000000 | 1015.000000 |  | 13.810000 | 0.500000 | 10000.000000 | 134.000000 | 1.57 | 0.480000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-08 23:00:00 | 100.000000 | 11.710000 | 12.570000 | 93.000000 | 1016.000000 |  | 12.810000 | 0.000000 | 10000.000000 | 158.000000 | 1.25 | 0.320000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21201580_OWM_Clouds_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Clouds_20220210.png)
![CNE_IDEAM_Station21201580_OWM_Dewpoint_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Dewpoint_20220210.png)
![CNE_IDEAM_Station21201580_OWM_Feelslike_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Feelslike_20220210.png)
![CNE_IDEAM_Station21201580_OWM_Humidity_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Humidity_20220210.png)
![CNE_IDEAM_Station21201580_OWM_Pressure_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Pressure_20220210.png)
![CNE_IDEAM_Station21201580_OWM_Rain_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Rain_20220210.png)
![CNE_IDEAM_Station21201580_OWM_Temp_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Temp_20220210.png)
![CNE_IDEAM_Station21201580_OWM_UVI_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_UVI_20220210.png)
![CNE_IDEAM_Station21201580_OWM_Visibility_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Visibility_20220210.png)
![CNE_IDEAM_Station21201580_OWM_Winddeg_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Winddeg_20220210.png)
![CNE_IDEAM_Station21201580_OWM_Windgust_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Windgust_20220210.png)
![CNE_IDEAM_Station21201580_OWM_Windspeed_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Windspeed_20220210.png)

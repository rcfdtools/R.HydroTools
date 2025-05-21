
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

* Current date time: 2022-02-13 07:30:06.495901
* Unix time to eval: 1644564606
* Days before (for historical data): 2
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220213.xls
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201580_OWM_20220213.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220213.csv)

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
{'lat': 4.4465, 'lon': -74.1548, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644564606, 'sunrise': 1644577916, 'sunset': 1644620996, 'temp': 7.81, 'feels_like': 7.81, 'pressure': 1014, 'humidity': 91, 'dew_point': 6.43, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 220, 'wind_gust': 0.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, 'hourly': [{'dt': 1644537600, 'temp': 10.28, 'feels_like': 9.77, 'pressure': 1014, 'humidity': 92, 'dew_point': 9.04, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 98, 'wind_gust': 1.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644541200, 'temp': 9.98, 'feels_like': 9.98, 'pressure': 1015, 'humidity': 91, 'dew_point': 8.58, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 105, 'wind_gust': 1.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644544800, 'temp': 9.91, 'feels_like': 9.91, 'pressure': 1015, 'humidity': 89, 'dew_point': 8.18, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 103, 'wind_gust': 1.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644548400, 'temp': 9.3, 'feels_like': 9.3, 'pressure': 1016, 'humidity': 90, 'dew_point': 7.75, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 105, 'wind_gust': 1.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644552000, 'temp': 8.96, 'feels_like': 8.96, 'pressure': 1016, 'humidity': 90, 'dew_point': 7.41, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 112, 'wind_gust': 1.34, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644555600, 'temp': 8.87, 'feels_like': 8.87, 'pressure': 1016, 'humidity': 90, 'dew_point': 7.32, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 110, 'wind_gust': 1.24, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644559200, 'temp': 8.65, 'feels_like': 8.65, 'pressure': 1015, 'humidity': 90, 'dew_point': 7.1, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 131, 'wind_gust': 1.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644562800, 'temp': 7.81, 'feels_like': 7.81, 'pressure': 1014, 'humidity': 90, 'dew_point': 6.27, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 153, 'wind_gust': 0.94, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644566400, 'temp': 7.81, 'feels_like': 7.81, 'pressure': 1014, 'humidity': 91, 'dew_point': 6.43, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 220, 'wind_gust': 0.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644570000, 'temp': 7.81, 'feels_like': 7.81, 'pressure': 1014, 'humidity': 92, 'dew_point': 6.59, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 246, 'wind_gust': 0.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644573600, 'temp': 6.81, 'feels_like': 6.81, 'pressure': 1014, 'humidity': 91, 'dew_point': 5.45, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 278, 'wind_gust': 0.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644577200, 'temp': 6.81, 'feels_like': 6.81, 'pressure': 1015, 'humidity': 90, 'dew_point': 5.29, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 264, 'wind_gust': 0.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644580800, 'temp': 7.81, 'feels_like': 7.81, 'pressure': 1015, 'humidity': 86, 'dew_point': 5.62, 'uvi': 0.44, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 36, 'wind_gust': 0.72, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644584400, 'temp': 11.81, 'feels_like': 11.19, 'pressure': 1016, 'humidity': 82, 'dew_point': 8.84, 'uvi': 2.45, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 81, 'wind_gust': 0.98, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644588000, 'temp': 13.81, 'feels_like': 13.26, 'pressure': 1016, 'humidity': 77, 'dew_point': 9.85, 'uvi': 5.78, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 109, 'wind_gust': 1.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644591600, 'temp': 14.81, 'feels_like': 14.15, 'pressure': 1015, 'humidity': 69, 'dew_point': 9.18, 'uvi': 9.69, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.22, 'wind_deg': 350, 'wind_gust': 1.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644595200, 'temp': 15.81, 'feels_like': 15.17, 'pressure': 1014, 'humidity': 66, 'dew_point': 9.48, 'uvi': 12.74, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 321, 'wind_gust': 1.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644598800, 'temp': 17.81, 'feels_like': 17.4, 'pressure': 1012, 'humidity': 67, 'dew_point': 11.61, 'uvi': 13.86, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 323, 'wind_gust': 2.51, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644602400, 'temp': 16.81, 'feels_like': 16.45, 'pressure': 1012, 'humidity': 73, 'dew_point': 11.95, 'uvi': 12.6, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 314, 'wind_gust': 2.49, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644606000, 'temp': 17.81, 'feels_like': 17.66, 'pressure': 1011, 'humidity': 77, 'dew_point': 13.73, 'uvi': 8.92, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 307, 'wind_gust': 2.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644609600, 'temp': 17.81, 'feels_like': 17.81, 'pressure': 1011, 'humidity': 83, 'dew_point': 14.89, 'uvi': 5.22, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 272, 'wind_gust': 1.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644613200, 'temp': 14.81, 'feels_like': 14.59, 'pressure': 1011, 'humidity': 86, 'dew_point': 12.49, 'uvi': 2.15, 'clouds': 91, 'visibility': 8372, 'wind_speed': 0.56, 'wind_deg': 247, 'wind_gust': 1.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644616800, 'temp': 14.81, 'feels_like': 14.72, 'pressure': 1012, 'humidity': 91, 'dew_point': 13.36, 'uvi': 0.5, 'clouds': 93, 'visibility': 6986, 'wind_speed': 0.27, 'wind_deg': 237, 'wind_gust': 1.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644620400, 'temp': 13.81, 'feels_like': 13.75, 'pressure': 1013, 'humidity': 96, 'dew_point': 13.18, 'uvi': 0, 'clouds': 92, 'visibility': 1811, 'wind_speed': 0.36, 'wind_deg': 115, 'wind_gust': 1.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 00:00:00 | 76.000000 | 9.040000 | 9.770000 | 92.000000 | 1014.000000 |  | 10.280000 | 0.000000 | 10000.000000 | 98.000000 | 1.61 | 1.370000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 01:00:00 | 93.000000 | 8.580000 | 9.980000 | 91.000000 | 1015.000000 |  | 9.980000 | 0.000000 | 10000.000000 | 105.000000 | 1.66 | 1.320000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 02:00:00 | 89.000000 | 8.180000 | 9.910000 | 89.000000 | 1015.000000 |  | 9.910000 | 0.000000 | 10000.000000 | 103.000000 | 1.24 | 0.910000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 03:00:00 | 85.000000 | 7.750000 | 9.300000 | 90.000000 | 1016.000000 |  | 9.300000 | 0.000000 | 10000.000000 | 105.000000 | 1.32 | 0.920000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 04:00:00 | 77.000000 | 7.410000 | 8.960000 | 90.000000 | 1016.000000 |  | 8.960000 | 0.000000 | 10000.000000 | 112.000000 | 1.34 | 0.960000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 05:00:00 | 77.000000 | 7.320000 | 8.870000 | 90.000000 | 1016.000000 |  | 8.870000 | 0.000000 | 10000.000000 | 110.000000 | 1.24 | 0.960000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 06:00:00 | 75.000000 | 7.100000 | 8.650000 | 90.000000 | 1015.000000 |  | 8.650000 | 0.000000 | 10000.000000 | 131.000000 | 1.11 | 0.750000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 07:00:00 | 90.000000 | 6.270000 | 7.810000 | 90.000000 | 1014.000000 |  | 7.810000 | 0.000000 | 10000.000000 | 153.000000 | 0.94 | 0.590000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 08:00:00 | 95.000000 | 6.430000 | 7.810000 | 91.000000 | 1014.000000 |  | 7.810000 | 0.000000 | 10000.000000 | 220.000000 | 0.66 | 0.260000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 09:00:00 | 97.000000 | 6.590000 | 7.810000 | 92.000000 | 1014.000000 |  | 7.810000 | 0.000000 | 10000.000000 | 246.000000 | 0.74 | 0.240000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 10:00:00 | 98.000000 | 5.450000 | 6.810000 | 91.000000 | 1014.000000 |  | 6.810000 | 0.000000 | 10000.000000 | 278.000000 | 0.57 | 0.280000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 11:00:00 | 97.000000 | 5.290000 | 6.810000 | 90.000000 | 1015.000000 |  | 6.810000 | 0.000000 | 10000.000000 | 264.000000 | 0.52 | 0.410000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 12:00:00 | 84.000000 | 5.620000 | 7.810000 | 86.000000 | 1015.000000 |  | 7.810000 | 0.440000 | 10000.000000 | 36.000000 | 0.72 | 0.330000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 13:00:00 | 95.000000 | 8.840000 | 11.190000 | 82.000000 | 1016.000000 |  | 11.810000 | 2.450000 | 10000.000000 | 81.000000 | 0.98 | 0.280000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 14:00:00 | 93.000000 | 9.850000 | 13.260000 | 77.000000 | 1016.000000 |  | 13.810000 | 5.780000 | 10000.000000 | 109.000000 | 1.24 | 0.280000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 15:00:00 | 91.000000 | 9.180000 | 14.150000 | 69.000000 | 1015.000000 |  | 14.810000 | 9.690000 | 10000.000000 | 350.000000 | 1.8 | 0.220000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 16:00:00 | 87.000000 | 9.480000 | 15.170000 | 66.000000 | 1014.000000 |  | 15.810000 | 12.740000 | 10000.000000 | 321.000000 | 1.92 | 0.810000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 17:00:00 | 82.000000 | 11.610000 | 17.400000 | 67.000000 | 1012.000000 |  | 17.810000 | 13.860000 | 10000.000000 | 323.000000 | 2.51 | 0.960000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 18:00:00 | 73.000000 | 11.950000 | 16.450000 | 73.000000 | 1012.000000 |  | 16.810000 | 12.600000 | 10000.000000 | 314.000000 | 2.49 | 1.090000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 19:00:00 | 87.000000 | 13.730000 | 17.660000 | 77.000000 | 1011.000000 |  | 17.810000 | 8.920000 | 10000.000000 | 307.000000 | 2.16 | 0.770000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 20:00:00 | 90.000000 | 14.890000 | 17.810000 | 83.000000 | 1011.000000 |  | 17.810000 | 5.220000 | 10000.000000 | 272.000000 | 1.89 | 0.680000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 21:00:00 | 91.000000 | 12.490000 | 14.590000 | 86.000000 | 1011.000000 |  | 14.810000 | 2.150000 | 8372.000000 | 247.000000 | 1.58 | 0.560000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 22:00:00 | 93.000000 | 13.360000 | 14.720000 | 91.000000 | 1012.000000 |  | 14.810000 | 0.500000 | 6986.000000 | 237.000000 | 1.71 | 0.270000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201580 | "PASQUILLA [21201580]" | 4.446500 | -74.154833 | 30.000000 | Pluviométrica | Convencional | Activa | 1981-11-14 19:00:00 | NaT | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-02-11 23:00:00 | 92.000000 | 13.180000 | 13.750000 | 96.000000 | 1013.000000 |  | 13.810000 | 0.000000 | 1811.000000 | 115.000000 | 1.17 | 0.360000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21201580_OWM_Clouds_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Clouds_20220213.png)
![CNE_IDEAM_Station21201580_OWM_Dewpoint_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Dewpoint_20220213.png)
![CNE_IDEAM_Station21201580_OWM_Feelslike_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Feelslike_20220213.png)
![CNE_IDEAM_Station21201580_OWM_Humidity_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Humidity_20220213.png)
![CNE_IDEAM_Station21201580_OWM_Pressure_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Pressure_20220213.png)
![CNE_IDEAM_Station21201580_OWM_Rain_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Rain_20220213.png)
![CNE_IDEAM_Station21201580_OWM_Temp_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Temp_20220213.png)
![CNE_IDEAM_Station21201580_OWM_UVI_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_UVI_20220213.png)
![CNE_IDEAM_Station21201580_OWM_Visibility_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Visibility_20220213.png)
![CNE_IDEAM_Station21201580_OWM_Winddeg_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Winddeg_20220213.png)
![CNE_IDEAM_Station21201580_OWM_Windgust_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Windgust_20220213.png)
![CNE_IDEAM_Station21201580_OWM_Windspeed_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201580_OWM_Windspeed_20220213.png)

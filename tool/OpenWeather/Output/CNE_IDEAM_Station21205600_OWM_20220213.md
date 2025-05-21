
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - VELODROMO 1 D MAYO [21205600] - Historical

Study case: Weather evaluation from historical openweathermap data for the CNE IDEAM network stations in Bogot� - Colombia - Suram�rica

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
* CNE IDEAM technology filter: ['All', 'Autom�tica sin Telemetr�a']
* CNE IDEAM status filter: ['All', 'Activa', 'En Mantenimiento']
* CNE IDEAM state filter: ['Bogot�']
* CNE IDEAM county filter: ['All']
* CNE IDEAM stream filter: ['All']
* CNE IDEAM operator filter: ['All']
* CNE IDEAM hydro area filter: ['All']
* CNE IDEAM hydro zone filter: ['All']
* CNE IDEAM hydro subzone filter: ['All']
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21205600_OWM_20220213.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220213.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.61666667,-74.06666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.61666667&lon=-74.06666667)

| Parameter | Value |
|---|---|
| Code | 21205600 |
| Name | VELODROMO 1 D MAYO [21205600] |
| Latitude, � | 4.61666667 |
| Longitude, � | -74.06666667 |
| Elevation, m | 2650 |
| Category | Meteorol�gica Especial |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1986-03-15 00:00:00 |
| Suspension date | 1993-06-15 00:00:00 |
| State | Bogot� |
| County | Bogota, D.C |
| Stream | Cauca |
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

### (CNE index 2226) Open Weather values for station 21205600 - VELODROMO 1 D MAYO [21205600]

JSON data from API OWM:

```
{'lat': 4.6167, 'lon': -74.0667, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644564606, 'sunrise': 1644577905, 'sunset': 1644620965, 'temp': 9.13, 'feels_like': 8.61, 'pressure': 1024, 'humidity': 93, 'dew_point': 8.06, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 40, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, 'hourly': [{'dt': 1644537600, 'temp': 11.53, 'feels_like': 11.17, 'pressure': 1014, 'humidity': 93, 'dew_point': 10.44, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 116, 'wind_gust': 1.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644541200, 'temp': 11.52, 'feels_like': 11.13, 'pressure': 1015, 'humidity': 92, 'dew_point': 10.27, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 125, 'wind_gust': 1.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644544800, 'temp': 11.47, 'feels_like': 11.05, 'pressure': 1015, 'humidity': 91, 'dew_point': 10.05, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 124, 'wind_gust': 1.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644548400, 'temp': 11.01, 'feels_like': 10.57, 'pressure': 1016, 'humidity': 92, 'dew_point': 9.76, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 135, 'wind_gust': 1.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644552000, 'temp': 10.73, 'feels_like': 10.26, 'pressure': 1016, 'humidity': 92, 'dew_point': 9.48, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 142, 'wind_gust': 1.08, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644555600, 'temp': 10.56, 'feels_like': 10.1, 'pressure': 1015, 'humidity': 93, 'dew_point': 9.48, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 136, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644559200, 'temp': 10.45, 'feels_like': 9.98, 'pressure': 1014, 'humidity': 93, 'dew_point': 9.37, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 161, 'wind_gust': 1.04, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644562800, 'temp': 9.13, 'feels_like': 8.61, 'pressure': 1024, 'humidity': 93, 'dew_point': 8.06, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 40, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644566400, 'temp': 9.13, 'feels_like': 9.13, 'pressure': 1023, 'humidity': 100, 'dew_point': 9.13, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644570000, 'temp': 9.13, 'feels_like': 9.13, 'pressure': 1024, 'humidity': 100, 'dew_point': 9.13, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644573600, 'temp': 8.13, 'feels_like': 8.13, 'pressure': 1023, 'humidity': 100, 'dew_point': 8.13, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1644577200, 'temp': 8.13, 'feels_like': 8.13, 'pressure': 1024, 'humidity': 100, 'dew_point': 8.13, 'uvi': 0, 'clouds': 40, 'visibility': 8000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1644580800, 'temp': 9.13, 'feels_like': 7.74, 'pressure': 1025, 'humidity': 100, 'dew_point': 9.13, 'uvi': 0.54, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 70, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1644584400, 'temp': 13.13, 'feels_like': 12.64, 'pressure': 1025, 'humidity': 82, 'dew_point': 10.13, 'uvi': 2.47, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 30, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1644588000, 'temp': 15.13, 'feels_like': 14.45, 'pressure': 1026, 'humidity': 67, 'dew_point': 9.05, 'uvi': 5.83, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 90, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1644591600, 'temp': 16.13, 'feels_like': 15.34, 'pressure': 1025, 'humidity': 59, 'dew_point': 8.12, 'uvi': 9.79, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644595200, 'temp': 17.13, 'feels_like': 16.44, 'pressure': 1025, 'humidity': 59, 'dew_point': 9.06, 'uvi': 12.22, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644598800, 'temp': 19.13, 'feels_like': 18.2, 'pressure': 1024, 'humidity': 42, 'dew_point': 5.93, 'uvi': 13.3, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 280, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644602400, 'temp': 18.13, 'feels_like': 17.54, 'pressure': 1023, 'humidity': 59, 'dew_point': 10, 'uvi': 12.08, 'clouds': 75, 'visibility': 10000, 'wind_speed': 6.17, 'wind_deg': 290, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644606000, 'temp': 19.13, 'feels_like': 18.56, 'pressure': 1022, 'humidity': 56, 'dew_point': 10.16, 'uvi': 7.84, 'clouds': 75, 'visibility': 7000, 'wind_speed': 6.17, 'wind_deg': 280, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644609600, 'temp': 19.13, 'feels_like': 18.56, 'pressure': 1021, 'humidity': 56, 'dew_point': 10.16, 'uvi': 4.58, 'clouds': 75, 'visibility': 8000, 'wind_speed': 6.69, 'wind_deg': 270, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644613200, 'temp': 16.13, 'feels_like': 15.55, 'pressure': 1021, 'humidity': 67, 'dew_point': 10.01, 'uvi': 1.88, 'clouds': 40, 'visibility': 8000, 'wind_speed': 5.66, 'wind_deg': 260, 'weather': [{'id': 211, 'main': 'Thunderstorm', 'description': 'thunderstorm', 'icon': '11d'}]}, {'dt': 1644616800, 'temp': 16.13, 'feels_like': 15.55, 'pressure': 1022, 'humidity': 67, 'dew_point': 10.01, 'uvi': 0.39, 'clouds': 40, 'visibility': 8000, 'wind_speed': 3.09, 'wind_deg': 300, 'weather': [{'id': 211, 'main': 'Thunderstorm', 'description': 'thunderstorm', 'icon': '11d'}]}, {'dt': 1644620400, 'temp': 15.13, 'feels_like': 14.58, 'pressure': 1022, 'humidity': 72, 'dew_point': 10.12, 'uvi': 0, 'clouds': 40, 'visibility': 9000, 'wind_speed': 2.06, 'wind_deg': 10, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 00:00:00 | 90.000000 | 10.440000 | 11.170000 | 93.000000 | 1014.000000 |  | 11.530000 | 0.000000 | 10000.000000 | 116.000000 | 1.46 | 0.970000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 01:00:00 | 99.000000 | 10.270000 | 11.130000 | 92.000000 | 1015.000000 |  | 11.520000 | 0.000000 | 10000.000000 | 125.000000 | 1.39 | 0.870000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 02:00:00 | 98.000000 | 10.050000 | 11.050000 | 91.000000 | 1015.000000 |  | 11.470000 | 0.000000 | 10000.000000 | 124.000000 | 1.07 | 0.680000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 03:00:00 | 95.000000 | 9.760000 | 10.570000 | 92.000000 | 1016.000000 |  | 11.010000 | 0.000000 | 10000.000000 | 135.000000 | 1.12 | 0.760000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 04:00:00 | 90.000000 | 9.480000 | 10.260000 | 92.000000 | 1016.000000 |  | 10.730000 | 0.000000 | 10000.000000 | 142.000000 | 1.08 | 0.750000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 05:00:00 | 90.000000 | 9.480000 | 10.100000 | 93.000000 | 1015.000000 |  | 10.560000 | 0.000000 | 10000.000000 | 136.000000 | 0.91 | 0.730000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 06:00:00 | 80.000000 | 9.370000 | 9.980000 | 93.000000 | 1014.000000 |  | 10.450000 | 0.000000 | 10000.000000 | 161.000000 | 1.04 | 0.740000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 07:00:00 | 75.000000 | 8.060000 | 8.610000 | 93.000000 | 1024.000000 |  | 9.130000 | 0.000000 | 10000.000000 | 40.000000 |  | 1.540000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 08:00:00 | 75.000000 | 9.130000 | 9.130000 | 100.000000 | 1023.000000 |  | 9.130000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 09:00:00 | 75.000000 | 9.130000 | 9.130000 | 100.000000 | 1024.000000 |  | 9.130000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 10:00:00 | 20.000000 | 8.130000 | 8.130000 | 100.000000 | 1023.000000 |  | 8.130000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 801 | Clouds | few clouds | 02n | 10 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 11:00:00 | 40.000000 | 8.130000 | 8.130000 | 100.000000 | 1024.000000 |  | 8.130000 | 0.000000 | 8000.000000 | 0.000000 |  | 1.030000 | 741 | Fog | fog | 50n | 11 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 12:00:00 | 40.000000 | 9.130000 | 7.740000 | 100.000000 | 1025.000000 |  | 9.130000 | 0.540000 | 10000.000000 | 70.000000 |  | 2.570000 | 741 | Fog | fog | 50d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 13:00:00 | 40.000000 | 10.130000 | 12.640000 | 82.000000 | 1025.000000 |  | 13.130000 | 2.470000 | 10000.000000 | 30.000000 |  | 2.570000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 14:00:00 | 40.000000 | 9.050000 | 14.450000 | 67.000000 | 1026.000000 |  | 15.130000 | 5.830000 | 10000.000000 | 90.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 15:00:00 | 75.000000 | 8.120000 | 15.340000 | 59.000000 | 1025.000000 |  | 16.130000 | 9.790000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 16:00:00 | 75.000000 | 9.060000 | 16.440000 | 59.000000 | 1025.000000 |  | 17.130000 | 12.220000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 17:00:00 | 75.000000 | 5.930000 | 18.200000 | 42.000000 | 1024.000000 |  | 19.130000 | 13.300000 | 10000.000000 | 280.000000 |  | 2.570000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 18:00:00 | 75.000000 | 10.000000 | 17.540000 | 59.000000 | 1023.000000 |  | 18.130000 | 12.080000 | 10000.000000 | 290.000000 |  | 6.170000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 19:00:00 | 75.000000 | 10.160000 | 18.560000 | 56.000000 | 1022.000000 |  | 19.130000 | 7.840000 | 7000.000000 | 280.000000 |  | 6.170000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 20:00:00 | 75.000000 | 10.160000 | 18.560000 | 56.000000 | 1021.000000 |  | 19.130000 | 4.580000 | 8000.000000 | 270.000000 |  | 6.690000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![11d.png](http://openweathermap.org/img/w/11d.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 21:00:00 | 40.000000 | 10.010000 | 15.550000 | 67.000000 | 1021.000000 |  | 16.130000 | 1.880000 | 8000.000000 | 260.000000 |  | 5.660000 | 211 | Thunderstorm | thunderstorm | 11d | 21 |
| ![11d.png](http://openweathermap.org/img/w/11d.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 22:00:00 | 40.000000 | 10.010000 | 15.550000 | 67.000000 | 1022.000000 |  | 16.130000 | 0.390000 | 8000.000000 | 300.000000 |  | 3.090000 | 211 | Thunderstorm | thunderstorm | 11d | 22 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21205600 | "VELODROMO 1 D MAYO [21205600]" | 4.616667 | -74.066667 | 2650.000000 | Meteorol�gica Especial | Convencional | Suspendida | 1986-03-15 00:00:00 | 1993-06-15 00:00:00 | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 23:00:00 | 40.000000 | 10.120000 | 14.580000 | 72.000000 | 1022.000000 |  | 15.130000 | 0.000000 | 9000.000000 | 10.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03d | 23 |


### Weather plots

![CNE_IDEAM_Station21205600_OWM_Clouds_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205600_OWM_Clouds_20220213.png)
![CNE_IDEAM_Station21205600_OWM_Dewpoint_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205600_OWM_Dewpoint_20220213.png)
![CNE_IDEAM_Station21205600_OWM_Feelslike_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205600_OWM_Feelslike_20220213.png)
![CNE_IDEAM_Station21205600_OWM_Humidity_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205600_OWM_Humidity_20220213.png)
![CNE_IDEAM_Station21205600_OWM_Pressure_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205600_OWM_Pressure_20220213.png)
![CNE_IDEAM_Station21205600_OWM_Rain_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205600_OWM_Rain_20220213.png)
![CNE_IDEAM_Station21205600_OWM_Temp_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205600_OWM_Temp_20220213.png)
![CNE_IDEAM_Station21205600_OWM_UVI_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205600_OWM_UVI_20220213.png)
![CNE_IDEAM_Station21205600_OWM_Visibility_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205600_OWM_Visibility_20220213.png)
![CNE_IDEAM_Station21205600_OWM_Winddeg_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205600_OWM_Winddeg_20220213.png)
![CNE_IDEAM_Station21205600_OWM_Windgust_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205600_OWM_Windgust_20220213.png)
![CNE_IDEAM_Station21205600_OWM_Windspeed_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205600_OWM_Windspeed_20220213.png)


## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - VEGAS LAS HACIENDA [21206230] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206230_OWM_20220213.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220213.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.66166667,-74.15141944) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.66166667&lon=-74.15141944)

| Parameter | Value |
|---|---|
| Code | 21206230 |
| Name | VEGAS LAS HACIENDA [21206230] |
| Latitude, � | 4.66166667 |
| Longitude, � | -74.15141944 |
| Elevation, m | 2543 |
| Category | Clim�tica Ordinaria |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1987-08-15 00:00:00 |
| Suspension date | 2011-05-10 00:00:00 |
| State | Bogot� |
| County | Bogota, D.C |
| Stream | Quebrada La Baja |
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

### (CNE index 1155) Open Weather values for station 21206230 - VEGAS LAS HACIENDA [21206230]

JSON data from API OWM:

```
{'lat': 4.6617, 'lon': -74.1514, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644564606, 'sunrise': 1644577928, 'sunset': 1644620983, 'temp': 10.05, 'feels_like': 9.54, 'pressure': 1024, 'humidity': 93, 'dew_point': 8.97, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 40, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, 'hourly': [{'dt': 1644537600, 'temp': 13.05, 'feels_like': 12.71, 'pressure': 1023, 'humidity': 88, 'dew_point': 11.11, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 170, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644541200, 'temp': 12.05, 'feels_like': 11.77, 'pressure': 1024, 'humidity': 94, 'dew_point': 11.11, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644544800, 'temp': 12.05, 'feels_like': 11.77, 'pressure': 1025, 'humidity': 94, 'dew_point': 11.11, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644548400, 'temp': 12.05, 'feels_like': 11.92, 'pressure': 1026, 'humidity': 100, 'dew_point': 12.05, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 20, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644552000, 'temp': 12.05, 'feels_like': 11.77, 'pressure': 1025, 'humidity': 94, 'dew_point': 11.11, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1644555600, 'temp': 11.05, 'feels_like': 10.64, 'pressure': 1025, 'humidity': 93, 'dew_point': 9.96, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1644559200, 'temp': 11.05, 'feels_like': 10.64, 'pressure': 1024, 'humidity': 93, 'dew_point': 9.96, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 360, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1644562800, 'temp': 10.05, 'feels_like': 9.54, 'pressure': 1024, 'humidity': 93, 'dew_point': 8.97, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 40, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644566400, 'temp': 10.05, 'feels_like': 9.72, 'pressure': 1023, 'humidity': 100, 'dew_point': 10.05, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644570000, 'temp': 10.05, 'feels_like': 9.72, 'pressure': 1024, 'humidity': 100, 'dew_point': 10.05, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644573600, 'temp': 9.05, 'feels_like': 9.05, 'pressure': 1023, 'humidity': 100, 'dew_point': 9.05, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1644577200, 'temp': 9.05, 'feels_like': 9.05, 'pressure': 1024, 'humidity': 100, 'dew_point': 9.05, 'uvi': 0, 'clouds': 40, 'visibility': 8000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1644580800, 'temp': 10.05, 'feels_like': 9.72, 'pressure': 1025, 'humidity': 100, 'dew_point': 10.05, 'uvi': 0.54, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 70, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1644584400, 'temp': 14.05, 'feels_like': 13.65, 'pressure': 1025, 'humidity': 82, 'dew_point': 11.03, 'uvi': 2.47, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 30, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1644588000, 'temp': 16.05, 'feels_like': 15.46, 'pressure': 1026, 'humidity': 67, 'dew_point': 9.93, 'uvi': 5.83, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 90, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1644591600, 'temp': 17.05, 'feels_like': 16.35, 'pressure': 1025, 'humidity': 59, 'dew_point': 8.99, 'uvi': 9.79, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644595200, 'temp': 18.05, 'feels_like': 17.45, 'pressure': 1025, 'humidity': 59, 'dew_point': 9.92, 'uvi': 12.22, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644598800, 'temp': 20.05, 'feels_like': 19.21, 'pressure': 1024, 'humidity': 42, 'dew_point': 6.76, 'uvi': 13.3, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 280, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644602400, 'temp': 19.05, 'feels_like': 18.55, 'pressure': 1023, 'humidity': 59, 'dew_point': 10.86, 'uvi': 12.08, 'clouds': 75, 'visibility': 10000, 'wind_speed': 6.17, 'wind_deg': 290, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644606000, 'temp': 20.05, 'feels_like': 19.57, 'pressure': 1022, 'humidity': 56, 'dew_point': 11.01, 'uvi': 7.84, 'clouds': 75, 'visibility': 7000, 'wind_speed': 6.17, 'wind_deg': 280, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644609600, 'temp': 20.05, 'feels_like': 19.57, 'pressure': 1021, 'humidity': 56, 'dew_point': 11.01, 'uvi': 4.58, 'clouds': 75, 'visibility': 8000, 'wind_speed': 6.69, 'wind_deg': 270, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644613200, 'temp': 17.05, 'feels_like': 16.56, 'pressure': 1021, 'humidity': 67, 'dew_point': 10.88, 'uvi': 1.88, 'clouds': 40, 'visibility': 8000, 'wind_speed': 5.66, 'wind_deg': 260, 'weather': [{'id': 211, 'main': 'Thunderstorm', 'description': 'thunderstorm', 'icon': '11d'}, {'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1644616800, 'temp': 17.05, 'feels_like': 16.56, 'pressure': 1022, 'humidity': 67, 'dew_point': 10.88, 'uvi': 0.39, 'clouds': 40, 'visibility': 8000, 'wind_speed': 3.09, 'wind_deg': 300, 'weather': [{'id': 211, 'main': 'Thunderstorm', 'description': 'thunderstorm', 'icon': '11d'}]}, {'dt': 1644620400, 'temp': 16.05, 'feels_like': 15.59, 'pressure': 1022, 'humidity': 72, 'dew_point': 11.01, 'uvi': 0, 'clouds': 40, 'visibility': 9000, 'wind_speed': 2.06, 'wind_deg': 10, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 00:00:00 | 75.000000 | 11.110000 | 12.710000 | 88.000000 | 1023.000000 |  | 13.050000 | 0.000000 | 10000.000000 | 170.000000 |  | 3.090000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 01:00:00 | 75.000000 | 11.110000 | 11.770000 | 94.000000 | 1024.000000 |  | 12.050000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 02:00:00 | 75.000000 | 11.110000 | 11.770000 | 94.000000 | 1025.000000 |  | 12.050000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 03:00:00 | 75.000000 | 12.050000 | 11.920000 | 100.000000 | 1026.000000 |  | 12.050000 | 0.000000 | 10000.000000 | 20.000000 |  | 1.540000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 04:00:00 | 40.000000 | 11.110000 | 11.770000 | 94.000000 | 1025.000000 |  | 12.050000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 05:00:00 | 40.000000 | 9.960000 | 10.640000 | 93.000000 | 1025.000000 |  | 11.050000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 06:00:00 | 40.000000 | 9.960000 | 10.640000 | 93.000000 | 1024.000000 |  | 11.050000 | 0.000000 | 10000.000000 | 360.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 07:00:00 | 75.000000 | 8.970000 | 9.540000 | 93.000000 | 1024.000000 |  | 10.050000 | 0.000000 | 10000.000000 | 40.000000 |  | 1.540000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 08:00:00 | 75.000000 | 10.050000 | 9.720000 | 100.000000 | 1023.000000 |  | 10.050000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 09:00:00 | 75.000000 | 10.050000 | 9.720000 | 100.000000 | 1024.000000 |  | 10.050000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 10:00:00 | 20.000000 | 9.050000 | 9.050000 | 100.000000 | 1023.000000 |  | 9.050000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 801 | Clouds | few clouds | 02n | 10 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 11:00:00 | 40.000000 | 9.050000 | 9.050000 | 100.000000 | 1024.000000 |  | 9.050000 | 0.000000 | 8000.000000 | 0.000000 |  | 1.030000 | 741 | Fog | fog | 50n | 11 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 12:00:00 | 40.000000 | 10.050000 | 9.720000 | 100.000000 | 1025.000000 |  | 10.050000 | 0.540000 | 10000.000000 | 70.000000 |  | 2.570000 | 741 | Fog | fog | 50d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 13:00:00 | 40.000000 | 11.030000 | 13.650000 | 82.000000 | 1025.000000 |  | 14.050000 | 2.470000 | 10000.000000 | 30.000000 |  | 2.570000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 14:00:00 | 40.000000 | 9.930000 | 15.460000 | 67.000000 | 1026.000000 |  | 16.050000 | 5.830000 | 10000.000000 | 90.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 15:00:00 | 75.000000 | 8.990000 | 16.350000 | 59.000000 | 1025.000000 |  | 17.050000 | 9.790000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 16:00:00 | 75.000000 | 9.920000 | 17.450000 | 59.000000 | 1025.000000 |  | 18.050000 | 12.220000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 17:00:00 | 75.000000 | 6.760000 | 19.210000 | 42.000000 | 1024.000000 |  | 20.050000 | 13.300000 | 10000.000000 | 280.000000 |  | 2.570000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 18:00:00 | 75.000000 | 10.860000 | 18.550000 | 59.000000 | 1023.000000 |  | 19.050000 | 12.080000 | 10000.000000 | 290.000000 |  | 6.170000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 19:00:00 | 75.000000 | 11.010000 | 19.570000 | 56.000000 | 1022.000000 |  | 20.050000 | 7.840000 | 7000.000000 | 280.000000 |  | 6.170000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 20:00:00 | 75.000000 | 11.010000 | 19.570000 | 56.000000 | 1021.000000 |  | 20.050000 | 4.580000 | 8000.000000 | 270.000000 |  | 6.690000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![11d.png](http://openweathermap.org/img/w/11d.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 21:00:00 | 40.000000 | 10.880000 | 16.560000 | 67.000000 | 1021.000000 | 0.15 | 17.050000 | 1.880000 | 8000.000000 | 260.000000 |  | 5.660000 | 211 | Thunderstorm | thunderstorm | 11d | 21 |
| ![11d.png](http://openweathermap.org/img/w/11d.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 22:00:00 | 40.000000 | 10.880000 | 16.560000 | 67.000000 | 1022.000000 |  | 17.050000 | 0.390000 | 8000.000000 | 300.000000 |  | 3.090000 | 211 | Thunderstorm | thunderstorm | 11d | 22 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206230 | "VEGAS LAS HACIENDA [21206230]" | 4.661667 | -74.151419 | 2543.000000 | Clim�tica Ordinaria | Convencional | Suspendida | 1987-08-15 00:00:00 | 2011-05-10 00:00:00 | Bogot� | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-02-11 23:00:00 | 40.000000 | 11.010000 | 15.590000 | 72.000000 | 1022.000000 |  | 16.050000 | 0.000000 | 9000.000000 | 10.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03d | 23 |


### Weather plots

![CNE_IDEAM_Station21206230_OWM_Clouds_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206230_OWM_Clouds_20220213.png)
![CNE_IDEAM_Station21206230_OWM_Dewpoint_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206230_OWM_Dewpoint_20220213.png)
![CNE_IDEAM_Station21206230_OWM_Feelslike_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206230_OWM_Feelslike_20220213.png)
![CNE_IDEAM_Station21206230_OWM_Humidity_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206230_OWM_Humidity_20220213.png)
![CNE_IDEAM_Station21206230_OWM_Pressure_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206230_OWM_Pressure_20220213.png)
![CNE_IDEAM_Station21206230_OWM_Rain_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206230_OWM_Rain_20220213.png)
![CNE_IDEAM_Station21206230_OWM_Temp_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206230_OWM_Temp_20220213.png)
![CNE_IDEAM_Station21206230_OWM_UVI_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206230_OWM_UVI_20220213.png)
![CNE_IDEAM_Station21206230_OWM_Visibility_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206230_OWM_Visibility_20220213.png)
![CNE_IDEAM_Station21206230_OWM_Winddeg_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206230_OWM_Winddeg_20220213.png)
![CNE_IDEAM_Station21206230_OWM_Windgust_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206230_OWM_Windgust_20220213.png)
![CNE_IDEAM_Station21206230_OWM_Windspeed_20220213.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206230_OWM_Windspeed_20220213.png)

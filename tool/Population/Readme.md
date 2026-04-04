# Population and public services demand projections (PPSD)

To convert a value from liters per capita per day (LPCD) to cubic meters per second (m³/s), multiply the LPCD value by the total population and then divide by (86400*1000).

## Colombia

DANE Census

* 1973: https://microdatos.dane.gov.co/index.php/catalog/117
* 1985: 
* 1993:
* 2005:
* 2018:


## Data dictionary: Fields and variables

The follow list contains the fields and variables used across the tables, shapefiles and processing results.

| Field / Var | Type         | Description                                         | Units                            |
|:------------|:-------------|:----------------------------------------------------|:---------------------------------|
| Source      | String (100) | Sorce data: DANE Colombia, DNP, rcfdtools           | n/a                              |
| Year        | Integer (32) | Data year record                                    | Year                             |
| CountryID   | String (5)   | International country code, https://countrycode.org | n/a                              |
| CountryName | String (100) | Country name                                        | n/a                              |
| StateID     | String (5)   | State code                                          | n/a                              |
| StateName   | String (100) | State name                                          | n/a                              |
| CountyID    | String (5)   | County code                                         | n/a                              |
| CountyName  | String (100) | County name                                         | n/a                              |
| PTotal      | Real (10)    | County total population = PUrban + PRural           | Habitant, hab                    |
| PUrban      | Real (10)    | County urban population                             | Habitant, hab                    |
| PRural      | Real (10)    | County rural population                             | Habitant, hab                    |
| ATotal      | Real (10)    | County total planar area with CRS 9377              | Square meters, m²                |
| AUrban      | Real (10)    | County urban planar area with CRS 9377              | Square meters, m²                |
| ARural      | Real (10)    | County rural planar area with CRS 9377              | Square meters, m²                |
| CZTotal     | Real (10)    | County mean level for the complete area             | Meters above the sea level, masl |
| CZUrban     | Real (10)    | County mean level for the urban area                | Meters above the sea level, masl |
| CZRural     | Real (10)    | County mean level for the rural area                | Meters above the sea level, masl |
| Notes       | String (255) | General notes                                       | n/a                              |
| Method      | n/a          | Regression or projection method                     | n/a                              |
| PD1         | n/a          | Polynomial Degree 1 (lineal)                        | n/a                              |
| PD2         | n/a          | Polynomial Degree 2                                 | n/a                              |
| PD3         | n/a          | Polynomial Degree 3                                 | n/a                              |
| PD4         | n/a          | Polynomial Degree 4                                 | n/a                              |
| Log         | n/a          | Logarithmic                                         | n/a                              |
| Pow         | n/a          | Potential                                           | n/a                              |
| Exp         | n/a          | Exponential                                         | n/a                              |
| Geo         | n/a          | Geometric                                           | n/a                              |
| Wap         | n/a          | Wappaus                                             | n/a                              |
| AbsError    | n/a          | Absolute error                                      | n/a                              |
| RelError    | n/a          | Relative error                                      | n/a                              |
| WS          | Real (10)    | Fresh water supply                                  | Liters per capita per day, lpcd  |
| WSAll       | Real (10)    | Zonal fresh water supply = WS * population / 86400  | Liters per second, l/s           |

> n/a: doesn't apply. 
> QGIS: area(transform($geometry, layer_property(@layer, 'crs'),'EPSG:9377'))


## Digital elevation model - DEM

* Copernicus 90m.


## References


### General

* Country codes: https://hub.arcgis.com/datasets/esri::world-countries-generalized/explore?location=6.175773%2C-72.180176%2C5
* https://allendowney.github.io/ModSimPy/chap05.html
* https://www.sdp.gov.co/sites/default/files/bogota_pasado_presente_y_futuro.pdf
* https://www.dane.gov.co/index.php/estadisticas-por-tema/demografia-y-poblacion/proyecciones-de-poblacion/proyecciones-de-poblacion-bogota
* [IGAC - Municipios, Distritos y Áreas no municipalizadas de Colombia](https://www.colombiaenmapas.gov.co/?u=0&t=29&servicio=610)
* [IGAC - Centros poblados y cabeceras municipales de Colombia](https://www.colombiaenmapas.gov.co/?u=0&t=29&servicio=591)


### Reglamento Técnico para el Sector de Agua Potable y Saneamiento Básico (RAS) 

* [Colombia - Resolución 330 DE 2017](https://www.alcaldiabogota.gov.co/sisjur/normas/Norma1.jsp?i=71542)
* [Colombia - Resolución 799 DE 2017](https://www.alcaldiabogota.gov.co/sisjur/normas/Norma1.jsp?i=119747)


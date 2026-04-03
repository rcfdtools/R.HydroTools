# Human population analysis


## Colombia

DANE Census

* 1973: https://microdatos.dane.gov.co/index.php/catalog/117
* 1985: 
* 1993:
* 2005:
* 2018:


## Fields

* ATotal: Total planar area in square meters with CRS 9377.
* AUrban: Urban planar area in square meters with CRS 9377.
* ARural: Rural planar area in square meters with CRS 9377, ("ATotal" - "AUrban").
* CZTotal: Correspond to mean level in meters above the sea level (masl) for all the county area.
* CZUrban: Correspond to mean level in meters above the sea level (masl) for the urban area.
* CZRural: Correspond to mean level in meters above the sea level (masl) for the rural area which for this study correspond with CZTotal considering the mean elevation of the urban areas.
* WaterSupply: Water supply in liters per capita per day (lpcd).

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


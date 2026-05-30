# SCS Curve Number (CN) 

The SCS Curve Number (CN) is an empirical parameter used in hydrology by the USDA Natural Resources Conservation Service (formerly the Soil Conservation Service) to estimate direct surface runoff and infiltration from rainfall. Ranging from \(0\) to \(100\), higher values indicate greater runoff and less soil retention.[^1]


## Source layers


### States 202604

* https://www.colombiaenmapas.gov.co/
* https://staigacmpcolv2.z20.web.core.windows.net/?b=igac&u=0&t=43&servicio=23


### Colombia Soil Maps

* es: Suelos por Departamento 100k, 2000.
* https://www.colombiaenmapas.gov.co/
* Service 382 to 413 (402 and 409 doesn't exist), 1613 Nariño, Sucre state service not available. 
* Sucre state old metadata https://metadatos.icde.gov.co/geonetwork/srv/api/records/69cf5eac-a191-4162-8f79-9190b5a7f3c3
* Sample https://staigacmpcolv2.z20.web.core.windows.net/?b=igac&u=0&t=43&servicio=382

Required displacement for v0

* DX = -370.54982010833919048309
* DY = 309.88952068053185939789


### Land use

* es: Vocación de Uso 100k, Territorio Nacional 2013.
* https://www.colombiaenmapas.gov.co/
* https://staigacmpcolv2.z20.web.core.windows.net/?b=igac&u=0&t=43&servicio=7301


## Data Dictionary


### CN.gpkg/ColombiaSoil

UCS text 255
UCSf text 255 *
Paisaje text 255 *
Clima text 255 *
TipoRelieve text 255 * 
CaracteristicaRelieve text 255
LitologiaSedimento text 255
CaracteristicaSuelo text 1000
ComponenteTaxonomico text 255
Perfil text 255 
Porcentaje text 255
Fase text 255
ProcesoGeomorfologico text 255
Conjunto text 255
DeNombre String 100


## QGIS tools

* Vector Table / Refactor Fields
* Vector Geometry / Translate
* Field Calculator: substr("path", 57, 255)
* Select by Expression: "LitologiaSedimento"  LIKE '%Arcilla%'

* Query Filter: 

"CaracteristicaSuelo" = 'Suelos de textura gruesa' AND "LitologiaSedimento" LIKE 'Arcilla%'
"CaracteristicaSuelo" = 'Suelos de textura media' AND "LitologiaSedimento" LIKE 'Arcilla%'
"CaracteristicaSuelo" = 'Suelos de textura fina' AND "LitologiaSedimento" LIKE 'Arcilla%'
"CaracteristicaSuelo" = 'Suelos de textura muy fina' AND "LitologiaSedimento" LIKE 'Arcilla%'

"CaracteristicaSuelo" = 'Suelos de textura gruesa' AND "LitologiaSedimento" LIKE 'Ceniza%'
"CaracteristicaSuelo" = 'Suelos de textura media' AND "LitologiaSedimento" LIKE 'Ceniza%'
"CaracteristicaSuelo" = 'Suelos de textura fina' AND "LitologiaSedimento" LIKE 'Ceniza%'
"CaracteristicaSuelo" = 'Suelos de textura muy fina' AND "LitologiaSedimento" LIKE 'Ceniza%'

"CaracteristicaSuelo" = 'Suelos de textura gruesa' AND "LitologiaSedimento" LIKE 'Coluvio%'
"CaracteristicaSuelo" = 'Suelos de textura media' AND "LitologiaSedimento" LIKE 'Coluvio%'
"CaracteristicaSuelo" = 'Suelos de textura fina' AND "LitologiaSedimento" LIKE 'Coluvio%'
"CaracteristicaSuelo" = 'Suelos de textura muy fina' AND "LitologiaSedimento" LIKE 'Coluvio%'

"CaracteristicaSuelo" = 'Suelos de textura gruesa' AND "LitologiaSedimento" LIKE 'Depósito%'
"CaracteristicaSuelo" = 'Suelos de textura media' AND "LitologiaSedimento" LIKE 'Depósito%'
"CaracteristicaSuelo" = 'Suelos de textura fina' AND "LitologiaSedimento" LIKE 'Depósito%'
"CaracteristicaSuelo" = 'Suelos de textura muy fina' AND "LitologiaSedimento" LIKE 'Depósito%'


## QGIS Procedure

1. 



## References

* https://www.hec.usace.army.mil/confluence/hmsdocs/hmstrm/cn-tables

[^1]: https://en.wikipedia.org/wiki/Runoff_curve_number
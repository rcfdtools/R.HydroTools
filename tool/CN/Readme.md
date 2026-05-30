<div align="center"><img alt="R.HydroTools" src="../../file/graph/R.HydroTools.svg" width="300px"></div>

# SCS Curve Number (CN) 

The SCS Curve Number (CN) is an empirical parameter used in hydrology by the USDA Natural Resources Conservation Service (formerly the Soil Conservation Service) to estimate direct surface runoff and infiltration from rainfall. Ranging from \(0\) to \(100\), higher values indicate greater runoff and less soil retention.[^1]


## A. Source layers


### Colombia States

* Version: 202604
* https://www.colombiaenmapas.gov.co/
* https://staigacmpcolv2.z20.web.core.windows.net/?b=igac&u=0&t=43&servicio=23


### Colombia Soil Maps

* es: Suelos por Departamento 100k, 2000.
* https://www.colombiaenmapas.gov.co/
* Service 382 to 413 (402 and 409 doesn't exist), 1613 Nariño, Sucre state service not available. 
* Sucre state old metadata https://metadatos.icde.gov.co/geonetwork/srv/api/records/69cf5eac-a191-4162-8f79-9190b5a7f3c3
* Sample https://staigacmpcolv2.z20.web.core.windows.net/?b=igac&u=0&t=43&servicio=382
* CN.gpkg/SueloColombia100k_v0: integrated Colombia version.
* CN.gpkg/SueloColombia100k_v1: integrated Colombia version from states.
* Required displacement for v0: DX = -370.54982010833919048309, DY = 309.88952068053185939789

Data dictionary

| Field                 |    Type     | Description (es)                                                                                                                                                                                            |
|:----------------------|:-----------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UCS                   | Text (255)  | Unidad cartográfica del suelo. Representa una zona del terreno donde se ha identificado una agrupación específica de suelos con características físicas, químicas, taxonómicas y geomorfológicas similares. |
| UCSf                  | Text (255)  | Sub-unidad cartográfica del suelo                                                                                                                                                                           |
| Paisaje               | Text (255)  | Paisaje local                                                                                                                                                                                               |
| Clima                 | Text (255)  | Clima local                                                                                                                                                                                                 |
| TipoRelieve           | Text (255)  | Tipo de relieve                                                                                                                                                                                             |
| CaracteristicaRelieve | Text (255)  | Característica del relieve                                                                                                                                                                                  |
| LitologiaSedimento    | Text (255)  | Litología de sedimentos                                                                                                                                                                                     |
| CaracteristicaSuelo   | Text (1000) | Características del suelo                                                                                                                                                                                   |
| ComponenteTaxonomico  | Text (255)  | Componentes taxonómicos                                                                                                                                                                                     |
| Perfil                | Text (255)  | Códigos de perfiles estratigráficos de muestreo                                                                                                                                                             |
| Porcentaje            | Text (255)  | Porcentajes de distribución de componentes taxonómicos en perfil                                                                                                                                            |
| Fase                  | Text (255)  |                                                                                                                                                                                                             |
| ProcesoGeomorfologico | Text (255)  |                                                                                                                                                                                                             |
| Conjunto              | Text (255)  |                                                                                                                                                                                                             |
| DeNombre              | Text (100)  | Departamento                                                                                                                                                                                                |


### Land use

* es: Vocación de Uso 100k, Territorio Nacional 2013.
* https://www.colombiaenmapas.gov.co/
* https://staigacmpcolv2.z20.web.core.windows.net/?b=igac&u=0&t=43&servicio=7301


## B. QGIS Tools

* Vector Table / Refactor Fields
* Vector Geometry / Translate
* Field Calculator: substr("path", 57, 255)
* Select by Expression: "LitologiaSedimento"  LIKE '%Arcilla%'

Query Filters: 

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


## C. QGIS Procedure

1. 



## References

* https://www.hec.usace.army.mil/confluence/hmsdocs/hmstrm/cn-tables

[^1]: https://en.wikipedia.org/wiki/Runoff_curve_number
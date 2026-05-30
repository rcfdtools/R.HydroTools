<div align="center"><img alt="R.HydroTools" src="../../file/graph/R.HydroTools.svg" width="300px"></div>

# SCS Curve Number (CN) 

The SCS Curve Number (CN) is an empirical parameter used in hydrology by the USDA Natural Resources Conservation Service (formerly the Soil Conservation Service) to estimate direct surface runoff and infiltration from rainfall. Ranging from \(0\) to \(100\), higher values indicate greater runoff and less soil retention.[^1]

:blue_heart:**Attention**: _The current CN analysis correspond to an Alpha version, and it will be used for academic purposes. For professional use you must validate the CN values assigned by Land Use and the percentages for each Land Soil cartographic unit for your specific project area._


## General concepts


### USDA Hydrologic groups

The USDA's Natural Resources Conservation Service (NRCS) classifies soils into four primary Hydrologic Soil Groups (A, B, C, and D) based on their infiltration rates and runoff potential when thoroughly wet.

Hydrologic soil groups are based on estimates of runoff potential. Soils are assigned to one of four groups according to the rate of water infiltration when the soils are not protected by vegetation, are thoroughly wet, and receive precipitation from long-duration storms. The soils in the United States are assigned to four groups (A, B, C, and D) and three dual classes (A/D, B/D, and C/D). The groups are defined as follows[^2]:

| Group | Description                                                                                                                                                                                          |      Infiltration       |          Rate           | Texture                                                                                              |
|:-----:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------:|:-----------------------:|:-----------------------------------------------------------------------------------------------------|
|   A   | High infiltration, low runoff potential. Typically deep, well-drained sands or gravels that transmit water rapidly.                                                                                  |     Fast<br/>Rápida     |        > 76 mm/h        | Sandy, Sandy-silty<br/>Arenosa, Arenosa - limosa                                                     |
|   B   | Moderate infiltration, moderately low runoff. Usually moderately deep to deep, well-drained soils with moderately fine to moderately coarse textures (e.g., sandy loams or silt loams).              |  Moderate<br/>Moderada  | between 76 and 38 mm/h  | Loamy, Clay-loamy, Sandy-loamy, Silt-loamy<br/>Franca, Franco - arcillosa - arenosa, Franco - limosa |
|   C   | Slow infiltration, moderately high runoff. Typically have fine textures or a sub-layer that impedes downward water movement (e.g., clay loams).                                                      |     Slow<br/>Lenta      | between 38 and 13 mm/h  | Loam, Clay Loam, Sandy Clay<br/>Franco - arcillosa, Franco - arcillo - limosa, Arcillo - arenosa     |
|   D   | Very slow infiltration, high runoff potential. Usually heavy clay soils, soils with high shrink-swell potential, soils with a permanent high water table, or soils shallow over an impervious layer. | Very Slow<br/>Muy Lenta |        < 13 mm/h        | Clayey<br/>Arcillosa                                                                                 |

> Infiltration when soils are completely wet and averge infiltration capacity.


## A. Layers and tables


### Layer: Depto (Colombia States)

* Version: 202604
* https://www.colombiaenmapas.gov.co/
* https://staigacmpcolv2.z20.web.core.windows.net/?b=igac&u=0&t=43&servicio=23


### Layer: SueloColombia100k (Colombia Soil Maps)

* es: Suelos por Departamento 100k, 2000.
* https://www.colombiaenmapas.gov.co/
* Service 382 to 413 (402 and 409 doesn't exist), 1613 Nariño, Sucre state service not available. 
* Sucre state old metadata https://metadatos.icde.gov.co/geonetwork/srv/api/records/69cf5eac-a191-4162-8f79-9190b5a7f3c3
* Sample https://staigacmpcolv2.z20.web.core.windows.net/?b=igac&u=0&t=43&servicio=382
* CN.gpkg/SueloColombia100k_v0: integrated Colombia version.
* CN.gpkg/SueloColombia100k_v1: integrated Colombia version from states with overlapping error.
* Required displacement for v0: DX = -370.54982010833919048309, DY = 309.88952068053185939789

<div align="center"> Data dictionary (es)

| Field                 |    Type     | Description                                                      |
|:----------------------|:-----------:|:-----------------------------------------------------------------|
| UCS                   | Text (255)  | Código de unidad cartográfica del suelo                          |
| UCSf                  | Text (255)  | Código de sub-unidad cartográfica del suelo                      |
| Paisaje               | Text (255)  | Paisaje local                                                    |
| Clima                 | Text (255)  | Clima local                                                      |
| TipoRelieve           | Text (255)  | Tipo de relieve                                                  |
| CaracteristicaRelieve | Text (255)  | Característica del relieve                                       |
| LitologiaSedimento    | Text (255)  | Litología de sedimentos                                          |
| CaracteristicaSuelo   | Text (1000) | Características del suelo                                        |
| ComponenteTaxonomico  | Text (255)  | Componentes taxonómicos                                          |
| Perfil                | Text (255)  | Códigos de perfiles estratigráficos de muestreo                  |
| Porcentaje            | Text (255)  | Porcentajes de distribución de componentes taxonómicos en perfil |
| DeNombre              | Text (100)  | Departamento                                                     |

</div>

> A UCS represents an area of terrain where a specific grouping of soils with similar physical, chemical, taxonomic, and geomorphological characteristics has been identified.


### Layer: VocacionUsoColombia100k (Land use)

* es: Vocación de Uso 100k, Territorio Nacional 2013.
* https://www.colombiaenmapas.gov.co/
* https://staigacmpcolv2.z20.web.core.windows.net/?b=igac&u=0&t=43&servicio=7301

<div align="center"> Data dictionary (es)

| Field      |    Type     | Description                                       |
|:-----------|:-----------:|:--------------------------------------------------|
| UCVocacion | Text (255)  | Código de unidad cartográfica por vocación de uso |
| Vocacion   | Text (255)  | Vocación de uso                                   |
| UsoPpal    | Text (255)  | Uso principal                                     |
| CNCode     | Text (255)  | Código asociado de tabla CN_LandUse               |

</div>


## B. QGIS Procedure

1. Join the _CN_LandUse_v0_ table to the _VocacionUsoColombia100k_v0_ layer using the `CNCode` field and check if all the record has associated CN values for the different hydrologic groups (CNA, CNB, CNC, CND).

2. Join the _CN_LandSoil_v0_ table to the _SueloColombia100k_v0_ layer using the `UCSf` field and check if all the record has associated CN percentage values for the different hydrologic groups (PctA, PctB, PctC, PctD).

3. With Processing _Toolbox / Vector Geometry / Union_, create a spatial between _VocacionUsoColombia100k_v0_ and _SueloColombia100k_v0_ and name the resulting layer as _gdb/CN.gpkg/VocacionUsoSueloColombia100kUnion_v0_ 

> If one of the layer has geometry error it could be fixed first with the tool _Vector Geometry / Fix geometries_ (Repair method: Structure)

4. 


## C. QGIS Tools

* Vector Table / Refactor Fields
* Vector Geometry / Translate
* Field Calculator: substr("path", 57, 255)
* Select by Expression: "LitologiaSedimento"  LIKE '%Arcilla%'
* Vector Geometry / Fix geometries (Repair method: Structure)

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


## References

* https://www.hec.usace.army.mil/confluence/hmsdocs/hmstrm/cn-tables



[^1]: https://en.wikipedia.org/wiki/Runoff_curve_number
[^2]: https://www.hec.usace.army.mil/confluence/hmsdocs/hmsguides/files/118099517/118099546/1/1665679165857/HydrologicSoilGroup_DominantCondition.pdf
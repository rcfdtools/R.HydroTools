## Evaluación y análisis de sinuosidad en cauces naturales
Keywords: `Hydraulics` `Sinuosity` `River bend` `Channel length` `Valley length`

A partir de las líneas de drenaje restituidas y las líneas esquemáticas que representan tránsito hidrológico en el modelo geográfico de HEC-GeoHMS, determinar el factor de sinuosidad por los siguientes métodos geográficos:

* Método 1: Estimación del factor de sinuosidad a partir de la longitud euclidiana del valle.
* Método 2: Estimación del factor de sinuosidad a partir de la longitud suavizada del valle (PAEK, 2 km).
* Método 3: Factor de sinuosidad a partir de la longitud euclidiana del tramo a reemplazar.


### Requerimientos

* [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel) 2013 o superior
* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/)
* Estudio de [Secciones transversales de inicio y entrega](https://github.com/rcfdtools/R.HydroTools/tree/main/SeccionTransvInicioEntrega)


### Ejemplos de cauces naturales y artificiales sinuosos y curvos con y sin sección compuesta

| Imagen[^1]                                                                                                                                                        | Cauce                                                                                                                   | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                        Google maps                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------:|
| <img alt="R.HydroTools" src="https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Graph/RioCalenturitasCesarColombia3.png" width="200px">  | Canal de desviación Río Calenturitas                                                                                    | C.I. Prodeco S.A.<br>Departamento del Cesar, Colombia, Suramérica<br>http://www.grupoprodeco.com.co/es/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |  [Ver](http://maps.google.com/maps?q=9.672087,-73.466907)  |
| <img alt="R.HydroTools" src="https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Graph/RioMaracasCesarColombia2.png" width="200px">       | Canal natural Río Maracas                                                                                               | Departamento del Cesar, Colombia, Suramérica                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  [Ver](http://maps.google.com/maps?q=9.694587,-73.399419)  |
| <img alt="R.HydroTools" src="https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Graph/ArroyoElZorroCesarColombia3.png" width="200px">    | Canal de desviación Arroyo San Antonio                                                                                  | Drummond Ltd.<br>Departamento del Cesar, Colombia, Suramérica.<br>http://www.drummondltd.com/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  [Ver](http://maps.google.com/maps?q=9.520558,-73.483489)  |
| <img alt="R.HydroTools" src="https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Graph/CaliforniaStateWaterProject2.png" width="200px">   | [California State water project](https://www.centerforfoodsafety.org/issues/4729/water/californias-state-water-project) | El Dorado Irrigation District                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                            |
| <img alt="R.HydroTools" src="https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Graph/MorwellRiverVictoriaAustralia4.png" width="200px"> | Morwell River, River Channel Relocation                                                                                 | Victoria, Australia                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | [Ver](http://maps.google.com/maps?q=-38.239749,146.350334) |
| <img alt="R.HydroTools" src="https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Graph/RiverNithCumnockUnitedKingdom3.png" width="200px"> | River Nith                                                                                                              | Cumnock, United Kingdom                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |  [Ver](http://maps.google.com/maps?q=55.379424,-4.288834)  |
| <img alt="R.HydroTools" src="https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Graph/IsaacRiverMoranbahAustralia2.png" width="200px">   | Isaac River                                                                                                             | Moranbah, Australia                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | [Ver](http://maps.google.com/maps?q=-21.826206,147.994263) |
| <img alt="R.HydroTools" src="https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Graph/TraralgonCreekAustralia2.png" width="200px">       | Traralgon Creek                                                                                                         | Traralgon, Australia                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Ver](http://maps.google.com/maps?q=-38.227016,146.539554) |
| <img alt="R.HydroTools" src="https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Graph/RioSegreLleidaSpain2.png" width="200px">           | Río Segre                                                                                                               | Lérida, Lleida, Spain                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |   [Ver](http://maps.google.com/maps?q=41.61386,0.627197)   |
| <img alt="R.HydroTools" src="https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Graph/CanalDelDiqueColombia.png" width="200px">          | [Canal del Dique](https://www.banrep.gov.co/es/el-canal-del-dique-y-su-subregion-economia-basada-riqueza-hidrica)       | La subregión Canal del Dique, ubicada en la Costa Caribe colombiana, es una llanura aluvial conformada por un complejo de humedales en donde habitan una gran biodiversidad de especies terrestres y piscícolas. El Canal del Dique fue un sistema de ciénagas interconectadas por un pequeño y sinuoso canal de desborde, habilitado en 1650 por Don Pedro Zapata de Mendoza para la navegación menor. Entre 1981 y 1984, se realizó la última rectificación del canal del Dique, reduciendo en número de curvas, el ancho del fondo se amplió entre 60 y 70 m con una profundidad mínima de 2.5 metros.<br><sub>Referencia por: 1000094166</sub> | [Ver](http://maps.google.com/maps?q=10.231693,-75.228782)  |
| <img alt="R.HydroTools" src="https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Graph/RioSaoFranciscoBrasil.png" width="200px">          | Desvío del Rio Sao Francisco en Brasil                                                                                  | Se diseñaron y construyeron dos grandes canales de derivación para uso agropecuario y de consumo para suministrar agua a 390 municipios, el canal norte tiene 140 km de longitud y un caudal de diseño de 99 m³/s; el canal del este tiene 217 km de longitud y un caudal de diseño de 28 m³/s.<br><sub>Referencia por: 1000020502</sub>                                                                                                                                                                                                                                                                                                           | [Ver](http://maps.google.com/maps?q=-8.538265,-39.455780)  |


### Método 1: Estimación del factor de sinuosidad a partir de la longitud euclidiana del valle.

Procedimiento usando ArcGIS:
1. Crear una capa de drenajes 2D digitalizando los cauces sobre una ortofoto o sobre un modelo de terreno lidar. La digitalización se debe realizar por tramos de río entre afluentes detallando las líneas meandriformes y en el sentido del flujo.					
2. Para cada tramo de drenaje obtener la coordenada de inicio y fin. En ArcGIS cree 4 campos numéricos dobles (cx_inicio, cy_inicio, cx_fin, cy_fin) y mediante calcular geometría (desde la tabla, clic derecho en cada columna), obtenga el valor de cada coordenada. Cree un campo numérico doble (l_eucl_m) para almacenar la longitud euclidiana y calcule la longitud con la expresión l_eucl_m = ( (cx_inicio - cx_fin)² + (cy_inicio - cy_fin)²)^(0.5). Este valor se considera como la longitud de valle.					
3. Indice de sinuosidad de cada tramo: Dividir la longitud euclidiana o longitud de valle, entre la longitud del cauce digitalizado.					

> Los datos obtenidos deberán ser copiados en la tabla del método 2 para obtener la ecuación de ajuste potencial que caracterizará el comportamiento sinuoso o meandriforme de los drenajes en la zona de llanura.


### Método 2: Estimación del factor de sinuosidad a partir de la longitud suavizada del valle (PAEK, 2 km).

Procedimiento usando ArcGIS:
1. Crear una capa de drenajes 2D digitalizando los cauces sobre una ortofoto o sobre un modelo de terreno lidar. La digitalización se debe realizar por tramos de río entre afluentes detallando las líneas meandriformes y en el sentido del flujo.					
2. A partir de la cada de drenajes 2D digitalizada, crear una nueva capa de drenajes suavizados utilizando la herramienta cartográfica de generalización "Suavizar Linea" o "Smooth Line" de ArcMAP. El radio de curvatura recomendado para la tangencia de suavizado es de 2000 metros. Estas líneas suavizadas se consideran como la línea de valle.
3. En ArcMAP, realizar la unión de la capa de drenajes 2D con drenajes suavizados usando la llave de objeto.					
(Opcional) Calcular la coordenada xyz del centroide de cada tramo para referencia de localización.					
4. Indice de sinuosidad de cada tramo: Dividir la longitud del tramo suavizado o línea de valle, entre la longitud del cauce digitalizado.					

> Los datos obtenidos deberán ser copiados en la tabla del método 3 para obtener la ecuación de ajuste potencial que caracterizará el comportamiento sinuoso o meandriforme de los drenajes en la zona de llanura.


### Método 3: Factor de sinuosidad a partir de la longitud euclidiana del tramo a reemplazar.

Procedimiento usando ArcGIS:
1. De la red de drenaje del modelo hidrológico, extraer los tramos a reemplazar, fusionar desde el editor de ArcMAP y eliminar los tramos sobrantes arriba y abajo del punto de inicio. Capa HMS_RiverReplaceSample_v0 de la GDB. Verificar el sentido vectorial de la polilínea hacia aguas abajo.
2. Utilizando la herramienta Feature Vertices To Points, obtener todos los nodos de la polilínea. Point Type = All. Nombrar como HMS_RiverReplaceSamplePoint_v0 dentro de la GDB.
3. Los nodos obtenidos serán numerados en el sentido de dibujo de la entidad.
4. En la tabla de atributos de la capa de puntos, crear dos campos tipo doble, CX y CY. Utilizando la calculadora de geometría desde la cabecera del campo en la tabla, obtener los valores de las coordenadas.
5. Seleccionar todos los nodos de la tabla y copiar en un libro de Excel nuevo. Copiar las columnas CX y CY en la tabla del Método 3.
6. Verificar los valores correspondientes a las longitudes de río y valle, así como el FS obtenido.

> El FS obtenido en este método debe ser similar al obtenido en el libro de análisis de [Secciones transversales de referencia inicio y entrega](https://github.com/rcfdtools/R.HydroTools/tree/main/SeccionTransvInicioEntrega) para diseño hidráulico.


### Ilustraciones

![R.HydroTools.SinuosidadCauceAnalisis.Screenshot1](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot1.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot2](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot2.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot3](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot3.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot4](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot4.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot5](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot5.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot6](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot6.png)


### Referencias

* www.tankonyvtar.hu
* https://es.wikipedia.org/wiki/Sinuosidad_de_un_r%C3%Ado
* https://www.banrep.gov.co/sites/default/files/publicaciones/archivos/DTSER-72_%28VE%29.pdf
* https://www.canaldeldique.com/anexos/junio3.pdf
* https://semspub.epa.gov/work/01/557060.pdf
* https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/water/manage/restoration/?cid=stelprdb1044707


### Control de versiones

| Versión     | Descripción                                            | Autor                                      | Horas |
|-------------|:-------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.07.25  | Actualización general de documentación.                | [rcfdtools](https://github.com/rcfdtools)  |  0.5  |
| 2021.10.19  | Actualización general de análisis, gráficas y formato. | [rcfdtools](https://github.com/rcfdtools)  |   2   |
| 2016.05.21  | Versión inicial.                                       | [rcfdtools](https://github.com/rcfdtools)  |   8   |

_R.HydroTools es de uso libre para fines académicos, conoce nuestra [licencia, cláusulas, condiciones de uso](https://github.com/rcfdtools/R.HydroTools/wiki/License) y como referenciar los contenidos publicados en este repositorio._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [r.cfdtools](https://github.com/rcfdtools) en GitHub._

| [:house: Inicio](https://github.com/rcfdtools/R.HydroTools/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.HydroTools/discussions/24) |
|------------------------------------------------------------------|------------------------------------------------------------------------------|

[^1]: Imágenes tomadas de [Google Maps](http://maps.google.com) y https://www.centerforfoodsafety.org/issues/4729/water/californias-state-water-project.
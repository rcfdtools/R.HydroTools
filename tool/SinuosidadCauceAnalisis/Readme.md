<div align="center"><img alt="R.HydroTools" src="../../file/graph/R.HydroTools.svg" width="300px"></div>

## Evaluación y análisis de sinuosidad en cauces naturales
Keywords: `hydraulics` `sinuosity` `river-bend` `channel-length` `valley-length`

A partir de las líneas de drenaje restituidas y las líneas esquemáticas que representan tránsito hidrológico en el modelo geográfico de HEC-GeoHMS, determinar el factor de sinuosidad por los siguientes métodos geográficos:

* Método 1: Estimación del factor de sinuosidad a partir de la longitud euclidiana del valle.
* Método 2: Estimación del factor de sinuosidad a partir de la longitud suavizada del valle (PAEK, 2 km).
* Método 3: Factor de sinuosidad a partir de la longitud euclidiana del tramo a reemplazar.


### Requerimientos

* [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel) 2013 o superior
* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/)
* Estudio de [Secciones transversales de inicio y entrega](https://github.com/rcfdtools/R.HydroTools/tree/main/SeccionTransvInicioEntrega)


### Método 1: Estimación del factor de sinuosidad a partir de la longitud euclidiana del valle.

Procedimiento usando ArcGIS:
1. Crear una capa de drenajes 2D digitalizando los cauces sobre una ortofoto o sobre un modelo de terreno lidar. La digitalización se debe realizar por tramos de río entre afluentes detallando las líneas meandriformes y en el sentido del flujo.					
2. Para cada tramo de drenaje obtener la coordenada de inicio y fin. En ArcGIS cree 4 campos numéricos dobles (cx_inicio, cy_inicio, cx_fin, cy_fin) y mediante calcular geometría (desde la tabla, clic derecho en cada columna), obtenga el valor de cada coordenada. Cree un campo numérico doble (l_eucl_m) para almacenar la longitud euclidiana y calcule la longitud con la expresión l_eucl_m = ( (cx_inicio - cx_fin)² + (cy_inicio - cy_fin)²)^(0.5). Este valor se considera como la longitud de valle.					
3. Índice de sinuosidad de cada tramo: Dividir la longitud euclidiana o longitud de valle, entre la longitud del cauce digitalizado.					

> Los datos obtenidos deberán ser copiados en la tabla del método 1 para obtener la ecuación de ajuste potencial que caracterizará el comportamiento sinuoso o meandriforme de los drenajes en la zona de llanura.


### Método 2: Estimación del factor de sinuosidad a partir de la longitud suavizada del valle (PAEK, 2 km).

Procedimiento usando ArcGIS:
1. Crear una capa de drenajes 2D digitalizando los cauces sobre una ortofoto o sobre un modelo de terreno lidar. La digitalización se debe realizar por tramos de río entre afluentes detallando las líneas meandriformes y en el sentido del flujo.					
2. A partir de la cada de drenajes 2D digitalizada, crear una nueva capa de drenajes suavizados utilizando la herramienta cartográfica de generalización "Suavizar Línea" o "Smooth Line" de ArcMAP. El radio de curvatura recomendado para la tangencia de suavizado es de 2000 metros. Estas líneas suavizadas se consideran como la línea de valle.
3. En ArcMAP, realizar la unión de la capa de drenajes 2D con drenajes suavizados usando la llave de objeto.					
(Opcional) Calcular la coordenada xyz del centroide de cada tramo para referencia de localización.					
4. Índice de sinuosidad de cada tramo: Dividir la longitud del tramo suavizado o línea de valle, entre la longitud del cauce digitalizado.					

> Los datos obtenidos deberán ser copiados en la tabla del método 2 para obtener la ecuación de ajuste potencial que caracterizará el comportamiento sinuoso o meandriforme de los drenajes en la zona de llanura.


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

![R.HydroTools.SinuosidadCauceAnalisis.Screenshot1](Screenshot/Screenshot1.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot2](Screenshot/Screenshot2.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot3](Screenshot/Screenshot3.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot4](Screenshot/Screenshot4.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot5](Screenshot/Screenshot5.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot6](Screenshot/Screenshot6.png)


### Referencias

* www.tankonyvtar.hu
* https://es.wikipedia.org/wiki/Sinuosidad_de_un_r%C3%Ado
* https://www.banrep.gov.co/sites/default/files/publicaciones/archivos/DTSER-72_%28VE%29.pdf
* https://www.canaldeldique.com/anexos/junio3.pdf
* https://semspub.epa.gov/work/01/557060.pdf
* https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/water/manage/restoration/?cid=stelprdb1044707


### Control de versiones

| Versión    | Descripción                                                                          | Autor                                      | Horas |
|------------|:-------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.07.25 | Actualización general de documentación.                                              | [rcfdtools](https://github.com/rcfdtools)  |  0.5  |
| 2021.10.19 | Actualización general de análisis, gráficas y formato.                               | [rcfdtools](https://github.com/rcfdtools)  |   2   |
| 2016.05.21 | Versión inicial.                                                                     | [rcfdtools](https://github.com/rcfdtools)  |   8   |


### Licencia, cláusulas y condiciones de uso

_R.HydroTools es de uso libre para fines académicos, conoce nuestra [licencia, cláusulas, condiciones de uso](../../LICENSE.md) y como referenciar los contenidos publicados en este repositorio._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [r.cfdtools](https://github.com/rcfdtools) en GitHub._

| [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.HydroTools/discussions/24) |
|------------------------------------------------------------------|------------------------------------------------------------------------------|


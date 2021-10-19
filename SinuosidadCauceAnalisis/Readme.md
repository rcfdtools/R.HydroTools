## Evaluación y análisis de la sinuosidad en cauces naturales

A partir de las líneas de drenaje restituidas y las líneas esquemáticas que representan tránsito hidrológico en el modelo geográfico de HEC-GeoHMS, determinar el factor de sinuosidad por los siguientes métodos geográficos.

* Método 1: Estimación del factor de sinuosidad a partir de la longitud euclidiana del valle.
* Metodo 2: Estimación del factor de sinuosidad a partir de la longitud suavizada del valle (PAEK, 2 km).
* Método 3: Factor de sinuosidad a partir de la longitud euclidiana del tramo a reemplazar.


### Método 1: Estimación del factor de sinuosidad a partir de la longitud euclidiana del valle.

Procedimiento usando ArcGIS:
1. Crear una capa de drenajes 2D digitalizando los cauces sobre una ortofoto o sobre un modelo de terreno lidar. La digitalización se debe realizar por tramos de río entre afluentes detallando las lineas meandriformes y en el sentido del flujo.					
2. Para cada tramo de drenaje obtener la coordenada de inicio y fin. En ArcGIS cree 4 campos numéricos dobles (cx_inicio, cy_inicio, cx_fin, cy_fin) y mediante calcular geometría (desde la tabla, clic derecho en cada columna), obtenga el valor de cada coordenada. Cree un campo numérico doble (l_eucl_m) para almacenar la longitud euclidiana y calcule la longitud con la expresión l_eucl_m = ( (cx_inicio - cx_fin)^2 + (cy_inicio - cy_fin)^2)^(0.5). Este valor se considera como la longitud de valle.					
3. Indice de sinuosidad de cada tramo: Dividir la longitud euclidiana o longitud de valle, entre la longitud del cauce digitalizado.					

Nota: los datos obtenidos deberán se copiados en la tabla del método 2 para obtener la ecuación de ajuste potencial que caracterizará el comportamiento sinuoso o mendriforme de los drenajes en la zona de llanura.


### Metodo 2: Estimación del factor de sinuosidad a partir de la longitud suavizada del valle (PAEK, 2 km).

Procedimiento usando ArcGIS:
1. Crear una capa de drenajes 2D digitalizando los cauces sobre una ortofoto o sobre un modelo de terreno lidar. La digitalización se debe realizar por tramos de río entre afluentes detallando las lineas meandriformes y en el sentido del flujo.					
2. Apartir de la cada de drenajes 2D digitalizada, crear una nueva capa de drenajes suavizados utilizando la herramienta cartográfica de generalización "Suavizar Linea" o "Smooth Line" de ArcMAP. El radio de curvatura recomendado para la tangencia de suavizado es de 2000 metros. Estas lineas suavisadas se consideran como la línea de valle.				3. En ArcMAP, realizar la unión de la capa de drenajes 2D con drenajes suavizados utilizando la llave de objeto.					
(Opcional) Calcular la coordenada x,y,z del centroide de cada tramo para referencia de localización.					
4. Indice de sinuosidad de cada tramo: Dividir la longitud del tramo suavizado o linea de valle, entre la longitud del cauce digitalizado.					

Nota: los datos obtenidos deberán se copiados en la tabla del método 3 para obtener la ecuación de ajuste potencial que caracterizará el comportamiento sinuoso o mendriforme de los drenajes en la zona de llanura.


### Método 3: Factor de sinuosidad a partir de la longitud euclidiana del tramo a reemplazar.

Procedimiento usando ArcGIS:
1. De la red de drenaje del modelo hidrológico, extraer los tramos a reemplazar, fusionar desde el editor de ArcMAP y eliminar los tramos sobrantes arriba y abajo del punto de inicio. Capa HMS_RiverReplaceSample_v0 de la GDB. Verificar el sentido vectorial de la polilínea hacia aguas abajo.
2. Utilizando la herramienta Feature Vertices To Points, obtener todos los nodos de la polilínea. Point Type = All. Nombrar como HMS_RiverReplaceSamplePoint_v0 dentro de la GDB. 3. Los nodos obtenidos serán numerados en el sentido de dibujo de la entidad.
4. En la tabla de atributos de la capa de puntos, crear dos campos tipo doble, CX y CY. Utilizando la calculadora de geometría desde la cabecera del campo en la tabla, obtener los valores de las coordenadas.
5. Seleccionar todos los nodos de la tabla y copiar en un libro de Excel nuevo. Copiar las columnas CX y CY en la tabla del Método 3.
Verificar los valores correspondientes a las longitudes de río y valle, así como el FS obtenido.

Nota: el FS obtenido en este método debe ser similar al obtenido en el libro de análisis de secciones transversales de referencia inicio y entrega para diseño hidráulico. https://github.com/rcfdtools/R.HydroTools/tree/main/SeccionTransvInicioEntrega


## Ilustraciones

![R.HydroTools.SinuosidadCauceAnalisis.Screenshot1](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot1.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot2](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot2.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot3](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot3.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot4](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot4.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot5](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot5.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot6](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot6.png)


## Referencias

www.tankonyvtar.hu
es.wikipedia.org/wiki/Sinuosidad_de_un_r%C3%Ado


## Keywords
Sinuosity. River bend. Channel length. Valley length.


## Control de versiones

Versión | Descripción
--- | ---
| v.20211019 | Actualización general de análisis, gráficas y formato.


## Licencia, cláusulas y condiciones de uso
https://github.com/rcfdtools/R.HydroTools/wiki/License

## Evaluación y análisis de la sinuosidad en cauces naturales

A partir de las líneas de drenaje restituidas y las líneas esquemáticas que representan tránsito hidrológico en el modelo geográfico de HEC-GeoHMS, determinar el factor de sinuosidad por los siguientes métodos geográficos.

* Método 1: Estimación del factor de sinuosidad a partir de la longitud euclidiana del valle.
* Metodo 2: Estimación del factor de sinuosidad a partir de la longitud suavizada del valle (PAEK, 2 km).
* Método 3: Factor de sinuosidad a partir de la longitud euclidiana del tramo a reemplazar.

### Método 1: Estimación del factor de sinuosidad a partir de la longitud euclidiana del valle.

Procedimiento usando ArcGIS

1.Crear una capa de drenajes 2D digitalizando los cauces sobre una ortofoto o sobre un modelo de terreno lidar. La digitalización se debe realizar por tramos de río entre afluentes detallando las lineas meandriformes y en el sentido del flujo.					
2.Para cada tramo de drenaje obtener la coordenada de inicio y fin. En ArcGIS cree 4 campos numéricos dobles (cx_inicio, cy_inicio, cx_fin, cy_fin) y mediante calcular geometría (desde la tabla, clic derecho en cada columna), obtenga el valor de cada coordenada. Cree un campo numérico doble (l_eucl_m) para almacenar la longitud euclidiana y calcule la longitud con la expresión l_eucl_m = ( (cx_inicio - cx_fin)^2 + (cy_inicio - cy_fin)^2)^(0.5). Este valor se considera como la longitud de valle.					
3.Indice de sinuosidad de cada tramo: Dividir la longitud euclidiana o longitud de valle, entre la longitud del cauce digitalizado.					

Nota: Los datos obtenidos deberán se copiados a esta tabla para obtener la ecuación de ajuste potencial que caracterizará el comportamiento sinuoso o mendriforme de los drenajes en la zona de llanura.


### Ilustraciones

![R.HydroTools.SinuosidadCauceAnalisis.Screenshot1](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot1.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot2](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot2.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot3](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot3.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot4](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot4.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot5](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot5.png)
![R.HydroTools.SinuosidadCauceAnalisis.Screenshot6](https://github.com/rcfdtools/R.HydroTools/blob/main/SinuosidadCauceAnalisis/Screenshot/Screenshot6.png)


### Keywords
Sinuosity. River bend. Channel length. Valley length.


### Control de versiones

Versión | Descripción
--- | ---
| v.20211019 | Actualización general de análisis, gráficas y formato.


### Licencia, cláusulas y condiciones de uso
https://github.com/rcfdtools/R.HydroTools/wiki/License

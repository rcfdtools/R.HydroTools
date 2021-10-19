## Secciones transversales de referencia inicio y entrega para diseño hidráulico

Secciones topográficas sobre el cauce actual donde inicia y entrega el canal de realineamiento a diseñar. Los datos de estación y elevación son extraídos del modelo de muestreo HEC-RAS, construido a partir del modelo de terreno de puntos topográficos y líneas de secciones transversales de la topografía. Las cotas de inicio y entrega para el diseño y modelación pueden ser más altas o bajas dependiendo si se considera rellenar,  dragar o rectificar el cauce natural antes de su intervención.

Se puede considerar que el canal artificial a diseñar deberá tener una profundidad similar a la del cauce natural a reemplazar, sin embargo, cuando se plantea realizar dragado o rectificación de fondo para rehabilitación o realce de los taludes de protección, las produndidades pueden variar y será necesario realizar un nuevo levantamiento topobatimétrico de las zonas de inicio y entrega para realizar un nuevo análisis.

Para el correcto cálculo del área hidráulica y perímetro mojado, la línea que describe el ancho superficial a partir de la selección de estaciones, no debe cruzar la línea de terreno. Tenga en cuenca que cuando existen bancos de arena o sobre elevaciones por encima de la lámina de água dentro del ancho superficial, la hoja de cálculo sobre estima o sub estima el valor del área y perímetro hidráulico calculado.


## Ilustraciones

![R.HydroTools.SeccionTransvInicioEntrega.Screenshot1](https://github.com/rcfdtools/R.HydroTools/blob/main/SeccionTransvInicioEntrega/Screenshot/Screenshot1.png)
![R.HydroTools.SeccionTransvInicioEntrega.Screenshot2](https://github.com/rcfdtools/R.HydroTools/blob/main/SeccionTransvInicioEntrega/Screenshot/Screenshot2.png)
![R.HydroTools.SeccionTransvInicioEntrega.Screenshot3](https://github.com/rcfdtools/R.HydroTools/blob/main/SeccionTransvInicioEntrega/Screenshot/Screenshot3.png)
![R.HydroTools.SeccionTransvInicioEntrega.Screenshot4](https://github.com/rcfdtools/R.HydroTools/blob/main/SeccionTransvInicioEntrega/Screenshot/Screenshot4.png)


## Keywords
XS Cross section. River cross section. Hydraulica area. Wet perimeter.


## Control de versiones

Versión | Descripción
--- | ---
| v.20211016 | Inclusión de coordenadas de localización de secciones de inicio y entrega en intersección con red de drenaje. Inclusión de selectores de estación inicial y final para estimación del ancho superficial T. Inclusión de localización geográfica e hipervinculación para visualización en Google Maps. Estimación de largo del valle recto sin puntos de cambio de dirección. Estimación del factor de sinuosidad característico Fs. Actualización general de gráficas.
| v.20211018 | Hoja de análisis ahora incluye de cálculo de área hidráulica y perímetro mojado. Actualización general de gráficas.


## Licencia, cláusulas y condiciones de uso
https://github.com/rcfdtools/R.HydroTools/wiki/License

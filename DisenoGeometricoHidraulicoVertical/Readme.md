## Diseño geométrico e hidráulico vertical de canales a superficie libre
Keywords: `Hydraulic design` `Critical depth` `Normal depth` `Yn` `Yc` `HEC-RAS hydraulic design` `Trapezoidal` `Circular` `Rectangular` `Triangular` _Tractive force_

Dimensionar la sección hidráulica dominante y de creciente del cauce principal y de los cauces laterales menores, verificando a flujo uniforme la capacidad hidráulica de la sección compuesta y el borde libre requerido.


### Requerimientos

* [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel) 2013 o superior


### Funcionalidades
* Registro y graficación de valores obtenidos en el módulo de diseño hidráulico HD de HEC-RAS.
* Secuenciamiento para construcción de regiones y polilíneas de sección en Autodesk Autocad y/o Autodek Civil 3D.
* Diseño y verificación de secciones transversales para diferentes tipos de geometría (rectangular, triangular, trapezoidal, circular) con cálculo y graficación de profunidades normal y crítica, parámetros y propiedades hidráulicas. Módulo desarrollado por r.cfdtools.
* Diseño de sección estable por el método de fuerza tractiva. Formulación r.cfdtools.


### Microsoft Excel procedure

1. Call the R_YnYc function.
2. Select a 9 columns by 7 files range matrix. The first selected cell correspond with the R_YnYc call.
3. With the currect selección, press F2 and then press <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>Enter</kbd>.


### Ilustraciones

![R.HydroTools.DisenoGeometricoHidraulicoVertical.Screenshot1](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoGeometricoHidraulicoVertical/Screenshot/Screenshot1.png)
![R.HydroTools.DisenoGeometricoHidraulicoVertical.Screenshot2](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoGeometricoHidraulicoVertical/Screenshot/Screenshot2.png)
![R.HydroTools.DisenoGeometricoHidraulicoVertical.Screenshot3](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoGeometricoHidraulicoVertical/Screenshot/Screenshot3.png)
![R.HydroTools.DisenoGeometricoHidraulicoVertical.Screenshot4](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoGeometricoHidraulicoVertical/Screenshot/Screenshot4.png)
![R.HydroTools.DisenoGeometricoHidraulicoVertical.Screenshot5](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoGeometricoHidraulicoVertical/Screenshot/Screenshot5.png)
![R.HydroTools.DisenoGeometricoHidraulicoVertical.Screenshot6](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoGeometricoHidraulicoVertical/Screenshot/Screenshot6.png)
![R.HydroTools.DisenoGeometricoHidraulicoVertical.Screenshot7](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoGeometricoHidraulicoVertical/Screenshot/Screenshot7.png)
![R.HydroTools.DisenoGeometricoHidraulicoVertical.Screenshot8](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoGeometricoHidraulicoVertical/Screenshot/Screenshot8.png)


### Referencias
* https://www.easycalculation.com/es/analytical/linear-interpolation.php
* https://es.slideshare.net/Ebene159/mcanica-de-fludos
* https://www.fullquimica.com/2012/04/densidad-del-agua.html
* Book: Julian Aguirre
* Ven Te Chow. Hidráulica de canales  (Ejemplo 7.4 Ven Te Chow)


### Control de versiones

| Versión    | Descripción                                             | Autor                                      | Horas |
|------------|:--------------------------------------------------------|--------------------------------------------|:-----:|
| 2021.10.19 | Actualización general de análisis, gráficas y formato.  | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2016.08.14 | Versión inicial.                                        | [rcfdtools](https://github.com/rcfdtools)  |  18   |


R.HydroTools es de uso libre para fines académicos, conoce nuestra [licencia, cláusulas, condiciones de uso](https://github.com/rcfdtools/R.HydroTools/wiki/License) y como referenciar los contenidos publicados en este repositorio.

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [r.cfdtools](https://github.com/rcfdtools) en GitHub._

| [:house: Inicio](https://github.com/rcfdtools/R.HydroTools/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.HydroTools/discussions/14) |
|------------------------------------------------------------------|------------------------------------------------------------------------------|

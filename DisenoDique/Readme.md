<div align=center> Hola </div>

## Diques de protección o encausamiento usando RAS Mapper

El diseño hidráulico de canales requiere de la verificación de zonas suceptibles a inundación, bien sea por que la creciente de diseño no puede ser encausada sin desbordarse previamente al pasar al canal diseñado en su zona de inicio, o por que en su punto de descarga no existen cotas de confinamiento hidráulico que garanticen que el flujo no desborde o inunde zonas próximas, razón por la cual es necesario realizar el diseño y localización de diques complementarios. 

### Procedimiento general
1. En ArcGIS, QGIS o RAS Mapper de HEC-RAS y a partir del modelo de terreno, identifique visualmente (p. ej. con ayuda de la extensión 3D Analyst y contornos manuales) las zonas suceptibles a inundación y trace en planta el eje del dique de encausamiento y/o de protección requerido. El proceso consiste en trazar lineas en planta hasta una cota de cierre definida o hasta una prolongación determinada que permita realizar el confinamiento hidráulico del flujo.
2. Exporte la línea(s) de eje de dique trazadas a formato ESRI Shapefile (.shp).
3. En RAS Mapper, trace una línea sobre el dique actual que requiere ser prolongado hasta el punto final que considere deberá ser el punto de inicio del dique de protección a extender.
4. Visualice el perfil de la línea trazada y obtenga los valores de estación - elevación.
5. Copie los valores estación - elevación y péguelos en la hoja de análisis de diques en la sección _Sample axe line over the current channel levee_. En la misma hoja, ingrese la longitud de la linea del nuevo eje de confinamiento, la relación de taludes a utilizar, la altura del dique a utilizar y el ancho en la corona.
6. Visualice los resultados del diseño y verifique el volumen de suelo que requerirá para la construcción del dique de protección.
7. Para la incorporación del dique en RAS Mapper, importe el eje del dique trazado en planta y agrege una sección transversal al inicio y final del eje de dique, considerando el ancho del dique o huella de mecanización del diseño y la prolongación de los taludes hasta una altura específica, p. ej. de 1.5 metros para conservar el mismo patron de diseño del dique actual. El ancho, p. ej., de la linea de sección es de 25 metros en corona + 2 x (1.5 altura de dique creciente x 14 m de talud)  = 67 metros.

> Nota: para el cálculo preciso del volúmen de material de suelo requerido para conformar el dique, se recomienda utilizar Autodesk Civil 3D creando el dique a partir del alineamiento identificado y el talud diseñado.

### Funcionalidades

* Registro de datos de muestreo del dique actual a partir de tabla estación - elevación RAS Mapper.
* Análisis de pendiente del dique actual.
* Ingreso de parámetros para el trazado del nuevo dique de protección.
* Calculo de parámetros y tablas con valores estación - elevación de las secciones requeridas por RAS Mapper para la creación del dique.
* Estimación preliminar del volumen de material requerido para su construcción.
* Gráfica del perfil de muestreo del tramo de dique actual.
* Gráfica de secciones transversales de talud en punto de inicio y fin.


## Ilustraciones

![R.HydroTools.DisenoDique.Screenshot1](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoDique/Screenshot/Screenshot1.png)
![R.HydroTools.DisenoDique.Screenshot2](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoDique/Screenshot/Screenshot2.png)
![R.HydroTools.DisenoDique.Screenshot3](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoDique/Screenshot/Screenshot3.png)
![R.HydroTools.DisenoDique.Screenshot4](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoDique/Screenshot/Screenshot4.png)


## Referencias

* https://www.hec.usace.army.mil/software/hec-ras/


## Colaboradores

* Creado por r.cfdtools@gmail.com


## Compatibilidad

* El libro de cálculo no utiliza funciones exclusivas de Microsoft 365 y puede ser ejecutado en cualquier version de Microsoft Excel.


## Keywords
Leeve design. Leeve protection. Overflow protection.


## Control de versiones

Versión | Descripción
--- | ---
| v.20211105 | Actualización general de análisis, gráficas y formato. Inclusión de cálculo básico de volumen de suelo requerido.


## Licencia, cláusulas y condiciones de uso
https://github.com/rcfdtools/R.HydroTools/wiki/License


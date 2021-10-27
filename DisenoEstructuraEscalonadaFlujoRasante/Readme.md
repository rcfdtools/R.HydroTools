## Estructura escalonada en sección rectangular a flujo rasante, método Iwao Ohtsu

El diseño y construcción de canales hidráulicos requiere frecuentemente del diseño de estructuras escalonadas, cuando existen diferencias importantes de nivel entre el fondo del cauce intervenido y el cauce o canal receptor.


### Casos en los que se requiere del uso de estructuras escalonadas

* Entrega de cauces laterales a cauces o a canales principales.
* Entrega de cuencas remanentes en cortes de vías a cunetas, canales perimetrales o ríos.
* Canales realineados en los que existe una diferencia considerable de altura entre el fondo de inicio realineado y el fondo del canal de entrega.


### Funcionalidades

* Diseño de estructura escalonada de hasta 100 escalones.
* Botónes de acción para resolver el tamaño de huella requerido para obtener una inclinación máxima de 19°.
* Graficación de perfil.
* Factor multiplicador para dibujo de tramos de aproximación de inicio y entrega, requeridos para desarrollar el flujo en la modelación hidráulica antes de pasar por la estructura.
* Ingreso de valor para prevención de coalineación en paredes verticales para el ensamble correcto del modelo de terreno triangulado. Este valor puede ser definido en cero cuando se requiere construir la superficie con paredes usando herramientas de dibujo diferentes a Esri ArcGIS for Desktop.
* Ingreso de valor de pendiente para tramos de aproximación de inicio y entrega.
* Generación de tabla con geolocalizadores XYZ de los nodos que conforman la estructura.
* Toolbox en ArcGIS for Desktop para la creación de la nube de puntos 3D, eliminación de nodos idénticos, modelo de terreno triangulado, grilla ráster de alta resolución, dominio límite y triangulos 3D.
* Representación 3D en ArcScene.


### Descripción de archivos y carpetas

Archivo / Folder | Descripción
--- | ---
| R.HydroTools.DisenoEstructuraEscalonadaFlujoRasanteGIS.mxd | Mapa ArcMap 10.2.2 para visualización 2D de resultados de ejecución del Toolbox.
| R.HydroTools.DisenoEstructuraEscalonadaFlujoRasanteGIS.sxd | Escena ArcScene 10.2.2 para visualización 3D de modelos de terreno y capas vectoriales de la estructura generados por el Toolbox.
| R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.xlsm | Libro de diseño de la estructura.
| R.HydroTools.DisenoEstructuraEscalonadaFlujoRasanteFolderStructure.zip | Comprimido con estructura de directorios requerida en D:\ para la ejecución del Toolbox. 
| R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.tbx | Caja de herramientas ToolBox ESRI ArcGIS for Desktop con modelador de procesos para creación de archivos de formas 3D.
| R.HydroTools.DisenoEstructuraEscalonadaFlujoRasanteGIS.xls | Tabla geocodificada con localización de nodos 3D de la estructura. Requerido por el modelador de procesos geográficos contenido en el Toolbox.
| /MDT/ | Carpeta de volcado de modelos de terreno en formato vectorial TIN y Ráster generado por el Toolbox.
| /SHP/ | Carpeta de volcado de nodos y caras 3D del modelo de terreno vectorial en formato ESRI Shapefile.


### Procedimiento para creación de superficie usando ArcGIS for Desktop

1. Copie los valores de la hoja _GIS_ del libro de diseño R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.xlsm, incluída la cabecera.
2. Peque los valores en el libro de cálculo R.HydroTools.DisenoEstructuraEscalonadaFlujoRasanteGIS.xls en la hoja _GIS_. Copiar libro en D:\R.HydroTools\DisenoEstructuraEscalonadaFlujoRasante\
3. En ArcMAP, cargue y ejecute el ToolBox R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.tbx. Se recomienda el uso de las rutas predeterminadas: D:\R.HydroTools\DisenoEstructuraEscalonadaFlujoRasante. Dentro de esta carpeta es necesario crear las carpetas MDT y SHP.
4. Visualice los resultados obtenidos en ArcMAP y en ArcScene.

Nota: El archivo R.HydroTools.DisenoEstructuraEscalonadaFlujoRasanteFolderStructure.zip contiene la estructura de directorios requerida en la unidad D:\.


## Ilustraciones

![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot1](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoEstructuraEscalonadaFlujoRasante/Screenshot/Screenshot1.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot2](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoEstructuraEscalonadaFlujoRasante/Screenshot/Screenshot2.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot3](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoEstructuraEscalonadaFlujoRasante/Screenshot/Screenshot3.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot4](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoEstructuraEscalonadaFlujoRasante/Screenshot/Screenshot4.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot5](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoEstructuraEscalonadaFlujoRasante/Screenshot/Screenshot5.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot6](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoEstructuraEscalonadaFlujoRasante/Screenshot/Screenshot6.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot7](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoEstructuraEscalonadaFlujoRasante/Screenshot/Screenshot7.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot8](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoEstructuraEscalonadaFlujoRasante/Screenshot/Screenshot8.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot9](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoEstructuraEscalonadaFlujoRasante/Screenshot/Screenshot9.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot10](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoEstructuraEscalonadaFlujoRasante/Screenshot/Screenshot10.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot11](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoEstructuraEscalonadaFlujoRasante/Screenshot/Screenshot11.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot12](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoEstructuraEscalonadaFlujoRasante/Screenshot/Screenshot12.png)



## Referencias

* Ohtsu, Y. Yasuda & Takahashi M., "Flood Characteristics of Skimming Flows in Stepped Channels", Journal of Hydraulic Engineering, Vol. 130, No. 9, ASCE, September 2004.
* Esquemas INVIAS, Manual de Drenaje, Pág. 4-81.
* Formulación: baalkara@gmail.com, ECIJG-JAGM, r.cfdtools@gmail.com. Esquema: r.cfdtools@gmail.com. Revisión y formato: r.cfdtools@gmail.com


## Keywords
Hydraulic Stepped structure.


## Control de versiones

Versión | Descripción
--- | ---
| v.20211027 | Actualización general de análisis, gráficas y formato. Desarrollo e incorporación de Esri Toolbox para la creación automática de superficies para ensamblado de prototipos hidráulicos en HEC-RAS 2D. Inclusión de factor multiplicador para dibujo de tramos de aproximación de inicio y entrega. Inclusión de valor para prevención de coalineación. Actualización para diseño de estructura de hasta 100 escalones. Validación para obtener número entero de escalones. Inclusión de pendiente en tramos de aproximación.


## Licencia, cláusulas y condiciones de uso
https://github.com/rcfdtools/R.HydroTools/wiki/License


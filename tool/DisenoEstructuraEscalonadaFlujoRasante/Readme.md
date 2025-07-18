<div align="center"><img alt="R.HydroTools" src="../../file/graph/R.HydroTools.svg" width="300px"></div>

## Estructura escalonada en sección rectangular a flujo rasante, método Iwao Ohtsu
Keywords: `hydraulics` `hydraulic-structure` `hydraulic-stepped-structure`

El diseño y construcción de canales hidráulicos, requiere frecuentemente del diseño de estructuras escalonadas cuando existen diferencias importantes de nivel entre el fondo del cauce lateral intervenido y el cauce o canal receptor.


### Casos en los que se requiere del uso de estructuras escalonadas

* Entrega de cauces laterales a cauces o a canales principales.
* Entrega de cuencas remanentes en cortes de vías a cunetas, canales perimetrales o ríos.
* Canales realineados en los que existe una diferencia considerable de altura entre el fondo de inicio realineado y el fondo del canal de entrega.


### Requerimientos

* [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel) 2013 o superior
* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/)


### Funcionalidades

* Diseño de estructura escalonada de hasta 100 escalones.
* Botones de acción para resolver el tamaño de huella requerido para obtener una inclinación máxima de 19°.
* Graficación de perfil.
* Factor multiplicador para dibujo de tramos de aproximación de inicio y entrega, requeridos para desarrollar el flujo en la modelación hidráulica antes de pasar por la estructura.
* Ingreso de valor para prevención de coalineación en paredes verticales para el ensamble correcto del modelo de terreno triangulado. Este valor puede ser definido en cero cuando se requiere construir la superficie con paredes usando herramientas de dibujo diferentes a Esri ArcGIS for Desktop.
* Ingreso de valor de pendiente para tramos de aproximación de inicio y entrega.
* Generación de tabla con geolocalizadores XYZ de los nodos que conforman la estructura.
* Toolbox en ArcGIS for Desktop para la creación de la nube de puntos 3D, eliminación de nodos idénticos, modelo de terreno triangulado, grilla ráster de alta resolución, dominio límite y triangulos 3D.
* Representación 3D en ArcScene.


### Descripción de archivos y carpetas

| Archivo / Folder                                                                                                                                                                                                                            | Descripción                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [R.HydroTools.DisenoEstructuraEscalonadaFlujoRasanteGIS.mxd ](R.HydroTools.DisenoEstructuraEscalonadaFlujoRasanteGIS.mxd)                        | Mapa ArcMap 10.2.2 para visualización 2D de resultados de ejecución del Toolbox.                                                               |
| [R.HydroTools.DisenoEstructuraEscalonadaFlujoRasanteGIS.sxd ](R.HydroTools.DisenoEstructuraEscalonadaFlujoRasanteGIS.sxd)                        | Escena ArcScene 10.2.2 para visualización 3D de modelos de terreno y capas vectoriales de la estructura generados por el Toolbox.              |
| [R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.xlsm ](R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.xlsm)                            | Libro de diseño de la estructura.                                                                                                              |
| [R.HydroTools.DisenoEstructuraEscalonadaFlujoRasanteFolderStructure.zip](R.HydroTools.DisenoEstructuraEscalonadaFlujoRasanteFolderStructure.zip) | Comprimido con estructura de directorios requerida en D:\ para la ejecución del Toolbox.                                                       | 
| [R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.tbx](R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.tbx)                               | Caja de herramientas ToolBox ESRI ArcGIS for Desktop con modelador de procesos para creación de archivos de formas 3D.                         |
| [R.HydroTools.DisenoEstructuraEscalonadaFlujoRasanteGIS.xls](R.HydroTools.DisenoEstructuraEscalonadaFlujoRasanteGIS.xls)                         | Tabla geocodificada con localización de nodos 3D de la estructura. Requerido por el modelador de procesos geográficos contenido en el Toolbox. |
| /MDT/                                                                                                                                                                                                                                       | Carpeta de volcado de modelos de terreno en formato vectorial TIN y ráster generado por el Toolbox.                                            |
| /SHP/                                                                                                                                                                                                                                       | Carpeta de volcado de nodos y caras 3D del modelo de terreno vectorial en formato ESRI Shapefile.                                              |


### Procedimiento para creación de superficie usando ArcGIS for Desktop

1. Copie los valores de la hoja _GIS_ del libro de diseño _R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.xlsm_, incluida la cabecera.
2. Peque los valores en el libro de cálculo _R.HydroTools.DisenoEstructuraEscalonadaFlujoRasanteGIS.xls_ en la hoja _GIS_. Copiar libro en _D:\R.HydroTools\DisenoEstructuraEscalonadaFlujoRasante\_
3. En ArcMAP, cargue y ejecute el ToolBox _R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.tbx_. Se recomienda el uso de las rutas predeterminadas: _D:\R.HydroTools\DisenoEstructuraEscalonadaFlujoRasante_. Dentro de esta carpeta es necesario crear las carpetas MDT y SHP.
4. Visualice los resultados obtenidos en ArcMAP y en ArcScene.

> El archivo _R.HydroTools.DisenoEstructuraEscalonadaFlujoRasanteFolderStructure.zip_ contiene la estructura de directorios requerida en la unidad D:\.


### Botones de acción

```
Sub Resolvery1()
    ' Resolver el valor de la altura de lámina sobre el escalón o y1
    ' https://github.com/rcfdtools/R.HydroTools/tree/main/DisenoEstructuraEscalonadaFlujoRasante
    Sheets("EscalonadaFlujoRasante").Select
    Range("C16").Select
    ActiveCell.FormulaR1C1 = 0.0001
    Range("C15").GoalSeek Goal:=0, ChangingCell:=Range("C16")
End Sub
```

```
Sub Resolverdw()
    ' Resolver el valor de la profundidad de lámina de agua cuando no se alcanza la condición de flujo quasi-uniforme
    ' https://github.com/rcfdtools/R.HydroTools/tree/main/DisenoEstructuraEscalonadaFlujoRasante
    Sheets("EscalonadaFlujoRasante").Select
    Range("C57").Select
    ActiveCell.FormulaR1C1 = 0.0001
    Range("C56").GoalSeek Goal:=0, ChangingCell:=Range("C57")
End Sub
```

```
Sub Resolverhuella19d()
    ' Resolver el valor de la longitud de la huella para que la inclinación del pseudo fondo no sea superior a 19 grados de inclinación
    ' https://github.com/rcfdtools/R.HydroTools/tree/main/DisenoEstructuraEscalonadaFlujoRasante
    Sheets("EscalonadaFlujoRasante").Select
    Range("C26").GoalSeek Goal:=18.999, ChangingCell:=Range("C7")
End Sub
```

```
Sub Resolvery2conqu()
    ' Resolver el valor de la altura de lámina o y2 en la zona inferior de la estructura alcanzando la condición Quasi uniforme.
    ' https://github.com/rcfdtools/R.HydroTools/tree/main/DisenoEstructuraEscalonadaFlujoRasante
    Sheets("EscalonadaFlujoRasante").Select
    Range("C77").Select
    ActiveCell.FormulaR1C1 = Range("C13") * 1.1
    Range("C79").GoalSeek Goal:=0, ChangingCell:=Range("C77")
End Sub
```

```
Sub Resolvery2sinqu()
    ' Resolver el valor de la altura de lámina o y2 en la zona inferior de la estructura sin alcanzar la condición Quasi uniforme.
    ' https://github.com/rcfdtools/R.HydroTools/tree/main/DisenoEstructuraEscalonadaFlujoRasante
    Sheets("EscalonadaFlujoRasante").Select
    Range("D77").Select
    ActiveCell.FormulaR1C1 = Range("C13") * 1.1
    Range("D79").GoalSeek Goal:=0, ChangingCell:=Range("D77")
End Sub
```


### Ilustraciones

![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot1](Screenshot/Screenshot1.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot2](Screenshot/Screenshot2.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot3](Screenshot/Screenshot3.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot4](Screenshot/Screenshot4.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot5](Screenshot/Screenshot5.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot6](Screenshot/Screenshot6.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot7](Screenshot/Screenshot7.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot8](Screenshot/Screenshot8.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot9](Screenshot/Screenshot9.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot10](Screenshot/Screenshot10.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot11](Screenshot/Screenshot11.png)
![R.HydroTools.DisenoEstructuraEscalonadaFlujoRasante.Screenshot12](Screenshot/Screenshot12.png)


### Referencias

* Ohtsu, Y. Yasuda & Takahashi M., "Flood Characteristics of Skimming Flows in Stepped Channels", Journal of Hydraulic Engineering, Vol. 130, No. 9, ASCE, September 2004.
* Esquemas INVIAS, Manual de Drenaje, Pág. 4-81.
* Formulación: [frankv13](https://github.com/frankv13), jagm, [rcfdtools](https://github.com/rcfdtools). Esquema y GIS: [rcfdtools](https://github.com/rcfdtools). Revisión y formato: [rcfdtools](https://github.com/rcfdtools)


### Control de versiones

| Versión     | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Autor                                                                                        | Horas |
|-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|:-----:|
| 2022.07.25  | Actualización general de documentación.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [rcfdtools](https://github.com/rcfdtools)                                                    |  0.5  |
| 2021.10.23  | Actualización general de análisis, gráficas y formato. Desarrollo e incorporación de Esri Toolbox para la creación automática de superficies para ensamblado de prototipos hidráulicos en HEC-RAS 2D. Inclusión de factor multiplicador para dibujo de tramos de aproximación de inicio y entrega. Inclusión de valor para prevención de coalineación. Actualización para diseño de estructura de hasta 100 escalones. Validación para obtener número entero de escalones. Inclusión de pendiente en tramos de aproximación. | [rcfdtools](https://github.com/rcfdtools)                                                    |  16   |
| 2018.08.08  | Versión inicial.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [rcfdtools](https://github.com/rcfdtools)<br>[frankv13](https://github.com/frankv13)<br>jagm |  12   |


### Licencia, cláusulas y condiciones de uso

_R.HydroTools es de uso libre para fines académicos, conoce nuestra [licencia, cláusulas, condiciones de uso](../../LICENSE.md) y como referenciar los contenidos publicados en este repositorio._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [r.cfdtools](https://github.com/rcfdtools) en GitHub._

| [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.HydroTools/discussions/12) |
|------------------------------------------------------------------|-------------------------------------------------------------------------------|

## Perfil de terreno del valle, evaluación de estructuras de caída y análisis de corte vs. relleno
Keywords: `Hydraulics` `River profile` `Valley profile` `Cut and filling`

A partir de la información topográfica disponible bajo la zona del eje del valle suavizado trazado y utilizando las secciones transversales del modelo de muestreo HEC-RAS, establecer si el canal artificial a diseñar estará en corte y/o relleno. El procedimiento presentado analiza solo el corte del valle y el posible uso de estructuras de caída para ajuste de pendiente.

Para obtener el perfil por los puntos más bajos de cada sección, crear un modelo HEC-GeoRAS con ejes de río, bancas, líneas de flujo y secciones transversales. Las secciones transversales deberán conectar los diferentes puntos de la topobatimetría de cada sección.

Luego de importar la geometría creada en HEC-GeoRAS al HEC-RAS, seleccionar el tramo de río y dibujar el perfil. El perfil mostrado en HEC-RAS corresponde a los puntos más bajos de cada sección de muestreo entre bancas. Para obtener las abscisas y las cotas asociadas de eje y bancas, en la ventana del perfil ir a _File_ y seleccionar la opción _Copy Values to Clipboard_.

El abscisado en HEC-RAS siempre se realiza en el sentido inverso del flujo. Aguas abajo en el punto de salida se encuentra la abscisa cero y aguas arriba la abscisa correspondiente al punto de inicio del realineamiento.


### Consideraciones

* El análisis de cortes y rellenos se calcula a partir de la diferencia entre la línea proyectada del fondo continuo y la cota del terreno natural.
* La relación de corte vs. relleno permite identificar si el alineamiento del valle requiere o no de un nuevo trazado para buscar la condición de equilibrio o garantizar que el nuevo canal se encuentre mayoritariamente en corte debido a que pueden existir restricciones de disponibilidad de material para la conformación del canal.
* Es necesario identificar las cotas de fondo de los cauces laterales en el punto de entrega al nuevo eje suavizado de valle e identificar si se encuentran entregado a fondo o por encima. En caso de que la cota de fondo de un cauce lateral esté entregando por debajo de la línea proyectada de fondo del valle, será necesario incluir una estructura de caída para que el cauce pueda entregar a fondo o por encima.
* Para canales prismáticos en los que no se realiza diseño sinuoso para la fracción correspondiente al cauce dominante, podrá como diseñador proponer e incluir estructuras de caída para reducir la pendiente.


### Requerimientos

* [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel) 2013 o superior


### Ilustraciones

![R.HydroTools.PerfilValleEstCaidaCorteRelleno.Screenshot1](https://github.com/rcfdtools/R.HydroTools/blob/main/PerfilValleEstCaidaCorteRelleno/Screenshot/Screenshot1.png)
![R.HydroTools.PerfilValleEstCaidaCorteRelleno.Screenshot2](https://github.com/rcfdtools/R.HydroTools/blob/main/PerfilValleEstCaidaCorteRelleno/Screenshot/Screenshot2.png)
![R.HydroTools.PerfilValleEstCaidaCorteRelleno.Screenshot3](https://github.com/rcfdtools/R.HydroTools/blob/main/PerfilValleEstCaidaCorteRelleno/Screenshot/Screenshot3.png)


### Control de versiones

| Versión     | Descripción                                            | Autor                                      | Horas |
|-------------|:-------------------------------------------------------|--------------------------------------------|:-----:|
| 2021.11.14  | Actualización general de formato, gráficas y títulos.  | [rcfdtools](https://github.com/rcfdtools)  |  2    |
| 2020.10.11  | Inclusión análisis de relación corte vs. relleno.      | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2014.09.08  | Versión inicial.                                       | [rcfdtools](https://github.com/rcfdtools)  |  12   |


R.HydroTools es de uso libre para fines académicos, conoce nuestra [licencia, cláusulas, condiciones de uso](https://github.com/rcfdtools/R.HydroTools/wiki/License) y como referenciar los contenidos publicados en este repositorio.

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [r.cfdtools](https://github.com/rcfdtools) en GitHub._

| [:house: Inicio](https://github.com/rcfdtools/R.HydroTools/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.HydroTools/discussions/21) |
|------------------------------------------------------------------|------------------------------------------------------------------------------|

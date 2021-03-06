## Registro y validación de hidrogramas obtenidos a partir de modelación hidrológica en HEC-HMS
Keywords: `Hydrology` `Hydrograph` `Water flow` `Tr - Design return period` 

Este libro de cálculo es utilizado para registrar y validar los pulsos obtenidos en modelos hidrológicos de eventos discretos o de valores máximos. La hoja _Hidrograma4a_ presenta un ejemplo para la estimación de pulsos de hidrogramas para periodos de retorno superiores a partir de los valores pico obtenidos en los periodos de retorno registrados. 


### Consideraciones

* La regresión es realizada a través de la tendencia logarítmica que se obtiene, por ejemplo, para periodos de retorno de 2.33, 5, 10, 25, 50 y 100 años. 
* El tiempo al pico se va reduciendo a medida que se aumenta el periodo de retorno.
* Para periodos de retorno altos, el tiempo al pico presenta poca variabilidad.


### Requerimientos

* [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel) 2013 o superior


### Guidelines for the selection of return period [^1]

| Type of project or feature                       | Tr - return period, yr  |
|:-------------------------------------------------|:------------------------|
| Urban drainage [low risk] (up to 100 ha)         | 5 to 10                 |                 
| Urban drainage [medium risk] (more than 100 ha)  | 25 to 50                |               
| Road drainage                                    | 25 to 50                |                
| Principal spillways (dams)                       | 25 to 100               |               
| Highway drainage                                 | 50 to 100               |               
| Levees [medium risk]                             | 50 to 100               |               
| Urban drainage [high risk] (more than 1,000 ha)  | 50 to 100               |               
| Flood plain development                          | 100                     |                     
| Bridge design (piers)                            | 100 to 500              |              
| Levees [high risk]                               | 200 to 1000             |            
| Emergency spillways (dams)                       | 100 to 10,000 (PMP)     |     
| Freeboard hydrograph [for a class (c) dam]       | 10,000 (PMP)            |            

> PMP: precipitación máxima probable.


### Lineamientos generales para modelos hidrológicos en HEC-HMS

1. Para importación de archivos .csv en HEC-DSS 3.2.3 o superior, es necesario saltar y no importar el último registro de la tabla en el proceso de extracción - transformación y cargue (ETL). Los archivos de hietogramas están compuestos de múltiples registros, de los cuales 5 corresponden a cabeceras de importación de unidades y partes A,B,C,F, los demás registros corresponden a datos, excepto el último registro que corresponde al salto de línea final del archivo .csv que no debe ser importado. Para saltar este registro, de clic derecho en el número de registro (p. ej. el número 295) y seleccione la opción Skip, para finalizar de clic en Import.
2. En subcuencas laterales que no tienen subdivisiones o tránsitos hidrológicos se toma el hidrograma obtenido de la transformación lluvia - escorrentía y para subcuencas laterales con subdivisiones y tránsitos, se toma el hidrograma del último tramo en tránsito de la subcuenca lateral más el hidrograma de la última subcuenca que corresponde a la transformación lluvia escorrentía de la cuenca del tramo en tránsito indicado.
3. En subcuencas laterales inmediatas al punto de entrega sobre un nuevo eje del valle, se debe descontar para cada pulso y proporcionalmente en función del área, la fracción correspondiente remanente luego del punto de entrega. Aplica tanto para subcuencas únicas laterales o subcuencas laterales con tramos en tránsito y su correspondiente subcuenca.
4. Para cuencas laterales se debe estimar un factor de atenuación de toda el área que aporta hasta el punto de descarga sobre el nuevo eje de valle; se realiza la modelación hidrológica con esos factores y se obtienen los hidrogramas. Para esas mismas cuencas también es necesario extraer los hidrogramas pero con el factor de atenuación del punto combinado. Los primeros hidrogramas se utilizan para diseñar las estructuras de entrega, los segundos hidrogramas para la modelación hidráulica conjunta del cauce principal con entregas laterales. 


### Ilustraciones

![R.HydroTools.HidrogramaRegVal.Screenshot1](https://github.com/rcfdtools/R.HydroTools/blob/main/HidrogramaRegVal/Screenshot/Screenshot1.png)
![R.HydroTools.HidrogramaRegVal.Screenshot2](https://github.com/rcfdtools/R.HydroTools/blob/main/HidrogramaRegVal/Screenshot/Screenshot2.png)
![R.HydroTools.HidrogramaRegVal.Screenshot3](https://github.com/rcfdtools/R.HydroTools/blob/main/HidrogramaRegVal/Screenshot/Screenshot3.png)
![R.HydroTools.HidrogramaRegVal.Screenshot4](https://github.com/rcfdtools/R.HydroTools/blob/main/HidrogramaRegVal/Screenshot/Screenshot4.png)


### Control de versiones

| Versión     | Descripción                                                                                                                                                                 | Autor                                      | Horas |
|-------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.07.25  | Actualización general de documentación.                                                                                                                                     | [rcfdtools](https://github.com/rcfdtools)  |  0.5  |
| 2021.10.14  | Actualización general de formato.                                                                                                                                           | [rcfdtools](https://github.com/rcfdtools)  |   2   |
| 2021.10.11  | Inclusión de regresión logarítmica para la estimación de pulsos para periodos de retorno superiores a los registrados por factor Trn / Tr100. Ejemplo en hoja Hidrograma4a. | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2014.09.06  | Versión inicial.                                                                                                                                                            | [rcfdtools](https://github.com/rcfdtools)  |  12   |


R.HydroTools es de uso libre para fines académicos, conoce nuestra [licencia, cláusulas, condiciones de uso](https://github.com/rcfdtools/R.HydroTools/wiki/License) y como referenciar los contenidos publicados en este repositorio.

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [r.cfdtools](https://github.com/rcfdtools) en GitHub._

| [:house: Inicio](https://github.com/rcfdtools/R.HydroTools/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.HydroTools/discussions/19) |
|------------------------------------------------------------------|-------------------------------------------------------------------------------|

[^1]: http://ponce.sdsu.edu/return_period.html
## Gradación y rugosidad de diseño en canales
Keywords: `Hydraulics` `Manning roughness` `Soil bed gradation` 

Tamaño característico del material que compone el lecho o la zona de corte en canales realineados y valores de rugosidad a utilizar en el diseño hidráulico de la sección compuesta para la aplicación de diferentes métodos de diseño (Shields, Lane) usando HEC-RAS o el libro de diseño r.cfdtools. El análisis de gradación para determinar los valores d16, d50, d65, d75, d84 y d90, utiliza como referencia la metodología Norma INV-E213-13 - Colombia - Suramérica.


### Requerimientos

* [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel) 2013 o superior


### Métodos incluidos para estimar el valor característico de la rugosidad de Manning


#### Basados en d50
| Autor                                                                      | Ecuación empírica                         | Descripción o referencia                                                                                                                                                                                          |
|----------------------------------------------------------------------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Strikler, 1923                                                             | 𝑛=0.0152(𝐷<sub>50</sub>)<sup>1⁄6<sup>   | Ríos con lecho de grava en Suiza                                                                                                                                                                                  |                                                                                                                                                                                  
| Posada, 1998                                                               | 𝑛=0.0487(𝐷<sub>50</sub>)<sup>1⁄6<sup>   | Ríos de montaña con lecho de grava, Antioquia y Risaralda. Estudio en canales naturales                                                                                                                           |                                                                                                                           
| Keulegan, 1938 y 1949                                                      | 𝑛=0.0260(𝐷<sub>50</sub>)<sup>1⁄6<sup>   | Universidad Nacional de Colombia, sede Medellín. Escuela de Geociencias y Medio Ambiente, Ramiro Marbello Pérez                                                                                                   |                                                                                                   
| Administración de carreteras federales de Estados unidos de América, 1975  | 𝑛=0.0395(𝐷<sub>50</sub>)<sup>1⁄6<sup>   | Universidad Nacional de Colombia, sede Medellín. Escuela de Geociencias y Medio Ambiente, Ramiro Marbello Pérez                                                                                                   |                                                                                                   
| Simons y Senturk, 1976                                                     | 𝑛=0.0389(𝐷<sub>50</sub>)<sup>1⁄6<sup>   | Universidad Nacional de Colombia, sede Medellín. Escuela de Geociencias y Medio Ambiente, Ramiro Marbello Pérez                                                                                                   |                                                                                                   
| Garde y Raju, 1978                                                         | 𝑛=0.039(𝐷<sub>50</sub>)<sup>1⁄6<sup>    | Universidad Nacional de Colombia, sede Medellín. Escuela de Geociencias y Medio Ambiente, Ramiro Marbello Pérez. Granulometría gruesa y libre de ondulaciones. 50% del material por peso tiene un diámetro menor. | 
| Bray, 1979                                                                 | 𝑛=0.0593(𝐷<sub>50</sub>)<sup>0.179<sup> | Universidad Nacional de Colombia, sede Medellín. Escuela de Geociencias y Medio Ambiente, Ramiro Marbello Pérez                                                                                                   |                                                                                                   
| Subramanya, 1982                                                           | 𝑛=0.047(𝐷<sub>50</sub>)<sup>1⁄6<sup>    | Universidad Nacional de Colombia, sede Medellín. Escuela de Geociencias y Medio Ambiente, Ramiro Marbello Pérez                                                                                                   |                                                                                                   


#### Basados en d65
| Autor                  | Ecuación empírica                         | Descripción o referencia                                                                                        |
|------------------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Keulegan, 1938 y 1949  | 𝑛=0.0416(𝐷<sub>65</sub>)<sup>1⁄6<sup>   | Universidad Nacional de Colombia, sede Medellín. Escuela de Geociencias y Medio Ambiente, Ramiro Marbello Pérez |                        
| Chow, 1959             | 𝑛=0.0417(𝐷<sub>65</sub>)<sup>1⁄6<sup>   | Universidad Nacional de Colombia, sede Medellín. Escuela de Geociencias y Medio Ambiente, Ramiro Marbello Pérez |                                       
| Raudkivi, 1975         | 𝑛=0.013(𝐷<sub>65</sub>)<sup>1⁄6<sup>    | Continuación del trabajo de Stickler. Universidad Nacional de Colombia, sede Medellín                           | 
| Bray, 1979             | 𝑛=0.0561(𝐷<sub>65</sub>)<sup>0.179<sup> | Universidad Nacional de Colombia, sede Medellín. Escuela de Geociencias y Medio Ambiente, Ramiro Marbello Pérez |                       


#### Basados en d75
| Autor          | Ecuación empírica                       | Descripción o referencia                                                         |
|----------------|-----------------------------------------|----------------------------------------------------------------------------------|
| Lane y Carlson | 𝑛=0.038(𝐷<sub>75</sub>)<sup>1⁄6<sup>  | Obtenida a través de experimentos de campo, en canales empedrados con guijarros. | 


#### Basados en d90
| Autor                        | Ecuación empírica                        | Descripción o referencia                                                                                                         |
|------------------------------|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Meyer - Peter y Muller, 1948 | 𝑛=0.038(𝐷<sub>90</sub>)<sup>1⁄6<sup>   | Mezclas de materiales de fondo con una significativa muestra de materiales granulométricos d90, tiene en cuenta el acorazamiento | 
| Keulegan, 1938 y 1949        | 𝑛=0.0249(𝐷<sub>90</sub>)<sup>1⁄6<sup>  | Universidad Nacional de Colombia, sede Medellín. Escuela de Geociencias y Medio Ambiente, Ramiro Marbello Pérez                  |                  
| Bray, 1979                   | 𝑛=0.0495(𝐷<sub>90</sub>)<sup>0.16<sup> | Universidad Nacional de Colombia, sede Medellín. Escuela de Geociencias y Medio Ambiente, Ramiro Marbello Pérez                  |                  
| Yen, 1992                    | 𝑛=0.0384(𝐷<sub>90</sub>)<sup>0.16<sup> | Universidad Nacional de Colombia, sede Medellín. Escuela de Geociencias y Medio Ambiente, Ramiro Marbello Pérez                  |                  


### Ilustraciones

![R.HydroTools.GradacionRugosidad.Screenshot1](https://github.com/rcfdtools/R.HydroTools/blob/main/GradacionRugosidad/Screenshot/Screenshot1.png)
![R.HydroTools.GradacionRugosidad.Screenshot2](https://github.com/rcfdtools/R.HydroTools/blob/main/GradacionRugosidad/Screenshot/Screenshot2.png)
![R.HydroTools.GradacionRugosidad.Screenshot3](https://github.com/rcfdtools/R.HydroTools/blob/main/GradacionRugosidad/Screenshot/Screenshot3.png)


### Referencias

* http://artemisa.unicauca.edu.co/~hdulica/T_TRANSPORTE_SEDIMENTOS.pdf
* http://wwwrcamnl.wr.usgs.gov/sws/fieldmethods/Indirects/nvalues/index.htm
* US Army Corps of Engineers. HEC-RAS River Analysis System, Hydraulic Reference Manual, Versión 5.0. CPD-69. 2016.2
* Escuela de Geociencias y Medio Ambiente, Ramiro Marbello Pérez
* Open Channel Hydraulics, 1985. French, R.
* http://bdigital.unal.edu.co/12697/60/3353962.2005.Parte%2011.pdf


### Control de versiones

| Versión     | Descripción                                            | Autor                                      | Horas |
|-------------|:-------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.07.25  | Actualización general de documentación.                | [rcfdtools](https://github.com/rcfdtools)  |  0.5  |
| 2021.10.19  | Actualización general de análisis, gráficas y formato. | [rcfdtools](https://github.com/rcfdtools)  |   2   |
| 2014.09.06  | Versión inicial.                                       | [rcfdtools](https://github.com/rcfdtools)  |  12   |


R.HydroTools es de uso libre para fines académicos, conoce nuestra [licencia, cláusulas, condiciones de uso](https://github.com/rcfdtools/R.HydroTools/wiki/License) y como referenciar los contenidos publicados en este repositorio.

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [r.cfdtools](https://github.com/rcfdtools) en GitHub._

| [:house: Inicio](https://github.com/rcfdtools/R.HydroTools/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.HydroTools/discussions/18)  |
|------------------------------------------------------------------|-------------------------------------------------------------------------------|

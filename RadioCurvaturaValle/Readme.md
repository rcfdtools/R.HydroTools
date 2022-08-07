## Estimación del radio de curvatura para el suavizado del valle en canales, Rc
Keywords: `Hydraulics` `Valley bend radius` 

Existen diversas metodologías para estimar la curvatura de suavizado del eje recto del valle. El suavizado tiene como propósito garantizar un adecuado cambio de dirección en el río que permita el flujo o tránsito de las crecientes de forma segura y evitando en lo posible turbulencias, oleaje y zonas susceptibles a procesos erosivos y/o de depositación de sedimentos, buscando de mantener velocidad constante en el flujo.


### Requerimientos

* [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel) 2013 o superior


### Consideraciones generales para el trazado del eje de valle

Generalmente, el alineamiento, ancho y suavizado del valle está condicionado por múltiples restricciones.

| Condición o restricción   | Descripción                                                                                                                                                                                                                                                               |
|:--------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Topográfica               | Zonas con bajos que impiden que el canal se trace en corte o zonas que hidráulicamente drenan hacia otras cuencas.                                                                                                                                                        |
| Geotécnica                | Fallas, afloramientos rocosos, acuíferos.                                                                                                                                                                                                                                 |
| Eco-ambiental             | Fauna y flora nativa en suelos de protección. Corredor para el transito de especies endémicas protegidas.                                                                                                                                                                 |
| Infraestructura existente | Instalaciones, vías, canales, tanques, bocatomas, asentamientos humanos.                                                                                                                                                                                                  |
| Territorial               | Incompatibilidad con los usos del suelo definidos en los POT, rondas de protección, zonas declararas de interés histórico. Resguardos indígenas y asentamientos de comunidades protegidas. Zonas agropecuarias productivas con puntos de agua superficial concesionada. |


### Métodos incluidos

| Método                                                                                          | Descripción                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Manual de procedimientos de pequeños sistemas de riego                                       | Estimación del radio de curvatura del valle para el diseño de canales a caudal máximo. Ref: Manual de procedimientos de pequeños sistemas de riego. Rango de caudales entre 0.5 y 20 m³/s.                                                                                                                                                                    |                                                                                                                                                                    
| 2. Universidad Utah State. Diseño Básico de Canales                                             | Estimación del radio de curvatura del valle para el diseño de canales a caudal máximo. Ref: Universidad Utah State. Diseño Básico de Canales. Rango de caudales entre 15 y 225 m³/s.                                                                                                                                                                          |                                                                                                                                                                          
| 3. En función del tipo de régimen. Subcrítico y Supercrítico                                    | Esta metodología no tiene en cuenta directamente el total caudal transportado por el valle y cauce dominante sino parámetros en función del régimen de flujo. Parámetros de entrada, profundidad del flujo y, velocidad V, ancho superficial T.                                                                                                               |                                                                                                               
| 4. Por factor multiplicador en función del caudal y la base (Wageningen, The Netherlands. 1978) | Estimación del radio de curvatura del valle para el diseño de canales a caudal máximo. Ref: "International Institute For Land Reclamation And Improvement" ILRI, Principios y Aplicaciones del Drenaje, Tomo IV, Wageningen The Netherlands 1978. Rango de caudales mínimos entre 0 y 17 m³/s. Rango de caudales máximos entre 10 y hasta mayores de 20 m³/s. | 
| 5. Por factor multiplicador en función del ancho (Urban Storm Drainage Criteria Manual )        | Estimación del radio de curvatura del valle para el diseño de canales. Ref:  Urban Drainage and Flood Control District. Urban Storm Drainage Criteria Manual Volume 1. Chapter 08 Open Channels, numeral 5.4, el radio de curvatura debe estar entre 3 o 4 veces el ancho superior del canal. Se estima en función del ancho superficial T.                   |                   
| 6. En función del tipo de canal. Salzitegger                                                    | Salzitegger Consult GMBH, Planificación de canales, Zona Piloto Ferreñafe, Tomo II/1. Proyecto Tinajones - Chiclayo 1984. En función del ancho superficial T y el tipo de drenaje o canal.                                                                                                                                                                    |                                                                                                                                                                    


### Referencias

* http://www.fao.org/3/a-at787s.pdf
* Manual de procedimientos de pequeños sistemas de riego.
* Universidad Utah State, Diseño Básico de Canales.
* International Institute For Land Reclamation And Improvement" ILRI, Principios y Aplicaciones del Drenaje, Tomo IV, Wageningen, The Netherlands. 1978.
* Urban Drainage and Flood Control District. Urban Storm Drainage Criteria Manual Volume 1. Chapter 08 Open Channels, numeral 5.4
* http://cybertesis.uach.cl/tesis/uach/2011/bmfcim722p/doc/bmfcim722p.pdf
* Salzitegger Consult GMBH, Planificación de canales, Zona Piloto Ferreñafe, Tomo II/1. Proyecto Tinajones - Chiclayo 1984.
* https://www.u-cursos.cl/ Facultad de ingeniería


### Ilustraciones

![R.HydroTools.RadioCurvaturaValle.Screenshot1](https://github.com/rcfdtools/R.HydroTools/blob/main/RadioCurvaturaValle/Screenshot/Screenshot1.png)
![R.HydroTools.RadioCurvaturaValle.Screenshot2](https://github.com/rcfdtools/R.HydroTools/blob/main/RadioCurvaturaValle/Screenshot/Screenshot2.png)
![R.HydroTools.RadioCurvaturaValle.Screenshot3](https://github.com/rcfdtools/R.HydroTools/blob/main/RadioCurvaturaValle/Screenshot/Screenshot3.png)
![R.HydroTools.RadioCurvaturaValle.Screenshot4](https://github.com/rcfdtools/R.HydroTools/blob/main/RadioCurvaturaValle/Screenshot/Screenshot4.png)


### Control de versiones

| Versión     | Descripción                                                                                                                                                                    | Autor                                      | Horas |
|-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.07.25  | Actualización general de documentación.                                                                                                                                        | [rcfdtools](https://github.com/rcfdtools)  |  0.5  |
| 2021.10.14  | Actualización general de formato.                                                                                                                                              | [rcfdtools](https://github.com/rcfdtools)  |   2   |
| 2020.10.11  | Inclusión de Método 5. Por factor multiplicador en función del ancho (Urban Storm Drainage Criteria Manual). Inclusión de Método 6. En función del tipo de canal. Salzitegger. | [rcfdtools](https://github.com/rcfdtools)  |   2   |
| 2016.05.19  | Versión inicial.                                                                                                                                                               | [rcfdtools](https://github.com/rcfdtools)  |   8   |

_R.HydroTools es de uso libre para fines académicos, conoce nuestra [licencia, cláusulas, condiciones de uso](https://github.com/rcfdtools/R.HydroTools/wiki/License) y como referenciar los contenidos publicados en este repositorio._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [r.cfdtools](https://github.com/rcfdtools) en GitHub._

| [:house: Inicio](https://github.com/rcfdtools/R.HydroTools/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.HydroTools/discussions/22) |
|------------------------------------------------------------------|------------------------------------------------------------------------------|


## CNE - Catálogo nacional de estaciones hidrometeorológicas del IDEAM - Colombia, descarga y análisis usando Python
Keywords: `IDEAM` `Station` `Weather` `Plot` `matplotlib` `Pandas` `os` `Meteorological` `Pivot Table` `Graph` `Catalog`

<div  align="center">
    <img align="center"  alt="CNEStationStatistic.png" src="https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/CNEStationStatistic.png" width="800px"/>
</div>


### Caso de estudio

El [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM](http://www.ideam.gov.co/) de Colombia, adscrito al [Ministerio de Medio Ambiente - Minambiente](https://www.minambiente.gov.co/), es la entidad nacional encargada registrar y mantener la información hidrometeorológica del país, incluida la localización y clasificación de la red de estaciones que hace parte del [Catálogo Nacional de Estaciones - CNE](http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls). A través del servicio de [Solicitud de Información](http://www.ideam.gov.co/solicitud-de-informacion) o a través del portal [DHIME](http://dhime.ideam.gov.co/atencionciudadano/) del IDEAM desde la pestaña _Recursos_, personas naturales o jurídicas, pueden obtener no solamente los catálogos, sino también las capas geográficas y los registros discretos registrados en cada estación. El código desarrollado en Python por [r.cfdtools](r.cfdtools@gmail.com), descarga de forma directa el archivo del catálogo nacional de estaciones y realiza un análisis estadístico detallado a través de los diferentes atributos registrados.


### Funcionalidades incorporadas

* Descarga directa del archivo del catálogo nacional de estaciones. Si en la fecha actual ya ha sido descargado el archivo, el script realizará únicamente su procesamiento.
* Configuración inicial modificable por el usuario para definir ruta de descarga `urlFile = 'http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls`, presentación de resumen corto de estaciones encontradas`sampleRecord = 12`, listado completo de estaciones con geo-localizadores `showAllRecords = False`.
* Despliegue de gráficas de análisis en ventanas emergentes a petición del usuario `showGraphScreen = False`, volcado automático de gráficas a formato PNG `plt.savefig()` y generación e impresión en consola de enlaces de consulta.
* Definición del método de análisis para la clasificación por pisos térmicos `thermalLevelCaldas = True`: convencional o Caldas 1802. Los arreglos de datos `thermalLevelRefConv` y `thermalLevelRefCaldas` utilizados para la clasificación pueden ser actualizados por el usuario.
* Definición de nombres de campos de atributos de análisis. En el evento de que el modelo de datos de estaciones IDEAM sea actualizado, reestructurado o normalizado, el usuario podrá evaluar el nombre de los nuevos campos y realizar la actualización de los nuevos nombres. Aplica para: nombre, latitud, longitud, altitud, CATEGORIA, TECNOLOGIA, ESTADO, FECHA_INSTALACION, DEPARTAMENTO, AREA_OPERATIVA, AREA_HIDROGRAFICA, ZONA_HIDROGRAFICA y SUBZONA_HIDROGRAFICA.
* Definición de nivel de transparencia en gráficas para ahorro en consumo de insumos de impresión.
* Identificación y resumen de atributos encontrados en el catálogo.
* Estadísticos generales sobre campos numéricos del catálogo.
* Estadístico de conteo y con normalización de estaciones por categoría, tecnología, estado, departamento, área operativa, área hidrográfica, zona hidrográfica, subzona hidrográfica y año de instalación.
* Generación automática de tablas y gráficas dinámicas por estado de actividad con análisis para categoría, tecnología, departamento, área operativa, área hidrográfica, zona hidrográfica, sub-zona hidrográfica y año de instalación.
* Análisis y graficación de estaciones por piso térmico para el método definido.
* Mapa de matriz de dispersión con localización de toda la red de estaciones subclasificada por elevación.
* Mapa de matriz de dispersión con localización de la red de estaciones subclasificada por elevación y por departamento.
* Diccionario de definiciones generales impreso como apéndice en la ventana de ejecución.
 
> En caso de que requiera analizar una versión antigua del archivo del catálogo nacional de estaciones, podrá cargar el archivo en cualquier repositorio de uso personal, redireccionar el script a la url del archivo y ejecutar el script. Tener en cuenta que las fechas presentadas en los análisis, corresponderán a la fecha del sistema operativo. Opcionalmente podrá crear una copia del archivo a analizar y modificar la fecha incluida en el nombre del archivo a la fecha actual en formato aaaammdd.

> En el evento de que por reestructuración del modelo de datos IDEAM, desaparezca alguno de los campos utilizados para el análisis general y la creación de las tablas dinámicas, el usuario deberá crear manualmente en el archivo .xls fuente, las columnas requeridas para la ejecución correcta del script.   


### Requerimientos

* Python 3.10.0+ como instalación independiente o standalone.
* PyCharm 2021.3+ for Anaconda.
* Sistema operativo Microsoft Windows.
* Xlrd 2.0.1.
* Matplotlib 3.5.1.
* Pandas 1.3.5.


### Atributos que componen el catálogo nacional de estaciones

Atributos tomados directamente del archivo [CNE_IDEAM.xls](http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls).

| Atributo             | Tipo           | Descripción                                                                                                                                                                                                                                     |
|----------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OBJECTID             | int64          | Identificador de objeto espacial proveniente de la GDB IDEAM.                                                                                                                                                                                   |
| CODIGO               | int64          | Código de la estación.                                                                                                                                                                                                                          |
| nombre               | object         | Nombre de la estación. Incluye el código de la estación entre corchetes.                                                                                                                                                                        |
| CATEGORIA            | object         | Categoría de la estación: Pluviométrica, Limnimétrica, Limnigráfica, Climática Ordinaria, Climática Principal, Pluviográfica, Meteorológica Especial, Agrometeorológica, Sinóptica Principal, Radio Sonda, Mareográfica, Sinóptica Secundaria.  |
| TECNOLOGIA           | object         | Tecnología para captura, registro y transmisión: Convencional, Automática con Telemetría, Automática sin Telemetría.                                                                                                                            |
| ESTADO               | object         | Estado de funcionamiento: Activa, Suspendida, En Mantenimiento.                                                                                                                                                                                 |
| FECHA_INSTALACION    | datetime64[ns] | Fecha de instalación.                                                                                                                                                                                                                           |
| altitud              | int64          | Altitud o cota sobre el nivel del mar en metros.                                                                                                                                                                                                |
| latitud              | float64        | Latitud en grados decimales.                                                                                                                                                                                                                    |
| longitud             | float64        | Longitud en grados decimales.                                                                                                                                                                                                                   |
| DEPARTAMENTO         | object         | Departamento o zonificación política. Equivalente a estados en otros países.                                                                                                                                                                    |
| MUNICIPIO            | object         | Municipio o subzonificación política. Equivalente a condado en otros países.                                                                                                                                                                    |
| AREA_OPERATIVA       | object         | Área operativa que administra la estación.                                                                                                                                                                                                      |
| AREA_HIDROGRAFICA    | object         | Área hidrográfica a la cual pertenece.                                                                                                                                                                                                          |
| ZONA_HIDROGRAFICA    | object         | Zona hidrográfica a la cual pertenece.                                                                                                                                                                                                          |
| observacion          | object         | Observaciones generales.                                                                                                                                                                                                                        |
| CORRIENTE            | object         | Corriente, cauce o río próximo o sobre la cuál está localizada la estación.                                                                                                                                                                     |
| FECHA_SUSPENSION     | datetime64[ns] | Fecha de suspensión.                                                                                                                                                                                                                            |
| SUBZONA_HIDROGRAFICA | object         | Subzona hidrográfica a la cual pertenece.                                                                                                                                                                                                       |
| ENTIDAD              | object         | Entidad encargada.                                                                                                                                                                                                                              |

> Los atributos presentados en la tabla, su tipo de escritura y notación han sido tomados del archivo original y no se encuentran normalizados a 11 caracteres para garantizar la compatibilidad con el formato .dbf. Se puede observar que los datos volcados en el archivo CNE_IDEAM.xls han sido generados utilizando la herramienta _Table to Table_ de ArcGIS desde una Geodatabase que permite la definición de atributos con más de 11 caracteres.


### Definiciones generales del catálogo nacional de estaciones

Tomado de [Anexo 2 - Definiciones CNE](http://www.ideam.gov.co/documents/10182/557765/Definiciones+CNE.pdf) del IDEAM.


#### Categorías de las estaciones

| Categoría                        | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Estación Agrometeorológica       | En esta estación se realizan observaciones meteorológicas y otras observaciones que ayudan a determinar las relaciones entre el clima, por una parte y la vida de las plantas y los animales por la otra. Incluye el mismo programa de observaciones de la estación climatológica principal, más registros de temperatura a varias profundidades (hasta un metro) y en la capa cercana al suelo (0, 10 y 20 cm sobre el suelo).                                                                                     |
| Estación Climatológica Ordinaria | Es aquella en la cual se hacen observaciones de precipitación, temperatura del aire, temperaturas máxima y mínima a 2 metros y humedad primordialmente. Poseen muy poco instrumental registrador. Algunas llevan instrumentos adicionales tales como tanque de evaporación, heliógrafo y anemómetro.                                                                                                                                                                                                                |
| Estación Climatológica Principal | Es aquella en la cual se hacen observaciones de precipitación, temperatura del aire, temperaturas máxima y mínima a 2 metros, humedad, viento, radiación, brillo solar, evaporación, temperaturas extremas del tanque de evaporación, cantidad de nubes y fenómenos especiales. Gran parte de estos parámetros se obtienen de instrumentos registradores.                                                                                                                                                           |
| Estación Limnigráfica            | Estación donde se mide el nivel de una corriente hídrica mediante un aparato registrador de nivel y que grafica una curva llamada limnigrama.                                                                                                                                                                                                                                                                                                                                                                       |
| Estación Limnimétrica            | Estación donde se mide el nivel de una corriente hídrica mediante un aparato (mira dividida en centímetros) que mide altura del agua, sin registrarla. Una persona toma el dato y lo registra en una libreta.                                                                                                                                                                                                                                                                                                       |
| Estación Mareográfica            | Estaciones para observación del estado del mar. Mide nivel, temperatura y salinidad de las aguas marinas.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Estación meteorológica especial  | Estación instalada para realizar seguimiento a un fenómeno o un fin específico, por ejemplo, las heladas.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Estación Pluviográfica           | Es aquella que registra en forma mecánica y continua la precipitación, en una gráfica que permite conocer la cantidad, duración, intensidad y periodo en que ha ocurrido la lluvia. Actualmente se utilizan los pluviógrafos de registro diario.                                                                                                                                                                                                                                                                    |
| Estación Pluviométrica           | Es una estación meteorológica dotada de un pluviómetro o recipiente que permite medir la cantidad de lluvia caída entre dos observaciones consecutivas.                                                                                                                                                                                                                                                                                                                                                             |
| Estación Radio Sonda             | La estación de radiosonda tiene por finalidad la medición directa de parámetros atmosféricos tales como temperatura del aire, presión atmosférica, humedad relativa y dirección y velocidad del viento en las capas altas de la atmósfera (tropósfera y baja estratósfera), mediante el rastreo, por medios electrónicos, de la trayectoria de un globo meteorológico que asciende libremente y que lleva un dispositivo con los sensores que miden y transmiten la señal con los datos.                            |
| Estación Sinóptica Principal     | En este tipo de estación se efectúan observaciones de los principales elementos meteorológicos en horas convenidas internacionalmente. Los datos se toman horariamente y corresponden a nubosidad, dirección y velocidad de los vientos, presión atmosférica, temperatura del aire, tipo y altura de las nubes, visibilidad, fenómenos especiales, características de humedad, precipitación, temperaturas extremas, capas significativas de nubes, recorrido del viento y secuencia de los fenómenos atmosféricos. |
| Estación Sinóptica Secundaria    | Al igual que en la estación anterior, las observaciones se realizan a horas convenidas internacionalmente y los datos corresponden comúnmente a visibilidad, fenómenos especiales, tiempo atmosférico, nubosidad, estado del suelo, precipitación, temperatura del aire, humedad del aire, presión y viento.                                                                                                                                                                                                        |

#### Estado de la estación

| Estado           | Descripción                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Activa           | Estación que se encuentra en operación y registra datos automáticos o tomados por un observador.                                                                                            |
| En mantenimiento | Estación que se encuentra en operación pero que temporalmente no registra datos automáticos o tomados por un observador por problemas en los equipos o como consecuencia de un siniestro.   |
| Suspendida       | Estación que se encuentra fuera de servicio de manera definitiva y no registra datos automáticos o tomados por un observador. Solo se puede consultar datos históricos en estas estaciones. |

####  Tecnología de la estación

| Estado                    | Descripción                                                                                                                                                                                                                                                                                                                                 |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Convencional              | Estación donde la toma del dato la efectúa un observador y la registra en una libreta para luego enviarla a los técnicos para que se capture y procesen estos datos.                                                                                                                                                                        |
| Automática con telemetría | Estación que obtiene los datos de manera automática mediante sensores de diferente tipo y que tiene la capacidad de enviarlos de manera automática al centro de recepción por diferentes medios de transmisión (satelital, radiofrecuencia, GPRS, etc.)                                                                                     |
| Automática sin telemetría | Estación que obtiene los datos de manera automática mediante sensores de diferente tipo y que tiene la capacidad de almacenarlos en un dispositivo dentro de la misma estación. No puede enviar los datos de manera automática. Los datos debes ser obtenidos por una persona que se conecta al sitio donde la estación almacena los datos. |

> De acuerdo a la nota del Anexo 2 del IDEAM: se debe tener en cuenta que la red es de tipo dinámico; es decir, a través de su operación se han instalado y suspendido estaciones a lo largo del territorio nacional, conservando en todo caso los datos históricos registrados. Esto significa que la sumatoria de las estaciones del Catálogo corresponde al número total de estaciones que han hecho parte de la red a través de su historia de operación y registro de información.


### Estructura de directorios

Para la ejecución correcta del script, es necesario clonar, descargar o crear la estructura de directorios definida en la siguiente tabla en el directorio `D:\R.GISPython\CNEStationStatistic`.

| Directorio                                                                                              | Descripción                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [/BasicTable](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/BasicTable)        | Directorio para volcado de tablas de estadísticos básicos y normalizados en formato de valores separados por comas [CSV](https://en.wikipedia.org/wiki/Comma-separated_values).                                                                                                                                                                                               |
| [/Data](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Data)                    | Directorio de descarga del archivo CNE_IDEAM.xls con registro de versiones.                                                                                                                                                                                                                                                                                                   |
| [/Graph](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Graph)                  | Directorio para volcado de gráficas en formato [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) (Portable Network Graphic) .png. Para cada ejecución se crea un nuevo grupo de imágenes con registro de versiones.                                                                                                                                              |
| [/Graph/PlotMap](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Graph/PlotMap)  | Directorio para volcado de gráficas por departamento en formato [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) (Portable Network Graphic) .png. Para cada ejecución se crea un nuevo grupo de imágenes con registro de versiones.                                                                                                                             |
| [/Old](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Old)                      | Directorio con versiones antiguas del script.                                                                                                                                                                                                                                                                                                                                 |
| [/PDF](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/PDF)                      | Directorio de impresión de la ventana de ejecución del script. Directamente no se realiza la escritura en un archivo .log de resultados por lo que su impresión se realiza de forma manual. En este directorio pueden existir versiones para clasificación de pisos térmicos con rangos convencionales o con los rangos definidos por Francisco José de Caldas en el año 1802. |
| [/PivotTable](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/PivotTable)        | Directorio para volcado de las tablas dinámicas producidas por el script en formato de valores separados por comas [CSV](https://en.wikipedia.org/wiki/Comma-separated_values).  Para cada ejecución se crea un nuevo grupo de archivos .csv con registro de versiones.                                                                                                       |
| [/Reference](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Reference)          | Documentos de referencias bibliográficas recopiladas.                                                                                                                                                                                                                                                                                                                         |
| [/Screenshot](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Screenshot)        | Capturas de pantalla de ejecución y configuración.                                                                                                                                                                                                                                                                                                                            |

> Para los archivos generados u obtenidos a través de la ejecución del script, se conserva el registro de versiones a partir de la fecha de ejecución utilizando el formato aaaammdd.


### Arreglos de datos para clasificación de estaciones por pisos térmicos


#### Cortes convencionales

| Valor de corte | Etiqueta                        |
|----------------|---------------------------------|
| 1000           | Cálido, 24°C+, <= 1000 meters   |
| 2000           | Templado, 18°C+, <= 2000 meters |
| 3000           | Frío, 12°C+, <= 3000 meters     |
| 4000           | Páramo, 0°C, <= 4000 meters     |
| 99999          | Glacial, 0°C-, > 4000 meters    |


#### Cortes Francisco José de Caldas, año 1802

| Valor de corte | Etiqueta                                    |
|----------------|---------------------------------------------|
| 800            | Cálido, T>=24°C, <=800meter                 |
| 1800           | Templado, 24°C>T>18°C, <=1800meter          |
| 2800           | Frío, 18°C>T>12°C, <=2800meter              |
| 3700           | Muy Frío, 12°C>T>6°C, <=3700meter           |
| 4700           | Extremadamente Frio, 6°C>T>0°C, <=4700meter |
| 99999          | Nival, T<0°C, >4700meter                    |


### Resumen general de datos analizados y publicados

Para cada ejecución del script principal, se analizan y publican en este repositorio diferentes [gráficas](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Graph), [tablas básicas](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/BasicTable) y [tablas dinámicas](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/PivotTable) que son ordenadas cronológicamente y a partir de las cuales se presenta el siguiente resumen general. 

| Fecha       | Activa | Suspendida | En Mantenimiento  |
|-------------|--------|------------|-------------------|
| 2021.12.13  | 2643   | 1832       | 17                |
| 2021.12.14  | 2643   | 1832       | 17                |
| 2021.12.15  | 2643   | 1832       | 17                |


### Ejecución en PyCharm usando Python 3.10.0

> PyCharm requiere de configuración previa del intérprete de Python a utilizar en la ejecución del script. Oprima `Ctrl+Alt+S` para acceder a la ventana de configuración y en la pestaña _Project: R.GISPython_ configurar los intérpretes disponibles en su equipo.

![PyCharm2021.3SetupPythonInterpreter.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/PyCharm2021.3SetupPythonInterpreter.png)

Ventana de ejecución con atributos obtenidos. 
![Python3.10.0StandalonePyCharm2021.3Attributes.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/Python3.10.0StandalonePyCharm2021.3Attributes.png)

Ventana de ejecución con atributos estadísticas generales. 
![Python3.10.0StandalonePyCharm2021.3GeneralStatistic.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/Python3.10.0StandalonePyCharm2021.3GeneralStatistic.png)

Ventana de ejecución con tablas dinámicas. 
![Python3.10.0StandalonePyCharm2021.3PivotTable.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/Python3.10.0StandalonePyCharm2021.3PivotTable.png)

Ventana de ejecución con clasificación por piso térmico. 
![Python3.10.0StandalonePyCharm2021.3ThermalLevel.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/Python3.10.0StandalonePyCharm2021.3ThermalLevel.png)


### Configuración para impresión de log de ejecución en PyCharm 2021.3

Configuración general de impresión.

![Pycharm2021.3RunSetupPrintSettings.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/Pycharm2021.3RunSetupPrintSettings.png)

Configuración de cabecera y pie de página.

![Pycharm2021.3RunSetupPrintHeaderFooter.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/Pycharm2021.3RunSetupPrintHeaderFooter.png)

Configuración avanzada.

![Pycharm2021.3RunSetupPrintAdvanced.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/Pycharm2021.3RunSetupPrintAdvanced.png)


### Ejemplo de gráficas obtenidas

![CategoryPivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/CategoryPivot20211214.png)
![GeoHydroAreaPivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/GeoHydroAreaPivot20211214.png)
![GeoHydroSubzonePivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/GeoHydroSubzonePivot20211214.png)
![GeoHydroZonePivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/GeoHydroZonePivot20211214.png)
![GeoOperativeAreaPivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/GeoOperativeAreaPivot20211214.png)
![GeoStatePivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/GeoStatePivot20211214.png)
![InstallationYearPivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/InstallationYearPivot20211214.png)
![TechnologyPivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/TechnologyPivot20211214.png)
![TechnologyPivotPie20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/TechnologyPivotPie20211214.png)
![ThermalLevelPivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/ThermalLevelPivot20211214.png)
![ThermalLevelPivotPie20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/ThermalLevelPivotPie20211214.png)
![StationScatterPlotMapCundinamarca20211215.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/PlotMap/StationScatterPlotMapCundinamarca20211215.png)
![CNEStationStatisticPlotMapDirectory.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/CNEStationStatisticPlotMapDirectory.png)


### Scripts

#### Script principal [CNEStationStatistic.py](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/CNEStationStatistic.py)

```
# -*- coding: UTF-8 -*-
# Name: CNEStationStatistic.py
# Description: Catálogo nacional de estaciones hidroclimatológicas del IDEAM - Colombia, descarga y análisis.
# Requirements: PyCharm 2021.3+, Python 3.10.0 (instalación independiente)

# Libraries
import pandas as pd # Tested with 1.3.4 version.
# import numpy as np # Tested with 1.21.4 version. # Has to be installed with not import required.
# import xlrd # Tested with 2.0.1 version. # Has to be installed with not import required.
from datetime import datetime
from datetime import date
import requests
import matplotlib.pyplot as plt
import os.path
import CNEStationDictionary # Import CNEStationDictionary.py
import matplotlib as mpl

# General variables
urlFile = 'http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls'
fileName = 'CNE_IDEAM'
fileExtension = '.xls'
sampleRecord = 12 # Number of records to show in the sample
showRecordSample = False  # Print some sample records
showAllRecords = False  # Print all the records at the report tail
showGraphScreen = False  # Show graphs on the screen. This script always update ./Graph & ./PivotTable
thermalLevelCaldas = True  # True for Caldas classification, False for conventional classification range
graphTransparency = 1 # Save color for paper print versions, 1 for full color. Doesn't apply for pie charts
stationName = 'nombre'
latitudeName = 'latitud'
longitudeName = 'longitud'
elevationName = 'altitud'
categoryName = 'CATEGORIA'
technologyName = 'TECNOLOGIA'
stateActiveName = 'ESTADO'
installationDate = 'FECHA_INSTALACION'
geoStateName = 'DEPARTAMENTO'
geoOperativeAreaName = 'AREA_OPERATIVA'
geoHydroAreaName = 'AREA_HIDROGRAFICA'
geoHydroZoneName = 'ZONA_HIDROGRAFICA'
geoHydroSubZoneName = 'SUBZONA_HIDROGRAFICA'
thermalLevelRefConv = [[1000,'Cálido, 24°C+, <= 1000 meters'],[2000,'Templado, 18°C+, <= 2000 meters'],[3000,'Frío, 12°C+, <= 3000 meters'],[4000,'Páramo, 0°C, <= 4000 meters'],[99999,'Glacial, 0°C-, > 4000 meters']] # Elevation value in meters
thermalLevelRefCaldas = [[800,'Cálido, T>=24°C, <=800meter'],[1800,'Templado, 24°C>T>18°C, <=1800meter'],[2800,'Frío, 18°C>T>12°C, <=2800meter'],[3700,'Muy Frío, 12°C>T>6°C, <=3700meter'],[4700,'Extremadamente Frio, 6°C>T>0°C, <=4700meter'],[99999,'Nival, T<0°C, >4700meter']] # Elevation value in meters
graphTitlePrefix='CNE IDEAM Colombia -  '
mySignature = 'By https://github.com/rcfdtools/R.GISPython' # Signature for print in graphs header
urlGraphPivotTable = 'https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic' # URL path for print in graphs

# General pandas and matplotlib settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 0)
mpl.rc('figure', max_open_warning = 0) # Don't show the python figure.max_open_warning

# Separation title line function
def SeparatorTitle(n=24): # Default using 24 - characters
    nc = '-'
    print(nc*n)

# Thermal level evaluation function
def thermalLevelF(elevation):
    for i in thermalLevelRef[:]:
        if elevation <= i[0]:
            return i[1]

# Downloading and reading the file
fileDownloadText = 'File downloaded and updated = No'
currentDate = date.today()
currentDateTxt=str(currentDate.year).zfill(4)+str(currentDate.month).zfill(2)+str(currentDate.day).zfill(2)
fileRequest = requests.get(urlFile)
fileSave = './Data/'+fileName+'_'+currentDateTxt+fileExtension
if fileRequest:
    if os.path.isfile(fileSave) == False:
        open(fileSave, 'wb').write(fileRequest.content)
        fileDownloadText = 'File downloaded and updated = Yes'
stationTable = pd.read_excel(fileSave)
pd.set_option('display.max_rows', stationTable.shape[0]+1) # Show all the records
pd.set_option('display.max_columns', None) # Show all the records

# Header and general file summary
shapeTable = stationTable.shape # Row and columns array size
SeparatorTitle(72)
print('Catálogo nacional de estaciones hidroclimatológicas del IDEAM - Colombia')
SeparatorTitle(72)
print(  '\nEjecutado en: '+str(datetime.now()),
        '\nData summary for '+fileSave,
        '\nUrl: '+urlFile,
        '\nStations file by: Instituto de Hidrología, Meteorología y Estudios Ambientales',
        '\nhttp://www.ideam.gov.co/web/atencion-y-participacion-ciudadana/condiciones-y-terminos-de-uso-de-la-informacion',
        '\nDataframe type: '+str(type(stationTable)),
        '\n'+fileDownloadText,
        '\nStations: '+ str(stationTable.shape[0])+'\nAttributes: '+ str(stationTable.shape[1]),
        '\nEncuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic'
        '\nCláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License'
        '\nCréditos: r.cfdtools@gmail.com\n')

# Sample records
if showRecordSample == True:
    SeparatorTitle(14)
    print('Sample records')
    SeparatorTitle(14)
    print('\nFirst '+str(sampleRecord)+' records: ')
    print(stationTable.head(sampleRecord)) # By default show 5 records
    print('Last '+str(sampleRecord)+' records: ')
    print(stationTable.tail(sampleRecord)) # By default show 5 records
    print('\n')

# Attributes summary
SeparatorTitle(27)
print('Attributes an types founded')
SeparatorTitle(27)
print(stationTable.columns)
print('\nTypes: ')
print(stationTable.dtypes) # With stationTable.columns you can get the attributes names in an array.
print('\nGeneral dataframe information: ')
print(stationTable.info())
print('\n')

# Basic dataframe statistics
SeparatorTitle(18)
print('General statistics')
SeparatorTitle(18)
print('\nBasic dataframe statistics: ')
print(stationTable.describe())
stationTable.describe().to_csv('./BasicTable/BasicDataframeStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/BasicDataframeStatistic'+currentDateTxt+'.csv')
print('\nCategory - Count: ')
print(stationTable[categoryName].value_counts())
stationTable[categoryName].value_counts().to_csv('./BasicTable/CategoryStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/CategoryStatistic'+currentDateTxt+'.csv')
print('\nCategory - Normalize percentage rate: ')
print(stationTable[categoryName].value_counts(normalize=True).round(4))
stationTable[categoryName].value_counts(normalize=True).to_csv('./BasicTable/CategoryStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/CategoryStatisticNormalize'+currentDateTxt+'.csv')
print('\nTechnology - Count: ')
print(stationTable[technologyName].value_counts())
stationTable[technologyName].value_counts().to_csv('./BasicTable/TechnologyStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/TechnologyStatistic'+currentDateTxt+'.csv')
print('\nTechnology - Normalize percentage rate: ')
print(stationTable[technologyName].value_counts(normalize=True).round(4))
stationTable[technologyName].value_counts(normalize=True).to_csv('./BasicTable/TechnologyStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/TechnologyStatisticNormalize'+currentDateTxt+'.csv')
print('\nStatus - Count: ')
print(stationTable[stateActiveName].value_counts())
stationTable[stateActiveName].value_counts().to_csv('./BasicTable/StatusStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/StatusStatistic'+currentDateTxt+'.csv')
print('\nStatus - Normalize percentage rate: ')
print(stationTable[stateActiveName].value_counts(normalize=True).round(4))
stationTable[stateActiveName].value_counts(normalize=True).to_csv('./BasicTable/StatusStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/StatusStatisticNormalize'+currentDateTxt+'.csv')
print('\nGeographical state location- Count: ')
print(stationTable[geoStateName].value_counts())
stationTable[geoStateName].value_counts().to_csv('./BasicTable/GeoStateStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoStateStatistic'+currentDateTxt+'.csv')
print('\nGeographical state location - Normalize percentage rate: ')
print(stationTable[geoStateName].value_counts(normalize=True).round(4))
stationTable[geoStateName].value_counts(normalize=True).to_csv('./BasicTable/GeoStateStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoStateStatisticNormalize'+currentDateTxt+'.csv')
print('\nGeographical operative area - Count: ')
print(stationTable[geoOperativeAreaName].value_counts())
stationTable[geoOperativeAreaName].value_counts().to_csv('./BasicTable/GeoOperativeAreaStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoOperativeAreaStatistic'+currentDateTxt+'.csv')
print('\nGeographical operative area - Normalize percentage rate: ')
print(stationTable[geoOperativeAreaName].value_counts(normalize=True).round(4))
stationTable[geoOperativeAreaName].value_counts(normalize=True).to_csv('./BasicTable/GeoOperativeAreaStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoOperativeAreaStatisticNormalize'+currentDateTxt+'.csv')
print('\nHydrographic area - Count: ')
print(stationTable[geoHydroAreaName].value_counts())
stationTable[geoHydroAreaName].value_counts().to_csv('./BasicTable/GeoHydroAreaStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoHydroAreaStatistic'+currentDateTxt+'.csv')
print('\nHydrographic area - Normalize percentage rate: ')
print(stationTable[geoHydroAreaName].value_counts(normalize=True).round(4))
stationTable[geoHydroAreaName].value_counts(normalize=True).to_csv('./BasicTable/GeoHydroAreaStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoHydroAreaStatisticNormalize'+currentDateTxt+'.csv')
print('\nHydrographic zone - Count: ')
print(stationTable[geoHydroZoneName].value_counts())
stationTable[geoHydroZoneName].value_counts().to_csv('./BasicTable/GeoHydroZoneStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoHydroZoneStatistic'+currentDateTxt+'.csv')
print('\nHydrographic zone - Normalize percentage rate: ')
print(stationTable[geoHydroZoneName].value_counts(normalize=True).round(4))
stationTable[geoHydroZoneName].value_counts(normalize=True).to_csv('./BasicTable/GeoHydroZoneStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoHydroZoneStatisticNormalize'+currentDateTxt+'.csv')
print('\nHydrographic subzone - Count: ')
print(stationTable[geoHydroSubZoneName].value_counts())
stationTable[geoHydroSubZoneName].value_counts().to_csv('./BasicTable/GeoHydroSubZoneStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoHydroSubZoneStatistic'+currentDateTxt+'.csv')
print('\nHydrographic subzone - Normalize percentage rate: ')
print(stationTable[geoHydroSubZoneName].value_counts(normalize=True).round(4))
stationTable[geoHydroSubZoneName].value_counts(normalize=True).to_csv('./BasicTable/GeoHydroSubZoneStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/GeoHydroSubZoneStatisticNormalize'+currentDateTxt+'.csv')
print('\nInstallation year - Count: ')
stationTable.sort_values(installationDate, ascending=True, inplace=True) # Reorder and uptate the dataframe by installation date records
stationTableYearCount = pd.DatetimeIndex(stationTable[installationDate]).year.value_counts(sort=False).round(0)
print(pd.DatetimeIndex(stationTable[installationDate]).year.value_counts(sort=False).round(0))
pd.DatetimeIndex(stationTable[installationDate]).year.value_counts(sort=False).to_csv('./BasicTable/InstallationYearStatistic'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/InstallationYearStatistic'+currentDateTxt+'.csv')
print('\nInstallation year - Normalize percentage rate: ')
print(pd.DatetimeIndex(stationTable[installationDate]).year.value_counts(sort=False, normalize=True).round(6))
pd.DatetimeIndex(stationTable[installationDate]).year.value_counts(sort=False, normalize=True).to_csv('./BasicTable/InstallationYearStatisticNormalize'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/BasicTable/InstallationYearStatisticNormalize'+currentDateTxt+'.csv')
print('\n')

# Pivot tables
SeparatorTitle(23)
print('Pivot tables and graphs')
SeparatorTitle(23)
print('\n')
# Category
pivotTable=stationTable.pivot_table(index=categoryName, columns=stateActiveName, values=technologyName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='barh', xlabel='Category', ylabel='Stations', title=graphTitlePrefix+'Stations by Category - Date:  '+str(currentDate)+'\n'+mySignature, figsize=(16,10), alpha=graphTransparency, rot=0, stacked=True) # alpha for transparency
plt.savefig('./Graph/CategoryPivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/CategoryPivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/CategoryPivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/CategoryPivot'+currentDateTxt+'.csv')
print('\n')
# Technology
pivotTable=stationTable.pivot_table(index=technologyName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Technology', ylabel='Stations', title=graphTitlePrefix+'Stations by Technology - Date: '+str(currentDate)+'\n'+mySignature, figsize=(8,8), fontsize=11, alpha=graphTransparency, rot=0, stacked=True )
plt.savefig('./Graph/TechnologyPivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/TechnologyPivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.plot(kind='pie', title=graphTitlePrefix+'Stations by Technology - Date: '+str(currentDate)+'\n'+mySignature, figsize=(24,8), startangle=30, subplots=True, autopct='%1.1f%%', fontsize=12, legend=False)
plt.savefig('./Graph/TechnologyPivotPie'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/TechnologyPivotPie'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/TechnologyPivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/TechnologyPivot'+currentDateTxt+'.csv')
print('\n')
# Geographical state
pivotTable=stationTable.pivot_table(index=geoStateName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Geographical state', ylabel='Stations', title=graphTitlePrefix+'Stations by Geographical State - Date: '+str(currentDate)+'\n'+mySignature, figsize=(14,18), alpha=graphTransparency, rot=-90, stacked=True)
plt.savefig('./Graph/GeoStatePivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/GeoStatePivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/GeoStatePivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/GeoStatePivot'+currentDateTxt+'.csv')
print('\n')
# Geographical operative area
pivotTable=stationTable.pivot_table(index=geoOperativeAreaName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Geographical operative area', ylabel='Stations', title=graphTitlePrefix+'Stations by Geographical Operative Area - Date: '+str(currentDate)+'\n'+mySignature, figsize=(10,16), alpha=graphTransparency, rot=-90, stacked=True)
plt.savefig('./Graph/GeoOperativeAreaPivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/GeoOperativeAreaPivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/GeoOperativeAreaPivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/GeoOperativeAreaPivot'+currentDateTxt+'.csv')
print('\n')
# Geographical hydrological area
pivotTable=stationTable.pivot_table(index=geoHydroAreaName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Geographical hydrological area', ylabel='Stations', title=graphTitlePrefix+'Stations by Geographical Hydrological Area - Date: '+str(currentDate)+'\n'+mySignature, figsize=(12,10), alpha=graphTransparency, rot=0, stacked=True, subplots=True, fontsize=11, grid=False, legend=False)
plt.savefig('./Graph/GeoHydroAreaPivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/GeoHydroAreaPivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/GeoHydroAreaPivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/GeoHydroAreaPivot'+currentDateTxt+'.csv')
print('\n')
# Geographical hydrological zone
pivotTable=stationTable.pivot_table(index=geoHydroZoneName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Geographical hydrological zone', ylabel='Stations', title=graphTitlePrefix+'Stations by Geographical Hydrological Zone - Date: '+str(currentDate)+'\n'+mySignature, figsize=(12,12), alpha=graphTransparency, rot=-90, stacked=True, fontsize=10)
plt.savefig('./Graph/GeoHydroZonePivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/GeoHydroZonePivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/GeoHydroZonePivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/GeoHydroZonePivot'+currentDateTxt+'.csv')
print('\n')
# Geographical hydrological subzone
pivotTable=stationTable.pivot_table(index=geoHydroSubZoneName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Geographical hydrological subzone', ylabel='Stations', title=graphTitlePrefix+'Stations by Geographical Hydrological Subzone - Date: '+str(currentDate)+'\n'+mySignature, figsize=(44,20), alpha=graphTransparency, rot=-90, stacked=True)
plt.savefig('./Graph/GeoHydroSubzonePivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/GeoHydroSubzonePivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/GeoHydroSubzonePivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/GeoHydroSubzonePivot'+currentDateTxt+'.csv')
print('\n')
# Installed stations by year
pivotTable = stationTable.pivot_table(index=pd.DatetimeIndex(stationTable[installationDate]).year, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Year', ylabel='Stations', title=graphTitlePrefix+'Installed Stations by year - Date: '+str(currentDate)+'\n'+mySignature, figsize=(22,12), alpha=graphTransparency, rot=-90, stacked=True)
plt.savefig('./Graph/InstallationYearPivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/InstallationYearPivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/InstallationYearPivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/InstallationYearPivot'+currentDateTxt+'.csv')
print('\n')

# Geospatial array
geoArray=stationTable[[latitudeName,longitudeName,elevationName]]
SeparatorTitle(39)
print('Geospatial array sample with '+str(sampleRecord)+' records')
SeparatorTitle(39)
print(geoArray.head(sampleRecord))
print('Dataframe type: '+str(type(geoArray))+'\n')

# Thermal level evaluation
if thermalLevelCaldas == True:
    thermalLevelRef = thermalLevelRefCaldas
    thermalLevelRefTitle = "Caldas classification"
    SeparatorTitleVal = 48
else:
    thermalLevelRef = thermalLevelRefConv
    thermalLevelRefTitle = "Conventional classification"
    SeparatorTitleVal = 54
SeparatorTitle(SeparatorTitleVal)
print('Thermal level evaluation - '+thermalLevelRefTitle)
SeparatorTitle(SeparatorTitleVal)
print('\nThermal level reference array:')
print(pd.DataFrame(thermalLevelRef,columns=['Elevation ref value','Thermic level']))
print('\n')
thermalLevelArray = []
for i in geoArray[elevationName]:
    thermalLevelArray.append(thermalLevelF(i))
stationTable['ThermalLevelValue']=thermalLevelArray
print('Geospatial array sample with '+str(sampleRecord)+' records:')
geoArray=stationTable[[geoStateName, stationName,latitudeName,longitudeName,elevationName,'ThermalLevelValue']]
print(geoArray.head(sampleRecord))
print('\nThermal level statistics:')
print('Count:')
print(geoArray['ThermalLevelValue'].value_counts())
print('\nNormalize percentage rate:')
print(geoArray['ThermalLevelValue'].value_counts(normalize=True).round(4))
print('\n')
pivotTable = stationTable.pivot_table(index='ThermalLevelValue', columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Thermal level', ylabel='Stations', title=graphTitlePrefix+'Stations by Thermal Level - Date: '+str(currentDate)+'\n'+mySignature, figsize=(12,12), fontsize=11, rot=10, stacked=True, alpha=graphTransparency)
plt.savefig('./Graph/ThermalLevelPivot'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/ThermalLevelPivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.plot(kind='pie', title=graphTitlePrefix+'Stations by Thermal Level - Date: '+str(currentDate)+'\n'+mySignature, figsize=(36,8), startangle=60, subplots=True, autopct='%1.1f%%', fontsize=12, legend=False)
plt.savefig('./Graph/ThermalLevelPivotPie'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/ThermalLevelPivotPie'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/ThermalLevelPivot'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/ThermalLevelPivot'+currentDateTxt+'.csv')
print('\n')

# General scatter plot map stations
SeparatorTitle(24)
print('General map plot station')
SeparatorTitle(24)
pivotTable=geoArray.plot.scatter(x=longitudeName, y=latitudeName, c=elevationName, colormap='viridis', colorbar=True, title=graphTitlePrefix+'Stations scatter plot map with altitude - Date: '+str(currentDate)+'\n'+mySignature, figsize=(10,11), grid=True, alpha=graphTransparency)
if showGraphScreen == True: plt.show()
plt.savefig('./Graph/StationScatterPlotMap'+currentDateTxt+'.png')
print('Graph >> '+urlGraphPivotTable+'/Graph/StationScatterPlotMap'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
geoArray.to_csv('./PivotTable/StationScatterPlotMap'+currentDateTxt+'.csv')
print('Table >> '+urlGraphPivotTable+'/PivotTable/StationScatterPlotMap'+currentDateTxt+'.csv')
# Geo State scatter plot map stations
geoStateList = stationTable[geoStateName].unique()
for i in geoStateList:
    #print(i)
    geoArrayState = geoArray[geoStateName].str.contains(i)
    #print(geoArray[geoArrayState])
    pivotTable=geoArray[geoArrayState].plot.scatter(x=longitudeName, y=latitudeName, c=elevationName, colormap='viridis', colorbar=True, title=graphTitlePrefix+'Stations scatter plot map with altitude - Date: '+str(currentDate)+'\n'+mySignature+'\n'+i, figsize=(10,11), grid=True, alpha=graphTransparency)
    if showGraphScreen == True: plt.show()
    plt.savefig('./Graph/PlotMap/StationScatterPlotMap' + i + currentDateTxt + '.png')
    print('Graph >> ' + urlGraphPivotTable + '/Graph/PlotMap/StationScatterPlotMap' + i + currentDateTxt + '.png')

# Show all data
if showAllRecords == True:
    SeparatorTitle(41)
    print('Stations in '+fileSave)
    SeparatorTitle(41)
    print('Index: ' + str(stationTable.index))
    pd.set_option('display.max_rows',stationTable.shape[0]+1)
    print(geoArray[[stationName,latitudeName,longitudeName]])
print('\n')

# General definitions
SeparatorTitle(8)
print('Appendix')
SeparatorTitle(8)
print('\nSource: IDEAM Colombia - Clasificación de los climas\nhttp://atlas.ideam.gov.co/basefiles/clima-text.pdf')
print('\n[Station categories]\n')
for i in CNEStationDictionary.stationCategoryDictEs:
    print(i[0]+': '+i[1]+'\n')
print('\n[Station status]\n')
for i in CNEStationDictionary.stationStatusDictEs:
    print(i[0]+': '+i[1]+'\n')
print('\n[Station technologies]\n')
for i in CNEStationDictionary.stationTechnologyDictEs:
    print(i[0]+': '+i[1]+'\n')
```

#### Script diccionario [CNEStationDictionary.py](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/CNEStationDictionary.py)

```
# -*- coding: UTF-8 -*-
# Name: CNEStationDictionary.py
# Description: Catálogo nacional de estaciones hidroclimatológicas del IDEAM - Colombia - Diccionario.
# Requirements: PyCharm 2021.3+, Python 3.10.0 (instalación independiente)
# Source: IDEAM Colombia - Clasificación de los climas (clima-text.pdf), http://atlas.ideam.gov.co/basefiles/clima-text.pdf
# Es: Español, En: English

stationCategoryDictEs = [
                    ['Estación Agrometeorológica','En esta estación se realizan observaciones meteorológicas y otras observaciones que ayudan a determinar las relaciones entre el clima, por una parte y la vida de las plantas y los animales por la otra. Incluye el mismo programa de observaciones de la estación climatológica principal, más registros de temperatura a varias profundidades (hasta un metro) y en la capa cercana al suelo (0, 10 y 20 cm sobre el suelo).'],
                    ['Estación Climatológica Ordinaria','Es aquella en la cual se hacen observaciones de precipitación, temperatura del aire, temperaturas máxima y mínima a 2 metros y humedad primordialmente. Poseen muy poco instrumental registrador. Algunas llevan instrumentos adicionales tales como tanque de evaporación, heliógrafo y anemómetro.'],
                    ['Estación Climatológica Principal','Es aquella en la cual se hacen observaciones de precipitación, temperatura del aire, temperaturas máxima y mínima a 2 metros, humedad, viento, radiación, brillo solar, evaporación, temperaturas extremas del tanque de evaporación, cantidad de nubes y fenómenos especiales. Gran parte de estos parámetros se obtienen de instrumentos registradores.'],
                    ['Estación Limnigráfica','Estación donde se mide el nivel de una corriente hídrica mediante un aparato registrador de nivel y que grafica una curva llamada limnigrama.'],
                    ['Estación Limnimétrica','Estación donde se mide el nivel de una corriente hídrica mediante un aparato (mira dividida en centímetros) que mide altura del agua, sin registrarla. Una persona toma el dato y lo registra en una libreta.'],
                    ['Estación Mareográfica','Estaciones para observación del estado del mar. Mide nivel, temperatura y salinidad de las aguas marinas.'],
                    ['Estación meteorológica especial','Estación instalada para realizar seguimiento a un fenómeno o un fin específico, por ejemplo, las heladas.'],
                    ['Estación Pluviográfica','Es aquella que registra en forma mecánica y continua la precipitación, en una gráfica que permite conocer la cantidad, duración, intensidad y periodo en que ha ocurrido la lluvia. Actualmente se utilizan los pluviógrafos de registro diario.'],
                    ['Estación Pluviométrica','Es una estación meteorológica dotada de un pluviómetro o recipiente que permite medir la cantidad de lluvia caída entre dos observaciones consecutivas.'],
                    ['Estación Radio Sonda','La estación de radiosonda tiene por finalidad la medición directa de parámetros atmosféricos tales como temperatura del aire, presión atmosférica, humedad relativa y dirección y velocidad del viento en las capas altas de la atmósfera (tropósfera y baja estratósfera), mediante el rastreo, por medios electrónicos, de la trayectoria de un globo meteorológico que asciende libremente y que lleva un dispositivo con los sensores que miden y transmiten la señal con los datos.'],
                    ['Estación Sinóptica Principal','En este tipo de estación se efectúan observaciones de los principales elementos meteorológicos en horas convenidas internacionalmente. Los datos se toman horariamente y corresponden a nubosidad, dirección y velocidad de los vientos, presión atmosférica, temperatura del aire, tipo y altura de las nubes, visibilidad, fenómenos especiales, características de humedad, precipitación, temperaturas extremas, capas significativas de nubes, recorrido del viento y secuencia de los fenómenos atmosféricos.'],
                    ['Estación Sinóptica Secundaria','Al igual que en la estación anterior, las observaciones se realizan a horas convenidas internacionalmente y los datos corresponden comúnmente a visibilidad, fenómenos especiales, tiempo atmosférico, nubosidad, estado del suelo, precipitación, temperatura del aire, humedad del aire, presión y viento.']]

stationStatusDictEs = [
                    ['Activa','Estación que se encuentra en operación y registra datos automáticos o tomados por un observador.'],
                    ['En mantenimiento','Estación que se encuentra en operación pero que temporalmente no registra datos automáticos o tomados por un observador por problemas en los equipos o como consecuencia de un siniestro.'],
                    ['Suspendida','Estación que se encuentra fuera de servicio de manera definitiva y no registra datos automáticos o tomados por un observador. Solo se puede consultar datos históricos en estas estaciones.']]

stationTechnologyDictEs = [
                    ['Convencional','Estación donde la toma del dato la efectúa un observador y la registra en una libreta para luego enviarla a los técnicos para que se capture y procesen estos datos.'],
                    ['Automática con telemetría','Estación que obtiene los datos de manera automática mediante sensores de diferente tipo y que tiene la capacidad de enviarlos de manera automática al centro de recepción por diferentes medios de transmisión (satelital, radiofrecuencia, GPRS, etc.)'],
                    ['Automática sin telemetría','Estación que obtiene los datos de manera automática mediante sensores de diferente tipo y que tiene la capacidad de almacenarlos en un dispositivo dentro de la misma estación. No puede enviar los datos de manera automática. Los datos debes ser obtenidos por una persona que se conecta al sitio donde la estación almacena los datos.']]
```


### Referencias

* [Data Analysis with Python for Excel Users - Full Course](https://www.youtube.com/watch?v=WcDaZ67TVRo&t=84s)
* [Python program to print current year, month and day](https://www.geeksforgeeks.org/python-program-to-print-current-year-month-and-day/)
* [How to extract year from date in pandas](https://www.codegrepper.com/code-examples/python/how+to+extract+year+from+date+in+pandas)
* [How to display all rows from data frame using pandas](https://dev.to/chanduthedev/how-to-display-all-rows-from-data-frame-using-pandas-dha)
* [How to rotate x-axis tick labels in Pandas barplot](https://stackoverflow.com/questions/32244019/how-to-rotate-x-axis-tick-labels-in-pandas-barplot)
* [Pandas dataFrame plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot)
* [Pandas dataframe plot bar](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html)
* [Pandas DataFrame Plot - Pie Chart](https://kontext.tech/column/code-snippets/402/pandas-dataframe-plot-pie-chart)
* [Make Better Bar Charts in Python using Pandas Plot](https://www.shanelynn.ie/bar-plots-in-python-using-pandas-dataframes/)
* [Annotate bars with values on Pandas bar plots](https://stackoverflow.com/questions/25447700/annotate-bars-with-values-on-pandas-bar-plots)
* [Pandas pie plot actual values for multiple graphs](https://stackoverflow.com/questions/48299254/pandas-pie-plot-actual-values-for-multiple-graphs)
* [How to print an entire Pandas DataFrame in Python?](https://www.geeksforgeeks.org/how-to-print-an-entire-pandas-dataframe-in-python/)
* [How to filter rows containing a string pattern from a Pandas dataframe](https://stackoverflow.com/questions/27975069/how-to-filter-rows-containing-a-string-pattern-from-a-pandas-dataframe)
* [Pandas: How to Find Unique Values in a Column](https://www.statology.org/pandas-unique-values-in-column/)
* [matplotlib get rid of max_open_warning output](https://stackoverflow.com/questions/27476642/matplotlib-get-rid-of-max-open-warning-output)
* [IDEAM Colombia - Clasificación de los climas (clima-text.pdf)](http://atlas.ideam.gov.co/basefiles/clima-text.pdf)
* [IDEAM Colombia - Clasificación climática de Caldas](http://www.ideam.gov.co/documents/10182/599272/Clasificacion+Climatica+de+Caldas+2014.pdf/d4ffa383-e60b-4ec5-8aa2-1b553d23b44f?version=1.0)
* [Pisos térmicos en Costa Rica](https://www.mep.go.cr/sites/default/files/recursos/recursos-interactivos/clima_tiempo/pdf/pisos_termicos.pdf)


### Compatibilidad

* Compatible con Python 3, librerías requeridas indicadas en la cabecera del archivo .py. 


### Control de versiones

| Versión    | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Autor                                     | Horas |
|------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|:-----:|
| 2021.12.16 | Documentación general.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | [rcfdtools](https://github.com/rcfdtools) |   8   |
| 2021.12.15 | Impresión de hiperenlaces en ventana de ejecución para cada gráfica y tabla dinámica generada. Generación de tablas con estadísticos básicos y normalizados en carpeta [/BasicTable](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/BasicTable). Creación de [diccionario](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/CNEStationDictionary.py) general con impresión en consola. Gráfica de localización de estaciones por departamento en [/Graph/PlotMap](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Graph/PlotMap) | [rcfdtools](https://github.com/rcfdtools) |   8   |
| 2021.12.14 | Incorporación de [gráficas](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Graph) y [tablas dinámicas](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/PivotTable), inclusión de clasificación Caldas.                                                                                                                                                                                                                                                                                                                                                 | [rcfdtools](https://github.com/rcfdtools) |   8   |
| 2021.12.13 | Versión inicial con estadísticos básicos y clasificación de pisos térmicos.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | [rcfdtools](https://github.com/rcfdtools) |   8   |


### Licencia, cláusulas y condiciones de uso

_R.GISPython es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio dando [clic aquí](https://github.com/rcfdtools/R.GISPython/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](https://github.com/rcfdtools/R.GISPython/tree/main/PandasBasic)     | [:house: Inicio](https://github.com/rcfdtools/R.GISPython/wiki) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.GISPython/discussions/13) | [Siguiente](https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather) |
|------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|

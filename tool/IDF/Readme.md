<div align="center"><img alt="R.HydroTools" src="file/graph/R.HydroStormMarkerIDF_v1.png" width="800px"></div>

# Herramienta para marcación, análisis de tormentas y construcción de curvas IDF a partir de eventos de precipitación obtenidos de pluviografos.

En hidrología, el estudio de la precipitación a partir de datos de tormentas registrados en estaciones de precipitación, permite analizar su comportamiento, duración, intensidad y patrón temporal.

R.HydroStormMarker, es una herramienta computacional que permite identificar y marcar los pulsos asociados a un mismo evento de lluvia, permitiendo conocer el valor total acumulado, duración e intensidad. Las tormentas identificadas pueden ser utilizadas para la construcción de curvas de Intesidad - Duración - Frecuencia ó IDF.

Los pulsos de precipitación pueden contener ceros intermedios en los cuales el sensor de captura no registra los cambios en la precipitación, razón por la cual la App permite incluir hasta 3 ceros consecutivos por cada evento.

* [:toolbox:R.HydroStormMarkerIDF.xlsm](file/table/R.HydroStormMarkerIDF.xlsm)


## 1. Conceptos


### 1.1. Obtención de curvas Intensidad, Duración, Período de retorno - IDF en estaciones pluviográficas
(Tomado del curso de Hidrología - GEAR)

![R.HydroStormMarker Screen9](file/graph/R.HydroStormMarkerIDF_Screen12.PNG)
![R.HydroStormMarkerIDF_IDFEcuacionGrafica](file/graph/R.HydroStormMarkerIDF_IDFEcuacionGrafica.PNG)

* Las curvas IDF son una síntesis de las lluvias intensas y de relativa corta duración, registradas en una estación específica.
* Para su construcción se utilizan en general precipitaciones de duraciones entre 5 minutos (cuando es posible), o menos, y 360 minutos como máximo.
* Las curvas IDF son de extrema utilidad en el cálculo o estimación de algunas variables en el proceso lluvia escorrentía.
* Su construcción solo puede realizarse con base en registros de estaciones pluviográficas, sin embargo, es posible obtener curvas IDF en estaciones pluviométricas utilizando algunos métodos indirectos o que involucran información de estaciones pluviográficas vecinas o regionales.


### 1.2. Consideraciones generales

* Si el pluviógrafo es diario, en general se pueden realizar lecturas para una duración mínima de 10 min, (lecturas hasta de 5 minutos pueden ser tomadas visualmente).
* Si el pluviógrafo es semanal, la lectura mínima corresponde a 1 hora, (lecturas de hasta 30 minutos pueden ser tomadas visualmente)
* Se deben conformar series anuales de precipitación máxima y para diferentes duraciones, p. ej. 5 min, 10 min, 15 min, 30 min, 45 min, 60 min, 120 min....
* Para la conformación final de la serie anual, se debe tomar 1 valor por año, que corresponde al máximo valor de precipitación registrada, en dicho año, para cada duración.
* Cuando los registros no son muy extensos se pueden conformar series parciales (n valores máximos en n años), pero el análisis varía ligeramente.
* De acuerdo con lo anterior, si en una estación pluviográfica se cuenta con, (p. ej.), 24 años de registros y si llueve en promedio en la zona 176 días al año, se deberían analizar las 24 x 176 = 4224 tormentas, tratando, de acuerdo con su duración total, de estimar la precipitación máxima caída en cada evento para cada una de las diferentes duraciones, es decir, 5 min, 10 min, 15 min, 30 min...., este proceso se conoce como "Clusterización".
* Esto es una labor larga y laboriosa. Entonces, más bien, frecuentemente y con un buen criterio, se pueden escoger algunos aguaceros por año (10 a 15 ), incluyendo, en lo posible, aquel de PMáx 24 horas y realizar (p. ej.) en este caso el proceso con los 10 x 24 = 240 aguaceros. Con la herramienta R.HydroStormMarkerIDF, es posible analizar solo los aguaceros seleccionados o usar todos los aguaceros presentes en la serie, obteniendo curvas IDF detalladas.
* Entonces, para cada duración y para cada año se tendría al final una serie de 10 a 15 valores, precipitaciones máximas para cada duración, de entre los cuales se escogería, para cada duración, la más grande de todas, con lo cual quedarían conformadas las series anuales (un valor, el máximo por año).
* Una vez obtenidas las series anuales de intensidades máximas para las diferentes duraciones, se ajustan a una Distribución de Valores Extremos (DVE), tipo Gumbel, Log-Pearson III o Log-Normal.
* Se realiza entonces un análisis de frecuencias y se obtiene, para cada duración, las intensidades esperadas para cada período de retorno deseado (2, 5, 10, 20 ó 25, 50, 100 años....).
* Con los valores obtenidos es posible dibujar las curvas IDF de trazos rectos.
* La familia de curvas obtenida tiene una ecuación del tipo: 
![Ecuacion Tipo IDF](file/graph/R.EcuacionTipoIDF.png)
* Cuyos coeficientes se pueden estimar por correlación lineal múltiple si se transforma de la siguiente manera:
![Correlacion Lineal Multiple](file/graph/R.CorrelacionLinealMultiple.png)


## 2. Procedimientos


### 2.0. Convenciones

| Convención  | Descripción                                                                                                                              |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [r]         | Hoja no editable.                                                                                                                        |
| [w]         | Hoja editable.                                                                                                                           |
| [rw]        | Hoja parcialmente editable.                                                                                                              |
| * *         | Asterisco en hoja MAIN indica que el dato es requerido. Estos datos son usados principalemente en los títulos dinámicos de las gráficas. |
| IDF         | Intensidad - Duración - Frecuencia.                                                                                                      |
| DMax        | Duración máxima encontrada en todas las tormentas analizadas.                                                                            |
| Índice      | Número entero consecutivo de 1 a n en función del pulso registrado y ordenado por año, mes, día y hora.                                  |
| min         | minuto.                                                                                                                                  |
| Mín         | Mínimo.                                                                                                                                  |
| Máx         | Máximo.                                                                                                                                  |
| Marca       | Marca de datos.                                                                                                                          |
| DVE         | Distribución de Valores Extremos.                                                                                                        |


### 2.1. Notas funcionales

* Nota 1: para el correcto funcionamiento de la aplicación, antes de pegar los datos en la App, asegúrese de indexar previamente los registros de 1 a n (Columna H de la hoja de Datos) ordenando los datos por fecha y hora. Desactive todos los filtros de datos antes de dar clic en *Ejecutar*.
* Nota 2: no se recomienda definir el número de ceros intermedios mayor a 1 si ejecutó previamente la función de eliminación de registros con ceros sucesivos, debido a que no se mantiene la continuidad de fechas y horas en los registros.
* Nota 3: para registros con frecuencia >= 30 minutos se recomienda utilizar solo 1 cero consecutivo.
* Nota 4: En la hoja "Datos", los valores ingresados en las columnas Año, Mes, Día, Dato e Índice, corresponden a valores numéricos. Para asegurarse de que copia y pega valores numéricos, puede utilizar en Microsoft Excel la opción de pegado especial solo de valores dando clic derecho en la celda B9. Opcionalmente, podrá pegar todos los datos en un editor de texto (p.e. Notepad++) y luego copiar desde el editor de texto todos los valores a partir de la misma celda B9.
* Nota 5: Para actualizar la ilustración de la Ecuación Característica obtenida de las curvas IDF, en algunos casos es necesario guardar, cerrar el archivo y volverlo abrir. Pruebe también oprimiendo Alt - F5.


### 2.2. Procedimientos externos preliminares

**1. Descarga de datos públicos (Proceso externo)**

* Identificar la Estación y descargar los datos pluviométricos o pluviográficos ya leídos
* Colombia: http://dhime.ideam.gov.co/atencionciudadano/
* Colombia: http://institucional.ideam.gov.co/jsp/loader.jsf?lServicio=Usuarios&lTipo=usuarios&lFuncion=login&
* USA: https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc:C00313
* USA: https://www.ncdc.noaa.gov/cdo-web/search?datasetid=PRECIP_HLY#

**2. Preprocesamiento externo**

* Ordenar los datos por fecha y hora, agregar índice consecutivo de 1 a n. 
* Segmentar los datos en las siguientes columnas de atributos: Año, Mes, Día, Hora (texto 4 dígitos), Dato, Marca, Índice.


### 2.3. Procedimientos en R.HydroStormMarker.IDF

**1. Procesamiento - Main**

* En la hoja _"Main"_ ingrese la información general de la estación. (Obligatorios: Código de la Estación, Latitud y Longitud)


**2. Procesamiento - Datos**

* Copiar y pegar los datos preprocesados en la hoja _"Datos"_ a partir de la celda B9. Los datos Año, Mes, Día, Dato, e Índice deben ser numéricos.

**3. Procesamiento - Calcular**

* En la hoja _"Datos"_, indique la Frecuencia en minutos, las Unidades (mm, ft), el número de Ceros intermedios y opcionalmente si requiere eliminar los ceros intermedios. De clic en el botón _"Calcular"_

**4. Análisis a partir de hojas disponibles:**

* Datos: Presenta el año de inicio y fin de la serie analizada, el # de registros procesados, el # de tormentas encontradas, la marcación de cada tormenta y sus valores acumulados.
* TormentaResumen: Presenta los pulsos por tormenta, duración, precipitación total e intensidad. (Permite filtar datos)
* TormentaResumenGrafico: Para cada tormenta, muestra el total de precipitación y su intensidad. Permite filtrar en las abscisas por rango de # de tormenta. (Editable)
* TormentaDuracionAnalisis, TormentaDuracionGrafico: Tabla y gráfica dinámica para análisis de duraciones por tormenta.  (Editable)
* Tormentas: Tabla Dinámica con tormentas identificadas y valores por pulso. (Editable)


## 3. Pruebas de Ejecución y Rendimiento

**_1. Resultados de ejecución limpiando registros con datos en cero (registros sin lluvia consecutiva) y procesando la serie sin análisis de clústers para construcción de curvas IDF_**

* Intel Core I5-8300H, 4 Cores, RAM 16gb: 100K registros en 9 minutos.
* AMD Ryzen 7 2700, 8 Cores 3.2GHz, RAM 32gb: 100K registros en 9 minutos.
* AMD Ryzen 7 2700, 8 Cores 3.2GHz, RAM 32gb: 500K registros en 84 minutos (12MB).

**_2. Resultados procesando la serie sin limpieza de registros en cero y sin análisis de clústers para construcción de curvas IDF_**

* AMD Ryzen 7 2700, 8 Cores 3.2GHz, RAM 32gb: 100K registros en 0.42 minutos, 406K registros en 1.47 minutos.


**_3. Resultados procesando la serie sin ceros intermedios y con análisis de clústers para construcción de curvas IDF_**

Este procedimiento es especialmente complejo debido a que es necesario procesar cada tormenta hasta la duración máxima encontrada para generar la matriz de máximos pulsos o valores por cada delta de frecuencia acumulada. Por ejemplo si la serie de datos es de 500k registros y la duración máxima encontrada en una de las tormentas es de 9.5 horas con pulsos cada 5 minutos, será necesario procesar 58 millones de clústers. Nota: Para simplificar este proceso puede optar primero por limpiar la serie de datos eliminando todos los ceros intermedios (registros sin lluvia consecutiva), sin embargo, _debe tener en cuenta que la linea de tiempo no se mantendrá consecutiva_ y deberá optar por no incluir ceros intermedios o utilizar máximo 1 en el procesamiento y análisis posterior de la serie. También puede optar por realizar el análisis año por año, ingresando en R.HydroStormMarker solo los registros del año a estudiar.

* AMD Ryzen 7 2700, 8 Cores 3.2GHz, RAM 32gb: 23K registros en 6.2 minutos (Archivo de 16MB con 3894 tormentas).


## 4. Funcionalidades agregadas por fecha de actualización

Código fuente: Microsoft Visual Basic para Aplicaciones VBA.
Probado en: **Microsoft Excel 2019**. Microsoft Windows 10 Pro 1903 (18362.449).

__**v.20191109**__

* Incluida correlación lineal múltiple y obtención de la ecuación IDF característica para la estación en estudio.
* Incluida tabla y gráfica IDF con valores calculados para diferentes periodos de retorno a partir de la ecuación característica.
* Optimización de algoritmo de cálculo hasta la duración máxima encontrada.

__**v.20191107**__

* Se incluyó nueva gráfica "DatoGraficoAcumulado" que muestra cada pulso por índice y los valores acumulados para cada tormenta identificada para cada duración acumulada.
* Se incluyó nueva hoja de datos "IDFValores" que contiene solo los datos de la IDF estimados para cada periodo de retorno. Esta hoja es requerida para la graficación de la IDF.
* Se incluyó nueva gráfica "IDFValoresGrafica" que muestra simultáneamente las curvas IDF para los 10 primeros periodos de retorno definidos en la hoja "Setup"
* Se incluyo nueva hoja de datos "IDFSerie" con las series de valores obtenidos para la construcción de la ecuación característica a partir de correlación múltiple

__**v.20191105**__

* Análisis de intensidades a partir de los Clústers de precipitación máxima para cada delta de tiempo.
* Definición de periodos de retorno en la hoja Setup.
* IDF - Estimación de precipitación para múltiples periodos de retorno y duraciones definidas por el usuario.

__**v.20191104**__

* El usuario puede definir ahora el tiempo en minutos para el análisis de IDF Clústers. En la versión anterior el análisis de clústers se realizaba de forma automática hasta la duración máxima encontrada. Ahora el analista puede decidir entre utilizar el valor de la máxima duración o realizar el análisis hasta una duración determinada (Generalmente a nivel de Colombia puede utilizar un valor entre 360 min a 540 min, dependiendo de la zona geográfica).

__**v.20191103**__

* Se incluyó hoja "IDFClusters" que resume los valores máximos por año encontrados para cada delta de duración. La opción IDF CLUSTER, realiza el análisis de los valores máximos por pulsos sucesivos de diferentes duraciones para encontrar los pulsos más intensos en cada evento de lluvia a utilizar en la construcción de curvas IDF. Atención: Para utilizar correctamente esta función es necesario eliminar primero los ceros intermedios de la serie. Una vez eliminados los ceros intermedios se recomienda establecer los Ceros Intermedios en cero para realizar el análisis de clústers de forma correcta, debido a que luego del proceso de eliminación de registros sucesivos en cero no se mantiene la continuidad de los eventos.
* Se identifican los registros de ceros consecutivos en la columna I de la hoja Datos. Estos registros pueden ser filtrados y eliminados de forma manual. El borrado manual es un procedimiento alterno más eficiente que el proceso interno automático de limpiado de registro y reordenamiento. Desde la hoja Datos, filtre los registros <> 1 identificados en la columna Cero Interm. (I)m copie y pegue los registros en Notepad++, desactive el filtro y elimine todos los registros de la hoja Datos, copie y pegue los registros desde el Notepad++.

__**v.20191102**__

* Se incluyó campo que índica la duración máxima encontrada. Este valor se calcula automáticamente y es requerido para el análisis de clusters para la construcción de curvas IDF.
* Se incluyó opción para procesamiento de clusters para la construcción de curvas IDF.
* Se optimizó el proceso de cálculo de la hoja "TormentaResumen"

__**v.20191101**__

* Se incluyó en la hoja de datos el secuenciamiento de frecuencias acumuladas por tormenta.
* Tabla dinámica "Tormentas" actualizada a partir de frecuencias acumuladas por tormenta.

__**v.20191031**__

* Mejoras de rendimiento.
* Menú con enlace a hojas de procesamiento y análisis.
* Datos DEMO de estación Colombiana con pulsos cada 10 minutos.

__**v.20191030**__

* Se incorporó nueva gráfica de todos los datos ingresados a partir del Índice consecutivo y el valor o dato registrado. 
* En la hoja de Setup se incorporó un campo para rótulo personalizado a mostrar en gráficas.
* Gráficas generales son solo de lectura y dinámicas permiten realizar filtros o modificación de parámetros. Se pueden filtrar los datos a visualizar desde la hoja Datos y TormentaResumen.

**v.20191029**

* Hoja de Conceptos Generales y Diagrama de Flujo General.
* Mejoras de rendimiento.
* Se ha incluido en la hoja "DatosEjemplo" datos que pueden ser utilizados para realizar pruebas de funcionamiento.
* En la hoja "DatosEjemplo" se ha incluido un ejemplo de la formulación requerida para segmentar el campo de la fecha del registro de datos (Formato AAAA/mm/dd HH:MM:SS) a columnas independientes de año, mes, día y hora en formato de texto con relleno de ceros en 4 caracteres.

**v.20191028**

* Títulos principales y secundarios en gráficas son aignados automáticamente a partir de los datos generales registrados para la estación.
* Optimizado el algoritmo de eliminación de registros con ceros consecutivos, reduciendo el tamaño del archivo y simplificando el análisis posterior de los datos. Ejecutar este procedimiento no es obligatorio; sin embargo, se recomienda su utilización para reducir el tamaño del archivo y los tiempos de análisis.
* Tabla y gráfica dinámica para análisis de duraciones.
* Gráfica general con # de tormenta asignada, Precipitación Total e Intensidad.
* Link R (Celda A1) en las hojas del libro para volver a la hoja MAIN.
* Resúmen de tormentas encontradas y tiempo empleado en el procesamiento.


## 5. Solución de errores

**IDFClusterIntensidad no calculados completa o correctamente**

Este error se presenta cuando el usuario en la hoja "Datos" en la celda "DMáx User" (I5), define una duración en la que no existen al menos dos valores anuales en algún Delta de tiempo para estimar la precipitación utilizando la distribución de Gumbel. Para solucionar este error, disminuya el valor de la duración máxima a analizar. 


## 6. Ilustraciones

![R.HydroStormMarker Screen1](file/graph/R.HydroStormMarkerIDF_Screen1.PNG)
![R.HydroStormMarker Screen2](file/graph/R.HydroStormMarkerIDF_Screen2.PNG)
![R.HydroStormMarker Screen3](file/graph/R.HydroStormMarkerIDF_Screen3.PNG)
![R.HydroStormMarker Screen4](file/graph/R.HydroStormMarkerIDF_Screen4.PNG)
![R.HydroStormMarker Screen5](file/graph/R.HydroStormMarkerIDF_Screen5.PNG)
![R.HydroStormMarker Screen6](file/graph/R.HydroStormMarkerIDF_Screen6.PNG)
![R.HydroStormMarker Screen7](file/graph/R.HydroStormMarkerIDF_Screen7.PNG)
![R.HydroStormMarker Screen8](file/graph/R.HydroStormMarkerIDF_Screen8.PNG)
![R.HydroStormMarker Screen9](file/graph/R.HydroStormMarkerIDF_Screen9.PNG)
![R.HydroStormMarkerIDF_IDFEcuacionGrafica](file/graph/R.HydroStormMarkerIDF_IDFEcuacionGrafica.PNG)


## Referencias

* GEAR - Curso de Hidrología






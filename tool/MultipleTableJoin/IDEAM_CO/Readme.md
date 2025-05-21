## Instituto de Hidrología, Meteorología y Estudios Ambientales - Colombia, IDEAM-CO  

El IDEAM es una institución pública de apoyo técnico y científico al Sistema Nacional Ambiental, que genera conocimiento, produce información confiable, consistente y oportuna, sobre el estado y las dinámicas de los recursos naturales y del medio ambiente, que facilite la definición y ajustes de las políticas ambientales y la toma de decisiones por parte de los sectores público, privado y la ciudadanía en general.[^1]

| Información        | Descripción                                                  |
|:-------------------|:-------------------------------------------------------------|
| Entidad            | Instituto de Hidrología, Meteorología y Estudios Ambientales |
| Área o dependencia | Gestión de datos y red hidrometeorológica                    |
| Localización       | Bogotá D.C. - Colombia - Suramérica                          |
| Orden              | Entidad de orden nacional                                    |
| Sector             | Ambiente y Desarrollo Sostenible                             |


### Información de los datos y licencia de uso

| Elemento                       | Descripción             |
|:-------------------------------|:------------------------|
| Idioma                         | Español                 |
| Cobertura geográfica           | Nacional Colombia       |
| Frecuencia de actualización    | Depende del parámetro   |
| Licencia                       | Dominio público         |
| Enlace de la fuente o citación | http://www.ideam.gov.co |


De acuerdo a la información disponible en el portal www.datos.gov.co, los datos disponibles pueden ser libremente consumidos bajo las siguientes cláusulas:

1. Los datos a visualizar o descargar no han sido validados por el IDEAM.
2. Los datos dispuestos son datos crudos instantáneos provenientes de los sensores de las estaciones automáticas de la red propia y/o producto de convenios inter-administrativos con terceras entidades.
3. Los datos son puestos a disposición de la ciudadanía como mecanismo de transparencia y para proveer una herramienta de apoyo a la gestión del riesgo territorial y como datos abiertos en cumplimiento de la Ley 1712 de 2014 de Colombia.
4. Es posible que los datos dispuestos tengan cierto retraso en el tiempo debido a las frecuencias de envío de datos de los sensores y los medios de transmisión utilizados. 
5. Los datos presenten errores y/o inconsistencias estando incluso por fuera de los límites considerados normales, producto de fallas en los sensores de origen.
6. El posterior uso e interpretación que se le dé para cualquier finalidad queda bajo la exclusiva responsabilidad del portador de los datos.
7. Cualquier destino que se le dé a los datos exime al IDEAM de realizarles cualquier tipo de justificación o iniciarles proceso alguno de validación posterior, cuya fuente primaria deben ser los canales oficialmente dispuestos por la Entidad para el suministro de información oficial y validada.
8. Por las razones expuestas anteriormente los datos dispuestos no podrán ser utilizados como evidencia jurídica ante entes de control acerca de la ocurrencia o no de fenómenos hidro-climatológicos o de soporte a cualquier tipo de situación o evento ocurrido como consecuencia de estos.


### Fuentes de datos (actualizados mensualmente)

A través del portal de datos abiertos de Colombia - Suramérica www.datos.gov.co, se pueden obtener las colecciones de datos crudos o Datasets publicados por el IDEAM Colombia. En la siguiente tabla encontrará un listado de las principales variables disponibles:  

<div align="center">

| Parámetro                                                                                                                                       | Periodo    |
|:------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|
| [Temperatura](https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Datos-Hidrometeorol-gicos-Crudos-Red-de-Estaciones/sbwg-7ju4)           | Diaria     |
| [Precipitación](https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Precipitaci-n/s54a-sgyg)                                              |            |
| [Presión atmosférica](https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Presi-n-Atmosf-rica/62tk-nxj5)                                  | Horaria    |
| [Velocidad viento](https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Velocidad-Viento/sgfv-3yp8)                                        | 10 minutos |
| [Dirección del viento](https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Direcci-n-Viento/kiw7-v9ta)                                    | 10 minutos |
| [Humedad relativa del aire a 2 metros](https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Humedad-del-Aire-2-metros/uext-mhny)           | Horaria    |
| [Temperatura máxima del aire a 2 metros](https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Temperatura-M%C3%A1xima-del-Aire/ccvq-rp9s) |            |
| [Temperatura mínima del aire a 2 metros](https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Temperatura-M%C3%ADnima-del-Aire/afdg-3zpb)  |            |
| [Nivel máximo del río medido en una hora](https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Nivel-M%C3%A1ximo/vfth-yucv)                | Horario    |
| [Nivel mínimo río](https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Nivel-M%C3%ADnimo/pt9a-aamx)                                   |            |
| [Nivel medio del mar mínimo](https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Nivel-del-Mar-M%C3%ADnimo/7z6g-yx9q)                     |            |
| [Nivel medio del mar máximo](https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Nivel-del-Mar-M%C3%A1ximo/uxy3-jchf)                     |            |

</div>


### Catálogo de objetos

Atención: los datos obtenidos desde el portal www.datos.gov.co no utilizan la misma estructura de los datos obtenidos desde el portal http://dhime.ideam.gov.co/atencionciudadano/

Atributos tomados directamente de los archivos de texto separados por comas obtenidos y tipos descritos en el portal.

| Atributo         | API nombre        | Tipo         | Descripción                                                                                                                          |
|:------------------|:------------------|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| CodigoEstacion    | codigoestacion    | Texto simple | Al código del catálogo nacional de estaciones se le ha realizado un relleno de ceros a la izquierda para completar 10 dígitos        |
| CodigoSensor      | codigosensor      | Texto simple | Código con relleno de ceros a izquierda para completar 4 dígitos                                                                     |
| FechaObservacion  | fechaobservacion  | Fecha y hora | Fecha y hora de la observación. Hora en formato de 12 horas, requiere AM/PM                                                          |
| ValorObservado    | valorobservado    | Número       | Valor observado o registrado                                                                                                         |
| NombreEstacion    | nombreestacion    | Texto simple | Nombre de la estación, no incluye el código de la estación al final entre corchetes como en el catálogo nacional de estaciones - CNE |
| Departamento      | departamento      | Texto simple | Departamento de Colombia. Correspondiente al nivel de estado en otros países                                                         |
| Municipio         | municipio         | Texto simple | Municipio de Colombia. Correspondiente al nivel de condado en otros países                                                           |
| ZonaHidrografica  | zonahidrografica  | Texto simple | Zona hidrográfica nacional establecida por el IDEAM - Colombia                                                                       |
| Latitud           | latitud           | Número       | Latitud en grados decimales                                                                                                          |
| Longitud          | longitud          | Número       | Longitud en grados decimales                                                                                                         |
| DescripcionSensor | descripcionsensor | Texto simple | Descripción del sensor. Corresponde al parámetro específico registrado                                                               |
| UnidadMedida      | unidadmedida      | Texto simple       | Unidad de medida                                                                                                                     |

> Los nombres de atributo son desplegados en los archivos de texto separados por comas .CSV 

Registros ejemplo para presión atmosférica 
```
CodigoEstacion,CodigoSensor,FechaObservacion,ValorObservado,NombreEstacion,Departamento,Municipio,ZonaHidrografica,Latitud,Longitud,DescripcionSensor,UnidadMedida
0036015020,0255,10/03/2017 06:00:00 AM,992.5,EL DIAMANTE - AUT,CASANARE,PAZ DE ARIPORO,META,5.816194444,-71.41983333,Presión Atmosferica (1h),HPa
0021195190,0255,02/14/2014 05:00:00 AM,785.2,PASCA - AUT,CUNDINAMARCA,PASCA,ALTO MAGDALENA,4.310111111,-74.31175,Presión Atmosferica (1h),HPa
```


### Referencias

* http://ideam.gov.co/
* http://www.ideam.gov.co/solicitud-de-informacion
* http://dhime.ideam.gov.co/atencionciudadano/

[^1]: http://www.ideam.gov.co/web/entidad/acerca-entidad
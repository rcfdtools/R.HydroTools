<div align="center"><a href="https://github.com/rcfdtools" target="_blank"><img src="https://github.com/rcfdtools/rcfdtools/blob/main/graph/rcfdtools_banner.png" alt="R.LTWB" width="100%" border="0" /></a></div>

# TOOL - R.Weather CDMS - Climate Data Management System

R.Weather CDMS, es un sistema computacional que integra colecciones de datos y su representación espacial, facilitando el registro, manejo, análisis, distribución y utilización de datos hidroclimatológicos. 


### Cláusulas de autor

* Al descargar, descomprimir, instalar, usar o explorar esta herramienta, sus archivos y documentación, usted como empresa, individuo, estudiante, profesional, empleado o persona, acepta los siguientes términos de uso:

* r.cfdtools@gmail.com le concede una licencia de uso global, no exclusiva, de libre uso y revocable en cualquier momento, siempre y cuando sea única y exclusivamente para su uso personal o privado y no tenga como fin un uso comercial.

* Cláusula de exención de responsabilidad: r.cfdtools@gmail.com, No se responsabiliza de la aplicación y uso de los resultados obtenidos a través de sus modelos. Es responsabilidad de los usuarios; verificar, comparar, evaluar y analizar Si los scripts, algoritmos, funciones, objetos aplicados y los resultados obtenidos, cumplen con las metodologías y estándares de análisis aplicables en estadística e hidrología.

* Se permite la reproducción digital de los documentos electrónicos impresos, No se permite su reproducción impresa.

* Se acoge a todas las leyes de propiedad intelectual o de derechos de autor, bien sean locales, de su país de procedencia o globales internacionales. 

* No se permite la eliminación, alteración, modificación o cambio del logo de este aplicativo ni de su iconografía. Capturas de pantalla deben mostrar el logo de la aplicación, siempre y cuando se trate de formularios, reportes o gráficas.

* Los contenidos, materiales, datos producidos a partir de datos base, son de uso libre y estrictamente para uso académico; no publique o distribuya estos datos ni los archivos producidos, sin la autorización expresa del autor. Los datos utilizados para el desarrollo, implementación y realización de pruebas funcionales, fueron obtenidos de diferentes fuentes de información (por ejemplo, Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM, Drummond Ltd., National Oceanic and Atmosferic Administration - NOAA U.S. Department of Commerce, National Aeronautics and Space Administration, U.S.A. - NASA, Instituto Geográfico Agustín Codazzi - IGAC y otras fuentes). Se aclara que los datos o información registrada en este sistema, en su mayoría tiene el carácter de pública y puede ser objeto de modificación y/o actualización permanente; así mismo, la utilización, reproducción, modificación o distribución de los manuales, guías y datos, impone la obligación de reconocer la autoría de los mismos y citar la fuente de referencia. Tenga en cuenta que esta información puede contener imprecisiones debidas a la escala de digitalización y solo es utilizada para esquematizar los ejemplos presentados en este software. Para el desarrollo de trabajos de ingeniería utilizando este software, se requiere de una licencia comercial, además se recomienda consultar las distintas fuentes de datos citadas y verificar el estado de actualización, los derechos de uso y restricción de los mismos. Los datos base incluídos en este Software y provenientes de diferentes fuentes públicas se acogen a La Ley de Transparencia y Acceso a la Información Pública Nacional de Colombia (Ley 1712 de 2014), que establece procedimientos para garantizar el derecho de acceso a la información pública, y el Decreto de Gobierno en Línea (Incluido en el Decreto único Reglamentario del sector TIC - 1078 de 2015). Para los datos base que han sido incluídos como ejemplo en este softwate y provenientes del Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM, se debe citar la fuente original como "IDEAM". Recuerde que la propiedad intelectual e industrial de estos datos pertenece al IDEAM. 

* El autor no se hace responsable por el uso inadecuado de las herramientas computacionales que hacen parte de este software, ni del uso inadecuado de los algoritmos, memorias de cálculo y herramientas propias disponibles.

* Se permite la modificación y mejora de los manuales, libros de cálculo electrónicos, scripts y demás herramientas propias incluidas en este software, siempre y cuando se preserven las misma libertades de distribución y copia de las modificaciones realizadas. Al realizar modificaciones, se compromete y obliga a publicarlas y a notificar al autor original a través del correo electrónico r.cfdtools@gmail.com, quién podrá incorporarlas a la versión oficial para su posterior distribución.

* No se permite la privatización, acaparamiento, venta o distribución comercial de este software, ni ningúno de sus componentes, ni de las memorias de cálculo, de los scripts y demás herramientas complementarias que se encuentran en el paquete de datos de instalación.


## Citación

Se permite la reproducción parcial o total de este documento, el modelo de datos y las herramientas de este sistema, siempre que se haga referencia como: "R.Weather CDMS – Sistema de Administración y Análisis de Datos Climatológicos, Software y Manual de Usuario, r.cfdtools@gmail.com, Bogotá - Colombia - Suramérica. 2017".


## Instalación y configuración
	
* Ruta nativa absoluta en D:\R.Weather\
* Ruta nativa GIS absoluta en D:\R.WeatherGIS\
* Ejecución desde el acceso directo D:\R.Weather\R.Weather o desde D:\R.Weather\DB\R.Weather.accdb
* Sistema operativo Microsoft Windows [Testeado en versión 10.0.19043.1055]
		
* Software requerido
  * Microsoft® Access® para Microsoft 365 MSO (16.0.13901.20148 o superior) 32 o 64 bits. Instalado sobre unidad SSD.
  * ESRI ArcGIS for Desktop 10.2.2 en Inglés.

* Hardware
  * Monitor con resolución: 1920 x 1080p.
  * Memoria RAM: 16 GB.
  * Procesador: Intel Core i7 serie HQ, H, X, Z. Intel Xeon. (recomendados)
  * Unidades de almacenamiento: Unidad C mínimo 256GB m.2 SSD y unidad D mínimo 512GB SSD SATA o m.2. (recomendados)
  * Para una única unidad de almacenamiento de estado sólido se requieren de dos particiones o de la asignación de letra de unidad como D:\
  * Tarjeta de video externa: Aceleradora mínimo 2GB para representación de escenas 3D y renderizado de modelos de terreno en 2D.

* Configuración adicional requerida en Microsoft® Access® para Microsoft 365
  * Permitir el uso de macros: Ejecutar la aplicación y en el menú Archivo seleccionar Opciones de Access - Centros de Confianza - Configuración del Centro de Confianza - Configuración de Macros - Habilitar todas las macros.
  * Configuración de cliente: Ejecutar la aplicación y en el menú Archivo seleccionar Opciones de Access - Configuración de Cliente - Confirmar, desactivar las casillas Cambios en los registros y Consultas de Acción, dejar marcado Eliminaciones de Documento.
  * Fuente tipográfica: Segoe Ui Light. Esta fuente está incluida en el paquete de instalación de Microsoft Office 365.
	
* Notación numérica del sistema operativo: Separador decimal usando punto (.), separador de miles usando coma (m), separador de listas usado coma (,). COnfigurar desde el Panel de Control - Región - Formatos - Configuración Adicional - Números.


## Referencias

* https://wmo.int/climate-data-management-systems-cdmss
* https://old.wmo.int/extranet/pages/prog/wcp/wcdmp/CDM_3.php
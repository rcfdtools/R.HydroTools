## Definir la versión por defecto de Python en el OS y configurar PyCharm
Keywords: `PyCharm` `Python Interpreter` `Windows Environmental Variables` `os` 

Definir una versión por defecto de Python en el CMD de Microsoft Windows, le permitirá lanzar este intérprete de comandos desde cualquier directorio de su sistema operativo y sin tener que ingresar la ruta completa del ejecutable Python.exe. La configuración de intérpretes en PyCharm, le permitirá ejecutar scripts de un proyecto utilizando una versión predefinida de Python. 

![DefaultVersion.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/DefaultVersion.png)

### Objetivos

* Establecer una versión de Python como la versión por defecto del OS.
* Configurar él(los) intérprete(s) a usar en PyCharm para la ejecución de scripts.


### Requerimientos

* Python 2.7.5 de ArcGIS for Desktop 10.2.2.
* Python 3.10.0+ como instalación independiente o standalone.
* PyCharm 2021.3+ for Anaconda.
* ArcGIS Pro 2.9+.
* QGIS 3.22.1+.

> Nota: en caso de no disponer de ArcGIS en su equipo, puede realizar las pruebas de funcionamiento realizando la instalación independiente de la versión 2.7 de Python.

> Nota: para la instalación de versiones independientes de Python, p.ej, la versión 3.10.0, se recomienda modificar la ruta de instalación a una ruta de fácil acceso como _C:\Python310\_


### Versión por defecto en el sistema operativo

1. En Microsoft Windows oprimir `Windows+R` y ejecutar `sysdm.cpl` para ingresar a las propiedades avanzadas del sistema.

![WindowsOSRunSysdm.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/WindowsOSRunSysdm.png)

2. En la ventana dar clic en la pestaña _Opciones Avanzadas_ y luego en _Variables de Entorno_.

![WindowsOSSystemProperties.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/WindowsOSSystemProperties.png)

3. En _Variables del sistema_, seleccionar _Path_ y dar clic en _Editar_.

![WindowsOSEnvironmentVariables.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/WindowsOSEnvironmentVariables.png)

4. Para establecer la versión de Python integrada a ArcGIS (p.ej, Python 2.7.5 sobre ArcGIS 10.2.2 for Desktop), ingresar (utilizando la opción _Nuevo_) o verificar que existan las variables de entorno direccionandas a las rutas _C:\Python27\ArcGIS10.2\Scripts_ y _C:\Python27\ArcGIS10.2_.

![WindowsOSEnvironmentVariablesEdit.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/WindowsOSEnvironmentVariablesEdit.png)

> En caso de que su instalación de ArcGIS for Desktop corresponda a una versión diferente, identifique las rutas de instalación e ingrese o modifique las variables de entorno. Más información en https://github.com/rcfdtools/R.GISPython/tree/main/PythonVersion

> Luego de la modificación de las variables de entorno, en algunas versiones de su sistema operativo, será necesario reiniciar su equipo o cerrar y abrir su sesión de usuario.

5. Para verificar el direccionamiento correcto, abra una nueva ventana de comandos oprimiendo la combinación de teclas `Windows+R` y _CMD_ ó busque el _Command Prompt_ en su lista de programas (no es necesaria la ejecución como Administrador).

![WindowsCMD.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/WindowsCMD.png)

6. En el intérprete de comandos de Windows, ejecute el comando _Python_. Observará que la versión por defecto es la 2.7.5.

![WindowsCMDPythonVersion.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/WindowsCMDPythonVersion.png)


## Configuración de intérprete(s) de Python en PyCharm 

En PyCharm, él(los) intérprete(s) de comandos son asociados a cada proyecto. Para este ejemplo, asociaremos Python 2.7.5 de ArcGIS for Desktop, Python 3.10.0 standalone y las versiones integradas de Python en ArcGIS Pro 2.9 y QGIS 3.22.1.  

1. Descargue e instale PyCharm Community desde _https://www.jetbrains.com/pycharm/download/_

2. Abra PyCharm y desde el menú _File_, cree (_New Project_) o abra (_Open_) un proyecto existente, (p.ej, crear en la unidad D:\ la carpeta R.GISPython). Seleccione _Virtualenv_ para la creación del nuevo ambiente que utilizará el intérprete y el intérprete base que se utilizará por defecto (p.ej, Python 2.7 ArcGIS for Desktop 10.2.2).

![PyCharmCreateProject.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/PyCharmCreateProject.png)

> Los nombres de los intérpretes base pueden cambiar dependiendo de la versión de ArcGIS for Desktop instalada o de la versión independiente instalada de Python en su sistema. 

3. En el menú _File_, seleccione la opción _Settings_ u oprima la combinación de teclas `Ctrl+Alt+S` para acceder a las opciones de configuración de PyCharm.

![PyCharmSettings.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/PyCharmSettings.png)

4. En la ventana de configuración, seleccione la pestaña _Project: R.GISPython_ y la opción Python Interpreter, de clic en el ícono de configuración y seleccione la opción _Show All_. 

![PyCharmProjectPythonInterpreter.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/PyCharmProjectPythonInterpreter.png)

5. En la ventana _Project Interpreters_, de clic en la opción de agregar _+_  

![PyCharmProjectPythonInterpreterAdd.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/PyCharmProjectPythonInterpreterAdd.png)

6. En la ventana de agregar, seleccione la pestaña correspondiente a _System Interpreter_ y de clic en la opción de búsqueda de ruta _..._

![PyCharmProjectPythonInterpreterAddSystem.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/PyCharmProjectPythonInterpreterAddSystem.png)

7. Seleccione la ruta de instalación de la versión independiente de Python instalada en su sistema, p.ej, 3.10.0.

![PyCharmProjectPythonInterpreterAddSystemPath.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/PyCharmProjectPythonInterpreterAddSystemPath.png)

> Para modificar el nombre por defecto, p.ej, de _Python 3.10_ a _Python 3.10 Standalone_, de clic en la opción Editar (ícono lápiz) y cambie el nombre.

Desde este momento, podrá seleccionar el intérprete de Python que requiera su proyecto o para la ejecución de un script en particular.

![PyCharmProjectPythonInterpreterShowAll.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/PyCharmProjectPythonInterpreterShowAll.png)

Opcionalmente podrá asociar el intérprete de Python integrado a QGIS, p.ej, Python 3.9.5 sobre QGIS 3.22.1. La ruta de asociación es _C:\Program Files\QGIS 3.22.1\apps\Python39_

![PyCharmProjectPythonInterpreterAddQGIS3.22.1.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/PyCharmProjectPythonInterpreterAddQGIS3.22.1.png)

También podrá asociar el intérprete de Python 3.7.11 integrado a ArcGIS Pro 2.9. La ruta de asociación podrá ser consultada desde las opciones de configuración de ArcGIS Pro en la pestaña Python y está localizada en _C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3_

![ArcGISProPythonPackageManager.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/ArcGISProPythonPackageManager.png)

![PyCharmProjectPythonInterpreterAddArcGISPro2.9.png](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/PyCharmProjectPythonInterpreterAddArcGISPro2.9.png)


### Referencias

* https://epjmorris.wordpress.com/2020/09/16/configuring-pycharm-for-use-with-arcgis-pro-and-arcmap/


### Compatibilidad

* Compatible con cualquier versión de Python.


### Control de versiones

| Versión    | Descripción                                                                       | Autor                                     | Horas |
|------------|:----------------------------------------------------------------------------------|-------------------------------------------|:-----:|
| 2021.12.04 | Asociación de intérpretes de Python en PyCharm para QGIS 3.22.1 y ArcGIS Pro 2.9. | [rcfdtools](https://github.com/rcfdtools) |  1.5  |
| 2021.12.01 | Versión inicial.                                                                  | [rcfdtools](https://github.com/rcfdtools) |  4.5  |


### Licencia, cláusulas y condiciones de uso

_R.GISPython es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio dando [clic aquí](https://github.com/rcfdtools/R.GISPython/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](https://github.com/rcfdtools/R.GISPython/tree/main/PythonVersion) | [:house: Inicio](https://github.com/rcfdtools/R.GISPython/wiki) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.GISPython/discussions/3) | [Siguiente](https://github.com/rcfdtools/R.GISPython/tree/main/HelpModulesKeywords) |
|------------------------------------------------------------------------------|-----------------------------------------------------------------|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
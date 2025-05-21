## Instalación, actualización de paquetes y creación de gráficas básicas usando matplotlib
Keywords: `Concentration time` `Giandotti` `Subbasin` `Hydrology` `Interactive` `define` `while` `matplotlib` `.lower()` 

Complementariamente a las librerías obtenidas con la instalación de Python, es posible adicionar nuevas librerías que posteriormente podrán ser invocadas desde la consola o desde scripts y también se pueden actualizar las librerías preinstaladas. El procedimiento más común de instalación automatizada se realiza a través del comando de consola `pip` disponible en el directorio _Scripts_ de Python. 

![InstallPackageGraph.png](https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/InstallPackageGraph.png)

Para el ejemplo de estimación del tiempo de concentración, además de permitir la entrada de datos del usuario y calcular la variación del tiempo obtenido cambiando la pendiente desde un valor bajo (p.ej, 0.001 m/m) hasta la pendiente ingresada por el usuario y para un determinado número de variaciones (p.ej, 12), crearemos una gráfica que permita analizar visualmente la tendencia de los datos.

> Dentro de las versiones independientes o standalone de Python no se incorpora el paquete matplotlib, sin embargo, puede ser instalada manualmente o desde PyCharm.


### Objetivos

* Instalar el paquete o librería matplotlib y actualizar paquetes preinstalados en Python.
* En PyCharm, ejecutar el script usando la versión de Python 2.7 y 3.10.
* Ejecutar el script desde la consola del sistema operativo o CMD.
* Graficar diferentes tiempos de concentración - Tc, variando la pendiente.

> Atención: no es recomendable actualizar las librerías preinstaladas de Python para ArcGIS, lo anterior debido a que son utilizadas por todo el entorno del paquete y su modificación puede ocasionar resultados inesperados debido al orden y etiquetado en la entrada de parámetros.


### ¿Qué es matplotlib?

Matplotlib es una librería que permite la graficación de datos en múltiples estilos de visualización; por defecto, esta librería viene incorporada en la instalación de Python en ArcGIS for Desktop, ArcGIS Pro y QGIS 3.

> Para conocer la versión instalada de esta o cualquier librería disponible, en la consola de Python, importar la librería (p.ej, `import pip`) e ingresar el comando `libreria.__version__`. Para conocer la localización de los archivos usar los comandos `libreria.__path__` y `libreria.__file__`, donde _libreria_ corresponde al nombre del paquete a consultar.


### Requerimientos

* Python 2.7.5 de ArcGIS for Desktop 10.2.2.
* Python 3.10.0+ como instalación independiente o standalone.
* PyCharm 2021.3+ for Anaconda.
* Sistema operativo Microsoft Windows.

> Nota: en caso de no disponer de ArcGIS en su equipo, puede realizar las pruebas de funcionamiento realizando la instalación independiente de la versión 2.7 de Python.


### Ruta de ejecución
 
Para el desarrollo de este ejercicio se recomienda que los scripts y demás archivos requeridos se encuentren en D:\R.GISPython\InstallPackageGraph\ 


### Caso de estudio

Para el desarrollo del script, estimaremos el tiempo de concentración en una cuenca hidrográfica - Tc, qué es el tiempo que tarda una gota de agua que cae en una cuenca hidrográfica, en viajar desde el punto más lejano hasta el punto de salida o sifón de la cuenca. Para este ejemplo utilizaremos la expresión de Giandotti.

<br>
<div  align="center">
    <img align="center"  alt="R.GISPython.InteractiveScript.TcGiangotti" src="https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/TcGiangotti.png" width="240px"/>
</div>


#### Parámetros

* tc, tiempo de concentración en horas.
* A, área de la cuenca = 9.1348 km².
* L, longitud del cauce principal = 4.6106 km.
* S, pendiente media del cauce principal = 0.144015 m/m


### Script Tc_v3.py

```
# -*- coding: UTF-8 -*-
# Nombre: Tc_v3.py
# Descripción: Script interactivo e iterativo para el cálculo y graficación del tiempo de concentración
# Requerimiento: PyCharm 2020.1+, Python 2.7.5 (ArcGIS 10.2.2), Python 3.10.0 (instalación independiente).

# Librerías
import sys
import matplotlib
import matplotlib.pyplot as plt

# Variables
i, variaciones, pendienteMinima = 0, 12, 0.001 # Incremento, variaciones y pendiente mínima

# Función de cálculo
def TcGiandotti(A,L,S):
	return (4*(A**0.5)+1.5*L)/(25.3*(S*L)**0.5)

# Función para creación de líneas de separación
def Separador(n=24): #Usando un valor por defecto de 24 guiones
	nc = "-"
	print(nc*n)

# Cabecera
Separador(56)
print ('Script interactivo e iterativo en Python con graficación')
Separador(56)
print ('Cálculo y graficación del Tiempo de Concentración de una cuenca hidrográfica usando la expresión de Giandotti.')
print ('Python versión: ' + str(sys.version))
print ('matplotlib versión: ' + str(matplotlib.__version__))
print ('Encuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/InstallPackageGraph')
print ('Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License')
print ('Créditos: r.cfdtools@gmail.com\n')

# Variables de entrada
Separador(18)
print("Datos de entrada")
Separador(18)
A = float(input("Área cuenca, km²: "))
L = float(input("Longitud cauce principal, km: "))
S = float(input("Pendiente media cauce principal, m/m: "))
imprimirTituloGrafica = input('Imprimir título descriptivo en gráfica, Python 3 (y/n), Python 2 no recomendado ("n"): ')

# Calculos
print("\nTc, min: " + str(TcGiandotti(A,L,S)*60)) # Impresión en pantalla usando +
print("\nResultados variando la pendiente y utilizando columnas tabuladas")
Separador()
print("i\tS, m/m\tTc, min")
Separador()
TcGiandottiGx, TcGiandottiGy = [], [] # Listas para graficación de datos
while i < variaciones:
	Svar =  (((S-pendienteMinima)/(variaciones-1))*i+pendienteMinima)
	# print(i+1, "\t", round(Svar,4), "\t", round(TcGiandotti(A,L,Svar)*60,4)) # Concatenación con coma
	print(str(i+1)+"\t"+str(round(Svar,4))+"\t"+str(round(TcGiandotti(A,L,Svar)*60,4))) # Concatenación con +
	TcGiandottiGx.append(Svar)
	TcGiandottiGy.append(TcGiandotti(A,L,Svar)*60)
	i += 1

# Graficación de datos
Separador()
print("Graficación de datos")
Separador()
print("S (m/m)\n",TcGiandottiGx)
print("Tc (min)\n",TcGiandottiGy)
graficaTitulo="Tc, Tiempo de concentración\nVariando la pendiente cada "+str(round(((S-pendienteMinima)/(variaciones-1)),4))+" m/m\nA, km²: "+str(A)+", L, km: "+str(L)
plt.plot(TcGiandottiGx,TcGiandottiGy, label="Tc Giandotti, min", color='black', linewidth=1, marker='p', markersize=4, markerfacecolor='black', markeredgecolor='black')
if str(imprimirTituloGrafica.lower()) == 'y':
    plt.title(graficaTitulo)
plt.xlabel("S, m/m")
plt.ylabel("Tc, min")
plt.show()
```

 

### Descripción instrucciones y comandos empleados

| Instrucción                                                                                                                                                              | Explicación                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| #                                                                                                                                                                        | Comentario de una línea.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| """<br/>"""                                                                                                                                                              | 3 comillas simples o dobles permiten definir el inicio y fin de comentarios en múltiples líneas.                                                                                                                                                                                                                                                                                                                                                             |
| # -*- coding: UTF-8 -*-                                                                                                                                                  | Permite definir la codificación de texto utilizada en el script.                                                                                                                                                                                                                                                                                                                                                                                             |
| import sys                                                                                                                                                               | Importación de librería de systema _sys_.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| sys.version                                                                                                                                                              | Muestra la versión actual de Python desde la que se está ejecutando el script.                                                                                                                                                                                                                                                                                                                                                                               |
| \n                                                                                                                                                                       | Agrega un salto de línea en impresiones en pantalla.                                                                                                                                                                                                                                                                                                                                                                                                         |
| print                                                                                                                                                                    | Permite realizar la impresión de un resultado en la consola. En las versiones de Python 2.x, todo aquello que aparezca después del print será impreso en pantalla, incluso los paréntesis sí existen concatenaciones con comas. En las versiones de Python 3.x, solo se imprimirá aquello que esté entre paréntesis. Nótese que es posible realizar cálculos adicionales en la impresión `(TcGiandotti*60)` e incluso concatenar resultados usando coma o +. |
| str()                                                                                                                                                                    | Permite convertir una variable o resultado numérico en una cadena de texto. Requerido para concatenación usando +.                                                                                                                                                                                                                                                                                                                                           |
| input('mensaje')                                                                                                                                                         | Entrada de usuario por consola.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| float()                                                                                                                                                                  | Convierte la entrada de usuario por consola a un valor numérico flotante.                                                                                                                                                                                                                                                                                                                                                                                    |
| i, variaciones, pendienteMinima = 0, 12, 0.001                                                                                                                           | Definición de múltiples variables en una única línea.                                                                                                                                                                                                                                                                                                                                                                                                        |
| def TCGiandotti(A,L,S):<br>return (4*(A**0.5)+1.5*L)/(25.3*(S*L)**0.5)                                                                                                   | Creación de función con tres parámetros de entrada para el cálculo del tiempo de concentración, `return` es utilizado para devolver el resultado de la función.                                                                                                                                                                                                                                                                                              |
| def Separador(n=24):<br>nc = '—'<br>print(nc*n)                                                                                                                          | Creación de una función para crear una línea de separación usando guiones y con un valor predeterminado. Esta función no requiere de `return`.<br>nc*n: Python permite operaciones con strings, por ejemplo, replicando un carácter n veces.                                                                                                                                                                                                                 |
| Separador(18)<br>Separador()                                                                                                                                             | Llamado de la función Separador() definiendo o no la longitud n de la línea.                                                                                                                                                                                                                                                                                                                                                                                 |
| i += 1                                                                                                                                                                   | `+=` permite incrementar una variable. También puede ser definido como `i=i+1` pero en Python convencionalmente se utiliza la sintaxis `+=`.                                                                                                                                                                                                                                                                                                                 | 
| while i < variaciones:                                                                                                                                                   | Bucle o ciclo desde `i=0` hasta el valor definido en variaciones.                                                                                                                                                                                                                                                                                                                                                                                            |
| import matplotlib <br> import matplotlib.pyplot as plt                                                                                                                   | Importación de librería general y objeto pyplot, requeridos para impresión en pantalla de la versión utilizada y la graficación.                                                                                                                                                                                                                                                                                                                             |
| matplotlib.__version__                                                                                                                                                   | Versión de matplotlib.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| .lower()                                                                                                                                                                 | Convierte una cadena o una variable de texto en minúsculas. Requerido para validar entradas de usuario en `input()` cuando se solicita al usuario ingresar _y/n_.                                                                                                                                                                                                                                                                                            |
| TcGiandottiGx, TcGiandottiGy = [], []                                                                                                                                    | Creación de listas vacías para el almacenamiento de los datos requeridos para la graficación.                                                                                                                                                                                                                                                                                                                                                                |
| TcGiandottiGx.append(Svar) <br> TcGiandottiGy.append(TcGiandotti(A,L,Svar)*60)                                                                                           | Agregar elementos calculados a la lista creada.                                                                                                                                                                                                                                                                                                                                                                                                              |
| plt.plot(TcGiandottiGx,TcGiandottiGy, label="Tc Giandotti, min", color='black', linewidth=1, marker='p', markersize=4, markerfacecolor='black', markeredgecolor='black') | Llamado de gráfica incluyendo estilo básico de graficación.                                                                                                                                                                                                                                                                                                                                                                                                  |
| if str(imprimirTituloGrafica.lower()) == 'y':<br> plt.title(graficaTitulo)                                                                                               | Validación para impresión de título de gráfica en Python 2 o 3. No recomendado en Python 2 usando matplotlib 1.3.0 de Python 2.7.5 sobre ArcGIS for Desktop.                                                                                                                                                                                                                                                                                                 |
| plt.xlabel("S, m/m") <br> plt.ylabel("Tc, min") <br> plt.show()                                                                                                          | Etiquetas de ejes y despliegue de gráfica.                                                                                                                                                                                                                                                                                                                                                                                                                   |

> En Python, por defecto se asume que la entrada ingresada por consola a través del comando `input()` es una cadena de texto, por tal motivo, cuando se trata de entradas numéricas, será necesaria la conversión a tipo flotante. <br><br>
> Dentro del paréntesis de la entrada `input()`, es necesario ingresar un texto descriptivo que permita al usuario entender el tipo y valor requerido.<br><br>
> Para la ejecución en Python 2, no se recomienda imprimir el título de la gráfica debido a que ha sido ensamblado a partir de la concatenación de varios de los valores ingresados.


### Procedimiento de instalación en Python 3.10.0

0. Verificar las librerías instaladas en Python 3.10 dentro del directorio _Scripts_. En la raíz del CMD de Windows ingresar el comando `dir Python310\Scripts` o desde cualquier ruta `dir C:\Python310\Scripts`.

> Tenga en cuenta que la ruta instalación de Python 3.10 depende de la ruta definida por el usuario en el momento de la instalación. Para consultar las rutas de las versiones instaladas de Python en su sistema, consultar https://github.com/rcfdtools/R.GISPython/tree/main/PythonVersion

![Python3.10.0StandaloneCMDScriptsDir.png](https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/Python3.10.0StandaloneCMDScriptsDir.png)


1. En el command o _CMD_ de Windows ejecutar `py -3.10 -m pip install -U pip`. Esta instrucción permite actualizar la versión existente de `pip` antes de instalar paquetes adicionales recientes.

> En el evento de que el paquete _pip_ no se encuentre instalado, la instrucción anterior realizará la instalación. <br><br>
> Para la instalación y actualización sobre la versión por defecto definida en las variables de entorno de Windows, no es necesario especificar la versión de Python y puede utilizar la instrucción `C:\Python -m pip install -U pip`. Tenga en cuenta que si la versión por defecto de Python es la correspondiente a la incluida en instalación de ESRI ArcGIS, se actualizarán las versiones por defecto de la aplicación y podrán presentarse errores o valores errados en la ejecución de los geo-procesos asociados a esta herramienta.

![Python3.10.0StandaloneCMDpipUpdate.png](https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/Python3.10.0StandaloneCMDpipUpdate.png)

> La actualización también puede ser realizada directamente desde PyCharm, oprimir `Ctrl+Alt+S`, ir a la pestaña _Project_, seleccionar _Python Interpreter_, seleccionar _Python 3.10_, dar doble clic en el paquete _pip_ y en la ventana _Available Packages_ seleccionar _pip_, especificar la versión a actualizar y dar clic en Install Package.

![Python3.10.0StandalonePyCharm2021.3pipUpdate.png](https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/Python3.10.0StandalonePyCharm2021.3pipUpdate.png)

2. Para la instalación de la versión más actual de _matplotlib_, en el CMD ejecutar `py -3.10 -m pip install -U matplotlib`.

![Python3.10.0StandaloneCMDmatplotlibInstall.png](https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/Python3.10.0StandaloneCMDmatplotlibInstall.png)

> matplotlib también puede ser instalado directamente desde el administrador de paquetes de PyCharm para el intérprete de Python seleccionado por el usuario.<br><br>
> Para desinstalar la librería podrá utilizar la secuencia de comandos `py -3.10 -m pip uninstall matplotlib`<br><br>
> Para instalar una versión específica de una librería podrá utilizar la instrucción indicando al final y despues de _==_ el número de versión requerida `py -3.10 -m pip install matplotlib==3.4.0`

3. Para verificar la correcta instalación de la librería, en el CMD del sistema, ejecutar Python `C:\py -3.10` y realizar el llamado de la librería y consultar la versión y ruta de instalación a través de los comandos `import matplotlib`, `matplotlib.__version__`, `matplotlib.__path__` y `matplotlib.__file__`

![Python3.10.0StandaloneCMDmatplotlibCheck.png](https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/Python3.10.0StandaloneCMDmatplotlibCheck.png)

> En Python 2.7.5 de ArcGIS for Desktop 10.2.2, podrá realizar la verificación de la versión preinstalada de matplotlib siguiendo el mismo procedimiento descrito anteriormente.

![Python2.7.5ArcGISDesktop10.2.2CMDmatplotlibCheck.png](https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/Python2.7.5ArcGISDesktop10.2.2CMDmatplotlibCheck.png)


### Ejecución desde Pycharm

> PyCharm requiere de configuración previa del intérprete de Python a utilizar en la ejecución del script. Oprima `Ctrl+Alt+S` para acceder a la ventana de configuración y en la pestaña _Project: R.GISPython_ configurar los intérpretes disponibles en su equipo.

![PyCharm2021.3SetupPythonInterpreter.png](https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/PyCharm2021.3SetupPythonInterpreter.png)

Ejecución en PyCharm usando Python 2.7.5 de ArcGIS for Desktop 10.2.2. 
![Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3.png](https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3.png)

Ejecución en PyCharm usando Python 3.10.0.
![Python3.10.0StandalonePyCharm2021.3.png](https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/Python3.10.0StandalonePyCharm2021.3.png)


### Ejecución desde el Command o CMD de Microsoft Windows

Para ejecutar desde la consola de comandos CMD del sistema operativo Windows usando cualquier versión de Python instalada, usar el comando py, la versión requerida (por ejemplo, -3.10) y la ruta completa del archivo .py.

```C:\py -2.7 D:\R.GISPython\InstallPackageGraph\Tc_v3.py```

```C:\py -3.10 D:\R.GISPython\InstallPackageGraph\Tc_v3.py```

Ejecución en consola CMD Python 2.7.5 de ArcGIS for Desktop 10.2.2. 

> En esta versión, la codificación de texto no imprime correctamente caracteres acentuados del español.

![Python2.7.5ArcGISDesktop10.2.2CMD.png](https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/Python2.7.5ArcGISDesktop10.2.2CMD.png)

Ejecución en consola CMD Python 3.10.0 Standalone.
![Python3.10.0StandaloneCMD.png](https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/Python3.10.0StandaloneCMD.png)


### Referencias

* https://packaging.python.org/en/latest/tutorials/installing-packages/
* https://matplotlib.org/stable/gallery/color/named_colors.html
* https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot


### Compatibilidad

* Compatible con cualquier versión de Python.


### Control de versiones

| Versión    | Descripción                                                                                                                                                        | Autor                                     | Horas |
|------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|:-----:|
| 2021.12.08 | Inclusión de propiedades de estilo en gráfica de resultados. Inclusión de condicional para la inclusión o no del título de la gráfica, no recomendado en Python 2. | [rcfdtools](https://github.com/rcfdtools) |   2   |
| 2021.12.01 | Versión inicial con incorporación de librería _sys_ para impresión en pantalla de la versión de Python.                                                            | [rcfdtools](https://github.com/rcfdtools) |   6   |


### Licencia, cláusulas y condiciones de uso

_R.GISPython es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio dando [clic aquí](https://github.com/rcfdtools/R.GISPython/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](https://github.com/rcfdtools/R.GISPython/tree/main/InteractiveScriptFunction) | [:house: Inicio](https://github.com/rcfdtools/R.GISPython/wiki) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.GISPython/discussions/9) | [Siguiente](https://github.com/rcfdtools/R.GISPython/tree/main/ErrorExceptionControl) |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------|

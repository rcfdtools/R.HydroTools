## Diseño geométrico horizontal sinuoso de canales

A partir de la estimación de los radios de curvatura característicos de los meandros existentes en cauces naturales, el índice de sinuosidad y los anchos de sección diseñados hidráulicamente para el transporte del caudal dominante y creciente; determinar los siguientes atributos geométricos requeridos para el trazado del corredor del cauce sinuoso en Autodesk Civil 3D:

* Angulo de deflexión de la onda, α.
* Longitud sinuosa del río, Lr.
* Número de ondas sinuosas, n.
* Longitud hidráulica de cada onda, Lb.
* Longitud de aproximación entre ondas, La.
* Número de subdivisiones en el eje del valle suavizado, Lc * (Lm/4).

### Procedimiento

* (1): Decidir el factor de sinuosidad a aplicar para: a. Mantener la pendiente original del cauce natural, b. Disminuir la pendiente del cauce con un factor de sinuosidad mayor ó c. Aumentar la pendiente del cauce con un factor de sinuosidad menor.
* (2A, 2B, 2C, 2D): Ingresar un radio de curvatura Rc (m) menor o igual al medido. Puede ingresar un valor de 10m para que solver estime el máximo permisible para que la Longitud de Aproximación La (m) sea cero, o para que una onda se empalme con otra sin aproximaxión. Para Solver establecer una alphasemilla cercana a cero y positiva, o ingresar 1. Nota: Este valor no puede ser una raiz negativa obtenida por Solver.
* (3A, 3B): Ingresar el valor calculado de ancho de la base del canal para caudal dominante de Tr: 2.33yr y el ancho del valle máximo. Al ancho de la base del valle disponible se le debe descontar un ancho de separación entre la curva externa de cada onda al borde de talud de la base del valle para evitar que el talud del cauce dominante y del valle sea contínuo y asi prevener la erosión del talud. Se recomiendan 5m a cada lado. Ejemplo:  Si el ancho disponible para valle es de 160m se debe realizar el diseño sinuoso con 150m. En el trazado de ejes usando CIVIL 3D se dibuja el corredor de 160m, un offset de 5m a cada lado y las curvas externas se trazan dentro del corredor efectivo libre para garantizar la separación de taludes.
* (4): Para trazar el eje de la clotoide en CIVIL3D, se toma la longitud hidraulica de cada onda y se divide en 4 partes (Lm/4), se multiplica por el numero de ondas requeridas y se divide el eje del valle en este numero. Luego se traza con una línea espiral o una clotoide de radio Rc característico calculado por el eje sinuoso por los puntos extremos de intersección de cada subtramo con el borde externo de la onda. Para las sample lines dividir B' entre 2 y utilizar este valor para su construcción.

### Funciones de llamado en VBA

```
Sub FUNCIONOBJ_ALPHA()
    ' Calcular el valor del ángulo de radio de giro (Alpha)
    Range("alphaVal").GoalSeek Goal:=0, ChangingCell:=Range("alphaSemilla")
End Sub
```
```
Sub FUNCIONOBJ_ALPHA_Rc_max()
    ' Calcular el valor del ángulo de radio de giro (Alpha)
    Mensaje = MsgBox("Utilice Solver para obtener alpha y Rc máximo", vbOKCancel, "R.HydroTools")
    Application.SendKeys "%D"
    Application.SendKeys "Y2"
End Sub
```

## Ilustraciones

![R.HydroTools.DisenoSinuosoCanal.Screenshot1](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoSinuosoCanal/Screenshot/Screenshot1.png)
![R.HydroTools.DisenoSinuosoCanal.Screenshot2](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoSinuosoCanal/Screenshot/Screenshot2.png)
![R.HydroTools.DisenoSinuosoCanal.Screenshot3](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoSinuosoCanal/Screenshot/Screenshot3.png)
![R.HydroTools.DisenoSinuosoCanal.Screenshot4](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoSinuosoCanal/Screenshot/Screenshot4.png)
![R.HydroTools.DisenoSinuosoCanal.Screenshot5](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoSinuosoCanal/Screenshot/Screenshot5.png)
![R.HydroTools.DisenoSinuosoCanal.Screenshot6](https://github.com/rcfdtools/R.HydroTools/blob/main/DisenoSinuosoCanal/Screenshot/Screenshot6.png)


## Referencias
* Desarrollado por baalkara@gmail.com, https://github.com/FrankV13 y r.cfdtools@gmail.com


## Keywords
Sinusoidal river design.


## Control de versiones

Versión | Descripción
--- | ---
| v.20211019 | Actualización general de análisis, gráficas y formato.


## Licencia, cláusulas y condiciones de uso
https://github.com/rcfdtools/R.HydroTools/wiki/License



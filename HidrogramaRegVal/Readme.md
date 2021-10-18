## Registro y validación de hidrogramas obtenidos a partir de modelación hidrológica en HEC-HMS

Este libro de cálculo es utilizado para registrar y validar los pulsos obtenidos en modelos hidrológicos de eventos discretos o de valores máximos. La hoja _Hidrograma4a_ presenta un ejemplo para la estimación de pulsos de hidrogramas para periodos de retorno superiores a partir de los valores pico obtenidos en los periodos de retorno registrados. 

### Consideraciones

* La regresión es realizada a través de la tendencia logarítmica que se obtiene, por ejemplo, para periodos de retorno de 2.33, 5, 10, 25, 50 y 100 años. 
* El tiempo al pico se va reduciendo a medida que se aumenta el periodo de retorno.
* Para periodos de retorno altos, el tiempo al pico presenta poca variabilidad.


### Ilustraciones

![R.HydroTools.HidrogramaRegVal.Screenshot1](https://github.com/rcfdtools/R.HydroTools/blob/main/HidrogramaRegVal/Screenshot/Screenshot1.png)
![R.HydroTools.HidrogramaRegVal.Screenshot2](https://github.com/rcfdtools/R.HydroTools/blob/main/HidrogramaRegVal/Screenshot/Screenshot2.png)
![R.HydroTools.HidrogramaRegVal.Screenshot3](https://github.com/rcfdtools/R.HydroTools/blob/main/HidrogramaRegVal/Screenshot/Screenshot3.png)
![R.HydroTools.HidrogramaRegVal.Screenshot4](https://github.com/rcfdtools/R.HydroTools/blob/main/HidrogramaRegVal/Screenshot/Screenshot4.png)


### Control de versiones

Versión | Descripción
--- | ---
| v.20201011 | Inclusión de regresión logarítmica para la estimación de pulsos para periodos de retorno superiores a los registrados por factor Trn / Tr100. Ejemplo en hoja Hidrograma4a.
| v.20211014 | Actualización general de formato. Inclusión de gráfica independiente con curvas potenciales para factores de atenuación California Montañoso - USA.


### Licencia, cláusulas y condiciones de uso
https://github.com/rcfdtools/R.HydroTools/wiki/License

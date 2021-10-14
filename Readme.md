### R.HydroTools
Tools for hydrological an hydraulics computational analysis, by r.cfdtools@gmail.com.

Licencia, cláusulas y condiciones de uso en https://github.com/rcfdtools/R.HydroTools/wiki/License

### Herramientas disponibles

Parámetro| Descripción
--- | ---
| Parámetros generales para el diseño y modelación de cauces | Este libro de cálculo contiene lineamientos generales y permite registrar: Parámetros técnicos requeridos. Parámetros técnicos estimados. Parámetros geotécnicos, ambientales y sociales. Parámetros territoriales. https://github.com/rcfdtools/R.HydroTools/tree/main/DisenoCaucesParametros

| Fa - Factor de atenuación de la precipitación por área simultánea | Es un valor numérico adimensional (entre 0 y 1) que multiplica la lluvia total máxima en 24 horas, estimada para cada subcuenca o sus pulsos equivalentes (del hietograma) en función del área de aportación y solo es válido en un punto de estudio determinado. Sirve para ajustar o atenuar el valor total de lluvia (mm) máxima, suponiendo que a mayor área acumulada existe menor probabilidad de que simultáneamente llueva sobre toda la cuenca. El factor de atenuación es inversamente proporcional al área acumulada de la cuenca hasta un determinado punto de estudio. A mayor área acumulada, menor factor y por ende menor precipitación máxima simultánea. Luego de la modelación o tránsito hidrológico, los valores de caudal pico e hietogramas, solo serán válidos para el punto en estudio. Para subcuencas pequeñas en cauces laterales al rio artificial a diseñar, puede suponerse que el centro de tormenta cubre toda esta área y por consiguiente el factor multiplicador será de 1. https://github.com/rcfdtools/R.HydroTools/tree/main/FactorAtenuacionPrecipitacionFa

| Registro y validación de hidrogramas obtenidos a partir de modelación hidrológica en HEC-HMS | Este libro de cálculo es utilizado para registrar y validar los pulsos obtenidos en modelos hidrológicos de eventos discretos o de valores máximos. La hoja Hidrograma4a presenta un ejemplo para la estimación de pulsos de hidrogramas para periodos de retorno superiores a partir de los valores pico obtenidos en los periodos de retorno registrados. https://github.com/rcfdtools/R.HydroTools/tree/main/HidrogramaRegVal

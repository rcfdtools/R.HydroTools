<div align="center"><img alt="R.HydroTools" src="../../file/graph/R.HydroTools.svg" width="300px"></div>

## PMP - Precipitación máxima probable utilizando 104 distribuciones de probabilidad
Keywords: `pmp` `probability-distributions` `scipy`

Estudio de la PMP utilizando las múltiples distribuciones de probabilidad disponibles en SciPy con estimación de precipitación para diferentes periodos de retorno - Tr.


### Probability distributions not right for rain analysis

When the annual values contain zeros, the follow distributions has to be avoided.

* foldcauchy
* genextreme
* genhyperbolic
* halfcauchy
* halfgennorm
* levy
* powerlognorm
* powernorm
* burr12
* cauchy
* skewcauchy
* rel_breitwigner


### References

* https://xiaoganghe.github.io/python-climate-visuals/chapters/data-analytics/scipy-basic.html
* https://docs.scipy.org/doc/scipy/reference/stats.html
* https://docs.scipy.org/doc/scipy/tutorial/stats.html
* https://github.com/GeomarPerales/Probability-Distributions-for-hydrology-with-Python
* https://github.com/openmeteo/hydrognomon/releases
* https://www.statgraphics.com/probability-distributions
* https://docs.python.org/es/3/library/math.html
* https://www.geeksforgeeks.org/python-normal-distribution-in-statistics/
* https://www.tutorialspoint.com/python_data_science/python_normal_distribution.htm
* https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html
* https://www.geeksforgeeks.org/how-to-print-an-entire-pandas-dataframe-in-python/
* https://www.geeksforgeeks.org/select-row-with-maximum-and-minimum-value-in-pandas-dataframe/
* https://www.geeksforgeeks.org/how-to-compare-two-columns-in-pandas/
* https://stackoverflow.com/questions/13091649/unique-plot-marker-for-each-plot
* https://hatarilabs.com/ih-en/statistical-analysis-of-precipitation-data-with-python
* https://www.youtube.com/watch?v=GnC6wFkViGk
* https://www.sciencedirect.com/science/article/pii/S0022169423005000
* https://csce.ca/elf/apps/CONFERENCEVIEWER/conferences/2017/pdfs/HYD/FinalPaper_725.pdf
* https://www.mrl.ucsb.edu/~seshadri/PreparingFigures-June2019.pdf
* https://zhauniarovich.com/post/2022/2022-09-matplotlib-graphs-in-research-papers/
* https://www3.nd.edu/~pkamat/pdf/graphs.pdf
* https://github.com/jbmouret/matplotlib_for_papers


**How to show more lines in the PyCharm RUN console**

* File --> Settings --> Editor --> General --> Console -->
* Then check "Override console cycle buffer size (1024 KB)"
* Change that values to whatever you need, p.e. 4096


### Licencia, cláusulas y condiciones de uso

_R.HydroTools es de uso libre para fines académicos, conoce nuestra [licencia, cláusulas, condiciones de uso](../../LICENSE.md) y como referenciar los contenidos publicados en este repositorio._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [r.cfdtools](https://github.com/rcfdtools) en GitHub._

| [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.HydroTools/discussions/xxx) |
|-----------------------------------|------------------------------|

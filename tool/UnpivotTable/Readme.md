<div align="center"><img alt="R.HydroTools" src="../../file/graph/R.HydroTools.svg" width="300px"></div>

# Unpivot a multiple column table into a table with stacked records
Keywords: `unpivot` `python` `stack`

> Over ArcGIS or a .dbf file, the maximum number of columns are 256. 
> 
> An extensive Pandas dataframe with more than 256 attributes, could be truncated if directly is converted into a GIS table.

The size of the transformed unpivot file, could be much bigger than the original pivot file. 

[UnpivotTable.py](UnpivotTable.py)

```
# -*- coding: UTF-8 -*-
# Name: UnpivotTable.py
# Description: unpivot a multiple column table into a table with multiple records
# Requirements: Python 3+, pandas
# Repository: https://github.com/rcfdtools/R.GISPython/tree/main/UnpivotTable
# License: https://github.com/rcfdtools/R.GISPython/wiki/License

# Libraries
import pandas as pd

# General variables
pivot_table = 'df_prec_ANA_20230216.csv'  # Current IDEAM records file with multiple columns
date_field = 'Date' # Column date name
var_name = 'Codigo' # Column code name
value_name = 'Valor' # Column value name

# Procedure
df = pd.read_csv(pivot_table, low_memory=False, parse_dates=[date_field], dayfirst=True) # Check your right day position in the date field
print(df.info(), '\n')
print(df.dtypes, '\n')
print(df, '\n')
df_unpivot = pd.melt(df, id_vars=date_field, var_name=var_name, value_name=value_name, ignore_index = True)
print(df_unpivot, '\n')
df_unpivot.index.name = 'Id'
df_unpivot.to_csv('unpivot_'+pivot_table)`
```

## References

* https://towardsdatascience.com/4-tricks-you-should-know-to-parse-date-columns-with-pandas-read-csv-27355bb2ad0e
* https://www.statology.org/pandas-unpivot/
* https://sparkbyexamples.com/pandas/pandas-unpivot-dataframe/


### Licencia, cláusulas y condiciones de uso

_R.HydroTools es de uso libre para fines académicos, conoce nuestra [licencia, cláusulas, condiciones de uso](../../LICENSE.md) y como referenciar los contenidos publicados en este repositorio._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [r.cfdtools](https://github.com/rcfdtools) en GitHub._

| [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.HydroTools/discussions/xxx) |
|-----------------------------------|------------------------------------------------------------------------------------------|


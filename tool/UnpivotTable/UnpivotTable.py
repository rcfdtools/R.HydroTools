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
df_unpivot.to_csv('unpivot_'+pivot_table)

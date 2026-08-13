# https://github.com/rcfdtools/R.HydroTools/tree/main/tool/Population
# paper.py: script for paper genaration over a .md file

# Libraries
# Requires the library openpyxl: pip install pandas openpyxl xlrd
import platform
import functions as funcs
import dictionary as dictionary
import pandas as pd
import numpy as np
import tabulate
from tabulate import tabulate
import matplotlib.pyplot as plt
from simpledbf import Dbf5
from datetime import datetime
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# General Setup
app_version = 'v20260806'
file_path = '../data/Population.xlsx'
drop_dataset_notes = True
create_plot = False # ● Creates, save and include plots into reports
show_plot = False # Show plot on Python screen console
print_on_screen = False # Global print control in screen
zone_vars = ['Total', 'Urban', 'Rural']
water_supply = pd.DataFrame({'CZ': [1000, 2000, 99999], 'WS': [120, 130, 140]}) # Water supply in liters per capita per day - lpcd: Level or elevation, Water Supply
runtime = datetime.now()
python_version = platform.python_version()
pandas_version = pd.__version__
numpy_version = np.__version__
file_log_name = f'../report/Readme.md'  # Markdown file log
file_log = open(file_log_name, 'w+', encoding='utf-8')  # w+ create the file if it doesn't exist
dtype={'Year': int, 'CountyID': str, 'StateID': str, 'PTotal': int, 'PUrban': int, 'PRural': int}
df = pd.read_excel(file_path, sheet_name='Population', dtype=dtype)

# Checking wrong Counties names (show only in console)
print('\nChecking wrong Counties names (empty list means all is right)')
df = df.sort_values(by=['CountyID', 'CountyName'])
df_check = df[['CountyID','CountyName']].drop_duplicates()
df_check = df_check[df_check.duplicated(subset=['CountyID'],keep=False)]
print(df_check.to_markdown(index=False))

# Processing
df = df.sort_values(by=['StateName', 'CountyID', 'Year'])
if drop_dataset_notes: df = df.drop(columns=['Notes'])
#df['Report'] = f'[{df['CountyID'].astype(str)}.md](Link)'
df['CountyIDmd'] = '[' + df['CountyID'].astype(str) + '](' + df['CountyID'].astype(str)+ '.md)'
df = df.drop_duplicates(subset=['CountyID'])
grouped = df.groupby('StateName')
funcs.print_log(file_log, '<img alt="R.HydroTools" src="../../../../file/graph/R.HydroTools.svg" width="250px">', center_div=True, on_screen=print_on_screen)
funcs.print_log(file_log, f'# {dictionary.dicts['study_name']} \n{dictionary.dicts['keywords']}\n\n{dictionary.dicts['study_desc']}', on_screen=print_on_screen)
for group_name, group_df in grouped:
    detailed_df = group_df.drop(columns=['CountyID', 'StateName', 'Source', 'Year', 'CountryID', 'CountryName', 'StateID', 'PTotal', 'PUrban', 'PRural'])
    detailed_df = detailed_df.rename(columns={'CountyIDmd': 'CountyID'})
    funcs.print_log(file_log, f'\n\n## {group_name.upper()} ({len(detailed_df)} Counties)\n\n')
    funcs.print_log(file_log, detailed_df[['CountyID', 'CountyName']].to_markdown(index=False))
funcs.print_log(file_log, f'\n\n<div align="center"><img alt="R.HydroTools" src="../graph/qr-code.png" width="250px"><br><sub>Share this research</sub></div><br>', on_screen = print_on_screen)
funcs.print_log(file_log, f'\n\n<sub>{dictionary.dicts['disclaimer']}</sub>', on_screen = print_on_screen)
funcs.print_log(file_log, f'\n\n| [:house: Home](../../Readme.md)  | [:beginner: Help / Collab](https://github.com/rcfdtools/R.HydroTools/discussions/31) |', on_screen=print_on_screen)
funcs.print_log(file_log, f'\n|----------------------------|-------------------------------------------------------------------------------------------|', on_screen=print_on_screen)



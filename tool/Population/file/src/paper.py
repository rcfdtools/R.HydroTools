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
file_path = '../data/Population.xlsx'
drop_dataset_notes = True
print_on_screen = False # Global print graph in screen
create_location_map = False # ● Create and save location map
file_log_name = f'../report/Readme.md'  # Markdown file log
file_log = open(file_log_name, 'w+', encoding='utf-8')  # w+ create the file if it doesn't exist
dtype={'Year': int, 'CountyID': str, 'StateID': str, 'PTotal': int, 'PUrban': int, 'PRural': int}
df = pd.read_excel(file_path, sheet_name='Population', dtype=dtype)
dbf = Dbf5('../shp/ColombiaState4326.dbf', codec='cp1252')
df_shapefile = pd.DataFrame(dbf.to_dataframe())
df_shapefile = df_shapefile[['DeCodigo', 'DeNombre', 'DeNorma', 'Latitude', 'Longitude']]
#print(df_shapefile.to_markdown(index=False))

# Checking wrong Counties names (show only in console)
print('\nChecking wrong Counties names (empty list means all is right)')
df = df.sort_values(by=['CountyID', 'CountyName'])
df_check = df[['CountyID','CountyName']].drop_duplicates()
df_check = df_check[df_check.duplicated(subset=['CountyID'],keep=False)]
print(f'{df_check.to_markdown(index=False)}\n')

# Processing
df = df.sort_values(by=['StateName', 'CountyID', 'Year'])
if drop_dataset_notes: df = df.drop(columns=['Notes'])
#df['Report'] = f'[{df['CountyID'].astype(str)}.md](Link)'
df['CountyIDmd'] = '[' + df['CountyID'].astype(str) + '](' + df['CountyID'].astype(str)+ '.md)'
df = df.drop_duplicates(subset=['CountyID'])
grouped = df.groupby('StateID')
funcs.print_log(file_log, '<img alt="R.HydroTools" src="../../../../file/graph/R.HydroTools.svg" width="250px">', center_div=True, on_screen=print_on_screen)
funcs.print_log(file_log, f'# {dictionary.dicts['study_name']} \n{dictionary.dicts['keywords']}\n\n{dictionary.dicts['study_desc']}\n', on_screen=print_on_screen)
for group_id, group_df in grouped:
    # print(f'Processing: ID {group_id}')
    df_shapefile_info = df_shapefile[df_shapefile['DeCodigo'] == group_id]
    state_name = df_shapefile_info['DeNombre'].values[0]
    print(f'Processing: {state_name} (ID: {group_id})')
    #print(f'\n{df_shapefile_info.to_markdown(index=False)}\n')
    state_latitude = df_shapefile_info['Latitude'].values[0]
    state_longitude = df_shapefile_info['Longitude'].values[0]
    fig_file0a = '../graph/' + group_id + 'LocationMap.png'
    if create_location_map:
        location_map_plot = funcs.location_map(point_latitude = state_latitude, point_longitude = state_longitude, point_name = df_shapefile_info['DeNombre'].values[0].upper(), state_filter = group_id, county_label_on = True)
        location_map_plot.savefig(fig_file0a, dpi=120)
        plt.close()
    detailed_df = group_df.drop(columns=['CountyID', 'StateName', 'Source', 'Year', 'CountryID', 'CountryName', 'StateID', 'PTotal', 'PUrban', 'PRural'])
    detailed_df = detailed_df.rename(columns={'CountyIDmd': 'CountyID'})
    funcs.print_log(file_log, f'\n## {df_shapefile_info['DeCodigo'].values[0]} - {state_name.upper()} ({len(detailed_df)} Counties)\n\nRegulation: {df_shapefile_info['DeNorma'].values[0]}\n')
    funcs.print_log(file_log, f'<img alt="rcfdtools" src="{fig_file0a}" width="500"></img>', center_div=True, on_screen=print_on_screen)
    funcs.print_log(file_log, detailed_df[['CountyID', 'CountyName']].to_markdown(index=False), center_div=True)
funcs.print_log(file_log, f'\n\n<div align="center"><img alt="R.HydroTools" src="../graph/qr-code.png" width="250px"><br><sub>Share this research</sub></div><br>', on_screen = print_on_screen)
funcs.print_log(file_log, f'\n\n<sub>{dictionary.dicts['disclaimer']}</sub>', on_screen = print_on_screen)
funcs.print_log(file_log, f'\n\n| [:house: Home](../../Readme.md)  | [:beginner: Help / Collab](https://github.com/rcfdtools/R.HydroTools/discussions/31) |', on_screen=print_on_screen)
funcs.print_log(file_log, f'\n|----------------------------|-------------------------------------------------------------------------------------------|', on_screen=print_on_screen)



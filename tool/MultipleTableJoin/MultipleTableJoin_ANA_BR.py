# -*- coding: UTF-8 -*-
# Name: MultipleTableJoin_ANA_BR.py
# Description: this script join multiple separated tables into a unique unpivot table.
# Source dataset: https://www.ufrgs.br/hge/ana-data-acquisition/
# Repository: https://github.com/rcfdtools/R.GISPython/tree/main/MultipleTableJoin
# License: https://github.com/rcfdtools/R.GISPython/wiki/License
# Requirements: Python 3+, Pandas,
# Attention: ANA-BR uses dd MM AAAA format and decimal point format for numeric values

# Libraries
import glob
import os
import pandas as pd
import shutil


# Functions
def processing_file(file):
    print('Processing %s' % file[len_input_path:9999])
    df = pd.read_csv(file, delim_whitespace=True, header=None)
    df.columns = [day_column, month_column, year_column, ana_br_type]
    df[station_id] = file[len_input_path:len_input_path + gauge_id_digits]
    df['date'] = pd.to_datetime(df[[year_column, month_column, day_column]])
    df.to_csv(temp_path + file[len_input_path:9999], encoding='utf-8', index=False)

# General parameters
input_path = 'ANA_BR/Source/Level/'  # Your local input file folder
temp_path = 'Temp/'  # Your local output temporal folder
stations_file = 'ANA_BR/Stations.csv'  # File with the stations list to process. If the list contains repeated values, transformed files is posted only one time in the temporal output folder. Use quotes for the first station, e.g. "00049000"
ana_br_type = 'level'  # ANA options: precipitation, discharge, level
format_file = '.txt'  # CAMELS-BR use .txt files
joined_file = 'ana_br' + '_' + ana_br_type + '.csv'  # Joined file name to import in ArcGIS
year_column = 'year'
month_column = 'month'
day_column = 'day'
station_id = 'codigo'
    replace_value = -9999.0  # For ANA-BR, -1.0 values correspond to nan values for precipitation & discharge and -9999.0 for level values.
gauge_id_digits = 8  # For ANA-BR, the gauge ID is the first eight digits of the file name
process_all = True  # Process all the stations. True ignore the file Stations.csv. False process only the list included in Stations.csv

# Procedure
shutil.rmtree(temp_path)
os.mkdir(temp_path, 0o666)
len_input_path = len(input_path)
if os.path.isfile(joined_file):
    os.remove(joined_file)
print('Processing all files contained in the %s folder: %s' % (input_path, process_all))
founded = 0
if not process_all:
    df_stations = pd.read_csv(stations_file, dtype={station_id: str})  # Station list to process
    n_stations = len(df_stations)
    print('Stations list: %s\nStations to process: %d\n\nStarting...' % (stations_file, n_stations))
    for j in range(len(df_stations)):
        station_file = input_path + str(df_stations[station_id][j]) + format_file
        if os.path.isfile(station_file):
            processing_file(station_file)
            founded += 1
        else:
            print('Processing %s - file not available' % station_file[len_input_path:9999])
    print('%d stations founded of %d required (%f%%)' %(founded, n_stations, (founded/n_stations)*100))
else:
    table_files = glob.glob(input_path + '*' + format_file)
    print('Files founded: %d\n\nStarting...' % len(table_files))
    for i in table_files:
        processing_file(i)
table_files = glob.glob(temp_path + '*' + format_file)
df = pd.concat(map(pd.read_csv, table_files), ignore_index=True)
print('\n')
df.describe()
df.info()
df[ana_br_type] = df[ana_br_type].replace(replace_value, None)
df.to_csv(joined_file, encoding='utf-8', index=False)
shutil.rmtree(temp_path)
os.mkdir(temp_path, 0o666)
print('\nJoined dataframe sample\n', df)
print('\nJoined file: %s\n' % joined_file)
print('Process accomplished...')
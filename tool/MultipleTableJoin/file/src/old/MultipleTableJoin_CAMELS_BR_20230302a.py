# -*- coding: UTF-8 -*-
# Name: MultipleTableJoin_02_CAMELS_BR_streamflow_m3s.py
# Description: this script join multiple separated tables in a unique unpivot table. Only for 02_CAMELS_BR_streamflow_m3s.zip https://zenodo.org/record/3964745
# Repository:
# License:
# Requirements: Python 3+, Pandas,

# Libraries
import glob
import os
import pandas as pd
import shutil

# Functions
def processing_file(file):
    print('Processing %s' % file[len_input_path:9999])
    df = pd.read_csv(file, sep=column_separator)
    df[station_id] = file[len_input_path:len_input_path + gauge_id_digits]
    df['date'] = pd.to_datetime(df[[year_column, month_column, day_column]])
    df.to_csv(output_path + file[len_input_path:9999], encoding='utf-8', index=False)

# General parameters
input_path = 'Input/'  # Your local input file folder
output_path = 'Output/'  # Your local output temporal folder
stations_file = 'Stations.csv'  # File with the stations list to process. Don't worries if the list contains repeated values because the transformed file is posted only one time in the temporal output folder.
joined_file = 'camels_br_streamflow_m3s.csv'  # Joined file name
format_file = '*.txt'
column_separator = ' '  # Separator used in the input files
year_column = 'year'
month_column = 'month'
day_column = 'day'
station_id = 'gauge_id'
gauge_id_digits = 8
process_all = False  # Process all the station. True ignore the file Stations.csv. False process only the list included in Stations.csv

# Procedure
shutil.rmtree(output_path)
os.mkdir(output_path, 0o666)
len_input_path = len(input_path)
if os.path.isfile(joined_file):
    os.remove(joined_file)
print('Processing all files contained in the %s folder: %s' % (input_path, process_all))
founded = 0
if not process_all:
    df_stations = pd.read_csv(stations_file, sep=column_separator)  # Station list to process
    n_stations = len(df_stations)
    print('Stations list: %s\nStations to process: %d\n\nStarting...' % (stations_file, n_stations))
    for j in range(len(df_stations)):
        station_file = input_path + str(df_stations[station_id][j]) + '_streamflow_m3s.txt'
        if os.path.isfile(station_file):
            processing_file(station_file)
            founded += 1
        else:
            print('Processing %s - file not available' % station_file[len_input_path:9999])
    print('%d stations founded of %d required (%f%%)' %(founded, n_stations, (founded/n_stations)*100))
else:
    table_files = glob.glob(input_path + format_file)
    print('Files founded: %d\n\nStarting...' % len(table_files))
    for i in table_files:
        processing_file(i)
print('Process acomplished...')

table_files = glob.glob(output_path + format_file)
df = pd.concat(map(pd.read_csv, table_files), ignore_index=True)
df.to_csv(joined_file, encoding='utf-8', index=False)
shutil.rmtree(output_path)
os.mkdir(output_path, 0o666)
print('\nJoined dataframe sample\n', df)
print('\nJoined file: %s\n' % joined_file)


'''
References
* https://stackoverflow.com/questions/19350806/how-to-convert-columns-into-one-datetime-column-in-pandas
'''

'''
(2.2) "02_CAMELS_BR_streamflow_m3s"

Files with daily streamflow time series obtained from ANA's website (Brazilian National Water Agency - http://www.snirh.gov.br/hidroweb/).
Each file refers to the time series of a stream gauge. The gauge ID is the first eight digits of the file name.
Missing values are represented by "nan".

The column "streamflow_m3s" indicates daily observed streamflow in cubic meters per second.
The column "qual_control_by_ana" is set to 1 if the data was quality checked by ANA (Brazilian National Water Agency) and a value of 0 otherwise.
The column "qual_flag" indicates the reliability of streamflow estimates. It is provided by ANA (Brazilian National Water Agency) and consists of the following quality flags: 0, when there is no description; 1, streamflow resulted from stream stage measurements and the rating-curve; 2, streamflow qualitatively estimated by ANA, i.e., without stream stage measurements; 3, streamflow values marked as doubtful; and 4, when the stream water level falls outside the range of the stream stage.
'''
# -*- coding: UTF-8 -*-
# Name: MultipleTableJoin_02_CAMELS_BR_streamflow_m3s.py
# Description: this script join multiple separated tables in an unique unpivot table. Only for 02_CAMELS_BR_streamflow_m3s.zip https://zenodo.org/record/3964745
# Repository:
# License:
# Requirements: Python 3+, Pandas,

# Libraries
import glob
import os
import pandas as pd
import shutil

# General parameters
input_path = 'Input/' # Your local input file folder
output_path = 'Output/' # Your local output temporal folder
join_file = 'camels_br_streamflow_m3s.csv' # Joined file name
format_file = '*.txt'
column_separator = ' ' # Separator used in the input files
year_column = 'year'
month_column = 'month'
day_column = 'day'
gauge_id_digits = 8

# Procedure
shutil.rmtree(output_path)
os.mkdir(output_path, 0o666)
len_input_path = len(input_path)
if os.path.isfile(join_file):
    os.remove(join_file)
table_files = glob.glob(input_path + format_file)
for i in table_files:
    print('Processing %s' %i[len_input_path:9999])
    df = pd.read_csv(i, sep=column_separator)
    df['gauge_id'] = i[len_input_path:len_input_path+gauge_id_digits]
    df['date'] = pd.to_datetime(df[[year_column, month_column, day_column]])
    df.to_csv(output_path + i[len_input_path:9999], encoding='utf-8', index=False)
table_files = glob.glob(output_path + format_file)
df = pd.concat(map(pd.read_csv, table_files), ignore_index=True)
df.to_csv(join_file, encoding='utf-8', index=False)
shutil.rmtree(output_path)
os.mkdir(output_path, 0o666)
print('\n', df)


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
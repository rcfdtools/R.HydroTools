# -*- coding: UTF-8 -*-

import glob
import vaex
import pandas as pd
import matplotlib.pylab as plt

input_path = 'D:/IDEAM_CO/csv_files/'
out_path = 'D:/IDEAM_CO/hdf5_files/'
out_filter = 'D:/IDEAM_CO/csv_files_filter/'
stations_file = 'IDEAM_CO/Stations.csv'  # File with the stations list to process. Use quotes for the first station, e.g. "2804500076"
station_code = 'CodigoEstacion'
sensor_code = 'CodigoSensor'
date_name = 'FechaObservacion'
value_name = 'ValorObservado'
station_name = 'NombreEstacion'
state_name = 'Departamento'
countie_name = 'Municipio'
hdg_zone_name = 'ZonaHidrografica'
latitude_name = 'Latitud'
longitude_name = 'Longitud'
parameter_name = 'DescripcionSensor'
unit_name = 'UnidadMedida'
count_by_parameter = False
hdf5_convert = False  # Only if the files are not converted yet
hdf5_name = 'PresionAtmosferica'
#station_include = ['2804500076', '0023190130']  # Use ['station1', 'station2', '...',]

'''
dtype = {station_code: 'str', sensor_code: 'str', value_name: 'float',
         station_name: 'str', state_name: 'str', countie_name: 'str',
         hdg_zone_name: 'str', latitude_name: 'float', longitude_name: 'float',
         parameter_name: 'str', unit_name: 'str'}
'''

dtype = {station_code: 'str', sensor_code: 'str'}

# Convert to HDF5 format
if hdf5_convert:
    csv_files = glob.glob(input_path+'*.csv')
    for i, csv_file in enumerate(csv_files, 1):
        #for j, df in enumerate(vaex.from_csv(csv_file, chunk_size=5_000_000, dtype=dtype, parse_dates=[date_name], low_memory=False), 1):  # Parse dates increase the processing time to hours
        for j, df in enumerate(vaex.from_csv(csv_file, chunk_size=5_000_000, dtype=dtype, low_memory=False), 1):  # Parse dates increase the processing time to hours
            print('Exporting %d %s to hdf5 part %d' % (i, csv_file, j))
            #df.export_hdf5(f'I:/IDEAM_CO/hdf5_files/Precipitacion_{i:02}_{j:02}.hdf5')
            df.export_hdf5(out_path+hdf5_name+'_'+str(i).zfill(2)+'_'+str(j).zfill(2)+'.hdf5')

# Dataframes
df = vaex.open(out_path+'*.hdf5')
df_stations = pd.read_csv(stations_file, dtype={station_code: str})  # Station list to process
n_stations = len(df_stations)
print(df_stations)
station_include = []
print('Stations list: %s\nStations to process: %d\n\nStarting...' % (stations_file, n_stations))
for j in df_stations:
    station_include.append(j[station_code])

print('Dataframe head\n', df.head())
print('\nRecords: %d (%fM)' %(df.shape[0], df.shape[0]/1000000))
print('\nDataframe tail\n', df.tail())
print('\nDataframe types\n', df.dtypes)
quantile = df.percentile_approx(value_name, 25)
print('\nFull percentile 25: %s\n' %quantile)
group_res = df.groupby(by=df[station_code], agg={value_name+'_count': vaex.agg.count(value_name)})
print('Count values\n ',group_res)
group_res = df.groupby(by=df[station_code], agg={value_name+'_mean': vaex.agg.mean(value_name)})
print('\nMean values\n ',group_res)
if count_by_parameter:
    group_res = df.groupby(by=df[parameter_name], agg={parameter_name+'_count': vaex.agg.count(parameter_name)})
    print('\nCount values\n ',group_res)


df = df[df[station_code].isin(station_include)]
df.export(out_filter+hdf5_name+'Filter.csv')
print('\nFiltered dataframe\n', df)
'''
plt.plot(df[value_name])
plt.xticks(rotation = 25)
plt.show()
plt.close('all')
'''



# https://vaex.readthedocs.io/en/docs/tutorial.html
# https://www.kdnuggets.com/2021/03/pandas-big-data-better-options.html
# https://towardsdatascience.com/process-dataset-with-200-million-rows-using-vaex-ad4839710d3b
# https://stackabuse.com/rotate-axis-labels-in-matplotlib/
# Vaex: Filtering Data in a Vaex Dataframe   https://www.youtube.com/watch?v=wa6PzcmGD4U
# https://stackoverflow.com/questions/72670884/how-to-filter-a-vaex-dataset-by-a-list-of-numbers-categories
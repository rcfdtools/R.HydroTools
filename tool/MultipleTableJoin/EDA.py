# -*- coding: UTF-8 -*-
# Name: EDA.py
# Description: exploratory data analysis
# Requirements: Python 3+, pandas, tabulate
# Attention: do not convert the .csv file into an Excel file because you would need process more than 1048576 records.


# Libraries
import sys
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import tabulate  # required for print tables in Markdown using pandas
from datetime import datetime


# Function for print and show results in a file
def print_log(txt_print, on_screen=True, center_div=False):
    if on_screen:
        print(txt_print)
    if center_div:
        file_log.write('\n<div align="center">\n' + '\n')
    file_log.write(txt_print + '\n')
    if center_div:
        file_log.write('\n</div>\n' + '\n')


# General variables
station_file = 'C:/IDEAM_CO/IDEAM_Precipitacion_20230426.csv'  # Current IDEAM records file
path = 'D:/R.GISPython/MultipleTableJoin/IDEAM_CO/Output/'  # Your local files output path, use /IDEAM_CO/Output/ for relative path
file_log_name = path + 'EDA.md'
file_log = open(file_log_name, 'w+')   # w+ create the file if it doesn't exist
station_code = 'CodigoEstacion'  # IDEAM station code name
station_name = 'NombreEstacion'  # IDEAM station code name
date_record_name = 'FechaObservacion'  # IDEAM date field name for the record values
latitude_name = 'Latitud'  # IDEAM latitude name
longitude_name = 'Longitud'  # IDEAM longitude name
value_name = 'ValorObservado'  # IDEAM value field name
tag_name = 'DescripcionSensor'  # IDEAM record parameter frequency tag
tag_desc_name = 'DescripcionSensor'  # IDEAM record parameter frequency tag
plot_colormap = 'magma'  # Color theme for plot graphics, https://matplotlib.org/stable/tutorials/colors/colormaps.html
sample_records = 3  # Records to show in the sample table head and tail
histogram_binds = 12
fig_size = 5  # Height size for figures plot
print_table_sample = False
start_year = 1980  # Chirps values starts at 1981
end_year = 2022  # This value have to correspond with the end of the IDEAM series
huge_file = True  # File size exceed you memory RAM size

# Header
print_log('## Exploración y análisis de series - EDA - Representación gráfica')
print_log('\n* Archivo de resultados: ' + file_log_name +
          '\n* Fecha y hora de inicio de ejecución: ' + str(datetime.now()) +
          '\n* Python versión: ' + str(sys.version) +
          '\n* Python rutas: ' + str(sys.path[0:5]) +
          '\n* matplotlib versión: ' + str(matplotlib.__version__) +
          '\n* pandas versión: ' + str(pd.__version__) +
          '\n* Print table samples: ' + str(print_table_sample) +
          '\n* Start year: ' + str(start_year) +
          '\n* End year: ' + str(end_year) +
          '\n* Encuentra este script en https://github.com/rcfdtools/R.LTWB/tree/main/Section03/EDA'
          '\n* Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md'
          '\n* Créditos: r.cfdtools@gmail.com')

# Open the IDEAM station dataframe and show general information
# Learn more about the IDEAM file in https://github.com/rcfdtools/R.GISPython/blob/main/MultipleTableJoin/IDEAM_CO/Readme.md
if huge_file:
    mylist = []
    for chunk in pd.read_csv(station_file, parse_dates=[date_record_name], converters={station_code: str}, low_memory=False, chunksize=30000000):
        mylist.append(chunk)
    station_df = pd.concat(mylist, axis= 0)
    del mylist
else:
    station_df = pd.read_csv(station_file, parse_dates=[date_record_name], converters={station_code: str}, low_memory=False)
ideam_regs = station_df.shape[0]
print_log('\n\n### General dataframe information with %d IDEAM records' % ideam_regs)
print(station_df.info())
print_log('Datatypes in the dataset', center_div=True)
print_log(station_df.dtypes.to_markdown(), center_div=True)
print_log('Null values in the dataset', center_div=True)
print_log(station_df.isnull().sum().to_markdown(), center_div=True)
if print_table_sample:
    print_log('\nDataframe records head sample\n')
    print_log(station_df.head(sample_records).to_markdown())
    print_log('\nDataframe records tail sample\n')
    print_log(station_df.tail(sample_records).to_markdown())
print_log('General statistics table with not year range filter', center_div=True)
print_log(station_df.describe().to_markdown(), center_div=True)
print_log('Stations in the dataset', center_div=True)
stations_np = pd.DataFrame(station_df[station_name].unique())
print_log(stations_np.to_markdown(), center_div=True)
print_log('Records by parameter and station with not year range filter', center_div=True)
stations_np = station_df.groupby([tag_desc_name, station_name]).size()
print_log(stations_np.to_markdown(), center_div=True)

'''
# Slice data from each parameter and station
parameter_list = station_df[tag_name].unique()

for parameter in parameter_list:
    # General information per parameter
    parameter_name = tag_name + ' == "' + parameter + '"'  # Parameter filter
    station_df1 = station_df.query(parameter_name)  # Filter for parameter
    station_df1 = station_df1[(station_df[date_record_name] >= str(start_year) + '-01-01') & (station_df[date_record_name] <= str(end_year) + '-12-31')]  # Filter per date range
    # station_df1.reset_index()
    ideam_regs_query = station_df1.shape[0]
    print_log('\n\n### Analysis from %d to %d for %s: %i (%s%%)' % (start_year, end_year, parameter_name, ideam_regs_query, str(round((ideam_regs_query / ideam_regs) * 100, 2))))
    # print_log('\n\n### Analysis from %d to %d for %s (%s): %i (%s%%)' % (start_year, end_year, station_df1[tag_desc_name][0], parameter_name, ideam_regs_query,str(round((ideam_regs_query / ideam_regs) * 100, 2))))
    pivot_file = 'Pivot_' + parameter + '.csv'
    corr_file = 'Pivot_' + parameter + '_Correlation.csv'
    print_log('\nPivot table: [%s](%s)' % (pivot_file, pivot_file))
    fig_name = 'Plot_' + parameter + '_TimeSerie.png'
    print_log('![R.LTWB](Graph/%s)' % fig_name, center_div=False)
    fig_name = 'Plot_' + parameter + '_DensityKDE.png'
    print_log('![R.LTWB](Graph/%s)' % fig_name, center_div=False)

    # Data analysis per station
    station_df1.set_index(date_record_name, inplace=True)
    station_list = station_df1[station_code].unique()
    for station in station_list:
        station_filter = station_code + ' == "' + station + '"'
        df = station_df1.query(station_filter)
        # df.set_index(date_record_name, inplace=True)  # Already indexed in station_df1
        map_location = ('Location over [Google Maps](http://maps.google.com/maps?q=' + str(df[latitude_name][0]) + ',' + str(
            df[longitude_name][0]) + ') or [Openstreet Map](https://www.openstreetmap.org/query?lat=' + str(df[latitude_name][0]) + '&lon=' + str(
            df[longitude_name][0]) + ')')
        print_log('\n\n**%s - Station: %s (%s rec.)**<br>%s' % (parameter, df[station_name][0], df.shape[0], map_location), center_div=True)
        print_log('\nStation first record\n')
        print_log(df.head(1).to_markdown())
        print_log('Statistics table', center_div=True)
        print_log(df[value_name].describe().to_markdown(), center_div=True)
        fig = df.plot(y=value_name, figsize=(fig_size, fig_size+1), rot=90, colormap=plot_colormap, legend=False, alpha=1, lw=1)
        fig.set_ylabel(value_name)
        plt.title('Time serie for %s - Station %s (%d records)' % (parameter, station, df.shape[0]), fontsize=10)
        fig_name = 'Plot_' + parameter + '_' + station + '_TimeSerie.png'
        plt.savefig(path + 'Graph/' + fig_name)
        print_log('\n![R.LTWB](Graph/%s)' % fig_name, center_div=False)
        plt.close('all')  # After the fig is saved, close the fig release memory and clean the plot
        fig = df.boxplot(column=value_name, figsize=(fig_size, fig_size+1), grid=False)
        plt.title('Boxplot for %s - Station %s (%d records)' % (parameter, station, df.shape[0]), fontsize=10)
        fig_name = 'Plot_' + parameter + '_' + station + '_Boxplot.png'
        plt.savefig(path + 'Graph/' + fig_name)
        print_log('![R.LTWB](Graph/%s)' % fig_name, center_div=False)
        plt.close('all')
        fig = df.plot.hist(column=value_name, bins=histogram_binds, alpha=0.9, figsize=(fig_size, fig_size+1), colormap=plot_colormap, edgecolor='white', legend=False)
        plt.title('Histogram for %s - Station %s (%d records)' % (parameter, station, df.shape[0]), fontsize=10)
        fig_name = 'Plot_' + parameter + '_' + station + '_Histogram.png'
        plt.savefig(path + 'Graph/' + fig_name)
        print_log('![R.LTWB](Graph/%s)' % fig_name, center_div=False)
        plt.close('all')  # After the fig is saved, close the fig release memory
        fig = df[value_name].plot.kde(colormap=plot_colormap, figsize=(fig_size, fig_size+1))
        plt.title('KDE density for %s - Station %s (%d rec.)' % (parameter, station, df.shape[0]), fontsize=10)
        fig_name = 'Plot_' + parameter + '_' + station + '_DensityKDE.png'
        plt.savefig(path + 'Graph/' + fig_name)
        print_log('![R.LTWB](Graph/%s)' % fig_name, center_div=False)
        plt.close('all')

    # Pivot table, plot, describe and correlations
    print_log('\n\n#### Pivot table statistics and correlation analysis for %s' % parameter)
    pivot_table = station_df1.pivot_table(index=date_record_name, columns=station_code, values=value_name)
    pivot_table.to_csv(path + pivot_file)
    pivot_table.corr().to_csv(path + corr_file)
    print_log('\nGeneral statistics table', center_div=False)
    print_log(pivot_table.describe().to_markdown(), center_div=False)
    print_log('\nCorrelation matrix [%s](%s)' % (corr_file, corr_file), center_div=False)
    print_log(pivot_table.corr().to_markdown())
    print_log('\nCorrelation statistics table', center_div=False)
    print_log(pivot_table.corr().describe().to_markdown(), center_div=False)
    fig = pivot_table.plot(figsize=(fig_size*2, fig_size+1), rot=90, colormap=plot_colormap, legend=False, alpha=0.5, lw=1)
    fig.set_ylabel(value_name)
    plt.title('Time series for %s with %d stations (%d rec.)' % (parameter, len(station_list), ideam_regs_query), fontsize=10)
    plt.savefig(path + 'Graph/Plot_' + parameter + '_TimeSerie.png')
    fig = pivot_table.plot.kde(colormap=plot_colormap, figsize=(fig_size*2, fig_size+1), legend=False)
    plt.title('KDE density for %s with %d stations (%d rec.)' % (parameter, len(station_list), ideam_regs_query), fontsize=10)
    plt.savefig(path + 'Graph/Plot_' + parameter + '_DensityKDE.png')
    plt.close('all')
    # Plot correlations in heatmap style
    plt.figure(figsize=(fig_size*3, fig_size*3))
    plt.imshow(pivot_table.corr(), cmap=plot_colormap)
    plt.colorbar()
    plt.xticks(range(len(pivot_table.corr())), pivot_table.corr().columns)
    plt.yticks(range(len(pivot_table.corr())), pivot_table.corr().index)
    plt.xticks(rotation=90)
    plt.title('Correlations for %s with %d stations (%d rec.)' % (parameter, len(station_list), ideam_regs_query), fontsize=10)
    plt.savefig(path + 'Graph/Plot_' + parameter + '_Correlation.png')
    fig_name = 'Plot_' + parameter + '_Correlation.png'
    print_log('\n![R.LTWB](Graph/%s)' % fig_name, center_div=False)
    # plt.show()
    plt.close('all')
'''



# Complementary references
# https://stackoverflow.com/questions/41303246/error-tokenizing-data-c-error-out-of-memory-pandas-python-large-file-csv
# https://www.statology.org/pandas-read-csv-only-specific-rows/
# https://stackoverflow.com/questions/55285217/pandas-how-to-read-specific-rows-from-a-csv-file
# https://www.kdnuggets.com/2021/03/pandas-big-data-better-options.html
# -*- coding: UTF-8 -*-
# Name: Impute.py
# Description: impute missing values in time series through statistical methods
# Requirements: Python 3+, pandas, tabulate, numpy, missingno, scikit-learn
# Attention: do not convert the .csv file into an Excel file because you would need process more than 1048576 records.


# Libraries
import sys
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import missingno as msno
import sklearn
from sklearn.impute import KNNImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn import linear_model
import tabulate  # required for print tables in Markdown using pandas
from datetime import datetime


# General variables
pivot_table_name = 'Pivot_PTPM_TT_M_only15.csv'  # <<<<< Pivot table name to process
path_input = 'D:/R.GISPython/Impute/Input/'  # Current location from pivot tables
station_file = path_input + pivot_table_name  # Current pivot IDEAM records file for a specified parameter
path = 'D:/R.GISPython/Impute/Output/'  # Your local output path, use ../.datasets/IDEAM_Impute/ for relative path
file_log_name = path + 'Impute_' + pivot_table_name + '.md'  # Markdown file log
file_log = open(file_log_name, 'w+')   # w+ create the file if it doesn't exist
station_file_log_name = path + 'Impute_Station_' + pivot_table_name + '.md'  # Markdown file log
date_record_name = 'Fecha'  # IDEAM date field name for the record values
plot_colormap = 'autumn'  # Color theme for plot graphics, https://matplotlib.org/stable/tutorials/colors/colormaps.html
sample_records = 3  # Records to show in the sample table head and tail
fig_size = 5  # Height size for figures plot
fig_alpha = 0.75  # Alpha transparency color in plots
print_table_sample = True
show_plot = False
plot_stations = True  # True: plot individual graphs for each station and update the complementary report
min_value = 0  # Minimum value for impute with Multivariate Imputation by Chained Equation - MICE from Scikit Learn. E.g.: 0 for rain, -inf for temperature.
n_neighbors = 4  # Number of natural neighbors for Natural Neigborns - KNN & Multivariate Imputation by Chained Equation - MICE
halflife = 3  # Number of values for the Exponential (Weighted) Moving Average - EWM
only_included = False  # True: let the user run this script only for the stations included in the station_include array. False: process all the stations but not the ones in the station_exclude array.
station_include = ['15015020', '15060050', '15060070', '15060080', '15060150']  # Use ['station1', 'station2', '...',]
station_exclude = ['28017140', '25027020', '25027410', '25027490', '25027330', '25027390', '25027630', '25027360', '25027320', '16067010', '25027420']  # Use ['station1', 'station2', '...',]


# Function for print and show results in a file
def print_log(txt_print, on_screen=True, center_div=False):
    if on_screen:
        print(txt_print)
    if center_div:
        file_log.write('\n<div align="center">\n' + '\n')
    file_log.write(txt_print + '\n')
    if center_div:
        file_log.write('\n</div>\n' + '\n')

# Function for plot original and imputed series
def plot_impute(df_org, df_imputed, method, file_name):
    ax1 = df_imputed.plot(color='black', legend=False, alpha=1, figsize=(fig_size*2, fig_size+1), linewidth=0.5)
    df_org.plot(ax=ax1, colormap=plot_colormap, alpha=fig_alpha, legend=False, figsize=(fig_size*2, fig_size+1), linewidth=0.85)
    plt.title('Impute with %s values for %d stations (%d missing & %d imputed)' % (method, df.shape[1], total_nulls, total_imputed))
    ax1.set_ylabel('Values in %s (%d recs.)' % (pivot_table_name, ideam_regs))
    plt.savefig(path + file_name + '.png')
    print_log('\n![R.LTWB](%s)' % (file_name + '.png'), center_div=False)
    if show_plot: plt.show()
    plt.close('all')
    # Missingno plot
    # msno.matrix(df_impute, fontsize=20, figsize=(fig_size * 4, fig_size * 2.5))
    msno.matrix(df_imputed, figsize=(fig_size * 3, fig_size * 2.5))
    plt.title('Missing values diagram for %d stations (%d missing values & %d imputed with %s)' % (df.shape[1], total_nulls, total_imputed, method))
    plt.savefig(path + 'Missingno_' + file_name + '.png')
    print_log('\n![R.LTWB](%s)' % ('Missingno_' + file_name + '.png'), center_div=False)
    if show_plot: plt.show()
    plt.close('all')
    # Plot individual graphs for station
    column_headers = df.columns.values.tolist()
    if plot_stations:
        for station in column_headers:
            ax2 = df_imputed[station].plot(color='black', legend=True, alpha=1, figsize=(fig_size, fig_size), linewidth=0.5, style='.-', markersize=3)
            df_org[station].plot(ax=ax2, colormap=plot_colormap, alpha=1, legend=True, figsize=(fig_size, fig_size), linewidth=0.85, style='.-', markersize=3)
            ax2.legend(['Imputed', 'Value']);
            # plt.legend('', frameon=False)  # Remove legend
            plt.title('%s - Station %s' % (method, station))
            ax2.set_ylabel('Values in %s (%d recs.)' % (pivot_table_name, ideam_regs))
            plt.savefig(path + 'Graph/' + station + '_' + file_name + '.png')
            plt.close('all')


# Header
print_log('# Impute missing values in time series through statistical methods')
print_log('\n* Processed file: [%s](%s)' % (str(station_file), '../IDEAM_Outlier/' + pivot_table_name) +
          '\n* Execution date: ' + str(datetime.now()) +
          '\n* Python version: ' + str(sys.version) +
          '\n* Python path: ' + str(sys.path[0:5]) +
          '\n* matplotlib version: ' + str(matplotlib.__version__) +
          '\n* pandas version: ' + str(pd.__version__) +
          '\n* numpy version: ' + str(np.__version__) +
          '\n* missingno version: ' + str(msno.__version__) +
          '\n* sklearn version: ' + str(sklearn.__version__) +
          '\n* Stations exclude: ' + str(station_exclude) +
          '\n* Stations include: ' + str(station_include) +
          '\n* Print table sample: ' + str(print_table_sample) +
          '\n* Instructions & script: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/Impute'
          '\n* License: https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md'
          '\n* Credits: r.cfdtools@gmail.com')


# Open the IDEAM station pivot dataframe and show general information
df = pd.read_csv(station_file, low_memory=False, parse_dates=[date_record_name], index_col=date_record_name)
if only_included:
    df = df.loc[:, df.columns.isin(station_include)]
else:
    df = df.loc[:, ~df.columns.isin(station_exclude)]
ideam_regs = df.shape[0]
print_log('\n\n## General dataframe information with %d IDEAM records for %d stations' % (ideam_regs, df.shape[1]))
print(df.info())
if print_table_sample:
    print_log('\nDataframe records head sample\n')
    print_log(df.head(sample_records).to_markdown())
    print_log('\nDataframe records tail sample\n')
    print_log(df.tail(sample_records).to_markdown())
print_log('\nDatatypes for station and nulls values in the initial file', center_div=False)
df_dtypes = pd.DataFrame(df.dtypes, columns=['Dtype'])
df_isnull = pd.DataFrame(df.isnull().sum(), columns=['Nulls'])
df_concat = pd.concat([df_dtypes, df_isnull], axis='columns').T  # .T for transpose
print_log(df_concat.to_markdown(), center_div=False)
total_nulls = df_concat.T['Nulls'].sum()
#print_log('\nTotal nulls values founded in the dataset: %d\n' % total_nulls, center_div=False)
#nul_data = pd.DataFrame(df.isnull())
#print_log(nul_data.to_markdown())
ax = df.plot(colormap=plot_colormap, legend=False, alpha=fig_alpha, figsize=(fig_size*2, fig_size+1), linewidth=0.85)  # colormap can be replaced by color='lightblue'
plt.title('Original serie with %d stations (%d missing values)' % (df.shape[1], total_nulls))
ax.set_ylabel('Values in %s (%d recs.)' % (pivot_table_name, ideam_regs))
plt.savefig(path + pivot_table_name + '.png')
print_log('\n![R.LTWB](%s)' % (pivot_table_name + '.png'), center_div=False)
if show_plot: plt.show()
plt.close('all')
# Missingno plot
msno.matrix(df, fontsize=16, figsize=(fig_size*3, fig_size*2.5))
plt.title('Missing values diagram for %d stations (%d missing values)' % (df.shape[1], total_nulls))
ax.set_ylabel('Records')
plt.savefig(path + 'Missingno_' + pivot_table_name + '.png')
print_log('\n![R.LTWB](%s)' % ('Missingno_' + pivot_table_name + '.png'), center_div=False)
if show_plot: plt.show()
plt.close('all')
# General stats
print_log('General statistics table - Initial file', center_div=True)
print_log(df.describe().T.to_markdown(), center_div=True)  # .T for transpose


# Method 1 - Impute missing values with mean values
df_impute = df.fillna(df.mean())
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
impute_file = 'Impute_Mean_' + pivot_table_name
df_impute.index.name = date_record_name
df_impute.to_csv(path + impute_file)
print_log('\n\n## Method 1 - Imputing with mean values' +
          '\nAccording to this technique, the missing values are imputed using the mean value in each feature and the serie has been completed filled.' +
          '\n\nImputed file: [%s](%s)' % (impute_file, impute_file))
plot_impute(df, df_impute, 'MEAN', impute_file)
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True)  # .T for transpose

# Method 2 - Impute missing values with median values
df_impute = df.fillna(df.median())
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
imputed_file = 'Impute_Median_' + pivot_table_name
df_impute.index.name = date_record_name
df_impute.to_csv(path + imputed_file)
print_log('\n\n## Method 2 - Imputing with median values' +
          '\nAccording to this technique, the missing values are imputed using the median value in each feature and the serie has been completed filled.' +
          '\n\nImputed file: [%s](%s)' % (imputed_file, imputed_file))
plot_impute(df, df_impute, 'MEDIAN', imputed_file)
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True)  # .T for transpose

# Method 3 - Impute missing values with Last Observation Carried Forward (LOCF)
df_impute = df.fillna(method='ffill')
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
imputed_file = 'Impute_LOCF_' + pivot_table_name
df_impute.index.name = date_record_name
df_impute.to_csv(path + imputed_file)
print_log('\n\n## Method 3 - Imputing with Last Observation Carried Forward (LOCF) values' +
          '\nAccording to this technique, the missing values are imputed using the immediate values before it in the time series and the missing values at the start are not filled but the series are completed fillet to the end.' +
          '\n\nImputed file: [%s](%s)' % (imputed_file, imputed_file))
plot_impute(df, df_impute, 'LOCF', imputed_file)
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True)  # .T for transpose

# Method 4 - Impute missing values with Next Observation Carried Backward (NOCB)
df_impute = df.fillna(method='bfill')
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
imputed_file = 'Impute_NOCB_' + pivot_table_name
df_impute.index.name = date_record_name
df_impute.to_csv(path + imputed_file)
print_log('\n\n## Method 4 - Imputing with Next Observation Carried Backward (NOCB) values' +
          '\nAccording to this technique, the missing values are imputed using the immediate values after it in the time series and the missing values at the end are not filled but the series are completed fillet to the start.' +
          '\n\nImputed file: [%s](%s)' % (imputed_file, imputed_file))
plot_impute(df, df_impute, 'NOCB', imputed_file)
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True)  # .T for transpose

# Method 5 - Impute missing values with Linear Interpolation
df_impute = df.interpolate(method='linear')  # limit=1, limit_direction="forward"
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
imputed_file = 'Impute_InterpolateLinear_' + pivot_table_name
df_impute.index.name = date_record_name
df_impute.to_csv(path + imputed_file)
print_log('\n\n## Method 5 - Impute missing values with Linear Interpolation values' +
          '\nAccording to this technique, the missing values are imputed using the linear interpolation between knowing pair values in the time series and the missing values at the start are not filled but the series are completed fillet to the end.' +
          '\n\nImputed file: [%s](%s)' % (imputed_file, imputed_file))
plot_impute(df, df_impute, 'Linear Interpolation', imputed_file)
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True)  # .T for transpose

# Method 6 - Impute missing values with Exponential (Weighted) Moving Average - EWM
df_impute = df.fillna(df.ewm(halflife=halflife).mean())
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
imputed_file = 'Impute_MeanEWM_' + pivot_table_name
df_impute.index.name = date_record_name
df_impute.to_csv(path + imputed_file)
print_log('\n\n## Method 6 - Impute missing values with Exponential (Weighted) Moving Average - EWM = %d' % halflife +
          '\nAccording to this technique, the missing values are imputed using the moving average values in the time series and the missing values at the start are not filled but the series are completed fillet to the end.' +
          '\n\nImputed file: [%s](%s)' % (imputed_file, imputed_file))
plot_impute(df, df_impute, 'Exponential Weighted Moving - EWM', imputed_file)
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True)  # .T for transpose

# Method 7 - Impute missing values with Natural Neigborns - KNN Imputer from Scikit Learn
#imputer = KNNImputer(n_neighbors=n_neighbors)
imputer = KNNImputer(n_neighbors=n_neighbors, weights='uniform', metric='nan_euclidean')
column_headers = df.columns.values.tolist()
index_list = list(df.index.values)
df_impute = imputer.fit_transform(df)
df_impute = pd.DataFrame(df_impute, columns=column_headers, index=index_list) # Convert numpy array to a pandas dataframe
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
imputed_file = 'Impute_KNN_' + pivot_table_name
df_impute.index.name = date_record_name
df_impute.to_csv(path + imputed_file)
print_log('\n\n## Method 7 - Impute missing values with Natural Neigborns - KNN = %d Imputer from Scikit Learn' % n_neighbors +
          '\nAccording to this technique, the missing values are imputed using the natural neighbors values and the serie has been completed filled. More information in https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html' +
          '\n\nImputer = KNNImputer(n_neighbors=n_neighbors, weights=uniform, metric=nan_euclidean)' +
          '\n\nImputed file: [%s](%s)' % (imputed_file, imputed_file))
plot_impute(df, df_impute, 'KNN Imputer', imputed_file)
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True)  # .T for transpose

# Method 8 - Impute missing values with Multivariate Imputation by Chained Equation - MICE from Scikit Learn
imputer = IterativeImputer(estimator=linear_model.BayesianRidge(), n_nearest_features=n_neighbors, initial_strategy='mean', min_value=min_value, imputation_order='ascending')
column_headers = df.columns.values.tolist()
index_list = list(df.index.values)
df_impute = imputer.fit_transform(df)
df_impute = pd.DataFrame(df_impute, columns=column_headers, index=index_list) # Convert numpy array to a pandas dataframe
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
imputed_file = 'Impute_MICE_' + pivot_table_name
df_impute.index.name = date_record_name
df_impute.to_csv(path + imputed_file)
print_log('\n\n## Method 8 - Impute missing values with Multivariate Imputation by Chained Equation - MICE from Scikit Learn' +
          '\nAccording to this technique, the missing values are imputed using MICE values and the serie has been completed filled. More information in https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html' +
          '\n\nImputer = %s' % str(imputer) +
          '\n\nImputed file: [%s](%s)' % (imputed_file, imputed_file))
plot_impute(df, df_impute, 'MICE Imputer', imputed_file)
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True)  # .T for transpose
detailed_report = 'Impute_Station_' + pivot_table_name + '.md'
print_log('\nComplementary report with individual graphs for stations in [%s](%s)' % (detailed_report, detailed_report))

# Create a Markdown report with individual graphs for station
column_headers = df.columns.values.tolist()
if plot_stations:
    station_file_log = open(station_file_log_name, 'w+')  # w+ create the file if it doesn't exist
    station_file_log.write('# Impute missing values in time series through statistical methods - Complementary report' +
                           '\n* Processed file: [%s](%s)' % (
                           str(station_file), '../IDEAM_Outlier/' + pivot_table_name) +
                           '\n* Execution date: ' + str(datetime.now()) +
                           '\n* Instructions & script: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/Impute'
                           '\n* License: https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md'
                           '\n* Credits: r.cfdtools@gmail.com')
    for station in column_headers:
        station_file_log.write('\n\n## Station: ' + station + '\n\n![R.LTWB](Graph/' + station + '_Impute_Mean_' + pivot_table_name + '.png)' +
                               '![R.LTWB](Graph/' + station + '_Impute_Median_' + pivot_table_name + '.png)' +
                               '![R.LTWB](Graph/' + station + '_Impute_LOCF_' + pivot_table_name + '.png)' +
                               '![R.LTWB](Graph/' + station + '_Impute_NOCB_' + pivot_table_name + '.png)' +
                               '![R.LTWB](Graph/' + station + '_Impute_InterpolateLinear_' + pivot_table_name + '.png)' +
                               '![R.LTWB](Graph/' + station + '_Impute_MeanEWM_' + pivot_table_name + '.png)' +
                               '![R.LTWB](Graph/' + station + '_Impute_KNN_' + pivot_table_name + '.png)' +
                               '![R.LTWB](Graph/' + station + '_Impute_MICE_' + pivot_table_name + '.png)')

# Comments
print_log('\n> As you notice, some of the techniques showed above can`t fill complete the missing values at the start or at the end, however, you can first choice a method and then apply another complementary method for get full filled the missin values.')


# References
# https://www.geeksforgeeks.org/how-to-plot-a-time-series-in-matplotlib/
# https://www.statology.org/remove-legend-matplotlib/
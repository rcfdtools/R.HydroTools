# -*- coding: UTF-8 -*-

# General libraries
from numpy.ma.core import minimum
import platform
import scipy
import functions as funcs
import dictionary as dictionary
import warnings
from pathlib import Path
import tabulate # required for print tables in Markdown using pandas
import numpy as np
import pandas as pd
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# General setup
app_version = 'v20260106'
input_path = 'dataset/pmax24h_in/' # Your local input file folder
output_path = 'dataset/pmax24h_out/' # Your local output file folder
station_dataset_file = input_path + 'conventional_cesarcolombia_1959_2022.csv' # Stations dataset ●
date_min = 1900 # Minimum year to eval til year_max ●
date_max = 2024 # Maximum year to eval since year_min ●
label_station = 'Station' # Station column name to eval from .csv station dataset file
label_x = 'Value' # Value column name to eval from .csv station file
label_date = 'Date' # Date column name from .csv station file
show_warnings = False # Show warnings on screen
low_extreme = False # Eval low extreme values, if False, evaluates high extreme values
pdist_logarithmic_on = True # Eval every SciPy distribution as logarithmic
if not show_warnings:
    warnings.filterwarnings('ignore')
minimum_sample = 5 # Exclude a station when doesn't have the minimum data sample (0 means any) ●
zscore_max = 3.5 # Z-Score maximum threshold to adjust a value, 0 means disable ●
zscore_min= -2.5 # Z-Score minimum threshold to adjust a value, 0 means disable ●
avoid_zeros = True # Exclude dataframe zeros, e.g. rain = 0
avoid_nans = True # Exclude null values


# Return periods and probabilities
tr = [2, 2.33, 5, 10, 15, 20, 25, 50, 75, 100, 200, 250, 500, 750, 1000]  # Tr, return period in years
#tr = [100]  # Tr, return period in years
df_tr = pd.DataFrame(tr, columns=['tr'])
df_tr['prob_l'] = 1-1/df_tr.tr  # P≤, Probability less than, for high extreme values
df_tr['prob_g'] = 1/df_tr.tr  # P≥, Probability greater than, for low extreme values
df_l_pdist_scipy = pd.DataFrame(funcs.l_pdist_scipy_extreme, columns=['p_dist', 'n_parameter', 'fit_method', 'label', 'active'])
df_l_pdist_scipy_inactive = df_l_pdist_scipy.query('active == False')
df_l_pdist_scipy = df_l_pdist_scipy.query('active == True')
df_l_pdist_scipy = df_l_pdist_scipy.sort_values(by=['p_dist'], ascending=True)
df_l_pdist_scipy = df_l_pdist_scipy.reset_index(drop=True)
df_l_pdist_scipy.index.name = 'id'


# Initial dataset filtering and cleaning
df_all = pd.read_csv(station_dataset_file, delimiter=',', parse_dates=True, dtype={label_station: 'str'})  # index_col=0
df_all = df_all[(df_all[label_date] >= date_min) & (df_all[label_date] <= date_max)] # Filter the required date range. &=and, |=or.
if avoid_zeros:
    df_all = df_all[df_all[label_x] != 0]
if avoid_nans:
    df_all = df_all.dropna(subset=[label_station, label_x, label_date])
df_all_stats = df_all.groupby(label_station)[label_x].agg(['count', 'mean', 'std']).reset_index()
#print(df_all_stats.to_markdown())
df_all_stats_join = pd.merge(df_all, df_all_stats, on=label_station, how='inner')
df_all_stats_join['zscore'] = (df_all_stats_join[label_x]-df_all_stats_join['mean'])/df_all_stats_join['std']
df_all = df_all_stats_join
df_all[f'{label_x}_initial'] = df_all_stats_join[label_x]
if zscore_max > 0:
    df_all[label_x] = np.where(df_all['zscore'] > zscore_max, df_all['mean'], df_all[label_x])
if zscore_min < 0:
    df_all[label_x] = np.where(df_all['zscore'] < zscore_min, df_all['mean'], df_all[label_x])
#print(df_all.to_markdown())
if minimum_sample > 0:
    df_all = df_all[df_all['count'] >= minimum_sample]


# Execution
stations = df_all[label_station].unique()
print(f'Stations in dataset: {stations}')
for station in stations:
    print(f'\n>>>>>>>>>>>>>>>>>>>> Station: {station} <<<<<<<<<<<<<<<<<<<<<<<<<\n')
    station_code = str(station)
    df = df_all[df_all[label_station] == station]
    df = df.sort_values(by=label_date)
    df = df.reset_index(drop=True)
    df.index.name = 'id'
    x = label_x
    date = label_date
    df = df.dropna()
    df = df.sort_values(by=x, ascending=True)
    df = df.reset_index(drop=True)
    df.index.name = 'id'
    df['station'] = station_code
    df['m'] = df.index+1
    df = df.rename(columns={x: 'x', date: 'date'})
    x = 'x'  # New value column name
    date = 'date'  # New date column name
    vDeltaKolmogorov = pd.DataFrame(columns=['station', 'empirical_dist', 'p_dist', 'delta', 'deltao', 'eval', 'fit', 'n', 'loc', 'scale', 'shape', 'shape1', 'shape2', 'shape3'])

    # CDF calculations
    dp_evaluated = 0 # cdf to eval
    for i in range(0, len(df_l_pdist_scipy)):
        print(f'Processing CDF: {df_l_pdist_scipy['p_dist'][i]}')  # Only for console
        dp_evaluated += 1
        try:
            funcs.pdist_scipy(df, df_l_pdist_scipy['p_dist'][i], df_l_pdist_scipy['n_parameter'][i], df_l_pdist_scipy['fit_method'][i], df_l_pdist_scipy['label'][i], x, low_extreme, df_tr, station_code, vDeltaKolmogorov)
        except ZeroDivisionError:
            # Handle a specific error and skip to the next iteration
            print(f"Processing CDF: Cannot divide by zero. Skipping.")
            continue
        except TypeError:
            # Handle another specific error and do nothing (pass)
            print(f"Processing CDF: Cannot perform operation on non-number. Continuing.")
            pass
        except Exception as e:
            # Catch any other general exception, print it, and continue
            print(f"Processing CDF: An unexpected error occurred:. Continuing.")
            continue
    if pdist_logarithmic_on: ########### logarithmic #############
        for i in range(0, len(df_l_pdist_scipy)):
            print(f'Processing LogCDF: {df_l_pdist_scipy['p_dist'][i]}')  # Only for console
            dp_evaluated += 1
            try:
                funcs.pdist_scipy_log(df, df_l_pdist_scipy['p_dist'][i], df_l_pdist_scipy['n_parameter'][i], df_l_pdist_scipy['fit_method'][i], df_l_pdist_scipy['label'][i], x, low_extreme, df_tr, station_code, vDeltaKolmogorov)
            except ZeroDivisionError:
                # Handle a specific error and skip to the next iteration
                print(f"\nProcessing LogCDF: Cannot divide by zero. Skipping.")
                continue
            except TypeError:
                # Handle another specific error and do nothing (pass)
                print(f"Processing LogCDF: Cannot perform operation on non-number. Continuing.")
                pass
            except Exception as e:
                # Catch any other general exception, print it, and continue
                print(f"Processing LogCDF: An unexpected error occurred:. Continuing.")
                continue
    #print(f'\n{vDeltaKolmogorov.to_markdown()}')
    df_tr['station'] = station_code
    df_tr['n'] = len(df)
    df_tr['risk_rate'] = 1-(1-1/df_tr['tr'])**df_tr['tr']
    df_tr = df_tr.reset_index(drop=True)
    df_tr.index.name = 'id'
    # print(f'\n{df_tr.to_markdown()}')
    df_tr.to_csv(f'{output_path}table/extreme_{station_code}.csv', index=False)

print(f'\nStations in dataset: {stations}\n')
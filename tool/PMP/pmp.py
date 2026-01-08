# -*- coding: UTF-8 -*-
# Tested with: Python 3.10, SciPy 1.11.3, NumPy 1.26.1, Pandas 2.1.3, xlrd
from numpy.ma.core import minimum

# General libraries
import platform
import scipy
import functions as funcs
import dictionary as dictionary
import warnings
from pathlib import Path
import matplotlib.pyplot as plt
plt.style.use('grayscale')
from matplotlib.pyplot import figure
from matplotlib.ticker import MaxNLocator
import tabulate # required for print tables in Markdown using pandas
import numpy as np
import pandas as pd
pd.set_option('display.max_colwidth', None)
from datetime import datetime
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# General setup
app_version = 'v20260108'
input_path = 'dataset/pmax24h_in/' # Your local input file folder
output_path = 'dataset/pmax24h_out/' # Your local output file folder
station_dataset_file = input_path + 'automatic_test.csv' # Stations dataset ●
station_catalog_file = 'dataset/CNE.xls' # CNE catalog for stations info
station_catalog_columns_drop = ['OBSERVACION', 'SUBRED'] # Dropped columns from CNE
parameter_name = 'Rain, Pmax24h' # rain, flow
parameter_units = '($mm/d$)' # ($mm/d$), ($m^3/s$)
parameter_title = 'PMP' # Probable Maximum Precipitation (PMP) or Probable Maximum Flood (PMF)
date_min = 1900 # Minimum year to eval til year_max ●
date_max = 2024 # Maximum year to eval since year_min ●
label_station = 'Station' # Station column name to eval from .csv station dataset file
label_x = 'Value' # Value column name to eval from .csv station file
label_date = 'Date' # Date column name from .csv station file
label_station_catalog = 'CODIGO' # Station column code in CNE_IDEAM.xls
label_latitude = 'LATITUD' # Station column latitude in CNE_IDEAM.xls
label_longitude = 'LONGITUD' # Station column longitude in CNE_IDEAM.xls
create_plot = True # Creates, save and include plots into reports ●
plot_only_simple = False # Plot only simple graphs avoiding multiple CDF and multiple Extreme values plots  ●
show_plot = False # Show plot on Python screen console
plot_only_fit = True # Plot only fit distributions with Δo > Δ
plot_rounding_val = 6 # Rounding values in plots to # decimal positions
print_on_screen = False # Global print control in screen
color_plot = 'black' # Global plot color
dpi = 96 # Graph plot resolution
show_warnings = False # Show warnings on screen
low_extreme = False # Eval low extreme values, if False, evaluates high extreme values
pdist_logarithmic_on = True # Eval every SciPy distribution as logarithmic
if not show_warnings:
    warnings.filterwarnings('ignore')
plot_legend_ncol = 3 # Columns on plot legend, '' for autofit
ddof = 1.00 # Standard deviation normalized
runtime = datetime.now()
minimum_sample = 5 # Exclude a station when doesn't have the minimum data sample (0 means any) ●
zscore_max = 3.5 # Z-Score maximum threshold to adjust a value, 0 means disable ●
zscore_min= -2.5 # Z-Score minimum threshold to adjust a value, 0 means disable ●
avoid_zeros = True # Exclude dataframe zeros, e.g. rain = 0
avoid_nans = True # Exclude null values
python_version = platform.python_version()
scipy_version = scipy.__version__
pandas_version = pd.__version__
numpy_version = np.__version__


# Return periods and probabilities
#tr = [2.33, 5, 10, 25, 50, 100]  # Tr, return period in years
tr = [2, 2.33, 5, 10, 15, 20, 25, 50, 75, 100, 200, 250, 500, 750, 1000]  # Tr, return period in years
df_tr = pd.DataFrame(tr, columns=['tr'])
n_tr = len(df_tr)
df_tr['prob_l'] = 1-1/df_tr.tr  # P≤, Probability less than, for high extreme values
df_tr['prob_g'] = 1/df_tr.tr  # P≥, Probability greater than, for low extreme values
df_l_pdist_scipy = pd.DataFrame(funcs.l_pdist_scipy, columns=['p_dist', 'n_parameter', 'fit_method', 'label', 'active'])
df_l_pdist_scipy['ref'] = '[:mortar_board:](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.'+df_l_pdist_scipy.p_dist+'.html)'
df_l_pdist_scipy_inactive = df_l_pdist_scipy.query('active == False')
df_l_pdist_scipy = df_l_pdist_scipy.query('active == True')
df_l_pdist_scipy = df_l_pdist_scipy.sort_values(by=['p_dist'], ascending=True)
df_l_pdist_scipy = df_l_pdist_scipy.reset_index(drop=True)
df_l_pdist_scipy.index.name = 'id'
df_edf_dist_dict = pd.DataFrame(dictionary.edf_dist_dict, columns=['edf_dist', 'edf_name', 'edf_expression', 'edf_year', 'edf_desc'])
edf_dist = df_edf_dist_dict['edf_dist'].unique()


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
print(f'Stations in dataset ({len(stations)})\n{stations}\n')
data_types = {label_station_catalog: 'str', label_latitude: 'float64', label_longitude: 'float64'}
df_catalog = pd.read_excel(station_catalog_file, sheet_name='CNE', parse_dates=True, dtype=data_types) # , dtype=data_types
df_catalog = df_catalog.drop(columns=station_catalog_columns_drop)
# print(df_catalog.dtypes)
for station in stations:
    print(f'\n>>>>>>>>>>>>>>>>>>>> Station: {station} <<<<<<<<<<<<<<<<<<<<<<<<<\n\n')
    station_code = str(station)
    fig_file0a = 'graph/' + station_code + '_locationmap.png'
    fig_file0 = 'graph/' + station_code + '_dataserie.png'
    file_log_name = f'{output_path}{station_code}.md'  # Markdown file log
    file_log = open(file_log_name, 'w+', encoding='utf-8')   # w+ create the file if it doesn't exist
    df = df_all[df_all[label_station] == station]
    df = df.sort_values(by=label_date)
    df = df.reset_index(drop=True)
    df.index.name = 'id'
    df_station_info = df_catalog[df_catalog[label_station_catalog] == station]
    df_station_info = df_station_info.reset_index(drop=True)
    df_station_info.index.name = 'id'
    point_latitude = df_station_info[label_latitude][0]
    point_longitude = df_station_info[label_longitude][0]
    google_maps_url = f'http://maps.google.com/maps?q={point_latitude},{point_longitude}'
    openstreetmap_url = f'https://www.openstreetmap.org/#map=18/{point_latitude}/{point_longitude}&layers=P'
    bing_map_url = f'https://www.bing.com/maps?cp={point_latitude}~{point_longitude}&lvl=18'
    apple_map_url = f'https://maps.apple.com/frame?center={point_latitude}%2C{point_longitude}&span=0.003%2C0.006'
    funcs.print_log(file_log, '<img alt="R.HydroTools" src="../../../../file/graph/R.HydroTools.svg" width="250px">', center_div=True, on_screen = print_on_screen)
    funcs.print_log(file_log, f'# {parameter_title} Station ({parameter_name}): {station_code}', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n\n{dictionary.dicts['pmp']}\n', on_screen = print_on_screen)
    funcs.print_log(file_log, f'<img alt="R.HydroTools" src="{fig_file0a}" width="500"></img>', center_div=True, on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n## A. General information\n\n\n### 1. General running parameters\n\n', on_screen = print_on_screen)
    for dict_var in dictionary.general_vars:
        funcs.print_log(file_log, f'• {dict_var[1]}: _{eval(dict_var[0])}_. ', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n\n:file_folder:Table: [dataset.csv](../../{station_dataset_file})', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n\n> {dictionary.dicts['ddof']}', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n\n\n### 2. Station info and location\n\n{df_station_info.to_markdown()}\n', on_screen = print_on_screen)
    funcs.print_log(file_log, f'Dynamic map: [:earth_americas:Google]({google_maps_url}) [:earth_americas:OSM]({openstreetmap_url}) [:earth_americas:Bing]({bing_map_url}) [:earth_americas:Apple]({apple_map_url})', center_div=True, on_screen = print_on_screen)
    geojson = '```geojson\n{\n  "type": "Feature",\n  "geometry": {\n    "type": "Point", \n    "coordinates": ['+str(point_longitude)+', '+str(point_latitude)+']\n  }, \n  "properties": {\n    "Name": "'+station+'"\n  }\n}\n```'
    funcs.print_log(file_log, f'{geojson}', center_div=True, on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n### 3. Discrete values table and plot\n', on_screen = print_on_screen)
    funcs.print_log(file_log, f'{df[[label_date, label_x, f'{label_x}_initial', 'count', 'mean', 'std', 'zscore']].transpose().to_markdown()}\n', center_div=True, on_screen = print_on_screen)
    if create_plot: funcs.print_log(file_log, f'<img alt="R.HydroTools" src="{fig_file0}" width="600"></img>', center_div=True, on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n> {dictionary.dicts['value_initial']}\n', on_screen = print_on_screen)
    funcs.print_log(file_log, f'>\n> {dictionary.dicts['why_not_complete_or_extend_data']}\n', on_screen = print_on_screen)

    # Plot location map & Plot x values
    # Location map always (graph 0a)
    location_map_plot = funcs.location_map(point_latitude, point_longitude, station)
    location_map_plot.savefig(output_path + fig_file0a, dpi=dpi)
    plt.close()
    if create_plot:
        # Plot x values  (graph 0)
        #df = df.sort_values(by=label_date)
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.plot(df[label_date], df[f'{label_x}_initial'], color=color_plot, lw=0.5, marker='o', markersize=2, label='Original', linestyle='dashed')
        plt.plot(df[label_date], df[label_x], color=color_plot, lw=1.25, marker='o', markersize=3, label='Adjusted (Z-Score)')
        plt.grid(color='gray', linestyle='--', linewidth=0.1)
        plt.title('Data serie')  #$_{ } for underscript text
        plt.xlabel('Year')
        plt.ylabel(parameter_name + ' ' + parameter_units)
        plt.xticks(rotation=0, ha='center')
        plt.annotate(f'Station: {station_code}', xy=(0.99, 0.01), xycoords='axes fraction', ha='right', fontsize=9)
        plt.annotate('github.com/rcfdtools', xy=(1.0275, 0.01), xycoords='axes fraction', ha='right', va='bottom', rotation='vertical', fontsize=7.5)
        plt.legend(loc='best', frameon=False)
        if show_plot: plt.show()
        plt.savefig(output_path + fig_file0, dpi=dpi)
        ax.xaxis.set_major_locator(MaxNLocator(integer=False))
        plt.close()
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
    funcs.print_log(file_log, f'\n\n### 4. Active continuous probability distributions from SciPy ({len(df_l_pdist_scipy.query('active == True'))} of {len(funcs.l_pdist_scipy)} available)', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n\n{dictionary.dicts['pdf']}\n', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n{dictionary.dicts['log_pdf']}\n', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n{dictionary.dicts['scipy_stats']}\n', on_screen = print_on_screen)
    funcs.print_log(file_log, f'{df_l_pdist_scipy.query('active == True').to_markdown()}', center_div=True, on_screen = print_on_screen)
    funcs.print_log(file_log, '> **n_parameter:** # arguments & localization & scale.\n>\n> **Fit methods:** (MLE) maximum likelihood, (MM) L-moments.', on_screen = print_on_screen)
    funcs.print_log(file_log, (f'\n>\n>**Inactive** ({dictionary.dicts['disable_pdf']})**:** '), on_screen = print_on_screen)
    for inactives in df_l_pdist_scipy_inactive['p_dist'].values:
        funcs.print_log(file_log, (f'{inactives}, '), on_screen = print_on_screen)
    funcs.print_log(file_log, '\n\n\n## B. Probability (PDF) vs. Empirical (EDF) distributions functions', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n\n{dictionary.dicts['cpd']}\n', on_screen = print_on_screen)
    vDeltaKolmogorov = pd.DataFrame(columns=['station', 'empirical_dist', 'p_dist', 'delta', 'deltao', 'eval', 'fit', 'n', 'loc', 'scale', 'shape', 'shape1', 'shape2', 'shape3'])
    #vDeltaKolmogorov = pd.DataFrame(columns=['station', 'empirical_dist', 'p_dist', 'delta', 'deltao', 'eval', 'fit', 'n'])

    # CDF calculations
    dp_evaluated = 0 # cdf to eval
    for i in range(0, len(df_l_pdist_scipy)):
        print(f'Processing CDF: {df_l_pdist_scipy['p_dist'][i]}')  # Only for console
        dp_evaluated += 1
        funcs.pdist_scipy(df, df_l_pdist_scipy['p_dist'][i], df_l_pdist_scipy['n_parameter'][i], df_l_pdist_scipy['fit_method'][i], df_l_pdist_scipy['label'][i], x, low_extreme, df_tr, station_code, vDeltaKolmogorov)
    if pdist_logarithmic_on: ########### logarithmic #############
        for i in range(0, len(df_l_pdist_scipy)):
            print(f'Processing LogCDF: {df_l_pdist_scipy['p_dist'][i]}')  # Only for console
            dp_evaluated += 1
            funcs.pdist_scipy_log(df, df_l_pdist_scipy['p_dist'][i], df_l_pdist_scipy['n_parameter'][i], df_l_pdist_scipy['fit_method'][i], df_l_pdist_scipy['label'][i], x, low_extreme, df_tr, station_code, vDeltaKolmogorov)
    funcs.print_log(file_log, f'Distributions parameters from station values\n{vDeltaKolmogorov[['station', 'p_dist', 'n', 'loc', 'scale', 'shape', 'shape1', 'shape2', 'shape3']].to_markdown()}', center_div=True, on_screen = print_on_screen)
    #print(f'\n\n**Distributions parameters**\n{vDeltaKolmogorov.to_markdown()}')
    funcs.print_log(file_log, f'> {dictionary.dicts['loc']}', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n>\n> {dictionary.dicts['scale']}', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n>\n> {dictionary.dicts['shape']}', on_screen = print_on_screen)
    if pdist_logarithmic_on: dp_evaluated_txt = 'and calculating $log(f(x))$ separately'
    funcs.print_log(file_log, f'\n\n\n### 0. Cumulative distribution values - CDF ({dp_evaluated} evaluated)\n\n', on_screen = print_on_screen)
    funcs.print_log(file_log, f'{dictionary.dicts['cdf']}\n', on_screen = print_on_screen)
    funcs.print_log(file_log, f'CDF ordered by x ascending {dp_evaluated_txt}\n{df.to_markdown()}\n\n', center_div=True, on_screen = print_on_screen)

    # Evaluation for each empirical distribution function
    dp_best_of_best = pd.DataFrame()
    num_inc = 1
    funcs.print_log(file_log, f'{dictionary.dicts['edf']}\n\n', on_screen = print_on_screen)
    funcs.print_log(file_log, f'{dictionary.dicts['kolmogorov_smirnov_test']}\n\n', on_screen = print_on_screen)
    # idk = 0 ################ <<<<<<<<<<<<<<<<<<<<<<<< Check
    for emp in edf_dist:
        fig_file1 = 'graph/' + station_code + '_' + emp + '_all.png'
        fig_file2 = 'graph/' + station_code + '_' + emp + '_bestfit.png'
        fig_file3 = 'graph/' + station_code + '_' + emp + '_estimatedpdf.png'
        fig_file4 = 'graph/' + station_code + '_extremevalues.png'
        fig_file5 = 'graph/' + station_code + '_extremevalues_bestfit.png'
        fig_file6 = 'graph/' + station_code + '_extremevalues_riskrate.png'
        df_edf_dist_dict_filter = df_edf_dist_dict[df_edf_dist_dict['edf_dist'] == emp]
        funcs.print_log(file_log, f'\n### {num_inc}. {df_edf_dist_dict_filter['edf_name'].to_string(index=False, header=False)} ({df_edf_dist_dict_filter['edf_year'].to_string(index=False, header=False)})\n', on_screen = print_on_screen)
        funcs.print_log(file_log, f'\n{df_edf_dist_dict_filter['edf_desc'].to_string(index=False, header=False)}\n', on_screen = print_on_screen)
        funcs.print_log(file_log, f'\n${df_edf_dist_dict_filter['edf_expression'].to_string(index=False, header=False)}$\n', center_div=True, on_screen = print_on_screen)

        # Return periods & empirical values
        df_tr['empirical_dist'] = emp
        df_tr['station'] = station_code
        df_tr['n'] = len(df)
        df_tr['risk_rate'] = 1-(1-1/df_tr['tr'])**df_tr['tr']
        funcs.pdist_empirical(df, emp, x)

        # Kolmogorov-Smirnov test & best fit ################ <<<<<<<<<<<<<<<<<<<<<<<< Check
        idk = 0
        #vDeltaKolmogorov_filter = vDeltaKolmogorov[vDeltaKolmogorov['p_dist'].str.startswith('log', na=False)]
        #print(f'\n\nDataset df for Kolmogorov:\n{df.to_markdown()}')  ################ <<<<<<<<<<<<<<<<<<<<<<<< Check
        for i in df_l_pdist_scipy['p_dist']:
            funcs.fTestKolmogorov(df, i, idk, emp, vDeltaKolmogorov)
            idk += 1
        #vDeltaKolmogorov_filter = vDeltaKolmogorov[vDeltaKolmogorov['p_dist'].str.startswith('log', na=True)]
        #idk = 0
        if pdist_logarithmic_on: ########### logarithmic #############
            for i in df_l_pdist_scipy['p_dist']:
                funcs.fTestKolmogorov(df, f'log{i}', idk, emp, vDeltaKolmogorov)
                idk += 1
        vDeltaKolmogorov['best_fit'] = np.where((vDeltaKolmogorov['delta'] == vDeltaKolmogorov['delta'].min()), 1, 0)
        vDeltaKolmogorov = vDeltaKolmogorov.sort_values(by=['delta'], ascending=True)
        vDeltaKolmogorov = vDeltaKolmogorov.reset_index(drop=True)
        vDeltaKolmogorov.index.name = 'id'
        funcs.print_log(file_log, f'\n**{num_inc}.1. Empirical values**\n', on_screen = print_on_screen)
        funcs.print_log(file_log, (df[['date', 'x', 'm', 'empirical_dist', 'empirical', 'empirical_tr']].transpose().to_markdown()), center_div=True, on_screen = print_on_screen)
        vDeltaKolmogorov['best_fit_sort'] = vDeltaKolmogorov.index+1
        funcs.print_log(file_log, f'\n**{num_inc}.2. Kolmogorov-Smirnov fit test (sorted by Δ)**\n\n', on_screen = print_on_screen)
        funcs.print_log(file_log, f'{vDeltaKolmogorov[['station', 'empirical_dist', 'p_dist', 'delta', 'deltao', 'eval', 'fit', 'n', 'best_fit', 'best_fit_sort']].transpose().to_markdown()}', center_div=True, on_screen = print_on_screen)
        dp_best = vDeltaKolmogorov[vDeltaKolmogorov.best_fit == 1]
        dp_best = dp_best.reset_index(drop=True)
        dp_best.index.name = 'id'
        dp_best_of_best = pd.concat([dp_best, dp_best_of_best])
        if create_plot == True & plot_only_simple == False: funcs.print_log(file_log, f'<img alt="R.HydroTools" src="{fig_file1}" width="1200"></img>', center_div=True, on_screen = print_on_screen)
        funcs.print_log(file_log, f'\n**{num_inc}.3. Best fit**\n', on_screen = print_on_screen)
        funcs.print_log(file_log, f'{dp_best[['station', 'empirical_dist', 'p_dist', 'delta', 'deltao', 'eval', 'fit', 'n', 'best_fit', 'best_fit_sort']].to_markdown()}', center_div=True, on_screen = print_on_screen)
        if create_plot: funcs.print_log(file_log, f'<img alt="R.HydroTools" src="{fig_file2}" width="500"></img><img alt="R.HydroTools" src="{fig_file3}" width="500"></img>', center_div=True, on_screen = print_on_screen)
        num_inc += 1

        # Plot analysis graphs
        if create_plot:

            # Plot empirical vs. all pdf (graph 1)
            if plot_only_simple == False:
                figure(figsize=(15, 12))
                for i in range(0, len(vDeltaKolmogorov)):
                    dp = vDeltaKolmogorov['p_dist'][i]
                    delta = vDeltaKolmogorov['delta'][i]
                    if plot_only_fit:
                        only_fit_txt = ' (only Δo > Δ)'
                        if vDeltaKolmogorov['fit'][i] == 1:
                            plt.plot(df[x], df[dp], lw=1, marker='o', markersize=0, alpha=0.75, label=f'{dp} (Δ: {round(delta,plot_rounding_val)})')
                    else:
                        plt.plot(df[x], df[dp], lw=1, marker='o', markersize=0, alpha=0.75, label=f'{dp} (Δ: {round(delta,plot_rounding_val)})')
                        only_fit_txt = ''
                plt.scatter(df[x], df['empirical'], color='black', facecolors='darkgray', s=24, label=f'{emp} (Δo: {round(vDeltaKolmogorov['deltao'][0], plot_rounding_val)})')
                plt.title(f'Cumulative distribution function CDF{only_fit_txt}')
                plt.xlabel(parameter_name + ' ' + parameter_units)
                plt.ylabel('CDF')
                plt.legend(loc='best', frameon=True, edgecolor='white', framealpha=0.9, ncol=plot_legend_ncol, facecolor='white')
                plt.grid(color = 'gray', linestyle = '--', linewidth = 0.1)
                plt.annotate(f'Station: {station_code}', xy=(0.99, 0.98), xycoords='axes fraction', ha='right', fontsize=9)
                plt.annotate('github.com/rcfdtools', xy=(1.0275, 0.01), xycoords='axes fraction', ha='right', va='bottom', rotation='vertical', fontsize=7.5)
                if show_plot: plt.show()
                plt.savefig(output_path + fig_file1, dpi=dpi)
                plt.close()

            # Plot empirical vs. best fit (graph 2)
            plt.plot(df[x], df[dp_best['p_dist'][0]], color=color_plot, lw=1.5, marker='o', markersize=0, label=f'{dp_best['p_dist'][0]} (Δ: {round(dp_best['delta'][0], plot_rounding_val)})')
            plt.scatter(df[x], df['empirical'], color='black', facecolors='darkgray', s=24, label=f'{emp} (Δo: {round(dp_best['deltao'][0], plot_rounding_val)})')
            plt.title('Cumulative distribution function CDF (Best fit)')
            plt.xlabel(parameter_name + ' ' + parameter_units)
            plt.ylabel('CDF')
            plt.legend(loc='best', frameon=False)
            plt.grid(color = 'gray', linestyle = '--', linewidth = 0.1)
            plt.annotate(f'Station: {station_code}', xy=(0.99, 0.01), xycoords='axes fraction', ha='right', fontsize=9)
            plt.annotate('github.com/rcfdtools', xy=(1.0275, 0.01), xycoords='axes fraction', ha='right', va='bottom', rotation='vertical', fontsize=7.5)
            if show_plot: plt.show()
            plt.savefig(output_path + fig_file2, dpi=dpi)
            plt.close()

            # Plot Empirical & Estimated PDF - Best Fit (graph 3)
            plt.hist(df.x, density=True, histtype='stepfilled', alpha=0.4, color='gray', label=f'Empirical {emp}')
            plt.plot(df.x, df[dp_best['p_dist'][0]+'_pdf'], 'r-', lw=1.5, color=color_plot, label=f'Estimated {dp_best['p_dist'][0]}')
            plt.legend(loc='best', frameon=False)
            plt.title('Empirical & Estimated PDF (Best fit)')
            plt.xlabel(parameter_name + ' ' + parameter_units)
            plt.ylabel('PDF')
            plt.grid(color='gray', linestyle='--', linewidth=0.1)
            plt.annotate(f'Station: {station_code}', xy=(0.99, 0.01), xycoords='axes fraction', ha='right', fontsize=9)
            plt.annotate('github.com/rcfdtools', xy=(1.0275, 0.01), xycoords='axes fraction', ha='right', va='bottom', rotation='vertical', fontsize=7.5)
            if show_plot: plt.show()
            plt.savefig(output_path + fig_file3, dpi=dpi)
            plt.close()

        # Print extreme values table
        vDeltaKolmogorov = vDeltaKolmogorov.sort_values(by=['p_dist'], ascending=True)  # Required for assign the parameters in the right order
        vDeltaKolmogorov = vDeltaKolmogorov.reset_index(drop=True)

    # Best of best & Plot for extreme values
    dp_best_of_best = dp_best_of_best.sort_values(by='delta', ascending=True)
    dp_best_of_best = dp_best_of_best.reset_index(drop=True)
    dp_best_of_best.index.name = 'id'
    dp_best_of_best['best_fit_sort'] = dp_best_of_best.index+1
    best_of_best_p_dist = dp_best_of_best[dp_best_of_best['best_fit_sort']==1]['p_dist'][0]
    #print(f'>>>>>>>>>>>>>>>>> Best of best: {best_of_best_p_dist}')

    # Plot multiple extreme values over return periods Tr (graph 4)
    if create_plot:
        # Plot multiple extreme values for different pdf
        if plot_only_simple == False:
            figure(figsize=(15, 12))
            for i in range(0, len(vDeltaKolmogorov)):
                dp = vDeltaKolmogorov['p_dist'][i]
                delta = vDeltaKolmogorov['delta'][i]
                if plot_only_fit:
                    only_fit_txt = ' (only Δo > Δ)'
                    if vDeltaKolmogorov['fit'][i] == 1:
                        plt.plot(df_tr.tr, df_tr[dp], lw=1, marker='o', markersize=0, alpha=0.75,
                                 label=f'{dp} (Δ: {round(delta,plot_rounding_val)})')
                else:
                    only_fit_txt = ''
                    plt.plot(df_tr.tr, df_tr[dp], lw=1, marker='o', markersize=0, alpha=0.75,
                             label=f'{dp} (Δ: {round(delta,plot_rounding_val)})')
            plt.title(f'Extreme values for specific return periods{only_fit_txt}')
            plt.xlabel('Tr ($years$)')
            plt.ylabel(parameter_name + ' ' + parameter_units)
            plt.legend(loc='best', frameon=True, edgecolor='white', framealpha=0.9, ncol=4, facecolor='white')
            plt.grid(color='gray', linestyle='--', linewidth=0.1)
            plt.annotate(f'Station: {station_code}', xy=(0.99, 0.01), xycoords='axes fraction', ha='right', fontsize=9)
            plt.annotate('github.com/rcfdtools', xy=(1.0275, 0.01), xycoords='axes fraction', ha='right', va='bottom', rotation='vertical', fontsize=7.5)
            if show_plot: plt.show()
            plt.savefig(output_path + fig_file4, dpi=dpi)
            plt.close()

        # Plot extreme values for specific return periods (Best fit) (graph 5)
        plt.plot(df_tr['tr'], df_tr[best_of_best_p_dist], color=color_plot, lw=1.5, marker='o', markersize=3, label=best_of_best_p_dist)
        plt.title('Extreme values for specific return periods (Best fit)')
        plt.xlabel('Tr ($years$)')
        plt.ylabel(parameter_name + ' ' + parameter_units)
        plt.legend(loc='best', frameon=False)
        plt.grid(color='gray', linestyle='--', linewidth=0.1)
        plt.annotate(f'Station: {station_code}', xy=(0.99, 0.01), xycoords='axes fraction', ha='right', fontsize=9)
        plt.annotate('github.com/rcfdtools', xy=(1.0275, 0.01), xycoords='axes fraction', ha='right', va='bottom', rotation='vertical', fontsize=7.5)
        if show_plot: plt.show()
        plt.savefig(output_path + fig_file5, dpi=dpi)
        plt.close()

        # Plot risk rate for specific return periods (graph 5)
        plt.plot(df_tr['tr'], df_tr['risk_rate'], color=color_plot, lw=1.5, marker='o', markersize=3, label=best_of_best_p_dist)
        plt.title('Risk rate values for specific return periods')
        plt.xlabel('Tr ($years$)')
        plt.ylabel('Risk rate')
        plt.legend(loc='best', frameon=False)
        plt.grid(color='gray', linestyle='--', linewidth=0.1)
        plt.annotate(f'Station: {station_code}', xy=(0.99, 0.01), xycoords='axes fraction', ha='right', fontsize=9)
        plt.annotate('github.com/rcfdtools', xy=(1.0275, 0.01), xycoords='axes fraction', ha='right', va='bottom', rotation='vertical', fontsize=7.5)
        if show_plot: plt.show()
        plt.savefig(output_path + fig_file6, dpi=dpi)
        plt.close()

    # Best CDF fit & Estimate extreme values for specific return periods - Tr
    funcs.print_log(file_log, f'\n## C. Best fit & Estimate extreme values for specific return periods - Tr\n\n{dictionary.dicts['bestfit']}\n\n', on_screen = print_on_screen)
    #print(df_tr.columns)
    df_tr.drop('empirical_dist', axis=1, inplace=True)
    df_tr.index.name = 'id'
    dp_best_of_best[['station', 'empirical_dist', 'p_dist', 'delta', 'deltao', 'eval', 'fit', 'n', 'best_fit', 'best_fit_sort']].to_csv(f'{output_path}table/bestfit_{station_code}.csv', index=False)
    ##################df_tr.to_csv(f'{output_path}table/extreme_{station_code}.csv', index=False) ##############################
    funcs.print_log(file_log,f'\n### 1. Best fit (ordered by delta Δ)', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n\n:file_folder:Table: [bestfit_{station_code}.csv](table/bestfit_{station_code}.csv)\n', on_screen = print_on_screen)
    funcs.print_log(file_log,f'{dp_best_of_best[['station', 'empirical_dist', 'p_dist', 'delta', 'deltao', 'eval', 'fit', 'n', 'best_fit', 'best_fit_sort']].to_markdown()}', center_div=True, on_screen = print_on_screen)
    funcs.print_log(file_log,f'\n### 2. Extreme values and % difference analysis\n\n', on_screen = print_on_screen)
    funcs.print_log(file_log,f'{dictionary.dicts['tr']}', on_screen = print_on_screen)
    funcs.print_log(file_log,f'\n\n> {dictionary.dicts['risk_rate']}', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n\n:file_folder:Table: [extreme_{station_code}.csv](table/extreme_{station_code}.csv), all PDFs.  \n:file_folder:Table: [extremepdiff_{station_code}.csv](table/extremepdiff_{station_code}.csv), % difference between bestfit and most used PDFs in Hydrology.\n', on_screen = print_on_screen)
    funcs.print_log(file_log,f'Extreme values table for only best fit PDFs\n{df_tr.to_markdown()}\n', center_div=True, on_screen = print_on_screen)
    if create_plot == True & plot_only_simple == False: funcs.print_log(file_log, f'<img alt="R.HydroTools" src="{fig_file4}" width="1200"></img>', center_div=True, on_screen = print_on_screen)
    if create_plot: funcs.print_log(file_log, f'<img alt="R.HydroTools" src="{fig_file5}" width="500"></img><img alt="R.HydroTools" src="{fig_file6}" width="500"></img>', center_div=True, on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n<sub>{dictionary.dicts['disclaimer']}</sub>', on_screen = print_on_screen)
    #print(df.to_csv(index=False))

print(f'\nStations in dataset ({len(stations)})\n{stations}')
# -*- coding: UTF-8 -*-
# Tested with: Python 3.10, SciPy 1.11.3, NumPy 1.26.1, Pandas 2.1.3, xlrd

# General libraries
import functions as funcs
import dictionary as dictionary
import warnings
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import tabulate  # required for print tables in Markdown using pandas
import numpy as np
import pandas as pd
from datetime import datetime
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# General setup
app_version = 'v20251220'
input_path = 'dataset/pmax24h_in/'  # Your local input file folder
ouput_path = 'dataset/pmax24h_out/'  # Your local output file folder
station_catalog_file = 'dataset/CNE_IDEAM.xls' # CNE catalog for stations info
station_dataset_file = input_path + 'conventional.csv' # Stations dataset
parameter_name = 'rain, Pmax24h'  # rain, flow
parameter_units = '($mm/d$)'  # ($mm/d$), ($m^3/s$)
label_station = 'Station' # Station column name to eval from .csv station dataset file
label_x = 'Value'  # Value column name to eval from .csv station file
label_date = 'Date'  # Date column name from .csv station file
label_station_catalog = 'CODIGO' # Station column code in CNE_IDEAM.xls
label_latitude = 'LATITUD' # Station column latitude in CNE_IDEAM.xls
label_longitude = 'LONGITUD' # Station column longitude in CNE_IDEAM.xls
create_plot = False  # Creates and save plots into files
show_plot = False  # Show plot on Python screen console
plot_only_fit = True  # Plot only fit distributions with Δo > Δ
color_line_plot = 'black' # green
dpi = 96  # Graph plot resolution
show_warnings = False  # Show warnings on screen
low_extreme = False  # Eval low extreme values, if False, evaluates high extreme values
pdist_gumbel_on = True  # Eval the Gumbel distribution (non include in SciPy)
pdist_loggumbel_on = True  # Eval the Log-Gumbel distribution (non include in SciPy)
if not show_warnings: warnings.filterwarnings('ignore')
plot_legend_ncol = 2  # Columns on plot legend, '' for autofit
ddof = 1.00  # Standard deviation normalized
runtime = datetime.now()


# Return periods and probabilities
#tr = [2.33, 5, 10, 25, 50, 100]  # Tr, return period in years
tr = [2, 2.33, 5, 10, 15, 20, 25, 50, 75, 100, 200, 250, 500, 750, 1000]  # Tr, return period in years
df_tr = pd.DataFrame(tr, columns=['tr'])
n_tr = len(df_tr)
df_tr['prob_l'] = 1-1/df_tr.tr  # P≤, Probability less than, for high extreme values
df_tr['prob_g'] = 1/df_tr.tr  # P≥, Probability greater than, for low extreme values
df_l_pdist_scipy = pd.DataFrame(funcs.l_pdist_scipy, columns=['p_dist', 'n_parameter', 'fit_method', 'label', 'active'])
df_l_pdist_scipy['ref'] = '[:mortar_board:](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.'+df_l_pdist_scipy.p_dist+'.html)'
df_l_pdist_scipy = df_l_pdist_scipy.query('active == True')
df_l_pdist_scipy = df_l_pdist_scipy.sort_values(by=['p_dist'], ascending=True)
df_l_pdist_scipy = df_l_pdist_scipy.reset_index(drop=True)
df_l_pdist_scipy.index.name = 'id'


# Execution
df_all = pd.read_csv(station_dataset_file, delimiter=',', parse_dates=True)  # index_col=0
stations = df_all[label_station].unique()
print(stations)
data_types = {label_latitude: 'float64', label_longitude: 'float64'}
df_catalog = pd.read_excel(station_catalog_file, sheet_name='CNE', parse_dates=True, dtype=data_types) # , dtype=data_types
# print(df_catalog.dtypes)
for station in stations:
    station_code = str(station)
    fig_file0 = 'graph/' + station_code + '_data_serie.png'
    fig_file0a = 'graph/' + station_code + '_location_map.png'
    file_log_name = f'{ouput_path}{station_code}.md'  # Markdown file log
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
    funcs.print_log(file_log, '<img alt="R.HydroTools" src="../../../../file/graph/R.HydroTools.svg" width="250px">', center_div=True)
    funcs.print_log(file_log, f'# Station ({parameter_name}): {station_code}' )
    funcs.print_log(file_log, f'\n\n\n## A. General information\n\n\n### 1. General running parameters\n\n')
    for dict_var in dictionary.dicts:
        funcs.print_log(file_log, f'●{dict_var[1]}: _{eval(dict_var[0])}_. ')
    funcs.print_log(file_log, f'\n\n\n### 2. Station info and location\n\n{df_station_info.to_markdown()}\n')
    funcs.print_log(file_log, f'Map location in: [:earth_americas:Google]({google_maps_url}) [:earth_americas:OSM]({openstreetmap_url}) [:earth_americas:Bing]({bing_map_url}) [:earth_americas:Apple]({apple_map_url})<br>\n<img alt="R.GISPython" src="{fig_file0a}" width="500"></img>', center_div=True)
    funcs.print_log(file_log, f'\n### 3. Discrete values table and plot\n\n{df[[label_date, label_x]].transpose().to_markdown()}\n')
    funcs.print_log(file_log, '<img alt="R.GISPython" src="%s" width="600"></img>' % fig_file0, center_div=True)

    # Plot location map & Plot x values
    if create_plot:

        # Location map (graph 0a)
        location_map_plot = funcs.location_map(point_latitude, point_longitude, station)
        location_map_plot.savefig(ouput_path + fig_file0a, dpi=dpi)
        plt.close()

        # Plot x values  (graph 0)
        #df = df.sort_values(by=label_date)
        plt.plot(df[label_date], df[label_x], color=color_line_plot, lw=1.5, marker='o', markersize=3)
        plt.grid(color='gray', linestyle='--', linewidth=0.1)
        plt.title('Data serie')  #$_{ } for underscript text
        plt.xlabel('Year')
        plt.ylabel(parameter_name + ' ' + parameter_units)
        plt.xticks(rotation=0, ha='center')
        plt.annotate('Station: %s' % station_code, xy=(0.99, 0.01), xycoords='axes fraction', ha='right', fontsize=9)
        plt.annotate('github.com/rcfdtools', xy=(1.0275, 0.01), xycoords='axes fraction', ha='right', va='bottom', rotation='vertical', fontsize=7.5)
        if show_plot: plt.show()
        plt.savefig(ouput_path + fig_file0, dpi=dpi)
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
    funcs.print_log(file_log, '\n## B. Active continuous probability distributions from SciPy (%d of %d available)\n\n%s' % (len(df_l_pdist_scipy.query('active == True')), len(funcs.l_pdist_scipy), df_l_pdist_scipy.query('active == True').to_markdown()))
    funcs.print_log(file_log, '\n\n> Gumbel and Lob-Gumbel probability distributions are not shown in the above table.  \n> n_parameter = # arguments & localization & scale.  \n> Fit methods: (MLE) maximum likelihood, (MM) L-moments.')
    funcs.print_log(file_log, '\n\n\n## C. Probability distributions')
    vDeltaKolmogorov = pd.DataFrame(columns=['station', 'empirical_dist', 'p_dist', 'delta', 'deltao', 'eval', 'fit', 'n', 'loc', 'scale', 'shape', 'shape1', 'shape2', 'shape3'])

    # CDF calculations
    dp_evalated = 0 # cdf to eval
    if pdist_gumbel_on:
        dp_evalated += 1
    if pdist_loggumbel_on:
        dp_evalated += 1
    for i in range(0, len(df_l_pdist_scipy)):
        print('Processing CDF: %s...' % df_l_pdist_scipy['p_dist'][i])  # Only for console
        dp_evalated += 1
        funcs.pdist_scipy(df, df_l_pdist_scipy['p_dist'][i], df_l_pdist_scipy['n_parameter'][i], df_l_pdist_scipy['fit_method'][i], df_l_pdist_scipy['label'][i], x, low_extreme, df_tr, station_code, vDeltaKolmogorov)
    if pdist_gumbel_on: funcs.pdist_gumbel(df, x, ddof, low_extreme, df_tr, station_code, vDeltaKolmogorov)
    if pdist_loggumbel_on: funcs.pdist_loggumbel(df, x, low_extreme, df_tr, station_code, vDeltaKolmogorov)
    funcs.print_log(file_log, '\n\n\n### Cumulative distribution values - CDF (%d evalated, ordered by x ascending) \n\n%s\n\n' %(dp_evalated, df.to_markdown()))

    # Evaluation for each empirical distribution
    dp_best_of_best = pd.DataFrame()
    for emp in funcs.emp_dist:
        fig_file1 = 'graph/' + station_code + '_' + emp + '_vs_all.png'
        fig_file2 = 'graph/' + station_code + '_' + emp + '_vs_bestfit.png'
        fig_file3 = 'graph/' + station_code + '_' + emp + '_vs_estimatedpdf.png'
        fig_file4 = 'graph/' + station_code + '_extreme_values.png'
        fig_file5 = 'graph/' + station_code + '_extreme_values_bestfit.png'
        funcs.print_log(file_log, '\n### Empirical: %s\n' % emp)

        # Return periods & empirical values
        df_tr['empirical_dist'] = emp
        df_tr['station'] = station_code
        df_tr['n'] = len(df)
        df_tr['risk_rate'] = 1-(1-1/df_tr['tr'])**df_tr['tr']
        funcs.pdist_empirical(df, emp, x)

        # Kolmogorov-Smirnov test & best fit
        idk = 0
        for i in df_l_pdist_scipy['p_dist']:
            funcs.fTestKolmogorov(df, i, idk, emp, vDeltaKolmogorov)
            idk += 1
        if pdist_gumbel_on: funcs.fTestKolmogorov(df, 'zzgumbel', idk, emp, vDeltaKolmogorov)  # Run always after for i in df_l_pdist_scipy['p_dist']
        if pdist_loggumbel_on: funcs.fTestKolmogorov(df, 'zzloggumbel', idk+1, emp, vDeltaKolmogorov)  # Run always after for i in df_l_pdist_scipy['p_dist']
        vDeltaKolmogorov['best_fit'] = np.where((vDeltaKolmogorov['delta'] == vDeltaKolmogorov['delta'].min()), 1, 0)
        vDeltaKolmogorov = vDeltaKolmogorov.sort_values(by=['delta'], ascending=True)
        vDeltaKolmogorov = vDeltaKolmogorov.reset_index(drop=True)
        vDeltaKolmogorov.index.name = 'id'
        funcs.print_log(file_log, '\n\n#### 1. Empirical values\n')
        funcs.print_log(file_log, (df[['date', 'x', 'm', 'empirical_dist', 'empirical', 'empirical_tr']].transpose().to_markdown()), center_div=True)
        vDeltaKolmogorov['best_fit_sort'] = vDeltaKolmogorov.index+1
        funcs.print_log(file_log, '\n####  2. Parameters & Kolmogorov-Smirnov fit test (sorted by Δ)\n\n%s\n' % vDeltaKolmogorov[['empirical_dist', 'p_dist', 'delta', 'deltao', 'eval', 'fit', 'n', 'loc', 'scale', 'shape', 'shape1', 'shape2', 'shape3', 'best_fit', 'best_fit_sort']].to_markdown())
        dp_best = vDeltaKolmogorov[vDeltaKolmogorov.best_fit == 1]
        dp_best = dp_best.reset_index(drop=True)
        dp_best.index.name = 'id'
        dp_best_of_best = pd.concat([dp_best, dp_best_of_best])
        funcs.print_log(file_log, '<img alt="R.GISPython" src="%s" width="1200"></img>' % fig_file1, center_div=True)
        funcs.print_log(file_log, '\n#### 3. Best fit\n\n%s\n' %dp_best.to_markdown())
        funcs.print_log(file_log, '<img alt="R.GISPython" src="%s" width="600"></img>' % fig_file2, center_div=True)
        funcs.print_log(file_log, '<img alt="R.GISPython" src="%s" width="600"></img>' % fig_file3, center_div=True)
        #funcs.print_log(file_log, '<img alt="R.GISPython" src="%s" width="1200"></img>' % fig_file4, center_div=True)

        # Plot analysis graphs
        if create_plot:

            # Plot empirical vs. all (graph 1)
            figure(figsize=(15, 12))
            plt.scatter(df[x], df['empirical'], color='black', facecolors='darkgray', s=24, label='%s (Δo: %f)' % (emp, vDeltaKolmogorov['deltao'][0]))
            for i in range(0, len(vDeltaKolmogorov)):
                dp = vDeltaKolmogorov['p_dist'][i]
                delta = vDeltaKolmogorov['delta'][i]
                if plot_only_fit:
                    only_fit_txt = ' (only Δo > Δ)'
                    if vDeltaKolmogorov['fit'][i] == 1:
                        plt.plot(df[x], df[dp], lw=1, marker='o', markersize=0, alpha=0.75, label='%s (Δ: %f)' %(dp, delta))
                else:
                    plt.plot(df[x], df[dp], lw=1, marker='o', markersize=0, alpha=0.75, label='%s (Δ: %f)' %(dp, delta))
                    only_fit_txt = ''
            plt.title('Cumulative distribution function CDF%s' %(only_fit_txt))
            plt.xlabel(parameter_name + ' ' + parameter_units)
            plt.ylabel('CDF')
            plt.legend(loc='best', frameon=True, edgecolor='white', framealpha=0.9, ncol=plot_legend_ncol, facecolor='white')
            plt.grid(color = 'gray', linestyle = '--', linewidth = 0.1)
            plt.annotate('Station: %s' %(station_code), xy=(0.99, 0.98), xycoords='axes fraction', ha='right', fontsize=9)
            plt.annotate('github.com/rcfdtools', xy=(1.0275, 0.01), xycoords='axes fraction', ha='right', va='bottom', rotation='vertical', fontsize=7.5)
            if show_plot: plt.show()
            plt.savefig(ouput_path + fig_file1, dpi=dpi)
            plt.close()

            # Plot empirical vs. best fit (graph 2)
            plt.scatter(df[x], df['empirical'], color='black', facecolors='darkgray', s=24, label='%s (Δo: %f)' %(emp, dp_best['deltao'][0]))
            plt.plot(df[x], df[dp_best['p_dist'][0]], color=color_line_plot, lw=1.5, marker='o', markersize=0, label='%s (Δ: %f)' %(dp_best['p_dist'][0], dp_best['delta'][0]))
            plt.title('Cumulative distribution function CDF (Best fit)')
            plt.xlabel(parameter_name + ' ' + parameter_units)
            plt.ylabel('CDF')
            plt.legend(loc='best', frameon=False)
            plt.grid(color = 'gray', linestyle = '--', linewidth = 0.1)
            plt.annotate('Station: %s' % (station_code), xy=(0.99, 0.01), xycoords='axes fraction', ha='right', fontsize=9)
            plt.annotate('github.com/rcfdtools', xy=(1.0275, 0.01), xycoords='axes fraction', ha='right', va='bottom', rotation='vertical', fontsize=7.5)
            if show_plot: plt.show()
            plt.savefig(ouput_path + fig_file2, dpi=dpi)
            plt.close()

            # Plot Empirical & Estimated PDF - Best Fit (graph 3)
            plt.hist(df.x, density=True, histtype='stepfilled', alpha=0.4, color='gray', label='Empirical %s' % emp)
            plt.plot(df.x, df[dp_best['p_dist'][0]+'_pdf'], 'r-', lw=1.5, color=color_line_plot, label='Estimated %s' % dp_best['p_dist'][0])
            plt.legend(loc='best', frameon=False)
            plt.title('Empirical & Estimated PDF (Best fit)')
            plt.xlabel(parameter_name + ' ' + parameter_units)
            plt.ylabel('PDF')
            plt.grid(color='gray', linestyle='--', linewidth=0.1)
            plt.annotate('Station: %s' % (station_code), xy=(0.99, 0.01), xycoords='axes fraction', ha='right', fontsize=9)
            plt.annotate('github.com/rcfdtools', xy=(1.0275, 0.01), xycoords='axes fraction', ha='right', va='bottom', rotation='vertical', fontsize=7.5)
            if show_plot: plt.show()
            plt.savefig(ouput_path + fig_file3, dpi=dpi)
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
    print(f'>>>>>>>>>>>>>>>>> Best of best: {best_of_best_p_dist}')

    # Plot multiple extreme values over return periods Tr (graph 4)
    if create_plot:
        figure(figsize=(15, 12))
        for i in range(0, len(vDeltaKolmogorov)):
            dp = vDeltaKolmogorov['p_dist'][i]
            delta = vDeltaKolmogorov['delta'][i]
            if plot_only_fit:
                only_fit_txt = ' (only Δo > Δ)'
                if vDeltaKolmogorov['fit'][i] == 1:
                    plt.plot(df_tr.tr, df_tr[dp], lw=1, marker='o', markersize=0, alpha=0.75,
                             label='%s (Δ: %f)' % (dp, delta))
            else:
                only_fit_txt = ''
                plt.plot(df_tr.tr, df_tr[dp], lw=1, marker='o', markersize=0, alpha=0.75,
                         label='%s (Δ: %f)' % (dp, delta))
        plt.title('Extreme values for specific return periods%s' % (only_fit_txt))
        plt.xlabel('Tr ($years$)')
        plt.ylabel(parameter_name + ' ' + parameter_units)
        plt.legend(loc='best', frameon=True, edgecolor='white', framealpha=0.9, ncol=4, facecolor='white')
        plt.grid(color='gray', linestyle='--', linewidth=0.1)
        #plt.annotate('Station: %s (Δo: %f %s)' % (station_code, vDeltaKolmogorov['deltao'][0], emp), xy=(0.99, 0.01), xycoords='axes fraction', ha='right', fontsize=9)
        plt.annotate(f'Station: {station_code}', xy=(0.99, 0.01), xycoords='axes fraction', ha='right', fontsize=9)
        plt.annotate('github.com/rcfdtools', xy=(1.0275, 0.01), xycoords='axes fraction', ha='right', va='bottom', rotation='vertical', fontsize=7.5)
        if show_plot: plt.show()
        plt.savefig(ouput_path + fig_file4, dpi=dpi)
        plt.close()

        # Plot best fit values over return periods Tr (graph 5)
        #plt.plot(df_tr['tr'], df_tr[best_of_best_p_dist], color=color_line_plot, lw=1.5, marker='o', markersize=3, label='%s (Δ: %f)' % (dp_best['p_dist'][0], dp_best['delta'][0]))
        plt.plot(df_tr['tr'], df_tr[best_of_best_p_dist], color=color_line_plot, lw=1.5, marker='o', markersize=3, label=best_of_best_p_dist)
        plt.title('Extreme values for specific return periods (Best fit)')
        plt.xlabel('Tr ($years$)')
        plt.ylabel(parameter_name + ' ' + parameter_units)
        plt.legend(loc='best', frameon=False)
        plt.grid(color='gray', linestyle='--', linewidth=0.1)
        plt.annotate('Station: %s' % (station_code), xy=(0.99, 0.01), xycoords='axes fraction', ha='right', fontsize=9)
        plt.annotate('github.com/rcfdtools', xy=(1.0275, 0.01), xycoords='axes fraction', ha='right', va='bottom', rotation='vertical', fontsize=7.5)
        if show_plot: plt.show()
        plt.savefig(ouput_path + fig_file5, dpi=dpi)
        plt.close()

    # Best CDF fit & Estimate extreme values for specific return periods - Tr
    funcs.print_log(file_log, '\n## D. Best CDF fit & Estimate extreme values for specific return periods - Tr\n\n')
    funcs.print_log(file_log,'> risk_rate: assuming the return period as the project useful life.\n\n')
    print(df_tr.columns)
    df_tr.drop('empirical_dist', axis=1, inplace=True)
    df_tr.index.name = 'id'
    dp_best_of_best.to_csv(f'{ouput_path}table/bestfit_{station_code}.csv', index=False) ##############
    funcs.print_log(file_log,f'\n### Best fit (ordered by delta Δ)\n\n{dp_best_of_best.to_markdown()}')
    funcs.print_log(file_log, f'\n\n[Table: bestfit_{station_code}.csv](table/bestfit_{station_code}.csv)')
    funcs.print_log(file_log,f'\n\n\n### Extreme values\n\n{df_tr.to_markdown()}\n')
    funcs.print_log(file_log, '<img alt="R.GISPython" src="%s" width="1200"></img>' % fig_file4, center_div=True)
    funcs.print_log(file_log, '<img alt="R.GISPython" src="%s" width="600"></img>' % fig_file5, center_div=True)
    funcs.print_log(file_log, '\n<sub>**APP DISCLAIMER**: NO WARRANTY - This software is provided by [github.com/rcfdtools](https://github.com/rcfdtools) "as is", without any express or implied warranty, including warranties of merchantability, fitness for a particular purpose, or non-infringement. There is no guarantee that the software will be error-free or operate without interruption. LIMITATION OF LIABILITY - Neither the authors nor copyright holders will be liable for claims or damages arising from the software or its use. You are responsible for determining if the software is appropriate for your use and assume all associated risks, including errors, legal compliance, and data loss. NO PROFESSIONAL ADVICE - The software provides general information and does not offer professional advice. It should not replace consultation with professional advisors.</sub>')
    #print(df.to_csv(index=False))

# -*- coding: UTF-8 -*-
# Tested with: Python 3.10, SciPy 1.11.3, NumPy 1.26.1, Pandas 2.1.3

# General libraries
import functions as funcs
import warnings
from pathlib import Path
import matplotlib.pyplot as plt
import tabulate  # required for print tables in Markdown using pandas
import numpy as np
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# General setup
parameter_name = 'rain'  # rain, flow
parameter_units = '($mm/d$)'  # ($mm/d$), ($m^3/s$)
create_plot = True  # Creates and print plots
show_plot = False  # Show plot on screen
plot_only_fit = True  # Plot only fit distributions with Δo > Δ
color_line_plot = 'green'
dpi = 128  # Save plot resolution
show_warnings = False  # Show warnings on screen
low_extreme = False  # Eval low extreme values, if False, evaluates high extreme values
pdist_gumbel_on = True  # Activate the Gumbel distribution
pdist_loggumbel_on = True  # Activate the Log-Gumbel distribution
if not show_warnings: warnings.filterwarnings('ignore')
plot_legend_ncol = 4  # Columns on the legend
ddof = 1  # Standard deviation normalized
x_label = 'Valor'  # Initial value column name to eval from .csv station file
date_label = 'Fecha'  # Initial value column name from .csv station file
# Periodos de retorno y probabilidades
tr = [2.33, 5, 10, 25, 50, 100]  # Tr, return period in years
#tr = [2, 2.33, 5, 10, 15, 20, 25, 50, 75, 100, 200, 250, 500, 750, 1000]  # Tr, return period in years
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
input_path = 'dataset/pmax24h_in/'  # Your local input file folder
ouput_path = 'dataset/pmax24h_out/'  # Your local input file folder
station_file = input_path + '25020230_1969_2009.csv'
station_name = Path(station_file).stem  # File name without extension
#df_in = pd.read_csv(station_file, delimiter=',', parse_dates=True)  # index_col=0
df = pd.read_csv(station_file, delimiter=',', parse_dates=True)  # index_col=0
file_log_name = ouput_path + station_name + '.md'  # Markdown file log
file_log = open(file_log_name, 'w+', encoding='utf-8')   # w+ create the file if it doesn't exist
funcs.print_log(file_log, '# Station: %s' %station_name)
# Plot x values - Start
if create_plot:
    df = df.sort_values(by=date_label)
    plt.plot(df[date_label], df[x_label], color=color_line_plot, lw=2, marker='o', markersize=3, )
    plt.grid(color='gray', linestyle='--', linewidth=0.1)
    plt.title('Data serie')  #$_{ } for underscript text
    plt.xlabel('Year')
    plt.ylabel(parameter_name + ' ' + parameter_units)
    plt.xticks(rotation=0, ha='center')
    plt.annotate('Station: %s' % station_name, xy=(0.99, 0.01), xycoords='axes fraction', ha='right', fontsize=9)
    if show_plot: plt.show()
    fig_file = 'graph/' + station_name + '_data_serie.png'
    plt.savefig(ouput_path + fig_file, dpi=dpi)
    funcs.print_log(file_log, '<img alt="R.GISPython" src="%s" width="700"></img>' % fig_file, center_div=True)
x = x_label
date = date_label
df = df.dropna()
df = df.sort_values(by=x, ascending=True)
df = df.reset_index(drop=True)
df.index.name = 'id'
df['station'] = station_name
df['m'] = df.index+1
df = df.rename(columns={x: 'x', date: 'date'})
x = 'x'  # New value column name
date = 'date'  # New date column name
funcs.print_log(file_log, '\n\n## A. Active distributions from SciPy (%d of %d available)\n\n%s' % (len(df_l_pdist_scipy.query('active == True')), len(funcs.l_pdist_scipy), df_l_pdist_scipy.query('active == True').to_markdown()))
funcs.print_log(file_log, '\n\n> Gumbel and Lob-Gumbel probability distributions are not shown in the above table.  \n> n_parameter = # arguments & localization & scale.  \n> Fit methods: (MLE) maximum likelihood, (MM) L-moments.')
funcs.print_log(file_log, '\n\n\n## B. Probability distributions')
vDeltaKolmogorov = pd.DataFrame(columns=['station', 'empirical_dist', 'p_dist', 'delta', 'deltao', 'eval', 'fit', 'n', 'loc', 'scale', 'shape', 'shape1', 'shape2', 'shape3'])

# CDF calculations
dp_evalated = 2  # 2 means we are including Gumbel & Log Gumbel
for i in range(0, len(df_l_pdist_scipy)):
    print('Processing CDF: %s...' % df_l_pdist_scipy['p_dist'][i])  # Only for console
    dp_evalated += 1
    funcs.pdist_scipy(df, df_l_pdist_scipy['p_dist'][i], df_l_pdist_scipy['n_parameter'][i], df_l_pdist_scipy['fit_method'][i], df_l_pdist_scipy['label'][i], x, low_extreme, df_tr, station_name, vDeltaKolmogorov)
if pdist_gumbel_on: funcs.pdist_gumbel(df, x, ddof, low_extreme, df_tr, station_name, vDeltaKolmogorov)
if pdist_loggumbel_on: funcs.pdist_loggumbel(df, x, low_extreme, df_tr, station_name, vDeltaKolmogorov)
funcs.print_log(file_log, '\n\n### Cumulative distribution values - CDF (%d evalated, ordered by x ascending) \n\n%s' %(dp_evalated, df.to_markdown()))

# Evaluation for each empirical distribution
for emp in funcs.emp_dist:
    funcs.print_log(file_log, '\n\n\n### Empirical: %s\n' % emp)

    # Return periods & empirical values
    df_tr['empirical_dist '] = emp
    df_tr['station'] = station_name
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
    funcs.print_log(file_log, '\n\n#### 1. Empirical values\n\n')
    funcs.print_log(file_log, '%s' %(df[['date', 'x', 'm', 'empirical_dist', 'empirical', 'empirical_tr']].to_markdown()), center_div=True)
    vDeltaKolmogorov['best_fit_sort'] = vDeltaKolmogorov.index+1
    funcs.print_log(file_log, '\n\n####  2. Parameters & Kolmogorov-Smirnov fit test (sorted by Δ)\n\n%s' % vDeltaKolmogorov[['empirical_dist', 'p_dist', 'delta', 'deltao', 'eval', 'fit', 'n', 'loc', 'scale', 'shape', 'shape1', 'shape2', 'shape3', 'best_fit', 'best_fit_sort']].to_markdown())
    dp_best = vDeltaKolmogorov[vDeltaKolmogorov.best_fit == 1]
    dp_best = dp_best.reset_index(drop=True)
    dp_best.index.name = 'id'
    funcs.print_log(file_log, '\n\n#### 3. Best fit for\n\n%s' %dp_best.to_markdown())

    # Plot analysis graphs
    if create_plot:

        # Plot empirical vs. all
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
        plt.annotate('Station: %s' %(station_name), xy=(0.99, 0.98), xycoords='axes fraction', ha='right', fontsize=9)
        if show_plot: plt.show()

        # Plot empirical vs. best fit
        plt.scatter(df[x], df['empirical'], color='black', facecolors='darkgray', s=24, label='%s (Δo: %f)' %(emp, dp_best['deltao'][0]))
        plt.plot(df[x], df[dp_best['p_dist'][0]], color=color_line_plot, lw=2, marker='o', markersize=0, label='%s (Δ: %f)' %(dp_best['p_dist'][0], dp_best['delta'][0]))
        plt.title('Cumulative distribution function CDF (Best fit)')
        plt.xlabel(parameter_name + ' ' + parameter_units)
        plt.ylabel('CDF')
        plt.legend(loc='best', frameon=False)
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.1)
        plt.annotate('Station: %s' % (station_name), xy=(0.99, 0.01), xycoords='axes fraction', ha='right', fontsize=9)
        if show_plot: plt.show()

        # Plot Empirical & Estimated PDF - Best Fit
        plt.hist(df.x, density=True, histtype='stepfilled', alpha=0.4, color='gray', label='Empirical %s' % emp)
        plt.plot(df.x, df[dp_best['p_dist'][0]+'_pdf'], 'r-', lw=2, color=color_line_plot, label='Estimated %s' % dp_best['p_dist'][0])
        plt.legend(loc='best', frameon=False)
        plt.title('Empirical & Estimated PDF (Best fit)')
        plt.xlabel(parameter_name + ' ' + parameter_units)
        plt.ylabel('PDF')
        plt.grid(color='gray', linestyle='--', linewidth=0.1)
        plt.annotate('Station: %s' % (station_name), xy=(0.99, 0.01), xycoords='axes fraction', ha='right', fontsize=9)
        if show_plot: plt.show()

        # Plot values over return periods Tr
        for i in range(0, len(vDeltaKolmogorov)):
            dp = vDeltaKolmogorov['p_dist'][i]
            delta = vDeltaKolmogorov['delta'][i]
            if plot_only_fit:
                only_fit_txt = ' (only Δo > Δ)'
                if vDeltaKolmogorov['fit'][i] == 1:
                    plt.plot(df_tr.tr, df_tr[dp], lw=1, marker='o', markersize=0, alpha=0.75, label='%s (Δ: %f)' %(dp, delta))
            else:
                only_fit_txt = ''
                plt.plot(df_tr.tr, df_tr[dp], lw=1, marker='o', markersize=0, alpha=0.75, label='%s (Δ: %f)' % (dp, delta))
        plt.title('Extreme values for specific return periods%s' %(only_fit_txt))
        plt.xlabel('Tr ($years$)')
        plt.ylabel(parameter_name + ' ' + parameter_units)
        plt.legend(loc='best', frameon=True, edgecolor='white', framealpha=0.9, ncol=plot_legend_ncol, facecolor='white')
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.1)
        plt.annotate('Station: %s (Δo: %f %s)' %(station_name, vDeltaKolmogorov['deltao'][0], emp), xy=(0.99, 0.01), xycoords='axes fraction', ha='right', fontsize=9)
        if show_plot: plt.show()

    # Print extreme values table
    vDeltaKolmogorov = vDeltaKolmogorov.sort_values(by=['p_dist'], ascending=True)  # Required for asign the parameters in the right order
    vDeltaKolmogorov = vDeltaKolmogorov.reset_index(drop=True)

funcs.print_log(file_log, '\n\n\n## C. Estimate extreme values for specific return periods - Tr\n')
df_tr.index.name = 'id'
funcs.print_log(file_log,df_tr.to_markdown())
funcs.print_log(file_log,'\n> risk_rate: assuming the return period as the project useful life.')

#print(df.to_csv(index=False))
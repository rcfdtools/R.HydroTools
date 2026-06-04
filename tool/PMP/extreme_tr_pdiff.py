# https://github.com/rcfdtools/R.HydroTools/blob/main/tool/PMP/Readme.md
# extreme_tr_pdiff.py: process the extremediff_station.csv obtaining the extreme differences between bestfit PDF and the regular PDFs used in Hydrology (norm, lognorm, gumbel_l, gumbel_r, gamma, pearson3, logpearson3, dweibull, kappa4).

import pandas as pd
pd.set_option('display.max_colwidth', None)
import glob
import os
import tabulate # required for print tables in Markdown using pandas


# General setup
app_version = 'v20260118'
input_path = 'dataset/pmax24h_out/table/' # Your local input file folder
label_station = 'station' # Station column name to eval from .csv station dataset file
regular_hydrology_pdf = ['norm', 'lognorm', 'gumbel_l', 'gumbel_r', 'gamma', 'pearson3', 'logpearson3', 'dweibull', 'kappa4'] # Most used PDFs in hydrology (bestfit difference analysis) ●
pdiff_suffix = 'pdiff'


# Join bestfit and extreme .csv results files
extension = 'csv'
# Bestfit files join
all_filenames = [i for i in glob.glob(os.path.join(input_path, 'bestfit_*.{}'.format(extension)))]
df_bestfit = pd.concat([pd.read_csv(f) for f in all_filenames], ignore_index=True)
df_bestfit[label_station] = df_bestfit[label_station].astype(str)
print(f'\nSuccessfully combined {len(all_filenames)} files: bestfit')
stations = df_bestfit[label_station].unique()
df_stations = pd.DataFrame(stations, columns=[label_station])
# Extreme values files join
all_filenames = [i for i in glob.glob(os.path.join(input_path, 'extreme_*.{}'.format(extension)))]
df_extreme = pd.concat([pd.read_csv(f) for f in all_filenames], ignore_index=True)
df_extreme[label_station] = df_extreme[label_station].astype(str)
print(f'Successfully combined {len(all_filenames)} files: extreme')


# Compare extreme values difference between bestfit PDF vs. most used PDF's in hydrology
df_bestfit_1 = df_bestfit[df_bestfit['best_fit_sort'] == 1].sort_values(by=[label_station], ascending=True)
stations = df_bestfit_1[label_station].unique()
print(f'Processing {len(stations)} stations')
for station in stations:
    bestfit_station_pdf = df_bestfit_1[df_bestfit_1[label_station] == station]
    bestfit_station_pdf = bestfit_station_pdf['p_dist'].item()
    print(f'Processing extreme diff for station: {station}, bestfit PDF: {bestfit_station_pdf}')
    general_fields = [label_station, 'tr', 'n', 'bestfit_pdf', 'bestfit_val']
    general_fields = general_fields + regular_hydrology_pdf # Join field list
    df_extreme_station = df_extreme[df_extreme[label_station] == station].sort_values(by=[label_station, 'tr'], ascending=True)
    df_extreme_station = df_extreme_station.reset_index(drop=True)
    df_extreme_station.index.name = 'id'
    df_extreme_station['bestfit_pdf'] = bestfit_station_pdf
    df_extreme_station['bestfit_val'] = df_extreme_station[bestfit_station_pdf]
    # Porcentual difference (diff)
    for regular in regular_hydrology_pdf:
        df_extreme_station[f'{regular}_{pdiff_suffix}'] = round((1-(df_extreme_station['bestfit_val']/df_extreme_station[regular]))*100, 2)
        general_fields = general_fields + [f'{regular}_pdiff']
    df_extreme_station[general_fields].to_csv(f'{input_path}extreme{pdiff_suffix}_{station}.csv', index=False)
    #print(f'\n{df_extreme_station[general_fields].to_markdown()}')


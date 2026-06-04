# Infinite values will be removed from extreme.csv dataset
# https://github.com/rcfdtools/R.HydroTools/blob/main/tool/PMP/Readme.md

# Import libraries
import pandas as pd
import numpy as np
import requests


# General vars
output_path = 'C:/R.WREM/file/table/'
main_url = 'https://raw.githubusercontent.com/rcfdtools/R.HydroTools/refs/heads/main/tool/PMP/dataset/pmax24h_out/paper/'
bestfit_sort = 1 # ● Best fit orden number, 1 is best and 12 is worst
get_files = False # ● Download files again or get an updated version
bestfit_file = 'bestfit.csv'
extreme_file = 'extreme.csv'
stations_file = 'stations.csv'
files = [bestfit_file,extreme_file,stations_file]
regular_hydrology_pdf = ['norm', 'lognorm', 'gumbel_l', 'gumbel_r', 'gamma', 'pearson3', 'logpearson3', 'dweibull', 'kappa4'] # Most used PDFs in hydrology (bestfit difference analysis) ●
print_explicit = True # Print detailed stations records


# Download required files
print('------------------------------\nPmax24hr Post-Processing Tool\n------------------------------\n\n* Research: Study and analysis of the 24 hours Maximum Precipitation (PMax24h) in the network of automatic climatological stations of Colombia - South America and estimation of extreme values for different return periods using various probability distributions.\n')
if get_files:
    print('* Download files: activated')
    for i in files:
        url = f'{main_url}{i}'
        response = requests.get(url)
        if response.status_code == 200:
            # Open a local file in 'write binary' (wb) mode
            with open(f'{output_path}{i}', "wb") as file:
                file.write(response.content)
            print(f'* Downloading {url}')
        else:
            print(f"Failed to download file. Status code: {response.status_code}")
else:
    print('* Download files: deactivated')


# Getting PMax24hr PDF values per station for multiple Tr`s
df_extreme = pd.read_csv(f'{output_path}{extreme_file}', sep=',')
df_extreme.dropna(inplace=True)
df_stations = pd.read_csv(f'{output_path}{stations_file}', sep=',')
df_stations = df_stations.rename(columns={'NOMBRE': 'name', 'LATITUD': 'latitude', 'LONGITUD': 'longitude'})
df_stations = df_stations[['station', 'name', 'latitude', 'longitude']]
df_extreme = pd.merge(df_extreme, df_stations, on='station')
df_extreme_gis = pd.DataFrame()


# Getting PMax24hr PDF Best Fit per station for multiple Tr`s
df_bestfit = pd.read_csv(f'{output_path}{bestfit_file}', sep=',')
df_bestfit = df_bestfit[df_bestfit['best_fit_sort'] == bestfit_sort]
df_bestfit = df_bestfit[['station', 'p_dist','n']]
df_bestfit = df_bestfit.sort_values(by='station')
print(f'* Evaluating bestfit #{bestfit_sort} PDF ({len(df_bestfit)} stations)')
csv_file = f'{output_path}extreme_bestfit_gis.csv'
print(f'* Getting PMax24hr PDF bestfit for multiple Tr`s ({len(df_bestfit)} stations): {csv_file}')
for station, p_dist in zip(df_bestfit.station, df_bestfit.p_dist):
    filtered_df_extreme = df_extreme[df_extreme['station'] == station]
    filtered_df_extreme = filtered_df_extreme[['station', 'name', 'latitude', 'longitude', 'tr', p_dist, 'n']]
    filtered_df_extreme['p_dist'] = p_dist
    filtered_df_extreme = filtered_df_extreme.rename(columns={p_dist: 'pmax24hr'})
    filtered_df_extreme = filtered_df_extreme.sort_values(by='tr')
    filtered_df_extreme = filtered_df_extreme.replace([np.inf, -np.inf], np.nan).dropna(subset=['pmax24hr'])
    if print_explicit:
        #print(filtered_df_extreme)
        print(f'* bestfit for Station: {station} ({p_dist})')
    df_extreme_gis = pd.concat([df_extreme_gis, filtered_df_extreme], ignore_index=True)
    del filtered_df_extreme
df_extreme_gis.to_csv(csv_file, index=False)
del df_extreme_gis

# Getting PMax24hr most common PDF per station for multiple Tr`s
for regular_pdf in regular_hydrology_pdf:
    csv_file = f'{output_path}extreme_{regular_pdf}_gis.csv'
    df_extreme_gis = pd.DataFrame()
    print(f'* Getting PMax24hr PDF {regular_pdf} for multiple Tr`s ({len(df_bestfit)} stations): {csv_file} ')
    for station in df_bestfit.station:
        filtered_df_extreme = df_extreme[df_extreme['station'] == station]
        filtered_df_extreme = filtered_df_extreme[['station', 'name', 'latitude', 'longitude', 'tr', regular_pdf, 'n']]
        filtered_df_extreme['p_dist'] = regular_pdf
        filtered_df_extreme = filtered_df_extreme.rename(columns={regular_pdf: 'pmax24hr'})
        filtered_df_extreme = filtered_df_extreme.sort_values(by='tr')
        filtered_df_extreme = filtered_df_extreme.replace([np.inf, -np.inf], np.nan).dropna(subset=['pmax24hr'])
        if print_explicit:
            #print(filtered_df_extreme)
            print(f'* {regular_pdf} for Station: {station} ({p_dist})')
        df_extreme_gis = pd.concat([df_extreme_gis, filtered_df_extreme], ignore_index=True)
        del filtered_df_extreme
    df_extreme_gis.to_csv(csv_file, index=False)
    del df_extreme_gis
#print(df_extreme.head())
#print(df_extreme_gis)
import pandas as pd7
import pandas as pd
pd.set_option('display.max_colwidth', None)
import glob
import os
import tabulate # required for print tables in Markdown using pandas
import functions as funcs
import dictionary as dictionary
import matplotlib.pyplot as plt
import numpy as np


# General setup
app_version = 'v20251229'
input_path = 'dataset/pmax24h_out/table/' # Your local input file folder
output_path = 'dataset/pmax24h_out/paper/' # Your local output file folder
station_catalog_file = 'dataset/CNE.xls' # CNE catalog for stations info
station_catalog_columns_drop = ['OBSERVACION', 'SUBRED'] # Dropped columns from CNE
parameter_name = 'Rain, Pmax24h' # rain, flow
parameter_title = 'PMP' # Probable Maximum Precipitation (PMP) or Probable Maximum Flood (PMF)
label_station = 'station' # Station column name to eval from .csv station dataset file
label_station_catalog = 'CODIGO' # Station column code in CNE_IDEAM.xls
label_name = 'NOMBRE' # Station column nome in CNE_IDEAM.xls
label_category = 'CATEGORIA' # Station column category in CNE_IDEAM.xls
label_technology = 'TECNOLOGIA' # Station column technology in CNE_IDEAM.xls
label_status = 'ESTADO' # Station column active in CNE_IDEAM.xls
label_install_date = 'FECHA_INSTALACION' # Station column activation date in CNE_IDEAM.xls
label_latitude = 'LATITUD' # Station column latitude in CNE_IDEAM.xls
label_longitude = 'LONGITUD' # Station column longitude in CNE_IDEAM.xls
label_state = 'DEPARTAMENTO' # Station column state in CNE_IDEAM.xls
label_county = 'MUNICIPIO' # Station column county in CNE_IDEAM.xls
label_ah = 'AREA_HIDROGRAFICA' # Station column hydrographic area in CNE_IDEAM.xls
label_zh = 'ZONA_HIDROGRAFICA' # Station column hydrographic zone in CNE_IDEAM.xls
label_szh = 'SUBZONA_HIDROGRAFICA' # Station column hydrographic subzone in CNE_IDEAM.xls
print_on_screen = False # Global print control in screen
file_log_name = f'{output_path}{'paper'}.md'  # Markdown file log
file_log = open(file_log_name, 'w+', encoding='utf-8')   # w+ create the file if it doesn't exist
create_plot = True # Creates, save and include plots into reports ●
show_plot = False # Show plot on Python screen console
color_plot = '#3b3b3b' # Global plot color
minimum_sample = 8 # Exclude a station when doesn't have the minimum data sample (0 means any) ●
dpi = 96 # Graph plot resolution
create_geojson_map = True
only_automatic_stations = True  # Evaluated only stations with automatic technology avoiding stations tag define in automatic_tag_not_in
automatic_tag_not_in = ['(No data)'] # Tag to exclude. Keep in mind some conventional stations are now automatic
#automatic_tag_not_in = ['Convencional', '(No data)'] # Tag to exclude. Keep in mind some conventional stations are now automatic
exclude_stations = True
stations_to_exclude = ['25020230', '25020240', '25020250', '25020260', '25020280', '25020690', '25020920', '25021240', '25021650', '25025250', '28010070', '28020080', '28020150', '28020230', '28020310', '28020420', '28020440', '28020460', '28020600', '28025070', '28025080', '28025090', '28035010', '28035040', '28040310', '28040350']
histogram_custom_bins_n = [5, 6, 7, 8, 9, 10, 15, 20, 25] # Bins for n years values histogram per station evaluated
#histogram_custom_bins_n = [5, 6, 7, 8, 9, 10, 15, 20, 25, 65] # Bins for n years values histogram per station evaluated, include 65 for conventional stations


# Header & join best fit .csv results files and read and filter the CNE catalog
funcs.print_log(file_log, '<img alt="R.HydroTools" src="../../../../../file/graph/R.HydroTools.svg" width="250px">', center_div=True, on_screen = print_on_screen)
funcs.print_log(file_log, f'# {dictionary.dicts['study_name']}\n', on_screen = print_on_screen)
funcs.print_log(file_log, f'\n\n{dictionary.dicts['pmp']}\n', on_screen = print_on_screen)
extension = 'csv'
all_filenames = [i for i in glob.glob(os.path.join(input_path, 'bestfit_*.{}'.format(extension)))]
df_bestfit = pd.concat([pd.read_csv(f) for f in all_filenames], ignore_index=True)
df_bestfit[label_station] = df_bestfit[label_station].astype(str)
if exclude_stations:
    df_bestfit = df_bestfit[~df_bestfit[label_station].isin(stations_to_exclude)] # Excluding stations using isin() with Boolean Negation (~)
#print(f'\ndf_bestfit types: \n{df_bestfit.dtypes}')
df_bestfit.to_csv(f'{output_path}bestfit.csv', index=False, encoding='utf-8')
print(f'\nSuccessfully combined {len(all_filenames)} files into bestfit.csv')
stations = df_bestfit[label_station].unique()
df_stations = pd.DataFrame(stations, columns=[label_station])
#print(f'\ndf_stations types:\n{df_stations.dtypes}')
#print(f'Stations in dataset:\n{stations}\n')
# Read and filter CNE catalog
data_types = {label_station_catalog: 'str', label_latitude: 'float64', label_longitude: 'float64'}
df_catalog = pd.read_excel(station_catalog_file, sheet_name='CNE', parse_dates=True, dtype=data_types) # , dtype=data_types
df_catalog = df_catalog.drop(columns=station_catalog_columns_drop)
#print(f'\ndf_catalog types: \n{df_catalog.dtypes.to_markdown()}') # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#print(f'\ndf_catalog.head().to_markdown()') # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
if only_automatic_stations:
    #df_catalog = df_catalog[df_catalog[label_technology] != automatic_tag_not_in]
    df_catalog = df_catalog[~df_catalog[label_technology].isin(automatic_tag_not_in)] # Excluding stations using isin() with Boolean Negation (~)
if exclude_stations:
    df_catalog = df_catalog[~df_catalog[label_station_catalog].isin(stations_to_exclude)] # Excluding stations using isin() with Boolean Negation (~)
df_catalog_filter = df_catalog[df_catalog[label_station_catalog].isin(df_stations[label_station])]
df_catalog_filter = df_catalog_filter.sort_values(by=[label_station_catalog], ascending=True)
df_catalog_filter = df_catalog_filter.reset_index(drop=True)
df_catalog_filter.index.name = 'id'
#print(f'\nfiltered_df types: \n{filtered_df.dtypes}')
#print(f'\n{df_catalog_filter.head().to_markdown()}')
df_catalog_filter_selected_columns = df_catalog_filter[[label_station_catalog, label_name, label_category, label_technology, label_status, label_install_date, label_latitude, label_longitude, label_state, label_county, label_ah, label_zh, label_szh]]


# Create GeoJSON map
if create_geojson_map:
    funcs.print_log(file_log, 'Dynamic map', center_div=True, on_screen = print_on_screen)
    funcs.print_log(file_log, '```topojson\n{"type": "Topology", "objects": {"example": {"type": "GeometryCollection","geometries": [\n', on_screen = print_on_screen)
    for index, row in df_catalog_filter_selected_columns.iterrows():
        #print (index)
        #print(f"Code: {row['CODIGO']}, Name: {row['NOMBRE']}")
        properties = (f'"Code": "{row[label_station_catalog]}", "Name": "{row[label_name]}", "Category": "{row[label_category]}", "Technology": "{row[label_technology]}", "Status": "{row[label_status]}", "Installation date": "{row[label_install_date]}", "Latitude": "{row[label_latitude]}", "Longitude": "{row[label_longitude]}", "State": "{row[label_state]}", "County": "{row[label_county]}", "AH": "{row[label_ah]}", "ZH": "{row[label_zh]}", "SZH": "{row[label_szh]}"')
        print_geojson = '{"type": "Point","properties": {'+str(properties)+'},"coordinates": [' + str(row[label_longitude]) + ',' + str(row[label_latitude]) + ']}'
        funcs.print_log(file_log, print_geojson, on_screen = print_on_screen)
        if index <= len(df_catalog_filter) - 2:
            funcs.print_log(file_log, ',\n', on_screen = print_on_screen)
        else:
            funcs.print_log(file_log, '\n', on_screen = print_on_screen)
    funcs.print_log(file_log, ']}}}\n\n```', on_screen = print_on_screen)


# Stations list & Static map
fig_file0a = 'graph/locationmap.png'
df_catalog_filter.to_csv(f'{output_path}stations.csv', index=False)
funcs.print_log(file_log, f'\n\n## A. Stations evaluated\n\n{dictionary.dicts['hydrometeorological_station']}\n', center_div=False, on_screen = print_on_screen)
funcs.print_log(file_log, f'\n:file_folder:Filtered tables: [Stations dataset](stations.csv) | [Bestfit probability distributions](bestfit.csv).\n\n', on_screen = print_on_screen) #######################
funcs.print_log(file_log, f'<img alt="R.HydroTools" src="{fig_file0a}" width="500"></img>', center_div=True, on_screen = print_on_screen)
#funcs.print_log(file_log, f'\n\n{df_catalog_filter.to_markdown()}', center_div=False, on_screen = print_on_screen) # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#print(f'\nFiltered stations catalog:\n{df_catalog_filter.to_markdown()}') # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
funcs.print_log(file_log, f'\n### 0. Stations list ({len(df_catalog_filter_selected_columns)} used)\n\n{dictionary.dicts['station_list']}\n\n', center_div=False, on_screen = print_on_screen)
for index, row in df_catalog_filter_selected_columns.iterrows():
    station_url = (f'<sub>•[{row[label_station_catalog]}](../{row[label_station_catalog]}.md)</sub>')
    funcs.print_log(file_log, f'{station_url} ', on_screen=print_on_screen)
    '''
    if index <= len(df_catalog_filter) - 2:
        funcs.print_log(file_log, f'{station_url}, ', on_screen=print_on_screen)
    else:
        funcs.print_log(file_log, f'{station_url}.', on_screen=print_on_screen)
    '''
location_map_plot = funcs.location_map_multiple(df_catalog_filter_selected_columns, label_latitude, label_longitude)
location_map_plot.savefig(output_path + fig_file0a, dpi=dpi)
plt.close()
if show_plot: location_map_plot.show()


# Station bestfit records analysis & Histogram of n
#general_stat_vars = ['label_category', 'label_technology', 'label_status', 'label_state', 'label_ah', 'label_zh'] # As text for the dictionary definitions call
#df_station_record = df_bestfit.groupby(label_station)['n'].mean().reset_index()
df_station_record = df_bestfit[df_bestfit['best_fit_sort'] == 1].sort_values(by=['n', label_station], ascending=False)
#df_station_record = df_station_record.sort_values(by=['n', label_station], ascending=False)
df_station_record = df_station_record.reset_index(drop=True)
df_station_record.index.name = 'id'
funcs.print_log(file_log, f'\n\n\n### 1. Records per Station (histogram)\n\n{dictionary.dicts['station_record']}\n', center_div=False, on_screen = print_on_screen)
#funcs.print_log(file_log, f'{df_station_record.to_markdown()}', center_div=True, on_screen = print_on_screen)
if create_plot: # Histogram plot
    funcs.print_log(file_log, f'<img alt="R.HydroTools" src="graph/stations_histogram_count.png" width="800"></img>', center_div=True, on_screen=print_on_screen)
    fig, ax = plt.subplots(figsize=(10, 6))
    N, bins, patches = ax.hist(df_station_record['n'], bins=histogram_custom_bins_n, color=color_plot, edgecolor='white', rwidth=1) # edgecolor='black'
    #N, bins, patches = ax.hist(df_station_record['n'], bins=10, color=color_plot, edgecolor='white', rwidth=1) # edgecolor='black'
    ax.bar_label(patches, labels=[f'{int(c)}' for c in N], label_type='edge', padding=3, rotation=90)
    ax.set_title('Histogram of n')
    ax.set_xlabel('Value Bins')
    ax.set_ylabel('Frequency')
    ax.set_xticks(bins[:-1] + np.diff(bins) / 2)  # Centers the x-tick labels within the bars
    ax.set_xticklabels([f'{bins[i].astype(int)}-{bins[i + 1].astype(int)}' for i in range(len(bins) - 1)], rotation=90, ha='center')
    plt.tight_layout()  # Adjust layout to prevent labels from being cut off
    plt.savefig(f'{output_path}graph/stations_histogram_count.png', dpi=dpi)
    if show_plot: plt.show()
    plt.close()
if minimum_sample > 0:
    df_station_record = df_station_record[df_station_record['n'] >= minimum_sample]
    funcs.print_log(file_log, f'\nWith a minimum length of records established in {minimum_sample} years, we are processing and analysing the best fit results for {len(df_station_record)} stations (minus those stations without no data information or not available in the CNE catalog).', on_screen = print_on_screen)


# CNE catalog general statistics
df_catalog_filter = df_catalog_filter[df_catalog_filter[label_station_catalog].isin(df_station_record[label_station])] # <<<<<<<<<<<<<<<<<<<<<<<<<<<<
general_stat_vars = ['label_category', 'label_technology', 'label_status', 'label_state', 'label_ah', 'label_zh'] # As text for the dictionary definitions call
funcs.print_log(file_log, f'\n\n', center_div=False, on_screen=print_on_screen)
general_index = 2
for general in general_stat_vars:
    #catalog_count=df_catalog_filter[eval(general)].value_counts().reset_index(name='Count').sort_values(by=eval(general)) # sort by var
    catalog_count=df_catalog_filter[eval(general)].value_counts().reset_index(name='Count').sort_values(by='Count', ascending=False) # sort by count
    catalog_count = catalog_count.reset_index(drop=True)
    catalog_count.index.name = 'id'
    catalog_count['plot_label']= catalog_count[eval(general)].str[:40] # short labels
    funcs.print_log(file_log, f'\n### {general_index}. Stations by {eval(general)}\n\n{dictionary.dicts[general]}\n', center_div=False, on_screen = print_on_screen)
    funcs.print_log(file_log, f'{catalog_count.to_markdown()}', center_div=True, on_screen = print_on_screen)
    general_index += 1
    if create_plot:
        catalog_count = catalog_count.sort_values(by='Count', ascending=True)
        funcs.print_log(file_log, f'<img alt="R.HydroTools" src="graph/stations_by_{eval(general)}.png" width="800"></img>',center_div=True, on_screen=print_on_screen)
        # Bar plot
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.barh(catalog_count['plot_label'], catalog_count['Count'], color=color_plot)
        plt.yticks(rotation=0, ha='right')
        ax.bar_label(bars, padding=3)
        ax.set_title(f'Stations by {eval(general)}')
        ax.set_xlabel('Count')
        plt.tight_layout() # Important >>> prevents cutting labels
        plt.subplots_adjust(bottom=0.075)
        plt.savefig(f'{output_path}graph/stations_by_{eval(general)}.png', dpi=dpi)
        if show_plot: plt.show()
        plt.close()


# Probability distributions - Best Fit
df_l_pdist_scipy = pd.DataFrame(funcs.l_pdist_scipy, columns=['p_dist', 'n_parameter', 'fit_method', 'label', 'active'])
df_l_pdist_scipy['ref'] = '[:mortar_board:](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.'+df_l_pdist_scipy.p_dist+'.html)'
df_l_pdist_scipy_inactive = df_l_pdist_scipy.query('active == False')
df_l_pdist_scipy = df_l_pdist_scipy.query('active == True')
df_l_pdist_scipy = df_l_pdist_scipy.sort_values(by=['p_dist'], ascending=True)
df_l_pdist_scipy = df_l_pdist_scipy.reset_index(drop=True)
df_l_pdist_scipy.index.name = 'id'
funcs.print_log(file_log, f'\n\n## B. Probability and Empirical distributions\n\n{dictionary.dicts['pdf']}\n', center_div=False, on_screen = print_on_screen)
funcs.print_log(file_log, f'\n{dictionary.dicts['log_pdf']}\n', on_screen=print_on_screen)
funcs.print_log(file_log,f'\n\n### 0. Active continuous probability distributions from SciPy ({len(df_l_pdist_scipy.query('active == True'))} of {len(funcs.l_pdist_scipy)} available)', on_screen=print_on_screen)
funcs.print_log(file_log, f'\n\n{dictionary.dicts['scipy_stats']}\n', on_screen=print_on_screen)
funcs.print_log(file_log, f'{df_l_pdist_scipy.query('active == True').to_markdown()}', center_div=True, on_screen=print_on_screen)
funcs.print_log(file_log,'> **n_parameter:** # arguments & localization & scale.\n>\n> **Fit methods:** (MLE) maximum likelihood, (MM) L-moments.', on_screen=print_on_screen)
funcs.print_log(file_log, (f'\n>\n>**Inactive** ({dictionary.dicts['disable_pdf']})**:** '), on_screen=print_on_screen)
for inactives in df_l_pdist_scipy_inactive['p_dist'].values:
    funcs.print_log(file_log, (f'{inactives}, '), on_screen=print_on_screen)
funcs.print_log(file_log, f'\n\n\n### 1. Cumulative distribution values - CDF\n\n', on_screen = print_on_screen)
funcs.print_log(file_log, f'{dictionary.dicts['cdf']}\n', on_screen = print_on_screen)
funcs.print_log(file_log, '\n\n### 2. Probability distributions vs. Empirical distributions', on_screen = print_on_screen)
funcs.print_log(file_log, f'\n\n{dictionary.dicts['cpd']}\n\n', on_screen = print_on_screen)
df_edf_dist_dict = pd.DataFrame(dictionary.edf_dist_dict, columns=['edf_dist', 'edf_name', 'edf_expression', 'edf_year', 'edf_desc'])
edf_dist = df_edf_dist_dict['edf_dist'].unique()
num_inc = 1
funcs.print_log(file_log, f'{dictionary.dicts['edf']}\n\n', on_screen = print_on_screen)
for emp in edf_dist:
    df_edf_dist_dict_filter = df_edf_dist_dict[df_edf_dist_dict['edf_dist'] == emp]
    funcs.print_log(file_log,
                    f'\n#### 2.{num_inc}. Empirical - {df_edf_dist_dict_filter['edf_name'].to_string(index=False, header=False)} ({df_edf_dist_dict_filter['edf_year'].to_string(index=False, header=False)})\n',
                    on_screen=print_on_screen)
    funcs.print_log(file_log, f'\n{df_edf_dist_dict_filter['edf_desc'].to_string(index=False, header=False)}\n',
                    on_screen=print_on_screen)
    funcs.print_log(file_log, f'\n${df_edf_dist_dict_filter['edf_expression'].to_string(index=False, header=False)}$\n',
                    center_div=True, on_screen=print_on_screen)
    num_inc += 1

# Best fit analysis
funcs.print_log(file_log, f'\n## C. Best Fit analysis\n\n{dictionary.dicts['bestfit']}', center_div=False, on_screen = print_on_screen)
funcs.print_log(file_log, f'\n\nFor each ranking position, results values are order by: empirical distribution (empirical_dist), probability distribution (p_dist) and Δ value (delta).', center_div=False, on_screen = print_on_screen)
for i in range(len(edf_dist)+1):
    df_station_record = df_bestfit[df_bestfit['best_fit_sort'] == i+1].sort_values(by=['n', label_station], ascending=False)
    df_station_record = df_station_record.reset_index(drop=True)
    df_station_record.index.name = 'id'
    if minimum_sample > 0:
        df_station_record = df_station_record[df_station_record['n'] >= minimum_sample]
    df_station_record = df_station_record.sort_values(by=['empirical_dist', 'p_dist', 'delta'], ascending=[True, True, True])
    funcs.print_log(file_log, f'\n\n\n### Best fit in sort position # {i+1}\n\n{df_station_record.to_markdown()}', center_div=False, on_screen = print_on_screen)

# Footer
funcs.print_log(file_log, f'\n\n<sub>{dictionary.dicts['disclaimer']}</sub>', on_screen = print_on_screen)
import pandas as pd
import glob
import os
import tabulate # required for print tables in Markdown using pandas
import functions as funcs
import dictionary as dictionary

# General setup
app_version = 'v20251229'
input_path = 'dataset/pmax24h_out/table/' # Your local input file folder
output_path = 'dataset/pmax24h_out/paper/' # Your local output file folder
station_catalog_file = 'dataset/CNE.xls' # CNE catalog for stations info
station_catalog_columns_drop = ['OBSERVACION', 'SUBRED'] # Dropped columns from CNE
label_station = 'station' # Station column name to eval from .csv station dataset file
label_station_catalog = 'CODIGO' # Station column code in CNE_IDEAM.xls
label_name = 'NOMBRE' # Station column nome in CNE_IDEAM.xls
label_category = 'CATEGORIA' # Station column category in CNE_IDEAM.xls
label_technology = 'TECNOLOGIA' # Station column technology in CNE_IDEAM.xls
label_active = 'ESTADO' # Station column active in CNE_IDEAM.xls
label_install_date = 'FECHA_INSTALACION' # Station column activation date in CNE_IDEAM.xls
label_latitude = 'LATITUD' # Station column latitude in CNE_IDEAM.xls
label_longitude = 'LONGITUD' # Station column longitude in CNE_IDEAM.xls
label_state = 'DEPARTAMENTO' # Station column state in CNE_IDEAM.xls
label_county = 'MUNICIPIO' # Station column county in CNE_IDEAM.xls
label_AH = 'AREA_HIDROGRAFICA' # Station column hydrographic area in CNE_IDEAM.xls
label_ZH = 'ZONA_HIDROGRAFICA' # Station column hydrographic zone in CNE_IDEAM.xls
label_SZH = 'SUBZONA_HIDROGRAFICA' # Station column hydrographic subzone in CNE_IDEAM.xls
print_on_screen = False # Global print control in screen
file_log_name = f'{output_path}{'paper'}.md'  # Markdown file log
file_log = open(file_log_name, 'w+', encoding='utf-8')   # w+ create the file if it doesn't exist
dpi = 96 # Graph plot resolution
create_geojson_map = True
only_automatic_stations = True  # Evaluated only stations with automatic technology avoiding only conventional ones
automatic_tag_not_in = ['(No data)'] # Tag to exclude. Keep in mind some conventional stations are now automatic
#automatic_tag_not_in = ['Convencional', '(No data)'] # Tag to exclude. Keep in mind some conventional stations are now automatic
stations_to_exclude = ['25020230', '25020240', '25020250', '25020260', '25020280', '25020690', '25020920', '25021240', '25021650', '25025250', '28010070', '28020080', '28020150', '28020230', '28020310', '28020420', '28020440', '28020460', '28020600', '28025070', '28025080', '28025090', '28035010', '28035040', '28040310', '28040350']


# Header & join best fit .csv results files and read and filter the CNE catalog
funcs.print_log(file_log, '<img alt="R.HydroTools" src="../../../../../file/graph/R.HydroTools.svg" width="250px">', center_div=True, on_screen = print_on_screen)
funcs.print_log(file_log, '# PMP paper\n', center_div=False, on_screen = print_on_screen)
extension = 'csv'
all_filenames = [i for i in glob.glob(os.path.join(input_path, 'bestfit_*.{}'.format(extension)))]
df_bestfit = pd.concat([pd.read_csv(f) for f in all_filenames], ignore_index=True)
df_bestfit[label_station] = df_bestfit[label_station].astype(str)
df_bestfit = df_bestfit[~df_bestfit[label_station].isin(stations_to_exclude)] # Excluding stations using isin() with Boolean Negation (~)
#print(f'\ndf_bestfit types: \n{df_bestfit.dtypes}')
df_bestfit.to_csv(f'{output_path}bestfit.csv', index=False, encoding='utf-8')
print(f'\nSuccessfully combined {len(all_filenames)} files into combined_output.csv')
stations = df_bestfit[label_station].unique()
df_stations = pd.DataFrame(stations, columns=[label_station])
#print(f'\ndf_stations types:\n{df_stations.dtypes}')
#print(f'Stations in dataset:\n{stations}\n')
# Read and filter CNE catalog
data_types = {label_station_catalog: 'str', label_latitude: 'float64', label_longitude: 'float64'}
df_catalog = pd.read_excel(station_catalog_file, sheet_name='CNE', parse_dates=True, dtype=data_types) # , dtype=data_types
df_catalog = df_catalog.drop(columns=station_catalog_columns_drop)
#print(f'\ndf_catalog types: \n{df_catalog.dtypes}')
#print(df_catalog.head())
if only_automatic_stations:
    #df_catalog = df_catalog[df_catalog[label_technology] != automatic_tag_not_in]
    df_catalog = df_catalog[~df_catalog[label_technology].isin(automatic_tag_not_in)] # Excluding stations using isin() with Boolean Negation (~)
df_catalog = df_catalog[~df_catalog[label_station_catalog].isin(stations_to_exclude)] # Excluding stations using isin() with Boolean Negation (~)
df_catalog_filter = df_catalog[df_catalog[label_station_catalog].isin(df_stations[label_station])]
df_catalog_filter = df_catalog_filter.sort_values(by=[label_station_catalog], ascending=True)
df_catalog_filter = df_catalog_filter.reset_index(drop=True)
df_catalog_filter.index.name = 'id'
#print(f'\nfiltered_df types: \n{filtered_df.dtypes}')
#print(f'\n{df_catalog_filter.head().to_markdown()}')
df_catalog_filter_selected_columns = df_catalog_filter[[label_station_catalog, label_name, label_category, label_technology, label_active, label_install_date, label_latitude, label_longitude, label_state, label_county]]


# Create GeoJSON map
if create_geojson_map:
    funcs.print_log(file_log, 'Dynamic map', center_div=True, on_screen = print_on_screen)
    funcs.print_log(file_log, '```topojson\n{"type": "Topology", "objects": {"example": {"type": "GeometryCollection","geometries": [\n', on_screen = print_on_screen)
    for index, row in df_catalog_filter_selected_columns.iterrows():
        #print (index)
        #print(f"Code: {row['CODIGO']}, Name: {row['NOMBRE']}")
        properties = (f'"Code": "{row[label_station_catalog]}", "Name": "{row[label_name]}", "Category": "{row[label_category]}", "Technology": "{row[label_technology]}", "Active": "{row[label_active]}", "Installation date": "{row[label_install_date]}", "Latitude": "{row[label_latitude]}", "Longitude": "{row[label_longitude]}", "State": "{row[label_state]}", "County": "{row[label_county]}"')
        print_geojson = '{"type": "Point","properties": {'+str(properties)+'},"coordinates": [' + str(row[label_longitude]) + ',' + str(row[label_latitude]) + ']}'
        funcs.print_log(file_log, print_geojson, on_screen = print_on_screen)
        if index <= len(df_catalog_filter) - 2:
            funcs.print_log(file_log, ',\n', on_screen = print_on_screen)
        else:
            funcs.print_log(file_log, '\n', on_screen = print_on_screen)
    funcs.print_log(file_log, ']}}}\n\n```', on_screen = print_on_screen)


# Stations list & Static map
fig_file0a = 'locationmap.png'
df_catalog_filter.to_csv(f'{output_path}stations.csv', index=False)
funcs.print_log(file_log, f'\n\n## Stations evaluated\n\n', center_div=False, on_screen = print_on_screen)
funcs.print_log(file_log, f'> {dictionary.dicts['limnimetric']}\n', on_screen = print_on_screen)
funcs.print_log(file_log, f'>\n> {dictionary.dicts['conventional_station']}\n\n', on_screen = print_on_screen)
funcs.print_log(file_log, f'\n:file_folder:Filtered tables: [Stations dataset](stations.csv), [Bestfit probability distributions](bestfit.csv).\n\n', on_screen = print_on_screen) #######################
funcs.print_log(file_log, f'<img alt="R.HydroTools" src="{fig_file0a}" width="500"></img>', center_div=True, on_screen = print_on_screen)
#funcs.print_log(file_log, f'\n\n{df_catalog_filter.to_markdown()}', center_div=False, on_screen = print_on_screen) # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
print(f'\nFiltered stations catalog:\n{df_catalog_filter.to_markdown()}') # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
funcs.print_log(file_log, 'Stations list: ', center_div=False, on_screen = print_on_screen)
for index, row in df_catalog_filter_selected_columns.iterrows():
    station_url = (f'•[{row[label_station_catalog]}](../{row[label_station_catalog]}.md)')
    funcs.print_log(file_log, f'{station_url} ', on_screen=print_on_screen)
    '''
    if index <= len(df_catalog_filter) - 2:
        funcs.print_log(file_log, f'{station_url}, ', on_screen=print_on_screen)
    else:
        funcs.print_log(file_log, f'{station_url}.', on_screen=print_on_screen)
    '''
location_map_plot = funcs.location_map_multiple(df_catalog_filter_selected_columns, label_latitude, label_longitude)
location_map_plot.savefig(output_path + fig_file0a, dpi=dpi)
#location_map_plot.show()


# Stations catalog general statistics
general_stat_vars = [label_category, label_technology, label_active, label_state, label_AH, label_ZH]
funcs.print_log(file_log, f'\n\n', center_div=False, on_screen=print_on_screen)
for general in general_stat_vars:
    catalog_count=df_catalog_filter[general].value_counts().reset_index(name='Count').sort_values(by=general)
    catalog_count = catalog_count.reset_index(drop=True)
    catalog_count.index.name = 'id'
    funcs.print_log(file_log, f'Stations by {general}  \n{catalog_count.to_markdown()}', center_div=True, on_screen = print_on_screen)

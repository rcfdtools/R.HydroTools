# https://github.com/rcfdtools/R.HydroTools/tree/main/tool/Population
# population_all.py: script for complete population projections with reports by .md file
# Location map are stored in https://github.com/rcfdtools/R.GISMobile/tree/main/file/gis/MiniMAP

# Libraries
# Requires the library openpyxl: pip install pandas openpyxl xlrd
import platform
import functions as funcs
import dictionary as dictionary
import pandas as pd
import numpy as np
import tabulate
import matplotlib.pyplot as plt
from simpledbf import Dbf5
from datetime import datetime
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# General Setup
app_version = 'v20260806'
file_path = '../data/Population.xlsx' # Census database
file_path_rups = '../data/RUPS.csv' # Public service companies database
county_list = ['All'] # ● Enter 'All' or specific County codes to be processed, e.g. ['25817', '25899'] for 25817 - Tocancipá, 25899 - Zipaquirá, 15667 - San Luis de Gaceno, 11001 - Bogotá, D.C., 50689 - San Martín - Meta
projection_year_max = 2050 # ● Projection year
process_polynomial_d2_up = False # ● Polynomial projection over grade 2 is not recommend because over fit the obtained values
process_wappaus = True # Projection only recommend for short term periods and condition_value < 200, evaluated automatically
set_negative_to_zero = True
set_infinite_to_zero = True
drop_dataset_notes = True
create_plot = False # ● Create or update plots
show_plot = False # Show plot on Python console
country_code = '57'
minimap_link = 'https://github.com/rcfdtools/R.GISMobile/blob/main/file/gis/MiniMAP/'
dpi = 96 # Graph plot resolution
print_on_screen = False # Global print control in screen
zone_vars = ['Total', 'Urban', 'Rural']
water_supply = pd.DataFrame({'CZ': [1000, 2000, 99999], 'WS': [120, 130, 140]}) # Water supply in liters per capita per day - lpcd: Level or elevation, Water Supply
runtime = datetime.now()
python_version = platform.python_version()
pandas_version = pd.__version__
numpy_version = np.__version__
unicode_translation_table = str.maketrans("áéíóúüñÇÁÉÍÓÚÜÑ", "aeiouunCAEIOUUN")
rups_state_name_var = 'DEPARTAMENTO_PRESTACION' # Column state name in RUPS.csv
rups_county_name_var = 'MUNICIPIO_PRESTACION' # Column county name in RUPS.csv
rups_phone_var = 'TELEFONO' # Column phone in RUPS.csv
rups_service_var = 'SERVICIO' # Column phone in RUPS.csv
rups_record_type_var = 'TIPO_INSCRIPCION' # Column record type in RUPS.csv
rups_ceo_var = 'REPRESENTANTE_LEGAL' # Column CEO in RUPS.csv
rups_service_var_drop = 'ASEO' # Values to exclude

# Read general census, RUPS and shapefile database
dtype = {'Year': int, 'CountyID': str, 'StateID': str, 'PTotal': int, 'PUrban': int, 'PRural': int}
dtype_rups = {rups_phone_var: str}
df = pd.read_excel(file_path, sheet_name='Population', dtype=dtype)
df = df.sort_values(by=['CountyID', 'Year'])
if drop_dataset_notes: df = df.drop(columns=['Notes'])
df_rups = pd.read_csv(file_path_rups, encoding='utf-8', dtype=dtype_rups)
df_rups = df_rups.sort_values(by=[rups_state_name_var, rups_county_name_var])
#print(df_rups.to_markdown())
dbf = Dbf5('../shp/ColombiaCounty4326.dbf', codec='cp1252')
df_shapefile = pd.DataFrame(dbf.to_dataframe())
df_shapefile = df_shapefile[['CountyID', 'Latitude', 'Longitude']]

# Pre-processing
if county_list[0] == 'All':
    county_list = df['CountyID'].unique()
run_percentage = 1
print(f'Counties to process: {len(county_list)}\n')
for county_id in county_list:
    print(f'Processing ({run_percentage:04d} → {round((run_percentage/len(county_list))*100, 2):.2f}%): {county_id}')
    file_log_name = f'../report/{county_id}.md'  # Markdown file log
    file_log = open(file_log_name, 'w+', encoding='utf-8')  # w+ create the file if it doesn't exist
    filtered_df = df[df['CountyID'] == county_id]
    #funcs.print_log(file_log, f'\n>>>> Head ({len(df)} records) <<<<\n{df.head().to_markdown(index=False)}')
    country_name = df[df['CountyID'] == county_id]['CountryName'].values[0]
    state_name = df[df['CountyID'] == county_id]['StateName'].values[0]
    state_name_unicode = state_name.translate(unicode_translation_table)
    county_name = df[df['CountyID'] == county_id]['CountyName'].values[0]
    county_name_unicode = county_name.translate(unicode_translation_table)
    df_rups_county = df_rups[(df_rups[rups_state_name_var] == state_name_unicode.upper()) & (df_rups[rups_county_name_var] == county_name_unicode.upper())] ##########
    subtitle = f'{country_name} - {state_name} - {county_name} (ID: {county_id})'
    subtitle_location_map = f'{county_name} (ID: {county_id})'
    df_shapefile_info = df_shapefile[df_shapefile['CountyID'] == county_id]
    county_latitude = df_shapefile_info['Latitude'].values[0]
    county_longitude = df_shapefile_info['Longitude'].values[0]
    google_maps_url = f'http://maps.google.com/maps?q={county_latitude},{county_longitude}'
    openstreetmap_url = f'https://www.openstreetmap.org/#map=18/{county_latitude}/{county_longitude}&layers=P'
    bing_map_url = f'https://www.bing.com/maps?cp={county_latitude}~{county_longitude}&lvl=18'
    apple_map_url = f'https://maps.apple.com/frame?center={county_latitude}%2C{county_longitude}&span=0.003%2C0.006'
    geojson = '```geojson\n{\n  "type": "Feature",\n  "geometry": {\n    "type": "Point", \n    "coordinates": [' + str(county_longitude) + ', ' + str(county_latitude) + ']\n  }, \n  "properties": {\n    "Name": "' + subtitle + '"\n  }\n}\n```'
    funcs.print_log(file_log, '<img alt="R.HydroTools" src="../../../../file/graph/R.HydroTools.svg" width="250px">', center_div=True, on_screen = print_on_screen)
    funcs.print_log(file_log, f'# 📜 _“Population and Public Services Demand Projections (PPSD) until Year {projection_year_max} for {subtitle}”_', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n{dictionary.dicts['keywords']}\n\n{dictionary.dicts['study_desc']}\n', on_screen = print_on_screen)
    fig_file0a = f'{minimap_link}{country_code}_{county_id}_LocationMapCountry.png'
    #funcs.print_log(file_log, f'\n\nDataset Types\n\n{df.dtypes.to_markdown()}')
    funcs.print_log(file_log, f'<img alt="rcfdtools" src="{fig_file0a}" width="600"></img>', center_div=True, on_screen=print_on_screen)
    funcs.print_log(file_log, f'\n> **General running parameters**: ', on_screen = print_on_screen)
    for dict_var in dictionary.general_vars:
        funcs.print_log(file_log, f'• {dict_var[1]}: _{eval(dict_var[0])}_. ', on_screen=print_on_screen)
    funcs.print_log(file_log, f'Dynamic map: [:earth_americas:Google]({google_maps_url}) [:earth_americas:OSM]({openstreetmap_url}) [:earth_americas:Bing]({bing_map_url}) [:earth_americas:Apple]({apple_map_url})', center_div=True, on_screen=print_on_screen)
    funcs.print_log(file_log, f'{geojson}', center_div=True, on_screen=print_on_screen)
    # Plot location map & Plot x values
    funcs.print_log(file_log, f'\n\n## 0. Census Data ({len(filtered_df)} records)')
    funcs.print_log(file_log, f'\n\n{dictionary.dicts['census_data']}\n\n📅Global census file: [Population.xlsx](../data/Population.xlsx)', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n\n{filtered_df.sort_values(by='Year').to_markdown(index=False)}')
    funcs.print_log(file_log, f'\n\n> 🔥Some records could had specific notes about the registered values or the corresponding urban or rural distribution.')
    df_rups_county = df_rups_county.drop(columns=[rups_state_name_var, rups_county_name_var, rups_record_type_var, rups_ceo_var])
    df_rups_county = df_rups_county[df_rups_county[rups_service_var] != rups_service_var_drop]
    if len(df_rups_county) > 0:
        funcs.print_log(file_log, f'\n\n📅[SUI-RUPS](https://www.datos.gov.co/Hacienda-y-Cr-dito-P-blico/Registro-nico-de-Prestadores-de-Servicios-P-blicos/4qkq-csdn/about_data) - Local public utility companies: [RUPS.csv](../data/RUPS.xlsx)\n\n {df_rups_county.to_markdown(index=False)}') # {state_name_unicode.upper()} - {county_name_unicode.upper()}

    # Processing by zone
    num = 1 # Counter required for contents table index
    for zone in zone_vars:
        fig_file = '../graph/' + county_id + zone + '.png'  #######################
        fig_file1 = '../graph/' + county_id + zone + 'Bestfit.png'  #######################
        filtered_df = df[df['CountyID'] == county_id]
        max_year = filtered_df['Year'].max()
        min_year = filtered_df['Year'].min()
        x_future = np.arange(min_year, projection_year_max + 1)
        df_projected = pd.DataFrame()
        df_relative_error = pd.DataFrame()
        df_projected['Year'] = x_future
        df_projected['CountyID'] = county_id
        funcs.print_log(file_log, f'\n\n## {num}. {zone}')

        # Polynomial projection Deg 1
        funcs.print_log(file_log, f'\n\n### {num}.1. Coefficients and Parameters\n\n')
        coefficients_deg1 = np.polyfit(filtered_df['Year'], filtered_df[f'P{zone}'], deg=1)
        c1, c2 = coefficients_deg1[0], coefficients_deg1[1]
        deg1_projection = np.round(c1 * x_future + c2, decimals=0)
        if set_negative_to_zero: deg1_projection[deg1_projection < 0] = 0
        if set_infinite_to_zero: deg1_projection[np.isinf(deg1_projection)] = 0
        deg1_projection[np.isnan(deg1_projection)] = 0  # = np.nan
        df_projected[f'P{zone}PD1'] =  deg1_projection
        funcs.print_log(file_log, f'* (PD1) Polynomial Deg 1: {coefficients_deg1[0]}, {coefficients_deg1[1]} (lineal)\n')

        if process_polynomial_d2_up:
            # Polynomial projection Deg 2
            coefficients_deg2 = np.polyfit(filtered_df['Year'], filtered_df[f'P{zone}'], deg=2)
            c1, c2, c3 = coefficients_deg2[0], coefficients_deg2[1], coefficients_deg2[2]
            deg2_projection = np.round(c1 * x_future**2 + c2 * x_future + c3, decimals=0)
            if set_negative_to_zero: deg2_projection[deg2_projection < 0] = 0
            if set_infinite_to_zero: deg2_projection[np.isinf(deg2_projection)] = 0
            deg2_projection[np.isnan(deg2_projection)] = 0  # = np.nan
            df_projected[f'P{zone}PD2'] =  deg2_projection
            funcs.print_log(file_log, f'* (PD2) Polynomial Deg 2: {coefficients_deg2[0]}, {coefficients_deg2[1]}, {coefficients_deg2[2]}\n')

            # Polynomial projection Deg 3
            coefficients_deg3 = np.polyfit(filtered_df['Year'], filtered_df[f'P{zone}'], deg=3)
            c1, c2, c3, c4 = coefficients_deg3[0], coefficients_deg3[1], coefficients_deg3[2], coefficients_deg3[3]
            deg3_projection = np.round(c1 * x_future**3 + c2 * x_future**2 + c3 * x_future + c4, decimals=0)
            if set_negative_to_zero: deg3_projection[deg3_projection < 0] = 0
            if set_infinite_to_zero: deg3_projection[np.isinf(deg3_projection)] = 0
            deg3_projection[np.isnan(deg3_projection)] = 0  # = np.nan
            df_projected[f'P{zone}PD3'] =  deg3_projection
            funcs.print_log(file_log, f'* (PD3) Polynomial Deg 3: {coefficients_deg3[0]}, {coefficients_deg3[1]}, {coefficients_deg3[2]}, {coefficients_deg3[3]}\n')

            # Polynomial projection Deg 4
            coefficients_deg4 = np.polyfit(filtered_df['Year'], filtered_df[f'P{zone}'], deg=4)
            c1, c2, c3, c4, c5 = coefficients_deg4[0], coefficients_deg4[1], coefficients_deg4[2], coefficients_deg4[3], coefficients_deg4[4]
            deg4_projection = np.round(c1 * x_future**4 + c2 * x_future**3 + c3 * x_future**2 + c4 * x_future + c5, decimals=0)
            if set_negative_to_zero: deg4_projection[deg4_projection < 0] = 0
            if set_infinite_to_zero: deg4_projection[np.isinf(deg4_projection)] = 0
            deg4_projection[np.isnan(deg4_projection)] = 0  # = np.nan
            df_projected[f'P{zone}PD4'] =  deg4_projection
            funcs.print_log(file_log, f'* (PD4) Polynomial Deg 4: {coefficients_deg4[0]}, {coefficients_deg4[1]}, {coefficients_deg4[2]}, {coefficients_deg4[3]}, {coefficients_deg4[4]}\n')

        # Logarithmic projection
        coefficients_logarithmic = np.polyfit(np.log(filtered_df['Year']), filtered_df[f'P{zone}'], deg=1)
        c1, c2 = coefficients_logarithmic[0], coefficients_logarithmic[1]
        logarithmic_projection = np.round(c1 * np.log(x_future) + c2, decimals=0)
        if set_negative_to_zero: logarithmic_projection[logarithmic_projection < 0] = 0
        if set_infinite_to_zero: logarithmic_projection[np.isinf(logarithmic_projection)] = 0
        logarithmic_projection[np.isnan(logarithmic_projection)] = 0  # = np.nan
        df_projected[f'P{zone}Log'] =  logarithmic_projection
        funcs.print_log(file_log, f'* (Log) Logarithmic: {coefficients_logarithmic[0]}, {coefficients_logarithmic[1]}\n')

        # Potential projection
        coefficients_potential = np.polyfit(np.log10(filtered_df['Year']), np.log10(filtered_df[f'P{zone}']), deg=1)
        c1, c2 = coefficients_potential[0], coefficients_potential[1]
        potential_projection = np.round(10**c2 * x_future**c1, decimals=0)
        if set_negative_to_zero: potential_projection[potential_projection < 0] = 0
        if set_infinite_to_zero: potential_projection[np.isinf(potential_projection)] = 0 # = np.nan
        potential_projection[np.isnan(potential_projection)] = 0 # = np.nan
        #if np.isnan(potential_projection).any() == False: ################
        df_projected[f'P{zone}Pow'] =  potential_projection
        funcs.print_log(file_log, f'* (Pow) Potential: {coefficients_potential[0]}, {coefficients_potential[1]}\n')

        # Exponential projection
        coefficients_exponential = np.polyfit(filtered_df['Year'], np.log(filtered_df[f'P{zone}']), deg=1)
        c1, c2 = coefficients_exponential[0], np.exp(coefficients_exponential[1])
        exponential_projection = np.round(c2 * np.exp(c1 * x_future), decimals=0)
        if set_negative_to_zero: exponential_projection[exponential_projection < 0] = 0
        if set_infinite_to_zero: exponential_projection[np.isinf(exponential_projection)] = 0
        exponential_projection[np.isnan(exponential_projection)] = 0  # = np.nan
        df_projected[f'P{zone}Exp'] =  exponential_projection
        funcs.print_log(file_log, f'* (Exp) Exponential: {c1}, {c2}\n')

        # Arithmetical projection
        filtered_df = filtered_df.set_index('Year')
        t_0 = filtered_df.index[0]
        t_end = filtered_df.index[-1]
        p_0 = filtered_df.loc[t_0, f'P{zone}']
        p_end = filtered_df.loc[t_end, f'P{zone}']
        total_growth = p_end - p_0
        elapsed_time = t_end - t_0
        annual_growth = total_growth / elapsed_time
        funcs.print_log(file_log, f'* (Art) Arithmetic: Year diff. {t_end} - {t_0} = {t_end-t_0}, Population diff. {p_end} - {p_0} = {p_end-p_0}, Annual growth = {annual_growth}\n')
        arithmetic_projection = np.round(p_0+((x_future-t_0)*annual_growth), decimals=0)
        if set_negative_to_zero: arithmetic_projection[arithmetic_projection < 0] = 0
        if set_infinite_to_zero: arithmetic_projection[np.isinf(arithmetic_projection)] = 0
        arithmetic_projection[np.isnan(arithmetic_projection)] = 0  # = np.nan
        df_projected[f'P{zone}Art'] =  arithmetic_projection

        # Geometric projection
        annual_growth = (p_end/p_0) ** (1 / elapsed_time) - 1
        funcs.print_log(file_log, f'* (Geo) Geometric: Year diff. {t_end} - {t_0} = {t_end-t_0}, Population diff. {p_end} - {p_0} = {p_end-p_0}, Annual growth % = {annual_growth}\n')
        geometric_projection = np.round(p_end*(1+annual_growth)**(x_future-t_end), decimals=0)
        df_projected[f'P{zone}Geo'] =  geometric_projection
        if set_negative_to_zero: geometric_projection[geometric_projection < 0] = 0
        if set_infinite_to_zero: geometric_projection[np.isinf(geometric_projection)] = 0
        geometric_projection[np.isnan(geometric_projection)] = 0  # = np.nan

        # Wappaus projection (Attention: always locate this method as the last one in the calculation because it shows the detailed Condition values)
        numerator = 200 * (p_end - p_0)
        denominator = (t_end - t_0) * (p_0 + p_end)
        i = numerator / denominator
        condition_value = i * (x_future - t_0)
        funcs.print_log(file_log, f'* (Wap) Wappaus: i = {i}, Condition values only valid for < 200)\n\n')
        funcs.print_log(file_log, f'<sub>\nWappaus condition values: {[f"{x:.2f}" for x in condition_value]}\n</sub>\n')
        if process_wappaus and np.max(condition_value) < 200:
            wappaus_projection = np.round(p_0 * ((200 + condition_value) / (200 - condition_value)), decimals=0)
            if set_negative_to_zero: wappaus_projection[wappaus_projection < 0] = 0
            if set_infinite_to_zero: wappaus_projection[np.isinf(wappaus_projection)] = 0
            wappaus_projection[np.isnan(wappaus_projection)] = 0  # = np.nan
            df_projected[f'P{zone}Wap'] =  wappaus_projection

        # Print and plot results
        funcs.print_log(file_log, f'\n\n### {num}.2. Projected Dataset\n\n{df_projected.to_markdown(index=False)}')
        #funcs.print_log(file_log, f'\n\n### Projected dataset\n\n{df_projected.transpose().to_markdown(index=True)}')
        # funcs.print_log(file_log, f'\n\nPlot must be here...')
        funcs.print_log(file_log, f'<img alt="R.HydroTools" src="{fig_file}" width="600"></img>', center_div=True, on_screen=print_on_screen)
        if create_plot:
            #p = np.poly1d(coefficients_deg1) # Create a 1D polynomial object
            #plt.scatter(filtered_df['Year'], filtered_df[f'P{zone}'], color='black', label='Censal Data')
            plt.scatter(filtered_df.index, filtered_df[f'P{zone}'], color='black', label='Censal Data')
            plt.plot(x_future, deg1_projection, color='black', linestyle='--', lw=1, label=f'(PD1) Polynomial D1 ({int(deg1_projection[-1])})')
            if process_polynomial_d2_up:
                plt.plot(x_future, deg2_projection, color='black', linestyle='-.', lw=1, label=f'(PD2) Polynomial D2 ({int(deg2_projection[-1])})')
                plt.plot(x_future, deg3_projection, color='black', linestyle=':', lw=1, label=f'(PD3) Polynomial D3 ({int(deg3_projection[-1])})')
                plt.plot(x_future, deg4_projection, color='green', linestyle='--', lw=1, label=f'(PD4) Polynomial D4 ({int(deg4_projection[-1])})')
            plt.plot(x_future, logarithmic_projection, color='green', linestyle='-.', lw=1, label=f'(Log) Logarithmic ({int(logarithmic_projection[-1])})')
            plt.plot(x_future, potential_projection, color='green', linestyle=':', lw=1, label=f'(Pow) Potential ({int(potential_projection[-1])})')
            plt.plot(x_future, exponential_projection, color='orange', linestyle='--', lw=1, label=f'(Exp) Exponential ({int(exponential_projection[-1])})')
            plt.plot(x_future, arithmetic_projection, color='orange', linestyle='-.', lw=1, label=f'(Art) Arithmetic ({int(arithmetic_projection[-1])})')
            plt.plot(x_future, geometric_projection, color='orange', linestyle=':', lw=1, label=f'(Geo) Geometric ({int(geometric_projection[-1])})')
            if process_wappaus and np.max(condition_value) < 200:
                plt.plot(x_future, wappaus_projection, color='pink', linestyle='--', lw=1, label=f'(Wap) Wappaus ({int(wappaus_projection[-1])})')
            #plt.plot(filtered_df['Year'], p(filtered_df['Year']), color='red', lw=1, label='Fitted Line')
            plt.xlabel('Year')
            plt.ylabel('Population')
            plt.title(f'{zone} county population projections until year {projection_year_max}\n{subtitle}')
            plt.legend(facecolor='black', frameon=False, framealpha=1)
            plt.grid(visible=True, color='black', linewidth=0.5, linestyle='--', alpha=0.1)
            plt.savefig(fig_file, dpi=dpi) ####################
            if show_plot: plt.show()
            plt.close()

        # Absolute and relative error
        filtered_df = pd.merge(filtered_df, df_projected, left_on='Year', right_on='Year', how='left')
        #funcs.print_log(file_log, f'\n\n# Filtered dataset with projected values\n\n{filtered_df.to_markdown(index=False)}')
        methods = ['PD1', 'Log', 'Pow', 'Exp', 'Art', 'Geo']
        if process_polynomial_d2_up:
            methods.insert(1, 'PD2')
            methods.insert(2, 'PD3')
            methods.insert(3, 'PD4')
        if process_wappaus and np.max(condition_value) < 200: methods.append('Wap')
        methods = [f'P{zone}' + item for item in methods]
        #funcs.print_log(file_log, f'\nMethods: {methods}')
        # Absolute error
        for i in methods:
            filtered_df[f'{i}AbsError'] = abs(filtered_df[i] - filtered_df[f'P{zone}'])
        # Relative error as percentage
        for i in methods:
            filtered_df[f'{i}RelError'] = 100 * filtered_df[f'{i}AbsError'] / filtered_df[f'P{zone}']
        funcs.print_log(file_log, f'\n\n### {num}.3. Best fit with absolute and relative error (%)\n\n{dictionary.dicts['abosulute_relative_error']}\n\nAbsolute and relative error\n\n{filtered_df.to_markdown(index=False)}')
        # Mean relative error
        funcs.print_log(file_log, '\n\nRelative error mean\n')
        relative_error = []
        for i in methods:
            relative_error.append(np.mean(filtered_df[f'{i}RelError']))
            #funcs.print_log(file_log, f'{i}: {np.mean(filtered_df[f'{i}RelError'])}')
        df_relative_error = pd.DataFrame({'Method': methods, 'RelError': relative_error})
        min_rel_error = min(df_relative_error['RelError'])
        df_relative_error['Best'] = np.where(df_relative_error['RelError'] == min_rel_error, 'True', '')
        funcs.print_log(file_log, f'\n{df_relative_error.to_markdown(index=False)}')
        #funcs.print_log(file_log, f'\n{min_rel_error:.4f} %')
        best_method = df_relative_error[df_relative_error['Best'] == 'True']['Method'].values[0]
        #funcs.print_log(file_log, f'\nProjected values for best method: {best_method}\n\n{df_projected[['Year', best_method]].transpose().to_markdown(index=True)}')
        #funcs.print_log(file_log, f'\nProjected values for best method: {best_method}\n\n{df_projected[['CountyID', 'Year', best_method]].to_markdown(index=False)}')
        funcs.print_log(file_log, f'\n\n💙Best method: _**{best_method}**_')
        # Plot best method
        # funcs.print_log(file_log, f'\n\nPlot must be here...')
        funcs.print_log(file_log, f'<img alt="R.HydroTools" src="{fig_file1}" width="600"></img>', center_div=True, on_screen=print_on_screen)
        if create_plot:
            plt.scatter(filtered_df['Year'], filtered_df[f'P{zone}'], color='black', label='Censal Data')
            plt.plot(x_future, df_projected[best_method], color='green', linestyle='-', lw=1, label=f'{best_method}')
            #plt.plot(x_future, df_projected[best_method], color='green', marker='o', markersize=3, markerfacecolor='green', markeredgecolor='black', markeredgewidth=0, linestyle='-', lw=1, label=f'{best_method}')
            plt.xlabel('Year')
            plt.ylabel('Population')
            plt.title(f'{zone} county population projections until year {projection_year_max} (Best fit)\n{subtitle}')
            plt.legend(facecolor='black', frameon=False, framealpha=1)
            plt.grid(visible=True, color='black', linewidth=0.5, linestyle='--', alpha=0.1)
            plt.savefig(fig_file1, dpi=dpi)  ####################
            if show_plot: plt.show()
            plt.close()

        # Water supply in liters per capita per day (lpcd)
        funcs.print_log(file_log, f'\n\n### {num}.4. Fresh water supply demand in liters per capita per day (lpcd)\n\n{dictionary.dicts['fresh_water_supply']}\n\n> `CZ`: Level in meters above the sea level (masl)<br> `WS`: Fresh water supply demand in liters per capita per day (lpcd or l/h/d)<br> `WSAll`: Zonal fresh water supply demand in liters per second (l/s)<br> `A`: Zonal area in square meters<br> `DP`: Population density (people/hectare or p/ha)\n\nReference values (RAS Colombia)\n\n{water_supply.to_markdown(index=False)}')
        dbf = Dbf5('../shp/ColombiaCounty4326.dbf', codec='cp1252')
        df_county = pd.DataFrame(dbf.to_dataframe())
        df_county = df_county[df_county['CountyID'] == county_id]
        df_county = df_county[['CountyID', f'A{zone}', f'CZ{zone}']]
        water_supply_conditions = [
            (df_county[f'CZ{zone}'] <= 1000),
            (df_county[f'CZ{zone}'] <= 2000),
            (df_county[f'CZ{zone}'] <= 99999)]
        water_supply_values = [120, 130, 140]
        df_county[f'WS{zone}'] = np.select(water_supply_conditions, water_supply_values, default=0)
        funcs.print_log(file_log, f'\n\nCounty shapefile geometry properties and water supply values\n\n{df_county.to_markdown(index=False)}')
        df_projected = pd.merge(df_projected, df_county, left_on='CountyID', right_on='CountyID', how='left')
        df_projected[f'DP{zone}'] = round(df_projected[best_method] / (df_projected[f'A{zone}']/10000),2) # Population density in people / hectare
        df_projected[f'WS{zone}All'] = (df_projected[best_method] * df_projected[f'WS{zone}'])/86400 # In liters per second (l/s)
        funcs.print_log(file_log, f'\n\nProjected values for best method: {best_method}\n\n{df_projected[['CountyID', 'Year', best_method, f'DP{zone}', f'WS{zone}', f'WS{zone}All']].to_markdown(index=False)}')
        num += 1
    funcs.print_log(file_log, f'\n\n#\n\n<div align="center"><img alt="rcfdtools" src="../graph/qr-code.png" width="250px"><br><sub>Share this research</sub></div><br>', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n\n<sub>{dictionary.dicts['disclaimer']}</sub>', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n\n| [:house: Home](Readme.md)  | [:beginner: Help / Collab](https://github.com/rcfdtools/R.HydroTools/discussions/31) |', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n|----------------------------|-------------------------------------------------------------------------------------------|', on_screen = print_on_screen)
    run_percentage += 1
# Requires the library openpyxl: pip install pandas openpyxl xlrd

# Libraries
import pandas as pd
import tabulate
import numpy as np
import matplotlib.pyplot as plt
from simpledbf import Dbf5

# General vars
file_path = '../data/Population.xlsx'
county_id = '25899' # ● County code to be processed, 25899 - Zipaquirá, 15667 - San Luis de Gaceno, 11001 - Bogotá, D.C., 50689 - San Martín - Meta
projection_year_max = 2050 # ● Projection year
process_polynomial_d2_up = False # ● Projection not recommend for population projections because it over fit correlation values
process_wappaus = False # ● Projection only recommend for short term periods and condition_value < 200
set_negative_to_zero = True
set_infinite_to_zero = True
show_plot = False # Show plot on Python screen console
zone_vars = ['Total', 'Urban', 'Rural']
water_supply = pd.DataFrame({'CZ': [1000, 2000, 99999], 'WS': [120, 130, 140]}) # Water supply in liters per capita per day - lpcd: Level or elevation, Water Supply

# Pre-processing
dtype={'Year': int, 'CountyID': str, 'StateID': str, 'PTotal': int, 'PUrban': int, 'PRural': int}
df = pd.read_excel(file_path, sheet_name='Population', dtype=dtype)
filtered_df = df[df['CountyID'] == county_id]
#print(f'\n>>>> Head ({len(df)} records) <<<<\n{df.head().to_markdown(index=False)}')
country_name = df[df['CountyID'] == county_id]['CountryName'].values[0]
state_name = df[df['CountyID'] == county_id]['StateName'].values[0]
county_name = df[df['CountyID'] == county_id]['CountyName'].values[0]
subtitle = f'{country_name} - {state_name} - {county_name} (ID: {county_id})'
print(f'\n# Population and public services demand projections (PPSD) until Year {projection_year_max} for {subtitle}')
#print(f'\n\nDataset Types\n\n{df.dtypes.to_markdown()}')
print(f'\n\n## Filtered censal dataset ({len(filtered_df)} records)\n\n{filtered_df.to_markdown(index=False)}')

# Processing by zone
for zone in zone_vars:
    filtered_df = df[df['CountyID'] == county_id]
    max_year = filtered_df['Year'].max()
    min_year = filtered_df['Year'].min()
    x_future = np.arange(min_year, projection_year_max + 1)
    df_projected = pd.DataFrame()
    df_relative_error = pd.DataFrame()
    df_projected['Year'] = x_future
    df_projected['CountyID'] = county_id
    print(f'\n\n## {zone} county population projections')

    # Polynomial projection Deg 1
    print(f'\n\n### Coefficients and Parameters\n')
    coefficients_deg1 = np.polyfit(filtered_df['Year'], filtered_df[f'P{zone}'], deg=1)
    c1, c2 = coefficients_deg1[0], coefficients_deg1[1]
    deg1_projection = np.round(c1 * x_future + c2, decimals=0)
    if set_negative_to_zero: deg1_projection[deg1_projection < 0] = 0
    df_projected[f'P{zone}PD1'] =  deg1_projection
    print(f'* (PD1) Polynomial Deg 1: {coefficients_deg1[0]}, {coefficients_deg1[1]} (lineal)')

    if process_polynomial_d2_up:
        # Polynomial projection Deg 2
        coefficients_deg2 = np.polyfit(filtered_df['Year'], filtered_df[f'P{zone}'], deg=2)
        c1, c2, c3 = coefficients_deg2[0], coefficients_deg2[1], coefficients_deg2[2]
        deg2_projection = np.round(c1 * x_future**2 + c2 * x_future + c3, decimals=0)
        if set_negative_to_zero: deg2_projection[deg2_projection < 0] = 0
        df_projected[f'P{zone}PD2'] =  deg2_projection
        print(f'* (PD2) Polynomial Deg 2: {coefficients_deg2[0]}, {coefficients_deg2[1]}, {coefficients_deg2[2]}')

        # Polynomial projection Deg 3
        coefficients_deg3 = np.polyfit(filtered_df['Year'], filtered_df[f'P{zone}'], deg=3)
        c1, c2, c3, c4 = coefficients_deg3[0], coefficients_deg3[1], coefficients_deg3[2], coefficients_deg3[3]
        deg3_projection = np.round(c1 * x_future**3 + c2 * x_future**2 + c3 * x_future + c4, decimals=0)
        if set_negative_to_zero: deg3_projection[deg3_projection < 0] = 0
        df_projected[f'P{zone}PD3'] =  deg3_projection
        print(f'* (PD3) Polynomial Deg 3: {coefficients_deg3[0]}, {coefficients_deg3[1]}, {coefficients_deg3[2]}, {coefficients_deg3[3]}')

        # Polynomial projection Deg 4
        coefficients_deg4 = np.polyfit(filtered_df['Year'], filtered_df[f'P{zone}'], deg=4)
        c1, c2, c3, c4, c5 = coefficients_deg4[0], coefficients_deg4[1], coefficients_deg4[2], coefficients_deg4[3], coefficients_deg4[4]
        deg4_projection = np.round(c1 * x_future**4 + c2 * x_future**3 + c3 * x_future**2 + c4 * x_future + c5, decimals=0)
        if set_negative_to_zero: deg4_projection[deg4_projection < 0] = 0
        df_projected[f'P{zone}PD4'] =  deg4_projection
        print(f'* (PD4) Polynomial Deg 4: {coefficients_deg4[0]}, {coefficients_deg4[1]}, {coefficients_deg4[2]}, {coefficients_deg4[3]}, {coefficients_deg4[4]}')

    # Logarithmic projection
    coefficients_logarithmic = np.polyfit(np.log(filtered_df['Year']), filtered_df[f'P{zone}'], deg=1)
    c1, c2 = coefficients_logarithmic[0], coefficients_logarithmic[1]
    logarithmic_projection = np.round(c1 * np.log(x_future) + c2, decimals=0)
    if set_negative_to_zero: logarithmic_projection[logarithmic_projection < 0] = 0
    df_projected[f'P{zone}Log'] =  logarithmic_projection
    print(f'* (Log) Logarithmic: {coefficients_logarithmic[0]}, {coefficients_logarithmic[1]}')

    # Potential projection
    coefficients_potential = np.polyfit(np.log10(filtered_df['Year']), np.log10(filtered_df[f'P{zone}']), deg=1)
    c1, c2 = coefficients_potential[0], coefficients_potential[1]
    potential_projection = np.round(10**c2 * x_future**c1, decimals=0)
    if set_negative_to_zero: potential_projection[potential_projection < 0] = 0
    if set_infinite_to_zero: potential_projection[np.isinf(potential_projection)] = 0 # = np.nan
    df_projected[f'P{zone}Pow'] =  potential_projection
    print(f'* (Pow) Potential: {coefficients_potential[0]}, {coefficients_potential[1]}')

    # Exponential projection
    coefficients_exponential = np.polyfit(filtered_df['Year'], np.log(filtered_df[f'P{zone}']), deg=1)
    c1, c2 = coefficients_exponential[0], np.exp(coefficients_exponential[1])
    exponential_projection = np.round(c2 * np.exp(c1 * x_future), decimals=0)
    if set_negative_to_zero: exponential_projection[exponential_projection < 0] = 0
    df_projected[f'P{zone}Exp'] =  exponential_projection
    print(f'* (Exp) Exponential: {c1}, {c2}')

    # Arithmetical projection
    filtered_df = filtered_df.set_index('Year')
    t_0 = filtered_df.index[0]
    t_end = filtered_df.index[-1]
    p_0 = filtered_df.loc[t_0, f'P{zone}']
    p_end = filtered_df.loc[t_end, f'P{zone}']
    total_growth = p_end - p_0
    elapsed_time = t_end - t_0
    annual_growth = total_growth / elapsed_time
    print(f'* (Art) Arithmetic: Year diff. {t_end} - {t_0} = {t_end-t_0}, Population diff. {p_end} - {p_0} = {p_end-p_0}, Annual growth {annual_growth}')
    arithmetic_projection = np.round(p_0+((x_future-t_0)*annual_growth), decimals=0)
    df_projected[f'P{zone}Art'] =  arithmetic_projection
    if set_negative_to_zero: arithmetic_projection[arithmetic_projection < 0] = 0

    # Geometric projection
    annual_growth = (p_end/p_0) ** (1 / elapsed_time) - 1
    print(f'* (Geo) Geometric: Year diff. {t_end} - {t_0} = {t_end-t_0}, Population diff. {p_end} - {p_0} = {p_end-p_0}, Annual growth % {annual_growth}')
    geometric_projection = np.round(p_end*(1+annual_growth)**(x_future-t_end), decimals=0)
    df_projected[f'P{zone}Geo'] =  geometric_projection
    if set_negative_to_zero: geometric_projection[geometric_projection < 0] = 0

    # Wappaus projection (Attention: always locate this method as the last one in the calculation because it shows the detailed Condition values)
    if process_wappaus:
        numerator = 200 * (p_end - p_0)
        denominator = (t_end - t_0) * (p_0 + p_end)
        i = numerator / denominator
        condition_value = i * (x_future - t_0)
        print(f'* (Wap) Wappaus: i = {i}')
        print(f'\n(Wap) Wappaus - Condition values (Method only applicable for < 200)\n\n{condition_value}')
        wappaus_projection = np.round(p_0 * ((200 + condition_value) / (200 - condition_value)), decimals=0)
        df_projected[f'P{zone}Wap'] =  wappaus_projection
        if set_negative_to_zero: wappaus_projection[wappaus_projection < 0] = 0

    # Print and plot results
    print(f'\n\n### Projected dataset\n\n{df_projected.to_markdown(index=False)}')
    #print(f'\n\n### Projected dataset\n\n{df_projected.transpose().to_markdown(index=True)}')
    print(f'\nPlot must be here...')
    if show_plot:
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
        if process_wappaus:
            plt.plot(x_future, wappaus_projection, color='pink', linestyle='--', lw=1, label=f'(Wap) Wappaus ({int(wappaus_projection[-1])})')
        #plt.plot(filtered_df['Year'], p(filtered_df['Year']), color='red', lw=1, label='Fitted Line')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title(f'{zone} county population projections until year {projection_year_max}\n{subtitle}')
        plt.legend(facecolor='black', frameon=False, framealpha=1)
        plt.grid(visible=True, color='black', linewidth=0.5, linestyle='--', alpha=0.1)
        plt.show()
        plt.close()

    # Absolute and relative error
    filtered_df = pd.merge(filtered_df, df_projected, left_on='Year', right_on='Year', how='left')
    #print(f'\n\n# Filtered dataset with projected values\n\n{filtered_df.to_markdown(index=False)}')
    methods = ['PD1', 'Log', 'Pow', 'Exp', 'Art', 'Geo']
    if process_polynomial_d2_up:
        methods.insert(1, 'PD2')
        methods.insert(2, 'PD3')
        methods.insert(3, 'PD4')
    if process_wappaus: methods.append('Wap')
    methods = [f'P{zone}' + item for item in methods]
    #print(f'\nMethods: {methods}')
    # Absolute error
    for i in methods:
        filtered_df[f'{i}AbsError'] = abs(filtered_df[i] - filtered_df[f'P{zone}'])
    # Relative error as percentage
    for i in methods:
        filtered_df[f'{i}RelError'] = 100 * filtered_df[f'{i}AbsError'] / filtered_df[f'P{zone}']
    print(f'\n\n### Filtered dataset with projected values, absolute error, relative error as percentage\n\nAbsolute and relative error\n\n{filtered_df.to_markdown(index=False)}')
    # Mean relative error
    print('\nRelative error mean')
    relative_error = []
    for i in methods:
        relative_error.append(np.mean(filtered_df[f'{i}RelError']))
        #print(f'{i}: {np.mean(filtered_df[f'{i}RelError'])}')
    df_relative_error = pd.DataFrame({'Method': methods, 'RelError': relative_error})
    min_rel_error = min(df_relative_error['RelError'])
    df_relative_error['Best'] = np.where(df_relative_error['RelError'] == min_rel_error, 'True', '')
    print(f'\n{df_relative_error.to_markdown(index=False)}')
    #print(f'\n{min_rel_error:.4f} %')
    best_method = df_relative_error[df_relative_error['Best'] == 'True']['Method'].values[0]
    #print(f'\nProjected values for best method: {best_method}\n\n{df_projected[['Year', best_method]].transpose().to_markdown(index=True)}')
    #print(f'\nProjected values for best method: {best_method}\n\n{df_projected[['CountyID', 'Year', best_method]].to_markdown(index=False)}')
    print(f'\nBest method: {best_method}')
    # Plot best method
    print(f'\nPlot must be here...')
    if show_plot:
        plt.scatter(filtered_df['Year'], filtered_df[f'P{zone}'], color='black', label='Censal Data')
        plt.plot(x_future, df_projected[best_method], color='green', linestyle='-', lw=1, label=f'{best_method}')
        #plt.plot(x_future, df_projected[best_method], color='green', marker='o', markersize=3, markerfacecolor='green', markeredgecolor='black', markeredgewidth=0, linestyle='-', lw=1, label=f'{best_method}')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title(f'{zone} county population projections until year {projection_year_max} (Best fit)\n{subtitle}')
        plt.legend(facecolor='black', frameon=False, framealpha=1)
        plt.grid(visible=True, color='black', linewidth=0.5, linestyle='--', alpha=0.1)
        plt.show()
        plt.close()

    # Water supply in liters per capita per day - lpcd
    print(f'\n\n### Water supply in Liters per capita per day - lpcd\n\nReference values (RAS Colombia)\n\n{water_supply.to_markdown(index=False)}\n\n> CZ: Level in meters above the sea level (masl).\n> WS: WaterSupply in liters per capita per day (lpcd or l/h/d).\n> WSAll: WaterSupply in liters per second (l/s).\n> A: Zonal area in square meters.')
    dbf = Dbf5('../shp/ColombiaCounty.dbf')
    df_county = pd.DataFrame(dbf.to_dataframe())
    df_county = df_county[df_county['CountyID'] == county_id]
    df_county = df_county[['CountyID', f'A{zone}', f'CZ{zone}']]
    water_supply_conditions = [
        (df_county[f'CZ{zone}'] <= 1000),
        (df_county[f'CZ{zone}'] <= 2000),
        (df_county[f'CZ{zone}'] <= 99999)]
    water_supply_values = [120, 130, 140]
    df_county[f'WS{zone}'] = np.select(water_supply_conditions, water_supply_values, default=0)
    print(f'\nCounty shapefile geometry properties and water supply values\n\n{df_county.to_markdown(index=False)}')
    df_projected = pd.merge(df_projected, df_county, left_on='CountyID', right_on='CountyID', how='left')
    df_projected[f'WS{zone}All'] = (df_projected[best_method] * df_projected[f'WS{zone}'])/86400 # In liters per second (cms)
    print(f'\nProjected values for best method: {best_method}\n\n{df_projected[['CountyID', 'Year', best_method, f'WS{zone}', f'WS{zone}All']].to_markdown(index=False)}')


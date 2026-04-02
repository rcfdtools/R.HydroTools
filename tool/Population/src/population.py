# Requires the library openpyxl: pip install pandas openpyxl xlrd

# Libraries
import pandas as pd
import tabulate
import numpy as np
import matplotlib.pyplot as plt

# General vars
file_path = '../data/PopulationTest.xlsx'
county_id = '25899' # ● County code to be processed, 25899 - Zipaquirá, 15667 - San Luis de Gaceno
population_col = 'PTotal' # ● PTotal, PUrban, PRural
projection_year_max = 2051 # ● Projection year
process_polynomial_d2_up = False # ● Doesn't recommend for population projections
set_negative_to_zero = True
show_plot = True # Show plot on Python screen console

# Processing
dtype={'Year': int, 'CountyID': str, 'StateID': str, 'PTotal': int, 'PUrban': int, 'PRural': int}
df = pd.read_excel(file_path, sheet_name='Population', dtype=dtype)
print(f'\n\n## Dataset Types\n\n{df.dtypes.to_markdown()}')
#print(f'\n>>>> Head ({len(df)} records) <<<<\n{df.head().to_markdown(index=False)}')
df_projected = pd.DataFrame()
filtered_df = df[df['CountyID'] == county_id]
max_year = filtered_df['Year'].max()
min_year = filtered_df['Year'].min()
county_name = filtered_df[filtered_df['CountyID'] == county_id]['CountyName'].values[0]
state_name = filtered_df[filtered_df['CountyID'] == county_id]['StateName'].values[0]
x_future = np.arange(min_year, projection_year_max+1)
df_projected['YearPrj'] =  x_future
print(f'\n\n## Censal Filter ({len(filtered_df)} records)\n\n{filtered_df.to_markdown(index=False)}')

# Polynomial projection Deg 1
print(f'\n\n## Coefficients and Parameters\n')
coefficients_deg1 = np.polyfit(filtered_df['Year'], filtered_df[population_col], deg=1)
c1, c2 = coefficients_deg1[0], coefficients_deg1[1]
deg1_projection = np.round(c1 * x_future + c2, decimals=0)
if set_negative_to_zero: deg1_projection[deg1_projection < 0] = 0
df_projected[f'{population_col}PD1'] =  deg1_projection
print(f'* (PD1) Polynomial Deg 1: {coefficients_deg1[0]}, {coefficients_deg1[1]} (lineal)')

if process_polynomial_d2_up:
    # Polynomial projection Deg 2
    coefficients_deg2 = np.polyfit(filtered_df['Year'], filtered_df[population_col], deg=2)
    c1, c2, c3 = coefficients_deg2[0], coefficients_deg2[1], coefficients_deg2[2]
    deg2_projection = np.round(c1 * x_future**2 + c2 * x_future + c3, decimals=0)
    if set_negative_to_zero: deg2_projection[deg2_projection < 0] = 0
    df_projected[f'{population_col}PD2'] =  deg2_projection
    print(f'* (PD2) Polynomial Deg 2: {coefficients_deg2[0]}, {coefficients_deg2[1]}, {coefficients_deg2[2]}')

    # Polynomial projection Deg 3
    coefficients_deg3 = np.polyfit(filtered_df['Year'], filtered_df[population_col], deg=3)
    c1, c2, c3, c4 = coefficients_deg3[0], coefficients_deg3[1], coefficients_deg3[2], coefficients_deg3[3]
    deg3_projection = np.round(c1 * x_future**3 + c2 * x_future**2 + c3 * x_future + c4, decimals=0)
    if set_negative_to_zero: deg3_projection[deg3_projection < 0] = 0
    df_projected[f'{population_col}PD3'] =  deg3_projection
    print(f'* (PD3) Polynomial Deg 3: {coefficients_deg3[0]}, {coefficients_deg3[1]}, {coefficients_deg3[2]}, {coefficients_deg3[3]}')

    # Polynomial projection Deg 4
    coefficients_deg4 = np.polyfit(filtered_df['Year'], filtered_df[population_col], deg=4)
    c1, c2, c3, c4, c5 = coefficients_deg4[0], coefficients_deg4[1], coefficients_deg4[2], coefficients_deg4[3], coefficients_deg4[4]
    deg4_projection = np.round(c1 * x_future**4 + c2 * x_future**3 + c3 * x_future**2 + c4 * x_future + c5, decimals=0)
    if set_negative_to_zero: deg4_projection[deg4_projection < 0] = 0
    df_projected[f'{population_col}PD4'] =  deg4_projection
    print(f'* (PD4) Polynomial Deg 4: {coefficients_deg4[0]}, {coefficients_deg4[1]}, {coefficients_deg4[2]}, {coefficients_deg4[3]}, {coefficients_deg4[4]}')

# Logarithmic projection
coefficients_logarithmic = np.polyfit(np.log(filtered_df['Year']), filtered_df[population_col], deg=1)
c1, c2 = coefficients_logarithmic[0], coefficients_logarithmic[1]
logarithmic_projection = np.round(c1 * np.log(x_future) + c2, decimals=0)
if set_negative_to_zero: logarithmic_projection[logarithmic_projection < 0] = 0
df_projected[f'{population_col}Log'] =  logarithmic_projection
print(f'* (Log) Logarithmic: {coefficients_logarithmic[0]}, {coefficients_logarithmic[1]}')

# Potential projection
coefficients_potential = np.polyfit(np.log10(filtered_df['Year']), np.log10(filtered_df[population_col]), deg=1)
c1, c2 = coefficients_potential[0], coefficients_potential[1]
potential_projection = np.round(10**c2 * x_future**c1, decimals=0)
if set_negative_to_zero: potential_projection[potential_projection < 0] = 0
df_projected[f'{population_col}Pow'] =  potential_projection
print(f'* (Pow) Potential: {coefficients_potential[0]}, {coefficients_potential[1]}')

# Exponential projection
coefficients_exponential = np.polyfit(filtered_df['Year'], np.log(filtered_df[population_col]), deg=1)
c1, c2 = coefficients_exponential[0], np.exp(coefficients_exponential[1])
exponential_projection = np.round(c2 * np.exp(c1 * x_future), decimals=0)
if set_negative_to_zero: exponential_projection[exponential_projection < 0] = 0
df_projected[f'{population_col}Exp'] =  exponential_projection
print(f'* (Exp) Exponential: {c1}, {c2}')

# Arithmetical projection
filtered_df = filtered_df.set_index('Year')
t_0 = filtered_df.index[0]
t_end = filtered_df.index[-1]
p_0 = filtered_df.loc[t_0, population_col]
p_end = filtered_df.loc[t_end, population_col]
total_growth = p_end - p_0
elapsed_time = t_end - t_0
annual_growth = total_growth / elapsed_time
print(f'* (Art) Arithmetic: Year diff. {t_end} - {t_0} = {t_end-t_0}, Population diff. {p_end} - {p_0} = {p_end-p_0}, Annual growth {annual_growth}')
arithmetic_projection = np.round(p_0+((x_future-t_0)*annual_growth), decimals=0)
df_projected[f'{population_col}Art'] =  arithmetic_projection
if set_negative_to_zero: arithmetic_projection[arithmetic_projection < 0] = 0

# Geometric projection
annual_growth = (p_end/p_0) ** (1 / elapsed_time) - 1
print(f'* (Geo) Geometric: Year diff. {t_end} - {t_0} = {t_end-t_0}, Population diff. {p_end} - {p_0} = {p_end-p_0}, Annual growth % {annual_growth}')
geometric_projection = np.round(p_end*(1+annual_growth)**(x_future-t_end), decimals=0)
df_projected[f'{population_col}Geo'] =  geometric_projection
if set_negative_to_zero: geometric_projection[geometric_projection < 0] = 0


# Print and plot results
print(f'\n\n# Dataset\n\n{df_projected.to_markdown(index=False)}')
if show_plot:
    p = np.poly1d(coefficients_deg1) # Create a 1D polynomial object
    #plt.scatter(filtered_df['Year'], filtered_df[population_col], color='black', label='Censal Data')
    plt.scatter(filtered_df.index, filtered_df[population_col], color='black', label='Censal Data')
    plt.plot(x_future, deg1_projection, color='black', linestyle='--', lw=1, label=f'Polynomial D1 ({int(deg1_projection[-1])})')
    if process_polynomial_d2_up:
        plt.plot(x_future, deg2_projection, color='black', linestyle='-.', lw=1, label=f'Polynomial D2 ({int(deg2_projection[-1])})')
        plt.plot(x_future, deg3_projection, color='black', linestyle=':', lw=1, label=f'Polynomial D3 ({int(deg3_projection[-1])})')
        plt.plot(x_future, deg4_projection, color='green', linestyle='--', lw=1, label=f'Polynomial D4 ({int(deg4_projection[-1])})')
    plt.plot(x_future, logarithmic_projection, color='green', linestyle='-.', lw=1, label=f'Logarithmic ({int(logarithmic_projection[-1])})')
    plt.plot(x_future, potential_projection, color='green', linestyle=':', lw=1, label=f'Potential ({int(potential_projection[-1])})')
    plt.plot(x_future, exponential_projection, color='orange', linestyle='--', lw=1, label=f'Exponential ({int(exponential_projection[-1])})')
    plt.plot(x_future, arithmetic_projection, color='orange', linestyle='-.', lw=1, label=f'Arithmetic ({int(arithmetic_projection[-1])})')
    plt.plot(x_future, geometric_projection, color='orange', linestyle=':', lw=1, label=f'Geometric ({int(geometric_projection[-1])})')
    #plt.plot(filtered_df['Year'], p(filtered_df['Year']), color='red', lw=1, label='Fitted Line')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title(f'Population Projections Until Year {projection_year_max} for {population_col}\nState: {state_name}, County: {county_name} (County Id: {county_id})')
    plt.legend(facecolor='red', frameon=False, framealpha=1)
    plt.grid(visible=True, color='black', linewidth=0.5, linestyle='--', alpha=0.1)
    plt.show()


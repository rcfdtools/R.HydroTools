# Requires the library openpyxl: pip install pandas openpyxl xlrd

# Libraries
import pandas as pd
import tabulate
import numpy as np
#from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


file_path = '../data/Population.xlsx'
dtype={'Year': int, 'CountyID': str, 'StateID': str, 'PTotal': int, 'PUrban': int, 'PRural': int}
projection_year_max = 2100

# Processing
df = pd.read_excel(file_path, sheet_name='Population', dtype=dtype)
print(f'\n>>>> Types <<<<\n{df.dtypes.to_markdown()}')
#print(f'\n>>>> Head ({len(df)} records) <<<<\n{df.head().to_markdown(index=False)}')


# Linear projection with numpy
filtered_df = df[df['CountyID'] == '15667']
max_year = filtered_df['Year'].max()
min_year = filtered_df['Year'].min()
x_future = np.arange(min_year, projection_year_max)
# filtered_df = filtered_df.set_index('Year')
print(f'\n>>>> Filtered ({len(filtered_df)} records) <<<<\n{filtered_df.to_markdown(index=True)}')
# Polynomial Deg 1
coefficients_deg1 = np.polyfit(filtered_df['Year'], filtered_df['PTotal'], deg=1)
c1, c2 = coefficients_deg1[0], coefficients_deg1[1]
deg1_projection = c1 * x_future + c2
print(f"\ncoefficients Deg 1: {coefficients_deg1}")
print(f'Grade 1: {deg1_projection}')
# Polynomial Deg 2
coefficients_deg2 = np.polyfit(filtered_df['Year'], filtered_df['PTotal'], deg=2)
c1, c2, c3 = coefficients_deg2[0], coefficients_deg2[1], coefficients_deg2[2]
deg2_projection = c1 * x_future**2 + c2 * x_future + c3
print(f"\ncoefficients Deg 2: {coefficients_deg2}")
print(f'Grade 2: {deg2_projection}')
# Polynomial Deg 3
coefficients_deg3 = np.polyfit(filtered_df['Year'], filtered_df['PTotal'], deg=3)
c1, c2, c3, c4 = coefficients_deg3[0], coefficients_deg3[1], coefficients_deg3[2], coefficients_deg3[3]
deg3_projection = c1 * x_future**3 + c2 * x_future**2 + c3 * x_future + c4
print(f"\ncoefficients Deg 2: {coefficients_deg2}")
print(f'Grade 3: {deg3_projection}')
# Polynomial Deg 4
coefficients_deg4 = np.polyfit(filtered_df['Year'], filtered_df['PTotal'], deg=4)
c1, c2, c3, c4, c5 = coefficients_deg4[0], coefficients_deg4[1], coefficients_deg4[2], coefficients_deg4[3], coefficients_deg4[4]
deg4_projection = c1 * x_future**4 + c2 * x_future**3 + c3 * x_future**2 + c4 * x_future + c5
print(f"\ncoefficients Deg 4: {coefficients_deg4}")
print(f'Grade 4: {deg4_projection}')
# Create a polynomial function and plot the results
p = np.poly1d(coefficients_deg1) # Create a 1D polynomial object
plt.scatter(filtered_df['Year'], filtered_df['PTotal'], color='black', label='Original Data')
plt.plot(x_future, deg1_projection, color='black', linestyle='--', lw=1, label='Polynomial Deg 1')
plt.plot(x_future, deg2_projection, color='black', linestyle='-.', lw=1, label='Polynomial Deg 2')
plt.plot(x_future, deg3_projection, color='black', linestyle=':', lw=1, label='Polynomial Deg 3')
plt.plot(x_future, deg4_projection, color='red', linestyle='--', lw=1, label='Polynomial Deg 4')
#plt.plot(filtered_df['Year'], p(filtered_df['Year']), color='red', lw=1, label='Fitted Line')
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Polynomial Fit using numpy.polyfit on Pandas DataFrame')
plt.legend(frameon=False)
plt.show()
# Project for n steps


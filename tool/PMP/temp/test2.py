import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import glob
import os
from scipy.stats import gumbel_l, gumbel_r
import numpy as np
from scipy.stats import pearson3
import math as math


# Join multiple .csv files
'''
folder_path = '../dataset/pmax24h_out/table/'
folder_output = ''
extension = 'csv'
all_filenames = [i for i in glob.glob(os.path.join(folder_path, 'bestfit_*.{}'.format(extension)))]
combined_csv_df = pd.concat([pd.read_csv(f) for f in all_filenames], ignore_index=True)
combined_csv_df.to_csv(f'{folder_output}bestfit.csv', index=False, encoding='utf-8')
print(f'Successfully combined {len(all_filenames)} files into combined_output.csv')
'''


# Pandas dataset sample
'''
station_label = 'Station'
input_path = 'dataset/pmax24h_in/'  # Your local input file folder
ouput_path = 'dataset/pmax24h_out/'  # Your local input file folder
station_file = input_path+'conventional.csv'
df_all = pd.read_csv(station_file, delimiter=',', parse_dates=True)  # index_col=0
stations = df_all[station_label].unique()
for station_code in stations:
    file_log_name = f'{ouput_path}{station_code}.csv'  # Markdown file log
    print(file_log_name)
    df = df_all[df_all[station_label] == station_code]
    print(df)
    # df.to_csv(file_log_name, index=False)
'''

# Geopandas sample
'''
shapefile_location = gpd.read_file('dataset/ColombiaState.shp')
point_latitude = 4.00
point_longitude = -72.00
point_location = Point(point_longitude, point_latitude)
point_gdf = gpd.GeoDataFrame(geometry=[point_location], crs=shapefile_location.crs)
fig, ax = plt.subplots(figsize=(10, 6)) # Adjust figure size as needed
shapefile_location.plot(ax=ax, color='lightgrey', edgecolor='black')
point_gdf.plot(ax=ax, color='darkblue', marker='o', markersize=50) # 'marker' and 'markersize' customize the point
ax.set_title('Shapefile with Point Location')
plt.xlabel('Longitude(°)')
plt.ylabel('Latitude(°)')
ax.annotate(
    'Station',
    xy=(point_longitude, point_latitude),
    xytext=(5, 5), # Offset the text slightly (e.g., 5 points right, 5 points up)
    textcoords='offset points',
    fontsize=10,
    color='black',
    bbox=dict(facecolor='white', alpha=0.5, pad=1)
)
plt.show()
'''

# Gumbel log cumulative distribution function (logcdf) with scipy.stats
'''
rng = np.random.default_rng()
x_values = rng.integers(low=80, high=110, size=10)
print(f'x values: {x_values}\n')
# Calculate the logcdf for the left-skewed Gumbel distribution
# Default loc=0, scale=1
logcdf_l = gumbel_l.logcdf(x_values)
print(f'LogCDF (gumbel_l): {logcdf_l}\n')
# Calculate the logcdf for the right-skewed Gumbel distribution
# Default loc=0, scale=1
logcdf_r = gumbel_r.logcdf(x_values)
print(f'LogCDF (gumbel_r): {logcdf_r}\n')
# You can also specify location (loc) and scale parameters
loc_val = 0.5
scale_val = 2
logcdf_custom = gumbel_r.logcdf(x_values, loc=loc_val, scale=scale_val)
print(f'LogCDF (custom params): {logcdf_custom}')
'''

# Estimate the 100-year flood event (Annual Exceedance Probability AEP = 0.01 or 1% chance) with Log-Pearson3
# Example data (replace with your actual data)
'''
data = np.array([100, 250, 500, 800, 1200, 1500, 2000, 3000, 4500, 6000])
AEP_100yr = 1/50 # Return period Tr = 100
print(f'Estimate the 100-year flood event (Annual Exceedance Probability AEP = 0.01 or 1% chance)\n\nPearson3\nFlow data: {data}')
# Fit the pearson3 distribution
shape, loc, scale = pearson3.fit(data)
print(f"Fitted parameters (shape, loc, scale): ({shape}, {loc}, {scale})")
# Calculate the value using the percent point function (PPF)
flood_100yr = pearson3.ppf(1 - AEP_100yr, shape, loc=loc, scale=scale)
print(f"Estimated 100-year flood (original units): {flood_100yr}")
# Apply natural log transformation
log_data = np.log(data)
print(f'\nLog-Pearson3\nFlow log(data): {log_data}')
# Fit the pearson3 distribution to the log-transformed data
shape, loc, scale = pearson3.fit(log_data)
print(f"Fitted parameters (shape, loc, scale): ({shape}, {loc}, {scale})")
# Calculate the log-value using the percent point function (PPF)
log_flood_100yr = pearson3.ppf(1 - AEP_100yr, shape, loc=loc, scale=scale)
# Convert back to original units using np.exp()
flood_100yr = np.exp(log_flood_100yr)
print(f"Estimated 100-year flood (original units): {flood_100yr}")
'''

# Simple rotated bar plot with python matplotlib sample fit labels
# Data for the plot
'''
categories = ['Category One With A Long Name',
              'Category Two Name',
              'Category Three Is Even Longer',
              'Category Four']
values = [10, 25, 13, 18]
# Create the figure and axes
fig, ax = plt.subplots(figsize=(12, 6)) # Adjust figure size as needed
# Create the bar plot
bars = ax.barh(categories, values)
# Rotate the x-axis labels
# Using rotation=45 degrees and ha='right' (horizontal alignment) often works well
plt.yticks(rotation=45, ha='right')
# Add labels to the bars (optional, but requested)
ax.bar_label(bars, padding=3)
# Set title and axis labels
ax.set_title("Simple Rotated Bar Plot with Labels")
ax.set_ylabel("Values")
# Adjust subplot params to fit labels (prevents labels from being cut off at the bottom)
plt.subplots_adjust(bottom=0.15) # Increase bottom margin as needed
# Display the plot
plt.show()
'''

#print(f'log(0.00001) = {math.log(0.00001)}')

# Python Pandas merge only certain columns
# Sample DataFrames
df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
                    'Age': [27, 24, 22, 32]})

df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
                    'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']})
# Merge DataFrames on the common column 'key'
merged_df = pd.merge(df1, df2[['key', 'Address']], on='key', how='left')
print(merged_df)
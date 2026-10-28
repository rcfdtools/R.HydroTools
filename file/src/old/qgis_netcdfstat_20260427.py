# https://github.com/rcfdtools
# ERA5 / Surface net solar radiation (ssr) / Zonal statistics
# Dataset: ERA5-Land monthly averaged data from 1950 to present
# Polygon layer requieres the area value over a real variable (20, 20) called AGm2

import processing
from qgis.core import QgsRasterLayer, QgsVectorLayer
import pandas as pd
import glob
import os
from datetime import date
from dateutil.relativedelta import relativedelta
import calendar

variable = 'SSR' 
bands = 900 # 900 for 1950 to 2024
original_date = date(1950, 1, 1) # Define a starting date yyyy-m-d
main_path = 'C:/TSIG/'
raster_path = main_path+'grid/ERA5_land_monthly_climatological_var_010dd_ssr_Colombia.tif'
polygon_path = main_path+'shp/ColombiaDptoContinental.shp'
output_path = main_path+'temp/stat/'
output_stat_file = main_path+'table/'+variable+'_stat.csv'
print(f'Temporal output path: {output_path}')

# Run the Zonal Statistics algorithm
for i in range(bands):
    output_file=output_path+variable+'_'+str(i+1)+'.csv'
    print(f'Processing band {i+1} as {variable+str(i+1)+'.csv'}')
    alg_params = {
        'COLUMN_PREFIX': variable+'_',
        'INPUT': polygon_path,
        'INPUT_RASTER': raster_path,
        'RASTER_BAND': 1,
        'STATISTICS': [0,2,4],  # 0-Count,1-Sum,2-Mean,3-Median,4-Standard deviation,5-Minimum,6-Maximum,7-Range,8-Minority (least common value),9-Majority (most common value),10-Variety (unique value count),11-Variance
        'OUTPUT': output_file
    }
    processing.run('native:zonalstatisticsfb', alg_params)

    # Adding fields
    df = pd.read_csv(output_file, encoding='cp1252')
    df['Band'] = i+1
    df['Date'] = original_date + relativedelta(months=i)
    year = (original_date + relativedelta(months=i)).year
    month = (original_date + relativedelta(months=i)).month
    df['Decade'] = (year // 10) * 10
    df['Year'] = year
    df['Month'] = month
    df['MonthDays'] = calendar.monthrange(year, month)[1]
    df['MonthSecs'] = (calendar.monthrange(year, month)[1])*24*60*60
    df[variable+'_Wattm2'] = df[variable+'_mean'] / df['MonthSecs']
    df[variable+'_GWatt'] = df[variable+'_Wattm2'] * df['AGm2'] / 1000000000
    df.to_csv(output_file, index=False)


# Join the .csv stat files
all_csv_files = glob.glob(os.path.join(output_path, '*.csv'))
df_list = []
for file in all_csv_files:
    df = pd.read_csv(file)
    df_list.append(df)
combined_df = pd.concat(df_list, ignore_index=True)
combined_df = combined_df.sort_values(by='Date', ascending=True)
combined_df.to_csv(output_stat_file, index=False)
print(f'Stats file: {output_stat_file}')

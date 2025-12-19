import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Pandas dataset sample
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


# Geopandas sample
shapefile_location = gpd.read_file('dataset/ColombiaState.shp')
point_latitude = 4.00
point_longitude = -72.00
point_location = Point(point_longitude, point_latitude)
point_gdf = gpd.GeoDataFrame(geometry=[point_location], crs=shapefile_location.crs)
fig, ax = plt.subplots(figsize=(10, 6)) # Adjust figure size as needed
shapefile_location.plot(ax=ax, color='lightgrey', edgecolor='black')
point_gdf.plot(ax=ax, color='darkblue', marker='o', markersize=50) # 'marker' and 'markersize' customize the point
ax.set_title("Shapefile with Point Location")
plt.xlabel("Longitude(°)")
plt.ylabel("Latitude(°)")
ax.annotate(
    'Station',
    xy=(point_longitude, point_latitude),
    xytext=(5, 5), # Offset the text slightly (e.g., 5 points right, 5 points up)
    textcoords="offset points",
    fontsize=10,
    color='black',
    bbox=dict(facecolor='white', alpha=0.5, pad=1)
)
plt.show()
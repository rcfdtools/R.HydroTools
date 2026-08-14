# https://github.com/rcfdtools/R.HydroTools/tree/main/tool/Population
# -*- coding: UTF-8 -*-

import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Function for print and show results in a log file
def print_log(file_log, txt_print, on_screen=False, center_div=False):
    # div50 is use for show 2 plots in the same line
    if on_screen:
        print(txt_print)
    if center_div:
        file_log.write('\n<div align="center">\n' + '\n')
    file_log.write(txt_print)
    if center_div:
        file_log.write('\n\n</div>\n' + '\n')

# Location map with GeoPandas (single)
def location_map(point_latitude, point_longitude, point_name, state_filter, county_label_on = False):
    if state_filter == 'All':
        state_shapefile = gpd.read_file('../shp/ColombiaState4326.shp')
        county_shapefile = gpd.read_file('../shp/ColombiaCounty4326.shp')
    else:
        # Under construction
        state_shapefile = gpd.read_file('../shp/ColombiaState4326.shp', where=f"DeCodigo = '{state_filter}'")
        county_shapefile = gpd.read_file('../shp/ColombiaCounty4326.shp', where=f"DeCodigo = '{state_filter}'")
    point_location = Point(point_longitude, point_latitude)
    point_gdf = gpd.GeoDataFrame(geometry=[point_location], crs=state_shapefile.crs)
    fig, ax = plt.subplots(figsize=(6, 6))  # Adjust figure size as needed
    if county_label_on:
        state_shapefile.plot(ax=ax, color='lightgray', edgecolor='black', linewidth=1, legend=True, legend_kwds={'fontsize': 'small'}, label='DeCodigo') # , label='AH'
    else:
        state_shapefile.plot(ax=ax, color='lightgray', edgecolor='black', linewidth=1, legend=True, legend_kwds={'fontsize': 'small'})  # , label='AH'
    #state_shapefile.plot(ax=ax, column='DeCodigo', cmap='Greens', edgecolor='black', linewidth=0.75, legend=True, legend_kwds={'fontsize': 'small'}) # , label='AH'
    county_shapefile.boundary.plot(ax=ax, edgecolor='black', linewidth=0.25) # , label='AH'
    point_gdf.plot(ax=ax, marker='o', color='brown', markersize=40, legend=False)  # color='black', 'marker' and 'markersize' customize the point
    #ax.legend(loc='lower left')
    ax.set_title("Map Location")
    plt.xlabel("Longitude°")
    plt.ylabel("Latitude°")
    ax.tick_params(axis='both', labelsize=9)
    ax.annotate(
        text= point_name,
        xy=(point_longitude, point_latitude),
        xytext=(6, 6),  # Offset the text slightly (e.g., 5 points right, 5 points up)
        textcoords="offset points",
        fontsize=10,
        color='white',
        bbox=dict(boxstyle='round', facecolor='brown', alpha=0.9, pad=0.25)
    )
    return plt

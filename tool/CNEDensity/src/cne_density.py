# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-
# _name: cne_density.py
# Description:
# Requirements:

# Libraries
# import xlrd # Tested with 2.0.1 version. # Has to be installed with not import required.
import pandas as pd
import rasterio
#from rasterio.plot import show
import geopandas as gpd
from rasterstats import point_query

# Functions
def shapefile_export():
    a = 1

# General variables
excel_cne_ideam_file = '../.datasets/CNE_IDEAM.xls'
excel_cne_oe_file = '../.datasets/CNE_OE.xls'
locations_file = '../.datasets/update_locations.csv'  # Attributes has to be: CODIGO,latitud,longitud
category_dict_file = '../.datasets/category_dict.csv'
concat_station_file = '../.datasets/CNE_Concat.csv'
intersect_station_file = '../.datasets/CNE_Concat_Intersect.csv'
dem_file = '../.dem/ASTER/ASTGTMV003.tif'
concat_station_shapefile = '../.shp/CNE_Concat.shp'
intersect_station_shapefile = '../.shp/CNE_Concat_Intersect.shp'
hydro_zone_shapefile = '../.shp/Zonificacion_hidrografica_2013_4326.shp'
objectid_name= 'OBJECTID'
code_name = 'CODIGO'
name_name = 'nombre'
category_name = 'CATEGORIA'
technology_name = 'TECNOLOGIA'
state_active_name = 'ESTADO'
installation_date = 'FECHA_INSTALACION'
elevation_name = 'altitud'
latitude_name = 'latitud'
longitude_name = 'longitud'
geo_state_name = 'DEPARTAMENTO'
geo_county_name = 'MUNICIPIO'
geo_operative_area_name = 'AREA_OPERATIVA'
geo_hydro_area_name = 'AREA_HIDROGRAFICA'
geo_hydro_zone_name = 'ZONA_HIDROGRAFICA'
remark_name = 'observacion'
geo_hydro_subzone_name = 'SUBZONA_HIDROGRAFICA'
state_owned_name = 'ENTIDAD'
stream_name = 'CORRIENTE'
suspension_date = 'FECHA_SUSPENSION'
subnet_name = 'subred'
parse_dates = [installation_date, suspension_date]
converters = {category_name:str, code_name:str, latitude_name:float, longitude_name:float, elevation_name:float}
drop_columns = [objectid_name, technology_name, state_active_name, geo_state_name, geo_county_name, geo_operative_area_name, geo_hydro_area_name, geo_hydro_zone_name, remark_name, geo_hydro_subzone_name, stream_name, subnet_name]
dem_round_pos = 0  # Decimal positions for elevations rounding
pi_number = 3.1415926535897932384626433832795
update_locations = True  # Update locations with locations_file
update_elevations = False  # Calculate elevations with a DEM raster, DEMValue in tables

# Load and concatenate stations catalogs
df_cne_ideam = pd.read_excel(excel_cne_ideam_file, parse_dates=parse_dates, converters=converters)
df_cne_oe = pd.read_excel(excel_cne_oe_file, parse_dates=parse_dates, converters=converters)
df_locations_file = pd.read_csv(locations_file, sep=',', converters = {code_name:str, latitude_name:float, longitude_name:float})
df_category_dict = pd.read_csv(category_dict_file, sep=',', converters = {category_name:str, 'CategId':str, 'CategDesc':str})  # To avoid , encoding='latin-1' file mus be converted first to UTF-8
df_cne_ideam = df_cne_ideam.drop(columns=drop_columns, errors='raise')
df_cne_oe = df_cne_oe.drop(columns=drop_columns, errors='ignore')
df_cne_concat = pd.concat([df_cne_ideam, df_cne_oe], ignore_index=True).set_index([code_name])
df_cne_concat = df_cne_concat.sort_values(by=[code_name])
print('\n%s\n%s\n%s' %(excel_cne_ideam_file, df_cne_ideam, df_cne_ideam.dtypes))
print('\n%s\n%s\n%s' %(excel_cne_oe_file, df_cne_oe, df_cne_oe.dtypes))

# Update locations
print(df_locations_file)
if update_locations:
    df_cne_concat.update(df_locations_file.set_index([code_name]))
    df_cne_concat.reset_index()
df_cne_concat['CODE'] = df_cne_concat.index  # Copy stations code to a new column before the category index change

# Set categories
print('\nCategories dictionary\n%s\n%s' %(df_category_dict, df_category_dict.dtypes))
df_cne_concat['CategId'] = ''
df_cne_concat['WMORadkm'] = ''
df_cne_concat = df_cne_concat.set_index([category_name])
df_cne_concat['CategName'] = df_cne_concat.index  # Copy stations category to a new column before the category index change
df_cne_concat.rename(columns = {'CODE':code_name}, inplace = True)
df_cne_concat.update(df_category_dict.set_index([category_name]))
df_cne_concat.reset_index()
df_cne_concat = df_cne_concat.set_index([code_name])
df_cne_concat.rename(columns = {'CategName':category_name}, inplace = True)

# Truncate column names to 10 characters
df_cne_concat.rename(columns = {code_name:code_name[:10], name_name:name_name[:10], category_name:category_name[:10], installation_date:installation_date[:10], elevation_name:elevation_name[:10], latitude_name:latitude_name[:10], longitude_name:longitude_name[:10], suspension_date:suspension_date[:10], state_owned_name:state_owned_name[:10]}, inplace = True)  # Only for the required analysis columns
print('\nConcatenated dataframe\n%s\n%s' %(df_cne_concat, df_cne_concat.dtypes))
count_stations = int(df_cne_concat.__len__())
print('\nStations: %s' %count_stations)
df_cne_concat.to_csv(concat_station_file)

# Convert to a shapefile without DEM elevations
df_cne_concat[installation_date[:10]] = df_cne_concat[installation_date[:10]].astype(str)  # Shapefile doesn't  support datetime fields
df_cne_concat[suspension_date[:10]] = df_cne_concat[suspension_date[:10]].astype(str)  # Shapefile doesn't  support datetime fields
gdf = gpd.GeoDataFrame(df_cne_concat, geometry=gpd.points_from_xy(df_cne_concat[longitude_name[:10]], df_cne_concat[latitude_name[:10]]), crs="EPSG:4326")
gdf.to_file(concat_station_shapefile)
print('\nGeo dataframe\n%s' % gdf)

# Zonal statistics to get the stations elevations using a DEM
# Attention: the shapefile and the DEM has to use the same CRS, e.g. 4326
df_cne_concat['DEMValue'] = -9999  # Set an initial value
if update_elevations:
    station_dem_value = point_query(concat_station_shapefile, dem_file)
    print(station_dem_value)
    print('Points evaluated: %d' % len(station_dem_value))
    for s in range(len(station_dem_value)):
        if station_dem_value[s] is None:
            df_cne_concat['DEMValue'][s] = df_cne_concat[elevation_name[:10]][s]
        else:
            df_cne_concat['DEMValue'][s] = round(station_dem_value[s], dem_round_pos)
    df_cne_concat.to_csv('../.datasets/CNE_Concat.csv')
    print('CNE with elevations from DEM\n%s' % df_cne_concat)
else:
    df_cne_concat['DEMValue'] = df_cne_concat[elevation_name[:10]]
df_cne_concat.to_csv(concat_station_file)
# Convert to a shapefile with DEM elevations
df_cne_concat[installation_date[:10]] = df_cne_concat[installation_date[:10]].astype(str)  # Shapefile doesn't  support datetime fields
df_cne_concat[suspension_date[:10]] = df_cne_concat[suspension_date[:10]].astype(str)  # Shapefile doesn't  support datetime fields
gdf = gpd.GeoDataFrame(df_cne_concat, geometry=gpd.points_from_xy(df_cne_concat[longitude_name[:10]], df_cne_concat[latitude_name[:10]]), crs="EPSG:4326")
gdf.to_file(concat_station_shapefile)
print('\nGeo dataframe\n%s' % gdf)

# Intersect stations with hydro geo zones
# The shapefile and the DEM has to use the same CRS, e.g. 4326
gdf_station = gpd.read_file(concat_station_shapefile)
gdf_hydro_zone = gpd.read_file(hydro_zone_shapefile)
gdf_intersection = gpd.overlay(gdf_station, gdf_hydro_zone, how='intersection')
gdf_intersection.to_file(intersect_station_shapefile)
pd.DataFrame(gdf_intersection.drop(columns=['geometry']).to_csv(intersect_station_file, index=None))
gdf_hydro_zone_areakm2 = gdf_hydro_zone['Akm2_SZH'].sum()
pd_hydro_zone = pd.DataFrame(gdf_hydro_zone.drop(columns=['geometry']))
print('\nGeo dataframe with intersection\n%s' % gdf_intersection)

# Category summary
df_cne_concat[installation_date[:10]] = df_cne_concat[installation_date[:10]].astype('datetime64[ns]')
df_cne_concat[suspension_date[:10]] = df_cne_concat[suspension_date[:10]].astype('datetime64[ns]')
print('\nProperties types\n%s' % df_cne_concat.dtypes)
print('\nDataframe statistics\n%s' % df_cne_concat.describe())
print('\nCategory analysis with all the stations')
df_category_file = '../.datasets/category_count.csv'
df_category = pd.DataFrame(df_cne_concat[category_name[:10]].value_counts(ascending=False))
df_category.to_csv(df_category_file, header=None)
df_category = pd.read_csv(df_category_file)
df_category.columns = [category_name[:10], 'Count']
df_category['LandAkm2'] = gdf_hydro_zone_areakm2
df_category['Coverkm2'] = gdf_hydro_zone_areakm2 / df_category['Count']
df_category['Radiuskm'] = (df_category['Coverkm2']/pi_number)**0.5
df_category['WMORadkm'] = ''
df_category = df_category.set_index([category_name[:10]])
df_category['CategId'] = ''
df_category.update(df_category_dict.set_index([category_name]))
df_category['WMOCheckRd'] = '1'
df_category['WMOCheckRd'] = df_category['WMOCheckRd'].where(df_category['Radiuskm'] <= df_category['WMORadkm'], '0')
df_category.to_csv(df_category_file, header=True)
print('\n%s' % df_category)

# Hydrographic area (ah) & category summary
print('\nHydrographic area & category analysis')
ah_area_file = '../.datasets/ah_area.csv'
df_ah_area = pd_hydro_zone.pivot_table(index=['NOM_AH'], values='Akm2_SZH', aggfunc='sum', sort=True)
df_ah_area.to_csv(ah_area_file, header=True)
df_ah_area = pd.read_csv(ah_area_file)
ah_category_count_file = '../.datasets/ah_category_count.csv'
print('\nHydrographic áreas, km²\n%s' % df_ah_area)
df_ah_category = pd.read_csv(intersect_station_file)
df_ah_category = df_ah_category.pivot_table(index=['NOM_AH', category_name[:10]], aggfunc='size', sort=True)
df_ah_category.to_csv(ah_category_count_file, header=True)
df_ah_category = pd.read_csv(ah_category_count_file)
df_ah_category.rename(columns = {'0':'Count'}, inplace = True)
df_ah_category['Akm2_SZH'] = 0
df_ah_category = df_ah_category.set_index(['NOM_AH'])
df_ah_category.update(df_ah_area.set_index(['NOM_AH']))
df_ah_category.rename(columns = {'Akm2_SZH':'LandAkm2'}, inplace = True)
df_ah_category['Coverkm2'] = df_ah_category['LandAkm2'] / df_ah_category['Count']
df_ah_category['Radiuskm'] = (df_ah_category['Coverkm2']/pi_number)**0.5
df_ah_category['NOM_AH1'] = df_ah_category.index
df_ah_category = df_ah_category.set_index([category_name[:10]])
df_ah_category['CategId'] = ''
df_ah_category['WMORadkm'] = ''
df_ah_category.rename(columns = {'NOM_AH1':'NOM_AH'}, inplace = True)
df_ah_category.update(df_category_dict.set_index([category_name]))
df_ah_category['WMOCheckRd'] = '1'
df_ah_category['WMOCheckRd'] = df_ah_category['WMOCheckRd'].where(df_ah_category['Radiuskm'] <= df_ah_category['WMORadkm'], '0')
df_ah_category = df_ah_category.reset_index(drop=False)
df_ah_category = df_ah_category[['NOM_AH', 'CategId', category_name[:10], 'LandAkm2', 'Count', 'Coverkm2', 'Radiuskm', 'WMORadkm', 'WMOCheckRd']]
df_ah_category.to_csv(ah_category_count_file, header=True, index=False)
print('\n%s' % df_ah_category)
print('\n> The current analysis includes only the stations located over the land areas from the hydrographic subzones and tide metering stations could be displayed because not updated locations or because some maritim limits was traced with low tide levels.')

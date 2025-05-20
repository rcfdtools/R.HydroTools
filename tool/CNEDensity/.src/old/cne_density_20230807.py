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
def raster_value(raster_file, longitude, latitude):
    raster = rasterio.open(raster_file)
    row, col = raster.index(longitude, latitude)
    return raster.read(1)[row, col]

# General variables
excel_cne_ideam_file = '../.datasets/CNE_IDEAM.xls'
excel_cne_oe_file = '../.datasets/CNE_OE.xls'
locations_file = '../.datasets/update_locations.csv'  # Attributes has to be: CODIGO,latitud,longitud
category_dict_file = '../.datasets/category_dict.csv'
dem_file = '../.dem/ASTER/ASTGTMV003.tif'
station_shapefile= '../.shp/CNE_Concat.shp'
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
update_locations = True  # Update locations with locations_file
update_elevations = False  # Update elevations with a DEM raster


# Preliminary
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
print(df_locations_file)
if update_locations:
    df_cne_concat.update(df_locations_file.set_index([code_name]))
    df_cne_concat.reset_index()
df_cne_concat['CODE'] = df_cne_concat.index  # Move station code to a new column before the category index change
df_cne_concat['CategId'] = ''
print('\nCategories dictionary\n%s\n%s' %(df_category_dict, df_category_dict.dtypes))
df_cne_concat = df_cne_concat.set_index([category_name])
df_cne_concat.rename(columns = {'CODE':code_name}, inplace = True)
df_cne_concat.update(df_category_dict.set_index([category_name]))
df_cne_concat.reset_index()
df_cne_concat = df_cne_concat.set_index([code_name])
# Truncate column names to 10 characters
df_cne_concat.rename(columns = {code_name:code_name[:10], name_name:name_name[:10], installation_date:installation_date[:10], elevation_name:elevation_name[:10], latitude_name:latitude_name[:10], longitude_name:longitude_name[:10], suspension_date:suspension_date[:10], state_owned_name:state_owned_name[:10]}, inplace = True)  # Only for the required analysis columns
print('\nConcatenated dataframe\n%s\n%s' %(df_cne_concat, df_cne_concat.dtypes))
count_stations = int(df_cne_concat.__len__())
print('\nStations: %s' %count_stations)
df_cne_concat.to_csv('../.datasets/CNE_Concat.csv')
# Convert to a shapefile
df_cne_concat[installation_date[:10]] = df_cne_concat[installation_date[:10]].astype(str)  # Shapefile doesn't  support datetime fields
df_cne_concat[suspension_date[:10]] = df_cne_concat[suspension_date[:10]].astype(str)  # Shapefile doesn't  support datetime fields
gdf = gpd.GeoDataFrame(df_cne_concat, geometry=gpd.points_from_xy(df_cne_concat[longitude_name[:10]], df_cne_concat[latitude_name[:10]]), crs="EPSG:4326")
gdf.to_file(station_shapefile)
print('\nGeo dataframe\n%s' % gdf)

# Zonal statistics to get the stations elevations using a DEM
# The shapefile and the DEM has to use the same CRS, e.g. 4326
station_dem_value = point_query(station_shapefile, dem_file)
print(station_dem_value)
print('Points evaluated: %d' % len(station_dem_value))
df_cne_concat['DEMValue'] = -9999  #
for s in range(len(station_dem_value)):
    if station_dem_value[s] is None:
        df_cne_concat['DEMValue'][s] = df_cne_concat[elevation_name[:10]][s]
    else:
        df_cne_concat['DEMValue'][s] = station_dem_value[s]
df_cne_concat.to_csv('../.datasets/CNE_Concat.csv')
print('CNE with elevations from DEM\n%s' % df_cne_concat)


#dem_stat.to_csv('../.datasets/CNE_DEM_Values.csv')

# Stations elevation upgrade from ASTER GDEM v3 raster (obsolete)
if update_elevations:
    print('\nASTER GDEM v3 recalculate elevations in process....')
    df_elevation = pd.DataFrame(columns=[code_name, elevation_name])
    for s in range(count_stations):
        #print('Station: %s' % df_cne_concat[name_name][s])
        #df_new_elevation = pd.DataFrame({code_name: df_cne_concat.index[s], elevation_name: 100})
        elevation_value = raster_value(dem_file, df_cne_concat[longitude_name][s], df_cne_concat[latitude_name][s])
        print('Station: %s Elevation: %f (%d/%d: %f%%)' %(df_cne_concat.index[s], elevation_value, s, count_stations, s/count_stations))
        df_new_elevation = pd.DataFrame({code_name: df_cne_concat.index[s], elevation_name: elevation_value}, index=[0])
        df_elevation = pd.concat([df_elevation, df_new_elevation]).reset_index(drop=True)
    df_elevation = df_elevation.set_index([code_name])
    print('df_elevation\n%s' % df_elevation)




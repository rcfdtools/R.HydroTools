# -*- coding: UTF-8 -*-
# _name: cne_density.py
# Description:
# Requirements:

# Libraries
# import xlrd # Tested with 2.0.1 version. # Has to be installed with not import required.
import pandas as pd
import rasterio
#from rasterio.plot import show

# Functions
def raster_value(raster_file, longitude, latitude):
    raster = rasterio.open(raster_file)
    row, col = raster.index(longitude, latitude)
    return raster.read(1)[row, col]

# General variables
excel_cne_ideam_file = '../.datasets/CNE_IDEAM.xls'
excel_cne_oe_file = '../.datasets/CNE_OE.xls'
locations_table = '../.datasets/update_locations.csv'  # Attributes has to be: CODIGO,latitud,longitud
dem_file = '../.dem/ASTER/ASTGTMV003.tif'
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
stream_name = 'CORRIENTE'
suspension_date = 'FECHA_SUSPENSION'
subnet_name = 'subred'
parse_dates = [installation_date, suspension_date]
converters = {code_name:str, latitude_name:float, longitude_name:float, elevation_name:float}
drop_columns = [objectid_name, technology_name, state_active_name, geo_state_name, geo_county_name, geo_operative_area_name, geo_hydro_area_name, geo_hydro_zone_name, remark_name, geo_hydro_subzone_name, stream_name, subnet_name]
update_locations = True  # Update locations with locations_table

# Preliminary
df_cne_ideam = pd.read_excel(excel_cne_ideam_file, parse_dates=parse_dates, converters=converters)
df_cne_oe = pd.read_excel(excel_cne_oe_file, parse_dates=parse_dates, converters=converters)
df_locations_table = pd.read_csv(locations_table, sep=',', converters = {code_name:str, latitude_name:float, longitude_name:float, elevation_name:float})
df_cne_ideam = df_cne_ideam.drop(columns=drop_columns, errors='raise')
df_cne_oe = df_cne_oe.drop(columns=drop_columns, errors='ignore')
df_cne_concat = pd.concat([df_cne_ideam, df_cne_oe], ignore_index=True).set_index([code_name])
df_cne_concat = df_cne_concat.sort_values(by=[code_name])
print('\n%s\n%s\n%s' %(excel_cne_ideam_file, df_cne_ideam, df_cne_ideam.dtypes))
print('\n%s\n%s\n%s' %(excel_cne_oe_file, df_cne_oe, df_cne_oe.dtypes))
print(df_locations_table)
df_cne_concat.update(df_locations_table.set_index([code_name]))
df_cne_concat.reset_index()
print('\nConcatenated dataframe\n%s\n%s' %(df_cne_concat, df_cne_concat.dtypes))
count_stations = int(df_cne_concat.__len__())
print('Stations: %s' %count_stations)
# Stations elevation upgrade from ASTER GDEM v3 raster
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


df_cne_concat.to_csv('../.datasets/CNE_Concat.csv')


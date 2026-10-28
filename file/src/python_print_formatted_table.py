# https://github.com/rcfdtools
# Print a shapefile table content in console as a Markdown table

# Libraries
import geopandas as gpd
import pandas as pd
import tabulate

# Execution
#shapefile_path = 'D:/R.IAMB/file/shp/SuelosVFAreaProyectoDissolve9377.shp' # ●
#columns = ['UCS_F', 'UCS', 'PAISAJE', 'CLIMA', 'TIPO_RELIE', 'LITOLOGÍA_', 'CARACTERÍS', 'CARACTER_1', 'COMPONENTE', 'PERFIL', 'PORCENTAJE', 'Aha', 'APD'] # ● Complete for SuelosVFAreaProyectoDissolve9377.shp
#columns = ['UCS_F', 'UCS', 'PAISAJE', 'CLIMA', 'COMPONENTE', 'PORCENTAJE', 'Aha', 'APD'] # ● For SuelosVFAreaProyectoDissolve9377.shp
#shapefile_path = 'D:/R.IAMB/file/shp/MunicipiosAreaProyectoClipDissolve9377.shp' # ●
#columns = ['MpCodigo', 'MpNombre', 'ATotalha', 'Aha', 'APD', 'APP'] # ● For MunicipiosAreaProyecto.shp
#shapefile_path = 'D:/R.IAMB/file/shp/VeredaAreaProyectoDissolve9377.shp' # ●
#columns = ['CODIGO_VER', 'NOMBRE_VER', 'NOMB_MPIO', 'NOM_DEP', 'Aha', 'APD'] # ● For VeredaAreaProyectoDissolve9377.shp
shapefile_path = 'D:/R.IAMB/file/shp/GestoresCatastralesAreaProyectoDissolve9377.shp' # ●
columns = ['gestor_cat', 'Aha', 'APD'] # ● For GestoresCatastrales20240301/municipioserviciosV.shp
gdf = gpd.read_file(shapefile_path, columns=columns)
df = pd.DataFrame(gdf).drop(columns=['geometry']) # Convert to Pandas dataframe
df.index.name = 'ID'
df.sort_values(by=columns, inplace=True)
print(df[columns].to_markdown(index=False)) # Print all

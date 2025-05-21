# -*- coding: UTF-8 -*-
# Name: EAAB_CO.py
# Description: this script extract and transform the EAAB SIH SQL Server database into record datasets tables
# Source dataset: www.acueducto.com.co
# Disclaimer: records are under EAAB license
# Repository: https://github.com/rcfdtools/R.GISPython/tree/main/MultipleTableJoin
# License: https://github.com/rcfdtools/R.GISPython/wiki/License
# Requirements: Python 3+, Pandas, sqlalchemy
# Notes: depending of the .csv generate file, at the end of every records are included the properties: cod_elemento, cod_eaab, cod_parametro, unidad,cod_descriptor, nombre_descriptor, cod_flag, nroObs, EtiquetaEAAB, DescripcionSerieEAAB

# Libraries
import pandas as pd
from sqlalchemy import create_engine  # Use a version below 2.0

# Functions
# Table export function
def table_export(sql, table_name):
    df = pd.read_sql(sql, engine)
    print('\nDataframe describe \n',df.describe())
    print('\nData types \n',df.dtypes)
    df.to_csv(output_path+table_name, index=False, encoding='utf-8')
    print('\nDataframe sample \n',df)

# Variables
driver = '{ODBC Driver 17 for SQL Server}'
server = 'ADMIN'  # For instances use ADMIN\MSSQLSERVER where MSSQLSERVER is the instance
database = 'SIH_20210502'
username = 'sa'
password = '123456'
output_path = 'EAAB_CO/'
locations_table = 'eaab_sih_estaciones_update_locations.csv'  # Attributes has to be: cod_elemento,Latitud,Longitud
parameters_table = 'eaab_sih_parametro_homologa_IDEAM.csv'  # Homologate parameters from EAAB to IDEAM, attributes has to be: IdParametro,Etiqueta,EtiquetaIDEAM,DescripcionSerieEAAB,DescripcionSerieIDEAM,Frecuencia
update_locations = True  # Update locations with locations_table
update_parameters = True  # Update parameters with IDEAM values
extract_monthly_values = True  # Extract or update

# Connector
engine = create_engine(
    'mssql+pyodbc://'
    + username
    + ':' + password
    + '@' + server
    + '/' + database + '?'
    + 'driver=ODBC+Driver+17+for+SQL+Server')

# Retrieve table names
print('DB Tables over: %s\%s' % (server, database))
table_name = 'eaab_sih_tables.csv'
sql = "SELECT Distinct TABLE_NAME FROM information_schema.TABLES"
table_export(sql, table_name)

# Retrieve monthly records
table_name = 'eaab_sih_monthly_records.csv'
if extract_monthly_values:
      print('\nExtracting or updating monthly values from: %s\%s' % (server, database))
      sql = "SELECT CAST(estaciones.cod_ideam AS varchar) as CodigoEstacion" \
            " ,elementos.nombre + ' [' + TRIM(Str(estaciones.cod_ideam)) + ']' as NombreEstacion" \
            " ,elementos.latitud as Latitud" \
            " ,elementos.longitud as Longitud" \
            " ,elementos.elevacion as Altitud" \
            " ,tipoestacion.nombre as Categoria" \
            " ,entidades.nombre as Entidad" \
            " ,null as AreaOperativa" \
            " ,departamentos.nombre as Departamento" \
            " ,municipios.nombre as Municipio" \
            " ,elementos.fecha_inicial as FechaInstalacion" \
            " ,elementos.fecha_final as FechaSuspension" \
            " ,null as IdParametro" \
            " ,parametros.cod_alfa as Etiqueta" \
            " ,parametros.nombre as DescripcionSerie" \
            " ,parametros.nivel as Frecuencia" \
            " ,datosMensuales.fecha as Fecha" \
            " ,datosMensuales.dato as Valor" \
            " ,null as Grado" \
            " ,flags.flag as Calificador" \
            " ,null as NivelAprobacion" \
            " ,datosMensuales.cod_elemento" \
            " ,estaciones.cod_eaab" \
            " ,datosMensuales.cod_parametro" \
            " ,unidades.unidad" \
            " ,parametros.cod_descriptor" \
            " ,descriptores.nombre as nombre_descriptor" \
            " ,datosMensuales.cod_flag" \
            " ,datosMensuales.nroObs" \
            " FROM datosMensuales" \
            " LEFT JOIN elementos ON datosMensuales.cod_elemento=elementos.codigo" \
            " LEFT JOIN estaciones ON datosMensuales.cod_elemento=estaciones.cod_elemento" \
            " LEFT JOIN parametros ON datosMensuales.cod_parametro=parametros.codigo" \
            " LEFT JOIN flags ON datosMensuales.cod_flag=flags.codigo" \
            " LEFT JOIN tipoestacion ON estaciones.cod_tipoest=tipoestacion.codigo" \
            " LEFT JOIN unidades ON parametros.cod_unidad=unidades.codigo" \
            " LEFT JOIN descriptores ON parametros.cod_descriptor=descriptores.codigo" \
            " LEFT JOIN entidades ON elementos.cod_entidad=entidades.codigo" \
            " LEFT JOIN departamentos ON elementos.cod_depto=departamentos.codigo" \
            " LEFT JOIN municipios ON elementos.cod_mpio=municipios.codigo AND departamentos.codigo=municipios.cod_depto" \
            " --WHERE estaciones.cod_ideam is not null" \
            " ORDER BY estaciones.cod_ideam, cod_parametro, fecha"
      print('\nSQL: %s' %sql)
      table_export(sql, table_name)
      # Update stations locations
      if update_locations:
            df1 = pd.read_csv(output_path+table_name)  # Monthly values
            df2 = pd.read_csv(output_path+locations_table)  # Updated stations locations table
            df1 = df1.merge(df2, on='cod_elemento', how='left')
            df1.drop(['Latitud_x', 'Longitud_x'], inplace=True, axis=1)
            df1.rename(columns={'Latitud_y':'Latitud', 'Longitud_y':'Longitud'}, inplace=True)
            new_cols = ['CodigoEstacion','NombreEstacion','Latitud','Longitud','Altitud','Categoria','Entidad','AreaOperativa',
                        'Departamento','Municipio','FechaInstalacion','FechaSuspension','IdParametro','Etiqueta','DescripcionSerie',
                        'Frecuencia','Fecha','Valor','Grado','Calificador','NivelAprobacion','cod_elemento','cod_eaab',
                        'cod_parametro','unidad','cod_descriptor','nombre_descriptor','cod_flag','nroObs']  # Reordering columns
            df1 = df1[new_cols]
            print('\nData types \n',df1.dtypes)
            print(df1)
            df1.to_csv(output_path+table_name, index=False, encoding='utf-8')
      # Update stations parameters with IDEAM values
      if update_parameters:
            df1 = pd.read_csv(output_path+table_name)  # Monthly values
            df2 = pd.read_csv(output_path+parameters_table)  # Parameters table with IDEAM values
            df1 = df1.merge(df2, on='Etiqueta', how='left')
            df1.drop(['IdParametro_x', 'Frecuencia_x', 'DescripcionSerie'], inplace=True, axis=1)
            df1.rename(columns={'IdParametro_y':'IdParametro', 'Etiqueta':'EtiquetaEAAB', 'EtiquetaIDEAM':'Etiqueta',
                                'Frecuencia_y':'Frecuencia', 'DescripcionSerieIDEAM':'DescripcionSerie'}, inplace=True)
            new_cols = ['CodigoEstacion','NombreEstacion','Latitud','Longitud','Altitud','Categoria','Entidad','AreaOperativa',
                        'Departamento','Municipio','FechaInstalacion','FechaSuspension','IdParametro','Etiqueta','DescripcionSerie',
                        'Frecuencia','Fecha','Valor','Grado','Calificador','NivelAprobacion','cod_elemento','cod_eaab',
                        'cod_parametro','unidad','cod_descriptor','nombre_descriptor','cod_flag','nroObs', 'EtiquetaEAAB', 'DescripcionSerieEAAB']  # Reordering columns
            df1 = df1[new_cols]
            print('\nData types \n',df1.dtypes)
            print(df1)
            df1.to_csv(output_path+table_name, index=False, encoding='utf-8')


# df1['yday'] = pd.to_datetime(df1['Fecha']).dt.dayofyear  # Day of the year in daily series


# References
# https://stackoverflow.com/questions/53175265/get-tables-list-from-sql-server-database-as-a-clean-python-list-of-strings
# https://www.mssqltips.com/sqlservertip/7324/python-pandas-read-sql-server-data-dataframe/
# https://towardsdatascience.com/how-to-export-pandas-dataframe-to-csv-2038e43d9c03
# https://stackoverflow.com/questions/10822635/get-the-number-of-rows-in-table-using-sqlalchemy
# https://stackoverflow.com/questions/38152416/how-to-execute-update-query-with-sqlalchemy-sql-builder-in-python
# https://www.statology.org/pandas-update-column-based-on-another-dataframe/
# https://sparkbyexamples.com/pandas/pandas-change-position-of-a-column/
# https://www.statology.org/pandas-get-day-of-year-from-date/
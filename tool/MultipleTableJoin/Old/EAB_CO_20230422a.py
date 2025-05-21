# -*- coding: UTF-8 -*-
# Name: EAB_CO.py
# Description: this script extract and transform the EAB SIH SQL Server database into record datasets tables
# Source dataset: www.acueducto.com.co
# Disclaimer: records are under EAB license
# Repository: https://github.com/rcfdtools/R.GISPython/tree/main/MultipleTableJoin
# License: https://github.com/rcfdtools/R.GISPython/wiki/License
# Requirements: Python 3+, Pandas, sqlalchemy
# Notes: at the end of every records are included the properties cod_elemento, cod_eaab, cod_parametro, unidad,cod_descriptor, nombre_descriptor, cod_flag,nroObs

# Libraries
import pandas as pd
from sqlalchemy import create_engine  # Use a version below 2.0

# Functions
# Table export function
def table_export(sql, table_name, station_code):
    df = pd.read_sql(sql, engine, )
    print(df.describe())
    print(df.dtypes)
    if station_code:
        df[station_code] = int(df[station_code]).astype('str')
    df.to_csv(output_path+table_name, index=False, encoding='utf-8')
    print(df)

# Variables
driver = '{ODBC Driver 17 for SQL Server}'
server = 'ADMIN'  # For instances use ADMIN\MSSQLSERVER where MSSQLSERVER is the instance
database = 'SIH_20210502'
username = 'sa'
password = '123456'
output_path = 'EAB_CO/'
extract_montly_values = True  # Extract or update

# Connector
engine = create_engine(
    'mssql+pyodbc://'
    + username
    + ':' + password
    + '@' + server
    + '/' + database + '?'
    + 'driver=ODBC+Driver+17+for+SQL+Server')

# Retrieving table names
print('DB Tables over: %s\%s' % (server, database))
sql = "SELECT Distinct TABLE_NAME FROM information_schema.TABLES"
table_export(sql, 'eab_sih_tables.csv', '')

# Retrieving monthly records
if extract_montly_values:
      print('\nExtracting or updating monthly values from: %s\%s' % (server, database))
      sql = "SELECT estaciones.cod_ideam as CodigoEstacion" \
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
      table_export(sql, 'eab_sih_monthly_records.csv', 'CodigoEstacion')





# References
# https://stackoverflow.com/questions/53175265/get-tables-list-from-sql-server-database-as-a-clean-python-list-of-strings
# https://www.mssqltips.com/sqlservertip/7324/python-pandas-read-sql-server-data-dataframe/
# https://towardsdatascience.com/how-to-export-pandas-dataframe-to-csv-2038e43d9c03
# https://stackoverflow.com/questions/10822635/get-the-number-of-rows-in-table-using-sqlalchemy

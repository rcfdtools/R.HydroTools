
# Libraries
import pyodbc
import pandas as pd
from sqlalchemy import create_engine

# Variables
driver = '{ODBC Driver 17 for SQL Server}'
server = 'ADMIN'  # For instances use ADMIN\MSSQLSERVER where MSSQLSERVER is the instance
database = 'SIH_20210502'
username = 'sa'
password = '123456'

# Connection
conn = pyodbc.connect('DRIVER=' + driver
                      + ';SERVER=' + server
                      + ';DATABASE=' + database
                      + ';UID=' + username
                      + ';PWD=' + password)

# Retrieving table names
sql = "SELECT Distinct TABLE_NAME FROM information_schema.TABLES"
cursor = conn.cursor()
cursor.execute(sql)
# print(cursor.fetchall())
print('DB Tables over: %s\%s' %(server, database))
for i in cursor:
    print('\t%s' %(i[0]))

# Retrieving monthly records
query = 'SELECT TOP (100) cod_elemento, cod_parametro, fecha, dato, cod_flag, nroObs FROM datosMensuales'
'''
for row in cursor.execute(query):
    print(row.cod_elemento, row.cod_parametro, row.fecha, row.dato, row.cod_flag, row.nroObs)
'''

df = pd.read_sql(query, conn)


# References
# https://stackoverflow.com/questions/53175265/get-tables-list-from-sql-server-database-as-a-clean-python-list-of-strings
# https://www.mssqltips.com/sqlservertip/7324/python-pandas-read-sql-server-data-dataframe/
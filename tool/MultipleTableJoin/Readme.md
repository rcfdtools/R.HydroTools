<div align="center"><img alt="R.HydroTools" src="../../file/graph/R.HydroTools.svg" width="300px"></div>

## Join multiple separate tables into a unique unpivot table dataset  
Keywords: `etl` `dataset` `camels-br` `ana-br` `car-co` `python`

Isolated time-series file parameters, has to be joined in a unique table if you want to use dynamic ArcGIS map views related with gauge stations or basin polygons through an ETL process.  

Accord with IBM, an ETL, which stands for extract, transform and load, is a data integration process that combines data from multiple data sources into a single, consistent data store that is loaded into a data warehouse or other target system.[^1]

As the databases grew in popularity in the 1970s, ETL was introduced as a process for integrating and loading data for computation and analysis, eventually becoming the primary method to process data for data warehousing projects.

ETL provides the foundation for data analytics and machine learning workstreams. Through a series of business rules, ETL cleanses and organizes data in a way which addresses specific business intelligence needs, like monthly reporting, but it can also tackle more advanced analytics, which can improve back-end processes or end user experiences. ETL is often used by an organization to: 

* Extract data from legacy systems
* Cleanse the data to improve data quality and establish consistency
* Load data into a target database


### CAMELS-BR [:hook:](CAMELS_BR)[^2]

Catchment Attributes and Meteorology for Large-sample Studies - Brazil

Dataset reference: Vinícius B. P. Chagas, Pedro L. B. Chaffe, Nans Addor, Fernando M. Fan, Ayan S. Fleischmann, Rodrigo C. D. Paiva, & Vinícius A. Siqueira. (2020). CAMELS-BR: Hydrometeorological time series and landscape attributes for 897 catchments in Brazil - link to files. (1.1) [Data set]. Zenodo. https://zenodo.org/record/3964745

* Script [MultipleTableJoin_CAMELS_BR.py](MultipleTableJoin_CAMELS_BR.py)  
* [Local source CAMELS-BR dataset.](CAMELS_BR/Source)  
* [Local joined files for Amazon Basin.](CAMELS_BR/Joined)

```
# -*- coding: UTF-8 -*-
# Name: MultipleTableJoin_CAMELS_BR.py
# Description: this script join multiple separated tables into a unique unpivot table.
# Source dataset: https://zenodo.org/record/3964745
# Repository: https://github.com/rcfdtools/R.GISPython/tree/main/MultipleTableJoin
# License: https://github.com/rcfdtools/R.GISPython/wiki/License
# Requirements: Python 3+, Pandas,

# Libraries
import glob
import os
import pandas as pd
import shutil

# Functions
def processing_file(file):
    print('Processing %s' % file[len_input_path:9999])
    df = pd.read_csv(file, sep=column_separator)
    df[station_id] = file[len_input_path:len_input_path + gauge_id_digits]
    df['date'] = pd.to_datetime(df[[year_column, month_column, day_column]])
    df.to_csv(temp_path + file[len_input_path:9999], encoding='utf-8', index=False)

# General parameters
input_path = 'CAMELS_BR/Source/Input'  # Your local input file folder
temp_path = 'Temp/'  # Your local output temporal folder
stations_file = 'CAMELS_BR/Stations.csv'  # File with the stations list to process. If the list contains repeated values, transformed files is posted only one time in the temporal output folder.
camels_br_type = '_streamflow_m3s'  # _streamflow_m3s, _streamflow_mm, _simulated_streamflow, _precipitation_chirps, _precipitation_mswep, _precipitation_cpc, _evapotransp_gleam, _evapotransp_mgb, _potential_evapotransp_gleam, _temperature_min, _temperature_mean, _temperature_max
format_file = '.txt'  # CAMELS-BR use .txt files
joined_file = 'camels_br' + camels_br_type + '.csv'  # Joined file name to import in ArcGIS
column_separator = ' '  # Separator used in the CAMELS-BR files
year_column = 'year'
month_column = 'month'
day_column = 'day'
station_id = 'gauge_id'
gauge_id_digits = 8  # For CAMELS-BR, the gauge ID is the first eight digits of the file name
process_all = False  # Process all the stations. True ignore the file Stations.csv. False process only the list included in Stations.csv

# Procedure
shutil.rmtree(temp_path)
os.mkdir(temp_path, 0o666)
len_input_path = len(input_path)
if os.path.isfile(joined_file):
    os.remove(joined_file)
print('Processing all files contained in the %s folder: %s' % (input_path, process_all))
founded = 0
if not process_all:
    df_stations = pd.read_csv(stations_file, sep=column_separator)  # Station list to process
    n_stations = len(df_stations)
    print('Stations list: %s\nStations to process: %d\n\nStarting...' % (stations_file, n_stations))
    for j in range(len(df_stations)):
        station_file = input_path + str(df_stations[station_id][j]) + camels_br_type + format_file
        if os.path.isfile(station_file):
            processing_file(station_file)
            founded += 1
        else:
            print('Processing %s - file not available' % station_file[len_input_path:9999])
    print('%d stations founded of %d required (%f%%)' %(founded, n_stations, (founded/n_stations)*100))
else:
    table_files = glob.glob(input_path + '*' + format_file)
    print('Files founded: %d\n\nStarting...' % len(table_files))
    for i in table_files:
        processing_file(i)
table_files = glob.glob(temp_path + '*' + format_file)
df = pd.concat(map(pd.read_csv, table_files), ignore_index=True)
df.to_csv(joined_file, encoding='utf-8', index=False)
shutil.rmtree(temp_path)
os.mkdir(temp_path, 0o666)
print('\nJoined dataframe sample\n', df)
print('\nJoined file: %s\n' % joined_file)
print('Process accomplished...')
```


#### Parameters & specifications

* `input_path` & `temp_path`: user can define the input and the temporal processing folder.
* `stations_file`: [Stations.csv](CAMELS_BR/Stations.csv) contains a list of the stations to be joined. The parameter `process_all = False` has to be established in False, otherwise, all the files founded in the Input folder will be joined. 
* `camels_br_type`: user have to specify the kind of file to process, e.g.: _streamflow_m3s, _streamflow_mm, _simulated_streamflow, _precipitation_chirps, _precipitation_mswep, _precipitation_cpc, _evapotransp_gleam, _evapotransp_mgb, _potential_evapotransp_gleam, _temperature_min, _temperature_mean, _temperature_max.
* `process_all`: all the files contained in the Input folder will be joined if this parameter is `True`, with `False` only the stations includes in Stations.csv will be joined.   

> For this example, Stations.csv contains all the Amazon basin stations.


### ANA Brasil [:hook:](ANA_BR)[^3]

A ferramenta ANA Data Acquisition realiza o download automático de várias estações pluviométricas e fluviométricas disponibilizados pela Agência Nacional de Águas (ANA). https://www.ufrgs.br/hge/ana-data-acquisition/

* Script [MultipleTableJoin_ANA_BR.py](MultipleTableJoin_ANA_BR.py)  
* [Local source ANA-BR dataset.](ANA_BR/Source)  
* [Local joined files for Amazon & Orinoco Basin.](ANA_BR/Joined)

```
# -*- coding: UTF-8 -*-
# Name: MultipleTableJoin_ANA_BR.py
# Description: this script join multiple separated tables into a unique unpivot table.
# Source dataset: https://www.ufrgs.br/hge/ana-data-acquisition/
# Repository: https://github.com/rcfdtools/R.GISPython/tree/main/MultipleTableJoin
# License: https://github.com/rcfdtools/R.GISPython/wiki/License
# Requirements: Python 3+, Pandas,
# Attention: ANA-BR uses dd MM AAAA format and decimal point format for numeric values

# Libraries
import glob
import os
import pandas as pd
import shutil


# Functions
def processing_file(file):
    print('Processing %s' % file[len_input_path:9999])
    df = pd.read_csv(file, delim_whitespace=True, header=None)
    df.columns = [day_column, month_column, year_column, ana_br_type]
    df[station_id] = file[len_input_path:len_input_path + gauge_id_digits]
    df['date'] = pd.to_datetime(df[[year_column, month_column, day_column]])
    df.to_csv(temp_path + file[len_input_path:9999], encoding='utf-8', index=False)

# General parameters
input_path = 'ANA_BR/Source/Level/'  # Your local input file folder
temp_path = 'Temp/'  # Your local output temporal folder
stations_file = 'ANA_BR/Stations.csv'  # File with the stations list to process. If the list contains repeated values, transformed files is posted only one time in the temporal output folder. Use quites for the first station, e.g. "00049000"
ana_br_type = 'level'  # ANA options: precipitation, discharge, level
format_file = '.txt'  # CAMELS-BR use .txt files
joined_file = 'ana_br' + '_' + ana_br_type + '.csv'  # Joined file name to import in ArcGIS
year_column = 'year'
month_column = 'month'
day_column = 'day'
station_id = 'codigo'
replace_value = -9999.0  # For ANA-BR, -1.0 values correspond to nan values for precipitation & discharge and -9999.0 for level values.
gauge_id_digits = 8  # For ANA-BR, the gauge ID is the first eight digits of the file name
process_all = True  # Process all the stations. True ignore the file Stations.csv. False process only the list included in Stations.csv

# Procedure
shutil.rmtree(temp_path)
os.mkdir(temp_path, 0o666)
len_input_path = len(input_path)
if os.path.isfile(joined_file):
    os.remove(joined_file)
print('Processing all files contained in the %s folder: %s' % (input_path, process_all))
founded = 0
if not process_all:
    df_stations = pd.read_csv(stations_file, dtype={station_id: str})  # Station list to process
    n_stations = len(df_stations)
    print('Stations list: %s\nStations to process: %d\n\nStarting...' % (stations_file, n_stations))
    for j in range(len(df_stations)):
        station_file = input_path + str(df_stations[station_id][j]) + format_file
        if os.path.isfile(station_file):
            processing_file(station_file)
            founded += 1
        else:
            print('Processing %s - file not available' % station_file[len_input_path:9999])
    print('%d stations founded of %d required (%f%%)' %(founded, n_stations, (founded/n_stations)*100))
else:
    table_files = glob.glob(input_path + '*' + format_file)
    print('Files founded: %d\n\nStarting...' % len(table_files))
    for i in table_files:
        processing_file(i)
table_files = glob.glob(temp_path + '*' + format_file)
df = pd.concat(map(pd.read_csv, table_files), ignore_index=True)
print('\n')
df.describe()
df.info()
df[ana_br_type] = df[ana_br_type].replace(replace_value, None)
df.to_csv(joined_file, encoding='utf-8', index=False)
shutil.rmtree(temp_path)
os.mkdir(temp_path, 0o666)
print('\nJoined dataframe sample\n', df)
print('\nJoined file: %s\n' % joined_file)
print('Process accomplished...')
```


#### Parameters & specifications

* `input_path` & `temp_path`: user can define the input and the temporal processing folder.
* `stations_file`: [Stations.csv](ANA_BR/Stations.csv) contains a list of the stations to be joined. The parameter `process_all = False` has to be established in False, otherwise, all the files founded in the Input folder will be joined. 
* `ana_br_type`: user have to specify the kind of file to process, e.g.: precipitation, discharge, level.
* `replace_value`: for ANA-BR, -1.0 values correspond to nan values for precipitation & discharge and -9999.0 for level values. User may to set the right value for replace as Nan. 
* `process_all`: all the files contained in the Input folder will be joined if this parameter is `True`, with `False` only the stations includes in Stations.csv will be joined.   

> For this example, Stations.csv only contains a sample, the first station has to be between quotes for set the codes as string.


### CAR-CO [:hook:](CAR_CO)[^4]


Corporación Autónoma Regional de Cundinamarca Colombia - https://www.car.gov.co/vercontenido/2524

This data collection, contains the active station list and the monthly historical record datasets for active and suspended stations. 

* Script [MultipleTableJoin_CAR_CO.py](MultipleTableJoin_CAR_CO.py)  
* [Local source CAR_CO dataset.](CAR_CO/Source)  
* [Local joined files for CAR jurisdiction.](CAR_CO/Joined)

Disclaimer: current script version do not create the records marks file and the wind directions file.

```
# -*- coding: UTF-8 -*-
# Name: MultipleTableJoin_CAR_CO.py
# Description: this script create a dataset file from monthly CAR - Cundinamarca - Colombia Excel records
# Source dataset: https://www.car.gov.co/vercontenido/2524
# Disclaimer: this script version do not create the records marks file and the wind directions file
# Repository: https://github.com/rcfdtools/R.GISPython/tree/main/MultipleTableJoin
# License: https://github.com/rcfdtools/R.GISPython/wiki/License
# Requirements: Python 3+, Pandas, openpyxl


# Libraries
import openpyxl
from openpyxl import Workbook, load_workbook
import pandas as pd
import glob


# General parameters
input_path = 'D:/R.GISPython/MultipleTableJoin/CAR_CO/Source/'
output_path = 'D:/R.GISPython/MultipleTableJoin/CAR_CO/Joined/'
parameter_value = 'Q_MEDIA_M'  # More info https://github.com/rcfdtools/R.GISPython/tree/main/MultipleTableJoin/CAR_CO
excel_file = '5bae92275ec7e.xlsx'
clean_file = 'Clean_'+excel_file
pivot_file = 'Pivot_'+parameter_value+'.csv'
unpivot_file = 'Unpivot_'+parameter_value+'.csv'
joined_file = 'CAR_Joined.csv'
head_rows = 15  # Header rows to delete
index_name = 'Id'
parameter_name = 'Label'
station_code = 'Code'
year_name = 'Year'
month_name = 'Month'
day_name = 'Day'
date_name = 'Date'
value_name = 'Value'
run_clean = True  # Execute the clean Excel process. Set False if you are going to join all the files.
run_pivot_dataset = True  # Execute the pivot dataset creation. Set False if you are going to join all the files.
run_unpivot_dataset = True  # Execute the unpivot dataset creation. Set False if you are going to join all the files.
year_to_integer = False  # Convert Year values to integer.
join_unpivot_files = True  # Set to True if you had all the files processed with unpivot tables and you require one joined file.


# Load workbook and delete catalog and not station sheets
book = load_workbook(input_path+excel_file, data_only=True)  # use data_only for read values and not formulas
delete_sheets = ['Catalogo', 'CATALOGO', 'Resumen', 'RESUMEN', 'Hoja1', 'Hoja2', 'Hoja3', 'Sheet1', 'Sheet2', 'Sheet3']
sheets = book.sheetnames
for j in sheets:
    for i in delete_sheets:
        if j == i:
            book.remove(book[i])
sheets = book.sheetnames


# Clean headers and intermediate columns
if run_clean:
    print('\nRunning the cleaning process\n'+ 40 * '-')
    for i in sheets:
        print('Processing: %s' %i)
        sheet = book[i]
        print('\tTotal rows: %d' % sheet.max_row)
        for merge in list(sheet.merged_cells):
            print('\tUnmerging %s' % merge)
            sheet.unmerge_cells(range_string=str(merge))
        sheet.delete_rows(1,head_rows)
        print('\tDeleting headers')
        print('\tDeleting white columns')
        sheet.delete_cols(2)
        for j in range(2,15):  # Delete intermediate columns
            sheet.delete_cols(j)
        print('\tRows: %d' % len(sheet['A']))
    book.save(output_path+clean_file)


# Pivot dataset creation
if run_pivot_dataset:
    print('\n\nRunning the pivot dataframe creation\n'+ 40 * '-')
    xl = pd.ExcelFile(output_path+clean_file)
    sheets = xl.sheet_names
    df = pd.DataFrame()
    for i in sheets:
        print('Processing: %s' % i)
        df1 = pd.read_excel(output_path+clean_file, sheet_name=i, header=None, names=[year_name, '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])
        df1[station_code] = i
        df1[parameter_name] = parameter_value
        df = pd.concat([df, df1])
    if year_to_integer:
        df = df.astype({year_name : int})
    print(df)
    df.to_csv(output_path+pivot_file, encoding='utf-8', index=False)


# Unpivot dataset creation
if run_unpivot_dataset:
    print('\n\nRunning the unpivot dataframe creation\n'+ 40 * '-')
    df = pd.read_csv(output_path+pivot_file, low_memory=False)
    print(df.info(), '\n')
    print(df.dtypes, '\n')
    print(df, '\n')
    df_unpivot = pd.melt(df, id_vars=(year_name, station_code, parameter_name), var_name=month_name, value_name=value_name, ignore_index = True)
    df_unpivot[day_name] = '01'
    df_unpivot[date_name] = pd.to_datetime(df_unpivot[[year_name, month_name, day_name]])
    df_unpivot.index.name = index_name
    df_unpivot = df_unpivot[[parameter_name, station_code, year_name, month_name, day_name, date_name, value_name]]
    print(df_unpivot, '\n')
    df_unpivot.to_csv(output_path+unpivot_file)


# Join all the unpivot files
if join_unpivot_files:
    print('\nJoining the unpivot files\n' + 40 * '-')
    csv_files = glob.glob(output_path + 'Unpivot_*.csv')
    print('Joining: %s' %csv_files)
    df = pd.concat(map(pd.read_csv, csv_files), ignore_index=True)
    df.to_csv(output_path + joined_file, encoding='utf-8', index=False)
    print(df)


print('\nClean file: %s' % output_path + clean_file,
          '\nPivot file: %s' % output_path + pivot_file,
          '\nUnpivot file: %s' % output_path + unpivot_file,
          '\nJoined file: %s' % output_path + joined_file)
```


#### Parameters & specifications

* `input_path` & `output_path`: user can define the input and the output processing folder.
* `parameter_value`: specific IDEAM - Colombia [label parameter to process](CAR_CO). 
* `excel_file`: user may to specify the Microsoft Excel file to process. `parameter_value` has to be related with the file.
* `clean_file`, `pivot_file`, `unpivot_file` & `joined_file`: this script create a cleaned Excel file, a pivot .csv file that contains columns with the monthly values and an unpivot .csv file with the stacked records. After the individual processing files, user can create a joined stacked file with all the records contained in the unpivot .csv files.
* `run_clean`: execute the clean Excel process. Set False if you are going to join all the files.
* `run_pivot_dataset`: execute the pivot dataset creation. Set False if you are going to join all the files.
* `run_unpivot_dataset`: execute the unpivot dataset creation. Set False if you are going to join all the files.
* `join_unpivot_files`: set to True if you had all the files processed with unpivot tables, and you require one joined file.
* `delete_sheets`: this Python list contains the sheet names that has to be deleted because don't correspond to datasets values.

> As you notice, you can run the cleaning, pivot, unpivot and joining process separately. This could you help to identify different kind of user errors in the source Excel dataset, e.g, text values over the data values cells, incorrect numeric decimal separators, more than 15 header lines. 


### EAAB-CO [:hook:](EAAB_CO)[^4]

Disclaimer: current script version is only used to join monthly values.

```
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
```

## References

* https://stackoverflow.com/questions/19350806/how-to-convert-columns-into-one-datetime-column-in-pandas
* https://essd.copernicus.org/articles/12/2075/2020/
* https://www.ufrgs.br/samewater/2020/12/02/camels-br/
* https://www.skytowner.com/explore/replacing_values_with_nans_in_pandas_dataframe
* https://sparkbyexamples.com/pandas/pandas-replace-by-examples/
* https://blog.aspose.com/cells/insert-and-delete-rows-and-columns-in-excel-using-python/
* https://www.youtube.com/watch?v=718edSNvKLA
* https://stackoverflow.com/questions/23527887/getting-sheet-names-from-openpyxl
* https://www.geeksforgeeks.org/how-to-delete-one-or-more-rows-in-excel-using-openpyxl/
* https://www.codespeedy.com/delete-rows-of-a-sheet-using-openpyxl/
* https://stackoverflow.com/questions/69891944/unmerge-every-cell-in-an-excel-worksheet-using-openpyxl
* https://stackoverflow.com/questions/40166714/replace-specific-values-in-openpyxl
* https://stackoverflow.com/questions/17977540/pandas-looking-up-the-list-of-sheets-in-an-excel-file
* https://practicaldatascience.co.uk/data-science/how-to-reorder-pandas-dataframe-columns


### Licencia, cláusulas y condiciones de uso

_R.HydroTools es de uso libre para fines académicos, conoce nuestra [licencia, cláusulas, condiciones de uso](../../LICENSE.md) y como referenciar los contenidos publicados en este repositorio._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [r.cfdtools](https://github.com/rcfdtools) en GitHub._

| [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.HydroTools/discussions/xxx) |
|-----------------------------------|------------------------------|

[^1]: https://www.ibm.com/topics/etl
[^2]: https://zenodo.org/record/3964745
[^3]: https://www.ufrgs.br/hge/ana-data-acquisition/
[^4]: https://www.car.gov.co/vercontenido/2524
[^5]: https://www.acueducto.com.co


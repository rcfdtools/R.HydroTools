# .gage and .met file generator
# https://github.com/rcfdtools
# This script can be run in any Python 3+ version

total_gages = 39 # Gages correspond with the number of subbasins for PMax24h
dss_file_name = 'HECHMS_v0.dss'
path_a = 'ArroyoElZorro' # Basin name
path_f = 'P_TR2.33_6h_FSCalif057' # Hyetograph name
start_time = '1 January 2004, 06:00'
end_time = '6 January 2004, 06:00'
subbasin_prefix = 'W'

# Gage file
print('*****************************\n.gage file\n*****************************\n')
for i in range(total_gages):
    print(f'Gage: {subbasin_prefix}{i+1}\n     Gage: {subbasin_prefix}{i+1}\n     Gage Type: Precipitation\n     Last Modified Date: 01 January 2026\n     Last Modified Time: 06:00:00\n     Reference Height Units: Meters\n     Reference Height: 9.9999\n     Data Source Type: External DSS\n     Filename: {dss_file_name}\n     Pathname: /{path_a}/{subbasin_prefix}{i+1}/PRECIP-INC//15Minute/{path_f}/\n     Variant: Variant-1\n       Start Time: {start_time}\n       End Time: {end_time}\n     End Variant: Variant-1\nEnd:\n')

# Met file
print('\n*****************************\n.met file\n*****************************\n')
for i in range(total_gages):
    print(f'Subbasin: {subbasin_prefix}{i+1}\n     Last Modified Date: 01 January 2026\n     Last Modified Time: 06:00:00\n     Gage: W{i+1}\nEnd:\n')


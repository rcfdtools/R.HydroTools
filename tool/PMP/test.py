import pandas as pd

station_label = 'Station'
input_path = 'dataset/pmax24h_in/'  # Your local input file folder
ouput_path = 'dataset/pmax24h_out/'  # Your local input file folder
station_file = input_path+'conventional.csv'
df_all = pd.read_csv(station_file, delimiter=',', parse_dates=True)  # index_col=0
stations = df_all[station_label].unique()
for station_code in stations:
    file_log_name = f'{ouput_path}{station_code}.csv'  # Markdown file log
    print(file_log_name)
    df = df_all[df_all[station_label] == station_code]
    print(df)
    df.to_csv(file_log_name, index=False)

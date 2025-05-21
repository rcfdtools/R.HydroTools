# Download records from www.datos.gov.co through socrata service
# https://github.com/rcfdtools/R.GISPython/blob/main/MultipleTableJoin/Readme.md

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
#client = Socrata("www.datos.gov.co", None)
client = Socrata(domain='www.datos.gov.co', app_token='YbwUzaxNjS1mPkewk5AZo1qCS')

# Example authenticated client (needed for non-public datasets):
# client = Socrata(www.datos.gov.co,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.

# Variables
# IDEAM Rain: s54a-sgyg (231619587 records in 20250506)
# MADS Rain: ksew-j3zj

varname = 'ksew-j3zj'
station = '24010390'
where_txt = str('"codigoestacion='+station+'"')
print(where_txt)

print(client.get_metadata(varname))

print(f'Station: {station}')
#results = client.get(varname, where="codigoestacion='2120000170'", limit=1000)
#results = client.get_all(varname, where="codigoestacion='2120000170'", exclude_system_fields=True, limit=1000)
results = client.get(varname, where="codigoestacion='24010390'", exclude_system_fields=True, limit=1000)
#results = client.get(varname, where="codigoestacion='24010390'", exclude_system_fields=True)


# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

# Save into an external .csv file
results_df.to_csv('c:/temp/'+station+'.csv', index=False)

client.close()

# References
# https://github.com/afeld/sodapy
# https://dev.socrata.com/foundry/www.datos.gov.co/v8aw-jabd
# Get your token at: https://www.datos.gov.co/login

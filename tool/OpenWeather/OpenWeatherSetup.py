
# General libraries
from datetime import date
from datetime import datetime
from datetime import timezone

# General variables
mainTitle = 'Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org'
studyCase = 'Weather evaluation from historical openweathermap data for the CNE IDEAM network stations in Bogotá - Colombia - Suramérica'
filePath = r'D:/R.GISPython/OpenWeather'  # r'.' for relative path
urlGitHub = 'https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather'
fileNameCNE = 'CNE_IDEAM'
daysBefore = 2  # Max to 4 days, current day or 0 count like a part of the 5 days in openweather, only for historical data.
currentDate = date.today()
currentDateTxt = str(currentDate.year).zfill(4)+str(currentDate.month).zfill(2)+str(currentDate.day).zfill(2)
currentDateTime = datetime.now()  # datetime.utcnow()
timeStampVal = int(currentDateTime.replace(tzinfo=timezone.utc).timestamp())
timeStampVal -= 86400 * daysBefore
fileCSV = fileNameCNE+'_OWM_'+currentDateTxt+'.csv'
unitSys = 'metric'  # '' for default, 'metric' or 'imperial'
showHistorical = True  # True for use the timemachine. False for get the current forecast
plotParameters = [  # Parameter, metric system units, imperial system units
                  ('Clouds', '%', '%', 'light:k'),
                  ('Dewpoint', '°C', '°F', 'viridis_r'),
                  ('Feelslike', '°C', '°F', 'viridis_r'),
                  ('Humidity', '%', '%', 'light:b'),
                  ('Pressure', 'hPa', 'hPa', 'light:k'),
                  ('Rain', 'mm', 'mm', 'Blues'),
                  ('Temp', '°C', '°F', 'viridis_r'),
                  ('UVI', 'DN', 'DN', 'viridis_r'),
                  ('Visibility', 'm', 'm', 'light:k'),
                  ('Winddeg', '°', '°', 'Spectral'),
                  ('Windgust', 'm/s', 'm/s', 'YlOrBr'),
                  ('Windspeed', 'm/s', 'm/s', 'YlOrBr'),]
plotConfidenceHue = ['Category',
                     'Technology',
                     'Status',
                     'State',
                     'County',
                     'Stream',
                     'Operator',
                     'AHName',
                     'SZName',
                     'SZHName']


import time
from datetime import date

day_of_year = time.strptime("2013.12.31", "%Y.%m.%d").tm_yday
print(day_of_year)


date_val = date(2013, 12, 31)

day_of_year = date_val.strftime('%j')

print("\nDay of year: ", day_of_year, "\n")


# Refs
# https://www.mytecbits.com/internet/python/day-of-year
# https://stackoverflow.com/questions/13943062/extract-day-of-year-and-julian-day-from-a-string-date#:~:text=To%20get%20the%20Julian%20day,in%20the%20proleptic%20Gregorian%20calendar.
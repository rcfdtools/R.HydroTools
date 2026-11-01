# Requires: pip install spei

import numpy as np
import pandas as pd
import spei as si  # SPI / SPEI library

'''
SPI Value	Drought / Wet Category
≥ 2.0	Extremely Wet
1.5 to 1.99	Very Wet
1.0 to 1.49	Moderately Wet
-0.99 to 0.99	Near Normal
-1.0 to -1.49	Moderate Drought
-1.5 to -1.99	Severe Drought
≤ -2.0	Extreme Drought
'''

spi_category = [[-2.00, 'Extreme Drought'],
                [-1.99, 'Severe Drought'],
                [-1.49, 'Moderate Drought'],
                [0.99, 'Near Normal'],
                [999999, 'Nival, mayores a 4000 m.s.n.m']
                [999999, 'Nival, mayores a 4000 m.s.n.m']
               ]

# 1. Generate fake monthly precipitation data (in mm) for 10 years
np.random.seed(42)
dates = pd.date_range(start="2016-01-01", end="2025-12-31", freq="ME")
# Generating realistic positive numbers using a gamma distribution
rain_data = np.random.gamma(shape=3, scale=20, size=len(dates))

# Create a Pandas Series with the DateTimeIndex
precipitation = pd.Series(rain_data, index=dates)

# 2. Calculate SPI for a 3-month timescale (SPI-3)
# The library automatically defaults to a Gamma distribution
spi3 = si.spi(precipitation, timescale=3)

# 3. View the results
df = pd.DataFrame({"Precipitation (mm)": precipitation, "SPI-3": spi3})
print(df.tail(12))  # Display the last year of data
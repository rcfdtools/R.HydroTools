# Requires: pip install spei

import numpy as np
import pandas as pd
import spei as si  # SPI / SPEI library

'''
***********************************
SPI Value	Drought / Wet Category
***********************************
2.0 < SPI	      Extremely Wet
1.5 < SPI ≤ 2.0	  Very Wet
1.0 < SPI ≤ 1.5	  Moderately Wet
-1.0 < SPI ≤ 1.0  Near Normal
-1.5 < SPI ≤ -1.0 Moderate Dry
-2.0 < SPI ≤ -1.5 Severe Dry
SPI ≤ -2.0        Extreme Dry
'''

# Cols: SPI range, Precipitation regime, Colour
spi_category = [[-999999, 'Extremely dry', '#FF0000'],
                [-2.00, 'Very dry', '#FFC000'],
                [-1.50, 'Moderately dry', '#FFFF00'],
                [1.00, 'Normal precipitation', '#FFFFFF'],
                [1.50, 'Moderately wet', '#E9CCF9'],
                [2.00, 'Very wet', '#C980C6'],
                [999999, 'Extremely wet', '#9900CC'],
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
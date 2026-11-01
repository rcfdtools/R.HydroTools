# https://github.com/rcfdtools
# SPI categories
# This script has to be loaded in QGIS into a Field Calculator function
# Call the function as: spi_category("your_spi_field")
# return i[1] give you the Tag, return i[0] the range value, return i[2] the colour
# ERA5 Collection: Monthly drought indices from 1940 to present derived from ERA5 reanalysis
# https://cds.climate.copernicus.eu/
# https://drought.emergency.copernicus.eu/data/factsheets/factsheet_spi.pdf
# https://raw.githubusercontent.com/Eurac-Research/ado-data/main/factsheets/SPI_4.pdf

from qgis.core import *
from qgis.gui import *

@qgsfunction(group='rcfdtools', referenced_columns=[])
def spi_category(spi):
  # Cols: SPI range, Precipitation regime, Colour
  spi_category = [[-999999, 'Extremely dry', '#FF0000'],
                  [-2.00, 'Very dry', '#FFC000'],
                  [-1.50, 'Moderately dry', '#FFFF00'],
                  [1.00, 'Normal precipitation', '#FFFFFF'],
                  [1.50, 'Moderately wet', '#E9CCF9'],
                  [2.00, 'Very wet', '#C980C6'],
                  [999999, 'Extremely wet', '#9900CC'],
                 ]
  for i in spi_category:
    if spi <= i[0]:
      return i[1]


'''
Complementary information

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

*************************
Accumulation Periods Mean
*************************
1-Month (SPI-1):
  • Focus: Immediate, short-term moisture conditions.
  • Impact: Reflects day-to-day meteorological dryness, immediate topsoil moisture, and short-term crop stress.
3-Month (SPI-3):
  • Focus: Seasonal estimation.
  • Impact: Captures medium-term agricultural patterns and seasonal moisture conditions over a quarter of the year.
6-Month (SPI-6):
  • Focus: Intermediate seasonal trends.
  • Impact: Highlights medium-term precipitation deficits tied to anomalous streamflows and changing reservoir levels.
9-Month (SPI-9):
  • Focus: Medium-to-long cumulative patterns.
  • Impact: Values dropping below -1.5 signal substantial agricultural damage and broader economic sector impacts.
12-Month to 48-Month (SPI-12, SPI-24, SPI-48):
	• Focus: Long-term hydrological balance.
	• Impact: Reflects long-term cumulative precipitation affecting deep groundwater tables, major river basin streamflows, and major reservoir storage.
'''   
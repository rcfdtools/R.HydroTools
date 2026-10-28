# https://github.com/rcfdtools
# This script has to be loaded in QGIS into a Field Calculator function
# Call the function as: thermiclevel("your_elevation_field")
# return i[1] give you the Tag and return i[0] the range value.

from qgis.core import *
from qgis.gui import *

@qgsfunction(group='_TSIG', referenced_columns=[])
def thermiclevel(elevation):
  thermicLevelVal = [[1000, 'Cálido, hasta 1000 m.s.n.m'],
                     [2000, 'Templado, de 1000 a 2000 m.s.n.m'],
                     [3000, 'Frío, de 2000 a 3000 m.s.n.m'],
                     [4000, 'Páramo, de 3000 a 4000 m.s.n.m'],
                     [999999, 'Nival, mayores a 4000 m.s.n.m']]
  for i in thermicLevelVal:
    if elevation <= i[0]:
      return i[1]
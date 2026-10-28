# https://github.com/rcfdtools
# This script has to be loaded in QGIS into a Field Calculator function
# Call the function as: class_range_eval("your_area_field")

from qgis.core import *
from qgis.gui import *

@qgsfunction(group='_TSIG', referenced_columns=[])
def class_range_eval(area):
  cut_value = [2104.38577042, 8565.51423253, 18263.3741091, 65618.9256689]
  j = 1
  for i in cut_value:
    if area <= i:
      return j
    j += 1
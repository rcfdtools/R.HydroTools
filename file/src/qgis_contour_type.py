# https://github.com/rcfdtools
# This script has to be loaded in QGIS into a Field Calculator function
# Call as: contour_type( "ELEV", 100 )

from qgis.core import *
from qgis.gui import *

@qgsfunction(group='Custom', referenced_columns=[])
def contour_type(elevation, main_interval):
    if elevation % main_interval:
        ctype = 0
    else:
        ctype = 1
    return ctype

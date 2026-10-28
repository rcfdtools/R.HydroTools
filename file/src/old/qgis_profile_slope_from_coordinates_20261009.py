# https://github.com/rcfdtools/R.TSIG/blob/main/file/src/qgis_profile_slope_from_coordinates.py
# Calculates distance, abscissa, and slope rate between coordinates nodes
# ArcGIS Pro sample: https://github.com/rcfdtools/R.SIGE/blob/main/activity/DEMProfile/Readme.md
#
# This script has to be run in the QGIS Python console
# Runnable for any geometry layer or table with the attributes CX, CY, CZ and only one secuence or entity, for multiple profiles you first filter one by one
# Records in the table has to be in the original geometry secuence FID
# Stop editing before run the script
# Make sure a point layer is selected in the Layers panel
# Tested in QGIS 4.2.3
#
# QGIS preliminars
# Optional: Vector Geometry / Smooth (Iteration: 10, Offset: 0.25, Maximum node angle to smooth: 180)
# From a vector line with multiple nodes >> Vector Geometry / Extract vertices
# From a straigth vector line >> Vector General / Split Lines by Maximum Length
# From a straigth vector line >> Vector Geometry / Extract specific vertices
# NodeID(int, 0 to n) = id(@geometry)
# CX(real) = x(@geometry)
# CY(real) = y(@geometry)
# CZ(real) values >> Raster Analysis / Sample Raster Values


from qgis.PyQt.QtCore import QVariant
from qgis.core import QgsField, edit
import qgis.utils

# Get the active layer from Layer panel
layer = iface.activeLayer()

# General vars
cx_field = 'CX' # ● X coordinate field name in table
cy_field = 'CY' # ● Y coordinate field name in table 
cz_field = 'CZ' # ● Z coordinate field name in table 
distance_field = 'Distance'
abscissa_field = 'Abscissa'
slope_field = 'Slope'

# Add fields
new_field_list = [distance_field, abscissa_field, slope_field] 
for field in new_field_list:
    # Check and delete existind required fields
    field_index = layer.fields().indexFromName(field)
    if field_index != -1:
        with edit(layer):
             layer.dataProvider().deleteAttributes([field_index])
    layer.updateFields()
    
    # New Field, parameters are: field name, data type, field length, precision
    new_field = QgsField(field, QVariant.Double, len=20, prec=10)
    
    # Use an editing buffer to add the field and commit changes automatically
    with edit(layer):
        layer.dataProvider().addAttributes([new_field])
        layer.updateFields() # Update the layer's fields after adding
    
    print(f'Field "{field}" added to layer "{layer.name()}"')
layer.commitChanges()

# Calculations
layer.startEditing()
field_index_node_dist_2d = layer.fields().indexFromName(distance_field)
field_index_node_abscissa = layer.fields().indexFromName(abscissa_field)
field_index_node_slope = layer.fields().indexFromName(slope_field)
#global cx_up, cy_up, acum
cx_up, cy_up, cz_up, accumulate_distance = -9999, -9999, -9999, 0
for feature in layer.getFeatures():
    cx = feature[layer.fields().indexFromName(cx_field)]
    cy = feature[layer.fields().indexFromName(cy_field)]
    cz = feature[layer.fields().indexFromName(cz_field)]
    # Distance calculation
    if cx_up == -9999:
        cx_up, cy_up = cx, cy
    dist = ((cx - cx_up)**2 + (cy - cy_up)**2)**0.5
    cx_up, cy_up = cx, cy
    # Abscissa calculation
    accumulate_distance += dist
    # Slope calculation
    if cz_up == -9999: 
        cz_up = cz
    if dist != 0:
        slope = (cz_up - cz) / dist
        cz_up = cz
    else:
        slope = 0
    layer.changeAttributeValue(feature.id(), field_index_node_dist_2d, dist)
    layer.changeAttributeValue(feature.id(), field_index_node_abscissa, accumulate_distance)
    layer.changeAttributeValue(feature.id(), field_index_node_slope, slope)
layer.commitChanges()
print('Calculations completed...')


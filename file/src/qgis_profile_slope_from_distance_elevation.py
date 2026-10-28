# https://github.com/rcfdtools/R.TSIG/blob/main/file/src/qgis_profile_slope_from_distance_elevation.py
# Calculates the slope rate from a distance - elevation table
#
# This script has to be run in the QGIS Python console
# Runnable for any table with the attributes Distance and Elevation values and one secuence profile, for multiple profiles you first filter one by one
# Stop editing before run the script
# Make sure the table layer is selected in the Layers panel
# Tested in QGIS 4.2.3
#
# QGIS preliminars
# With a river or line and a terrain surface: View / New Elevation Profile, and export the Distance - Elevation values table and save as .gpkg

from qgis.PyQt.QtCore import QVariant
from qgis.core import QgsField, edit
import qgis.utils

# Get the active layer from Layer panel
layer = iface.activeLayer()

# General vars
distance_field = 'distance' # ● Field with accumulated distance values
elevation_field = 'elevation' # ● Field with the Z value or elevation
slope_field = 'Slope'

# Add fields
new_field_list = [slope_field] 
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
field_index_node_slope = layer.fields().indexFromName(slope_field)
distance_up, elevation_up = -9999, -9999
for feature in layer.getFeatures():
    distance = feature[layer.fields().indexFromName(distance_field)]
    elevation = feature[layer.fields().indexFromName(elevation_field)]
    # Slope calculation
    if distance_up == -9999:
        distance_up, elevation_up = distance, elevation
    if (distance_up - distance) != 0:
        slope = (elevation_up - elevation) / (distance - distance_up)
    else:
        slope = 0
    distance_up, elevation_up = distance, elevation
    layer.changeAttributeValue(feature.id(), field_index_node_slope, slope)
layer.commitChanges()
print('Calculations completed...')


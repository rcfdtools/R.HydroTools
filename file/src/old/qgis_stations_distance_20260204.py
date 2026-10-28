# https://github.com/rcfdtools/R.TSIG
# Calculate distance between a reference station and multiple stations with transform coordinates 
# Tested in QGIS 3.44.6
# Only for points layer
# Stop editing before run the script
# Make sure a layer is selected in the Layers panel

from qgis.PyQt.QtCore import QVariant
from qgis.core import QgsField, edit
import qgis.utils
from math import *


# Get the active layer from Layer panel
layer = iface.activeLayer()


# General parameters
cx_ref = 953750.4722457461 # Main station x coordinate ●
cy_ref = 1083615.4754182266 # Main station y coordinate ●
cz_ref = 1270.00000000000 # Main station z coordinate ●
cz_ref_name = 'COORD_Z_m' # CZ field in original stations table ●
crs_source = '4326' # Check the original CRS in source layer ●
crs_destination = '9377' # Define the CRS fot the calculations ●
cx_name = f'CX{crs_destination}'
cy_name = f'CY{crs_destination}'
dist2d_name = f'Dist2D{crs_destination}'
dist3d_name = f'Dist3D{crs_destination}'
direction_name = f'Direct{crs_destination}' # Calculated in gradians
inclination_name = f'Inclin{crs_destination}' # Calculated in gradians
transform = QgsCoordinateTransform(QgsCoordinateReferenceSystem(f'EPSG:{crs_source}'), QgsCoordinateReferenceSystem(f'EPSG:{crs_destination}'), QgsProject.instance())


# Add fields and do calculations
new_field_list = [cx_name, cy_name, dist2d_name, dist3d_name, direction_name, inclination_name]
if layer and layer.dataProvider().capabilities() & QgsVectorDataProvider.AddAttributes:
    # Fields creation
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
    
    # Calculate x projected values
    field_index = layer.fields().indexOf(cx_name)
    for feature in layer.getFeatures():
        geometry = feature.geometry()
        point = geometry.asPoint()
        fid = feature.id()
        x_in = point.x()
        y_in = point.y()
        point_out = transform.transform(QgsPointXY(x_in, y_in))
        layer.startEditing()
        layer.changeAttributeValue(fid, field_index, point_out.x())
    layer.commitChanges()
    print('Coordinates x calculated.')
    
    # Calculate y projected values
    field_index = layer.fields().indexOf(cy_name)
    for feature in layer.getFeatures():
        geometry = feature.geometry()
        point = geometry.asPoint()
        fid = feature.id()
        x_in = point.x()
        y_in = point.y()
        point_out = transform.transform(QgsPointXY(x_in, y_in))
        layer.startEditing()
        layer.changeAttributeValue(fid, field_index, point_out.y())
    layer.commitChanges()
    print('Coordinates y calculated.')

    # Calculate 2D distance
    layer.startEditing()
    field_index = layer.fields().indexFromName(dist2d_name)
    for feature in layer.getFeatures():
        deltax = cx_ref - feature[layer.fields().indexFromName(cx_name)]
        deltay = cy_ref - feature[layer.fields().indexFromName(cy_name)]
        dist2D = (deltax**2 + deltay**2)**0.5
        layer.changeAttributeValue(feature.id(), field_index, dist2D)
    layer.commitChanges()
    print('Distaces 2D calculated.')

    # Calculate 3D distance
    layer.startEditing()
    field_index = layer.fields().indexFromName(dist3d_name)
    for feature in layer.getFeatures():
        dist2D = feature[layer.fields().indexFromName(dist2d_name)]
        cz_val = feature[layer.fields().indexFromName(cz_ref_name)] or 0.00000 # Get values from each station (handling potential NULL values with 'or 0')
        deltaz =  cz_ref - cz_val
        dist3D = (dist2D**2 + deltaz**2)**0.5
        layer.changeAttributeValue(feature.id(), field_index, dist3D)
    layer.commitChanges()
    print('Distaces 3D calculated.')

    # Calculate direction in gradians
    layer.startEditing()
    field_index = layer.fields().indexFromName(direction_name)
    for feature in layer.getFeatures():
        deltax = cx_ref - feature[layer.fields().indexFromName(cx_name)]
        deltay = cy_ref - feature[layer.fields().indexFromName(cy_name)]
        if deltay != 0:
            direction = math.atan(deltay / deltax) * 180 / math.pi
        else:
            direction = 0
        layer.changeAttributeValue(feature.id(), field_index, direction)
    layer.commitChanges()
    print('Directions calculated.')

    # Calculate inclination in gradians
    layer.startEditing()
    field_index = layer.fields().indexFromName(inclination_name)
    for feature in layer.getFeatures():
        cz_val = feature[layer.fields().indexFromName(cz_ref_name)] or 0.00000 # Get values from each station (handling potential NULL values with 'or 0')
        deltaz =  cz_ref - cz_val        
        dist2D = feature[layer.fields().indexFromName(dist2d_name)]
        if deltaz != 0:
            inclination = abs(math.atan(deltaz / dist2D) * 180 / math.pi)
        else:
            inclination = 0
        layer.changeAttributeValue(feature.id(), field_index, inclination)
    layer.commitChanges()
    print('Inclinations calculated.')

   
else:
    print('Error: No active layer found, or the layer does not support adding or calculate fields.')


### Test
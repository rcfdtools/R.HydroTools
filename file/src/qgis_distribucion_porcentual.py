# https://github.com/rcfdtools
# Area percentual distribution calculator - APD
# This script has to be run in the QGIS Python console
# Stop editing before run the script
# Make sure the layer is selected in the Layers panel
# Tested in QGIS 3.44.6

from qgis.PyQt.QtCore import QVariant
from qgis.core import QgsField, edit
import qgis.utils


# Get the active layer from Layer panel
layer = iface.activeLayer()

# General parameters
area_field = ['Aha', QVariant.Double]
areapd_field = ['APD', QVariant.Double]
crs_source = layer.crs()
crs_target = QgsCoordinateReferenceSystem('EPSG:9377') # ● Define the CRS for the calculations
transform = QgsCoordinateTransform(crs_source, crs_target, QgsProject.instance().transformContext())

# Add fields and do calculations
new_field_list = [area_field, areapd_field]
if layer and layer.dataProvider().capabilities() & QgsVectorDataProvider.AddAttributes:
    # Fields creation
    for field in new_field_list:
        # Delete existing calculated fields
        field_index = layer.fields().indexFromName(field[0])
        if field_index != -1:
            with edit(layer):
                 layer.dataProvider().deleteAttributes([field_index])
        layer.updateFields()
        
        # New Field, parameters are: field name, data type, field length, precision
        if field[1] == QVariant.String:
            new_field = QgsField(field[0], field[1], field[2], field[3])
        else:
            new_field = QgsField(field[0], field[1], len=20, prec=10)
            
        # Use an editing buffer to add the field and commit changes automatically
        with edit(layer):
            layer.dataProvider().addAttributes([new_field])
            layer.updateFields() # Update the layer's fields after adding
        
        print(f'Field "{field[0]}" added to layer "{layer.name()}"')
    layer.commitChanges()
    
    # Area and porcentual distribution values
    layer.startEditing()
    if layer and layer.geometryType() == QgsWkbTypes.PolygonGeometry:
        total_area = 0.0
        field_index = layer.fields().indexOf(area_field[0])
        for feature in layer.getFeatures():
            fid = feature.id()
            geom = feature.geometry()
            geom.transform(transform)
            area = geom.area()/10000 
            total_area += area
            layer.changeAttributeValue(fid, field_index, area)
        print(f'Total area: {total_area} ha')
        field_index = layer.fields().indexOf(areapd_field[0])
        for feature in layer.getFeatures():
            fid = feature.id()
            areadp = (feature[layer.fields().indexFromName(area_field[0])] / total_area) * 100
            layer.changeAttributeValue(fid, field_index, areadp)        
    else:
        print('Please select a valid polygon layer')
    layer.commitChanges()
    print('Assigned values completed.')    
   
else:
    print('Error: No active layer found, or the layer does not support adding or calculate fields.')


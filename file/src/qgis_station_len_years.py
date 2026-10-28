# https://github.com/rcfdtools
# Calculate the hipotetical stations year length in a full range or in a specified time window
# This script has to be run in the QGIS Python console
# Stop editing before run the script
# Make sure a layer is selected in the Layers panel
# Before run create manually the follow fields:
# FInst = to_date("FECHA_INSTALACION",'dd/M/yyyy')
# FSus = to_date("FECHA_SUSPENSION",'dd/M/yyyy')
# Tested in QGIS 3.44.6

from qgis.PyQt.QtCore import QVariant
from qgis.core import QgsField, edit
import qgis.utils
from PyQt5.QtCore import QDate # ● PyQt5 for QGIS 3 or PyQt6 for QGIS 4


# Get the active layer from Layer panel
layer = iface.activeLayer()


# General parameters
installation_date_field = 'FInst' # ● Your installation date field name
suspension_date_field = 'FSus' # ● Your suspension date field name
tw_start_date = QDate(1980, 1, 1) # ● Time-window start
tw_end_date = QDate(2025, 12, 31) # ●Time-window end
tw_start_date_name = 'InDateTW'
tw_end_date_name = 'OutDateTW'
lyears_name = 'LYearS'
lyearstw_name = 'LYearSTW'


# Add fields and do calculations
new_field_list = [[tw_start_date_name, QVariant.Date], [tw_end_date_name, QVariant.Date], [lyears_name, QVariant.Double], [lyearstw_name, QVariant.Double]]
if layer and layer.dataProvider().capabilities() & QgsVectorDataProvider.AddAttributes:
    # Fields creation
    for field in new_field_list:
        # Check and delete existind required fields
        field_index = layer.fields().indexFromName(field[0])
        if field_index != -1:
            with edit(layer):
                 layer.dataProvider().deleteAttributes([field_index])
        layer.updateFields()
        
        # New Field, parameters are: field name, data type, field length, precision
        if field[1] == QVariant.Date:
            new_field = QgsField(field[0], field[1])
        else:
            new_field = QgsField(field[0], field[1], len=20, prec=10)
            
        # Use an editing buffer to add the field and commit changes automatically
        with edit(layer):
            layer.dataProvider().addAttributes([new_field])
            layer.updateFields() # Update the layer's fields after adding
        
        print(f'Field "{field[0]}" added to layer "{layer.name()}"')
    layer.commitChanges()
    
    # Calculate LYearS
    for feature in layer.getFeatures():
        fid = feature.id()
        installation_date = feature[layer.fields().indexFromName(installation_date_field)]
        suspension_date = feature[layer.fields().indexFromName(suspension_date_field)]
        if installation_date:
            if installation_date <= tw_start_date:
                tw_installation_date = tw_start_date
            else:
                tw_installation_date = installation_date
            if suspension_date:
                if suspension_date >= tw_end_date:
                    tw_suspension_date = tw_end_date
                else:
                    tw_suspension_date = suspension_date
                diff_date = installation_date.daysTo(suspension_date)
                tw_diff_date = tw_installation_date.daysTo(tw_suspension_date)
            else:
                diff_date = installation_date.daysTo(tw_end_date)
                tw_diff_date = tw_installation_date.daysTo(tw_end_date)
            diff_date = float(diff_date)/365
            tw_diff_date = float(tw_diff_date)/365
            if diff_date < 0: diff_date = 0
            if tw_diff_date < 0: tw_diff_date = 0
        else:
            diff_date = 0
            tw_diff_date = 0
        layer.startEditing()
        field_index = layer.fields().indexOf(tw_start_date_name)
        layer.changeAttributeValue(fid, field_index, tw_start_date)        
        field_index = layer.fields().indexOf(tw_end_date_name)
        layer.changeAttributeValue(fid, field_index, tw_end_date)   
        field_index = layer.fields().indexOf(lyears_name)
        layer.changeAttributeValue(fid, field_index, diff_date)
        field_index = layer.fields().indexOf(lyearstw_name)
        layer.changeAttributeValue(fid, field_index, tw_diff_date)
    layer.commitChanges()
    print('Calculations done')    
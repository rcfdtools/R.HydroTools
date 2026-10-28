# https://github.com/rcfdtools
# Geology homologation from AGC to ANLA model
# This script has to be run in the QGIS Python console
# Stop editing before run the script
# Make sure the UC layer is selected in the Layers panel
# Tested in QGIS 3.44.6

from qgis.PyQt.QtCore import QVariant
from qgis.core import QgsField, edit
import qgis.utils


# Get the active layer from Layer panel
layer = iface.activeLayer()

# General parameters
eon_field = ['EON', QVariant.Double]
era_field = ['ERA', QVariant.Double]
periodo_field = ['PERIODO', QVariant.Double]
epoca_field = ['EPOCA', QVariant.Double]
edad_field = ['EDAD', QVariant.Double]
nombre_field = ['NOMBRE', QVariant.String, '', 100]
nomenclat_field = ['NOMENCLAT', QVariant.String, '', 20]
uc_old_edad_field = 'Edad'  # Current edad name in UC layer
uc_new_edad_field = 'EdadTxt'  # New edad txt name in UC layer
uc_nombre_field = 'Descripcio'    
uc_nomenclat_field = 'SimboloUC'    
# geology_homologation >> UC_EdadTxt, ANLA_EON, ANLA_ERA, ANLA_PERIODO, ANLA_EPOCA, ANLA_EDAD
geology_homologation = [['Albiano-Maastrichtiano',100000,120000,121000,121100,121160],
                        ['Bartoniano-Chattiano',100000,110000,113000,113200,113260],
                        ['Cenomaniano-Maastrichtiano',100000,120000,121000,121200,121210],
                        ['Cuaternario',100000,110000,111000,'',''],
                        ['Maastrichtiano-Paleoceno',100000,120000,121000,121200,121260],
                        ['Mioceno',100000,110000,112000,112100,''],
                        ['Paleoceno',100000,110000,113000,113100,''],
                        ['Pleistoceno',100000,110000,111000,111100,''],
                        ['Plioceno-Pleistoceno',100000,110000,111000,111100,''],
                        ['Serravaliano-Mesiniano',100000,110000,112000,112100,112140],
                        ['Valanginiano-Albiano',100000,120000,121000,121100,121120]]

# Add fields and do calculations
new_field_list = [eon_field, era_field, periodo_field, epoca_field, edad_field, nombre_field, nomenclat_field]
if layer and layer.dataProvider().capabilities() & QgsVectorDataProvider.AddAttributes:
    # Rename current UC Edad name
    field_index = layer.fields().indexFromName(uc_old_edad_field)
    if field_index != -1:
        layer.startEditing()
        try:
            layer.renameAttribute(field_index, uc_new_edad_field)
            layer.commitChanges()
            print(f"Field '{uc_old_edad_field}' successfully renamed to '{uc_new_edad_field}'.")
        except:
            layer.rollbackChanges()
            print("Error renaming field. Changes rolled back.")
    else:
        print(f"Field '{uc_old_edad_field}' not found.")        
    
    # Fields creation
    for field in new_field_list:
        # Check and delete existind required fields
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
    
    # Assign values
    layer.startEditing()
    for feature in layer.getFeatures():
        fid = feature.id()
        
        # Exisiting values
        field_index = layer.fields().indexOf(nombre_field[0])
        layer.changeAttributeValue(fid, field_index, feature[layer.fields().indexFromName(uc_nombre_field)])
        field_index = layer.fields().indexOf(nomenclat_field[0])
        layer.changeAttributeValue(fid, field_index, feature[layer.fields().indexFromName(uc_nomenclat_field)])
        edad_val = feature[layer.fields().indexFromName(uc_new_edad_field)]
        
        # EON
        field_index = layer.fields().indexOf(eon_field[0])
        for homologa_val in geology_homologation:
            if edad_val == homologa_val[0]:
                layer.changeAttributeValue(fid, field_index, homologa_val[1])
        
        # ERA
        field_index = layer.fields().indexOf(era_field[0])
        for homologa_val in geology_homologation:
            if edad_val == homologa_val[0]:
                layer.changeAttributeValue(fid, field_index, homologa_val[2])       
        
        # Period
        field_index = layer.fields().indexOf(periodo_field[0])
        for homologa_val in geology_homologation:
            if edad_val == homologa_val[0]:
                layer.changeAttributeValue(fid, field_index, homologa_val[3])  
        
        # Epoch
        field_index = layer.fields().indexOf(epoca_field[0])
        for homologa_val in geology_homologation:
            if edad_val == homologa_val[0]:
                layer.changeAttributeValue(fid, field_index, homologa_val[4])  
        
        # Ages
        field_index = layer.fields().indexOf(edad_field[0])
        for homologa_val in geology_homologation:
            if edad_val == homologa_val[0]:
                layer.changeAttributeValue(fid, field_index, homologa_val[5])  
                
    layer.commitChanges()
    print('Assigned values completed.')    
   
else:
    print('Error: No active layer found, or the layer does not support adding or calculate fields.')



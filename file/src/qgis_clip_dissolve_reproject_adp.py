# https://github.com/rcfdtools
# Clip, Dissolve, Reproject and calculates the area percentual distribution APD
# Before run set Settings / Options / Processing / General / Invalid features filtering / Do not filter

# Libraries
import processing
import os
from qgis.core import QgsField, QgsVectorLayer

# General parameters
#input_layer_path = 'D:/R.IAMB/file/data/SGC/agc2023.gdb|layername=UC' # ● Atlas geológico de Colombia - Unidades cronoestratigráficas
#input_layer_path = 'D:/R.IAMB/file/data/IGAC/SUELOS_CUNDINAMARCA_100K.gdb|layername=SUELOS_CUNDINAMARCA_VF' # ● Mapa de suelos de cundinamarca
#input_layer_path = 'D:/R.IAMB/file/shp/MunicipiosAreaProyecto.shp' # ● Municipios de Colombia
#input_layer_path = 'D:/R.IAMB/file/data/DANE/VeredasColombia20260306.shp' # ● Veredas de Colombia
output_path = 'D:/R.IAMB/file/shp/' # ●
input_layer_path = 'D:/R.IAMB/file/data/IGAC/GestoresCatastrales20240301/municipioserviciosV.shp' # ● Veredas de Colombia
overlay_layer_path = 'D:/R.IAMB/file/gdb/BD_ANLA_MAGNA_NACIONAL.gdb|layername=AreaProyecto' # ● Layer used as clip mask
output_file_clip_name = 'GestoresCatastralesAreaProyecto' # Name without .shp extension, e.g., UCAreaProyecto, SuelosVFAreaProyecto, MunicipiosAreaProyectoClip, VeredaAreaProyecto ●
dissolve_field = 'gestor_cat' # e.g., SimboloUC, UCS_F, MpCodigo, CODIGO_VER, gestor_cat ●
crs_target_code = '9377' # Define the CRS code for the calculations ●
output_file_clip_path = f'{output_path}{output_file_clip_name}.shp'
output_file_dissolve_path = f'{output_path}{output_file_clip_name}Dissolve.shp'
output_file_dissolve_path_reprojected = f'{output_path}{output_file_clip_name}Dissolve{crs_target_code}.shp'
crs_target = QgsCoordinateReferenceSystem(f'EPSG:{crs_target_code}')
area_field = ['Aha', QVariant.Double]
areapd_field = ['APD', QVariant.Double] # ● APD correspond to Area Percentual Distribution


# Load the vector layers into QGIS
input_layer = QgsVectorLayer(input_layer_path, 'InputLayer', 'ogr')
overlay_layer = QgsVectorLayer(overlay_layer_path, 'OverlayLayer', 'ogr')

# Check if layers loaded correctly
if not input_layer.isValid() or not overlay_layer.isValid():
    print('One or both layers failed to load. Check file paths.')
else:
    # Clip
    parameters = {'INPUT': input_layer, 'OVERLAY': overlay_layer, 'OUTPUT': output_file_clip_path}
    processing.run('qgis:clip', parameters)
    print(f'Clipped layer {output_file_clip_path}')
    
    # Dissolve
    parameters = {'INPUT': output_file_clip_path, 'FIELD': [dissolve_field], 'OUTPUT': output_file_dissolve_path}
    processing.run('native:dissolve', parameters)
    #layer = QgsVectorLayer(output_file_dissolve_path, f'{output_file_clip_name}Dissolve', 'ogr')
    #QgsProject.instance().addMapLayer(layer)
    print(f'Dissolved layer {output_file_dissolve_path}')
 
    # Reproject layer
    parameters = {'INPUT': output_file_dissolve_path, 'TARGET_CRS': crs_target, 'OUTPUT': output_file_dissolve_path_reprojected}
    processing.run('native:reprojectlayer', parameters)
    layer = QgsVectorLayer(output_file_dissolve_path_reprojected, f'{output_file_clip_name}Dissolve{crs_target_code}', 'ogr')
    QgsProject.instance().addMapLayer(layer)
    print(f'Dissolved reprojected layer {output_file_dissolve_path}')
    
    # APD calculations
    crs_source = layer.crs()
    transform = QgsCoordinateTransform(crs_source, crs_target, QgsProject.instance().transformContext())    
    layer.startEditing()
    layer.dataProvider().addAttributes([QgsField(area_field[0], area_field[1])])
    layer.dataProvider().addAttributes([QgsField(areapd_field[0], areapd_field[1])])
    layer.updateFields()
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
        print('Assigned values completed.')
    else:
        print('Please use a valid polygon layer')
    layer.commitChanges()

# https://github.com/rcfdtools
# Clip, Dissolve, Reproject and calculates the percentual distribution area ADP
# Before run set Settings -> Options -> Processing -> General -> Invalid features filtering as Do not filter

# Libraries
import processing
import os

# General parameters
input_layer_path = 'D:/R.IAMB/file/data/SGC/agc2023.gdb|layername=UC' # ●
overlay_layer_path = 'D:/R.IAMB/file/gdb/BD_ANLA_MAGNA_NACIONAL.gdb|layername=AreaProyecto' # ●
output_path = 'D:/R.IAMB/file/shp/'
output_file_clip_name = 'UCAreaProyecto' # Name without .shp extension ●
dissolve_field = 'SimboloUC' # ●
output_file_clip_path = f'{output_path}{output_file_clip_name}.shp'
output_file_dissolve_path = f'{output_path}{output_file_clip_name}Dissolve.shp'

# Load the vector layers into QGIS
input_layer = QgsVectorLayer(input_layer_path, 'InputLayer', 'ogr')
overlay_layer = QgsVectorLayer(overlay_layer_path, 'OverlayLayer', 'ogr')

# Check if layers loaded correctly
if not input_layer.isValid() or not overlay_layer.isValid():
    print('One or both layers failed to load. Check file paths.')
else:
    parameters = {'INPUT': input_layer, 'OVERLAY': overlay_layer, 'OUTPUT': output_file_clip_path}
    clip = processing.run('qgis:clip', parameters)
    parameters = {'INPUT': output_file_clip_path, 'FIELD': [dissolve_field], 'OUTPUT': output_file_dissolve_path}
    processing.run("native:dissolve", parameters)
    if os.path.exists(output_file_dissolve_path):
        dissolved_layer = QgsVectorLayer(output_file_dissolve_path, f'{output_file_clip_name}Dissolve', 'ogr')
        if dissolved_layer.isValid():
            QgsProject.instance().addMapLayer(dissolved_layer)
            print(f'Clipped layer saved to: {output_file_dissolve_path} and added to map.')
        else:
            print('Clipped layer generated but failed to load into QGIS project.')
    else:
        print('Algorithm ran, but output file was not created.')

from qgis import processing
from qgis.core import QgsRasterLayer, QgsVectorLayer

raster_path = 'C:/Temp/ERA5/ERA5_land_monthly_climatological_var_010ddRioBogota_ssr.tif'
polygon_path = 'C:/Temp/ERA5/SZH2120.shp'
raster_layer = QgsRasterLayer(raster_path, 'Raster Layer')
polygon_layer = QgsVectorLayer(polygon_path, 'Polygon Layer', "ogr")


alg_params = {
            'COLUMN_PREFIX': 'ssr_',
            'INPUT': polygon_layer,
            'INPUT_RASTER': raster_layer,
            'RASTER_BAND': 1,
            'STATISTICS': [0,1,2,3,4],
            'OUTPUT': 'C:/Temp/ERA5/test/Test.csv'
        }
processing.run('native:zonalstatisticsfb', alg_params, is_child_algorithm=True)

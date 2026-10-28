from qgis import processing
from qgis.core import QgsRasterLayer, QgsVectorLayer

alg_params = {
            'COLUMN_PREFIX': 'ssr_',
            'INPUT': 'C:/Temp/ERA5/SZH2120.shp',
            'INPUT_RASTER': 'C:/Temp/ERA5/ERA5_land_monthly_climatological_var_010ddRioBogota_ssr.tif',
            'RASTER_BAND': 1,
            'STATISTICS': [0,1,2,3,4],
            'OUTPUT': 'C:/Temp/ERA5/stat/Test.csv'
        }
processing.run('native:zonalstatisticsfb', alg_params)


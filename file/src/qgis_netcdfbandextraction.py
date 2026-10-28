# NetCDF band extraction
# 0. Load the required .nc variable into QGIS layers.
# 1. Export to a Tiff file.
import processing

variable = 'ssr' 
steps = 12 # number of hours, days or months to extract
raster_path = 'C:/Temp/ERA5/ERA5_land_monthly_climatological_var_010ddRioBogota_ssr.tif'
raster_layer = QgsRasterLayer(raster_path, 'Raster Layer')
output_path = 'C:/Temp/ERA5/band/'

for i in range(steps):
    print('Processing band: '+str(i+1))
    processing.run(
        "gdal:rearrange_bands",
        {
            'INPUT': raster_layer,
            'BANDS': i+1,
            'OPTIONS': '',  # Additional creation options (optional)
            'DATA_TYPE': 0, # 0 for "Use Input Layer Data Type"
            'OUTPUT': output_path+variable+str(i+1)+'.tif'
        }
    )


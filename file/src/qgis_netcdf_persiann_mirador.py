# https://github.com/rcfdtools
# Processing Persiann & Mirador NetCDF files in QGIS
# From OSGeo4W Shell install: 
# python -m pip install rasterio
# Convert CRS from QGIS command
# >gdal_translate -a_srs EPSG:4326 -of netCDF 3B42_Daily.20191230.7.nc4.nc 3B42_Daily.20191230.7.nc4.4326.nc

import rasterio
from matplotlib import pyplot
import numpy as np

#Load file and check properties
#src = rasterio.open(r'C:\Temp\QH6E\Datos\Mirador\3B42_Daily.20191230.7.nc4.nc')
src = rasterio.open(r'C:\TSIG\Taller6\6E\Persiann\PERSIANN-CDR_v01r01_20191230_c20200522.nc')
srcprofile = src.profile
print(f'\nSource profile\n{srcprofile}')
array = src.read(1) #1 means precipitation
print(f'\nGeneral parameters\n* File: {src.name}\n* Bounds: {src.bounds}\n* Time steps: {src.count}\n* CRS: {src.crs}\n* Array shape: {array.shape}')

#Show original image
pyplot.figure()
pyplot.imshow(array, cmap='viridis')
pyplot.show() 

#Coordinates for a given cell
print(f'* Cell value in xy(64,64): {src.xy(64,64)}')

#Show original image
arrayrot = np.rot90(array,-1)
arrayrot = np.flip(arrayrot,-1)
pyplot.figure()
pyplot.imshow(arrayrot, cmap='viridis')
pyplot.show() 


'''
References NetCDF in QGIS
https://courses.gisopencourseware.org/mod/book/tool/print/index.php?id=1342
https://hatarilabs.com/ih-en/netcdf-for-water-resources-with-python-for-dummies-chirps-dataset-tutorial
https://stackoverflow.com/questions/75659352/convert-the-netcdf-file-to-geotiff-with-chosen-coordinate-system
https://gis.stackexchange.com/questions/323317/converting-netcdf-dataset-array-to-geotiff-using-rasterio-python
https://landscapearchaeology.org/2018/installing-python-packages-in-qgis-3-for-windows/
'''


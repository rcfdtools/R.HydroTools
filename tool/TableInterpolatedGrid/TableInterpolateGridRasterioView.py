# Install Rasterio over Python 3.10
# https://rasterio.readthedocs.io/en/latest/topics/plotting.html

import rasterio
from matplotlib import pyplot
src = rasterio.open("D:\R.GISPython\TableInterpolatedGrid\OutputGrid\GRDM039.tif")
pyplot.imshow(src.read(1), cmap='pink')
#<matplotlib.image.AxesImage object at 0x...>
pyplot.show()
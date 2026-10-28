# https://github.com/rcfdtools
# Print a table or a shapefile table content in console
# This script has to be run in the QGIS Python console
# Stop editing before run the script
# Make sure the UC layer is selected in the Layers panel
# Tested in QGIS 3.44.6
# Before run: Open OSGeo4W Shell and run python -m pip install tabulate

# Libraries
from qgis.core import QgsField, QgsVectorLayer
from tabulate import tabulate

layer = iface.activeLayer()
if layer:
    features = layer.getFeatures()
    field_names = [field.name() for field in layer.fields()]
    table_data = []

    for ft in features:
        table_data.append(ft.attributes())

    # Print the data as a "pretty" table
    print(tabulate(table_data, headers=field_names, tablefmt='markdown'))

else:
    print("No active layer found or layer is not a vector layer.")
# Create a shapefile incluiding a point feature
import qgis

output_path = 'D:/R.DAPC/file/shp/DAPC_newshapefile.shp'  # Specify your desired output path
crs = QgsCoordinateReferenceSystem('EPSG:9377')  # WGS 84
fields = QgsFields()
fields.append(QgsField('ID', QVariant.Int))
fields.append(QgsField('Name', QVariant.String))
fields.append(QgsField('Value', QVariant.Double))
# Geometry type can be QgsWkbTypes.Point, QgsWkbTypes.LineString, or QgsWkbTypes.Polygon
writer = QgsVectorFileWriter(output_path, 'UTF-8', fields, QgsWkbTypes.Point, crs, 'ESRI Shapefile')
if writer.hasError() != QgsVectorFileWriter.NoError:
    print(f'Error creating shapefile: {writer.hasError()}')
    #exit()
feat = QgsFeature()
feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(5000000, 2000000)))
feat.setAttributes([1,'DAPC Point', 2025])
writer.addFeature(feat)
iface.addVectorLayer(output_path, '', 'ogr')
del writer
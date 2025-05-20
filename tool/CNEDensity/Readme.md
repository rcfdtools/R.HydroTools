<div align="center"><img alt="R.HydroTools" src="../../file/graph/R.HydroTools.svg" width="300px"></div>

## Análisis de la distribución espacial de la red de estaciones hidroclimatológicas de Colombia y su importancia en los estudios hidrológicos (en construcción)
Keywords: 'cne' `cne-spatial-disbribution`
 
en: Spatial distribution analysis from the National Colombia stations catalog and their relevance in hydrologic studies

Estudio general de la distribución espacial de la estaciones hidro-climatológicas de Colombia. 


### Preliminary (ok)

1. Get the IDEAM CNE stations and other stations catalogs (Microsoft Excel files)
	http://dhime.ideam.gov.co/atencionciudadano/
	http://www.ideam.gov.co/solicitud-de-informacion
	http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
	http://bart.ideam.gov.co/cneideam/CNE_OE.xls
2. Delete not updated or not required attributes: OBJECTID, AREA_HIDROGRAFICA, ZONA_HIDROGRAFICA, SUBZONA_HIDROGRAFICA.....
3. Concat catalogs into a dataframe
4. Update locations with an external manual locations table. Many current CNE locations are not accurate. update_locations.csv
5. Create station categories dictionary with abbreviations (category_dict.csv) and join with stations catalog
6. Truncate long attributes names to 10 characters for dBase .dbf shapefile compatibility
7. Convert joined catalog into a shapefile with CRS 4326
8. Upgrade the stations elevations using a DEM file. ASTER GDEM v3
9. Colombia hydrographic subzones (external and manual procedure, required only one time. Not included in Python script)
	Get manually the Colombia hydrographic subzones Zonificacion_hidrografica_2013.shp. CRS 4686
	Convert manually to CRS 4326 Zonificacion_hidrografica_2013_4326.shp
	Calculate area Akm2_SZH manually using QGIS and CRS 3857 WGS_1984_Web_Mercator_Auxiliary_Sphere
	(Optional) Dissolve subzones to zones and hydrographic areas
10. Spatial intersection between stations catalog and hydrographic subzones as points using Python. New attributes: COD_AH, COD_ZH, COD_SZH, NOM_AH, NOM_ZH, NOM_SZH, Akm2_SZH
11. Create categories parametes dictionary (category_parameter_dict.csv). Required for the main study analysis


### Research analysis

Ok. Number stations per category with Coverage, radius and WMO reference evaluation
Ok. Number stations per AH (basic analysis)
Ok. Number stations per ZH (basic analysis)
Number stations per SZH
Number stations per year (analysis with installation and suspension dates) 

Coverage area per station C = (Akm2 / n)
Coverage radius per station r = √ ( C / π)
Compare coverage radius and reference value from the World Meteorological Organization WMO. See https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStationElevation


### Complementary analysis
	
* Distance between stations from a TIN surface with the elevation value
* Coverage area from station with Thiessen Voronoi polygons
* Thermal level analysis (Caldas and conventional cuts)


### References

* https://www.includehelp.com/python/update-a-dataframe-value-from-another-dataframe.aspx
* https://gis.stackexchange.com/questions/441326/computing-zonal-statistics-with-rasterstats-in-python
* https://www.geeksforgeeks.org/python-get-last-n-characters-of-a-string/
* https://geopandas.org/en/stable/gallery/create_geopandas_from_pandas.html (also includes a plot representation)
* https://pygis.io/docs/e_vector_overlay.html
* https://www.geeksforgeeks.org/convert-the-column-type-from-string-to-datetime-format-in-pandas-dataframe/
* https://www.sharpsightlabs.com/blog/pandas-value_counts/#value-counts-parameters
* https://stackoverflow.com/questions/13148429/how-to-change-the-order-of-dataframe-columns


### Licencia, cláusulas y condiciones de uso

_R.HydroTools es de uso libre para fines académicos, conoce nuestra [licencia, cláusulas, condiciones de uso](../../LICENSE.md) y como referenciar los contenidos publicados en este repositorio._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [r.cfdtools](https://github.com/rcfdtools) en GitHub._

| [:house: Inicio](../../README.md)  | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.HydroTools/discussions/xxx) |
|------------------------------------|------------------------------------------------------------------------------------------|
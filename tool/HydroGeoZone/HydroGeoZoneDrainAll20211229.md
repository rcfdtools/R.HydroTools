## Zonificación hidrográfica de Colombia - Análisis de forma y densidad usando Python - Todos los subtipos de drenaje

![HydroGeoZone.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/HydroGeoZone.png)

* Archivo de resultados: D:/R.GISPython/HydroGeoZone/HydroGeoZoneDrainAll20211229.md
* Fecha y hora de inicio de ejecución: 2021-12-29 12:24:41.952392
* Script compatible con: ArcGIS for Desktop 10.6+ y ArcGIS Pro
* Python versión: 3.7.11 [MSC v.1927 64 bit (AMD64)]
* Python rutas: ['D:\\R.GISPython\\HydroGeoZone', 'C:\\Program Files\\ArcGIS\\Pro\\Resources\\ArcPy', 'D:\\R.GISPython', 'D:\\R.GISPython.wiki', 'C:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\arcgispro-py3\\python37.zip']
* matplotlib versión: 3.4.2
* Encuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone
* Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License
* Créditos: r.cfdtools@gmail.com

```
Sistema de coordenadas: PROJCS['MAGNA-SIRGAS / Origen-Nacional',GEOGCS['GCS_MAGNA',DATUM['D_MAGNA',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',5000000.0],PARAMETER['False_Northing',2000000.0],PARAMETER['Central_Meridian',-73.0],PARAMETER['Scale_Factor',0.9992],PARAMETER['Latitude_Of_Origin',4.0],UNIT['Meter',1.0]] # GEOGCS['GCS_MAGNA',DATUM['D_MAGNA',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]
```

### Parámetros y datos de entrada ([/Data](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone/Data))

* Ruta absoluta: D:/R.GISPython/HydroGeoZone
* Espacio de trabajo ArcPy: D:/R.GISPython/HydroGeoZone/Data
* Capa de entrada SZH - Subzonas hidrográficas: D:/R.GISPython/HydroGeoZone/Data/Zonificacion_hidrografica_2013.shp
* Capa de entrada Drenajes: D:/R.GISPython/HydroGeoZone/Data/Drenaje_Sencillo.shp
* Intersección SZH & Drenajes: False
* Recálculo de estadísticos: False
* Analizar solo drenajes permanentes: False

## Propiedades y entidades encontradas para las capas de entrada

### Campos en D:/R.GISPython/HydroGeoZone/Data/Zonificacion_hidrografica_2013.shp (Polygons 316)

| # | Campo | Tipo |
|---|---|---|
| 1 | FID | OID |
| 2 | Shape | Geometry |
| 3 | OBJECTID_1 | Integer |
| 4 | COD_AH | SmallInteger |
| 5 | COD_ZH | SmallInteger |
| 6 | COD_SZH | SmallInteger |
| 7 | NOM_AH | String |
| 8 | NOM_ZH | String |
| 9 | NOM_SZH | String |
| 10 | Shape_Leng | Double |
| 11 | Shape_Area | Double |
| 12 | RULEID | Integer |


### Campos en D:/R.GISPython/HydroGeoZone/Data/Drenaje_Sencillo.shp (Polylines 426719)

| # | Campo | Tipo |
|---|---|---|
| 1 | FID | OID |
| 2 | Shape | Geometry |
| 3 | OBJECTID | Integer |
| 4 | NOMBRE_GEO | String |
| 5 | ESTADO_DRE | Integer |
| 6 | PROYECTO | String |
| 7 | SYMBOL | String |
| 8 | FECHA | Date |
| 9 | DISPERSION | String |
| 10 | RULEID | Integer |
| 11 | PK_CUE | Double |
| 12 | GLOBALID | String |
| 13 | SHAPE_Leng | Double |
| 14 | LDre | Double |

### Evaluación de drenajes por subtipo

> (0 - Sin asignación, 5101 - Permanente, 5102 - Intermitente)

| Código | # Drenajes |
|---|---|
| 0 | 140 |
| 5101 | 421909 |
| 5102 | 4670 |

## Distribución de áreas en km² de subzonas por área hidrográfica

### Total nacional de SZH - subzonas hidrográficas por rango de área

| Rango km² | # Subzonas | Acumulado |
|---|---|---|
| 0-300 | 9 | 9 |
| 300-700 | 19 | 28 |
| 700-900 | 16 | 44 |
| 900-1100 | 18 | 62 |
| 1100-1300 | 18 | 80 |
| 1300-1500 | 11 | 91 |
| 1500-2000 | 34 | 125 |
| 2000-2500 | 29 | 154 |
| 2500-3500 | 40 | 194 |
| 3500-5000 | 45 | 239 |
| 5000-10000 | 60 | 299 |
| 10000-20000 | 14 | 313 |
| 20000-999999 | 1 | 314 |

### Total SZH - subzonas hidrográficas por rango de área para cada AH - área hidrográfica


#### AH - Área hidrográfica 1 - Caribe

| Rango km² | # Subzonas | Acumulado |
|---|---|---|
| 0-300 | 3 | 3 |
| 300-700 | 3 | 6 |
| 700-900 | 2 | 8 |
| 900-1100 | 4 | 12 |
| 1100-1300 | 3 | 15 |
| 1300-1500 | 3 | 18 |
| 1500-2000 | 9 | 27 |
| 2000-2500 | 3 | 30 |
| 2500-3500 | 8 | 38 |
| 3500-5000 | 3 | 41 |
| 5000-10000 | 5 | 46 |
| 10000-20000 | 0 | 46 |
| 20000-999999 | 0 | 46 |

#### AH - Área hidrográfica 2 - Magdalena Cauca

| Rango km² | # Subzonas | Acumulado |
|---|---|---|
| 0-300 | 4 | 4 |
| 300-700 | 13 | 17 |
| 700-900 | 7 | 24 |
| 900-1100 | 9 | 33 |
| 1100-1300 | 10 | 43 |
| 1300-1500 | 7 | 50 |
| 1500-2000 | 10 | 60 |
| 2000-2500 | 7 | 67 |
| 2500-3500 | 14 | 81 |
| 3500-5000 | 9 | 90 |
| 5000-10000 | 14 | 104 |
| 10000-20000 | 1 | 105 |
| 20000-999999 | 0 | 105 |

#### AH - Área hidrográfica 3 - Orinoco

| Rango km² | # Subzonas | Acumulado |
|---|---|---|
| 0-300 | 2 | 2 |
| 300-700 | 0 | 2 |
| 700-900 | 2 | 4 |
| 900-1100 | 2 | 6 |
| 1100-1300 | 3 | 9 |
| 1300-1500 | 1 | 10 |
| 1500-2000 | 8 | 18 |
| 2000-2500 | 7 | 25 |
| 2500-3500 | 5 | 30 |
| 3500-5000 | 16 | 46 |
| 5000-10000 | 21 | 67 |
| 10000-20000 | 6 | 73 |
| 20000-999999 | 0 | 73 |

#### AH - Área hidrográfica 4 - Amazonas

| Rango km² | # Subzonas | Acumulado |
|---|---|---|
| 0-300 | 0 | 0 |
| 300-700 | 1 | 1 |
| 700-900 | 0 | 1 |
| 900-1100 | 1 | 2 |
| 1100-1300 | 1 | 3 |
| 1300-1500 | 0 | 3 |
| 1500-2000 | 4 | 7 |
| 2000-2500 | 6 | 13 |
| 2500-3500 | 7 | 20 |
| 3500-5000 | 9 | 29 |
| 5000-10000 | 20 | 49 |
| 10000-20000 | 7 | 56 |
| 20000-999999 | 1 | 57 |

#### AH - Área hidrográfica 5 - Pacifico

| Rango km² | # Subzonas | Acumulado |
|---|---|---|
| 0-300 | 0 | 0 |
| 300-700 | 2 | 2 |
| 700-900 | 5 | 7 |
| 900-1100 | 2 | 9 |
| 1100-1300 | 1 | 10 |
| 1300-1500 | 0 | 10 |
| 1500-2000 | 3 | 13 |
| 2000-2500 | 6 | 19 |
| 2500-3500 | 6 | 25 |
| 3500-5000 | 8 | 33 |
| 5000-10000 | 0 | 33 |
| 10000-20000 | 0 | 33 |
| 20000-999999 | 0 | 33 |

## Visualización de tablas resultados para análisis de forma y densidad

### AH - área hidrográfica

D:/R.GISPython/HydroGeoZone/Output/AreaHidrograficaEstadistica.dbf

| AH | Nombre AH | Área, km² | Perm, km | n Drenajes | Sum. LCi, km | Kc | Dd | Dc | Kc Tag |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Caribe | 102803.08 | 4814.69 | 39119 | 108190.65 | 4.24 | 1.05 | 0.38 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 270888.94 | 3763.38 | 134281 | 314458.56 | 2.04 | 1.16 | 0.5 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 346081.36 | 3736.08 | 122458 | 301766.4 | 1.79 | 0.87 | 0.35 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 341164.55 | 6122.88 | 101572 | 298438.97 | 2.96 | 0.87 | 0.3 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 77372.03 | 3360.07 | 35124 | 81609.93 | 3.41 | 1.05 | 0.45 | Oval-oblonga a rectangular-oblonga |

### ZH - zona hidrográfica

D:/R.GISPython/HydroGeoZone/Output/ZonaHidrograficaEstadistica.dbf

| AH | Nombre AH | ZH | Nombre ZH | Área, km² | Perm, km | n Drenajes | Sum. LCi, km | Kc | Dd | Dc | Kc Tag |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Caribe | 11 | Atrato - Darién | 37837.02 | 1568.38 | 13615 | 39050.93 | 2.27 | 1.03 | 0.36 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 12 | Caribe - Litoral | 12975.9 | 1336.35 | 4344 | 13865.35 | 3.31 | 1.07 | 0.33 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 13 | Sinú | 14101.53 | 890.79 | 3166 | 10845.28 | 2.12 | 0.77 | 0.22 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 21371.89 | 1252.31 | 8310 | 23469.98 | 2.42 | 1.1 | 0.39 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 16 | Catatumbo | 16439.46 | 789.96 | 9679 | 20948.14 | 1.74 | 1.27 | 0.59 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 17 | Islas Caribe | 77.29 | 109.87 | 5 | 10.96 | 3.53 | 0.14 | 0.06 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 44503.94 | 1891.31 | 23992 | 55857.48 | 2.53 | 1.26 | 0.54 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 22 | Saldaña | 9961.0 | 603.0 | 7774 | 14866.61 | 1.7 | 1.49 | 0.78 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 59628.27 | 2005.81 | 32194 | 71567.76 | 2.32 | 1.2 | 0.54 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 24 | Sogamoso | 23206.44 | 1046.29 | 12392 | 28066.87 | 1.94 | 1.21 | 0.53 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 25 | Bajo Magdalena- Cauca -San Jorge | 21142.21 | 1045.18 | 5496 | 17827.1 | 2.03 | 0.84 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 45739.61 | 2627.71 | 25193 | 57307.42 | 3.47 | 1.25 | 0.55 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 27 | Nechí | 14603.72 | 872.53 | 9015 | 17024.62 | 2.04 | 1.17 | 0.62 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 28 | Cesar | 22892.03 | 849.58 | 9155 | 25441.49 | 1.58 | 1.11 | 0.4 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 29211.73 | 1309.22 | 9070 | 26499.23 | 2.16 | 0.91 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 31 | Inírida | 53591.77 | 1926.75 | 20940 | 50386.44 | 2.35 | 0.94 | 0.39 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 84348.26 | 2733.95 | 29348 | 75165.5 | 2.66 | 0.89 | 0.35 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 33 | Vichada | 26118.92 | 1469.25 | 15943 | 28040.12 | 2.56 | 1.07 | 0.61 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 34 | Tomo | 20213.3 | 1189.87 | 7857 | 15978.9 | 2.36 | 0.79 | 0.39 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 82506.03 | 2504.65 | 26097 | 73274.44 | 2.46 | 0.89 | 0.32 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 36 | Casanare | 24176.66 | 791.28 | 2903 | 14808.37 | 1.44 | 0.61 | 0.12 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 37 | Arauca | 11348.72 | 999.15 | 2944 | 9176.94 | 2.65 | 0.81 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 38 | Orinoco Directos | 43514.08 | 3424.61 | 16336 | 34695.0 | 4.63 | 0.8 | 0.38 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 39 | Apure | 263.63 | 106.78 | 90 | 240.7 | 1.86 | 0.91 | 0.34 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 41 | Guanía | 31130.32 | 1561.0 | 12852 | 29879.38 | 2.5 | 0.96 | 0.41 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 42 | Vaupes | 37570.93 | 1820.01 | 7763 | 25828.86 | 2.65 | 0.69 | 0.21 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 43 | Apaporis | 53359.39 | 2615.79 | 12581 | 42687.56 | 3.19 | 0.8 | 0.24 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 99768.59 | 3755.68 | 32157 | 93819.82 | 3.35 | 0.94 | 0.32 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 45 | Yarí | 36591.94 | 1621.95 | 10793 | 33205.62 | 2.39 | 0.91 | 0.29 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 46 | Caguán | 21207.97 | 1279.19 | 8737 | 21303.05 | 2.48 | 1.0 | 0.41 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 57822.73 | 3855.06 | 15800 | 48839.68 | 4.52 | 0.84 | 0.27 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 48 | Amazonas - Directos | 3256.52 | 375.27 | 698 | 2444.36 | 1.86 | 0.75 | 0.21 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 49 | Napo | 456.15 | 159.57 | 191 | 430.64 | 2.11 | 0.94 | 0.42 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 51 | Mira | 5874.67 | 679.52 | 2357 | 4443.78 | 2.5 | 0.76 | 0.4 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 52 | Patía | 24029.6 | 1236.12 | 10183 | 23227.29 | 2.25 | 0.97 | 0.42 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 20848.95 | 1088.56 | 8732 | 20179.07 | 2.13 | 0.97 | 0.42 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 54 | San Juán | 16393.56 | 946.72 | 8156 | 20697.74 | 2.09 | 1.26 | 0.5 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 55 | Baudó - Directos Pacifico | 5968.79 | 719.69 | 3277 | 7614.21 | 2.63 | 1.28 | 0.55 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 56 | Pacífico - Directos | 4256.46 | 1031.69 | 2419 | 5447.84 | 4.46 | 1.28 | 0.57 | Oval-oblonga a rectangular-oblonga |

### SZH - Subzona hidrográfica

D:/R.GISPython/HydroGeoZone/Output/SubZonaHidrograficaEstadistica.dbf

| AH | Nombre AH | ZH | Nombre ZH | SZH | Nombre SZH | Área, km² | Perm, km | n Drenajes | Sum. LCi, km | Kc | Dd | Dc | Kc Tag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Caribe | 11 | Atrato - Darién | 1101 | Río Andágueda | 901.97 | 214.5 | 410 | 1020.98 | 2.01 | 1.13 | 0.45 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1102 | Alto Atrato | 1668.11 | 242.54 | 583 | 1732.97 | 1.68 | 1.04 | 0.35 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1103 | Río Quito | 1817.46 | 310.67 | 862 | 2161.13 | 2.06 | 1.19 | 0.47 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1104 | Río Bebaramá y otros Directos Atrato (md) | 2599.28 | 259.65 | 830 | 2715.14 | 1.44 | 1.04 | 0.32 | Oval-redonda a oval oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1105 | Directos Atrato entre ríos Quito y Bojayá (mi) | 3095.85 | 376.54 | 1633 | 4031.18 | 1.91 | 1.3 | 0.53 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1106 | Directos Atrato entre ríos Bebaramá y Murrí (md) | 1605.86 | 277.03 | 549 | 1820.55 | 1.95 | 1.13 | 0.34 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1107 | Río Murrí | 3472.61 | 401.88 | 1327 | 3741.37 | 1.92 | 1.08 | 0.38 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1108 | Río Bojayá | 1821.28 | 280.75 | 982 | 2375.23 | 1.86 | 1.3 | 0.54 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1109 | Río Napipí - Río Opogadó | 1120.47 | 205.04 | 485 | 1361.28 | 1.73 | 1.21 | 0.43 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1110 | Río Murindó - Directos al Atrato | 2656.99 | 292.61 | 569 | 2038.36 | 1.6 | 0.77 | 0.21 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1111 | Río Sucio | 5377.12 | 577.2 | 1705 | 5185.55 | 2.22 | 0.96 | 0.32 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1112 | Río Salaquí  y otros directos Bajo Atrato | 5849.07 | 489.76 | 1970 | 5921.61 | 1.81 | 1.01 | 0.34 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1113 | Río Cacarica | 1158.56 | 164.07 | 254 | 960.9 | 1.36 | 0.83 | 0.22 | Oval-redonda a oval oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1114 | Directos Bajo Atrato entre río Sucio y desembocadura | 2057.02 | 392.81 | 283 | 972.1 | 2.44 | 0.47 | 0.14 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1115 | Río Tanela y otros Directos al Caribe | 1452.44 | 247.87 | 528 | 1541.37 | 1.83 | 1.06 | 0.36 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1116 | Río Tolo y otros Directos al Caribe | 714.92 | 194.43 | 378 | 868.47 | 2.05 | 1.21 | 0.53 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1117 | Río Cabi y otros Directos Atrato (md) | 467.99 | 122.05 | 267 | 602.73 | 1.59 | 1.29 | 0.57 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 12 | Caribe - Litoral | 1201 | Río León | 2279.19 | 252.78 | 735 | 2475.74 | 1.49 | 1.09 | 0.32 | Oval-redonda a oval oblonga |
| 1 | Caribe | 12 | Caribe - Litoral | 1202 | Río Mulatos y otros directos al Caribe | 2981.99 | 341.32 | 1001 | 3450.35 | 1.76 | 1.16 | 0.34 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 12 | Caribe - Litoral | 1203 | Río San Juan | 1444.54 | 258.03 | 305 | 1172.48 | 1.92 | 0.81 | 0.21 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 12 | Caribe - Litoral | 1204 | Rio Canalete y otros Arroyos Directos al Caribe | 1898.25 | 285.98 | 578 | 1797.0 | 1.85 | 0.95 | 0.3 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 12 | Caribe - Litoral | 1205 | Directos Caribe Golfo de Morrosquillo | 2504.61 | 316.25 | 821 | 2614.71 | 1.78 | 1.04 | 0.33 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 12 | Caribe - Litoral | 1206 | Arroyos Directos al Caribe | 1867.32 | 326.99 | 904 | 2355.08 | 2.13 | 1.26 | 0.48 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 13 | Sinú | 1301 | Alto Sinú - Urrá | 4596.16 | 382.36 | 1260 | 3849.95 | 1.59 | 0.84 | 0.27 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 13 | Sinú | 1302 | Medio Sinú | 3926.58 | 365.31 | 705 | 2850.67 | 1.64 | 0.73 | 0.18 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 13 | Sinú | 1303 | Bajo Sinú | 5578.79 | 507.07 | 1201 | 4144.65 | 1.92 | 0.74 | 0.22 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1501 | Río  Piedras - Río Manzanares | 928.48 | 187.87 | 588 | 1222.89 | 1.74 | 1.32 | 0.63 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1502 | Río Don Diego | 541.15 | 135.0 | 356 | 785.61 | 1.64 | 1.45 | 0.66 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1503 | Río Ancho y Otros Directos al caribe | 1952.39 | 206.67 | 1208 | 2614.82 | 1.32 | 1.34 | 0.62 | Oval-redonda a oval oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1504 | Río Tapias | 1076.53 | 162.59 | 571 | 1377.39 | 1.4 | 1.28 | 0.53 | Oval-redonda a oval oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1505 | Río Camarones y otros directos Caribe | 892.74 | 183.4 | 275 | 871.43 | 1.73 | 0.98 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1506 | Río Ranchería | 4276.8 | 427.77 | 1558 | 4590.35 | 1.85 | 1.07 | 0.36 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1507 | Directos Caribe - Ay.Sharimahana Alta Guajira | 5374.02 | 634.64 | 1695 | 5514.55 | 2.44 | 1.03 | 0.32 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1508 | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | 5646.16 | 607.86 | 1577 | 5559.94 | 2.28 | 0.98 | 0.28 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1509 | Rio Guachaca - Mendiguaca y Buritaca | 683.63 | 124.89 | 482 | 933.0 | 1.35 | 1.36 | 0.71 | Oval-redonda a oval oblonga |
| 1 | Caribe | 16 | Catatumbo | 1601 | Río Pamplonita | 1402.87 | 372.15 | 812 | 1781.65 | 2.8 | 1.27 | 0.58 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 16 | Catatumbo | 1602 | Río Zulia | 3420.53 | 421.91 | 2031 | 4487.43 | 2.04 | 1.31 | 0.59 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 16 | Catatumbo | 1603 | Río Nuevo Presidente - Tres Bocas (Sardinata, Tibu) | 3434.34 | 334.15 | 2506 | 4898.81 | 1.61 | 1.43 | 0.73 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 16 | Catatumbo | 1604 | Río Tarra | 1760.13 | 278.18 | 1373 | 2583.08 | 1.87 | 1.47 | 0.78 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 16 | Catatumbo | 1605 | Río Algodonal (Alto Catatumbo) | 2336.05 | 340.94 | 1647 | 3476.41 | 1.99 | 1.49 | 0.71 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 16 | Catatumbo | 1606 | Río Socuavo del Norte y Río Socuavo Sur | 964.18 | 159.61 | 119 | 603.65 | 1.45 | 0.63 | 0.12 | Oval-redonda a oval oblonga |
| 1 | Caribe | 16 | Catatumbo | 1607 | Bajo Catatumbo | 1247.6 | 252.46 | 401 | 1145.79 | 2.02 | 0.92 | 0.32 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 16 | Catatumbo | 1608 | Río del Suroeste y directos Río de Oro | 1873.75 | 312.68 | 790 | 1971.33 | 2.04 | 1.05 | 0.42 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 17 | Islas Caribe | 1701 | San Andres | 27.4 | 39.75 | 1 | 0.78 | 2.14 | 0.03 | 0.04 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 17 | Islas Caribe | 1702 | Providencia | 22.49 | 32.55 | 4 | 10.18 | 1.94 | 0.45 | 0.18 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 17 | Islas Caribe | 1703 | Roncador y Quitasueño | 27.41 | 37.57 | 0 | 0.0 | 2.02 | 0.0 | 0.0 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2101 | Alto Magdalena | 2507.03 | 319.8 | 1352 | 3429.09 | 1.8 | 1.37 | 0.54 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2102 | Río Timaná y otros directos al Magdalena | 382.26 | 146.1 | 144 | 385.24 | 2.11 | 1.01 | 0.38 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2103 | Río Suaza | 1422.26 | 238.82 | 728 | 1757.18 | 1.79 | 1.24 | 0.51 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2104 | Ríos Directos al Magdalena (mi) | 1543.87 | 320.1 | 497 | 1464.96 | 2.3 | 0.95 | 0.32 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2105 | Río Páez | 5203.62 | 434.89 | 2825 | 6288.3 | 1.7 | 1.21 | 0.54 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2106 | Ríos directos Magdalena (md) | 1149.7 | 246.05 | 872 | 1608.12 | 2.05 | 1.4 | 0.76 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2108 | Río Yaguará y Río Iquira | 937.19 | 160.0 | 503 | 1083.71 | 1.47 | 1.16 | 0.54 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2109 | Juncal y otros Rios directos al Magdalena | 451.67 | 150.62 | 387 | 650.45 | 2.0 | 1.44 | 0.86 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2110 | Rio Neiva | 1070.3 | 176.09 | 1064 | 1936.87 | 1.52 | 1.81 | 0.99 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2111 | Rio Fortalecillas y otros | 2158.1 | 268.06 | 1858 | 3276.7 | 1.63 | 1.52 | 0.86 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2112 | Río Baché | 1168.15 | 205.31 | 744 | 1496.39 | 1.69 | 1.28 | 0.64 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2113 | Río Aipe, Río Chenche y otros directos al Magdalena | 2605.73 | 399.1 | 1322 | 2923.0 | 2.21 | 1.12 | 0.51 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2114 | Río Cabrera | 2804.02 | 355.14 | 1788 | 3707.31 | 1.89 | 1.32 | 0.64 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2115 | Directos Magdalena entre ríos Cabrera y Sumapaz | 1035.29 | 294.4 | 593 | 1282.62 | 2.58 | 1.24 | 0.57 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2116 | Río Prado | 1674.75 | 207.0 | 862 | 2134.97 | 1.43 | 1.27 | 0.51 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2118 | Río Luisa y otros directos al Magdalena | 1075.5 | 227.81 | 509 | 1380.92 | 1.96 | 1.28 | 0.47 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2119 | Río Sumapaz | 3045.26 | 352.88 | 1206 | 3411.17 | 1.8 | 1.12 | 0.4 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2120 | Río Bogotá | 5925.89 | 581.65 | 2396 | 6362.44 | 2.13 | 1.07 | 0.4 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2121 | Río Coello | 1831.15 | 285.94 | 1390 | 2970.78 | 1.89 | 1.62 | 0.76 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2122 | Río Opía | 552.76 | 153.34 | 108 | 529.95 | 1.84 | 0.96 | 0.2 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2123 | Río Seco y otros Directos al Magdalena | 1771.39 | 346.21 | 829 | 2134.23 | 2.32 | 1.2 | 0.47 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2124 | Río Totare | 1436.31 | 203.79 | 633 | 1735.02 | 1.52 | 1.21 | 0.44 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2125 | Río Lagunilla y Otros Directos al Magdalena | 2751.75 | 272.46 | 1382 | 3908.06 | 1.47 | 1.42 | 0.5 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 22 | Saldaña | 2201 | Alto Saldaña | 2583.74 | 267.84 | 1660 | 3503.69 | 1.49 | 1.36 | 0.64 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 22 | Saldaña | 2202 | Río Atá | 1534.98 | 247.22 | 870 | 1954.49 | 1.78 | 1.27 | 0.57 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 22 | Saldaña | 2203 | Medio Saldaña | 604.01 | 161.92 | 458 | 869.99 | 1.86 | 1.44 | 0.76 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 22 | Saldaña | 2204 | Río Amoyá | 1462.36 | 233.18 | 1081 | 2148.82 | 1.72 | 1.47 | 0.74 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 22 | Saldaña | 2206 | Río Tetuán, Río Ortega | 1204.44 | 183.87 | 1357 | 2182.59 | 1.49 | 1.81 | 1.13 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 22 | Saldaña | 2207 | Rïo Cucuana | 1865.74 | 261.08 | 1901 | 3276.16 | 1.71 | 1.76 | 1.02 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 22 | Saldaña | 2208 | Bajo Saldaña | 705.73 | 232.02 | 447 | 930.87 | 2.46 | 1.32 | 0.63 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2301 | Río Gualí | 875.8 | 219.88 | 531 | 1302.38 | 2.1 | 1.49 | 0.61 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2302 | Río Guarinó | 843.39 | 234.13 | 545 | 1248.2 | 2.27 | 1.48 | 0.65 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2303 | Directos al Magdalena entre Ríos Seco y Negro (md) | 434.39 | 153.13 | 272 | 570.36 | 2.07 | 1.31 | 0.63 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2304 | Directos Magdalena entre Ríos Guarinó y La Miel | 965.1 | 169.23 | 767 | 1771.98 | 1.54 | 1.84 | 0.79 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2305 | Río La Miel (Samaná) | 2398.89 | 264.82 | 1842 | 3829.8 | 1.53 | 1.6 | 0.77 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2306 | Río Negro | 4567.37 | 438.65 | 3027 | 5631.62 | 1.83 | 1.23 | 0.66 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2307 | Directos Magdalena Medio entre ríos La Miel y Nare | 1483.27 | 244.57 | 415 | 1446.11 | 1.79 | 0.97 | 0.28 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2308 | Río Nare | 5596.74 | 458.68 | 4432 | 7589.83 | 1.73 | 1.36 | 0.79 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2310 | Rió San Bartolo y otros directos al Magdalena Medio | 3592.46 | 350.67 | 1912 | 4083.5 | 1.65 | 1.14 | 0.53 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2311 | Directos al Magdalena Medio entre ríos Negro | 2681.99 | 359.54 | 1162 | 3070.69 | 1.96 | 1.14 | 0.43 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2312 | Río Carare (Minero) | 7273.39 | 544.29 | 3474 | 8252.58 | 1.8 | 1.13 | 0.48 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2314 | Río Opón | 4312.06 | 424.24 | 1536 | 4101.77 | 1.82 | 0.95 | 0.36 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2317 | Río Cimitarra y otros directos al Magdalena | 4966.83 | 433.82 | 1220 | 3214.65 | 1.74 | 0.65 | 0.25 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2319 | Río Lebrija y otros directos al Magdalena | 9575.1 | 560.16 | 5088 | 12458.3 | 1.61 | 1.3 | 0.53 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2320 | Directos al Magdalena (Brazo Morales) | 7092.22 | 482.2 | 4106 | 8563.25 | 1.62 | 1.21 | 0.58 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2321 | Quebrada El Carmen y Otros Directos al Magdalena | 2969.27 | 282.24 | 1865 | 4432.76 | 1.46 | 1.49 | 0.63 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 24 | Sogamoso | 2401 | Río Suárez | 7843.08 | 599.68 | 4078 | 9802.22 | 1.91 | 1.25 | 0.52 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 24 | Sogamoso | 2402 | Río Fonce | 2406.2 | 273.42 | 1342 | 2953.96 | 1.57 | 1.23 | 0.56 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 24 | Sogamoso | 2403 | Río Chicamocha | 9554.3 | 719.31 | 5425 | 11654.85 | 2.08 | 1.22 | 0.57 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 24 | Sogamoso | 2405 | Río Sogamoso | 3402.85 | 367.12 | 1547 | 3655.83 | 1.78 | 1.07 | 0.45 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 25 | Bajo Magdalena- Cauca -San Jorge | 2501 | Alto San Jorge | 3960.43 | 396.1 | 1218 | 3572.98 | 1.78 | 0.9 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 25 | Bajo Magdalena- Cauca -San Jorge | 2502 | Bajo San Jorge - La Mojana | 17181.78 | 779.56 | 4278 | 14254.12 | 1.68 | 0.83 | 0.25 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2601 | Alto Río Cauca | 854.62 | 187.35 | 261 | 839.96 | 1.81 | 0.98 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2602 | Río Palacé | 934.6 | 189.91 | 545 | 1292.61 | 1.75 | 1.38 | 0.58 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2603 | Rio Salado y otros directos Cauca | 1247.99 | 261.83 | 883 | 1562.85 | 2.09 | 1.25 | 0.71 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2604 | Río Palo | 1651.31 | 234.67 | 1327 | 2425.1 | 1.63 | 1.47 | 0.8 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2605 | Río Timba | 485.14 | 125.66 | 323 | 681.04 | 1.61 | 1.4 | 0.67 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2606 | Río Ovejas | 924.28 | 155.18 | 637 | 1493.31 | 1.44 | 1.62 | 0.69 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2607 | Río Guachal (Bolo - Fraile y Párraga) | 1186.31 | 185.58 | 358 | 1094.17 | 1.52 | 0.92 | 0.3 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2608 | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | 1288.7 | 313.98 | 516 | 1375.36 | 2.47 | 1.07 | 0.4 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2609 | Ríos Amaime y Cerrito | 1124.62 | 189.54 | 432 | 1269.5 | 1.59 | 1.13 | 0.38 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2610 | Ríos Tulua y Morales | 1078.41 | 179.44 | 562 | 1377.42 | 1.54 | 1.28 | 0.52 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2611 | Río Frío | 476.3 | 124.47 | 162 | 491.39 | 1.61 | 1.03 | 0.34 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2612 | Río La Vieja | 2836.45 | 303.82 | 1672 | 4590.07 | 1.61 | 1.62 | 0.59 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2613 | Río Otún y otros directos al Cauca | 1220.72 | 226.26 | 585 | 1648.57 | 1.83 | 1.35 | 0.48 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2614 | Río Risaralda | 1259.39 | 231.16 | 697 | 1889.28 | 1.84 | 1.5 | 0.55 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2615 | Río Chinchiná | 1054.24 | 177.36 | 551 | 1466.09 | 1.54 | 1.39 | 0.52 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2616 | Rio Tapias y otros directos al Cauca | 1404.02 | 226.68 | 1417 | 2503.89 | 1.71 | 1.78 | 1.01 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2617 | Río Frío y Otros Directos al Cauca | 1638.21 | 338.8 | 799 | 2150.88 | 2.36 | 1.31 | 0.49 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2618 | Río Arma | 1860.27 | 261.43 | 1367 | 2797.17 | 1.71 | 1.5 | 0.73 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2619 | Río San Juan | 1416.12 | 217.9 | 724 | 1843.55 | 1.63 | 1.3 | 0.51 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2620 | Directos Río Cauca  entre Río San Juan y  Pto Valdivia | 3552.96 | 503.22 | 2404 | 4602.56 | 2.38 | 1.3 | 0.68 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2621 | Directos Río Cauca entre Río San Juan y Pto Valdia | 3413.51 | 524.35 | 2217 | 4404.63 | 2.53 | 1.29 | 0.65 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2622 | Río Desbaratado | 191.48 | 113.15 | 70 | 197.4 | 2.31 | 1.03 | 0.37 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2624 | Río Taraza - Río Man | 2578.59 | 346.4 | 885 | 2346.37 | 1.92 | 0.91 | 0.34 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2625 | Directos al Cauca entre Pto Valdivia y Río Nechí | 1436.42 | 405.47 | 846 | 1569.53 | 3.02 | 1.09 | 0.59 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2626 | Directos Bajo Cauca - Cga La Raya entre río Nechí | 4343.67 | 459.57 | 2163 | 4180.79 | 1.97 | 0.96 | 0.5 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2627 | Río Piendamo | 601.69 | 208.32 | 467 | 917.32 | 2.4 | 1.52 | 0.78 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2628 | Río Quinamayo y otros directos al Cauca | 810.98 | 174.12 | 472 | 1353.56 | 1.72 | 1.67 | 0.58 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2629 | Ríos Claro y Jamundí | 668.82 | 152.62 | 169 | 553.02 | 1.66 | 0.83 | 0.25 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2630 | Ríos Lilí, Melendez y Canaveralejo | 193.06 | 70.25 | 32 | 93.69 | 1.43 | 0.49 | 0.17 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2631 | Rios Arroyohondo - Yumbo - Mulalo - Vijes - Yotoco | 631.27 | 234.4 | 265 | 658.2 | 2.63 | 1.04 | 0.42 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2632 | Ríos Guabas,Sabaletas y Sonso | 556.67 | 114.0 | 179 | 604.49 | 1.36 | 1.09 | 0.32 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2633 | Ríos Guadalajara y San Pedro | 463.3 | 148.76 | 125 | 404.88 | 1.95 | 0.87 | 0.27 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2634 | Ríos Cali | 212.46 | 81.26 | 45 | 147.69 | 1.57 | 0.7 | 0.21 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2635 | Río Bugalagrande | 834.94 | 210.88 | 536 | 1135.96 | 2.06 | 1.36 | 0.64 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2636 | Río Paila | 525.76 | 109.02 | 239 | 645.88 | 1.34 | 1.23 | 0.45 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2637 | Rios Las Cañas - Los Micos y Obando | 782.38 | 187.43 | 261 | 699.22 | 1.89 | 0.89 | 0.33 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 27 | Nechí | 2701 | Río Porce | 5228.39 | 639.38 | 4206 | 7586.11 | 2.49 | 1.45 | 0.8 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 27 | Nechí | 2702 | Alto Nechí | 2936.92 | 340.29 | 2771 | 3997.73 | 1.77 | 1.36 | 0.94 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 27 | Nechí | 2703 | Bajo Nechí (md) | 4487.76 | 409.48 | 1432 | 3744.25 | 1.72 | 0.83 | 0.32 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 27 | Nechí | 2704 | Directos al Bajo Nechí (mi) | 1950.66 | 263.85 | 606 | 1696.53 | 1.69 | 0.87 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 28 | Cesar | 2801 | Alto Cesar | 3435.73 | 294.28 | 2625 | 5754.67 | 1.42 | 1.67 | 0.76 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 28 | Cesar | 2802 | Medio Cesar | 8260.98 | 459.97 | 2752 | 8256.57 | 1.43 | 1.0 | 0.33 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 28 | Cesar | 2804 | Río Ariguaní | 5325.51 | 428.45 | 1745 | 5650.34 | 1.66 | 1.06 | 0.33 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 28 | Cesar | 2805 | Bajo Cesar | 5869.81 | 391.02 | 2033 | 5779.91 | 1.44 | 0.98 | 0.35 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2901 | Directos al Bajo Magdalena entre El Plato y Calamar | 2010.94 | 231.53 | 850 | 2485.3 | 1.46 | 1.24 | 0.42 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2902 | Directos al Bajo Magdalena entre El Plato y Calamar | 2473.59 | 304.6 | 853 | 2596.2 | 1.73 | 1.05 | 0.34 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2903 | Canal del Dique margen derecho | 2103.34 | 312.05 | 656 | 2046.38 | 1.92 | 0.97 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2904 | Directos al Bajo Magdalena entre Calamar y desembocadura | 1151.53 | 215.04 | 278 | 914.23 | 1.79 | 0.79 | 0.24 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2905 | Canal del Dique margen izquierda | 2299.23 | 393.21 | 722 | 2008.96 | 2.31 | 0.87 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2906 | Cga Grande de Santa Marta | 8219.98 | 529.41 | 2713 | 7182.44 | 1.65 | 0.87 | 0.33 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2907 | Directos Bajo Magdalena entre El Banco y El Plato | 6998.88 | 568.62 | 1848 | 5324.61 | 1.92 | 0.76 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2908 | Ríos Chimicuica y Corozal | 3692.2 | 284.91 | 1070 | 3708.04 | 1.32 | 1.0 | 0.29 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2909 | Cienaga Mallorquin | 262.04 | 89.87 | 80 | 233.07 | 1.57 | 0.89 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 31 | Inírida | 3101 | Río Inírida Alto | 11752.53 | 654.03 | 2609 | 9654.83 | 1.7 | 0.82 | 0.22 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 31 | Inírida | 3104 | Río Inírida Medio | 18344.68 | 1250.21 | 7913 | 18306.77 | 2.6 | 1.0 | 0.43 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 31 | Inírida | 3105 | Río Papunaya | 6830.93 | 610.59 | 1459 | 5297.99 | 2.08 | 0.78 | 0.21 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 31 | Inírida | 3107 | Caño Nabuquén | 1728.93 | 288.14 | 1159 | 2276.91 | 1.95 | 1.32 | 0.67 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 31 | Inírida | 3108 | R._Inírida_(mi),_hasta_bocas_Caño_Bocón,_y_R._Las Viñas | 7983.66 | 902.09 | 4820 | 8811.12 | 2.85 | 1.1 | 0.6 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 31 | Inírida | 3110 | Caño Bocón | 6951.02 | 562.33 | 2980 | 6038.81 | 1.9 | 0.87 | 0.43 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3201 | Río Guayabero | 6264.86 | 555.18 | 3216 | 7015.84 | 1.98 | 1.12 | 0.51 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3202 | Río Guape | 3837.91 | 471.18 | 1553 | 3981.23 | 2.15 | 1.04 | 0.4 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3203 | Rio Losada | 3654.06 | 357.86 | 954 | 3175.2 | 1.67 | 0.87 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3204 | Alto Guaviare | 10351.53 | 599.86 | 2820 | 8668.36 | 1.66 | 0.84 | 0.27 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3206 | Río Ariari | 8069.11 | 673.73 | 3192 | 8212.24 | 2.12 | 1.02 | 0.4 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3207 | Río Guejar | 3291.47 | 386.5 | 693 | 2768.45 | 1.9 | 0.84 | 0.21 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3210 | Medio Guaviare | 13738.92 | 982.43 | 5038 | 11191.95 | 2.36 | 0.81 | 0.37 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3212 | Río Siare | 4433.73 | 581.29 | 2386 | 5426.39 | 2.46 | 1.22 | 0.54 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3213 | Río Iteviare | 4854.11 | 651.48 | 2363 | 5207.02 | 2.64 | 1.07 | 0.49 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3214 | Bajo Guaviare | 8872.89 | 1011.66 | 1296 | 4389.32 | 3.03 | 0.49 | 0.15 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3215 | Caño Minisiare | 2336.11 | 359.37 | 1808 | 3161.22 | 2.1 | 1.35 | 0.77 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3216 | Alto Río Uvá | 4422.98 | 395.89 | 1833 | 4643.63 | 1.68 | 1.05 | 0.41 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3217 | Bajo Río Uvá | 5403.34 | 494.36 | 1429 | 4521.89 | 1.9 | 0.84 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3218 | Caño Chupabe | 4817.24 | 625.02 | 767 | 2802.76 | 2.54 | 0.58 | 0.16 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 33 | Vichada | 3301 | Alto Vichada | 8049.09 | 524.47 | 6595 | 11362.17 | 1.65 | 1.41 | 0.82 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 33 | Vichada | 3302 | Río Guarrojo | 3646.74 | 484.86 | 2934 | 4458.82 | 2.26 | 1.22 | 0.8 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 33 | Vichada | 3303 | Río Muco | 4448.89 | 518.52 | 2643 | 4052.78 | 2.19 | 0.91 | 0.59 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 33 | Vichada | 3305 | Directos Vichada Medio | 4985.17 | 461.11 | 1846 | 3858.92 | 1.84 | 0.77 | 0.37 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 33 | Vichada | 3306 | Bajo Vichada | 4989.02 | 502.98 | 1925 | 4307.42 | 2.01 | 0.86 | 0.39 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 34 | Tomo | 3401 | Alto Río Tomo | 8023.92 | 642.65 | 3283 | 6620.73 | 2.02 | 0.83 | 0.41 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 34 | Tomo | 3402 | Río Elvita | 5554.77 | 507.91 | 1990 | 4069.19 | 1.92 | 0.73 | 0.36 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 34 | Tomo | 3403 | Bajo Río Tomo | 4080.21 | 635.41 | 1436 | 2995.64 | 2.81 | 0.73 | 0.35 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 34 | Tomo | 3405 | Caño Lioni o Terecay | 2554.4 | 447.49 | 1148 | 2293.34 | 2.5 | 0.9 | 0.45 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3501 | Rio Metica (Guamal - Humadea) | 3838.4 | 333.4 | 1404 | 4401.4 | 1.52 | 1.15 | 0.37 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3502 | Río Guayuriba | 3194.71 | 470.05 | 1413 | 3402.91 | 2.35 | 1.07 | 0.44 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3503 | Río Guatiquía | 1777.88 | 320.92 | 584 | 1881.12 | 2.15 | 1.06 | 0.33 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3504 | Río Guacavía | 848.92 | 158.1 | 183 | 716.79 | 1.53 | 0.84 | 0.22 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3505 | Río Humea | 1438.04 | 285.2 | 384 | 1090.0 | 2.12 | 0.76 | 0.27 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3506 | Río Guavio | 2285.13 | 307.65 | 1890 | 3354.73 | 1.82 | 1.47 | 0.83 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3507 | Río Garagoa | 2483.0 | 312.64 | 1226 | 2845.02 | 1.77 | 1.15 | 0.49 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3508 | Río Lengupá | 1875.21 | 245.24 | 1040 | 2186.42 | 1.6 | 1.17 | 0.55 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3509 | Río Upía | 1821.86 | 373.47 | 756 | 1794.95 | 2.47 | 0.99 | 0.41 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3510 | Río Negro | 925.75 | 203.36 | 157 | 1019.43 | 1.89 | 1.1 | 0.17 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3511 | Directos Rio Metica entre ríos Guayuriba y Yucao | 1964.36 | 456.75 | 766 | 1769.64 | 2.91 | 0.9 | 0.39 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3512 | Río Yucao | 2435.19 | 288.91 | 1395 | 2595.86 | 1.65 | 1.07 | 0.57 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3513 | Río Melúa | 1880.31 | 266.96 | 1047 | 2344.51 | 1.74 | 1.25 | 0.56 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3514 | Caño Cumaral | 1110.74 | 228.96 | 600 | 1417.38 | 1.94 | 1.28 | 0.54 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3515 | Río Manacacias | 6969.94 | 831.28 | 4478 | 9099.4 | 2.81 | 1.31 | 0.64 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3516 | Lago de Tota | 225.16 | 86.7 | 120 | 229.76 | 1.63 | 1.02 | 0.53 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3518 | Río Túa y otros directos al Meta | 4963.06 | 402.82 | 1086 | 3676.99 | 1.61 | 0.74 | 0.22 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3519 | Río Cusiana | 5089.28 | 456.32 | 1580 | 4519.56 | 1.8 | 0.89 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3520 | Directos al Meta entre ríos Cusiana y Cravo Sur | 1660.34 | 239.73 | 153 | 908.44 | 1.66 | 0.55 | 0.09 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3521 | Río Cravo Sur | 5148.16 | 502.04 | 1532 | 4470.54 | 1.97 | 0.87 | 0.3 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3522 | Caño Guanápalo y otros directos al Meta | 6225.95 | 411.43 | 539 | 3922.83 | 1.47 | 0.63 | 0.09 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 35 | Meta | 3523 | Río Pauto | 7998.7 | 610.07 | 1030 | 6117.96 | 1.92 | 0.76 | 0.13 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3524 | Directos al Río Meta entre ríos Pauto y Carare | 5347.05 | 489.78 | 419 | 3209.2 | 1.89 | 0.6 | 0.08 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3525 | Directos Bajo Meta entre ríos Casanare y Orinoco | 6323.0 | 777.79 | 1618 | 3634.07 | 2.76 | 0.57 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3526 | Directos al Río Meta entre ríos Cusiana y Carare | 3434.83 | 680.38 | 383 | 1607.95 | 3.27 | 0.47 | 0.11 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3527 | Directos al Río Meta entre ríos Humea y Upia (mi) | 1241.07 | 188.44 | 314 | 1057.58 | 1.51 | 0.85 | 0.25 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 36 | Casanare | 3601 | Río Ariporo | 5268.11 | 619.92 | 631 | 3307.62 | 2.41 | 0.63 | 0.12 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 36 | Casanare | 3602 | Río Casanare | 6645.61 | 754.81 | 1195 | 4329.99 | 2.61 | 0.65 | 0.18 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 36 | Casanare | 3603 | Río Cravo Norte | 8876.2 | 522.09 | 879 | 5621.19 | 1.56 | 0.63 | 0.1 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 36 | Casanare | 3604 | Caño Samuco | 915.68 | 188.82 | 58 | 478.5 | 1.76 | 0.52 | 0.06 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 36 | Casanare | 3605 | Caño Aguaclarita | 2471.05 | 249.25 | 140 | 1071.07 | 1.41 | 0.43 | 0.06 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 37 | Arauca | 3701 | Río Chítaga | 2483.57 | 334.98 | 1099 | 2572.93 | 1.9 | 1.04 | 0.44 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 37 | Arauca | 3702 | Río Margua | 744.48 | 146.11 | 267 | 685.23 | 1.51 | 0.92 | 0.36 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 37 | Arauca | 3703 | Río Cobugón - Río Cobaría | 1974.35 | 203.74 | 683 | 1775.78 | 1.29 | 0.9 | 0.35 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 37 | Arauca | 3704 | Río Bojabá | 1130.39 | 215.18 | 402 | 979.61 | 1.81 | 0.87 | 0.36 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 37 | Arauca | 3705 | Rio Banadia y otros Directos al Río Arauca | 2097.01 | 294.04 | 287 | 1272.45 | 1.81 | 0.61 | 0.14 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 37 | Arauca | 3706 | Directos Río Arauca (md) | 2918.92 | 352.38 | 206 | 1890.95 | 1.84 | 0.65 | 0.07 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 38 | Orinoco Directos | 3801 | Río Vita | 8207.17 | 962.81 | 3982 | 6390.91 | 3.0 | 0.78 | 0.49 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 38 | Orinoco Directos | 3802 | Río Tuparro | 11505.4 | 813.17 | 6368 | 11782.29 | 2.14 | 1.02 | 0.55 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 38 | Orinoco Directos | 3803 | Caño Matavén | 10461.36 | 684.71 | 2225 | 7135.35 | 1.89 | 0.68 | 0.21 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 38 | Orinoco Directos | 3804 | Directos Río Atabapo (mi) | 4617.54 | 447.6 | 2272 | 4853.28 | 1.86 | 1.05 | 0.49 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 38 | Orinoco Directos | 3805 | Directos Orinoco entre ríos Tomo y Meta (mi) | 4171.25 | 439.65 | 1164 | 2454.53 | 1.92 | 0.59 | 0.28 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 38 | Orinoco Directos | 3809 | Río Cinaruco y Directos Río Orinoco | 4551.36 | 466.37 | 325 | 2078.64 | 1.95 | 0.46 | 0.07 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 39 | Apure | 3901 | Alto Río Apure | 263.63 | 106.78 | 90 | 240.7 | 1.86 | 0.91 | 0.34 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 41 | Guanía | 4101 | Alto Rio Guanía | 3692.65 | 422.29 | 1617 | 3876.29 | 1.96 | 1.05 | 0.44 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 41 | Guanía | 4102 | Medio Rio Guanía | 2773.34 | 379.32 | 1698 | 3185.69 | 2.03 | 1.15 | 0.61 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 41 | Guanía | 4105 | Bajo Rio Guanía | 7911.65 | 838.55 | 3286 | 7441.47 | 2.66 | 0.94 | 0.42 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 41 | Guanía | 4106 | Río Aquió o Caño Aque | 2978.85 | 307.37 | 656 | 2166.78 | 1.59 | 0.73 | 0.22 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 41 | Guanía | 4107 | Directos Río Negro (md) | 3519.66 | 473.45 | 1951 | 3773.35 | 2.25 | 1.07 | 0.55 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 41 | Guanía | 4108 | Río Cuiary | 4387.85 | 594.84 | 1963 | 4526.71 | 2.53 | 1.03 | 0.45 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 41 | Guanía | 4109 | Río Isana | 3444.02 | 579.6 | 1152 | 3209.57 | 2.79 | 0.93 | 0.33 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 41 | Guanía | 4110 | Río Tomo | 2422.3 | 256.7 | 529 | 1699.51 | 1.47 | 0.7 | 0.22 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 42 | Vaupes | 4201 | Río Itilla | 2565.38 | 391.07 | 620 | 2233.21 | 2.18 | 0.87 | 0.24 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 42 | Vaupes | 4202 | Río Unilla | 2303.8 | 353.11 | 447 | 1809.76 | 2.08 | 0.79 | 0.19 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 42 | Vaupes | 4203 | Alto Vaupés | 8615.07 | 675.79 | 1749 | 6131.41 | 2.05 | 0.71 | 0.2 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 42 | Vaupes | 4207 | Bajo Vaupés | 13402.76 | 1072.82 | 2743 | 8526.08 | 2.61 | 0.64 | 0.2 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 42 | Vaupes | 4208 | Río Querary | 4275.8 | 582.99 | 857 | 2689.79 | 2.52 | 0.63 | 0.2 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 42 | Vaupes | 4209 | Río Papurí | 5387.41 | 667.63 | 1101 | 3617.82 | 2.57 | 0.67 | 0.2 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 42 | Vaupes | 4211 | Río Tiquié | 1020.71 | 186.81 | 246 | 820.81 | 1.65 | 0.8 | 0.24 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 43 | Apaporis | 4301 | Río Tunia ó Macayá | 9253.02 | 849.66 | 2012 | 7260.7 | 2.49 | 0.78 | 0.22 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 43 | Apaporis | 4302 | Río Ajaju | 7817.77 | 606.53 | 2458 | 7606.92 | 1.94 | 0.97 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 43 | Apaporis | 4303 | Alto Río Apaporis | 12319.61 | 950.36 | 2814 | 9432.56 | 2.42 | 0.77 | 0.23 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 43 | Apaporis | 4305 | Bajo Río Apaporis | 12739.33 | 991.16 | 2518 | 9084.08 | 2.48 | 0.71 | 0.2 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 43 | Apaporis | 4306 | Río Cananari | 3839.19 | 419.52 | 931 | 3072.4 | 1.91 | 0.8 | 0.24 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 43 | Apaporis | 4307 | Río Pira Paraná | 5843.84 | 606.97 | 1556 | 5034.04 | 2.24 | 0.86 | 0.27 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 43 | Apaporis | 4309 | Directos Río Taraira | 1546.64 | 423.39 | 292 | 1196.87 | 3.04 | 0.77 | 0.19 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4401 | Alto Caqueta | 5813.76 | 448.5 | 4874 | 7969.25 | 1.66 | 1.37 | 0.84 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4402 | Río Caqueta Medio | 15565.72 | 1684.37 | 4350 | 13222.47 | 3.81 | 0.85 | 0.28 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4403 | Río Orteguaza | 7905.2 | 608.09 | 3751 | 8899.37 | 1.93 | 1.13 | 0.47 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4404 | Río Pescado | 2066.91 | 301.11 | 1091 | 2376.67 | 1.87 | 1.15 | 0.53 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4407 | Río Rutuya | 1134.73 | 173.78 | 356 | 1159.94 | 1.46 | 1.02 | 0.31 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 44 | Caquetá | 4408 | Río Mecaya | 4535.95 | 531.06 | 867 | 3140.71 | 2.22 | 0.69 | 0.19 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4409 | Río Sencella | 1741.46 | 343.43 | 376 | 1350.55 | 2.32 | 0.78 | 0.22 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4410 | Río Peneya | 1604.22 | 227.67 | 496 | 1543.41 | 1.6 | 0.96 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4414 | Río Cuemaní | 2427.54 | 345.6 | 943 | 2748.25 | 1.98 | 1.13 | 0.39 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4415 | Río Caqueta Bajo | 25311.12 | 1753.12 | 7216 | 23202.18 | 3.11 | 0.92 | 0.29 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4417 | Río Cahuinarí | 15029.05 | 919.14 | 3897 | 13658.44 | 2.12 | 0.91 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4418 | Río Mirití-Paraná | 9004.68 | 872.51 | 1962 | 7349.48 | 2.59 | 0.82 | 0.22 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4420 | Río Puré | 7628.25 | 565.65 | 1978 | 7199.08 | 1.83 | 0.94 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 45 | Yarí | 4501 | Alto Yarí | 7434.2 | 584.02 | 2988 | 7492.52 | 1.91 | 1.01 | 0.4 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 45 | Yarí | 4502 | Río Camuya | 2765.61 | 404.75 | 739 | 2244.45 | 2.17 | 0.81 | 0.27 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 45 | Yarí | 4504 | Medio Yarí | 5349.27 | 456.88 | 1059 | 4071.99 | 1.76 | 0.76 | 0.2 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 45 | Yarí | 4505 | Río Luisa | 3041.37 | 410.1 | 699 | 2910.25 | 2.1 | 0.96 | 0.23 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 45 | Yarí | 4506 | Bajo Yarí | 3863.39 | 513.83 | 1091 | 3396.76 | 2.33 | 0.88 | 0.28 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 45 | Yarí | 4509 | Río Cuñare | 5514.33 | 442.94 | 2020 | 5783.93 | 1.68 | 1.05 | 0.37 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 45 | Yarí | 4510 | Río Mesay | 8623.76 | 762.34 | 2197 | 7305.72 | 2.32 | 0.85 | 0.25 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 46 | Caguán | 4601 | Río Caguan Alto | 5837.11 | 612.17 | 2925 | 6346.7 | 2.26 | 1.09 | 0.5 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 46 | Caguán | 4602 | Río Guayas | 5491.62 | 477.6 | 3229 | 6759.71 | 1.82 | 1.23 | 0.59 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 46 | Caguán | 4604 | Río Caguan Bajo | 7413.53 | 721.41 | 1929 | 6074.55 | 2.36 | 0.82 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 46 | Caguán | 4605 | Río Sunsiya | 2465.71 | 430.93 | 654 | 2122.08 | 2.45 | 0.86 | 0.27 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 4701 | Alto Río Putumayo | 6986.15 | 481.02 | 3477 | 7316.86 | 1.62 | 1.05 | 0.5 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 4702 | Río San_Miguel | 2244.85 | 373.51 | 588 | 2086.29 | 2.22 | 0.93 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 4703 | Río Putumayo Medio | 5068.57 | 754.41 | 1049 | 3735.78 | 2.99 | 0.74 | 0.21 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 4704 | Río Putumayo Directos (mi) | 3522.47 | 852.89 | 746 | 2198.03 | 4.05 | 0.62 | 0.21 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 4705 | Río Cará-Paraná | 7315.68 | 737.49 | 2265 | 7190.22 | 2.43 | 0.98 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 4706 | Río Putumayo Bajo | 14172.27 | 1779.28 | 3118 | 10514.43 | 4.22 | 0.74 | 0.22 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 4707 | Río Igará-Paraná | 12879.11 | 872.39 | 3303 | 11189.37 | 2.17 | 0.87 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 4710 | Río Cotuhe | 3643.88 | 355.47 | 760 | 2921.91 | 1.66 | 0.8 | 0.21 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 4711 | Río Purite | 1989.76 | 278.0 | 494 | 1686.79 | 1.76 | 0.85 | 0.25 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 48 | Amazonas - Directos | 4801 | Directos Río Amazonas (mi) | 3256.52 | 375.27 | 698 | 2444.36 | 1.86 | 0.75 | 0.21 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 49 | Napo | 4901 | Río Chingual | 456.15 | 159.57 | 191 | 430.64 | 2.11 | 0.94 | 0.42 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 51 | Mira | 5101 | Río San Juan (Frontera Ecuador) | 351.31 | 159.02 | 72 | 218.91 | 2.39 | 0.62 | 0.2 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 51 | Mira | 5102 | Río Mira | 4093.84 | 623.44 | 1762 | 3257.49 | 2.75 | 0.8 | 0.43 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 51 | Mira | 5103 | Río Rosario | 833.46 | 151.6 | 438 | 636.91 | 1.48 | 0.76 | 0.53 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 51 | Mira | 5104 | Río Tola | 596.07 | 161.29 | 85 | 330.47 | 1.86 | 0.55 | 0.14 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 52 | Patía | 5201 | Río Patia Alto | 3220.19 | 464.44 | 1201 | 3059.09 | 2.31 | 0.95 | 0.37 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 52 | Patía | 5202 | Río Guachicono | 2627.15 | 281.07 | 2131 | 3992.4 | 1.55 | 1.52 | 0.81 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 52 | Patía | 5203 | Río Mayo | 874.61 | 169.19 | 699 | 1261.15 | 1.61 | 1.44 | 0.8 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 52 | Patía | 5204 | Río Juananbú | 2085.38 | 240.66 | 1278 | 2703.54 | 1.49 | 1.3 | 0.61 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 52 | Patía | 5205 | Río Guáitara | 3653.86 | 377.21 | 1998 | 4607.85 | 1.76 | 1.26 | 0.55 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 52 | Patía | 5206 | Río Telembí | 4641.09 | 377.59 | 1082 | 3235.67 | 1.56 | 0.7 | 0.23 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 52 | Patía | 5207 | Río Patia Medio | 2392.65 | 414.12 | 902 | 2233.99 | 2.39 | 0.93 | 0.38 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 52 | Patía | 5209 | Río Patia Bajo | 4534.66 | 454.54 | 892 | 2133.59 | 1.9 | 0.47 | 0.2 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5302 | Río Tapaje | 1604.0 | 251.96 | 660 | 1550.5 | 1.77 | 0.97 | 0.41 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5303 | Río Iscuandé | 2338.82 | 411.98 | 804 | 2010.59 | 2.4 | 0.86 | 0.34 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5304 | Río Guapi | 2626.35 | 278.84 | 1096 | 2631.89 | 1.53 | 1.0 | 0.42 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5305 | Río Timbiquí | 808.95 | 195.0 | 300 | 815.22 | 1.93 | 1.01 | 0.37 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5306 | Río Saija | 1089.23 | 200.98 | 518 | 1314.06 | 1.72 | 1.21 | 0.48 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5307 | Río San Juan del Micay | 4455.53 | 490.3 | 1775 | 4402.86 | 2.07 | 0.99 | 0.4 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5308 | Río Naya - Yurumanguí | 2667.43 | 319.11 | 1401 | 2885.23 | 1.74 | 1.08 | 0.53 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5309 | Ríos Cajambre - Mayorquín - Raposo | 2011.54 | 285.41 | 865 | 1596.64 | 1.8 | 0.79 | 0.43 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5310 | Río Anchicayá | 1293.58 | 231.68 | 460 | 1009.93 | 1.82 | 0.78 | 0.36 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5311 | Dagua - Buenaventura - Bahia Málaga | 1966.32 | 382.96 | 853 | 1962.14 | 2.44 | 1.0 | 0.43 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 54 | San Juán | 5401 | Río San Juan Alto | 2054.45 | 331.58 | 1025 | 2621.82 | 2.06 | 1.28 | 0.5 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 54 | San Juán | 5402 | Río Tamaná y otros Directos San Juan | 2827.0 | 329.17 | 1341 | 3447.38 | 1.75 | 1.22 | 0.47 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 54 | San Juán | 5403 | Río Sipí | 3028.03 | 334.48 | 1355 | 3683.39 | 1.71 | 1.22 | 0.45 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 54 | San Juán | 5404 | Río Cajón | 743.24 | 143.96 | 319 | 887.71 | 1.49 | 1.19 | 0.43 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 54 | San Juán | 5405 | Río Capoma y otros directos al San Juan | 2428.6 | 312.71 | 1259 | 3299.74 | 1.79 | 1.36 | 0.52 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 54 | San Juán | 5406 | Río Munguidó | 833.41 | 169.4 | 413 | 1147.54 | 1.66 | 1.38 | 0.5 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 54 | San Juán | 5407 | Ríos Calima y  Bajo San Juan | 3543.49 | 554.72 | 1900 | 4440.96 | 2.63 | 1.25 | 0.54 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 54 | San Juán | 5408 | Río San Juan Medio | 935.33 | 291.72 | 544 | 1169.19 | 2.69 | 1.25 | 0.58 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 55 | Baudó - Directos Pacifico | 5501 | Río Baudó | 4060.64 | 545.75 | 2238 | 5185.84 | 2.42 | 1.28 | 0.55 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 55 | Baudó - Directos Pacifico | 5502 | Río Docampadó y Directos Pacífico | 1908.15 | 324.3 | 1039 | 2428.37 | 2.09 | 1.27 | 0.54 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 56 | Pacífico - Directos | 5601 | Directos Pacifico Frontera Panamá | 4256.46 | 1031.69 | 2419 | 5447.84 | 4.46 | 1.28 | 0.57 | Oval-oblonga a rectangular-oblonga |

### Graficas generales

Grafica Área, km² vs. # Drenajes - Todos los subtipos de drenaje

![Graph0](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone//Graph/PlotAreaVsFREQUENCYDrainAll.png)

Grafica Área, km² vs. Sum. Long. Drenajes, km - Todos los subtipos de drenaje

![Graph1](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone//Graph/PlotAreaVsSUM_LDreDrainAll.png)

Grafica Área, km² vs. Kc - Índice de Compacidad - Todos los subtipos de drenaje

![Graph2](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone//Graph/PlotAreaVsKcDrainAll.png)

Grafica Área, km² vs. Dd - Densidad de drenajes - Todos los subtipos de drenaje

![Graph3](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone//Graph/PlotAreaVsDdDrainAll.png)

Grafica Área, km² vs. Dc - Densidad de corrientes - Todos los subtipos de drenaje

![Graph4](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone//Graph/PlotAreaVsDcDrainAll.png)

### Archivos de resultados ([/Output](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone/Output) [/Graph](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone/Graph))

* Capa AH - Área hidrográfica: D:/R.GISPython/HydroGeoZone/Output/AreaHidrografica.shp
* Capa ZH - Zona hidrográfica: D:/R.GISPython/HydroGeoZone/Output/ZonaHidrografica.shp
* Capa SZH - Subzona hidrográfica: D:/R.GISPython/HydroGeoZone/Output/SubZonaHidrografica.shp
* Capa Drenajes filtro permanentes: D:/R.GISPython/HydroGeoZone/Data/Drenaje_Sencillo.shp
* Capa intersección SZH & Drenajes: D:/R.GISPython/HydroGeoZone/Output/DrenajeSencilloIntersect.shp
* Tabla resultados AH - Área hidrográfica (dBase): D:/R.GISPython/HydroGeoZone/Output/AreaHidrograficaEstadistica.dbf
* Tabla resultados ZH - Zona hidrográfica (dBase): D:/R.GISPython/HydroGeoZone/Output/ZonaHidrograficaEstadistica.dbf
* Tabla resultados SZH - Subzona hidrográfica (dBase): D:/R.GISPython/HydroGeoZone/Output/SubZonaHidrograficaEstadistica.dbf
* Tabla resultados AH - Área hidrográfica (Excel): D:/R.GISPython/HydroGeoZone/Output/AreaHidrograficaEstadistica.xls
* Tabla resultados ZH - Zona hidrográfica (Excel): D:/R.GISPython/HydroGeoZone/Output/ZonaHidrograficaEstadistica.xls
* Tabla resultados SZH - Subzona hidrográfica (Excel): D:/R.GISPython/HydroGeoZone/Output/SubZonaHidrograficaEstadistica.xls
* Tabla resultados Drenajes por subtipo: D:/R.GISPython/HydroGeoZone/Output/DrenajeSencilloSubtipoEstadistica.dbf

> Los mapas desplegados en [/Graph](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone/Map) han sido generados manualmente en ArcGIS a partir de los datos obtenidos utilizando los mapas de proyecto disponibles en [/Map](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone/Map).

Fecha y hora de terminación de ejecución: 2021-12-29 12:25:12.813859

Proceso completado (dt = 30.9 sec o 0.5 min)

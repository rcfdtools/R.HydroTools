# https://github.com/rcfdtools
# HEC-HMS 4.13: Geometric properties calculator, Tc, LT, .gage and .met sentences generator
# This script has to be run in QGIS 3+ (Tested versions: 3.44.9, 4.0.1)
# Subbasin layer and CN map has to use the same projection system
# Before run, set Settings / Options / Processing / General / Invalid features filtering / Do not filter
# Steps (QGIS does't recognize the geometric fields Akm2, Pkm.... after the first run)
#   1. Run the script with compute_tc_lt = False
#   2. Close QGIS and reopen the projec
#   3. Switch compute_tc_lt = True and run  


# Libraries
import processing
from qgis.core import QgsRasterLayer, QgsVectorLayer
import pandas as pd
#import math as math
from math import pi


# General parameters
main_path = 'D:/R.TSIG/file/hec/HECHMS_v0/' # ● Your local main path
subbasin_path = main_path+'shp/ArroyoElZorroCuencas.shp' # ● Subbasin shapefile exported from HEC-HMS
cn_path = main_path+'grid/CNII_v1.tif' # ● Curve Number has to be always normal CNII grid map
total_gages = 39 # ● Gages correspond with the number of subbasins for PMax24h
cn_prefix = 'CNII_' # ● CN prefix for statistical fields
compute_tc_with_cn = 'CNII' # ● Compute Concentration Time Tc with curve number CNI-Dry, CNII-Normal or CNIII-Wet
subbasin_prefix = 'W' # ● Subbasin prefix assigned in HEC-HMS
# HEC-DSS database file parameters assigned for time series records
dss_file_name = 'HECHMS_v0.dss' # ● Your HEC-DSS database file
path_a = 'ArroyoElZorro' # ● Basin name
path_f = 'P_TR2.33_6h_FSCalif057' # ● Hyetograph
start_time = '1 January 2004, 06:00' # ● Start time
end_time = '6 January 2004, 06:00' # ● End time
lagtime_multiplier = 0.6
output_file = main_path+'table/'+path_a+'CuencasCN.csv' # ● Output .csv results file
compute_tc_lt = True # Compute Concentration Time Tc and LagTime
create_hms_sentences = True # Create .gage and .met sentences
# New fields and definitions
new_field_list = ['Akm2', # Subbasin area
                  'APD', #Area Percentual Distribution
                  'Pkm', # Subbasin perimeter
                  'ReachLTkm', # Subbasin total river length
                  'Kc' # Compactness factor (or Gravelius coefficient)
                 ]
definitions = (
              'name: Subbasin name with the prefix established by the user in HEC-HMS.'
              
              'long_len: Longest Flowpath Length (L) extends from the subbasin outlet to the most hydraulically-remote point upstream. Longest flowpath length is significant in that it is typically used to determine the time of concentration for a watershed.',
              
              'long_slo: Longest Flowpath Slope (SL) is calculated using the most upstream point of the longest flowpath and the most downstream point of the longtest flowpath (rise/run). The tabular result is presented in standard slope format and not as a percent slope.',
              
              'cent_len: Centroidal Flowpath Length (Lca) is a subset of the longest flowpath length. It begins at the subbasin outlet and extends upstream along the longest flowpath until it reaches the point along the longest flowpath that is nearest to the subbasin centroid. A comparison of centroidal flowpath and longest flowpath can be seen in the image below.',
              
              'cent_slo: Centroidal Flowpath Slope (Sca) is calculated using the point along the longest flowpath that is nearest to the subbasin centroid and the point at the subbasin outlet (rise/run). The tabular result is presented in standard slope format and not as a percent slope.',
              
              '10_85_len: 10-85 Flowpath Length (L10-85) is also a subset of longest flowpath length. Measuring from the outlet in the upstream direction, the 10-85 flowpath begins at a point representing ten percent of the total length of the longest flowpath and ends at a point representing eighty-five percent of the total length.',
              
              '10_85_slo: 10-85 Flowpath Slope (S10-85) is calculated using the point representing eighty-five percent of the total length and the point representing ten percent of the total length (rise/run). The tabular result is presented in standard slope format and not as a percent slope.  The 10-85 slope is often more representative of flowpath slopes as a whole within the watershed as it is not affected by the more extreme upstream elevations of the longest flowpath that are typically found near the watershed divide.',
              
              'basin_slo: Basin Slope (S) represents the average slope of the entire subbasin (rise/run). For each elevation raster value within the subbasin, the algorithm scans the surrounding eight neighbors and computes the slope using the maximum scanned elevation difference. The algorithm does not weigh north, east, south, and west neighbors more than diagonal neighbors; each neighbor is considered equally. The basin slope output is the average of all the computed slope values in the subbasin.',
              
              'basin_rel: Basin Relief (R) represents the elevation difference between the highest point on the drainage divide and the outlet point of the subbasin.',
              
              'elong_ra: Relief Ratio (RR) is simply the basin relief divided by the length of the longest flowpath.',
              
              'relief_ra: Elongation Ratio (El) is a dimensionless ratio used to categorize the general shape of a subbasin. It is a ratio between the diameter of a circle with the same area as the subbasin and the basin length. Elongation ratio values typically range from ~0.2 to 1.0, with lower values representing elongated basins and values close to 1 representing circular basins. ElongationRatio=(Area^0.5/BasinLength)*(2/π^0.5).',
              
              'drain_den: Drainage Density (DD) is a metric used to describe the efficiency in which a subbasin is drained by stream channels. It is computed by summing the total length of stream channels within the subbasin and then dividing by the area of the subbasin. It is important to note that drainage density that is calculated by HEC-HMS is dependent on the stream threshold used when defining a stream network.',
              
              'len_units: Indicates the unit system used for the HEC-HMS calculations.',

              'Akm2: Subbasin geodesic area.',
              
              'APD: Area percentual distribution.',
              
              'Pkm: Subbasin geodesic perimeter.',
              
              'ReachLTkm: Subbasin total river length. ReachLTkm=Akm2*drain_den/1000',
                      
              'Kc: Compactness factor or Gravelius coefficient: denoted also as Cc, measures a drainage basin’s shape by comparing its perimeter to the circumference of a circle with the same area. A ratio closer to 1 indicates a circular basin with rapid runoff and high flood risk, while higher values (e.g., >1.5) suggest elongated, safer watersheds. Low Kc (close to 1): Highly compact or circular. These basins collect water from all directions simultaneously, causing sharp, high-intensity peak flows. High Kc (>1): Elongated or irregular. These basins provide slower runoff, allowing water to infiltrate and reducing peak flow. Kc=P/2√(πA)',

              'CN: The Curve Number is an empirical parameter used in hydrology, developed by the USDA Soil Conservation Service (SCS), to predict direct runoff or infiltration from rainfall excess based on land use, soil type, and antecedent moisture. Ranging from 30 to 100, higher CN values (e.g., 98 for paved parking) indicate higher runoff potential, while lower values (e.g., <50 for forest) indicate higher infiltration. It is often called the SCS Curve Number or NRCS Curve Number. https://www.hec.usace.army.mil/confluence/hmsdocs/hmstrm/cn-tables',
              
              'Tc: The time of concentration is the time required for runoff to travel from the most hydraulically distant point in a watershed to its outlet. It represents the watershed’s response time to rainfall, used by engineers and hydrologists to predict peak discharge, design infrastructure like culverts, and evaluate flood risk.',
              
              'LT: Lag time in a hydrograph is the time delay between the center of mass of peak rainfall (or, more generally, the storm’s peak) and the peak discharge (maximum flow) in a river or stream. It measures how fast a watershed responds to rain, with shorter times indicating faster, more intense flooding.'
             )


# Geometric properties calculation
print('\n****************************************\nDefinitions and parameters calculations\n****************************************\n')
print(f'Subbasin parameters: {output_file}\n')
print('Definitions\n')
for i in definitions:
    print(f'{i}\n')
print('Calculations\n')
layer = QgsVectorLayer(subbasin_path, 'InputLayer', 'ogr')
if layer and layer.geometryType() == QgsWkbTypes.PolygonGeometry:
    
    # Delete existing fields
    for field in new_field_list:
        field_index = layer.fields().indexFromName(field)
        if field_index != -1:
            with edit(layer):
                 layer.dataProvider().deleteAttributes([field_index])
        layer.updateFields()
    
    # Create fields
    for field in new_field_list:
        layer.startEditing()
        layer.dataProvider().addAttributes([QgsField(field, QVariant.Double)])
    layer.commitChanges()
    layer.startEditing()
    
    # [Akm2] Area calculator
    total_area = 0.0
    field_index = layer.fields().indexOf('Akm2')
    for feature in layer.getFeatures():
        fid = feature.id()
        geom = feature.geometry()
        area = geom.area()/1000000 
        total_area += area
        layer.changeAttributeValue(fid, field_index, area)
    print(f'[Akm2] Total area (km²): {total_area}')

    # [APD] Area percentual distribution calculator
    field_index = layer.fields().indexOf('APD')
    total_apd = 0.0
    for feature in layer.getFeatures():
        fid = feature.id()
        apd = (feature[layer.fields().indexFromName('Akm2')] / total_area) * 100
        total_apd += apd
        layer.changeAttributeValue(fid, field_index, apd) 
    print(f'[APD] Area Percentual Distribution (%): {total_apd}')

    # [Pkm] Perimeter calculator
    field_index = layer.fields().indexOf('Pkm')
    for feature in layer.getFeatures():
        fid = feature.id()
        geom = feature.geometry()
        perimeter = geom.length()/1000
        layer.changeAttributeValue(fid, field_index, perimeter)
    print(f'[Pkm] Perimeter calculator (km): Done...')

    # [ReachLTkm] Subbasin total river length = "Akm2" * "drain_den" / 1000
    total_river_length = 0.0
    field_index = layer.fields().indexOf('ReachLTkm')
    for feature in layer.getFeatures():
        fid = feature.id()
        reachltkm = feature[layer.fields().indexFromName('Akm2')] * 1000000 * feature[layer.fields().indexFromName('drain_den')] / 1000
        total_river_length += reachltkm
        layer.changeAttributeValue(fid, field_index, reachltkm)    
    print(f'[ReachLTkm] Total river length (km): {total_river_length}')  
    
    # [Kc] Compactness factor (or Gravelius coefficient) calculator
    field_index = layer.fields().indexOf('Kc')
    for feature in layer.getFeatures():
        fid = feature.id()
        kc = feature[layer.fields().indexFromName('Pkm')] / (2*(pi*feature[layer.fields().indexFromName('Akm2')])**0.5)
        layer.changeAttributeValue(fid, field_index, kc) 
    print(f'[Kc] Gravelius coefficient (%): Done...')
else:
    print('Please use a valid polygon layer')
layer.commitChanges()


# CN zonal statistics
alg_params = {
    'COLUMN_PREFIX': cn_prefix,
    'INPUT': subbasin_path,
    'INPUT_RASTER': cn_path,
    'RASTER_BAND': 1,
    'STATISTICS': [4,2],  # 0-Count,1-Sum,2-Mean,3-Median,4-Standard deviation,5-Minimum,6-Maximum,7-Range,8-Minority (least common value),9-Majority (most common value),10-Variety (unique value count),11-Variance
    'OUTPUT': output_file
}
processing.run('native:zonalstatisticsfb', alg_params)


# CNI, CNIII and Concentration time - Tc and LagTime
df = pd.read_csv(output_file, sep=',')
df.rename(columns={'CNII_mean': 'CNII'}, inplace=True)
# CNI & CNIII
df['CNI'] =  df['CNII'] / (2.3 - 0.013 * df['CNII'])
df['CNIII'] = df['CNII'] / (0.43 + 0.0057 * df['CNII'])
if compute_tc_lt:
    # Tc in hours
    print('Concentration time - Tc (hours)')
    print(f'[TcSCS] Soil Conservation Service - SCS (USDA): done with {compute_tc_with_cn}...')
    df['TcSCS'] = (0.0526*(df['long_len']/0.3048)**0.8*((1000/ df[compute_tc_with_cn])-9)**0.7*(df['basin_slo']*100)**-0.5)/60
    print('[TcPilgrim] Pilgrim: Done...')
    df['TcPilgrim'] = 0.76*(df['Akm2'])**0.38
    print('[TcTemez] Témez: Done...')
    df['TcTemez'] =  0.30*((df['10_85_len']/1000)/(df['10_85_slo']**0.25))**0.76
    print('[TcKirpich] Kirpich: Done...')
    df['TcKirpich'] = 0.00013*((df['10_85_len']/0.3048)**0.77/(df['10_85_slo']**0.385))
    print('[TcGiandott] Giandotti: Done...')
    df['TcGiandott'] = (4*df['Akm2']**0.5+1.5*df['10_85_len']/1000)/(25.3*(df['10_85_slo']*df['10_85_len']/1000)**0.5)
    print('[TcValenZul] Valencia y Zuluaga: Done...')
    df['TcValenZul'] = 1.7694*df['Akm2']**0.325*(df['10_85_len']/1000)**-0.096*(df['10_85_slo']*100)**-0.29
    print('[TcClark] Clark: Done...')
    df['TcClark'] = 0.335*(df['Akm2']/df['10_85_slo']**0.5)**0.593
    print('[TcJCross] Johnstone y Cross: Done...')
    df['TcJCross'] = 2.6*((df['10_85_len']/1000)/((df['10_85_slo']*1000)**0.5))**0.5
    print('[TcRanser] SCS – Ranser: Done...')
    df['TcRanser'] = 0.947*((df['10_85_len']/1000)**3/df['basin_rel'])**0.385
    print('[TcVentura] Ventura - Heras: Done...')
    df['TcVentura'] = 0.30*((df['10_85_len']/1000)/(df['10_85_slo']*100)**0.25)**0.75
    print('[TcVTChow] Ven Te Chow: Done...')
    df['TcVTChow'] = 0.273*((df['10_85_len']/1000)/(df['10_85_slo']**0.5))**0.64
    print('[TcUSArmyC] U.S. Army Corps: Done...')
    df['TcUSArmyC'] = 0.28*((df['10_85_len']/1000)/(df['10_85_slo']**0.25))**0.76
    print('[TcWilliams] Williams: Done...')
    df['TcWilliams'] = 0.683*((df['10_85_len']/1000)*(df['Akm2'])**0.40/((2*(df['Akm2']/pi)**0.5)*(df['10_85_slo']*100)**0.25))
    print('[TcBransby] Bransby: Done...')
    df['TcBransby'] = 0.00032*((df['10_85_len']/0.3048)**0.77/(df['10_85_slo']**0.385))
    print('[TcPassini] Passini: Done...') 
    print('Some regional variations of the Pasini formula adjust the leading constant, ranging between 0.04 and 0.13 depending on localized calibration. Hydrological studies have shown that the Pasini formula typically performs with relatively low error in certain rural and natural watersheds, making it a reliable tool in many professional toolkits.')
    df['TcPassini'] = 0.108*((df['Akm2']*(df['10_85_len']/1000))**0.333/(df['10_85_slo']**0.5))
    print('[TcFAA] Federal Aviation Administration - FAA: Done...')
    df['TcFAA'] = 0.00013*((df['10_85_len'])**0.77/(df['10_85_slo']**0.385))
    print('[TcKerby] Kerby: Done...')
    df['TcKerby'] = 0.828*((df['long_len']/1000)**0.467/(df['basin_slo']**0.235))   
    # LagTime in minutes
    #a="df['LTSCS']"
    #b="lagtime_multiplier * df['TcSCS'] * 60"
    df['LTSCS'] = lagtime_multiplier * df['TcSCS'] * 60
    df['LTPilgrim'] = lagtime_multiplier * df['TcPilgrim'] * 60
    df['LTTemez'] = lagtime_multiplier * df['TcTemez'] * 60  
    df['LTKirpich'] = lagtime_multiplier * df['TcKirpich'] * 60 
    df['LTGiandott'] = lagtime_multiplier * df['TcGiandott'] * 60
    df['LTValenZul'] = lagtime_multiplier * df['TcValenZul'] * 60 
    df['LTClark'] = lagtime_multiplier * df['TcClark'] * 60 
    df['LTJCross'] = lagtime_multiplier * df['TcJCross'] * 60 
    df['LTRanser'] = lagtime_multiplier * df['TcRanser'] * 60 
    df['LTVentura'] = lagtime_multiplier * df['TcVentura'] * 60 
    df['LTVTChow'] = lagtime_multiplier * df['TcVTChow'] * 60 
    df['LTUSArmyC'] = lagtime_multiplier * df['TcUSArmyC'] * 60 
    df['LTWilliams'] = lagtime_multiplier * df['TcWilliams'] * 60 
    df['LTBransby'] = lagtime_multiplier * df['TcBransby'] * 60 
    df['LTPassini'] = lagtime_multiplier * df['TcPassini'] * 60 
    df['LTFAA'] = lagtime_multiplier * df['TcFAA'] * 60 
    df['LTKerby'] = lagtime_multiplier * df['TcKerby'] * 60 
    print('LagTime - LT (minutes): Done...') 
df.to_csv(output_file, index=False)
df = df.sort_values(by='name')
df.index.name = 'FID'
#print(df.select_dtypes(include='number').agg(['mean', 'max', 'min', 'sum']))
stats = ['mean'] # 'mean', 'sum', 'min', 'max'
for i in stats:
    print(f'\nDataset statistics ({i})\n')
    print(eval(f'df.{i}(numeric_only=True)'))


# Process .gage and .met file sentences 
if create_hms_sentences:
    # .gage file sentences
    print('\n\n****************************************\n.gage file sentences\n****************************************\n')
    for i in range(total_gages):
        print(f'Gage: {subbasin_prefix}{i+1}\n     Gage: {subbasin_prefix}{i+1}\n     Gage Type: Precipitation\n     Last Modified Date: 01 January 2026\n     Last Modified Time: 06:00:00\n     Reference Height Units: Meters\n     Reference Height: 9.9999\n     Data Source Type: External DSS\n     Filename: {dss_file_name}\n     Pathname: /{path_a}/{subbasin_prefix}{i+1}/PRECIP-INC//15Minute/{path_f}/\n     Variant: Variant-1\n       Start Time: {start_time}\n       End Time: {end_time}\n     End Variant: Variant-1\nEnd:\n')

    # .met file sentences
    print('\n****************************************\n.met file sentences\n****************************************\n')
    for i in range(total_gages):
        print(f'Subbasin: {subbasin_prefix}{i+1}\n     Last Modified Date: 01 January 2026\n     Last Modified Time: 06:00:00\n     Gage: W{i+1}\nEnd:\n')

print('\nProcess completed...')
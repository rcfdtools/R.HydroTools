# CAMELS-BR

Readme file created by Vinícius B. P. Chagas, 2020 (vbchagas@gmail.com).

Vinícius B. P. Chagas, Pedro L. B. Chaffe, Nans Addor, Fernando M. Fan, Ayan S. Fleischmann, Rodrigo C. D. Paiva, & Vinícius A. Siqueira. (2020). CAMELS-BR: Hydrometeorological time series and landscape attributes for 897 catchments in Brazil - link to files. (1.1) [Data set]. Zenodo.

https://zenodo.org/record/3964745


## (1) Description

This is the CAMELS-BR dataset (Catchment Attributes and MEteorology for Large-sample Studies - Brazil) accompanying the paper: 
Chagas et al., Hydrometeorological time series and landscape attributes for 897 catchments in Brazil, Earth System Science Data, 2020.

CAMELS-BR provides daily observed streamflow time series for 3679 stream gauges, daily meteorological time series and 65 attributes for 897 catchments in Brazil.

The daily hydrometeorological time series include (i) observed streamflow accompanied by quality control information, (ii) precipitation extracted from three global products, (iii) actual evapotranspiration, (iv) potential evapotranspiration, and (v) minimum, average, and maximum temperature.

The 65 catchment attributes cover properties such as (i) topography, (ii) climate, (iii) hydrology, (iv) land cover, (v) geology, (vi) soil, and (vii) human intervention.

The data follow the same standards from the other CAMELS datasets for the United States (https://doi.org/10.5194/hess-21-5293-2017), Chile (https://doi.org/10.5194/hess-22-5817-2018), and Great Britain (https://doi.org/10.5194/essd-2020-49).


## Changes in version 1.1:

* Added two climatic indices: et_mean and asynchronicity.
* Added simulated streamflow time series (from 1980 to 2014) for 593 catchments using the continental-scale MGB-SA model (Siqueira et al., 2018). Only gauges with upstream area difference < 10 % were included in the dataset.  
* Removed the streamflow time series of 34 gauges located outside Brazil, reducing from 3713 to 3679 gauges with available data.
* Added the areas of the 3679 catchments according to ANA (the Brazilian National Water Agency) and GSIM (Global Streamflow Indices and Metadata Archive; Do et al., 2018) to the location attributes (camels_br_location.txt).
* Added a shapefile with the location of the 3679 gauges and their respective catchment areas according to ANA and GSIM.
* Some attributes that referred to fractions (ranging from 0-1) now refer to percentages.
* Changed the name of some attributes to increase consistency in the dataset.
* Fixed incorrect gauge_id values in the catchment boundaries shapefile.


## (2) Contents


### (2.1) "01_CAMELS_BR_attributes"

This directory contains 9 txt files with the catchment attributes according to their categories and 1 Excel file with the description of the attributes and their associated units.
Missing values are represented by "nan".


### (2.2) "02_CAMELS_BR_streamflow_m3s"

This directory contains 3679 files with daily streamflow time series obtained from ANA's website (Brazilian National Water Agency - http://www.snirh.gov.br/hidroweb/).
Each file refers to the time series of a stream gauge. The gauge ID is the first eight digits of the file name.
Missing values are represented by "nan".

The column "streamflow_m3s" indicates daily observed streamflow in cubic meters per second.
The column "qual_control_by_ana" is set to 1 if the data was quality checked by ANA (Brazilian National Water Agency) and a value of 0 otherwise.
The column "qual_flag" indicates the reliability of streamflow estimates. It is provided by ANA (Brazilian National Water Agency) and consists of the following quality flags: 0, when there is no description; 1, streamflow resulted from stream stage measurements and the rating-curve; 2, streamflow qualitatively estimated by ANA, i.e., without stream stage measurements; 3, streamflow values marked as doubtful; and 4, when the stream water level falls outside the range of the stream stage.


### (2.3) "03_CAMELS_BR_streamflow_mm_selected_catchments"

This directory contains 897 files with daily streamflow time series.
Each file refers to the time series of a stream gauge. The gauge ID is the first eight digits of the file name.
Missing values are represented by "nan".

The column "streamflow_mm" indicates observed streamflow in millimeters per day.
The column "qual_control_by_ana" is set to 1 if the data was quality checked by ANA (Brazilian National Water Agency) and a value of 0 otherwise.
The column "qual_flag" indicates the reliability of streamflow estimates. It is provided by ANA (Brazilian National Water Agency) and consists of the following quality flags: 0, when there is no description; 1, streamflow resulted from stream stage measurements and the rating-curve; 2, streamflow qualitatively estimated by ANA, i.e., without stream stage measurements; 3, streamflow values marked as doubtful; and 4, when the stream water level falls outside the range of the stream stage.


### (2.4) "04_CAMELS_BR_streamflow_simulated"

This directory contains 593 files with simulated daily streamflow time series using the large-scale MGB-SA model (Modelo de Grandes Bacias; Siqueira et al., 2018).
Each file refers to the time series of a stream gauge. The gauge ID is the first eight digits of the file name.
Missing values are represented by "nan".

The column "simulated_streamflow_m3s" indicates simulated streamflow in cubic meters per second.


### (2.5) "05_CAMELS_BR_precipitation_chirps"

This directory contains 897 files with daily precipitation time series extracted from CHIRPS v2.0 (Funk et al., 2015).
Each file refers to the time series of a catchment. The gauge ID of the catchment is the first eight digits of the file name.
Missing values are represented by "nan".

The column "precipitation_chirps" indicates catchment averages of precipitation in millimeters per day.


### (2.6) "06_CAMELS_BR_precipitation_mswep"

This directory contains 897 files with daily precipitation time series extracted from MSWEP v2.2 (Beck et al., 2019).
Each file refers to the time series of a catchment. The gauge ID of the catchment is the first eight digits of the file name.
Missing values are represented by "nan".

The column "precipitation_mswep" indicates catchment averages of precipitation in millimeters per day.


### (2.7) "07_CAMELS_BR_precipitation_cpc"

This directory contains 897 files with daily precipitation time series extracted from CPC (NOAA, 2019a).
Each file refers to the time series of a catchment. The gauge ID of the catchment is the first eight digits of the file name.
Missing values are represented by "nan".

The column "precipitation_cpc" indicates catchment averages of precipitation in millimeters per day.


### (2.8) "08_CAMELS_BR_evapotransp_gleam"

This directory contains 897 files with daily actual evapotranspiration time series extracted from GLEAM v3.3a (Miralles et al., 2011; Martens et al., 2017).
Each file refers to the time series of a catchment. The gauge ID of the catchment is the first eight digits of the file name.
Missing values are represented by "nan".

The column "evapotransp_gleam" indicates catchment averages of evapotranspiration in millimeters per day.


### (2.9) "09_CAMELS_BR_evapotransp_mgb"

This directory contains 897 files with daily actual evapotranspiration time series extracted from MGB-SA (Siqueira et al., 2018).
Each file refers to the time series of a catchment. The gauge ID of the catchment is the first eight digits of the file name.
Missing values are represented by "nan".

The column "evapotransp_mgb" indicates catchment averages of evapotranspiration in millimeters per day.


### (2.10) "10_CAMELS_BR_potential_evapotransp_gleam"

This directory contains 897 files with daily potential evapotranspiration time series extracted from GLEAM v3.3a (Miralles et al., 2011; Martens et al., 2017).
Each file refers to the time series of a catchment. The gauge ID of the catchment is the first eight digits of the file name.
Missing values are represented by "nan".

The column "potential_evapotransp_gleam" indicates catchment averages of potential evapotranspiration in millimeters per day.


### (2.11) "11_CAMELS_BR_temperature_min_cpc"

This directory contains 897 files with daily minimum temperature time series extracted from CPC (NOAA, 2019b).
Each file refers to the time series of a catchment. The gauge ID of the catchment is the first eight digits of the file name.
Missing values are represented by "nan".

The column "temperature_min" indicates catchment averages of minimum daily temperature in degree Celsius.


### (2.12) "12_CAMELS_BR_temperature_mean_cpc"

This directory contains 897 files with daily average temperature time series, computed by averaging the daily minimum and maximum temperature extracted from CPC (NOAA, 2019b).
Each file refers to the time series of a catchment. The gauge ID of the catchment is the first eight digits of the file name.
Missing values are represented by "nan".

The column "temperature_mean" indicates catchment averages of average daily temperature in degree Celsius.


### (2.13) "13_CAMELS_BR_temperature_max_cpc"

This directory contains 897 files with daily maximum temperature time series extracted from CPC (NOAA, 2019b).
Each file refers to the time series of a catchment. The gauge ID of the catchment is the first eight digits of the file name.
Missing values are represented by "nan".

The column "temperature_max" indicates catchment averages of maximum daily temperature in degree Celsius.


### (2.14) "14_CAMELS_BR_catchment_boundaries"

This directory contains 5 files with the ESRI shapefile of the 897 catchment boundaries used in CAMELS-BR to extract the meteorological time series and catchment attributes.
The catchment boundaries were computed by Do et al. (2018) and Gudmundsson et al. (2018).


### (2.15) "15_CAMELS_BR_gauges_location_shapefile"

This directory contains 5 files with the ESRI shapefile of the location of the 3679 gauges with available streamflow time series.
The table of contents includes the location attributes, the catchment areas according to ANA (the Brazilian National Water Agency) and GSIM (Global Streamflow Indices and Metadata Archive; Do et al., 2018), and the data quality associated with GSIM estimates.


## (3) References

* Beck, H. E., Wood, E. F., Pan, M., Fisher, C. K., Miralles, D. G., van Dijk, A. I. J. M., McVicar, T. R. and Adler, R. F.: MSWEP V2 Global 3-Hourly 0.1° Precipitation: Methodology and Quantitative Assessment, Bull. Amer. Meteor. Soc., 100(3), 473–500, doi:10.1175/BAMS-D-17-0138.1, 2019.
* Do, H. X., Gudmundsson, L., Leonard, M. and Westra, S.: The Global Streamflow Indices and Metadata Archive (GSIM) – Part 1: The production of a daily streamflow archive and metadata, Earth Syst. Sci. Data, 10(2), 765–785, doi:10.5194/essd-10-765-2018, 2018.
* Funk, C., Peterson, P., Landsfeld, M., Pedreros, D., Verdin, J., Shukla, S., Husak, G., Rowland, J., Harrison, L., Hoell, A. and Michaelsen, J.: The climate hazards infrared precipitation with stations—a new environmental record for monitoring extremes, Sci Data, 2(1), doi:10.1038/sdata.2015.66, 2015.
* Gudmundsson, L., Do, H. X., Leonard, M. and Westra, S.: The Global Streamflow Indices and Metadata Archive (GSIM) – Part 2: Quality control, time-series indices and homogeneity assessment, Earth Syst. Sci. Data, 10(2), 787–804, doi:10.5194/essd-10-787-2018, 2018.
* Martens, B., Miralles, D. G., Lievens, H., van der Schalie, R., de Jeu, R. A. M., Fernández-Prieto, D., Beck, H. E., Dorigo, W. A. and Verhoest, N. E. C.: GLEAM v3: satellite-based land evaporation and root-zone soil moisture, Geosci. Model Dev., 10(5), 1903–1925, doi:10.5194/gmd-10-1903-2017, 2017.
* Miralles, D. G., Holmes, T. R. H., De Jeu, R. A. M., Gash, J. H., Meesters, A. G. C. A. and Dolman, A. J.: Global land-surface evaporation estimated from satellite-based observations, Hydrol. Earth Syst. Sci., 15(2), 453–469, doi:10.5194/hess-15-453-2011, 2011.
* NOAA: CPC Global Temperature, available from: https://www.esrl.noaa.gov/psd/ (Accessed 15 June 2019), 2019a.
* NOAA: CPC Global Unified Precipitation, available from: https://www.esrl.noaa.gov/psd/ (Accessed 15 June 2019), 2019b.
* Siqueira, V. A., Paiva, R. C. D., Fleischmann, A. S., Fan, F. M., Ruhoff, A. L., Pontes, P. R. M., Paris, A., Calmant, S. and Collischonn, W.: Toward continental hydrologic–hydrodynamic modeling in South America, Hydrol. Earth Syst. Sci., 22(9), 4815–4842, doi:10.5194/hess-22-4815-2018, 2018.
* https://essd.copernicus.org/articles/12/2075/2020/
* https://www.ufrgs.br/samewater/2020/12/02/camels-br/
* https://zenodo.org/record/3964745
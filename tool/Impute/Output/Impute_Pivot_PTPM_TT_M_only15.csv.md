# Impute missing values in time series through statistical methods

* Processed file: [D:/R.GISPython/Impute/Input/Pivot_PTPM_TT_M_only15.csv](../IDEAM_Outlier/Pivot_PTPM_TT_M_only15.csv)
* Execution date: 2023-04-25 15:48:06.695826
* Python version: 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
* Python path: ['D:\\R.GISPython\\Impute', 'D:\\R.GISPython', 'D:\\R.LTWB', 'D:\\R.GISPython.wiki', 'D:\\R.TeachingResearchGuide']
* matplotlib version: 3.7.1
* pandas version: 1.5.3
* numpy version: 1.24.2
* missingno version: 0.5.2
* sklearn version: 1.2.2
* Stations exclude: ['28017140', '25027020', '25027410', '25027490', '25027330', '25027390', '25027630', '25027360', '25027320', '16067010', '25027420']
* Stations include: ['15015020', '15060050', '15060070', '15060080', '15060150']
* Print table sample: True
* Instructions & script: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/Impute
* License: https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md
* Credits: r.cfdtools@gmail.com


## General dataframe information with 504 IDEAM records for 14 stations

Dataframe records head sample

| Fecha               |   15015020 |   15060050 |   15060070 |   15060080 |   15060150 |   15065040 |   16050240 |   16060010 |   16070010 |   16070020 |   16070030 |   16070040 |   23210020 |   23215050 |
|:--------------------|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|
| 1980-01-01 00:00:00 |          0 |          0 |          0 |          0 |          0 |        nan |        nan |         53 |         50 |        nan |        200 |         67 |        nan |         50 |
| 1980-01-02 00:00:00 |          0 |         27 |        133 |         23 |         23 |        nan |        nan |         16 |         87 |        nan |         97 |         59 |        nan |         14 |
| 1980-01-03 00:00:00 |          0 |          0 |          0 |          0 |          4 |        nan |        nan |          6 |         18 |        nan |          0 |         34 |        nan |          9 |

Dataframe records tail sample

| Fecha               |   15015020 |   15060050 |   15060070 |   15060080 |   15060150 |   15065040 |   16050240 |   16060010 |   16070010 |   16070020 |   16070030 |   16070040 |   23210020 |   23215050 |
|:--------------------|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|
| 2021-01-10 00:00:00 |        nan |        214 |        nan |        307 |        356 |        nan |        nan |        245 |        nan |        nan |        nan |        932 |        525 |      273.3 |
| 2021-01-11 00:00:00 |        nan |         11 |        nan |         81 |         34 |        nan |        nan |        402 |        nan |        nan |        nan |        437 |        330 |      123   |
| 2021-01-12 00:00:00 |        nan |         16 |        nan |         23 |         43 |        nan |        nan |        132 |        nan |        nan |        nan |        468 |         42 |       52.5 |

Datatypes for station and nulls values in the initial file
|       | 15015020   | 15060050   | 15060070   | 15060080   | 15060150   | 15065040   | 16050240   | 16060010   | 16070010   | 16070020   | 16070030   | 16070040   | 23210020   | 23215050   |
|:------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Dtype | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    |
| Nulls | 165        | 17         | 117        | 1          | 0          | 261        | 177        | 0          | 67         | 350        | 195        | 32         | 207        | 37         |

![R.LTWB](Pivot_PTPM_TT_M_only15.csv.png)

![R.LTWB](Missingno_Pivot_PTPM_TT_M_only15.csv.png)

<div align="center">

General statistics table - Initial file

</div>


<div align="center">

|          |   count |     mean |      std |   min |    25% |   50% |     75% |    max |
|---------:|--------:|---------:|---------:|------:|-------:|------:|--------:|-------:|
| 15015020 |     339 |  59.7829 |  74.2829 |     0 |   0.5  |  30.1 |  85.2   |  407   |
| 15060050 |     487 |  87.9507 |  83.7311 |     0 |  12.1  |  74   | 138.1   |  489.2 |
| 15060070 |     387 | 103.287  | 105.964  |     0 |  15    |  82   | 150     |  655   |
| 15060080 |     503 |  98.771  |  93.6652 |     0 |  15    |  83   | 148.5   |  722   |
| 15060150 |     504 |  72.1262 |  80.4786 |     0 |   8    |  46.1 | 107.375 |  383   |
| 15065040 |     243 |  65.5008 |  59.54   |     0 |  10.8  |  53   | 107.75  |  237.7 |
| 16050240 |     327 | 178.577  | 136.351  |     0 |  82    | 156   | 246     | 1150   |
| 16060010 |     504 | 304.344  | 206.676  |     0 | 146.25 | 284.5 | 426.25  | 1005   |
| 16070010 |     437 | 410.432  | 267.691  |     0 | 196    | 396   | 578     | 1444   |
| 16070020 |     154 | 393.565  | 269.214  |     0 | 162.25 | 366   | 557.5   | 1210   |
| 16070030 |     309 | 390.891  | 245.702  |     0 | 216    | 359   | 524     | 1351   |
| 16070040 |     472 | 353.798  | 208.838  |     8 | 204.5  | 341   | 485.25  | 1173   |
| 23210020 |     297 | 159.691  | 137.871  |     0 |  45    | 130   | 241     |  649   |
| 23215050 |     467 | 233.842  | 212.824  |     0 |  74.5  | 182.3 | 332.85  | 1094.2 |

</div>



## Method 1 - Imputing with mean values
According to this technique, the missing values are imputed using the mean value in each feature and the serie has been completed filled.

Imputed file: [Impute_Mean_Pivot_PTPM_TT_M_only15.csv](Impute_Mean_Pivot_PTPM_TT_M_only15.csv)

![R.LTWB](Impute_Mean_Pivot_PTPM_TT_M_only15.csv.png)

![R.LTWB](Missingno_Impute_Mean_Pivot_PTPM_TT_M_only15.csv.png)

<div align="center">

General statistics table - Imputed file

</div>


<div align="center">

|          |   count |     mean |      std |   min |     25% |      50% |      75% |    max |
|---------:|--------:|---------:|---------:|------:|--------:|---------:|---------:|-------:|
| 15015020 |     504 |  59.7829 |  60.8924 |     0 |  12.225 |  59.7829 |  60.275  |  407   |
| 15060050 |     504 |  87.9507 |  82.304  |     0 |  15     |  76.4    | 132.475  |  489.2 |
| 15060070 |     504 | 103.287  |  92.826  |     0 |  33.025 | 103.287  | 132.25   |  655   |
| 15060080 |     504 |  98.771  |  93.572  |     0 |  15     |  83      | 148.25   |  722   |
| 15060150 |     504 |  72.1262 |  80.4786 |     0 |   8     |  46.1    | 107.375  |  383   |
| 15065040 |     504 |  65.5008 |  41.2984 |     0 |  61.05  |  65.5008 |  65.5008 |  237.7 |
| 16050240 |     504 | 178.577  | 109.77   |     0 | 123.5   | 178.577  | 186.25   | 1150   |
| 16060010 |     504 | 304.344  | 206.676  |     0 | 146.25  | 284.5    | 426.25   | 1005   |
| 16070010 |     504 | 410.432  | 249.226  |     0 | 228.5   | 410.432  | 549.5    | 1444   |
| 16070020 |     504 | 393.565  | 148.477  |     0 | 393.565 | 393.565  | 393.565  | 1210   |
| 16070030 |     504 | 390.891  | 192.265  |     0 | 312     | 390.891  | 408      | 1351   |
| 16070040 |     504 | 353.798  | 202.086  |     8 | 215     | 353.798  | 469.5    | 1173   |
| 23210020 |     504 | 159.691  | 105.763  |     0 | 102.825 | 159.691  | 160      |  649   |
| 23215050 |     504 | 233.842  | 204.847  |     0 |  83.15  | 200.55   | 316.6    | 1094.2 |

</div>



## Method 2 - Imputing with median values
According to this technique, the missing values are imputed using the median value in each feature and the serie has been completed filled.

Imputed file: [Impute_Median_Pivot_PTPM_TT_M_only15.csv](Impute_Median_Pivot_PTPM_TT_M_only15.csv)

![R.LTWB](Impute_Median_Pivot_PTPM_TT_M_only15.csv.png)

![R.LTWB](Missingno_Impute_Median_Pivot_PTPM_TT_M_only15.csv.png)

<div align="center">

General statistics table - Imputed file

</div>


<div align="center">

|          |   count |     mean |      std |   min |     25% |   50% |     75% |    max |
|---------:|--------:|---------:|---------:|------:|--------:|------:|--------:|-------:|
| 15015020 |     504 |  50.0653 |  62.4683 |     0 |  12.225 |  30.1 |  60.275 |  407   |
| 15060050 |     504 |  87.4802 |  82.3426 |     0 |  15     |  74   | 132.475 |  489.2 |
| 15060070 |     504 |  98.345  |  93.2609 |     0 |  33.025 |  82   | 132.25  |  655   |
| 15060080 |     504 |  98.7397 |  93.5746 |     0 |  15     |  83   | 148.25  |  722   |
| 15060150 |     504 |  72.1262 |  80.4786 |     0 |   8     |  46.1 | 107.375 |  383   |
| 15065040 |     504 |  59.0272 |  41.769  |     0 |  53     |  53   |  53     |  237.7 |
| 16050240 |     504 | 170.648  | 110.298  |     0 | 123.5   | 156   | 186.25  | 1150   |
| 16060010 |     504 | 304.344  | 206.676  |     0 | 146.25  | 284.5 | 426.25  | 1005   |
| 16070010 |     504 | 408.513  | 249.274  |     0 | 228.5   | 396   | 549.5   | 1444   |
| 16070020 |     504 | 374.423  | 149.02   |     0 | 366     | 366   | 366     | 1210   |
| 16070030 |     504 | 378.552  | 192.892  |     0 | 312     | 359   | 408     | 1351   |
| 16070040 |     504 | 352.985  | 202.11   |     8 | 215     | 341   | 469.5   | 1173   |
| 23210020 |     504 | 147.496  | 106.769  |     0 | 102.825 | 130   | 160     |  649   |
| 23215050 |     504 | 230.058  | 205.289  |     0 |  83.15  | 182.3 | 316.6   | 1094.2 |

</div>



## Method 3 - Imputing with Last Observation Carried Forward (LOCF) values
According to this technique, the missing values are imputed using the immediate values before it in the time series and the missing values at the start are not filled but the series are completed fillet to the end.

Imputed file: [Impute_LOCF_Pivot_PTPM_TT_M_only15.csv](Impute_LOCF_Pivot_PTPM_TT_M_only15.csv)

![R.LTWB](Impute_LOCF_Pivot_PTPM_TT_M_only15.csv.png)

![R.LTWB](Missingno_Impute_LOCF_Pivot_PTPM_TT_M_only15.csv.png)

<div align="center">

General statistics table - Imputed file

</div>


<div align="center">

|          |   count |     mean |      std |   min |     25% |    50% |     75% |    max |
|---------:|--------:|---------:|---------:|------:|--------:|-------:|--------:|-------:|
| 15015020 |     504 |  54.7111 |  68.8435 |     0 |   0     |  23.05 | 110.55  |  407   |
| 15060050 |     504 |  86.123  |  83.3989 |     0 |  10.1   |  73.2  | 133     |  489.2 |
| 15060070 |     504 |  93.9502 |  94.8751 |     0 |  18.575 |  72    | 132.25  |  655   |
| 15060080 |     504 |  98.7615 |  93.5722 |     0 |  15     |  83    | 148.25  |  722   |
| 15060150 |     504 |  72.1262 |  80.4786 |     0 |   8     |  46.1  | 107.375 |  383   |
| 15065040 |     501 |  69.2156 |  53.3627 |     0 |   5.6   |  86    | 104.9   |  237.7 |
| 16050240 |     454 | 227.649  | 139.976  |     0 | 111.25  | 219.95 | 354     | 1150   |
| 16060010 |     504 | 304.344  | 206.676  |     0 | 146.25  | 284.5  | 426.25  | 1005   |
| 16070010 |     504 | 421.466  | 254.652  |     0 | 220.75  | 433    | 568     | 1444   |
| 16070020 |     430 | 375.453  | 162.083  |     0 | 366     | 366    | 366     | 1210   |
| 16070030 |     504 | 390.49   | 196.475  |     0 | 309.5   | 380    | 423     | 1351   |
| 16070040 |     504 | 346.702  | 209.566  |     8 | 185.75  | 340.5  | 471.25  | 1173   |
| 23210020 |     320 | 150.934  | 136.594  |     0 |  32.75  | 113.75 | 231     |  649   |
| 23215050 |     504 | 236.717  | 206.501  |     0 |  79.8   | 195.2  | 319     | 1094.2 |

</div>



## Method 4 - Imputing with Next Observation Carried Backward (NOCB) values
According to this technique, the missing values are imputed using the immediate values after it in the time series and the missing values at the end are not filled but the series are completed fillet to the start.

Imputed file: [Impute_NOCB_Pivot_PTPM_TT_M_only15.csv](Impute_NOCB_Pivot_PTPM_TT_M_only15.csv)

![R.LTWB](Impute_NOCB_Pivot_PTPM_TT_M_only15.csv.png)

![R.LTWB](Missingno_Impute_NOCB_Pivot_PTPM_TT_M_only15.csv.png)

<div align="center">

General statistics table - Imputed file

</div>


<div align="center">

|          |   count |     mean |      std |   min |     25% |    50% |     75% |    max |
|---------:|--------:|---------:|---------:|------:|--------:|-------:|--------:|-------:|
| 15015020 |     408 |  70.2412 |  74.0461 |     0 |   1.5   |  51.2  | 139.5   |  407   |
| 15060050 |     504 |  85.5754 |  83.3238 |     0 |  10.5   |  71.9  | 132.475 |  489.2 |
| 15060070 |     406 |  98.453  | 105.73   |     0 |   7.175 |  75.35 | 146.85  |  655   |
| 15060080 |     504 |  98.8944 |  93.6131 |     0 |  15     |  83    | 149     |  722   |
| 15060150 |     504 |  72.1262 |  80.4786 |     0 |   8     |  46.1  | 107.375 |  383   |
| 15065040 |     342 |  77.8336 |  56.9421 |     0 |  20.25  |  83.5  | 124     |  237.7 |
| 16050240 |     377 | 155.291  | 140.267  |     0 |  49     | 134    | 224     | 1150   |
| 16060010 |     504 | 304.344  | 206.676  |     0 | 146.25  | 284.5  | 426.25  | 1005   |
| 16070010 |     453 | 405.518  | 265.859  |     0 | 197     | 388    | 575     | 1444   |
| 16070020 |     230 | 312.648  | 249.51   |     0 | 144     | 164.5  | 487     | 1210   |
| 16070030 |     343 | 398.378  | 240.054  |     0 | 233.5   | 378    | 542.5   | 1351   |
| 16070040 |     504 | 356.642  | 202.87   |     8 | 215     | 358    | 469.5   | 1173   |
| 23210020 |     504 | 165.338  | 107.483  |     0 |  99.75  | 183    | 183     |  649   |
| 23215050 |     504 | 231.5    | 205.603  |     0 |  79.8   | 195.45 | 319     | 1094.2 |

</div>



## Method 5 - Impute missing values with Linear Interpolation values
According to this technique, the missing values are imputed using the linear interpolation between knowing pair values in the time series and the missing values at the start are not filled but the series are completed fillet to the end.

Imputed file: [Impute_InterpolateLinear_Pivot_PTPM_TT_M_only15.csv](Impute_InterpolateLinear_Pivot_PTPM_TT_M_only15.csv)

![R.LTWB](Impute_InterpolateLinear_Pivot_PTPM_TT_M_only15.csv.png)

![R.LTWB](Missingno_Impute_InterpolateLinear_Pivot_PTPM_TT_M_only15.csv.png)

<div align="center">

General statistics table - Imputed file

</div>


<div align="center">

|          |   count |     mean |      std |   min |      25% |      50% |     75% |    max |
|---------:|--------:|---------:|---------:|------:|---------:|---------:|--------:|-------:|
| 15015020 |     504 |  55.7865 |  70.3477 |     0 |   0      |  22.95   | 110.55  |  407   |
| 15060050 |     504 |  85.8492 |  83.2329 |     0 |  10.1692 |  72      | 132.475 |  489.2 |
| 15060070 |     504 |  93.6298 |  95.1532 |     0 |  18.575  |  72      | 132.25  |  655   |
| 15060080 |     504 |  98.828  |  93.5808 |     0 |  15      |  83      | 148.25  |  722   |
| 15060150 |     504 |  72.1262 |  80.4786 |     0 |   8      |  46.1    | 107.375 |  383   |
| 15065040 |     501 |  77.9172 |  47.697  |     0 |  35.8    |  97.4286 | 104.9   |  237.7 |
| 16050240 |     454 | 227.649  | 139.976  |     0 | 111.25   | 219.95   | 354     | 1150   |
| 16060010 |     504 | 304.344  | 206.676  |     0 | 146.25   | 284.5    | 426.25  | 1005   |
| 16070010 |     504 | 419.183  | 252.871  |     0 | 223.5    | 431.5    | 551.75  | 1444   |
| 16070020 |     430 | 375.56   | 161.407  |     0 | 366      | 366      | 366     | 1210   |
| 16070030 |     504 | 391.499  | 195.543  |     0 | 311.5    | 380      | 441.75  | 1351   |
| 16070040 |     504 | 351.672  | 204.024  |     8 | 207.5    | 341.5    | 471.25  | 1173   |
| 23210020 |     320 | 153.059  | 135.068  |     0 |  45      | 113.75   | 231     |  649   |
| 23215050 |     504 | 234.109  | 205.405  |     0 |  83.15   | 195.2    | 316.6   | 1094.2 |

</div>



## Method 6 - Impute missing values with Exponential (Weighted) Moving Average - EWM = 3
According to this technique, the missing values are imputed using the moving average values in the time series and the missing values at the start are not filled but the series are completed fillet to the end.

Imputed file: [Impute_MeanEWM_Pivot_PTPM_TT_M_only15.csv](Impute_MeanEWM_Pivot_PTPM_TT_M_only15.csv)

![R.LTWB](Impute_MeanEWM_Pivot_PTPM_TT_M_only15.csv.png)

![R.LTWB](Missingno_Impute_MeanEWM_Pivot_PTPM_TT_M_only15.csv.png)

<div align="center">

General statistics table - Imputed file

</div>


<div align="center">

|          |   count |     mean |      std |   min |      25% |      50% |      75% |    max |
|---------:|--------:|---------:|---------:|------:|---------:|---------:|---------:|-------:|
| 15015020 |     504 |  64.0539 |  61.2785 |     0 |  12.225  |  73.3108 |  74.9122 |  407   |
| 15060050 |     504 |  86.9911 |  82.4987 |     0 |  15      |  72      | 132.475  |  489.2 |
| 15060070 |     504 |  95.698  |  94.4906 |     0 |  18.8089 |  80.6381 | 132.25   |  655   |
| 15060080 |     504 |  98.6782 |  93.5952 |     0 |  15      |  82.5    | 148.25   |  722   |
| 15060150 |     504 |  72.1262 |  80.4786 |     0 |   8      |  46.1    | 107.375  |  383   |
| 15065040 |     501 |  57.6942 |  42.7212 |     0 |  46.613  |  46.613  |  67.0514 |  237.7 |
| 16050240 |     454 | 197.172  | 119.464  |     0 | 111.25   | 219.95   | 245.05   | 1150   |
| 16060010 |     504 | 304.344  | 206.676  |     0 | 146.25   | 284.5    | 426.25   | 1005   |
| 16070010 |     504 | 407.988  | 249.694  |     0 | 228.5    | 387.106  | 549.5    | 1444   |
| 16070020 |     430 | 418.767  | 161.986  |     0 | 433.235  | 433.235  | 433.235  | 1210   |
| 16070030 |     504 | 399.801  | 193.47   |     0 | 312      | 413.167  | 418.25   | 1351   |
| 16070040 |     504 | 348.936  | 203.945  |     8 | 204.902  | 340.5    | 471.25   | 1173   |
| 23210020 |     320 | 158.144  | 132.975  |     0 |  49.85   | 135.518  | 231      |  649   |
| 23215050 |     504 | 231.228  | 205.215  |     0 |  79.8    | 194.9    | 316.6    | 1094.2 |

</div>



## Method 7 - Impute missing values with Natural Neigborns - KNN = 4 Imputer from Scikit Learn
According to this technique, the missing values are imputed using the natural neighbors values and the serie has been completed filled. More information in https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html

Imputer = KNNImputer(n_neighbors=n_neighbors, weights=uniform, metric=nan_euclidean)

Imputed file: [Impute_KNN_Pivot_PTPM_TT_M_only15.csv](Impute_KNN_Pivot_PTPM_TT_M_only15.csv)

![R.LTWB](Impute_KNN_Pivot_PTPM_TT_M_only15.csv.png)

![R.LTWB](Missingno_Impute_KNN_Pivot_PTPM_TT_M_only15.csv.png)

<div align="center">

General statistics table - Imputed file

</div>


<div align="center">

|          |   count |     mean |      std |   min |      25% |     50% |      75% |    max |
|---------:|--------:|---------:|---------:|------:|---------:|--------:|---------:|-------:|
| 15015020 |     504 |  58.2724 |  67.1701 |     0 |   0.6375 |  36.45  |  89.6063 |  407   |
| 15060050 |     504 |  87.8003 |  83.0588 |     0 |  13.75   |  74.5   | 138.05   |  489.2 |
| 15060070 |     504 | 102.636  | 101.032  |     0 |  16      |  83     | 151.5    |  655   |
| 15060080 |     504 |  98.9242 |  93.6352 |     0 |  15      |  83     | 149      |  722   |
| 15060150 |     504 |  72.1262 |  80.4786 |     0 |   8      |  46.1   | 107.375  |  383   |
| 15065040 |     504 |  64.0865 |  52.8249 |     0 |  13.475  |  61.575 | 103.65   |  237.7 |
| 16050240 |     504 | 170.717  | 124.441  |     0 |  78.9375 | 150.25  | 236.625  | 1150   |
| 16060010 |     504 | 304.344  | 206.676  |     0 | 146.25   | 284.5   | 426.25   | 1005   |
| 16070010 |     504 | 403.25   | 260.419  |     0 | 195.312  | 391.5   | 569.188  | 1444   |
| 16070020 |     504 | 397.849  | 243.98   |     0 | 181.188  | 406.375 | 567.438  | 1210   |
| 16070030 |     504 | 380.948  | 225.814  |     0 | 215.5    | 359.5   | 522.5    | 1351   |
| 16070040 |     504 | 355.734  | 205.394  |     8 | 210.188  | 343.5   | 487.812  | 1173   |
| 23210020 |     504 | 159.489  | 128.69   |     0 |  54.0125 | 138     | 246.325  |  649   |
| 23215050 |     504 | 232.206  | 207.638  |     0 |  75.375  | 188.65  | 330.15   | 1094.2 |

</div>



## Method 8 - Impute missing values with Multivariate Imputation by Chained Equation - MICE from Scikit Learn
According to this technique, the missing values are imputed using MICE values and the serie has been completed filled. More information in https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html

Imputer = IterativeImputer(estimator=BayesianRidge(), min_value=0, n_nearest_features=4)

Imputed file: [Impute_MICE_Pivot_PTPM_TT_M_only15.csv](Impute_MICE_Pivot_PTPM_TT_M_only15.csv)

![R.LTWB](Impute_MICE_Pivot_PTPM_TT_M_only15.csv.png)

![R.LTWB](Missingno_Impute_MICE_Pivot_PTPM_TT_M_only15.csv.png)

<div align="center">

General statistics table - Imputed file

</div>


<div align="center">

|          |   count |     mean |      std |   min |       25% |     50% |      75% |    max |
|---------:|--------:|---------:|---------:|------:|----------:|--------:|---------:|-------:|
| 15015020 |     504 |  62.8381 |  67.5679 |     0 |   6.87378 |  45.2   |  92.5444 |  407   |
| 15060050 |     504 |  87.8203 |  83.2162 |     0 |  14.5038  |  73.75  | 138.05   |  489.2 |
| 15060070 |     504 | 106.592  | 102.608  |     0 |  19       |  85     | 160.147  |  655   |
| 15060080 |     504 |  99.0062 |  93.7208 |     0 |  15       |  83     | 149      |  722   |
| 15060150 |     504 |  72.1262 |  80.4786 |     0 |   8       |  46.1   | 107.375  |  383   |
| 15065040 |     504 |  65.0901 |  50.0436 |     0 |  23.2824  |  59.25  |  95.5015 |  237.7 |
| 16050240 |     504 | 179.496  | 121.331  |     0 |  92.6377  | 159     | 242      | 1150   |
| 16060010 |     504 | 304.344  | 206.676  |     0 | 146.25    | 284.5   | 426.25   | 1005   |
| 16070010 |     504 | 414.649  | 261.885  |     0 | 201.25    | 400     | 579.25   | 1444   |
| 16070020 |     504 | 390.195  | 218.038  |     0 | 208.049   | 369.743 | 534.738  | 1210   |
| 16070030 |     504 | 377.449  | 215.824  |     0 | 224.249   | 358.5   | 505      | 1351   |
| 16070040 |     504 | 354.441  | 204.699  |     8 | 208.75    | 343.476 | 480.25   | 1173   |
| 23210020 |     504 | 155.797  | 124.318  |     0 |  51.092   | 137.558 | 235.075  |  649   |
| 23215050 |     504 | 231.818  | 206.84   |     0 |  78.55    | 186.317 | 323.825  | 1094.2 |

</div>


Complementary report with individual graphs for stations in [Impute_Station_Pivot_PTPM_TT_M_only15.csv.md](Impute_Station_Pivot_PTPM_TT_M_only15.csv.md)

> As you notice, some of the techniques showed above can`t fill complete the missing values at the start or at the end, however, you can first choice a method and then apply another complementary method for get full filled the missin values.

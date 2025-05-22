# -*- coding: UTF-8 -*-
# Tested with: Python 3.10, SciPy 1.11.3, NumPy 1.26.1, Pandas 2.1.3

import pandas as pd

dr = pd.read_csv('Changi_daily_rainfall.csv', index_col=0, header=0, parse_dates=True)
print(dr.head())
print(dr.describe())

# Mean (Location Parameter)
print(dr.mean())

# Median (Location Parameter)
print(dr.median())

# Variance (Scale Parameter)
print(dr.var())

# Skewness (Shape Parameter)
print(dr.skew())

# Kurtosis (Shape Parameter)
print(dr.kurtosis())



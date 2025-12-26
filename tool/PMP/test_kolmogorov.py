# To compare two sample series using the Kolmogorov-Smirnov (K-S) test in SciPy, use the scipy.stats.ks_2samp() function or the more general scipy.stats.kstest() function, which automatically performs the two-sample test if provided two arrays of data.
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ks_2samp.html

from scipy import stats
import numpy as np

# Generate two example data series (samples)
# Sample 1 from a normal distribution with mean 5, scale 10
#rvs1 = stats.norm.rvs(loc=5, scale=10, size=20)
rvs1 = [0.025641026,0.051282051,0.076923077,0.102564103,0.128205128,0.153846154,0.179487179,0.205128205,0.230769231,0.256410256,0.282051282,0.307692308,0.333333333,0.358974359,0.384615385,0.41025641,0.435897436,0.461538462,0.487179487,0.512820513,0.538461538,0.564102564,0.58974359,0.615384615,0.641025641,0.666666667,0.692307692,0.717948718,0.743589744,0.769230769,0.794871795,0.820512821,0.846153846,0.871794872,0.897435897,0.923076923,0.948717949,0.974358974,1] # station 25020230 EDF California values
# Sample 2 from a different normal distribution with mean 8, scale 10
#rvs2 = stats.norm.rvs(loc=8, scale=10, size=20)
rvs2 = [0.0150854,0.0194003,0.0338425,0.108387,0.129029,0.17654,0.1941,0.261359,0.261359,0.272628,0.281967,0.313769,0.313769,0.357423,0.368495,0.368495,0.368495,0.379609,0.424302,0.435486,0.479991,0.566182,0.57655,0.586807,0.586807,0.68226,0.683143,0.699616,0.793723,0.796969,0.803345,0.868211,0.877071,0.877071,0.877071,0.877071,0.897034,0.914126,0.994854] # alpha_cdf values

# Perform the two-sample K-S test
ks_statistic, p_value = stats.ks_2samp(rvs1, rvs2, method='auto')

print(f"KS Statistic: {ks_statistic}")
print(f"P-value: {p_value}")
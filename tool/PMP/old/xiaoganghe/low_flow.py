# -*- coding: UTF-8 -*-
# Tested with: Python 3.10, SciPy 1.11.3, NumPy 1.26.1, Pandas 2.1.3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import genextreme as gev

show_plot = True  # Show plot on screen

ds = pd.read_csv('Streamflow_02401390.dat', delimiter='\s+', index_col=0, header=None, parse_dates=True)
ds.columns = ["Streamflow"]
ds.index.name = 'Date'
print(ds.head())

# Calculate 5-day flow
ds5day = ds.rolling(5, center=True).mean()  # moving average
ds5day.columns = ["5-day flow"]
print(ds5day.head())

# Extract annual low-flow
lowf = ds5day.resample("Y").min()  # yearly minimum
lowf.index = lowf.index.year
lowf.columns = ["Annual low-flow"]
print(lowf.head())

# Plot annual 5-day low-flow
plt.plot(lowf)
plt.xlabel("Year")
plt.ylabel("Low-flow ($m^3/s$)")
if show_plot: plt.show()

# Fit distribution (parameter estimation)
c0, loc0, scale0  = gev.fit(lowf, method="MLE")
print(loc0, scale0, c0)
MLEGEV = gev(c0, loc=loc0, scale=scale0)  # Frozen distribution
'''
c1, loc1, scale1  = gev.fit(lowf, method="MM")
print(loc1, scale1, c1)
MMGEV = gev(c1, loc=loc1, scale=scale1)  # Frozen distribution
'''

# Plot empirical PDF
plt.hist(lowf, density=True, histtype='stepfilled', alpha=0.2, label='Empirical PDF')
# Plot estimated PDF based on maximum likelihood method
bins = np.linspace(MLEGEV.ppf(0.01), MLEGEV.ppf(0.99), 100)
plt.plot(bins, MLEGEV.pdf(bins), 'r-', lw=2, label='Estimated PDF (MLE)')
plt.legend(loc='best', frameon=False)
if show_plot: plt.show()

# Plot empirical CDF
plt.scatter(lowf.sort_values(by = ["Annual low-flow"]), np.arange(1, lowf.size+1, dtype=float)/lowf.size, color = 'orangered', facecolors='none', label='Empirical CDF')
# Plot estimated PDF based on maximum likelihood method
bins = np.linspace(MLEGEV.ppf(0.01), MLEGEV.ppf(0.99), 100)
plt.plot(bins, MLEGEV.cdf(bins), 'r-', lw=2, label='Estimated CDF (MLE)')
plt.legend(loc='best', frameon=False)
if show_plot: plt.show()

MLEKS = stats.kstest(lowf["Annual low-flow"], MLEGEV.cdf)
print('\nKolmogorov-Smirnov (KS) test')
print(MLEKS)

# Estimate extreme values for specific return periods from 2 years to 1000 years
T = np.arange(2, 1001)

# extreme low-flow under each return period
LFTmle = MLEGEV.ppf(1.0 / T)
LFTmle = pd.DataFrame(LFTmle, index=T, columns=["Annual 5-day low-flow"])
LFTmle.index.name = "Return period"
print(LFTmle.loc[[2, 5, 10, 15, 20, 25, 50, 75, 100, 200, 250, 500, 1000]])

# Plot low-flow vs return periods
plt.plot(LFTmle, 'r-', lw=2, label='MLE')
plt.xscale('log')
plt.ylabel('Annual 5-day low-flow ($m^3/s$)')
plt.xlabel('Return period (years)')
plt.legend(loc='best', frameon=False)
if show_plot: plt.show()


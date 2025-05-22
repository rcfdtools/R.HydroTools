# -*- coding: UTF-8 -*-
# Tested with: Python 3.10, SciPy 1.11.3, NumPy 1.26.1, Pandas 2.1.3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import genextreme
from scipy.stats import invgauss
from scipy.stats import ncf

show_plot = True  # Show plot on screen
parameter_name = 'rain'
parameter_units = '($mm$)'
f_dist = 'invgauss'  # Only works with probability distributions with 3 parameters: loc, scale, shape
print('# arguments: %s' %eval(f_dist).numargs)

df = pd.read_csv('25020230.csv', delimiter=',', index_col=0, parse_dates=True)
df.columns = [parameter_name]
df.index.name = 'date'
print(df.head())

# Plot annual
plt.plot(df)
plt.xlabel("Year")
plt.ylabel(parameter_name + ' ' + parameter_units)
if show_plot: plt.show()

# Fit distribution (parameter estimation)
c0, loc0, scale0  = eval(f_dist).fit(df, method="MLE")
print(loc0, scale0, c0)
MLE_p_dist = eval(f_dist)(c0, loc=loc0, scale=scale0)  # Frozen distribution


# Plot empirical PDF
plt.hist(df, density=True, histtype='stepfilled', alpha=0.2, label='Empirical PDF')
# Plot estimated PDF based on maximum likelihood method
bins = np.linspace(MLE_p_dist.ppf(0.01), MLE_p_dist.ppf(0.99), 100)
plt.plot(bins, MLE_p_dist.pdf(bins), 'r-', lw=2, label='Estimated PDF (MLE)')
plt.legend(loc='best', frameon=False)
if show_plot: plt.show()

# Plot empirical CDF
plt.scatter(df.sort_values(by = [parameter_name]), np.arange(1, df.size+1, dtype=float)/df.size, color = 'orangered', facecolors='none', label='Empirical CDF')
# Plot estimated PDF based on maximum likelihood method
bins = np.linspace(MLE_p_dist.ppf(0.01), MLE_p_dist.ppf(0.99), 100)
plt.plot(bins, MLE_p_dist.cdf(bins), 'r-', lw=2, label='Estimated CDF (MLE)')
plt.legend(loc='best', frameon=False)
if show_plot: plt.show()

MLEKS = stats.kstest(df[parameter_name], MLE_p_dist.cdf)
print('\nKolmogorov-Smirnov (KS) test')
print(MLEKS)

# Estimate extreme values for specific return periods from 2 years to 1000 years
tr = [2, 2.33, 5, 10, 15, 20, 25, 50, 75, 100, 200, 250, 500, 750, 1000]
df_tr = pd.DataFrame(tr, columns=['tr'])

# extreme values under each return period
#LFTmle = MLE_p_dist.ppf(1.0 - 1.0 / df_tr)  # maximum
LFTmle = MLE_p_dist.ppf(1.0 / df_tr)  # minimum
LFTmle = pd.DataFrame(LFTmle, index=tr, columns=[parameter_name])
LFTmle.index.name = "Return period"
print(LFTmle)

# Plot x vs return periods
plt.plot(LFTmle, 'r-', lw=2, label='MLE')
plt.xscale('log')
plt.ylabel(parameter_name)
plt.xlabel('Return period (years)')
plt.legend(loc='best', frameon=False)
if show_plot: plt.show()


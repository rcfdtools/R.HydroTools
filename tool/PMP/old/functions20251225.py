# -*- coding: UTF-8 -*-
# Tested with: Python 3.10, SciPy 1.11.3, NumPy 1.26.1, Pandas 2.1.3

# General libraries
from scipy import stats
import numpy as np
import math
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# General vars description
dicts = ([['app_version', 'app_version'], # App control version
          ['runtime', 'runtime'],
          ['python_version', 'Python version'],
          ['scipy_version', 'SciPy version'],
          ['pandas_version', 'Pandas version'],
          ['numpy_version', 'NumPy version'],
          ['station_dataset_file', 'Stations dataset (station_dataset_file)'],
          ['station_catalog_file', 'Stations catalog (station_catalog_file)'],
          ['plot_only_fit', 'Plot only fit distributions with Δo > Δ (plot_only_fit)'],
          ['low_extreme', 'Eval low extreme values, if False, evaluates high extreme values (low_extreme)'],
          ['pdist_gumbel_on', 'Eval Gumbel distribution, non include in SciPy (pdist_loggumbel_on)'],
          ['pdist_loggumbel_on', 'Eval Log-Gumbel distribution, non include in SciPy (pdist_loggumbel_on)'],
          ['pdist_logarithmic_on', 'Eval every SciPy distribution as logarithmic (pdist_logarithmic_on)'],
          ['ddof', 'Standard deviation normalized (ddof)'],
          ['tr', 'Return periods to eval in years (Tr)'],
          ['minimum_sample', 'Minimum data sample per station, 0 means any (minimum_sample)'],
          ['zscore', 'Z-Score threshold to adjust a value, 0 means disable (zscore)'],
          ['avoid_zeros', 'Avoid zeros, e.g. rain = 0 (avoid_zeros)'],
          ['avoid_nans', 'Avoid null values (avoid_nans)']
         ])


# Probability density function - PDF (from SciPy)
# l_pdist_scipy requires: ([Distribution function, # parameters, fit method, label, active)]
l_pdist_scipy = ([['gumbel_l', 2, 'MM', 'Gumbel Left Skew', True],
                  ['gumbel_r', 2, 'MM', 'Gumbel Right Skew', True],
                  ['norm', 2, 'MM', 'Normal', True],
                  ['lognorm', 3, 'MLE', 'Log Normal', True],
                  ['foldnorm', 3, 'MM', 'Fold Normal', False],  # Check: not for rain data
                  ['halfnorm', 2, 'MM', 'Half Normal', True],
                  ['gennorm', 3, 'MLE', 'Generalized Normal', False],
                  ['norminvgauss', 4, 'MLE', 'Normal Inverse Gaussian', False],
                  ['powernorm', 3, 'MLE', 'Power normal', False],
                  ['powerlognorm', 4, 'MLE', 'Power log-normal', False],
                  ['skewnorm', 3, 'MLE', 'Skew normal', False],
                  ['truncnorm', 4,'MLE', 'Truncated normal', True],
                  ['pearson3', 3, 'MM', 'Pearson type III', True],
                  ['genextreme', 3, 'MLE', 'Generalized exponential', False],
                  ['alpha', 3, 'MLE', 'Alpha', True],
                  ['anglit', 2, 'MM', 'Anglit', False],
                  ['arcsine', 2, 'MM', 'Arcsine', False],
                  ['argus', 3, 'MLE', 'Argus', False],
                  ['beta', 4, 'MLE', 'Beta', False],
                  ['betaprime', 4, 'MLE', 'Beta prime', True],
                  ['bradford', 3, 'MLE', 'Bradford', False],
                  ['burr', 4, 'MLE', 'Burr (Type III)', False],
                  ['burr12', 4, 'MLE', 'Burr (Type III) 12', False],
                  ['cauchy', 2, 'MLE', 'Cauchy', False],
                  ['cosine', 2, 'MLE', 'Cosine', False],
                  ['halfcauchy', 2, 'MLE', 'Half-Cauchy', False],
                  ['foldcauchy', 3, 'MLE', 'Fold Cauchy', False],
                  ['skewcauchy', 3, 'MLE', 'Skewed Cauchy', False],
                  ['wrapcauchy', 3, 'MLE', 'Wrapped  Cauchy', False],
                  ['chi2', 3, 'MLE', 'Chi²', True],
                  ['crystalball', 4, 'MLE', 'Crystalball', True],
                  ['gamma', 3, 'MLE', 'Gamma', True],
                  ['dgamma', 3, 'MLE', 'Double gamma', True],
                  ['gengamma', 4, 'MLE', 'Generalized gamma', False],
                  ['invgamma', 3, 'MLE', 'Inverted gamma', True],
                  ['loggamma', 3, 'MLE', 'Log gamma', True],
                  ['expon', 2, 'MLE', 'Exponential', True],
                  ['genexpon', 5, 'MLE', 'Generalized exponential', True],
                  ['exponnorm', 3, 'MLE', 'Exponentially modified Normal', True],
                  ['exponweib', 4, 'MLE', 'Exponentiated Weibull', False],
                  ['exponpow', 3, 'MLE', 'Exponential power', False],
                  ['erlang', 3, 'MLE', 'Erlang', True],  # Check: integer value alert
                  ['fatiguelife', 3, 'MLE', 'Fatigue-life (Birnbaum-Saunders)', True],
                  ['truncexpon', 3, 'MLE', 'Truncated exponential', False],
                  ['f', 4, 'MLE', 'F', True],
                  ['fisk', 3, 'MLE', 'Fisk', True],
                  ['genlogistic', 3, 'MLE', 'Generalized logistic', True],
                  ['gausshyper', 6, 'MLE', 'Gauss hypergeometric', False],
                  ['genhalflogistic', 3, 'MLE', 'Generalized half-logistic', False],
                  ['genhyperbolic', 5, 'MLE', 'Generalized hyperbolic', False],
                  ['geninvgauss', 4, 'MLE', 'Generalized Inverse Gaussian', False],
                  ['gibrat', 2, 'MM', 'Gibrat', True],
                  ['gompertz', 3, 'MLE', 'Gompertz (or truncated Gumbel)', True],
                  ['halflogistic', 2, 'MM', 'Half-logistic', True],
                  ['halfgennorm', 3, 'MLE', 'Upper half of a generalized normal', False],
                  ['hypsecant', 2, 'MM', 'hyperbolic secant', True],
                  ['invgauss', 3, 'MLE', 'Inverse Gaussian', True],
                  ['invweibull', 3, 'MLE', 'Inverted Weibull', True],
                  ['johnsonsb', 4, 'MLE', 'Johnson SB', False],
                  ['johnsonsu', 4, 'MLE', 'Johnson Su', True],
                  ['kappa4', 4, 'MLE', 'Kappa 4', False],
                  ['kappa3', 3, 'MLE', 'Kappa 3', False],
                  ['ksone', 3, 'MLE', 'Kolmogorov-Smirnov one-sided test statistic distribution', False],
                  ['kstwo', 3, 'MLE', 'Kolmogorov-Smirnov two-sided test statistic distribution', False],  # Check: zero division, don't use
                  ['kstwobign', 2, 'MLE', 'Limiting distribution of scaled Kolmogorov-Smirnov two-sided test statistic', True],
                  ['laplace', 2, 'MM', 'Laplace', True],
                  ['laplace_asymmetric', 3, 'MLE', 'Asymmetric Laplace', True],
                  ['loglaplace', 3, 'MLE', 'Log-Laplace', False],
                  ['levy', 2, 'MLE', 'Levy', False],
                  ['levy_l', 2, 'MLE', 'Left-skewed Levy', False],
                  ['levy_stable', 4, 'MLE', 'Levy-stable', False],
                  ['logistic', 2, 'MM', 'Logistic (or Sech-squared)', True],
                  ['maxwell', 2, 'MM', 'Maxwell', True],
                  ['mielke', 4, 'MLE', 'Mielke Beta-Kappa / Dagum', True],
                  ['moyal', 2, 'MM', 'Moyal', True],
                  ['nakagami', 3, 'MLE', 'Nakagami', True],
                  ['ncx2', 4, 'MLE', 'Non-central chi-squared', False],
                  ['ncf', 5, 'MLE', 'Non-central F distribution', True],
                  ['nct', 4, 'MLE', 'Non-central Student’s t', True],
                  ['pareto', 3, 'MLE', 'Pareto', True],
                  ['genpareto', 3, 'MLE', 'Generalized Pareto', False],
                  ['truncpareto', 4, 'MLE', 'Upper truncated Pareto', False],
                  ['lomax', 3, 'MLE', 'Lomax (Pareto of the second kind)', False],
                  ['powerlaw', 3, 'MLE', 'Power-function', False],
                  ['rdist', 3, 'MLE', 'R-distributed (symmetric beta)', False],
                  ['rayleigh', 2, 'MM', 'Rayleigh', True],
                  ['rel_breitwigner', 3, 'MLE', 'Relativistic Breit-Wigner', False],
                  ['rice', 3, 'MLE', 'Rice', True],
                  ['recipinvgauss', 3, 'MLE', 'Reciprocal inverse Gaussian', True],
                  ['semicircular', 2, 'MM', 'Semicircular', False],
                  ['studentized_range', 4, 'MLE', 'Studentized range', False],  # Check: don't converge
                  ['t', 3, 'MLE', 'Student’s t', True],
                  ['trapezoid', 4, 'MLE', 'Trapezoid', False],
                  ['triang', 3, 'MLE', 'Triangular', False],
                  ['truncweibull_min', 5, 'MLE', 'Doubly truncated Weibull minimum', False],
                  ['tukeylambda', 3, 'MLE', 'Tukey-Lamdba', False],
                  ['uniform', 2, 'MLE', 'Uniform', False],
                  ['loguniform', 4, 'MLE', 'Log-Uniform or reciprocal', False],
                  ['vonmises', 3, 'MLE', 'Von Mises', False],  # Check: values out of range
                  ['vonmises_line', 3, 'MLE', 'Von Mises line', False],
                  ['wald', 2, 'MM', 'Wald', True],
                  ['weibull_min', 3, 'MLE', 'Weibull minimum', True],
                  ['weibull_max', 3, 'MLE', 'Weibull maximum', False],  # Check: not for rain data
                  ['dweibull', 3, 'MLE', 'Double Weibull', False]
                 ])


# Scipy probability distributions
def pdist_scipy(dfx, p_dist, n_parameter, fit_method, p_dist_tag, x, low_extreme, df_tr, station_code, vDeltaKolmogorov):
    # dfx: dataset to eval
    # p_dist: probability distribution function name in SciPy
    # n_parameter: # parameters required
    # fit_method: parameter estimation method. (MLE) Maximum likelihood method or (MM) L-moments
    # p_dist_tag: probability distribution label for reports
    n_parameter = eval('stats.'+p_dist).numargs + 2  # + 2 means loc and scale
    n = len(dfx)
    if n_parameter == 2:
        loc, scale = eval('stats.'+p_dist).fit(dfx[x], method=fit_method)
        dfx[p_dist] = eval('stats.'+p_dist).cdf(dfx[x], loc, scale)  # Cumulative distribution function
        shape, shape1, shape2, shape3 = '', '', '', ''
        frozen_dist = eval('stats.'+p_dist)(loc=loc, scale=scale)  # Frozen distribution
        if low_extreme:
            x_extreme = frozen_dist.ppf(1 / df_tr.tr)
        else:
            x_extreme = frozen_dist.ppf(1 - 1 / df_tr.tr)
        df_tr[p_dist] = x_extreme
    elif n_parameter == 3:
        shape, loc, scale = eval('stats.'+p_dist).fit(dfx[x], method=fit_method)
        dfx[p_dist] = eval('stats.'+p_dist).cdf(dfx[x], shape, loc, scale)  # Cumulative distribution function
        shape1, shape2, shape3 = '', '', ''
        frozen_dist = eval('stats.'+p_dist)(shape, loc=loc, scale=scale)  # Frozen distribution
        if low_extreme:
            x_extreme = frozen_dist.ppf(1 / df_tr.tr)
        else:
            x_extreme = frozen_dist.ppf(1 - 1 / df_tr.tr)
        df_tr[p_dist] = x_extreme
    elif n_parameter == 4:
        shape, shape1, loc, scale = eval('stats.'+p_dist).fit(dfx[x], method=fit_method)
        dfx[p_dist] = eval('stats.'+p_dist).cdf(dfx[x], shape, shape1, loc, scale)  # Cumulative distribution function
        shape2, shape3 = '', ''
        frozen_dist = eval('stats.'+p_dist)(shape, shape1, loc=loc, scale=scale)  # Frozen distribution
        if low_extreme:
            x_extreme = frozen_dist.ppf(1 / df_tr.tr)
        else:
            x_extreme = frozen_dist.ppf(1 - 1 / df_tr.tr)
        df_tr[p_dist] = x_extreme
    elif n_parameter == 5:
        shape, shape1, shape2, loc, scale = eval('stats.'+p_dist).fit(dfx[x], method=fit_method)
        dfx[p_dist] = eval('stats.'+p_dist).cdf(dfx[x], shape, shape1, shape2, loc, scale)  # Cumulative distribution function
        shape3 = ''
        frozen_dist = eval('stats.'+p_dist)(shape, shape1, shape2, loc=loc, scale=scale)  # Frozen distribution
        if low_extreme:
            x_extreme = frozen_dist.ppf(1 / df_tr.tr)
        else:
            x_extreme = frozen_dist.ppf(1 - 1 / df_tr.tr)
        df_tr[p_dist] = x_extreme
    elif n_parameter == 6:
        shape, shape1, shape2, shape3, loc, scale = eval('stats.'+p_dist).fit(dfx[x], method=fit_method)
        dfx[p_dist] = eval('stats.'+p_dist).cdf(dfx[x], shape, shape1, shape2, shape3, loc, scale)  # Cumulative distribution function
        frozen_dist = eval('stats.'+p_dist)(shape, shape1, shape2, shape3, loc=loc, scale=scale)  # Frozen distribution
        if low_extreme:
            x_extreme = frozen_dist.ppf(1 / df_tr.tr)
        else:
            x_extreme = frozen_dist.ppf(1 - 1 / df_tr.tr)
        df_tr[p_dist] = x_extreme
    else:
        print('%s\n* Error: check the # parameters entered...')
    dfx[p_dist+'_pdf'] =  frozen_dist.pdf(dfx.x)
    vDeltaKolmogorovData = [station_code, '', p_dist, 0.0, 0.0, '', '', n, loc, scale, shape, shape1, shape2,shape3]
    #vDeltaKolmogorovData = [station_code, '', '', 0.0, 0.0, '', '', n, loc, scale, shape, shape1, shape2,shape3]
    #vDeltaKolmogorovData = [station_code, '', '', 0.0, 0.0, '', '', n]
    vDeltaKolmogorov.loc[len(vDeltaKolmogorov)] = vDeltaKolmogorovData  # Add the results as a new record


# Scipy probability distributions logarithmic
def pdist_scipy_log(dfx, p_dist, n_parameter, fit_method, p_dist_tag, x, low_extreme, df_tr, station_code, vDeltaKolmogorov):
    # dfx: dataset to eval
    # p_dist: probability distribution function name in SciPy
    # n_parameter: # parameters required
    # fit_method: parameter estimation method. (MLE) Maximum likelihood method or (MM) L-moments
    # p_dist_tag: probability distribution label for reports
    n_parameter = eval('stats.'+p_dist).numargs + 2  # + 2 means loc and scale
    n = len(dfx)
    if n_parameter == 2:
        loc, scale = eval('stats.'+p_dist).fit(np.log(dfx[x]), method=fit_method)
        dfx[f'log{p_dist}'] = eval('stats.'+p_dist).cdf(np.log(dfx[x]), loc, scale)  # Cumulative distribution function
        shape, shape1, shape2, shape3 = '', '', '', ''
        frozen_dist = eval('stats.'+p_dist)(loc=loc, scale=scale)  # Frozen distribution
        if low_extreme:
            x_extreme = frozen_dist.ppf(1 / df_tr.tr)
        else:
            x_extreme = frozen_dist.ppf(1 - 1 / df_tr.tr)
        df_tr[f'log{p_dist}'] = np.exp(x_extreme)
    elif n_parameter == 3:
        shape, loc, scale = eval('stats.'+p_dist).fit(np.log(dfx[x]), method=fit_method)
        dfx[f'log{p_dist}'] = eval('stats.'+p_dist).cdf(np.log(dfx[x]), shape, loc, scale)  # Cumulative distribution function
        shape1, shape2, shape3 = '', '', ''
        frozen_dist = eval('stats.'+p_dist)(shape, loc=loc, scale=scale)  # Frozen distribution
        if low_extreme:
            x_extreme = frozen_dist.ppf(1 / df_tr.tr)
        else:
            x_extreme = frozen_dist.ppf(1 - 1 / df_tr.tr)
        df_tr[f'log{p_dist}'] = np.exp(x_extreme)
    elif n_parameter == 4:
        shape, shape1, loc, scale = eval('stats.'+p_dist).fit(np.log(dfx[x]), method=fit_method)
        dfx[f'log{p_dist}'] = eval('stats.'+p_dist).cdf(np.log(dfx[x]), shape, shape1, loc, scale)  # Cumulative distribution function
        shape2, shape3 = '', ''
        frozen_dist = eval('stats.'+p_dist)(shape, shape1, loc=loc, scale=scale)  # Frozen distribution
        if low_extreme:
            x_extreme = frozen_dist.ppf(1 / df_tr.tr)
        else:
            x_extreme = frozen_dist.ppf(1 - 1 / df_tr.tr)
        df_tr[f'log{p_dist}'] = np.exp(x_extreme)
    elif n_parameter == 5:
        shape, shape1, shape2, loc, scale = eval('stats.'+p_dist).fit(np.log(dfx[x]), method=fit_method)
        dfx[f'log{p_dist}'] = eval('stats.'+p_dist).cdf(np.log(dfx[x]), shape, shape1, shape2, loc, scale)  # Cumulative distribution function
        shape3 = ''
        frozen_dist = eval('stats.'+p_dist)(shape, shape1, shape2, loc=loc, scale=scale)  # Frozen distribution
        if low_extreme:
            x_extreme = frozen_dist.ppf(1 / df_tr.tr)
        else:
            x_extreme = frozen_dist.ppf(1 - 1 / df_tr.tr)
        df_tr[f'log{p_dist}'] = np.exp(x_extreme)
    elif n_parameter == 6:
        shape, shape1, shape2, shape3, loc, scale = eval('stats.'+p_dist).fit(np.log(dfx[x]), method=fit_method)
        dfx[f'log{p_dist}'] = eval('stats.'+p_dist).cdf(np.log(dfx[x]), shape, shape1, shape2, shape3, loc, scale)  # Cumulative distribution function
        frozen_dist = eval('stats.'+p_dist)(shape, shape1, shape2, shape3, loc=loc, scale=scale)  # Frozen distribution
        if low_extreme:
            x_extreme = frozen_dist.ppf(1 / df_tr.tr)
        else:
            x_extreme = frozen_dist.ppf(1 - 1 / df_tr.tr)
        df_tr[f'log{p_dist}'] = np.exp(x_extreme)
    else:
        print('%s\n* Error: check the # parameters entered...')
    dfx[f'log{p_dist}_pdf'] =  frozen_dist.pdf(np.log(dfx.x))
    vDeltaKolmogorovData = [station_code, '', f'log{p_dist}', 0.0, 0.0, '', '', n, loc, scale, shape, shape1, shape2,shape3]
    #vDeltaKolmogorovData = [station_code, '', '', 0.0, 0.0, '', '', n, loc, scale, shape, shape1, shape2,shape3]
    #vDeltaKolmogorovData = [station_code, '', '', 0.0, 0.0, '', '', n]
    vDeltaKolmogorov.loc[len(vDeltaKolmogorov)] = vDeltaKolmogorovData  # Add the results as a new record


# Empirical distributions function - EDF
# edf_dist_dict requires: ([EDF function, EDF name, expression, year, description)]
edf_dist_dict = ([
                  ['edf_california', 'EDF California', 'P=m/n', '1923', 'California´s estimates the true probability distribution of water-related data (like rainfall, streamflow) using observed samples, crucial for risk assessment.'],
                  ['edf_hazen', 'EDF Hazen', 'P=(m-0.5)/n', '1930', 'Hazen method for plotting positions is a formula used to estimate the empirical cumulative probability distribution of flood events or other hydrological data. This formula often results in biased estimations, particularly when extrapolating to extreme events (high return periods).'],
                  ['edf_weibull', 'EDF Weibull', 'P=m/(n+1)', '1939', 'Weibull plotting position formula is an empirical method used to estimate the non-exceedance probability or plotting position for a set of observed data, is often recommended or widely used in practice, particularly in flood frequency analysis.'],
                  ['edf_beard', 'EDF Beard', 'P=(m-0.31)/(n+0.38)', '1943', 'The Beard formula (or Beard´s plotting position formula) in hydrology is used to estimate the empirical non-exceedance probability _(P)_ of a flood event (or other extreme hydrological data point) within a given dataset.'],
                  ['edf_chegodayev', 'EDF Chegodayev', 'P=(m-b)/(n+1-2b)', '1955', 'The Chegodayev formula is an empirical plotting position formula used in hydrological frequency analysis to estimate the exceedance probability or return period of a specific event from a set of observed data. It is primarily used for plotting observed data points on probability paper to fit a theoretical distribution, particularly for analyzing extreme events like maximum flood flows or rainfall intensities. The constant _b_ value in the generalized plotting position formula is 0.3.'],
                  ['edf_blom', 'EDF Blom', 'P=(m-a)/(n+1-2a)', '1958', 'The Blom formula is a specific "plotting position" formula used in hydrology and statistical analysis to estimate the empirical cumulative probability (or non-exceedance probability) of a data series. It is particularly recommended for data that are approximately normally distributed. The constant _a_ is set to 0.375 (or 3/8).'],
                  ['edf_tukey', 'EDF Tukey', 'P=(m-c)/(n+1-2c)', '1962', 'In hydrology, the Tukey formula is used as a plotting position formula to estimate the empirical probability or frequency of a flood event (or other hydrological data). The formula parameter is given as _c=0.333_ (or 1/3).'],
                  ['edf_gringorten', 'EDF Gringorten', 'P=(m-a)/(n+1-2a)', '1963', 'Gringorten plotting position formula is essential for estimating the probability and return periods of extreme events like floods and heavy rainfall. The constant _a=0.44_.'],
                  ['edf_jenkinson', 'EDF Jenkinson', 'P=(m-a)/(n+b)', '1977', 'The Jenkinson formula in hydrology is an empirical plotting position formula used to estimate the non-exceedance probability _(P)_ or return period _(T)_ of a given ordered observation within a sample. It is a widely used method in the frequency analysis of extreme events such as floods and rainfall, as it provides a distribution-free way to plot data. _a≈0.31_ and _b≈0.38_ are constants derived to approximate the median of the probability distribution for the given rank.'],
                  ['edf_cunnane', 'EDF Cunnane', 'P=(m-b)/(n+1-2b)', '1978', 'Cunnane´s work in statistical hydrology has focused on the performance and evaluation of different probability distributions (such as GEV, Gumbel, Lognormal) for flood frequency estimation. _b_ is a constant, typically set to 0.4.'],
                  ['edf_adamowski', 'EDF Adamowski', 'P=(m-0.25)/(n+0.5)', '1981', 'The Adamowski formula in hydrology refers to a specific plotting position formula used for estimating the non-parametric empirical distribution of hydrological events (like flood peaks) to calculate their return periods. This formula provides an alternative to traditional parametric methods (like the Gumbel or Log Pearson Type III distributions). ']
                 ])
def pdist_empirical(dfx, edf, x):
    dfx['empirical_dist'] = edf
    if edf == 'edf_california':  # Year 1923
        dfx['empirical'] = dfx['m'] / len(dfx[x])
    elif edf == 'edf_hazen':  # Year 1930
        dfx['empirical'] = (dfx['m']-0.5) / len(dfx[x])
    elif edf == 'edf_weibull':  # Year 1939
        dfx['empirical'] = dfx['m'] / (len(dfx[x]) + 1)
    elif edf == 'edf_beard':  # Year 1943
        dfx['empirical'] = (dfx['m']-0.31) / (len(dfx[x])+0.38)
    elif edf == 'edf_chegodayev':  # Year 1955
        dfx['empirical'] = (dfx['m']-0.3) / (len(dfx[x])+0.4)
    elif edf == 'edf_blom':  # Year 1958
        dfx['empirical'] = (dfx['m']-0.375) / (len(dfx[x]) + 0.25)
    elif edf == 'edf_tukey':  # Year 1962
        dfx['empirical'] = (3*dfx['m']-1) / (3*len(dfx[x]) + 1)
    elif edf == 'edf_gringorten':  # Year 1963
        dfx['empirical'] = (dfx['m']-0.44) / (len(dfx[x]) + 0.12)
    elif edf == 'edf_jenkinson':  # Year 1977
        dfx['empirical'] = (dfx['m']-0.31) / (len(dfx[x]) + 0.38)
    elif edf == 'edf_cunnane':  # Year 1978
        dfx['empirical'] = (dfx['m']-0.4) / (len(dfx[x]) + 0.2)
    elif edf == 'edf_adamowski':  # Year 1981
        dfx['empirical'] = (dfx['m']-0.25) / (len(dfx[x]) + 0.5)
    else:
        dfx['empirical'] = dfx['m'] / len(dfx[x])  # California
    dfx['empirical_tr'] = 1 / (1-dfx['empirical'])


# Fitting test Kolmogorov
def fTestKolmogorov(dfx, p_dist, idk, emp, vDeltaKolmogorov):  # Kolmogorov-Smirnov fit test
    print('Processing Kolmogorov for: %s...' % p_dist)
    dfp = pd.DataFrame()
    dfp['dfp'] = abs(dfx['empirical']-dfx[p_dist])
    dfp = dfp.sort_values(by='dfp', ascending=[False])
    dfp = dfp.reset_index(drop=True)
    #print(f'\n\nDataset dfp for Kolmogorov: {emp} vs. {p_dist}\n{dfp.to_markdown()}')  ################ <<<<<<<<<<<<<<<<<<<<<<<< Check
    n = len(dfp)
    if (n < 35):
        deltao = 0.000003848186*n**4-0.00033109622*n**3+0.010220554*n**2-0.141035449935*n+1.07518805168
    else:
        deltao = 1.36/math.sqrt(n)
    delta = dfp['dfp'][0]
    if (deltao > delta):
        fit, operator = 1, '>'
    else:
        fit, operator = 0, '<='
    vDeltaKolmogorov['empirical_dist'][idk] = emp
    vDeltaKolmogorov['p_dist'][idk] = p_dist
    vDeltaKolmogorov['delta'][idk] = delta
    vDeltaKolmogorov['deltao'][idk] = deltao
    vDeltaKolmogorov['eval'][idk] = 'Δo %s Δ' % operator
    vDeltaKolmogorov['fit'][idk] = fit
    #print(f'\n\nFinal vDeltaKolmogorov: {emp} vs. {p_dist}\n{vDeltaKolmogorov.to_markdown()}') ################################


# Gumbel distribution Yn parameter calculation
def gumbel_yn(n):
    su = 0
    for m in range(1, n+1):
        ym = -np.log(-np.log((n + 1 - m) / (n + 1)))
        su = su + ym
    mi = su / n
    return mi


# Gumbel distribution Sn parameter calculation
def gumbel_sn(n, mi):
    su = 0
    for m in range (1, n+1):
        ym = -np.log(-np.log((n + 1 - m) / (n + 1)))
        su = su + (ym - mi) ** 2
    mi = su / n
    mi2 = mi ** 0.5
    return mi2


# Probability distribution: Gumbel
def pdist_gumbel(dfx, x, ddof, low_extreme, df_tr, station_code, vDeltaKolmogorov):
    print('Processing CDF: zzgumbel...')  # Only for console
    n = len(dfx[x])
    yn = gumbel_yn(n)
    sn = gumbel_sn(n, yn)
    scale = math.sqrt(6) * dfx[x].std(ddof=ddof) / math.pi
    loc = dfx[x].mean() - yn / scale
    dfx['zzgumbel'] = np.exp(-np.exp(-(dfx[x] - loc) / scale))  ## zzgumbel: zz used to put this manual distribution at the end of the tables
    if low_extreme:
        x_extreme = loc - np.log(-np.log(1 / df_tr.tr)) * scale
    else:
        x_extreme = loc - np.log(-np.log(1 - 1 / df_tr.tr)) * scale
    df_tr['zzgumbel'] = x_extreme
    dfx['gumbel_pdf'] = 0  # <<<<<<<<<<<<<<<<<< pdf not calculated
    vDeltaKolmogorovData = [station_code, '', '', 0.0, 0.0, '', '', n, loc, scale, yn, sn, '', '']
    vDeltaKolmogorov.loc[len(vDeltaKolmogorov)] = vDeltaKolmogorovData  # Add the results as a new record


# Probability distribution: Log-Gumbel
def pdist_loggumbel(dfx, x, low_extreme, df_tr, station_code, vDeltaKolmogorov):
    print('Processing CDF: zzloggumbel...')  # Only for console
    n = len(dfx[x])
    yn = gumbel_yn(n)
    sn = gumbel_sn(n, yn)
    scale = math.sqrt(6) * np.std(np.log(dfx[x])) / math.pi
    loc = np.mean(np.log(dfx[x])) - yn * scale
    dfx['zzloggumbel'] = np.exp(-np.exp(-(np.log(dfx[x]) - loc) / scale))  ## zzloggumbel: zz used to put this manual distribution at the end of the tables
    if low_extreme:
        x_extreme = np.exp(loc - np.log(-np.log(1 / df_tr.tr)) * scale)
    else:
        x_extreme = np.exp(loc - np.log(-np.log(1 - 1 / df_tr.tr)) * scale)
    df_tr['zzloggumbel'] = x_extreme
    dfx['loggumbel_pdf'] = 0  # <<<<<<<<<<<<<<<<<< pdf not calculated
    vDeltaKolmogorovData = [station_code, '', '', 0.0, 0.0, '', '', n, loc, scale, yn, sn, '', '']
    vDeltaKolmogorov.loc[len(vDeltaKolmogorov)] = vDeltaKolmogorovData  # Add the results as a new record


# Function for print and show results in a log file
def print_log(file_log, txt_print, on_screen=True, center_div=False):
    # div50 is use for show 2 plots in the same line
    if on_screen:
        print(txt_print)
    if center_div:
        file_log.write('\n<div align="center">\n' + '\n')
    file_log.write(txt_print)
    if center_div:
        file_log.write('\n\n</div>\n' + '\n')


# Location map with GeoPandas
def location_map(point_latitude, point_longitude, station):
    shapefile_location = gpd.read_file('dataset/ColombiaState.shp')
    point_location = Point(point_longitude, point_latitude)
    point_gdf = gpd.GeoDataFrame(geometry=[point_location], crs=shapefile_location.crs)
    fig, ax = plt.subplots(figsize=(6, 7))  # Adjust figure size as needed
    shapefile_location.plot(ax=ax, color='lightgrey', edgecolor='black', linewidth=0.75)
    point_gdf.plot(ax=ax, marker='o', color='black', markersize=40)  # color='black', 'marker' and 'markersize' customize the point
    ax.set_title("Station location")
    plt.xlabel("Longitude°")
    plt.ylabel("Latitude°")
    ax.annotate(
        text= station,
        xy=(point_longitude, point_latitude),
        xytext=(6, 6),  # Offset the text slightly (e.g., 5 points right, 5 points up)
        textcoords="offset points",
        fontsize=10,
        color='white',
        bbox=dict(boxstyle='round', facecolor='black', alpha=0.9, pad=0.25)
    )
    return plt
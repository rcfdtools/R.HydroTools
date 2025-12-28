# -*- coding: UTF-8 -*-
# Tested with: Python 3.10, SciPy 1.11.3, NumPy 1.26.1, Pandas 2.1.3

# General libraries
import warnings
import math
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


# SciPy probability distributions libraries
# l_pdist_scipy requires: ([Distribution function, parameters, fit method, label, active)]
l_pdist_scipy = ([['gumbel_l', 2, 'MM', 'Gumbel Left Skew', False],
                  ['gumbel_r', 2, 'MM', 'Gumbel Right Skew', False],
                  ['norm', 2, 'MM', 'Normal', True],
                  ['lognorm', 3, 'MLE', 'Log Normal', True],
                  ['foldnorm', 3, 'MM', 'Fold Normal', False],  # Check: not for rain data
                  ['halfnorm', 2, 'MM', 'Half Normal', False],
                  ['gennorm', 3, 'MLE', 'Generalized Normal', False],
                  ['norminvgauss', 4, 'MLE', 'Normal Inverse Gaussian', False],
                  ['powernorm', 3, 'MLE', 'Power normal', False],
                  ['powerlognorm', 4, 'MLE', 'Power log-normal', False],
                  ['skewnorm', 3, 'MLE', 'Skew normal', True],
                  ['truncnorm', 4,'MLE', 'Truncated normal', False],
                  ['pearson3', 3, 'MM', 'Pearson type III', True],
                  ['genextreme', 3, 'MLE', 'Generalized exponential', False],
                  ['alpha', 3, 'MLE', 'Alpha', False],
                  ['anglit', 2, 'MM', 'Anglit', False],
                  ['arcsine', 2, 'MM', 'Arcsine', False],
                  ['argus', 3, 'MLE', 'Argus', False],
                  ['beta', 4, 'MLE', 'Beta', True],
                  ['betaprime', 4, 'MLE', 'Beta prime', False],
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
                  ['crystalball', 4, 'MLE', 'Crystalball', False],
                  ['gamma', 3, 'MLE', 'Gamma', True],
                  ['dgamma', 3, 'MLE', 'Double gamma', False],
                  ['gengamma', 4, 'MLE', 'Generalized gamma', False],
                  ['invgamma', 3, 'MLE', 'Inverted gamma', False],
                  ['loggamma', 3, 'MLE', 'Log gamma', False],
                  ['expon', 2, 'MLE', 'Exponential', False],
                  ['genexpon', 5, 'MLE', 'Generalized exponential', False],
                  ['exponnorm', 3, 'MLE', 'Exponentially modified Normal', False],
                  ['exponweib', 4, 'MLE', 'Exponentiated Weibull', False],
                  ['exponpow', 3, 'MLE', 'Exponential power', False],
                  ['erlang', 3, 'MLE', 'Erlang', False],  # Check: integer value alert
                  ['fatiguelife', 3, 'MLE', 'Fatigue-life (Birnbaum-Saunders)', False],
                  ['truncexpon', 3, 'MLE', 'Truncated exponential', False],
                  ['f', 4, 'MLE', 'F', True],
                  ['fisk', 3, 'MLE', 'Fisk', False],
                  ['genlogistic', 3, 'MLE', 'Generalized logistic', False],
                  ['gausshyper', 6, 'MLE', 'Gauss hypergeometric', True],
                  ['genhalflogistic', 3, 'MLE', 'Generalized half-logistic', False],
                  ['genhyperbolic', 5, 'MLE', 'Generalized hyperbolic', False],
                  ['geninvgauss', 4, 'MLE', 'Generalized Inverse Gaussian', False],
                  ['gibrat', 2, 'MM', 'Gibrat', False],
                  ['gompertz', 3, 'MLE', 'Gompertz (or truncated Gumbel)', False],
                  ['halflogistic', 2, 'MM', 'Half-logistic', False],
                  ['halfgennorm', 3, 'MLE', 'Upper half of a generalized normal', False],
                  ['hypsecant', 2, 'MM', 'hyperbolic secant', False],
                  ['invgauss', 3, 'MLE', 'Inverse Gaussian', True],
                  ['invweibull', 3, 'MLE', 'Inverted Weibull', False],
                  ['johnsonsb', 4, 'MLE', 'Johnson SB', False],
                  ['johnsonsu', 4, 'MLE', 'Johnson Su', False],
                  ['kappa4', 4, 'MLE', 'Kappa 4', False],
                  ['kappa3', 3, 'MLE', 'Kappa 3', False],
                  ['ksone', 3, 'MLE', 'Kolmogorov-Smirnov one-sided test statistic distribution', False],
                  ['kstwo', 3, 'MLE', 'Kolmogorov-Smirnov two-sided test statistic distribution', False],  # Check: zero division, don't use
                  ['kstwobign', 2, 'MLE', 'Limiting distribution of scaled Kolmogorov-Smirnov two-sided test statistic', False],
                  ['laplace', 2, 'MM', 'Laplace', False],
                  ['laplace_asymmetric', 3, 'MLE', 'Asymmetric Laplace', False],
                  ['loglaplace', 3, 'MLE', 'Log-Laplace', False],
                  ['levy', 2, 'MLE', 'Levy', False],
                  ['levy_l', 2, 'MLE', 'Left-skewed Levy', False],
                  ['levy_stable', 4, 'MLE', 'Levy-stable', False],
                  ['logistic', 2, 'MM', 'Logistic (or Sech-squared)', False],
                  ['maxwell', 2, 'MM', 'Maxwell', False],
                  ['mielke', 4, 'MLE', 'Mielke Beta-Kappa / Dagum', False],
                  ['moyal', 2, 'MM', 'Moyal', False],
                  ['nakagami', 3, 'MLE', 'Nakagami', False],
                  ['ncx2', 4, 'MLE', 'Non-central chi-squared', False],
                  ['ncf', 5, 'MLE', 'Non-central F distribution', False],
                  ['nct', 4, 'MLE', 'Non-central Student’s t', False],
                  ['pareto', 3, 'MLE', 'Pareto', False],
                  ['genpareto', 3, 'MLE', 'Generalized Pareto', False],
                  ['truncpareto', 4, 'MLE', 'Upper truncated Pareto', False],
                  ['lomax', 3, 'MLE', 'Lomax (Pareto of the second kind)', False],
                  ['powerlaw', 3, 'MLE', 'Power-function', False],
                  ['rdist', 3, 'MLE', 'R-distributed (symmetric beta)', False],
                  ['rayleigh', 2, 'MM', 'Rayleigh', False],
                  ['rel_breitwigner', 3, 'MLE', 'Relativistic Breit-Wigner', False],
                  ['rice', 3, 'MLE', 'Rice', False],
                  ['recipinvgauss', 3, 'MLE', 'Reciprocal inverse Gaussian', False],
                  ['semicircular', 2, 'MM', 'Semicircular', False],
                  ['studentized_range', 4, 'MLE', 'Studentized range', False],  # Check: don't converge
                  ['t', 3, 'MLE', 'Student’s t', False],
                  ['trapezoid', 4, 'MLE', 'Trapezoid', False],
                  ['triang', 3, 'MLE', 'Triangular', False],
                  ['truncweibull_min', 5, 'MLE', 'Doubly truncated Weibull minimum', False],
                  ['tukeylambda', 3, 'MLE', 'Tukey-Lamdba', False],
                  ['uniform', 2, 'MLE', 'Uniform', False],
                  ['loguniform', 4, 'MLE', 'Log-Uniform or reciprocal', False],
                  ['vonmises', 3, 'MLE', 'Von Mises', False],  # Check: values out of range
                  ['vonmises_line', 3, 'MLE', 'Von Mises line', False],
                  ['wald', 2, 'MM', 'Wald', False],
                  ['weibull_min', 3, 'MLE', 'Weibull minimum', False],
                  ['weibull_max', 3, 'MLE', 'Weibull maximum', False],  # Check: not for rain data
                  ['dweibull', 3, 'MLE', 'Double Weibull', False]
                  ])
# Load libraries only for active distributions
for i in l_pdist_scipy:
    if i[4]:
        exec('from scipy.stats import %s' %i[0])


def fTestKolmogorov(dfx, f_dist, loc, scale, shape, shape1, shape2, shape3):  # Kolmogorov-Smirnov fit test
    dfp = pd.DataFrame()
    dfp['dfp'] = abs(dfx['emp_weibull']-dfx[f_dist])
    dfp = dfp.sort_values(by='dfp', ascending=[False])
    dfp = dfp.reset_index(drop=True)
    n = len(dfp)
    if (n < 35):
        deltao = 0.000003848186*n**4-0.00033109622*n**3+0.010220554*n**2-0.141035449935*n+1.07518805168
    else:
        deltao = 1.36/math.sqrt(n)
    delta = dfp['dfp'][0]
    if (deltao > delta):
        fit, operator = 'fit', '>'
    else:
        fit, operator = 'doesn’t fit', '<='
    eval = 'Δo %s Δ, %s' % (operator, fit)
    vDeltaKolmogorovData = [station_name, f_dist, delta, deltao, eval, loc, scale, shape, shape1, shape2, shape3]
    vDeltaKolmogorov.loc[len(vDeltaKolmogorov)] = vDeltaKolmogorovData

def pdist_weibull(dfx):  # Probability distribution: Weibull (empírica)
    dfx['emp_weibull'] = dfx['oid'] / (len(dfx[x])+1)


def gumbel_yn(n):  # Gumbel Yn parameter
    su = 0
    for m in range(1, n+1):
        ym = -np.log(-np.log((n + 1 - m) / (n + 1)))
        su = su + ym
    mi = su / n
    return mi


def gumbel_sn(n, mi):  # Gumbel Sn parameter
    su = 0
    for m in range (1, n+1):
        ym = -np.log(-np.log((n + 1 - m) / (n + 1)))
        su = su + (ym - mi) ** 2
    mi = su / n
    mi2 = mi ** 0.5
    return mi2


def pdist_gumbel(dfx):  # Probability distribution: Gumbel
    n = len(dfx[x])
    yn = gumbel_yn(n)
    sn = gumbel_sn(n, yn)
    scale = math.sqrt(6) * dfx[x].std(ddof=ddof) / math.pi
    loc = dfx[x].mean() - yn / scale
    #print('* Gumbel distribution (gumbel) >> Yn: %f, Sn: %f, Loc: %f, Scale: %f' % (yn, sn, loc, scale))
    dfx['gumbel'] = np.exp(-np.exp(-(dfx[x] - loc) / scale))
    fTestKolmogorov(dfx, 'gumbel', loc, scale, yn, sn, '', '')


def pdist_loggumbel(dfx):  # Probability distribution: Log-Gumbel
    n = len(dfx[x])
    yn = gumbel_yn(n)
    sn = gumbel_sn(n, yn)
    scale = math.sqrt(6) * np.std(np.log(dfx[x])) / math.pi
    loc = np.mean(np.log(dfx[x])) - yn * scale
    #print('* Log Gumbel distribution (loggumbel) >> Yn: %f, Sn: %f, Loc: %f, Scale: %f' % (yn, sn, loc, scale))
    dfx['loggumbel'] = np.exp(-np.exp(-(np.log(dfx[x]) - loc) / scale))
    fTestKolmogorov(dfx, 'loggumbel', loc, scale, yn, sn, '', '')


def pdist_scipy(dfx, p_dist, n_parameter, fit_method, p_dist_tag):
    # dfx: dataset to eval
    # p_dist: probability distribution function name in SciPy
    # n_parameter: # parameters required
    # fit_method: parameter estimation method. (MLE) Maximum likelihood method or (MM) L-moments
    # p_dist_tag: probability distribution label for reports
    n_parameter = eval(p_dist).numargs + 2  # + 2 means loc and scale
    if n_parameter == 2:
        loc, scale = eval(p_dist).fit(dfx[x], method=fit_method)
        #print('* %s (%s) >> Loc: %f, Scale: %f' % (p_dist_tag, p_dist, loc, scale))
        dfx[p_dist] = eval(p_dist).cdf(dfx[x], loc, scale)  # Cumulative distribution function
        shape, shape1, shape2, shape3 = '', '', '', ''
        frozen_dist = eval(p_dist)(loc=loc, scale=scale)  # Frozen distribution
        if low_extreme:
            x_extreme = frozen_dist.ppf(1 / df_tr.tr)
        else:
            x_extreme = frozen_dist.ppf(1 - 1 / df_tr.tr)
        df_tr[p_dist] = x_extreme
    elif n_parameter == 3:
        shape, loc, scale = eval(p_dist).fit(dfx[x], method=fit_method)
        #print('* %s (%s) >> Shape: %f, Loc: %f, Scale: %f' % (p_dist_tag, p_dist, shape, loc, scale))
        dfx[p_dist] = eval(p_dist).cdf(dfx[x], shape, loc, scale)  # Cumulative distribution function
        shape1, shape2, shape3 = '', '', ''
        frozen_dist = eval(p_dist)(shape, loc=loc, scale=scale)  # Frozen distribution
        if low_extreme:
            x_extreme = frozen_dist.ppf(1 / df_tr.tr)
        else:
            x_extreme = frozen_dist.ppf(1 - 1 / df_tr.tr)
        df_tr[p_dist] = x_extreme
    elif n_parameter == 4:
        shape, shape1, loc, scale = eval(p_dist).fit(dfx[x], method=fit_method)
        #print('* %s (%s) >> Shape: %f, Shape 1: %f, Loc: %f, Scale: %f' % (p_dist_tag, p_dist, shape, shape1, loc, scale))
        dfx[p_dist] = eval(p_dist).cdf(dfx[x], shape, shape1, loc, scale)  # Cumulative distribution function
        shape2, shape3 = '', ''
        frozen_dist = eval(p_dist)(shape, shape1, loc=loc, scale=scale)  # Frozen distribution
        if low_extreme:
            x_extreme = frozen_dist.ppf(1 / df_tr.tr)
        else:
            x_extreme = frozen_dist.ppf(1 - 1 / df_tr.tr)
        df_tr[p_dist] = x_extreme
    elif n_parameter == 5:
        shape, shape1, shape2, loc, scale = eval(p_dist).fit(dfx[x], method=fit_method)
        #print('* %s (%s) >> Shape: %f, Shape 1: %f, Shape 2: %f, Loc: %f, Scale: %f' % (p_dist_tag, p_dist, shape, shape1, shape2, loc, scale))
        dfx[p_dist] = eval(p_dist).cdf(dfx[x], shape, shape1, shape2, loc, scale)  # Cumulative distribution function
        shape3 = ''
        frozen_dist = eval(p_dist)(shape, shape1, shape2, loc=loc, scale=scale)  # Frozen distribution
        if low_extreme:
            x_extreme = frozen_dist.ppf(1 / df_tr.tr)
        else:
            x_extreme = frozen_dist.ppf(1 - 1 / df_tr.tr)
        df_tr[p_dist] = x_extreme
    elif n_parameter == 6:
        shape, shape1, shape2, shape3, loc, scale = eval(p_dist).fit(dfx[x], method=fit_method)
        #print('* %s (%s) >> Shape: %f, Shape 1: %f, Shape 2: %f, Shape 3: %f, Loc: %f, Scale: %f' % (p_dist_tag, p_dist, shape, shape1, shape2, shape3, loc, scale))
        dfx[p_dist] = eval(p_dist).cdf(dfx[x], shape, shape1, shape2, shape3, loc, scale)  # Cumulative distribution function
        frozen_dist = eval(p_dist)(shape, shape1, shape2, shape3, loc=loc, scale=scale)  # Frozen distribution
        if low_extreme:
            x_extreme = frozen_dist.ppf(1 / df_tr.tr)
        else:
            x_extreme = frozen_dist.ppf(1 - 1 / df_tr.tr)
        df_tr[p_dist] = x_extreme
    else:
        print('%s\n* Error: check the # parameters entered...')
    fTestKolmogorov(dfx, p_dist, loc, scale, shape, shape1, shape2, shape3)


# General setup
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
parameter_name = 'rain'  # rain, flow
parameter_units = '($mm/d$)'  # ($mm/d$), ($m^3/s$)
show_plot = True  # Show plot on screen
show_warnings = True  # Show warnings on screen
low_extreme = True  # Eval low extreme values, if False, evaluates high extreme values
if not show_warnings: warnings.filterwarnings('ignore')
ddof = 1  # Standard deviation normalized
x = 'Valor'  # Initial value column name to eval from .csv station file
date = 'Fecha'  # Initial value column name from .csv station file
# Periodos de retorno y probabilidades
tr = [2, 2.33, 5, 10, 15, 20, 25, 50, 75, 100, 200, 250, 500, 750, 1000]  # Tr, return period in years
df_tr = pd.DataFrame(tr, columns=['tr'])
n_tr = len(df_tr)
df_tr['prob_l'] = 1-1/df_tr.tr  # P≤, Probability less than, for high extreme values
df_tr['prob_g'] = 1/df_tr.tr  # P≥, Probability greater than, for low extreme values
vDeltaKolmogorov = pd.DataFrame(columns=['station', 'p_dist', 'delta', 'deltao', 'eval', 'loc', 'scale', 'shape', 'shape1', 'shape2', 'shape3'])
df_l_pdist_scipy = pd.DataFrame(l_pdist_scipy, columns=['p_dist', 'n_parameter', 'fit_method', 'label', 'active'])


# Execution
input_path = 'station/'  # Your local input file folder
station_file = input_path + 'ideam_rain_25020230_ahoc.csv'
station_name = Path(station_file).stem
print('## Station: %s' %station_name)
df_tr['station'] = station_name
df = pd.read_csv(station_file, delimiter=',', index_col=0, parse_dates=True)
df = df.dropna()
# Plot x values
plt.plot(df)
plt.xlabel("Year")
plt.ylabel(parameter_name + ' ' +  parameter_units)
if show_plot: plt.show()
df = df.sort_values(by=x)
df = df.reset_index(drop=True)
df['station'] = station_name
df['oid'] = df.index+1
df = df.rename(columns={x: 'x', date: 'date'})
x = 'x'  # New value column name
date = 'date'  # New date column name
print('\n### Basic stats\n\n* n: %d\n* mean: %f\n* std(%d): %f\n* min: %f\n* max: %f' % (df[x].count(), df[x].mean(), ddof, df[x].std(ddof=ddof), df[x].min(), df[x].max()))
print('\n\n### Probability distributions')
print('\nActive distributions from SciPy (%d of %d available)\n\n%s' % (len(df_l_pdist_scipy.query('active == True')), len(df_l_pdist_scipy), df_l_pdist_scipy.query('active == True')))
print('\n> Gumbel and Lob-Gumbel probability distributions are not shown in the above table.')
pdist_weibull(df)
pdist_gumbel(df)
pdist_loggumbel(df)
dp_evalated = 3
for i in l_pdist_scipy:
    if i[4]:
        dp_evalated += 1
        pdist_scipy(df, i[0], i[1], i[2], i[3])
vDeltaKolmogorov['best_fit'] = np.where((vDeltaKolmogorov['delta'] == vDeltaKolmogorov['delta'].min()), 1, 0)
vDeltaKolmogorov = vDeltaKolmogorov.sort_values(by=['delta'], ascending=True)
vDeltaKolmogorov = vDeltaKolmogorov.reset_index(drop=True)
print('\nCumulative distribution values - CDF (%d evalated, ordered by x ascend) \n\n%s' %(dp_evalated, df))
print('\nParameters & Kolmogorov-Smirnov fit test (sorted by Δ)\n\n%s' % vDeltaKolmogorov)
dp_best = vDeltaKolmogorov[vDeltaKolmogorov.best_fit == 1]
dp_best = dp_best.reset_index(drop=True)
print('\nBest fit for\n\n%s' %dp_best)

# Plot empirical vs. all
plt.scatter(df[x], df['emp_weibull'], color='black', facecolors='black', s=14, label='Empirical')
for i in range(0, len(vDeltaKolmogorov)):
    dp = vDeltaKolmogorov['p_dist'][i]
    delta = vDeltaKolmogorov['delta'][i]
    plt.plot(df[x], df[dp], lw=1, marker='o', markersize=2, label='%s (Δ: %f)' %(dp, delta))
plt.title("Cumulative distribution function CDF")
plt.xlabel(parameter_name + ' ' + parameter_units)
plt.ylabel('CDF')
plt.legend(loc='best', frameon=False)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.1)
if show_plot: plt.show()

# Plot empirical vs. best fit
plt.scatter(df[x], df['emp_weibull'], color='black', facecolors='black', s=14, label='Empirical')
plt.plot(df[x], df[dp_best['p_dist'][0]], 'red', lw=1, marker='o', markersize=2, label='%s (Δ: %f)' %(dp_best['p_dist'][0], dp_best['delta'][0]))
plt.title("Cumulative distribution function CDF - Best fit")
plt.xlabel(parameter_name + ' ' + parameter_units)
plt.ylabel('CDF')
plt.legend(loc='best', frameon=False)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.1)
if show_plot: plt.show()

print('\n\n### Estimate extreme values for specific return periods\n')

print(df_tr)

#print(df.to_csv(index=False))
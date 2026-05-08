# -*- coding: UTF-8 -*-
# Tested with: Python 3.10, SciPy 1.11.3, NumPy 1.26.1, Pandas 2.1.3

import math
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from scipy.stats import anglit
from scipy.stats import arcsine
from scipy.stats import argus
from scipy.stats import cosine
from scipy.stats import erlang
from scipy.stats import norm
from scipy.stats import lognorm
from scipy.stats import pearson3
from scipy.stats import gumbel_r
from scipy.stats import gumbel_l
from scipy.stats import genextreme
from scipy.stats import alpha
from scipy.stats import beta
from scipy.stats import betaprime
from scipy.stats import bradford
from scipy.stats import burr
from scipy.stats import burr12
from scipy.stats import cauchy
from scipy.stats import chi2
from scipy.stats import crystalball
from scipy.stats import gamma
from scipy.stats import dgamma
from scipy.stats import invgamma
from scipy.stats import dweibull
from scipy.stats import expon
from scipy.stats import genexpon
from scipy.stats import exponnorm
from scipy.stats import exponweib
from scipy.stats import exponpow
from scipy.stats import fatiguelife
from scipy.stats import f
from scipy.stats import fisk
from scipy.stats import foldcauchy
from scipy.stats import foldnorm
from scipy.stats import genlogistic
from scipy.stats import gennorm
from scipy.stats import genpareto
from scipy.stats import gausshyper
from scipy.stats import gengamma
from scipy.stats import genhalflogistic
from scipy.stats import genhyperbolic
from scipy.stats import geninvgauss
from scipy.stats import gibrat
from scipy.stats import gompertz
from scipy.stats import halfcauchy
from scipy.stats import halflogistic
from scipy.stats import halfnorm
from scipy.stats import halfgennorm
from scipy.stats import hypsecant
from scipy.stats import invgauss
from scipy.stats import invweibull
from scipy.stats import johnsonsb
from scipy.stats import johnsonsu
from scipy.stats import kappa4
from scipy.stats import kappa3
from scipy.stats import ksone
from scipy.stats import kstwo
from scipy.stats import kstwobign
from scipy.stats import laplace
from scipy.stats import laplace_asymmetric
from scipy.stats import levy
from scipy.stats import levy_l
from scipy.stats import levy_stable
from scipy.stats import logistic
from scipy.stats import loggamma
from scipy.stats import loglaplace
from scipy.stats import loguniform
from scipy.stats import lomax
from scipy.stats import maxwell
from scipy.stats import mielke
from scipy.stats import moyal
from scipy.stats import nakagami
from scipy.stats import ncx2
from scipy.stats import ncf
from scipy.stats import nct
from scipy.stats import norminvgauss
from scipy.stats import pareto
from scipy.stats import powerlaw
from scipy.stats import powerlognorm
from scipy.stats import powernorm
from scipy.stats import rdist
from scipy.stats import rayleigh
from scipy.stats import rel_breitwigner
from scipy.stats import rice
from scipy.stats import recipinvgauss
from scipy.stats import semicircular
from scipy.stats import skewcauchy
from scipy.stats import skewnorm
from scipy.stats import studentized_range
from scipy.stats import t
from scipy.stats import trapezoid
from scipy.stats import triang
from scipy.stats import truncexpon
from scipy.stats import truncnorm
from scipy.stats import truncpareto
from scipy.stats import truncweibull_min
from scipy.stats import tukeylambda
from scipy.stats import uniform
from scipy.stats import vonmises
from scipy.stats import vonmises_line
from scipy.stats import wald
from scipy.stats import weibull_min
from scipy.stats import weibull_max
from scipy.stats import wrapcauchy


def fTestKolmogorov(x, F_Dist):  # Kolmogorov-Smirnov fit test
    dFP = pd.DataFrame()
    dFP['dFP'] = abs(x['weibull']-x[F_Dist])
    dFP = dFP.sort_values(by='dFP', ascending=[False])
    dFP = dFP.reset_index(drop=True)
    n = len(dFP)
    if (n < 35):
        deltao = 0.000003848186*n**4-0.00033109622*n**3+0.010220554*n**2-0.141035449935*n+1.07518805168
    else:
        deltao = 1.36/math.sqrt(n)
    delta = dFP['dFP'][0]
    if (deltao > delta):
        fit, operator = 'fit', '>'
    else:
        fit, operator = 'doesn’t fit', '<='
    eval = 'Δo %s Δ, %s' % (operator, fit)
    vDeltaKolmogorovData = [station_name, F_Dist, delta, deltao, eval]
    vDeltaKolmogorov.loc[len(vDeltaKolmogorov)] = vDeltaKolmogorovData

def pdist_weibull(x):  # Probability distribution: Weibull (empírica)
    x['weibull'] = x['OID'] / (len(x[station_name])+1)


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


def pdist_gumbel(x):  # Probability distribution: Gumbel
    n = len(x[station_name])
    yn = gumbel_yn(n)
    sn = gumbel_sn(n, yn)
    print()
    scale = math.sqrt(6) * x[station_name].std(ddof=ddof)/math.pi
    loc = x[station_name].mean() - yn/scale
    print('* Gumbel distribution (gumbel) >> Yn: %f, Sn: %f, Loc: %f, Scale: %f' % (yn, sn, loc, scale))
    x['gumbel'] = np.exp(-np.exp(-(x[station_name] - loc) / scale))
    fTestKolmogorov(x, 'gumbel')


def pdist_loggumbel(x):  # Probability distribution: Log-Gumbel
    n = len(x[station_name])
    yn = gumbel_yn(n)
    sn = gumbel_sn(n, yn)
    scale = math.sqrt(6)*np.std(np.log(x[station_name]))/math.pi
    loc = np.mean(np.log(x[station_name])) - yn * scale
    print('* Log Gumbel distribution (loggumbel) >> Yn: %f, Sn: %f, Loc: %f, Scale: %f' % (yn, sn, loc, scale))
    x['loggumbel'] = np.exp(-np.exp(-(np.log(x[station_name])-loc)/scale))
    fTestKolmogorov(x, 'loggumbel')


def pdist_scipy(x, p_dist, n_parameter, fit_method, p_dist_tag):
    # x: dataset to eval
    # p_dist: probability distribution function name in SciPy
    # n_parameter: # parameters required
    # fit_method: parameter estimation method. (MLE) Maximum likelihood method or (MM) L-moments
    # p_dist_tag: probability distribution label for reports
    if n_parameter == 2:
        loc, scale = eval(p_dist).fit(x[station_name], method=fit_method)
        print('* %s (%s) >> Loc: %f, Scale: %f' % (p_dist_tag, p_dist, loc, scale))
        x[p_dist] = eval(p_dist).cdf(x[station_name], loc, scale)  # Cumulative distribution function
    elif n_parameter == 3:
        shape, loc, scale = eval(p_dist).fit(x[station_name], method=fit_method)
        print('* %s (%s) >> Shape: %f, Loc: %f, Scale: %f' % (p_dist_tag, p_dist, shape, loc, scale))
        x[p_dist] = eval(p_dist).cdf(x[station_name], shape, loc, scale)  # Cumulative distribution function
    elif n_parameter == 4:
        shape, shape1, loc, scale = eval(p_dist).fit(x[station_name], method=fit_method)
        print('* %s (%s) >> Shape: %f, Shape 1: %f, Loc: %f, Scale: %f' % (p_dist_tag, p_dist, shape, shape1, loc, scale))
        x[p_dist] = eval(p_dist).cdf(x[station_name], shape, shape1, loc, scale)  # Cumulative distribution function
    elif n_parameter == 5:
        shape, shape1, shape2, loc, scale = eval(p_dist).fit(x[station_name], method=fit_method)
        print('* %s (%s) >> Shape: %f, Shape 1: %f, Shape 2: %f, Loc: %f, Scale: %f' % (p_dist_tag, p_dist, shape, shape1, shape2, loc, scale))
        x[p_dist] = eval(p_dist).cdf(x[station_name], shape, shape1, shape2, loc, scale)  # Cumulative distribution function
    elif n_parameter == 6:
        shape, shape1, shape2, shape3, loc, scale = eval(p_dist).fit(x[station_name], method=fit_method)
        print('* %s (%s) >> Shape: %f, Shape 1: %f, Shape 2: %f, Shape 3: %f, Loc: %f, Scale: %f' % (p_dist_tag, p_dist, shape, shape1, shape2, shape3, loc, scale))
        x[p_dist] = eval(p_dist).cdf(x[station_name], shape, shape1, shape2, shape3, loc, scale)  # Cumulative distribution function
    else:
        print('%s\n* Error: check the # parameters entered...')
    fTestKolmogorov(x, p_dist)


# General
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
input_path = 'station/'  # Your local input file folder
station_file = input_path + '25020230.csv'
station_name = Path(station_file).stem
# l_pdist_scipy requires: ([Distribution, parameters, fit method, label, active)]
l_pdist_scipy = ([['gumbel_l', 2, 'MM', 'Gumbel Left Skew', False],
                  ['gumbel_r', 2, 'MM', 'Gumbel Right Skew', False],
                  ['norm', 2, 'MM', 'Normal', True],
                  ['lognorm', 3, 'MLE', 'Log Normal', True],
                  ['foldnorm', 3, 'MM', 'Fold Normal', False],
                  ['halfnorm', 2, 'MM', 'Half Normal', False],
                  ['gennorm', 3, 'MLE', 'Generalized Normal', False],
                  ['norminvgauss', 4, 'MLE', 'Normal Inverse Gaussian', False],
                  ['powernorm', 3, 'MLE', 'Power normal', False],
                  ['powerlognorm', 4, 'MLE', 'Power log-normal', False],
                  ['skewnorm', 3, 'MLE', 'Skew normal', skewnorm],
                  ['truncnorm', 4,'MLE', 'Truncated normal', False],
                  ['pearson3', 3, 'MM', 'Pearson type III', True],
                  ['genextreme', 3, 'MLE', 'Generalized exponential', False],
                  ['alpha', 3, 'MLE', 'Alpha', False],
                  ['anglit', 2, 'MM', 'Anglit', False],
                  ['arcsine', 2, 'MM', 'Arcsine', False],
                  ['argus', 3, 'MLE', 'Argus', False],
                  ['beta', 4, 'MLE', 'Beta', True],
                  ['betaprime', 4, 'MLE', 'Beta prime', False],
                  ['bradford ', 3, 'MLE', 'Bradford', False],
                  ['burr', 4, 'MLE', 'Burr (Type III)', False],
                  ['burr12', 4, 'MLE', 'Burr (Type III) 12', False],
                  ['cauchy', 2, 'MLE', 'Cauchy', False],
                  ['cosine', 2, 'MLE', 'Cosine', False],
                  ['halfcauchy', 2, 'MLE', 'Half-Cauchy', False],
                  ['foldcauchy ', 3, 'MLE', 'Fold Cauchy', False],
                  ['skewcauchy ', 3, 'MLE', 'Skewed Cauchy', False],
                  ['wrapcauchy ', 3, 'MLE', 'Wrapped  Cauchy', False],
                  ['chi2', 3, 'MLE', 'Chi²', chi2],
                  ['crystalball', 4, 'MLE', 'Crystalball', False],
                  ['gamma', 3, 'MLE', 'Gamma', True],
                  ['dgamma', 3, 'MLE', 'Double gamma', False],
                  ['gengamma', 4, 'MLE', 'Generalized gamma', True],
                  ['invgamma', 3, 'MLE', 'Inverted gamma', False],
                  ['loggamma', 3, 'MLE', 'Log gamma', False],
                  ['expon', 2, 'MLE', 'Exponential', False],
                  ['genexpon ', 5, 'MLE', 'Generalized exponential', False],
                  ['exponnorm', 3, 'MLE', 'Exponentially modified Normal', False],
                  ['exponweib', 4, 'MLE', 'Exponentiated Weibull', False],
                  ['exponpow', 3, 'MLE', 'Exponential power', False],
                  ['erlang', 3, 'MLE', 'Erlang', False],  # Check: integer value alert
                  ['fatiguelife', 3, 'MLE', 'Fatigue-life (Birnbaum-Saunders)', False],
                  ['truncexpon', 3, 'MLE', 'Truncated exponential', False],
                  ['f', 4, 'MLE', 'F', True],
                  ['fisk', 3, 'MLE', 'Fisk', False],
                  ['genlogistic', 3, 'MLE', 'Generalized logistic', False],
                  ['gausshyper ', 6, 'MLE', 'Gauss hypergeometric', True],
                  ['genhalflogistic ', 3, 'MLE', 'Generalized half-logistic', False],
                  ['genhyperbolic ', 5, 'MLE', 'Generalized hyperbolic', False],
                  ['geninvgauss ', 4, 'MLE', 'Generalized Inverse Gaussian', False],
                  ['gibrat ', 2, 'MM', 'Gibrat', False],
                  ['gompertz ', 3, 'MLE', 'Gompertz (or truncated Gumbel)', False],
                  ['halflogistic ', 2, 'MM', 'Half-logistic', False],
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
                  ['truncpareto', 4, 'MLE', 'Upper truncated Pareto ', False],
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
                  ['triang', 3, 'MLE', 'Triangular ', False],
                  ['truncweibull_min', 5, 'MLE', 'Doubly truncated Weibull minimum', False],
                  ['tukeylambda', 3, 'MLE', 'Tukey-Lamdba', False],
                  ['uniform', 2, 'MLE', 'Uniform', False],
                  ['loguniform', 4, 'MLE', 'Log-Uniform or reciprocal', False],
                  ['vonmises', 3, 'MLE', 'Von Mises', False],  # Check: values out of range
                  ['vonmises_line', 3, 'MLE', 'Von Mises line', False],
                  ['wald', 2, 'MM', 'Wald', False],
                  ['weibull_min', 3, 'MLE', 'Weibull minimum', False],
                  ['weibull_max', 3, 'MLE', 'Weibull maximum', False],
                  ['dweibull', 3, 'MLE', 'Double Weibull', False]
                  ])
print('## Station: %s' %station_name)
ddof = 1  # Standard deviation normalized
vDeltaKolmogorov = pd.DataFrame(columns=['Station', 'Dp', 'Delta', 'Deltao', 'Eval'])
DNMR = pd.DataFrame(columns=['DNMR'])
df = pd.read_csv(station_file, delimiter=',')
df = df.dropna()
df = df.sort_values(by=station_name)
df = df.reset_index(drop=True)
df['OID'] = df.index+1
print('\n### Basic stats\n\n* n: %d\n* mean: %f\n* std(%d): %f\n* min: %f\n* max: %f' % (df[station_name].count(), df[station_name].mean(), ddof, df[station_name].std(ddof=ddof), df[station_name].min(), df[station_name].max()))
print('\n\n### Probability distributions')
pdist_weibull(df)
pdist_gumbel(df)
pdist_loggumbel(df)
dp_evalated = 3
for i in l_pdist_scipy:
    #print(i[0])
    if i[4]:
        dp_evalated += 1
        pdist_scipy(df, i[0], i[1], i[2], i[3])
vDeltaKolmogorov['BestFit'] = np.where((vDeltaKolmogorov['Delta'] == vDeltaKolmogorov['Delta'].min()), 'True', 'False')
print('\n\n### Cumulative distribution values - CDF (%d evalated) \n\n %s' %(dp_evalated, df))
print('\n\n### Kolmogorov-Smirnov fit test - Δ values\n\n%s' % vDeltaKolmogorov)
dp_best = vDeltaKolmogorov[vDeltaKolmogorov.BestFit == 'True']
dp_best = dp_best.reset_index(drop=True)
print('\nBest fit for\n\n%s' %dp_best)

# Plot empirical vs. all
plt.scatter(df[station_name], df['weibull'], color = 'black', facecolors='none', s=14, label='Empirical')
for i in range(0, len(vDeltaKolmogorov)):
    dp = vDeltaKolmogorov['Dp'][i]
    delta = vDeltaKolmogorov['Delta'][i]
    plt.plot(df[station_name], df[dp], lw=1, marker='.', markersize=4, label='%s (Δ: %f)' %(dp, delta))
plt.xlabel('Rain ($mm/d$)')
plt.ylabel('CDF')
plt.legend(loc='best', frameon=False)
plt.show()

# Plot empirical vs. best fit
plt.scatter(df[station_name], df['weibull'], color = 'black', facecolors='none', s=14, label='Empirical CDF')
plt.plot(df[station_name], df[dp_best['Dp']], 'red', lw=1, marker='.', markersize=4, label='Estimated CDF - Best fit (%s)' % dp_best['Dp'][0])
plt.xlabel('Rain ($mm/d$)')
plt.ylabel('CDF')
plt.legend(loc='best', frameon=False)
plt.show()

#print(df.to_csv(index=False))
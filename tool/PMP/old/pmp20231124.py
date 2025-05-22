# -*- coding: UTF-8 -*-
# Tested with: Python 3.10, SciPy 1.11.3, NumPy 1.26.1, Pandas 2.1.3

# General libraries
import warnings
import math
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import tabulate  # required for print tables in Markdown using pandas


# SciPy probability distributions libraries
# l_pdist_scipy requires: ([Distribution function, parameters, fit method, label, active)]
l_pdist_scipy = ([['gumbel_l', 2, 'MM', 'Gumbel Left Skew', True],
                  ['gumbel_r', 2, 'MM', 'Gumbel Right Skew', True],
                  ['norm', 2, 'MM', 'Normal', True],
                  ['lognorm', 3, 'MLE', 'Log Normal', True],
                  ['foldnorm', 3, 'MM', 'Fold Normal', True],  # Check: not for rain data
                  ['halfnorm', 2, 'MM', 'Half Normal', True],
                  ['gennorm', 3, 'MLE', 'Generalized Normal', True],
                  ['norminvgauss', 4, 'MLE', 'Normal Inverse Gaussian', False],
                  ['powernorm', 3, 'MLE', 'Power normal', False],
                  ['powerlognorm', 4, 'MLE', 'Power log-normal', False],
                  ['skewnorm', 3, 'MLE', 'Skew normal', True],
                  ['truncnorm', 4,'MLE', 'Truncated normal', True],
                  ['pearson3', 3, 'MM', 'Pearson type III', True],
                  ['genextreme', 3, 'MLE', 'Generalized exponential', False],
                  ['alpha', 3, 'MLE', 'Alpha', True],
                  ['anglit', 2, 'MM', 'Anglit', True],
                  ['arcsine', 2, 'MM', 'Arcsine', True],
                  ['argus', 3, 'MLE', 'Argus', True],
                  ['beta', 4, 'MLE', 'Beta', True],
                  ['betaprime', 4, 'MLE', 'Beta prime', True],
                  ['bradford', 3, 'MLE', 'Bradford', True],
                  ['burr', 4, 'MLE', 'Burr (Type III)', True],
                  ['burr12', 4, 'MLE', 'Burr (Type III) 12', False],
                  ['cauchy', 2, 'MLE', 'Cauchy', False],
                  ['cosine', 2, 'MLE', 'Cosine', True],
                  ['halfcauchy', 2, 'MLE', 'Half-Cauchy', False],
                  ['foldcauchy', 3, 'MLE', 'Fold Cauchy', False],
                  ['skewcauchy', 3, 'MLE', 'Skewed Cauchy', False],
                  ['wrapcauchy', 3, 'MLE', 'Wrapped  Cauchy', True],
                  ['chi2', 3, 'MLE', 'Chi²', True],
                  ['crystalball', 4, 'MLE', 'Crystalball', True],
                  ['gamma', 3, 'MLE', 'Gamma', True],
                  ['dgamma', 3, 'MLE', 'Double gamma', True],
                  ['gengamma', 4, 'MLE', 'Generalized gamma', True],
                  ['invgamma', 3, 'MLE', 'Inverted gamma', True],
                  ['loggamma', 3, 'MLE', 'Log gamma', True],
                  ['expon', 2, 'MLE', 'Exponential', True],
                  ['genexpon', 5, 'MLE', 'Generalized exponential', True],
                  ['exponnorm', 3, 'MLE', 'Exponentially modified Normal', True],
                  ['exponweib', 4, 'MLE', 'Exponentiated Weibull', True],
                  ['exponpow', 3, 'MLE', 'Exponential power', True],
                  ['erlang', 3, 'MLE', 'Erlang', False],  # Check: integer value alert
                  ['fatiguelife', 3, 'MLE', 'Fatigue-life (Birnbaum-Saunders)', True],
                  ['truncexpon', 3, 'MLE', 'Truncated exponential', True],
                  ['f', 4, 'MLE', 'F', True],
                  ['fisk', 3, 'MLE', 'Fisk', True],
                  ['genlogistic', 3, 'MLE', 'Generalized logistic', True],
                  ['gausshyper', 6, 'MLE', 'Gauss hypergeometric', True],
                  ['genhalflogistic', 3, 'MLE', 'Generalized half-logistic', True],
                  ['genhyperbolic', 5, 'MLE', 'Generalized hyperbolic', False],
                  ['geninvgauss', 4, 'MLE', 'Generalized Inverse Gaussian', True],
                  ['gibrat', 2, 'MM', 'Gibrat', True],
                  ['gompertz', 3, 'MLE', 'Gompertz (or truncated Gumbel)', True],
                  ['halflogistic', 2, 'MM', 'Half-logistic', True],
                  ['halfgennorm', 3, 'MLE', 'Upper half of a generalized normal', False],
                  ['hypsecant', 2, 'MM', 'hyperbolic secant', True],
                  ['invgauss', 3, 'MLE', 'Inverse Gaussian', True],
                  ['invweibull', 3, 'MLE', 'Inverted Weibull', True],
                  ['johnsonsb', 4, 'MLE', 'Johnson SB', True],
                  ['johnsonsu', 4, 'MLE', 'Johnson Su', True],
                  ['kappa4', 4, 'MLE', 'Kappa 4', True],
                  ['kappa3', 3, 'MLE', 'Kappa 3', True],
                  ['ksone', 3, 'MLE', 'Kolmogorov-Smirnov one-sided test statistic distribution', True],
                  ['kstwo', 3, 'MLE', 'Kolmogorov-Smirnov two-sided test statistic distribution', False],  # Check: zero division, don't use
                  ['kstwobign', 2, 'MLE', 'Limiting distribution of scaled Kolmogorov-Smirnov two-sided test statistic', True],
                  ['laplace', 2, 'MM', 'Laplace', True],
                  ['laplace_asymmetric', 3, 'MLE', 'Asymmetric Laplace', True],
                  ['loglaplace', 3, 'MLE', 'Log-Laplace', True],
                  ['levy', 2, 'MLE', 'Levy', False],
                  ['levy_l', 2, 'MLE', 'Left-skewed Levy', True],
                  ['levy_stable', 4, 'MLE', 'Levy-stable', True],
                  ['logistic', 2, 'MM', 'Logistic (or Sech-squared)', True],
                  ['maxwell', 2, 'MM', 'Maxwell', True],
                  ['mielke', 4, 'MLE', 'Mielke Beta-Kappa / Dagum', True],
                  ['moyal', 2, 'MM', 'Moyal', True],
                  ['nakagami', 3, 'MLE', 'Nakagami', True],
                  ['ncx2', 4, 'MLE', 'Non-central chi-squared', True],
                  ['ncf', 5, 'MLE', 'Non-central F distribution', True],
                  ['nct', 4, 'MLE', 'Non-central Student’s t', True],
                  ['pareto', 3, 'MLE', 'Pareto', True],
                  ['genpareto', 3, 'MLE', 'Generalized Pareto', True],
                  ['truncpareto', 4, 'MLE', 'Upper truncated Pareto', True],
                  ['lomax', 3, 'MLE', 'Lomax (Pareto of the second kind)', True],
                  ['powerlaw', 3, 'MLE', 'Power-function', True],
                  ['rdist', 3, 'MLE', 'R-distributed (symmetric beta)', True],
                  ['rayleigh', 2, 'MM', 'Rayleigh', True],
                  ['rel_breitwigner', 3, 'MLE', 'Relativistic Breit-Wigner', False],
                  ['rice', 3, 'MLE', 'Rice', True],
                  ['recipinvgauss', 3, 'MLE', 'Reciprocal inverse Gaussian', True],
                  ['semicircular', 2, 'MM', 'Semicircular', True],
                  ['studentized_range', 4, 'MLE', 'Studentized range', False],  # Check: don't converge
                  ['t', 3, 'MLE', 'Student’s t', True],
                  ['trapezoid', 4, 'MLE', 'Trapezoid', True],
                  ['triang', 3, 'MLE', 'Triangular', True],
                  ['truncweibull_min', 5, 'MLE', 'Doubly truncated Weibull minimum', True],
                  ['tukeylambda', 3, 'MLE', 'Tukey-Lamdba', True],
                  ['uniform', 2, 'MLE', 'Uniform', True],
                  ['loguniform', 4, 'MLE', 'Log-Uniform or reciprocal', True],
                  ['vonmises', 3, 'MLE', 'Von Mises', False],  # Check: values out of range
                  ['vonmises_line', 3, 'MLE', 'Von Mises line', True],
                  ['wald', 2, 'MM', 'Wald', True],
                  ['weibull_min', 3, 'MLE', 'Weibull minimum', True],
                  ['weibull_max', 3, 'MLE', 'Weibull maximum', False],  # Check: not for rain data
                  ['dweibull', 3, 'MLE', 'Double Weibull', True]
                  ])
# Load libraries only for active distributions
for i in l_pdist_scipy:
    if i[4]:
        exec('from scipy.stats import %s' %i[0])


def fTestKolmogorov(dfx, f_dist, idk):  # Kolmogorov-Smirnov fit test
    print('Processing Kolmogorov for: %s...' % f_dist)
    dfp = pd.DataFrame()
    dfp['dfp'] = abs(dfx['empirical']-dfx[f_dist])
    dfp = dfp.sort_values(by='dfp', ascending=[False])
    dfp = dfp.reset_index(drop=True)
    n = len(dfp)
    if (n < 35):
        deltao = 0.000003848186*n**4-0.00033109622*n**3+0.010220554*n**2-0.141035449935*n+1.07518805168
    else:
        deltao = 1.36/math.sqrt(n)
    delta = dfp['dfp'][0]
    if (deltao > delta):
        fit, fit_txt, operator = 1, 'fit', '>'
    else:
        fit, fit_txt, operator = 0, 'doesn’t fit', '<='
    vDeltaKolmogorov['empirical_dist'][idk] = emp
    vDeltaKolmogorov['p_dist'][idk] = f_dist
    vDeltaKolmogorov['delta'][idk] = delta
    vDeltaKolmogorov['deltao'][idk] = deltao
    vDeltaKolmogorov['eval'][idk] = 'Δo %s Δ, %s' % (operator, fit_txt)
    vDeltaKolmogorov['fit'][idk] = fit


emp_dist = ['emp_california', 'emp_hazen', 'emp_weibull', 'emp_beard', 'emp_chegodayev', 'emp_blom', 'emp_tukey', 'emp_gringorten', 'emp_jenkinson', 'emp_cunnane', 'emp_adamowski']
def pdist_empirical(dfx, emp):
    dfx['empirical_dist'] = emp
    if emp == 'emp_california':  # 1923
        dfx['empirical'] = dfx['m'] / len(dfx[x])
    elif emp == 'emp_hazen':  # Year 1930
        dfx['empirical'] = (dfx['m']-0.5) / len(dfx[x])
    elif emp == 'emp_weibull':  # Year 1939
        dfx['empirical'] = dfx['m'] / (len(dfx[x]) + 1)
    elif emp == 'emp_beard':  # Year 1943
        dfx['empirical'] = (dfx['m']-0.31) / (len(dfx[x])+0.38)
    elif emp == 'emp_chegodayev':  # Year 1955
        dfx['empirical'] = (dfx['m']-0.3) / (len(dfx[x])+0.4)
    elif emp == 'emp_blom':  # Year 1958
        dfx['empirical'] = (dfx['m']-0.375) / (len(dfx[x]) + 0.25)
    elif emp == 'emp_tukey':  # Year 1962
        dfx['empirical'] = (3*dfx['m']-1) / (3*len(dfx[x]) + 1)
    elif emp == 'emp_gringorten':  # Year 1963
        dfx['empirical'] = (dfx['m']-0.44) / (len(dfx[x]) + 0.12)
    elif emp == 'emp_jenkinson':  # Year 1977
        dfx['empirical'] = (dfx['m']-0.31) / (len(dfx[x]) + 0.38)
    elif emp == 'emp_cunnane':  # Year 1978
        dfx['empirical'] = (dfx['m']-0.4) / (len(dfx[x]) + 0.2)
    elif emp == 'emp_adamowski':  # Year 1981
        dfx['empirical'] = (dfx['m']-0.25) / (len(dfx[x]) + 0.5)
    else:
        dfx['empirical'] = dfx['m'] / len(dfx[x])  # California
    dfx['empirical_tr'] = 1 / (1-dfx['empirical'])


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
    vDeltaKolmogorovData = [station_name, '', '', 0.0, 0.0, '', '', n, loc, scale, yn, sn, '', '']
    vDeltaKolmogorov.loc[len(vDeltaKolmogorov)] = vDeltaKolmogorovData  # Add the results as a new record


def pdist_loggumbel(dfx):  # Probability distribution: Log-Gumbel
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
    vDeltaKolmogorovData = [station_name, '', '', 0.0, 0.0, '', '', n, loc, scale, yn, sn, '', '']
    vDeltaKolmogorov.loc[len(vDeltaKolmogorov)] = vDeltaKolmogorovData  # Add the results as a new record


def pdist_scipy(dfx, p_dist, n_parameter, fit_method, p_dist_tag):
    # dfx: dataset to eval
    # p_dist: probability distribution function name in SciPy
    # n_parameter: # parameters required
    # fit_method: parameter estimation method. (MLE) Maximum likelihood method or (MM) L-moments
    # p_dist_tag: probability distribution label for reports
    n = len(dfx)
    n_parameter = eval(p_dist).numargs + 2  # + 2 means loc and scale
    if n_parameter == 2:
        loc, scale = eval(p_dist).fit(dfx[x], method=fit_method)
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
        dfx[p_dist] = eval(p_dist).cdf(dfx[x], shape, shape1, shape2, shape3, loc, scale)  # Cumulative distribution function
        frozen_dist = eval(p_dist)(shape, shape1, shape2, shape3, loc=loc, scale=scale)  # Frozen distribution
        if low_extreme:
            x_extreme = frozen_dist.ppf(1 / df_tr.tr)
        else:
            x_extreme = frozen_dist.ppf(1 - 1 / df_tr.tr)
        df_tr[p_dist] = x_extreme
    else:
        print('%s\n* Error: check the # parameters entered...')
    dfx[p_dist+'_pdf'] =  frozen_dist.pdf(dfx.x)
    vDeltaKolmogorovData = [station_name, '', '', 0.0, 0.0, '', '', n, loc, scale, shape, shape1, shape2,shape3]
    vDeltaKolmogorov.loc[len(vDeltaKolmogorov)] = vDeltaKolmogorovData  # Add the results as a new record


# General setup
parameter_name = 'rain'  # rain, flow
parameter_units = '($mm/d$)'  # ($mm/d$), ($m^3/s$)
create_plot = True  # Creates and print plots
show_plot = True  # Show plot on screen
plot_only_fit = True  # Plot only fit distributions with Δo > Δ
color_line_plot = 'green'
show_warnings = False  # Show warnings on screen
low_extreme = False  # Eval low extreme values, if False, evaluates high extreme values
pdist_gumbel_on = True  # Activate the Gumbel distribution
pdist_loggumbel_on = True  # Activate the Log-Gumbel distribution
if not show_warnings: warnings.filterwarnings('ignore')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
plot_legend_ncol = 4  # Columns on the legend
ddof = 1  # Standard deviation normalized
x_label = 'Valor'  # Initial value column name to eval from .csv station file
date_label = 'Fecha'  # Initial value column name from .csv station file
# Periodos de retorno y probabilidades
tr = [2, 2.33, 5, 10, 15, 20, 25, 50, 75, 100, 200, 250, 500, 750, 1000]  # Tr, return period in years
df_tr = pd.DataFrame(tr, columns=['tr'])
n_tr = len(df_tr)
df_tr['prob_l'] = 1-1/df_tr.tr  # P≤, Probability less than, for high extreme values
df_tr['prob_g'] = 1/df_tr.tr  # P≥, Probability greater than, for low extreme values
df_l_pdist_scipy = pd.DataFrame(l_pdist_scipy, columns=['p_dist', 'n_parameter', 'fit_method', 'label', 'active'])
df_l_pdist_scipy['reference'] = '[Help](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.'+df_l_pdist_scipy.p_dist+'.html)'
df_l_pdist_scipy.index.name = 'id'
df_l_pdist_scipy = df_l_pdist_scipy.query('active == True')
df_l_pdist_scipy = df_l_pdist_scipy.sort_values(by=['p_dist'], ascending=True)
df_l_pdist_scipy = df_l_pdist_scipy.reset_index(drop=True)


# Execution
input_path = 'dataset/pmax24h_in/'  # Your local input file folder
station_file = input_path + '25020230AHOC.csv'
station_name = Path(station_file).stem  # File name without extension
#df_in = pd.read_csv(station_file, delimiter=',', parse_dates=True)  # index_col=0
df = pd.read_csv(station_file, delimiter=',', parse_dates=True)  # index_col=0
print('## Station: %s' %station_name)
# Plot x values - Start
if create_plot:
    df = df.sort_values(by=date_label)
    plt.plot(df[date_label], df[x_label], color=color_line_plot, lw=2, marker='o', markersize=3, )
    plt.grid(color='gray', linestyle='--', linewidth=0.1)
    plt.title('$_{Station: %s}$\nData serie' % station_name)  #$_{ } for underscript text
    plt.xlabel('Year')
    plt.ylabel(parameter_name + ' ' + parameter_units)
    plt.xticks(rotation=25, ha='right')
    if show_plot: plt.show()
x = x_label
date = date_label
df = df.dropna()
df = df.sort_values(by=x, ascending=True)
df = df.reset_index(drop=True)
df.index.name = 'id'
df['station'] = station_name
df['m'] = df.index+1
df = df.rename(columns={x: 'x', date: 'date'})
x = 'x'  # New value column name
date = 'date'  # New date column name
#print('\n### Basic stats\n\n* n: %d\n* mean: %f\n* std(%d): %f\n* min: %f\n* max: %f' % (df[x].count(), df[x].mean(), ddof, df[x].std(ddof=ddof), df[x].min(), df[x].max()))
print('\n### Active distributions from SciPy (%d of %d available)\n\n%s' % (len(df_l_pdist_scipy.query('active == True')), len(l_pdist_scipy), df_l_pdist_scipy.query('active == True').to_markdown()))
print('\n> Gumbel and Lob-Gumbel probability distributions are not shown in the above table.\n> n_parameter = # arguments & localization & scale.\n> Fit methods: (MLE) maximum likelihood, (MM) L-moments.')
print('\n\n### Probability distributions\n')
vDeltaKolmogorov = pd.DataFrame(columns=['station', 'empirical_dist', 'p_dist', 'delta', 'deltao', 'eval', 'fit', 'n', 'loc', 'scale', 'shape', 'shape1', 'shape2', 'shape3'])

# CDF calculations
dp_evalated = 2  # 2 means we are including Gumbel & Log Gumbel
for i in range(0, len(df_l_pdist_scipy)):
    print('Processing CDF: %s...' % df_l_pdist_scipy['p_dist'][i])  # Only for console
    dp_evalated += 1
    pdist_scipy(df, df_l_pdist_scipy['p_dist'][i], df_l_pdist_scipy['n_parameter'][i], df_l_pdist_scipy['fit_method'][i], df_l_pdist_scipy['label'][i])
if pdist_gumbel_on: pdist_gumbel(df)
if pdist_loggumbel_on: pdist_loggumbel(df)

# Evaluation for each empirical distribution
for emp in emp_dist:
    print('\n\n#### Empirical: %s\n' % emp)

    # Return periods & empirical values
    df_tr['empirical_dist '] = emp
    df_tr['station'] = station_name
    df_tr['n'] = len(df)
    df_tr['risk_rate'] = 1-(1-1/df_tr['tr'])**df_tr['tr']
    pdist_empirical(df, emp)

    # Kolmogorov-Smirnov test & best fit
    idk = 0
    for i in df_l_pdist_scipy['p_dist']:
        fTestKolmogorov(df, i, idk)
        idk += 1
    if pdist_gumbel_on: fTestKolmogorov(df, 'zzgumbel', idk)  # Run always after for i in df_l_pdist_scipy['p_dist']
    if pdist_loggumbel_on: fTestKolmogorov(df, 'zzloggumbel', idk+1)  # Run always after for i in df_l_pdist_scipy['p_dist']
    vDeltaKolmogorov['best_fit'] = np.where((vDeltaKolmogorov['delta'] == vDeltaKolmogorov['delta'].min()), 1, 0)
    vDeltaKolmogorov = vDeltaKolmogorov.sort_values(by=['delta'], ascending=True)
    vDeltaKolmogorov = vDeltaKolmogorov.reset_index(drop=True)
    vDeltaKolmogorov.index.name = 'id'
    print('\nCumulative distribution values - CDF (%d evalated, ordered by x ascending) \n\n%s' %(dp_evalated, df.to_markdown()))
    vDeltaKolmogorov['best_fit_sort'] = vDeltaKolmogorov.index+1
    print('\nParameters & Kolmogorov-Smirnov fit test (sorted by Δ)\n\n%s' % vDeltaKolmogorov.to_markdown())
    dp_best = vDeltaKolmogorov[vDeltaKolmogorov.best_fit == 1]
    dp_best = dp_best.reset_index(drop=True)
    dp_best.index.name = 'id'
    print('\nBest fit for\n\n%s' %dp_best.to_markdown())

    # Plot analysis graphs
    if create_plot:

        # Plot empirical vs. all
        plt.scatter(df[x], df['empirical'], color='black', facecolors='darkgray', s=24, label='%s (Δo: %f)' % (emp, vDeltaKolmogorov['deltao'][0]))
        for i in range(0, len(vDeltaKolmogorov)):
            dp = vDeltaKolmogorov['p_dist'][i]
            delta = vDeltaKolmogorov['delta'][i]
            if plot_only_fit:
                only_fit_txt = ' (only Δo > Δ)'
                if vDeltaKolmogorov['fit'][i] == 1:
                    plt.plot(df[x], df[dp], lw=1, marker='o', markersize=0, alpha=0.75, label='%s (Δ: %f)' %(dp, delta))
            else:
                plt.plot(df[x], df[dp], lw=1, marker='o', markersize=0, alpha=0.75, label='%s (Δ: %f)' %(dp, delta))
                only_fit_txt = ''
        plt.title('$_{Station: %s}$\nCumulative distribution function CDF%s' %(station_name, only_fit_txt))
        plt.xlabel(parameter_name + ' ' + parameter_units)
        plt.ylabel('CDF')
        plt.legend(loc='best', frameon=True, edgecolor='white', framealpha=0.9, ncol=plot_legend_ncol, facecolor='white')
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.1)
        if show_plot: plt.show()

        # Plot empirical vs. best fit
        plt.scatter(df[x], df['empirical'], color='black', facecolors='darkgray', s=24, label='%s (Δo: %f)' %(emp, dp_best['deltao'][0]))
        plt.plot(df[x], df[dp_best['p_dist'][0]], color=color_line_plot, lw=2, marker='o', markersize=0, label='%s (Δ: %f)' %(dp_best['p_dist'][0], dp_best['delta'][0]))
        plt.title('$_{Station: %s}$\nCumulative distribution function CDF (Best fit)' % station_name)
        plt.xlabel(parameter_name + ' ' + parameter_units)
        plt.ylabel('CDF')
        plt.legend(loc='best', frameon=False)
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.1)
        if show_plot: plt.show()

        # Plot Empirical & Estimated PDF - Best Fit
        plt.hist(df.x, density=True, histtype='stepfilled', alpha=0.4, color='gray', label='Empirical %s' % emp)
        plt.plot(df.x, df[dp_best['p_dist'][0]+'_pdf'], 'r-', lw=2, color=color_line_plot, label='Estimated %s' % dp_best['p_dist'][0])
        plt.legend(loc='best', frameon=False)
        plt.title('$_{Station: %s}$\nEmpirical & Estimated PDF (Best fit)' % station_name)
        plt.xlabel(parameter_name + ' ' + parameter_units)
        plt.ylabel('PDF')
        plt.grid(color='gray', linestyle='--', linewidth=0.1)
        if show_plot: plt.show()

        # Plot values over return periods Tr
        for i in range(0, len(vDeltaKolmogorov)):
            dp = vDeltaKolmogorov['p_dist'][i]
            delta = vDeltaKolmogorov['delta'][i]
            if plot_only_fit:
                only_fit_txt = ' (only Δo > Δ)'
                if vDeltaKolmogorov['fit'][i] == 1:
                    plt.plot(df_tr.tr, df_tr[dp], lw=1, marker='o', markersize=0, alpha=0.75, label='%s (Δ: %f)' %(dp, delta))
            else:
                only_fit_txt = ''
                plt.plot(df_tr.tr, df_tr[dp], lw=1, marker='o', markersize=0, alpha=0.75, label='%s (Δ: %f)' % (dp, delta))
        plt.title('$_{Station: %s}$\nExtreme values for specific return periods%s\n(Δo: %f %s)' %(only_fit_txt, station_name, vDeltaKolmogorov['deltao'][0], emp))
        plt.xlabel('Tr ($years$)')
        plt.ylabel(parameter_name + ' ' + parameter_units)
        plt.legend(loc='best', frameon=True, edgecolor='white', framealpha=0.9, ncol=plot_legend_ncol, facecolor='white')
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.1)
        if show_plot: plt.show()

    # Print extreme values table
    vDeltaKolmogorov = vDeltaKolmogorov.sort_values(by=['p_dist'], ascending=True)  # Required for asign the parameters in the right order
    vDeltaKolmogorov = vDeltaKolmogorov.reset_index(drop=True)
    print('\n\nEstimate extreme values for specific return periods\n')
    df_tr.index.name = 'id'
    print(df_tr.to_markdown())

    #print(df.to_csv(index=False))
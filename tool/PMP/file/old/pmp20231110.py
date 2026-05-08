# -*- coding: UTF-8 -*-

import math
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.stats import norm
from scipy.stats import pearson3
from scipy.stats import gumbel_r
from scipy.stats import gumbel_l
from scipy.stats import gamma


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)


#Prueba de bondad de ajuste usando el método de Kolmogorov-Smirnov usando una función
def fTestKolmogorov(x, F_Dist):
    dFP = pd.DataFrame()
    dFP['dFP'] = abs(x['P_E']-x[F_Dist])
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
    print('* Kolmogorov-Smirnov test (Δo > Δ): %f %s %f (distribution %s the empirical curve)' % (deltao, operator, dFP['dFP'][0], fit))
    vDeltaKolmogorovData = [station_name, F_Dist, delta, deltao]
    vDeltaKolmogorov.loc[len(vDeltaKolmogorov)] = vDeltaKolmogorovData


#Función de distribución: Weibull (empírica)
def fDistEmpWeibull(x):
    x['P_E'] = x['OID'] / (len(x[station_name])+1)


# Función de distribución: Gumbel
def fDistGumbel(x):
    print('\nGumbel distribution')
    alph = math.sqrt(6) * x[station_name].std(ddof=ddof)/math.pi
    mu = x[station_name].mean() - 0.57721/alph
    print('* α: %f\n* μ: %f' % (alph ,mu))
    x['F_DGumbel'] = np.exp(-np.exp(-(x[station_name] - mu) / alph))
    fTestKolmogorov(x, 'F_DGumbel')

# Función de distribución: Log-Gumbel
def fDistLogGumbel(x):
    print('\nLog Gumbel distribution')
    alph = math.sqrt(6)*np.std(np.log(x[station_name]))/math.pi
    mu = np.mean(np.log(x[station_name]))-0.57721*alph
    print('* α: %f\n* μ: %f' % (alph, mu))
    x['F_DLogGumbel'] = np.exp(-np.exp(-(np.log(x[station_name])-mu)/alph))
    fTestKolmogorov(x, 'F_DLogGumbel')

def fDistGumbel_r(x):
    print('\nGumbel right skew distribution')
    mu = x[station_name].mean()
    std = x[station_name].std(ddof=ddof)
    print('* μ: %f\n* σ: %f' % (mu, std))
    x['z_score'] = (x[station_name] - mu) / std
    x['F_DGumbel_r'] = gumbel_r.cdf(x['z_score'])  # Cumulative distribution function
    fTestKolmogorov(x, 'F_DGumbel_r')

def fDistGumbel_l(x):
    print('\nGumbel right skew distribution')
    mu = x[station_name].mean()
    std = x[station_name].std(ddof=ddof)
    print('* μ: %f\n* σ: %f' % (mu, std))
    x['z_score'] = (x[station_name] - mu) / std
    x['F_DGumbel_l'] = gumbel_l.cdf(x['z_score'])  # Cumulative distribution function
    fTestKolmogorov(x, 'F_DGumbel_l')


# Función de distribución: Normal
def fDistNormal(x):
    print('\nNormal distribution')
    mu = x[station_name].mean()
    std = x[station_name].std(ddof=ddof)
    print('* μ: %f\n* σ: %f' % (mu, std))
    x['z_score'] = (x[station_name] - mu) / std
    x['F_DNormal'] = norm.cdf(x['z_score'])  # Cumulative distribution function
    fTestKolmogorov(x, 'F_DNormal')


def fDistNormala(x):
    print('\nNormal distribution')
    mu = x[station_name].mean()
    std = x[station_name].std(ddof=ddof)
    print('* μ: %f\n* σ: %f' % (mu, std))
    x['z_score'] = (x[station_name] - mu) / std
    x['F_DNormala'] = norm.cdf(x[station_name], mu, std)  # Cumulative distribution function
    fTestKolmogorov(x, 'F_DNormala')

def fDistLogPearsonIIIa(x):
    print('\nLog-Person III distribution')
    skew = -2
    mean, var, skew, kurt = pearson3.stats(skew, moments='mvsk')
    mu = x[station_name].mean()
    std = x[station_name].std(ddof=ddof)
    print('* μ: %f\n* σ: %f' % (mu, std))
    x['z_score'] = (x[station_name] - mu) / std
    x['F_DLogPearsonIII'] = pearson3.cdf(x['z_score'], skew)  # Cumulative distribution function
    fTestKolmogorov(x, 'F_DLogPearsonIII')


# Función de distribución: Log-Pearson III
def fDistLogPearsonIII(x):
    n = len(x)
    print('\nLog-Person III distribution')
    #print(type(x))
    # Bias to calculating the position parameter
    CSG = n * np.sum((np.log(x[station_name]) - np.mean(np.log(x[station_name]))) ** 3) / ((n - 1) * (n - 2) * np.std(np.log(x[station_name])) ** 3)
    print('* CSG: %f (bias)' % (CSG))
    # Position parameter
    Xo = np.mean(np.log(x[station_name])) - 2 * np.std(np.log(x[station_name])) / CSG
    # Form parameter
    gam = 4 / CSG ** 2
    # Scale Parameter
    Beta = CSG * np.std(np.log(x[station_name]))/2
    print('* Xo: %f (position parameter)\n* γ: %f (form parameter or Gamma)\n* β: %f (scale parameter or Beta)' % (Xo, gam, Beta))
    # Cumulative Distribution Si se cumple con la condición: β > 0
    Lga = gam * (gam + 1)
    vDNMR = [gam]
    DNMR.loc[len(DNMR)] = vDNMR
    for i in range (1, n):
        vDNMR = [Lga]
        DNMR.loc[len(DNMR)] = vDNMR
        Lga = Lga * (gam + i + 1)
    DNMR['OID'] = DNMR.index + 1
    DNMR['LY'] = (np.log(x[station_name]) - Xo) / Beta
    DNMR['NMDR'] = 0
    DNMR['Gy'] = 0
    #print('\nDNMR\n%s' % DNMR)
    for i in range(0, n):
        for j in range(0, n):
            DNMR['NMDR'][j] = DNMR['LY'][i] ** (gam + j)
        if Xo > 0:
            DNMR['Gy'] = np.exp(-DNMR['LY']) * np.sum(DNMR['NMDR']/DNMR['DNMR'])  # <<<<<< check here
    print('\nDNMR\n%s' % DNMR)
    '''
    for (i in 1:n)
    {
        NMDR <- c()
        for (j in 0:(n-1)){
          NMDR[j+1] <- LY[i]**(gam+j)}
          NMDR <<- NMDR
        if (Xo>0){Gy[i] <- (exp(-LY[i])*sum(NMDR/DNMR)/gamma(gam))}
    }; 
    '''

# General
input_path = 'station/'  # Your local input file folder
station_file = input_path + '25020230.csv'
station_name = Path(station_file).stem
print('## Station: %s' %station_name)
ddof = 1  # Standard deviation normalized
vDeltaKolmogorov = pd.DataFrame(columns=['Station', 'Dp', 'Delta', 'Deltao'])
DNMR = pd.DataFrame(columns=['DNMR'])
df = pd.read_csv(station_file, delimiter=',')
df = df.dropna()
df = df.sort_values(by=station_name)
df = df.reset_index(drop=True)
df['OID'] = df.index+1
print('\nBasic stats\n* n: %d\n* mean: %f\n* std(%d): %f\n* min: %f\n* max: %f' % (df[station_name].count(), df[station_name].mean(), ddof, df[station_name].std(ddof=ddof), df[station_name].min(), df[station_name].max()))
fDistEmpWeibull(df)
fDistNormal(df)
fDistNormala(df)
#fDistGumbel(df)
#fDistGumbel_r(df)
#fDistGumbel_l(df)
#fDistLogGumbel(df)
#fDistLogPearsonIIIa(df)
df = df.drop(columns=['z_score'])
print('\n %s' % df)
print('\nKolmogorov-Smirnov Δ values\n%s' % vDeltaKolmogorov)

#print(df.to_csv(index=False))
import numpy as np
import math
from scipy.stats import norm

def normal_dist(x, mean, sd):
    prob_density = (np.pi * sd) * np.exp(-0.5 * ((x - mean) / sd) ** 2)
    return prob_density


def normpdf(x, mean, sd):
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

mean = 105.8007
sd = 38.72746
x = 37.52732
result = normal_dist(x, mean, sd)
print(result)
result = normpdf(x, mean, sd)
print(result)
z_score = (x - mean) / sd
result = norm.cdf(z_score)  # Cumulative distribution function
print(result)
result = (1/(sd*math.sqrt(2*math.pi)))*math.exp(-(x-mean)**2/(2*sd**2))
print(result)
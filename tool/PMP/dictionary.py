# Dictionary definitions
# Author https://github.com/rcfdtools

# General vars description
general_vars = ([['app_version', 'app_version'], # App control version
          ['runtime', 'runtime'],
          ['python_version', 'Python version'],
          ['scipy_version', 'SciPy version'],
          ['pandas_version', 'Pandas version'],
          ['numpy_version', 'NumPy version'],
          ['station_dataset_file', 'Stations dataset (station_dataset_file)'],
          ['station_catalog_file', 'Stations catalog (station_catalog_file)'],
          ['date_min', 'Minimum year to eval til year_max (date_min)'],
          ['date_max', 'Maximum year to eval since year_min (date_max)'],
          ['create_plot', 'Creates, save and include plots into reports (create_plot)'],
          ['plot_only_fit', 'Plot only fit distributions with Δo > Δ (plot_only_fit)'],
          ['low_extreme', 'Eval low extreme values, if False, evaluates high extreme values (low_extreme)'],
          ['pdist_logarithmic_on', 'Eval every SciPy distribution as logarithmic (pdist_logarithmic_on)'],
          ['ddof', 'Standard deviation normalized (ddof)'],
          ['tr', 'Return periods to eval in years (Tr)'],
          ['minimum_sample', 'Minimum data sample per station, 0 means any (minimum_sample)'],
          ['zscore_max', 'Z-Score maximum threshold to adjust a value, 0 means disable (zscore_max)'],
          ['zscore_min', 'Z-Score minimum threshold to adjust a value, 0 means disable (zscore_min)'],
          ['avoid_zeros', 'Avoid zeros, e.g. rain = 0 (avoid_zeros)'],
          ['avoid_nans', 'Avoid null values (avoid_nans)']
         ])


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

                  ['edf_filliben', 'EDF Filliben', 'P=(m-0.3175)/(n+0.365)', '1975', 'The specific values of the constants (0.3175) (often denoted as $alpha$) and (0.365) are derived from a method proposed by James J. Filliben in a 1975 paper. This particular formula is the mean value of the $i$-th order statistic of the normal distribution and is considered a robust and effective plotting position formula for the normal probability plot correlation coefficient test for normality.'],

                  ['edf_jenkinson', 'EDF Jenkinson', 'P=(m-a)/(n+b)', '1977', 'The Jenkinson formula in hydrology is an empirical plotting position formula used to estimate the non-exceedance probability _(P)_ or return period _(T)_ of a given ordered observation within a sample. It is a widely used method in the frequency analysis of extreme events such as floods and rainfall, as it provides a distribution-free way to plot data. _a≈0.31_ and _b≈0.38_ are constants derived to approximate the median of the probability distribution for the given rank.'],

                  ['edf_cunnane', 'EDF Cunnane', 'P=(m-b)/(n+1-2b)', '1978', 'Cunnane´s work in statistical hydrology has focused on the performance and evaluation of different probability distributions (such as GEV, Gumbel, Lognormal) for flood frequency estimation. _b_ is a constant, typically set to 0.4.'],

                  ['edf_adamowski', 'EDF Adamowski', 'P=(m-0.25)/(n+0.5)', '1981', 'The Adamowski formula in hydrology refers to a specific plotting position formula used for estimating the non-parametric empirical distribution of hydrological events (like flood peaks) to calculate their return periods. This formula provides an alternative to traditional parametric methods (like the Gumbel or Log Pearson Type III distributions). ']
                 ])


# General definitions
dicts = {
    'pmp': 'Probable Maximum Precipitation (PMP) is the greatest amount of rainfall for a specific duration that is meteorologically possible for a given location, acting as a "worst-case" scenario for extreme storms, crucial for designing safety-critical infrastructure like bridges, river deviations, dams, spillways, and nuclear plants to prevent catastrophic failure. PMP is calculated by hydrologists using meteorological data to determine the upper limit of extreme rainfall, often leading to the Probable Maximum Flood (PMF) for flood control design, and is increasingly being studied for climate change impacts.',

    'scipy_stats': '[scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) is a Python´s powerful submodule within the SciPy library for comprehensive statistical analysis, offering over 130 probability distributions (like Normal, Poisson), functions for descriptive stats (mean, variance), hypothesis testing (t-tests, chi-square), random variable generation, and statistical tests, making it essential for data science, modeling, and research. It provides tools to explore, model, and draw conclusions from data efficiently, working seamlessly with NumPy.',

    'cpd': 'A continuous probability distribution (CPD) describes probabilities for variables that can take any value within a range (like rain any time), unlike discrete variables with specific outcomes (like temperature). It uses a Probability Density Function (PDF), a curve where the total area under it equals 1, and the probability of the variable falling within an interval (a to b) is found by calculating the area under the curve between those points. A key feature is that the probability of hitting any single exact value is zero, so probabilities are always expressed for ranges, e.g., $P(a ≤ X ≤ b)$.',

    'loc': '**loc** (Location parameter): This shifts the distribution along the x-axis. For many common distributions, like the normal (Gaussian) distribution, loc represents the mean $μ$. For others, like the uniform distribution, it might represent the minimum value, or for the beta distribution, the left end of the support interval.',

    'scale': '**scale** (Scale parameter): This determines the width or spread of the distribution. For the normal distribution, scale represents the standard deviation $σ$. For a uniform distribution, it defines the length of the interval (from $loc$ to $loc + scale$).',

    'shape': '**shape** (Shape parameters): Refers to parameters that define the specific form of a probability distribution, distinct from its location (loc) and scale (scale). These parameters are required arguments for most distribution functions. For example, a normal (Gaussian) distribution is fully defined by its location (mean) and scale (standard deviation), so it has no specific shape parameters beyond loc and scale. However, other distributions have intrinsic properties that need specification, as Gamma distribution that takes a shape parameter, often named $a$ or $alpha$.',

    'edf': 'An Empirical Distribution Function (EDF) is a step-function estimate of a true cumulative distribution function (CDF) based on observed sample data, representing the proportion of data points less than or equal to a given value. It is calculated by ordering your data and jumping up by $1/n$ (where $n$ is sample size) at each unique data point, allowing analysis without assuming an underlying population distribution, and it gets closer to the true CDF as the sample size grows.',

    'tr': 'In hydrology, a return period (or recurrence interval $Tr$) is the statistical average time between extreme events like floods or droughts of a specific magnitude, indicating how rare an event is, with a 100-year flood, for example, having a 1% chance of occurring in any given year, not that it happens exactly every century. It is a key tool for infrastructure design (like bridges or dams) and risk assessment, calculated from historical data to determine the probability of future events, although it is important to remember it is statistical average, and events can cluster or be missed.',

    'cdf': 'Cumulative Distribution Function (CDF), denoted as $F$<sub>$X$</sub>$(x)$, is a function that gives the probability that a random variable $X$ will take a value less than or equal to a specific value, $x$ (i.e., $(P(X≥x)$. It essentially "accumulates" probabilities from a given point up to the far right (positive infinity), providing a complete picture of the distribution´s probabilities for both discrete (like rain) and continuous (like temperature) variables, helping to find probabilities over ranges or above certain values.',

    'ddof': 'Delta Degrees of Freedom (DDOF): is a parameter used in the formulas for calculating variance and standard deviation. When ddof=0, the divisor is $N$ (the total number of observations) and this is used when your data set is the entire population. When ddof=1, the divisor is $N-1$ and this is used when your data set is a sample drawn from a larger population. Using $N-1$ provides an unbiased estimate of the population variance (known as Bessel´s correction).',

    'value_initial': 'The initial value (value_initial) correspond to the initial obtained or null completed value, and value (value) is adjusted only when the initial value is outside the valid range definite through the Z-Score value. If Z-Score is active, values out of range or outliers are replaced with the station mean value',

    'limnimetric': 'Limnimetric stations and rain gauges are distinct instruments, but they often work in tandem at the same monitoring locations. A limnimetric station (or gauging station) is used to measure and record water levels (stage) in open-air waterways such as rivers, lakes, and reservoirs. A rain gauge (also known as a pluviometer or udometer) is a specific instrument used to gather and measure the amount of liquid precipitation over a predefined area. While a limnimetric station itself measures water levels in a body of water, it does not typically contain the internal mechanism to directly record rainfall. Instead, hydrologists commonly install separate rain gauges (pluviometric stations) nearby to collect precipitation data. This allows them to correlate rainfall events with subsequent changes in river or lake levels, which is crucial for flood forecasting and water resource management.',

    'conventional_station': 'Note: In the National Stations Catalog (CNE), multiple stations are currently tagged as Conventional technology despite multiple has been upgrated to Automatics ones.',

    'disclaimer': '**APP DISCLAIMER**: NO WARRANTY - This software is provided by [github.com/rcfdtools](https://github.com/rcfdtools) "as is", without any express or implied warranty, including warranties of merchantability, fitness for a particular purpose, or non-infringement. There is no guarantee that the software will be error-free or operate without interruption. LIMITATION OF LIABILITY - Neither the authors nor copyright holders will be liable for claims or damages arising from the software or its use. You are responsible for determining if the software is appropriate for your use and assume all associated risks, including errors, legal compliance, and data loss. NO PROFESSIONAL ADVICE - The software provides general information and does not offer professional advice. It should not replace consultation with professional advisors.',
}



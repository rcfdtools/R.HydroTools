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
    'study_name': 'Study and analysis of the Probable Maximum Precipitation (PMP) in the network of automatic stations in Colombia - South America and estimation of extreme values for different return periods from multiple probability distributions.',

    'pmp': 'Probable Maximum Precipitation (PMP) is the greatest amount of rainfall for a specific duration that is meteorologically possible for a given location, acting as a "worst-case" scenario for extreme storms, crucial for designing safety-critical infrastructure like bridges, river deviations, dams, spillways, and nuclear plants to prevent catastrophic failure. PMP is calculated by hydrologists using meteorological data to determine the upper limit of extreme rainfall, often leading to the Probable Maximum Flood (PMF) for flood control design, and is increasingly being studied for climate change impacts.',

    'pdf': 'A Probability Density Function (PDF) describes the relative likelihood of a continuous random variable falling within a specific range, where the total area under its curve equals 1, and the area over any interval gives the actual probability for that range. Unlike discrete probabilities (like rolling a die), a PDF shows density, not direct probability for a single point (which is zero), with higher points indicating higher likelihood, often visualized as a bell curve for normal distributions.',

    'log_pdf': 'A log of a probability density function (log-PDF) is simply the logarithm of the PDF´s value, denoted as $log(f(x))$, useful for converting multiplication of probabilities into addition, improving numerical stability with tiny numbers, and connecting to information theory concepts like entropy. Instead of dealing with very small probabilities (e.g., 0.000001), log-PDFs use negative numbers (e.g., $log(0.00001) ≈ -11.51$ that are easier for computers to handle, preventing underflow errors and simplifying complex calculations. In this study, each active probability distribution from SciPy is also evaluated in the $log$ form.',

    'disable_pdf': 'With the only purpose of prevent loops, zero divisions, infinite values, over high estimated values or horizontal trending for recurrence intervals estimations, the follow distributions were disabled.',

    'scipy_stats': '[scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) is a Python´s powerful submodule within the SciPy library for comprehensive statistical analysis, offering over 130 probability distributions (like Normal, Poisson), functions for descriptive stats (mean, variance), hypothesis testing (t-tests, chi-square), random variable generation, and statistical tests, making it essential for data science, modeling, and research. It provides tools to explore, model, and draw conclusions from data efficiently, working seamlessly with NumPy.',

    'cpd': 'A continuous probability distribution (CPD) describes probabilities for variables that can take any value within a range (like rain any time), unlike discrete variables with specific outcomes (like temperature). It uses a Probability Density Function (PDF), a curve where the total area under it equals 1, and the probability of the variable falling within an interval (a to b) is found by calculating the area under the curve between those points. A key feature is that the probability of hitting any single exact value is zero, so probabilities are always expressed for ranges, e.g., $P(a ≤ X ≤ b)$.',

    'loc': '**loc** (Location parameter): This shifts the distribution along the x-axis. For many common distributions, like the normal (Gaussian) distribution, loc represents the mean $μ$. For others, like the uniform distribution, it might represent the minimum value, or for the beta distribution, the left end of the support interval.',

    'scale': '**scale** (Scale parameter): This determines the width or spread of the distribution. For the normal distribution, scale represents the standard deviation $σ$. For a uniform distribution, it defines the length of the interval (from $loc$ to $loc + scale$).',

    'shape': '**shape** (Shape parameters): Refers to parameters that define the specific form of a probability distribution, distinct from its location (loc) and scale (scale). These parameters are required arguments for most distribution functions. For example, a normal (Gaussian) distribution is fully defined by its location (mean) and scale (standard deviation), so it has no specific shape parameters beyond loc and scale. However, other distributions have intrinsic properties that need specification, as Gamma distribution that takes a shape parameter, often named $a$ or $alpha$.',

    'edf': 'An Empirical Distribution Function (EDF) is a step-function estimate of a true cumulative distribution function (CDF) based on observed sample data, representing the proportion of data points less than or equal to a given value. It is calculated by ordering your data and jumping up by $1/n$ (where $n$ is sample size) at each unique data point, allowing analysis without assuming an underlying population distribution, and it gets closer to the true CDF as the sample size grows. For the empirical probability calculations, the parameter $m$ correspond to the order number which means the position of the $x$ values in an ascending order list.',

    'tr': 'In hydrology, a return period (or recurrence interval $Tr$) is the statistical average time between extreme events like floods or droughts of a specific magnitude, indicating how rare an event is, with a 100-year flood, for example, having a 1% chance of occurring in any given year, not that it happens exactly every century. It is a key tool for infrastructure design (like bridges or dams) and risk assessment, calculated from historical data to determine the probability of future events, although it is important to remember it is statistical average, and events can cluster or be missed.',

    'cdf': 'Cumulative Distribution Function (CDF), denoted as $F$<sub>$X$</sub>$(x)$, is a function that gives the probability that a random variable $X$ will take a value less than or equal to a specific value, $x$ (i.e., $(P(X≥x)$. It essentially "accumulates" probabilities from a given point up to the far right (positive infinity), providing a complete picture of the distribution´s probabilities for both discrete (like rain) and continuous (like temperature) variables, helping to find probabilities over ranges or above certain values. Each station is evaluated separately ordering the $x$ values ascending, calculating the CDF and PDF values for the activated distributions and their logarithmic forms.',

    'ddof': 'Delta Degrees of Freedom (DDOF): is a parameter used in the formulas for calculating variance and standard deviation. When ddof=0, the divisor is $N$ (the total number of observations) and this is used when your data set is the entire population. When ddof=1, the divisor is $N-1$ and this is used when your data set is a sample drawn from a larger population. Using $N-1$ provides an unbiased estimate of the population variance (known as Bessel´s correction).',

    'value_initial': 'The initial value (value_initial) correspond to the initial obtained or null completed value, and value (value) is adjusted only when the initial value is outside the valid range definite through the Z-Score value. If Z-Score is active, values out of range or outliers are replaced with the station mean value',

    'bestfit': 'Best fit in probability distribution analysis means finding the theoretical distribution (like Normal, Poisson, Exponential) that most accurately mirrors your real-world data´s patterns (shape, center, spread) for better predictions, using methods like visual checks (Q-Q plots), goodness-of-fit tests (Kolmogorov-Smirnov, Chi-Squared), and information criteria (AIC) to score and select the simplest, most representative model.',

    'label_category': 'Hydrometeorological stations are categorized by their function and automation, including Automatic Weather Stations, Synoptic Stations, and specialized types like River Gauging Stations and Agrometeorological Stations, all combining weather (meteorological) and water (hydrological) monitoring for tasks like flood forecasting, water management, and climate studies. They range from basic manual setups to sophisticated automated networks, measuring precipitation, streamflow, water levels, temperature, humidity, and more.\n\n> Limnimetric stations and rain gauges are distinct instruments, but they often work in tandem at the same monitoring locations. A limnimetric station (or gauging station) is used to measure and record water levels (stage) in open-air waterways such as rivers, lakes, and reservoirs. A rain gauge (also known as a pluviometer or udometer) is a specific instrument used to gather and measure the amount of liquid precipitation over a predefined area. While a limnimetric station itself measures water levels in a body of water, it does not typically contain the internal mechanism to directly record rainfall. Instead, hydrologists commonly install separate rain gauges (pluviometric stations) nearby to collect precipitation data. This allows them to correlate rainfall events with subsequent changes in river or lake levels, which is crucial for flood forecasting and water resource management.',

    'label_technology': 'Hydrometeorological stations use both conventional (manual) and modern (automated/technological) methods to monitor a wide range of weather and water-related parameters, providing data for forecasting, resource management, and disaster preparedness. Conventional methods typically involve manual observations and basic, robust instruments that require human interaction at regular intervals. Modern technology has largely automated data collection, enabling real-time monitoring and data transmission, especially in remote or hazardous environments.\n\n> In the Colombia National Stations Catalog (CNE), multiple stations are currently tagged as Conventional technology despite multiple has been upgraded to Automatic ones.',

    'label_status': 'The status of hydrometeorological stations (active or inactive) is generally maintained at the level of the individual network or data provider and can often be viewed through specific online portals or databases. During inactive periods, stations may not record or report data.',

    'label_state': 'A geographic state refers to a defined territory with a sovereign government, characterized by its physical location, boundaries, shape, size, and relative position, distinguishing it from other political entities like regions or nations. It´s a fundamental unit in political geography, possessing recognized borders, a populace, and governing authority that controls its territory and resources.',

    'label_county': 'A geographic county is a primary local administrative division within a country or state, serving as a fundamental unit for local government, administration and often defined by specific boundaries for services like roads or policing, acting as an intermediate level between large states/provinces and smaller cities or towns.',

    'label_ah': 'A hydrographic area, often called a river basin, watershed, or drainage basin, is a geographic region where all water (from rain, streams, rivers) drains into a common outlet, like a single river, lake, or ocean, defined by its natural boundaries. It encompasses land and water, studying water flow, quality, and distribution for management, navigation, and environmental analysis, covering features from rivers and lakes to surrounding land and seafloor.',

    'label_zh': 'A hydrographic zone is essentially a river basin or watershed: a geographic area where all water (rain, runoff) drains to a common point, like a river, lake, or ocean, defined by its topography and water flow. It´s used in water management and science to study water quantity, quality, and movement, encompassing features like rivers, streams, coastlines, and even the seafloor, crucial for safe navigation and resource planning. Dividing a hydrographic area (drainage basin or watershed) into smaller hydrographic zones is essential for effective water resource management, planning, and analysis. This subdivision allows managers to analyze the behavior of different parts of the water cycle and address specific local issues within a larger system.',

    'label_szh': 'A hydrographic sub-zone, often called a sub-basin or sub-catchment, is a smaller geographical area that channels all its surface runoff to a specific point within a larger river system. It functions as a component of a larger hydrographic basin (watershed). Dividing a large basin into smaller sub-zones allows for more detailed study and management of specific areas. This enables: Modeling hydrological processes (e.g., runoff potential, infiltration capacity), Predicting and managing flood risks, Monitoring pollutants and their transport, Developing specific conservation and land-use plans tailored to local conditions.',

    'hydrometeorological_station': 'A hydrometeorological station is a facility with instruments to measure both weather (meteorological) (temperature, wind, humidity, pressure) and water (hydrological) (river levels, flow, rainfall, soil moisture, water quality) data, providing a comprehensive view of the water cycle for forecasting floods, droughts, managing resources, and supporting agriculture and ecosystems. These stations are crucial for understanding the interaction between water and atmosphere, enabling better decision-making for disaster preparedness and sustainable water management.',

    'station_list': 'The following list contains the stations used in the current study, each one contains an specific detailed report with the probability distributions analysis and the extreme values for different recurrence intervals. Note: some conventional stations may be include in the current analysis.',

    'station_record': 'Number of records (yearly values) founded per station for the probability distributions analysis. The current study, consider as valid any station with at least 8 years of records to include a wide geographic range (keep in mind for specific hydrologic studies, the minimal recommended length has to be at least 10 years, which are necessary to obtain stable storm or flow properties).',

    'disclaimer': '**APP DISCLAIMER**: NO WARRANTY - This software is provided by [github.com/rcfdtools](https://github.com/rcfdtools) "as is", without any express or implied warranty, including warranties of merchantability, fitness for a particular purpose, or non-infringement. There is no guarantee that the software will be error-free or operate without interruption. LIMITATION OF LIABILITY - Neither the authors nor copyright holders will be liable for claims or damages arising from the software or its use. You are responsible for determining if the software is appropriate for your use and assume all associated risks, including errors, legal compliance, and data loss. NO PROFESSIONAL ADVICE - The software provides general information and does not offer professional advice. It should not replace consultation with professional advisors.',
}



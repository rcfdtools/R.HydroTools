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
          ['plot_only_fit', 'Plot only fit distributions with Δo > Δ (plot_only_fit)'],
          ['low_extreme', 'Eval low extreme values, if False, evaluates high extreme values (low_extreme)'],
          ['pdist_logarithmic_on', 'Eval every SciPy distribution as logarithmic (pdist_logarithmic_on)'],
          ['ddof', 'Standard deviation normalized (ddof)'],
          ['tr', 'Return periods to eval in years (Tr)'],
          ['minimum_sample', 'Minimum data sample per station, 0 means any (minimum_sample)'],
          ['zscore', 'Z-Score threshold to adjust a value, 0 means disable (zscore)'],
          ['avoid_zeros', 'Avoid zeros, e.g. rain = 0 (avoid_zeros)'],
          ['avoid_nans', 'Avoid null values (avoid_nans)']
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

    'disclaimer': '**APP DISCLAIMER**: NO WARRANTY - This software is provided by [github.com/rcfdtools](https://github.com/rcfdtools) "as is", without any express or implied warranty, including warranties of merchantability, fitness for a particular purpose, or non-infringement. There is no guarantee that the software will be error-free or operate without interruption. LIMITATION OF LIABILITY - Neither the authors nor copyright holders will be liable for claims or damages arising from the software or its use. You are responsible for determining if the software is appropriate for your use and assume all associated risks, including errors, legal compliance, and data loss. NO PROFESSIONAL ADVICE - The software provides general information and does not offer professional advice. It should not replace consultation with professional advisors.',
}



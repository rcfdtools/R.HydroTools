# Dictionary definitions
# Author https://github.com/rcfdtools

# General vars description in pmp.py
general_vars = ([
                  ['app_version', 'app_version'], # App control version
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
                  ['plot_only_simple', 'Plot only simple graphs avoiding multiple CDFs and multiple Extreme values plots (plot_only_simple)']
               ])


# General definitions
dicts = {
    'study_name': 'RESEARCH: _“Population and Public Services Demand Projections (PPSD)”_',

    'keywords': 'Keywords: `population` `public-service` `projection` `lineal` `polynomial` `logarithmic` `potential` `exponential` `arithmetic` `geometric` `wappaus` `dane` `colombia` `south-america`',

    'census_data': 'Census data are official statistics collected by a government about the people and housing in a country. They usually include counts of total population, age, sex, race, income, education, and jobs.',

    'abosulute_relative_error': 'Relative error puts that difference into context by dividing the absolute error by the true value, creating a unitless ratio or percentage that shows the scale of the mistake.',

    'fresh_water_supply': 'The fresh water supply demand typically ranges from 100 to 300 liters per capita per day (lpcd) for standard domestic and municipal planning, though absolute survival minimums set by the World Health Organization are as low as 7.5 to 20 liters per day, and total consumption in high-income nations can exceed 400 liters.',

    'disclaimer': '**APP DISCLAIMER**: NO WARRANTY - This software is provided by [github.com/rcfdtools](https://github.com/rcfdtools) "as is", without any express or implied warranty, including warranties of merchantability, fitness for a particular purpose, or non-infringement. There is no guarantee that the software will be error-free or operate without interruption. LIMITATION OF LIABILITY - Neither the authors nor copyright holders will be liable for claims or damages arising from the software or its use. You are responsible for determining if the software is appropriate for your use and assume all associated risks, including errors, legal compliance, and data loss. NO PROFESSIONAL ADVICE - The software provides general information and does not offer professional advice. It should not replace consultation with professional advisors.',
}



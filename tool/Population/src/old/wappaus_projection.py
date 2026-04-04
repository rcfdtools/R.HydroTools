def wappaus_projection(p_initial, p_recent, year_initial, year_recent, year_target):
    """
    Calculates population projection using the Wappaus Method.
    
    Args:
        p_initial (int): Population of the first (initial) census.
        p_recent (int): Population of the most recent census.
        year_initial (int): Year of the initial census.
        year_recent (int): Year of the most recent census.
        year_target (int): Year to project the population for.
    """
    # 1. Calculate growth rate (i)
    numerator = 200 * (p_recent - p_initial)
    denominator = (year_recent - year_initial) * (p_initial + p_recent)
    i = numerator / denominator
    
    # 2. Check the applicability condition
    time_diff = year_target - year_initial
    condition_value = i * time_diff
    
    if condition_value >= 200:
        return f"Method not applicable: i * (Tf - Tci) = {condition_value:.2f} (must be < 200)"
    
    # 3. Calculate Future Population (Pf)
    pf = p_initial * ((200 + condition_value) / (200 - condition_value))
    
    return {
        "growth_rate_i": round(i, 4),
        "projected_population": round(pf, 0),
        "target_year": year_target
    }

# Example usage:
# Population in 1990: 10,000; Population in 2010: 15,000; Project for 2030
result = wappaus_projection(10000, 15000, 1990, 2010, 2030)
print(result)
import numpy as np
from evpc.core.general_cost import double_linear_depreciation, calculate_depreciated_value, calculate_maintenance_cost, calculate_insurance_cost



def mean_electricity_cost(cost_per_unit, percentage_distribution):
    """
    Calculate the mean electricity cost based on a distribution of costs and usage percentages.

    Parameters
    ----------
    cost_per_unit : array_like
        Array of electricity costs per unit (e.g., per kWh) for different time periods or providers.
    percentage_distribution : array_like
        Corresponding percentage distribution of usage for each cost per unit.

    Returns
    -------
    mean_cost : float
        The weighted mean electricity cost.

    Notes
    -----
    The percentages in percentage_distribution should sum to 1 (or 100%).
    """
    cost_per_unit = np.array(cost_per_unit)
    percentage_distribution = np.array(percentage_distribution)
    mean_cost = np.dot(cost_per_unit, percentage_distribution)
    return mean_cost

def compute_energy_cost_over_distance(distance_km, mean_price, consumption_per_100km,
                                      km_per_year=25000, price_inflation=0.02):
    """
    Calculate the energy cost over a distance, considering price inflation.

    Parameters
    ----------
    distance_km : array_like
        Distance driven in kilometers.
    mean_price : float
        Mean price per unit of energy (e.g., per kWh).
    consumption_per_100km : float
        Energy consumption per 100 kilometers.
    km_per_year : float, optional
        Average kilometers driven per year.
    price_inflation : float, optional
        Annual price inflation rate (e.g., 0.02 for 2%).

    Returns
    -------
    energy_cost : ndarray
        The total energy cost over the distance.

    Notes
    -----
    This function accounts for the increase in energy prices over time due to inflation.
    """
    time_years = np.array(distance_km) / km_per_year
    inflation_factor = (1 + price_inflation) ** time_years
    energy_cost = distance_km * inflation_factor * mean_price * (consumption_per_100km / 100)
    return energy_cost


def total_cost_of_ownership(base_price, distance_km, km_per_year, maintenance_rate_per_km,
                            mean_price, consumption_per_100km, **kwargs):
    """
    Calculate the total cost of ownership (TCO) of a vehicle over a distance.

    Parameters
    ----------
    base_price : float
        Initial purchase price of the vehicle.
    distance_km : array_like
        Distance driven in kilometers.
    km_per_year : float
        Average kilometers driven per year.
    maintenance_rate_per_km : float
        Maintenance cost per kilometer.
    mean_price : float
        Mean price per unit of energy (e.g., per kWh).
    consumption_per_100km : float
        Energy consumption per 100 kilometers.
    **kwargs
        Additional arguments for depreciation, insurance, and energy cost calculations.

    Returns
    -------
    total_cost : ndarray
        The total cost of ownership over the distance.

    Notes
    -----
    The TCO includes purchase price, energy costs, maintenance, insurance, and accounts for depreciation.
    """
    

    
    # Depreciated value
    depreciated_value = calculate_depreciated_value(base_price, distance_km, km_per_year, **kwargs)

    # Energy cost
    energy_cost = compute_energy_cost_over_distance(
        distance_km,
        mean_price,
        consumption_per_100km,
        km_per_year,
        kwargs.get('price_inflation', 0.03)
    )

    # Maintenance cost
    maintenance_cost = calculate_maintenance_cost(distance_km, maintenance_rate_per_km)

    # Insurance cost
    time_years = np.array(distance_km) / km_per_year
    insurance_cost = calculate_insurance_cost(
        time_years,
        kwargs.get('base_insurance_cost', 1000),
        kwargs.get('annual_increase_rate', 0.05)
    )

    # Total cost (purchase price + costs - residual value)
    # total_cost = base_price + energy_cost + maintenance_cost + insurance_cost - depreciated_value

    total_cost = base_price - depreciated_value + energy_cost

    return total_cost

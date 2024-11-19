import numpy as np

def double_linear_depreciation(time_years, initial_slope=0.25, later_slope=0.04,
                               transition_year=2, residual_year=12, residual_value=0.1):
    """
    Calculate the depreciation factor of a vehicle over time using a double linear model.

    Parameters
    ----------
    time_years : array_like
        Time in years at which to calculate the depreciation factor.
    initial_slope : float, optional
        Depreciation rate per year before the transition year.
    later_slope : float, optional
        Depreciation rate per year after the transition year.
    transition_year : float, optional
        The time in years at which the depreciation rate changes from initial_slope to later_slope.
    residual_year : float, optional
        The time in years after which the depreciation factor remains constant at residual_value.
    residual_value : float, optional
        The residual value factor after residual_year.

    Returns
    -------
    depreciation_factor : ndarray
        The depreciation factor (remaining value as a fraction of initial value) at each time point.

    Notes
    -----
    The depreciation model assumes a higher depreciation rate initially, which transitions to a
    lower rate after a certain period, and eventually settles at a residual value.
    """
    time_years = np.array(time_years)
    depreciation_factor = np.zeros_like(time_years)

    # Before transition year
    mask_initial = time_years <= transition_year
    depreciation_factor[mask_initial] = 1 - initial_slope * time_years[mask_initial]

    # Value at the transition point
    value_at_transition = 1 - initial_slope * transition_year

    # Between transition year and residual year
    mask_later = (time_years > transition_year) & (time_years <= residual_year)
    depreciation_factor[mask_later] = value_at_transition - later_slope * (time_years[mask_later] - transition_year)

    # After residual year
    mask_residual = time_years > residual_year
    depreciation_factor[mask_residual] = residual_value

    return depreciation_factor

def calculate_depreciated_value(base_price, distance_km, km_per_year=25000, **kwargs):
    """
    Calculate the depreciated value of a vehicle based on the distance driven.

    Parameters
    ----------
    base_price : float
        The initial purchase price of the vehicle.
    distance_km : array_like
        The distance driven in kilometers.
    km_per_year : float, optional
        Average kilometers driven per year.
    **kwargs
        Additional arguments passed to the double_linear_depreciation function.

    Returns
    -------
    depreciated_value : ndarray
        The depreciated value of the vehicle at each distance point.

    Notes
    -----
    This function converts the distance driven to time in years based on km_per_year
    and applies a depreciation model to calculate the vehicle's value over time.
    """
    time_years = np.array(distance_km) / km_per_year
    depreciation_factor = double_linear_depreciation(time_years, **kwargs)
    depreciated_value = base_price * depreciation_factor
    return depreciated_value

def calculate_maintenance_cost(distance_km, maintenance_rate_per_km):
    """
    Calculate the maintenance cost over a distance.

    Parameters
    ----------
    distance_km : array_like
        Distance driven in kilometers.
    maintenance_rate_per_km : float
        Maintenance cost per kilometer.

    Returns
    -------
    maintenance_cost : ndarray
        The total maintenance cost over the distance.

    Notes
    -----
    Maintenance costs can include regular servicing, tire replacements, and other wear-and-tear items.
    """
    maintenance_cost = np.array(distance_km) * maintenance_rate_per_km
    return maintenance_cost

def calculate_insurance_cost(time_years, base_insurance_cost, annual_increase_rate=0.05):
    """
    Calculate the cumulative insurance cost over time, considering annual increases.

    Parameters
    ----------
    time_years : array_like
        Time in years for which to calculate insurance costs.
    base_insurance_cost : float
        Initial annual insurance cost.
    annual_increase_rate : float, optional
        Annual rate at which insurance cost increases (e.g., 0.05 for 5%).

    Returns
    -------
    cumulative_insurance_cost : ndarray
        The cumulative insurance cost over the given time periods.

    Notes
    -----
    Insurance costs typically increase over time due to inflation and other factors.
    """
    cumulative_cost = np.zeros_like(time_years)
    for i, t in enumerate(time_years):
        years = np.arange(1, int(np.ceil(t)) + 1)
        annual_costs = base_insurance_cost * ((1 + annual_increase_rate) ** (years - 1))
        cumulative_cost[i] = annual_costs.sum()
    return cumulative_cost

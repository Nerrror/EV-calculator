import numpy as np

def double_linear_decay(t, slope1=0.25, slope2=0.04, t_transition=2, t_residual=12, residual_value=0.1):
    # Calculate the exponential decay
    decay = np.zeros_like(t)
    decay[t < t_transition] = 1 - slope1 * t[t < t_transition]
    A = (1 - slope1 * t[t <= t_transition])[-1]
    decay[t > t_transition] = A - slope2 * (t[t > t_transition] - t_transition)
    decay[t > t_residual] = residual_value
    
    return decay


def price_depreciation(base_price, x, depreciation_rate=0.05, km_per_year=25000):
    t = x / km_per_year
    decay = double_linear_decay(t)
    
    cost = base_price * (1 - decay)
    return cost

def mean_electricity_cost(cost, percentage):
    return cost @ percentage

def compute_price_over_km(x, P_mean, consumption, km_per_year=25000, price_inflation=0.02):
    '''
    x : km driven
    P_mean : price distribution mean
    consumption : consumption in [units of energy] per 100 km
    '''
    i = x / km_per_year
    return x * (1 + price_inflation)**i * P_mean * consumption / 100
from ..core import total_cost_of_ownership
import plotly.graph_objs as go
import numpy as np


def generate_ev_tco_plot(
    base_price,
    distance_km,
    km_per_year,
    maintenance_rate_per_km,
    mean_price,
    consumption_per_100km,
):
    """
    Generates a Plotly figure showing the total cost of ownership for EV vehicles.

    Parameters:
    ev_params (dict): Parameters for the EV including base price, consumption, and cost per kWh.
    distance_range (tuple): Range of distances to calculate TCO over.
    num_points (int): Number of points to calculate in the distance range.

    Returns:
    fig_ev (plotly.graph_objs.Figure): Plotly figure object for EV.
    """
    # x = np.linspace(distance_range[0], distance_range[1], num_points)

    x = np.linspace(0, distance_km, km_per_year)

    # Calculate TCO for EV
    tco_ev = total_cost_of_ownership(
        base_price,
        x,
        km_per_year,
        maintenance_rate_per_km,
        mean_price,
        consumption_per_100km,
    )

    # Create trace for the plot
    trace_ev = go.Scatter(x=x, y=tco_ev, mode="lines", name="EV")

    # Create the figure
    fig_ev = go.Figure(data=[trace_ev])

    # Update layout
    fig_ev.update_layout(
        title="Total Cost of Ownership for EV Over Distance Driven",
        xaxis_title="Distance Driven (km)",
        yaxis_title="Total Cost of Ownership (€)",
        legend_title="Vehicle Type",
    )

    return fig_ev


# def generate_cv_tco_plot(cv_params, distance_range=(0, 200000), num_points=1000):
#     """
#     Generates a Plotly figure showing the total cost of ownership for CV vehicles.

#     Parameters:
#     cv_params (dict): Parameters for the CV including base price, consumption, and cost per liter.
#     distance_range (tuple): Range of distances to calculate TCO over.
#     num_points (int): Number of points to calculate in the distance range.

#     Returns:
#     fig_cv (plotly.graph_objs.Figure): Plotly figure object for CV.
#     """
#     x = np.linspace(distance_range[0], distance_range[1], num_points)

#     # Calculate TCO for CV
#     tco_cv = total_cost_of_ownership(
#         base_price=cv_params["base_price"],
#         consumption=cv_params["consumption"],
#         cost_per_unit=cv_params["cost_per_liter"],
#         distance=x,
#         depreciation_rate=cv_params.get("depreciation_rate", 0.1),
#     )

#     # Create trace for the plot
#     trace_cv = go.Scatter(x=x, y=tco_cv, mode="lines", name="CV")

#     # Create the figure
#     fig_cv = go.Figure(data=[trace_cv])

#     # Update layout
#     fig_cv.update_layout(
#         title="Total Cost of Ownership for CV Over Distance Driven",
#         xaxis_title="Distance Driven (km)",
#         yaxis_title="Total Cost of Ownership (€)",
#         legend_title="Vehicle Type",
#     )

#     return fig_cv

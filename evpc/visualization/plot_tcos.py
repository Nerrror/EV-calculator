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
    # fig_ev = go.Figure(data=[trace_ev])

    # # Update layout
    # fig_ev.update_layout(
    #     title="Total Cost of Ownership for EV Over Distance Driven",
    #     xaxis_title="Distance Driven (km)",
    #     yaxis_title="Total Cost of Ownership (€)",
    #     legend_title="Vehicle Type",
    # )

    return trace_ev


def generate_cv_tco_plot(
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
    trace_ev = go.Scatter(x=x, y=tco_ev, mode="lines", name="CV")

    # Create the figure
    fig_ev = go.Figure(data=[trace_ev])

    # Update layout
    fig_ev.update_layout(
        title="Total Cost of Ownership for CV Over Distance Driven",
        xaxis_title="Distance Driven (km)",
        yaxis_title="Total Cost of Ownership (€)",
        legend_title="Vehicle Type",
    )

    return trace_ev

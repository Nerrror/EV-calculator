import dash
from dash import dcc, html, Input, Output
import dash_daq as daq
import logging


# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("Vehicle Cost Comparison Tool"),

    # Shared Annual Mileage Slider
    html.Label("Annual Mileage (km)", style={'marginBottom': '40px', 'marginTop': '20px'}),
    daq.Slider(
        id='shared-annual-mileage',
        min=0,
        max=40000,
        step=1000,
        value=12000,
        handleLabel={"showCurrentValue": True, "label": "km"},
        marks={i: str(i) for i in range(0, 40001, 10000)}
    ),

    html.Div([
        # Electric Vehicle Configuration
        html.Div([
            html.H3("Electric Vehicle Configuration"),

            # Price of Purchase
            html.Label("Price of Purchase (€)", style={'marginBottom': '40px', 'marginTop': '20px'}),
            daq.Slider(
                id='ev-price-of-purchase',
                min=10000,
                max=100000,
                step=1000,
                value=40000,
                handleLabel={"showCurrentValue": True, "label": "€"},
                marks={i: f"{i//1000}k" for i in range(10000, 100001, 20000)},
            ),

            # Age of the Car
            html.Label("Age of the Car (years)", style={'marginBottom': '40px', 'marginTop': '20px'}),
            daq.Slider(
                id='ev-car-age',
                min=0,
                max=20,
                step=1,
                value=3,
                handleLabel={"showCurrentValue": True, "label": "years"},
                marks={i: str(i) for i in range(0, 21, 5)},
            ),

            # Efficiency
            html.Label("Consumption (kwh)", style={'marginBottom': '40px', 'marginTop': '20px'}),
            daq.Slider(
                id='ev-consumption',
                min=5,
                max=30,
                step=1,
                value=18,
                handleLabel={"showCurrentValue": True, "label": "kwh"},
                marks={i: str(i) for i in range(0, 31, 5)},
            ),

            # Mean Electric Price Configuration
            html.H4("Electric Charging Price Configuration"),
            html.Div([
                html.Label("Define Charging Percentages (Home | AC | DC)", style={'marginBottom': '20px'}),
                dcc.RangeSlider(
                    id='charging-type-range',
                    min=0,
                    max=100,
                    step=1,
                    value=[40, 70],  # Initial breakpoints
                    marks={i: f"{i}%" for i in range(0, 101, 20)},
                    pushable = True,
                    tooltip={"placement": "bottom", "always_visible": True},
                ),
                html.Div(id='charging-type-percentages-display', style={'marginTop': '20px'}),
                html.Div([
                    html.Label("Home Charging (€/kWh)", style={'marginRight': '10px'}),
                    dcc.Input(id='home-charging-price', type='number', value=0.15, step=0.01, style={'width': '100px'}),
                    html.Label("AC Charging (€/kWh)", style={'marginLeft': '20px', 'marginRight': '10px'}),
                    dcc.Input(id='ac-charging-price', type='number', value=0.25, step=0.01, style={'width': '100px'}),
                    html.Label("DC Charging (€/kWh)", style={'marginLeft': '20px', 'marginRight': '10px'}),
                    dcc.Input(id='dc-charging-price', type='number', value=0.40, step=0.01, style={'width': '100px'}),
                ], style={'marginBottom': '40px'}),
                html.Div([
                    html.Label("Yearly progression (%)", style={'marginRight': '10px'}),
                    dcc.Input(id='yearlyProgressionEV', type='number', value=0.03, step=0.01, style={'width': '100px'}),
                ], style={'marginBottom': '40px'}),
            ], style={'width': '48%', 'marginBottom': '40px'}),
        ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),

        # Combustion Vehicle Configuration
        html.Div([
            html.H3("Combustion Vehicle Configuration"),

            # Price of Purchase
            html.Label("Price of Purchase (€)", style={'marginBottom': '40px', 'marginTop': '20px'}),
            daq.Slider(
                id='cv-price-of-purchase',
                min=10000,
                max=100000,
                step=1000,
                value=25000,
                handleLabel={"showCurrentValue": True, "label": "€"},
                marks={i: f"{i//1000}k" for i in range(10000, 100001, 20000)},
            ),

            # Age of the Car
            html.Label("Age of the Car (years)", style={'marginBottom': '40px', 'marginTop': '20px'}),
            daq.Slider(
                id='cv-car-age',
                min=0,
                max=20,
                step=1,
                value=5,
                handleLabel={"showCurrentValue": True, "label": "years"},
                marks={i: str(i) for i in range(0, 21, 5)},
            ),

            # Efficiency
            html.Label("Consumption (l)", style={'marginBottom': '40px', 'marginTop': '20px'}),
            daq.Slider(
                id='cv-consumption',
                min=0,
                max=20,
                step=0.2,
                value=6,
                handleLabel={"showCurrentValue": True, "label": "l"},
                marks={i: str(i) for i in range(0, 20, 5)},
            ),
            # Mean Fuel Price Configuration
            html.H4("Fuel Price Configuration"),
            html.Div([
                # Fuel Price Mean
                html.Label("Fuel Price Mean (€/liter)", style={'marginBottom': '40px', 'marginTop': '20px'}),
                daq.Slider(
                    id='cv-fuel-price-mean',
                    min=1.3,
                    max=2.5,
                    step=0.1,
                    value=1.7,
                    handleLabel={"showCurrentValue": True, "label": "€/liter"},
                    marks={i / 20: f"{i / 20:.1f}" for i in range(0, 21, 5)},
                ),
                html.Div([
                    html.Label("Yearly progression (%)", style={'marginRight': '10px'}),
                    dcc.Input(id='yearlyProgressionCV', type='number', value=0.03, step=0.01, style={'width': '100px'}),
                ], style={'marginBottom': '40px'}),
            ], style={'width': '48%', 'marginBottom': '40px'}),
        ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'})
    ]),

    html.Button('Calculate', id='calculate-button', n_clicks=0, style={'marginTop': '20px'}),

    dcc.Graph(id='cost-comparison-graph', style={'marginTop': '20px'})
])

# Callback to dynamically calculate and display the percentages
@app.callback(
    Output('charging-type-percentages-display', 'children'),
    Input('charging-type-range', 'value')
)
def update_charging_percentages(range_values):
    home = range_values[0]
    ac = range_values[1] - range_values[0]
    dc = 100 - range_values[1]
    return html.Div([
        html.P(f"Home: {home}%, AC: {ac}%, DC: {dc}%", style={'marginTop': '10px'})
    ])


@app.callback(
    Output('cost-comparison-graph', 'figure'),
    [
        Input('shared-annual-mileage', 'value'),
        Input('ev-price-of-purchase', 'value'),
        Input('ev-car-age', 'value'),
        Input('ev-consumption', 'value'),
        Input('charging-type-range', 'value'),
        Input('home-charging-price', 'value'),
        Input('ac-charging-price', 'value'),
        Input('dc-charging-price', 'value'),
        Input('yearlyProgressionEV', 'value'),
        Input('cv-price-of-purchase', 'value'),
        Input('cv-car-age', 'value'),
        Input('cv-consumption', 'value'),
        Input('cv-fuel-price-mean', 'value'),
        Input('yearlyProgressionCV', 'value'),
        Input('calculate-button', 'n_clicks')  # Add n_clicks here
    ]
)
def update_comparison_graph(
    annual_mileage,
    ev_price,
    ev_age,
    ev_consumption,
    charging_range,
    home_price,
    ac_price,
    dc_price,
    yearly_progression_ev,
    cv_price,
    cv_age,
    cv_consumption,
    cv_fuel_price,
    yearly_progression_cv,
    n_clicks
):
    print(f"Callback triggered with n_clicks={n_clicks}, annual_mileage={annual_mileage}")
    # Ensure the callback only processes after the button is clicked
    if n_clicks is None or n_clicks == 0:
        logger.info("No clicks yet; returning an empty figure.")
        return {}

    logger.info("Processing input values.")
    # Calculate charging percentages
    home_percentage = charging_range[0]
    ac_percentage = charging_range[1] - charging_range[0]
    dc_percentage = 100 - charging_range[1]

    # Summarize the variables for visualization or calculation
    ev_total_charging_cost = (
        (home_percentage / 100) * home_price +
        (ac_percentage / 100) * ac_price +
        (dc_percentage / 100) * dc_price
    )

    # Example data processing for the comparison graph
    cv_total_fuel_cost = annual_mileage * cv_fuel_price / 100  # Simplified example
    ev_total_cost = ev_price + ev_total_charging_cost * ev_age  # Simplified example
    cv_total_cost = cv_price + cv_total_fuel_cost * cv_age  # Simplified example
    # Log calculated values
    logger.debug(f"EV Total Cost: {ev_total_cost}, CV Total Cost: {cv_total_cost}")


    # Prepare data for the graph
    data = {
        'Vehicle Type': ['Electric Vehicle', 'Combustion Vehicle'],
        'Total Cost (€)': [ev_total_cost, cv_total_cost]
    }

    # Create a bar graph comparing EV and CV
    fig = {
        'data': [
            {
                'x': data['Vehicle Type'],
                'y': data['Total Cost (€)'],
                'type': 'bar',
                'name': 'Total Cost'
            }
        ],
        'layout': {
            'title': 'Vehicle Cost Comparison',
            'xaxis': {'title': 'Vehicle Type'},
            'yaxis': {'title': 'Total Cost (€)'}
        }
    }
    logger.info("Graph created successfully.")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True, threaded=False)
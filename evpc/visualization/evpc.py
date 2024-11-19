import dash
from dash import dcc, html, Input, Output
import dash_daq as daq

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
            # Mean Electric Price Configuration
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
    Input('calculate-button', 'n_clicks'),
    Input('vehicle-type', 'value'),
    Input('annual-mileage', 'value'),
    Input('ownership-period', 'value'),
    Input('electricity-price-mean', 'value'),
    Input('electricity-price-std', 'value')
)
def update_graph(n_clicks, vehicle_type, annual_mileage, ownership_period, electricity_price_mean, electricity_price_std):
    if n_clicks > 0:
        years = np.arange(1, ownership_period + 1)
        if vehicle_type == 'EV':
            total_costs, residual_values = calculate_ev_costs(
                annual_mileage, years, electricity_price_mean, electricity_price_std)
        else:
            total_costs, residual_values = calculate_cv_costs(annual_mileage, years)

        # Create the figure
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=total_costs, mode='lines+markers', name='Total Cost'))
        fig.add_trace(go.Scatter(x=years, y=residual_values, mode='lines+markers', name='Residual Value'))
        fig.update_layout(title='Cost and Residual Value Over Time', xaxis_title='Years', yaxis_title='Amount (€)')
        return fig
    else:
        return go.Figure()



if __name__ == '__main__':
    app.run_server(debug=True)
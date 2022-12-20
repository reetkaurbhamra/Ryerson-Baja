import math
from datetime import datetime
import styles as sty

from dash import Dash, html, dcc, Input, Output
import dash_daq as daq
import plotly.graph_objs as go

app = Dash()  # almost the same as using html
app.layout = html.Div([
    html.Div([
        # gauge
        daq.Gauge(
            id='gauge',
            label='Speedometer',
            min=0,
            max=50,
            value=0,
            showCurrentValue=True,
            units="MPH",
            color="#1e81b0",
            size=200,
            scale={'interval': 2, 'labelInterval': 5},
            style=sty.obj,
        ),
        # some tank
        daq.Tank(
            id='tank',
            label='some tank',
            min=0,
            max=20,
            value=0,
            height=300,
            width=100,
            showCurrentValue=True,
            units='units',
            scale={'interval': 2, 'labelInterval': 5},
            style=sty.obj,
        ),
    ],
        style={'display': 'flex', 'flex-flow': 'column wrap'}
    ),

    # some line graph
    dcc.Graph(
        id='graph',
        style=sty.obj,
    ),

    # update clock
    dcc.Interval(
        id='interval',
        interval=100,
        n_intervals=0,
    ),
],
    style=sty.body,
)


# update speedometer
@app.callback(Output('gauge', 'value'), Input('interval', 'n_intervals'))
def update_gauge(i):
    return round(i * math.pi / 10, 2)  # replace with arduino values


# update some tank
@app.callback(Output('tank', 'value'), Input('interval', 'n_intervals'))
def update_tank(i):
    return round(20 - i * math.pi / 20, 2)  # replace with arduino values


# update some line graph
@app.callback(Output('graph', 'figure'), Input('interval', 'n_intervals'))
def update_tank(i):
    if len(gr) == 20:
        gr.pop(0)
    gr.append((datetime.now().time(), math.sin(i)))  # replace with arduino values
    fig = go.Figure(data=[go.Scatter(x=[i[0] for i in gr], y=[i[1] for i in gr])])
    return fig


if __name__ == '__main__':
    gr = []
    app.run_server(debug=True)

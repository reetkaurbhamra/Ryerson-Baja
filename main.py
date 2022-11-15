import time, random, threading, math
from dash import Dash, html, dcc, Input, Output
import dash_daq as daq


app = Dash()
app.layout = html.Div([
    daq.Gauge(
        id='gauge',
        label='Speedometer',
        min=0,
        max=50,
        value=6.4,
        showCurrentValue=True,
        units="MPH",
        color="#1e81b0",
        size=200,
        scale={'start': 0, 'interval': 2, 'labelInterval': 5},
        style={
            'border': 'solid 2px #A2B1C6',
            'border-radius': '5px',
            'padding-top': '20px',
            'margin': '50px',
            'font': '2px Arial, Helvetica, sans-serif',
            'width': '300px',
        }
    ),
    dcc.Interval(
        id='interval',
        interval=100,
        n_intervals=0,
    ),
])


@app.callback(Output('gauge', 'value'), Input('interval', 'n_intervals'))
def update_output(i):
    return round(i * math.pi / 10, 2) # change this to arduino values


if __name__ == '__main__':
    app.run_server(debug=True)

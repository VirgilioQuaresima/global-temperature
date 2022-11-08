'''Applicazione'''

import dash
from dash.dependencies import Input, Output
from Temperature.Extract import Extract
from Temperature.Actions import *
from Main import layout

app = dash.Dash(__name__)

temperature_df = Extract.load()

app.layout = layout


@app.callback(
    [Output("temperature-chart", "figure")],
    [
        Input("source-filter", "value"),
        Input("date-filter", "value"),
    ],
)
def update_temp_chart(source, date):
    x_name, filtered_df = set_data(temperature_df, date, source)
    return update_charts(source, filtered_df, x_name)


app.run_server(debug=True)

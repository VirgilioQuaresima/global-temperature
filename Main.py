'''Layout principale della pagina'''

from dash import html
import PageComponents
from Temperature import TemperatureComponents


layout = html.Div(
    children=[
        PageComponents.header,
        TemperatureComponents.layout,
        PageComponents.footer
    ]
)

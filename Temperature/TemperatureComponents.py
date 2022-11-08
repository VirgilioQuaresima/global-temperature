'''Componenti della sezione Temperatura media terrestre'''

from dash import dcc, html

header = html.Div(
    children=[
        html.H2(children="Global Temperature Time Series"),
        html.P(children="Global Temperature Time Series. Data are included from the GISS Surface Temperature (GISTEMP) analysis and the global component of Climate at a Glance (GCAG). "),
        html.P(children="Two datasets are provided: "),
        html.P(children="1) global monthly mean and"),
        html.P(children="2) annual mean temperature anomalies in degrees Celsius from 1880 to the present."),
        html.Button(children=["update data ", html.Img(
                    src="https://cdn-icons-png.flaticon.com/512/100/100487.png", className="icon")]),
    ]
)


source_filter = html.Div(
    children=[
        html.Div(children="Data set", className="menu-title"),
        dcc.Dropdown(
            id="source-filter",
            options=[
                {"label": source, "value": source}
                for source in ['GCAG', 'GISTEMP']
            ],
            value="GCAG",
            clearable=False,
            className="dropdown",
        ),
    ]
)


date_filter = html.Div(
    children=[
        html.Div(children="Time", className="menu-title"),
        dcc.Dropdown(
            id="date-filter",
            options=[
                {"label": source, "value": source}
                for source in ['Monthly', 'Annual']
            ],
            value="Monthly",
            clearable=False,
            className="dropdown",
        ),
    ]
)

dropbox_form = html.Div(
    children=[
        source_filter,
        date_filter
    ],
    className="dropdown-form"
)

graph = html.Div(
    children=[
        dcc.Graph(id="temperature-chart", figure={}),
        html.A(children="GISTEMP Global Land-Ocean Temperature Index",
               href="http://data.giss.nasa.gov/gistemp"),
    ]
)

layout = html.Div(
    children=[
        header,
        dropbox_form,
        graph
    ]
)



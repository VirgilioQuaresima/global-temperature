'''Azioni che variano il grafico della temperatura media'''

from Temperature.graph import Graph


def update_charts(source, filtered_df, x_name):

    g = Graph(source, x_name, filtered_df)

    return [
        {
            "data": g.data,
            "layout": g.layout
        }
    ]


def set_data(df, date, source):
    if date == "Monthly":
        df2 = df[1]
        x_name = "Date"
    else:
        df2 = df[0]
        x_name = "Year"

    return x_name, df2[df2['Source'] == source]

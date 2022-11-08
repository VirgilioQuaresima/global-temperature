'''Layout e dati del grafico della temperatura media'''

class Graph:

    def __init__(self, source, x_name, df) -> None:
        self.data = [
            {
                "x": df[x_name],
                "y": df["Mean"],
                "type": "line",
            },
        ]

        self.layout = {
            "title": {
                "text": f"{source} Time vs Mean Temperature",
                "x": 0.05,
                "xanchor": "left"
            },
            "showlegend": False,
            "xaxis": {
                "title": {
                    "text": "Timestamp",
                    "font": {
                        "color": "rgb(23, 23, 116)",
                        "size": 24,
                        "family": "Courier New, Courier, monospace",
                    },

                }
            },
            "yaxis": {
                "title": {
                    "text": "Mean Temperature [ °C ]",
                    "font": {
                        "color": "rgb(23, 23, 116)",
                        "size": 24,
                        "family":"Courier New, Courier, monospace",
                    }
                }
            }
        }

'''Componenti HTML della pagina'''

from dash import html

header = html.Div(
    children=[
        html.H1(children="Sito di Virgilio Quaresima",
                className="header-title",),
        html.P(children="Mi piace definirmi un’adaptive developer. "),
        html.P(children="Uno sviluppatore con la capacità di imparare e mettere in pratica velocemente nuove tecnologie e strategie, così da adattarsi facilmente in progetti le cui necessità cambiano nel tempo."),
        html.P(children="Nel settembre del 2021, ho conseguito la laurea magistrale in fisica bio-sanitaria all’università di Pavia, dove ho avuto la possibilità di studiare approfonditamente:"),
        html.P(children="• Radiobiologia; "),
        html.P(children="• Radioprotezione;"),
        html.P(children="• Metodi computazionali;"),
        html.P(children="• Statistica; "),
        html.P(children="• Matematica."),
        html.P(children="Ho sempre amato produrre codici fin dal liceo e ho deciso, dopo aver concluso il mio percorso all’università, di voler applicare il modo di pensare e di risoluzione dei problemi, acquisiti studiando fisica, al mondo dell’informatica e delle tecnologie innovative, con particolare interesse nei campi: "),
        html.P(children="• Web developing;"),
        html.P(children="• Intelligenza artificiale; "),
        html.P(children="• Blockchain; "),
        html.P(children="• Cybersecurity; "),
        html.P(children="• IoT.",),
    ]
)

footer = html.Div(
    children=[
        html.P(children="virgilioquaresima.dev@gmail.com +39 388 170 5952",)
    ]
)

from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
import plotly.graph_objects as go

figure = {
    'layout': go.Layout(
        colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
        template='plotly_dark',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        margin={'b': 15},
        hovermode='x',
        autosize=True,
        title={'text': 'Stock Prices', 'font': {'color': 'white'}, 'x': 0.5},
    ),
}

blox_chart = dbc.Row([
    html.H4("Analysis of the restaurant's revenue"),
    html.P("x-axis:"),
    dcc.Checklist(
        id='x-axis',
        options=['smoker', 'day', 'time', 'sex'],
        value=['time'],
        inline=True
    ),
    html.P("y-axis:"),
    dcc.RadioItems(
        id='y-axis',
        options=['total_bill', 'tip', 'size'],
        value='total_bill',
        inline=True
    ),
    dcc.Graph(id="graph", figure=figure),
])

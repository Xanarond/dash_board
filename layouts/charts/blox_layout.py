import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
from dash import dcc
from dash import html
import plotly.graph_objects as go

np.random.seed(0)
data = [np.random.normal(0, 1, 100) for _ in range(3)]


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


fig = go.Figure()

for i, dataset in enumerate(data):
    fig.add_trace(go.Box(y=dataset, name=f'Группа {i + 1}'))

fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)',
                  title={'text': 'Чарты с границами', 'font': {'color': 'white', 'family': 'Open Sans Semi Bold'},
                         'x': 0.46, 'y': 0.92}, )

blox_chart = dbc.Row([
    dcc.Graph(figure=fig, style={'width': '100%', 'height': '100vh'})
])
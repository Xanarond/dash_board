import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import dcc
from dash import html


def get_options(graph_data):
    dict_list = []
    for i in graph_data:
        dict_list.append({'label': i['name'], 'value': i['name']})
    return dict_list


linear_chart2 = html.Div([
    dbc.Row([dcc.Dropdown(id='stockselector2', options=[],
                          multi=True, value=[],
                          style={'backgroundColor': '#1E1E1E'},
                          className='stockselector2'
                          )]),
    dbc.Row(dcc.Graph(id='timeseries2',
                      config={'displayModeBar': False},
                      animate=True,
                      style={'backgroundColor': 'rgba(0, 0, 0, 0)'}))
], style={'color': '#1E1E1E'})

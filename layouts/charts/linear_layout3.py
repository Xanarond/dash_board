import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

opt = [{'label': 'CH3 mass flow, 1 unit = 0.04 L/S', 'value': 'CH3 mass flow, 1 unit = 0.04 L/S'},
       {'label': 'NO mass flow, 1 unit = 0.02 L/S', 'value': 'NO mass flow, 1 unit = 0.02 L/S'},
       {'label': 'CO mass flow, 1 unit = 2.0 L/S', 'value': 'CO mass flow, 1 unit = 2.0 L/S'}]


def get_value(opts):
    list_arr = []
    for el in opts:
        list_arr.append(el['label'])
    return list_arr


def get_options(graph_data):
    dict_list = []
    for i in graph_data:
        dict_list.append({'label': i['name'], 'value': i['name']})
    return dict_list


linear_chart3 = html.Div([
    dbc.Row([dcc.Dropdown(id='stockselector3', options=opt, value=get_value(opt),
                          multi=True,
                          className='stockselector3 pb-3 pt-3'
                          )]),
    dbc.Row(dcc.Graph(id='timeseries3',
                      config={'displayModeBar': False},
                      animate=True,
                      style={'backgroundColor': 'rgba(0, 0, 0, 0)'}))
], style={'color': '#1E1E1E'})

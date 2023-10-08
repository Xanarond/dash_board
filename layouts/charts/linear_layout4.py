import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

opt = [{'label': 'Cumulative exhaled volume, 1 unit = 3.0 L', 'value': 'Cumulative exhaled volume, 1 unit = 3.0 L'},
       {'label': 'CO2 Cumulative exhaled volume, 1 unit = 6000.0 L',
        'value': 'CO2 Cumulative exhaled volume, 1 unit = 6000.0 L'}]


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


linear_chart4 = html.Div([
    dbc.Row([dcc.Dropdown(id='stockselector4', options=opt, value=get_value(opt),
                          multi=True,
                          className='stockselector3 pb-3 pt-3'
                          )]),
    dbc.Row(dcc.Graph(id='timeseries4',
                      config={'displayModeBar': False},
                      animate=True,
                      style={'backgroundColor': 'rgba(0, 0, 0, 0)'}))
], style={'color': '#1E1E1E'})

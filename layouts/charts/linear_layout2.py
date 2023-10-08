import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

opt = [{'label': 'Tidal volume, 1 unit = 0.8 L', 'value': 'Tidal volume, 1 unit = 0.8 L'},
       {'label': 'CO2 concetration, 1 unit = 200.0 %', 'value': 'CO2 concetration, 1 unit = 200.0 %'}]


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


linear_chart2 = html.Div([
    dbc.Row([dcc.Dropdown(id='stockselector2', options=opt, value=get_value(opt),
                          multi=True,
                          className='stockselector2 pb-3'
                          )]),
    dbc.Row(dcc.Graph(id='timeseries2',
                      config={'displayModeBar': False},
                      animate=True,
                      style={'backgroundColor': 'rgba(0, 0, 0, 0)'}))
], style={'color': '#1E1E1E'})

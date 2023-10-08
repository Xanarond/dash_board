import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

opt = [{'label': 'CH3 concetration, 1 unit = 0.004 %', 'value': 'CH3 concetration, 1 unit = 0.004 %'},
       {'label': 'NO concetration, 1 unit = 0.002 %', 'value': 'NO concetration, 1 unit = 0.002 %'},
       {'label': 'CO concetration, 1 unit = 0.3 %', 'value': 'CO concetration, 1 unit = 0.3 %'}]


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


linear_chart = html.Div([
    dbc.Row([dcc.Dropdown(id='stockselector1', options=opt, value=get_value(opt),
                          multi=True,
                          className='stockselector1 pb-3'
                          )]),
    dbc.Row(dcc.Graph(id='timeseries1',
                      config={'displayModeBar': False},
                      animate=True,
                      )),
], style={'backgroundColor': 'rgba(0, 0, 0, 0)'})

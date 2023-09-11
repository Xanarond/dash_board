import pandas as pd
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

df = pd.read_csv('data/stockdata2.csv', index_col=0, parse_dates=True, date_format='%Y-%m-%d')
df.index = pd.to_datetime(df['Date'])


def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list


linear_chart3 = html.Div([
    dbc.Row([dcc.Dropdown(id='stockselector3', options=get_options(df['stock'].unique()),
                          multi=True, value=[df['stock'].sort_values()[0]],
                          style={'backgroundColor': '#1E1E1E'},
                          className='stockselector3'
                          )]),
    dbc.Row(dcc.Graph(id='timeseries3',
                      config={'displayModeBar': False},
                      animate=True))
], style={'color': '#1E1E1E'})

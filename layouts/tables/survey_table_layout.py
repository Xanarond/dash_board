import json
from dash import html
from dash import dash_table
import pandas as pd
from dash import dcc


survey_table = html.Div([
    dcc.Loading(
        children=[
            dash_table.DataTable(
                id='survey-table',
                columns=[{'name': 'Name', 'id': 'Name'}, {'name': 'Value', 'id': 'Value'}],
                data=[],
                style_table={},
                style_header={
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white',
                    'textAlign': 'center',
                    'font-size': '22px'
                },
                style_data={
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white',
                    'textAlign': 'left',
                    'font-size': '20px'
                },
            ),
        ],
        type='circle',
    ),
])

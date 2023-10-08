import json
from dash import html
from dash import dash_table
import pandas as pd
from dash import dcc

json_data = '{"ID": 1,"Gender": "Male","Age": 28,"Weight": 75.5,"Height": 180,"SmokingStatus": "Never Smoked"}'
dataj = json.loads(json_data)

survey_table = html.Div([
    dcc.Loading(
        children=[
            dash_table.DataTable(
                id='survey-table',
                columns=[
                    {"name": col, "id": col} for col in ["ID", "Gender", "Age", "Weight", "Height", "SmokingStatus"]
                ],
                data=[dataj],
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
], className='align-center')

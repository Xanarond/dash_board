import json
from dash import html
from dash import dash_table
import pandas as pd
from dash import dcc


json_data = '{"ID": 1, "Gender": "Male", "Age": 28, "Weight": 75.5, "Height": 180, "SmokingStatus": "Never Smoked"}'
data = json.loads(json_data)

data_tuples = [(key, value) for key, value in data.items()]
df = pd.DataFrame(data_tuples, columns=['Name', 'Value'])
# Определяем макет Dash
survey_table = html.Div([
    dcc.Loading(
        children=[
            dash_table.DataTable(
                id='survey-table',
                columns=[{'name': 'Name', 'id': 'Name'}, {'name': 'Value', 'id': 'Value'}],
                data=df.to_dict('records'),
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

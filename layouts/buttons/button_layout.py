import base64
import io
import json

import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc, html

button_download = html.Div([
    dcc.Upload(id='upload-data',
               children=dbc.Button("Выбор папки данных",
                                   color="dark", className='mt-5 align-center'), multiple=True),
])


def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
        elif 'json' in filename:
            df = json.loads(decoded.decode('utf-8'))
        return df
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

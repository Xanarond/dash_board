import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash import dash_table

spirometry_table = dbc.Row([
    html.H3("Spirometry", className='text-center'),
    dcc.Loading(
        children=[
            dash_table.DataTable(
                id='spy-table',
                columns=[
                    {'name': 'Name', 'id': 'Name'},
                    {'name': 'Value', 'id': 'Value'}
                ],
                data=[],
                style_table={},
                style_header={
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white',
                    'textAlign': 'center'
                },
                style_data={
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white',
                    'textAlign': 'left'
                },
            ),
        ],
        type='circle',
    ),
])

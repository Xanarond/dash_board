import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash import dash_table

co2_table = dbc.Row([
    html.H3("CO2", className='text-center'),
    dcc.Loading(
        children=[
            dash_table.DataTable(
                id='co2-table',
                columns=[
                    {'name': 'CO', 'id': 'CO'},
                    {'name': 'NO', 'id': 'NO'},
                    {'name': 'CO2', 'id': 'CO2'}
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

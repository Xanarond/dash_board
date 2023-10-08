import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash import dash_table

biomarkers_table = dbc.Row([
    html.H3("Biomarkers", className='text-center'),
    dcc.Loading(
        children=[
            dash_table.DataTable(
                id='biomarkers-table',
                columns=[{'name': '', 'id': '', "presentation": "dropdown"},
                         {'name': 'CO, ppm', 'id': 'CO, ppm'},
                         {'name': 'NO, ppb', 'id': 'NO, ppb'},
                         {'name': 'CO2, %', 'id': 'Ch3, ppb'},
                         {'name': 'Ch3, ppb', 'id': 'Ch3, ppb'}
                         ],
                data=[],
                style_table={'white-space': 'normal'},
                style_header={
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white',
                    'textAlign': 'center',
                    'white-space': 'normal'
                },
                style_data={
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white',
                    'textAlign': 'center',
                    'white-space': 'normal'
                },
            ),
        ],
        type='circle',
    ),
])

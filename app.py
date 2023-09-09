import dash
import dash_bootstrap_components as dbc
from dash import html

from callbacks.callback_pool import callback_pool
from layouts.charts.blox_layout import blox_chart
from layouts.tables.co2_table_layout import co2_table
from layouts.tables.co_table_layout import co_table
from layouts.tables.no_table_layout import no_table
from layouts.tables.spyrometry_table_layout import spyrometry_table

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

app.layout = dbc.Container([
    dbc.Row(dbc.Col([dbc.Button("Выбор папки данных",
                                color="dark", className='mt-5 align-center')],
                    width=3,
                    )),
    dbc.Row([
        dbc.Col([
            html.H1('Числовые данные', className='fs-5 text-center'),
            co_table,
            html.Div(style={'height': '5px'}),
            no_table,
            html.Div(style={'height': '5px'}),
            co2_table,
            html.Div(style={'height': '5px'}),
            spyrometry_table
        ], width=4),
        dbc.Col([
            html.H1('Графики', className='fs-5 text-center'),
            dbc.Row([dbc.Col([], width=6),
                     dbc.Col([], width=6), ]),
            html.Div(style={'height': '20px'}),
            dbc.Row([dbc.Col([], width=6),
                     dbc.Col([], width=6), ]),
            dbc.Row([dbc.Col([html.H1('Таблица данных опросов', className='fs-5 text-center'), ],
                             width=6),
                     dbc.Col([html.H1('Чарты с границами', className='fs-5 text-center'), blox_chart], width=6), ]),
        ], width=8),
    ]),
], className='container-fluid g-0')

# Регистрация обратных вызовов
callback_pool(app)

# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)

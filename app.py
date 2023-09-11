import dash
import dash_bootstrap_components as dbc
from dash import html
from callbacks.callback_pool import callback_pool
from layouts.charts.blox_layout import blox_chart
from layouts.charts.linear_layout import linear_chart
from layouts.charts.linear_layout2 import linear_chart2
from layouts.charts.linear_layout3 import linear_chart3
from layouts.charts.linear_layout4 import linear_chart4
from layouts.tables.co2_table_layout import co2_table
from layouts.tables.co_table_layout import co_table
from layouts.tables.no_table_layout import no_table
from layouts.tables.spyrometry_table_layout import spyrometry_table
from layouts.tables.survey_table_layout import survey_table

# from weasyprint import HTML, pdf

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dbc.Row(dbc.Col([dbc.Button("Выбор папки данных",
                                color="dark", className='mt-5 align-center')],
                    width=4,
                    )),
    html.Div(style={'height': '5px'}),
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
        ], width=2),
        dbc.Col([
            html.H1('Графики', className='fs-5 text-center'),
            dbc.Row([dbc.Col([linear_chart], width=6),
                     dbc.Col([linear_chart2], width=6), ]),
            html.Div(style={'height': '20px'}),
            dbc.Row([dbc.Col([linear_chart3], width=6),
                     dbc.Col([linear_chart4], width=6), ]),
            dbc.Row([
                dbc.Col([html.Div(style={'height': '57px'}),
                         html.H1('Таблица данных опросов', className='fs-5 text-center'), survey_table],
                        width=3),
                dbc.Col([blox_chart], width=9), ]),
        ], width=10),
    ]),
], className='m-0 px-3')

# Регистрация обратных вызовов
callback_pool(app)

# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)

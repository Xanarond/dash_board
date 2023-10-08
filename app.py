import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from callbacks.callback_pool import callback_pool
from layouts.charts.linear_layout import linear_chart
from layouts.charts.linear_layout2 import linear_chart2
from layouts.charts.linear_layout3 import linear_chart3
from layouts.charts.linear_layout4 import linear_chart4
from layouts.tables.biomarkers_layout import biomarkers_table
from layouts.tables.spirometry_table_layout import spirometry_table
from layouts.tables.survey_table_layout import survey_table

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Store(id='csv-store'),
    dcc.Store(id='json-store'),
    dbc.Row([
        # dbc.Col([
        #     dbc.Row([
        #         dbc.Col([button_download], width=6, className='text-start'),
        #         dbc.Col([pdf_button], width=6, className='text-start')
        #     ], className='align-center mb-3 g-0')
        # ],
        #     width=3,
        # ),
        dbc.Col([dbc.Row([
            html.H1('Patient data', className='fs-4 text-center'),
            survey_table],
            style={'backgroundColor': '#201F21'}, className='pb-5')],
            width=9, className='mt-3 pe-4 ps-4 justify-content-center')
    ]),
    html.Div(style={'height': '30px'}),
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Row([dbc.CardBody([html.H2('Table Data', className='fs-2 text-center')],
                                          style={'backgroundColor': '#201F21'}, className='pe-2 mb-3')]),
                    dbc.Row([dbc.CardBody(
                        [
                            biomarkers_table
                        ], style={'backgroundColor': '#201F21'},
                        className='col-4 col-md-4, col-lg-2 col-xl-2 col-xxl-2 p-2'
                    )]),
                ]),
                dbc.Col([linear_chart], className='col-4 col-md-4 col-lg-5 col-xl-5 col-xxl-5'),
                dbc.Col([linear_chart2], className='col-4 col-md-4 col-lg-5 col-xl-5 col-xxl-5')]),
            dbc.Row([
                dbc.Col([dbc.CardBody([spirometry_table], style={'backgroundColor': '#201F21'}, className='mt-3 p-2')],
                        width=2),
                dbc.Col([linear_chart3], width=5),
                dbc.Col([linear_chart4], width=5)]),
        ], width=12),
    ]),
    dbc.Row([html.Img(src="./assets/images/logo-low-resolution-logo-color-on-transparent-background.png", height=100,
                      style={'width': '180px'})])
], className='m-0 px-3')

# Регистрация обратных вызовов
callback_pool(app)
# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0')

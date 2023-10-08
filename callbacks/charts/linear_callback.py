import pandas as pd
import plotly.graph_objects as go
from dash import Output, Input

from functions.chart_functions import create_plot1

dataf = pd.read_csv('data/synthetic_data.csv')


def linear1_callback_register(app):
    @app.callback(Output('timeseries1', 'figure'),
                  [Input('stockselector1', 'value')])
    def update_timeseries(selected_dropdown_value):
        trace = []
        shapes = []
        df = pd.DataFrame(dataf,
                          columns=["Time", "CO2", "CO", "NO", "CH3",
                                   "Temperature", "Humidity",
                                   "Pressure", "Spirometry"])

        df_sub = create_plot1(df, '')

        colors = ['#5E0DAC', '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056']

        for i, name in enumerate(selected_dropdown_value):
            for elem in df_sub:
                if elem['name'] == name:
                    color = colors[i % len(colors)]
                    trace.append(go.Scatter(x=df['Time'],
                                            y=elem['graph'],
                                            mode='lines',
                                            opacity=0.7,
                                            name=elem['name'],
                                            line={'color': color},
                                            textposition='bottom center'))
                    shapes.append({
                        'type': 'line',
                        'xref': 'paper',
                        'x0': 0,
                        'x1': 1,
                        'y0': elem['upper'],
                        'y1': elem['upper'],
                        'yref': 'y',
                        'line': {
                            'color': color,  # Задаем цвет линии такой же, как у графика
                            'width': 2,
                            'dash': 'solid'
                        }
                    })

                    shapes.append({
                        'type': 'line',
                        'xref': 'paper',
                        'x0': 0,
                        'x1': 1,
                        'yref': 'y',
                        'y0': elem['lower'],
                        'y1': elem['lower'],
                        'line': {
                            'color': color,  # Задаем цвет линии такой же, как у графика
                            'width': 2,
                            'dash': 'solid'
                        }
                    })

        traces = [trace]
        data = [val for sublist in traces for val in sublist]

        figure = {'data': data,
                  'layout': go.Layout(
                      template='plotly_dark',
                      paper_bgcolor='#201F21',
                      plot_bgcolor='#201F21',
                      margin={'b': 15},
                      hovermode='x',
                      autosize=True,
                      title={'text': 'Concentrations', 'font': {'color': 'white'}, 'x': 0.5},
                      legend={'x': 0, 'y': -0.5, 'yanchor': 'bottom'},
                      shapes=shapes,
                      xaxis={'title': 'Time'},
                      yaxis={'title': 'Value'}
                  ),
                  }
        return figure

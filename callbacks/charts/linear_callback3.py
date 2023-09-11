import pandas as pd
from dash import Output, Input
import plotly.graph_objects as go

df = pd.read_csv('data/stockdata2.csv', index_col=0, parse_dates=True, date_format='%Y-%m-%d')
df.index = pd.to_datetime(df['Date'])


def linear2_callback_register(app):
    @app.callback(Output('timeseries3', 'figure'),
                  [Input('stockselector3', 'value')])
    def update_timeseries(selected_dropdown_value):
        ''' Draw traces of the feature 'value' based one the currently selected stocks '''
        # STEP 1
        trace = []
        df_sub = df
        # STEP 2
        # Draw and append traces for each stock
        for stock in selected_dropdown_value:
            trace.append(go.Scatter(x=df_sub[df_sub['stock'] == stock].index,
                                    y=df_sub[df_sub['stock'] == stock]['value'],
                                    mode='lines',
                                    opacity=0.7,
                                    name=stock,
                                    textposition='bottom center'))
        # STEP 3
        traces = [trace]
        data = [val for sublist in traces for val in sublist]
        # Define Figure
        # STEP 4
        figure = {'data': data,
                  'layout': go.Layout(
                      colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                      template='plotly_dark',
                      paper_bgcolor='rgba(0, 0, 0, 0)',
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      margin={'b': 15},
                      hovermode='x',
                      autosize=True,
                      title={'text': 'Stock Prices', 'font': {'color': 'white'}, 'x': 0.5},
                      xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
                  ),
                  }

        return figure

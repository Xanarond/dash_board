import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
from dash import dcc

np.random.seed(0)
data = [np.random.normal(0, 1, 100) for _ in range(3)]

fig = go.Figure()

for i, dataset in enumerate(data):
    fig.add_trace(go.Box(y=dataset, name=f'Группа {i + 1}'))

fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)',
                  title={'text': 'Чарты с границами', 'font': {'color': 'white', 'family': 'Open Sans Semi Bold'},
                         'x': 0.46, 'y': 0.92}, )

blox_chart = dbc.Row([
    dcc.Graph(
        id='box-plot',
        figure={
            'data': [
                go.Box(
                    y=data,
                    boxpoints='all',  # Показывать все значения в box plot
                    jitter=0.3,  # Разброс точек для лучшей видимости
                    pointpos=-1.8  # Позиция точек по вертикали (-1.8 - слева от box plot)
                ),
                go.Scatter(
                    x=[2, 2],  # Добавляем две вертикальные линии
                    # y=[min(data), max(data)],
                    mode='lines',
                    name='Вертикальные линии'
                )
            ],
            'layout': go.Layout(
                title='Горизонтальный Box Plot с вертикальными линиями',
                yaxis=dict(title='Значения'),
                boxmode='group'  # Группируем box plot
            )
        }
    )
])

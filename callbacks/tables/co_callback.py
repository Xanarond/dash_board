import json
import os

import pandas as pd
from dash.dependencies import Input, Output

from functions.table_functions import (
    CO_mean,
    CO_min,
    CO_max,
    CO_var,
    CO_mode,
    CO_top_5_percent_mean,
    CO_bottom_5_percent_mean,
    CO_mean_top_outlier,
    CO_mean_bottom_outlier,
)


def register_co_callback(app):
    # Обновление таблицы с помощью функций
    @app.callback(
        Output('co-table', 'data'),
        Input('co-table', 'id'),
        Input('csv-store', 'data'),
        Input('json-store', 'data')
    )
    def update_table(_, csv_data, json_data):
        # Вызываем функции и добавляем их результаты в список
        functions = [
            CO_mean,
            CO_min,
            CO_max,
            CO_var,
            CO_mode,
            CO_top_5_percent_mean,
            CO_bottom_5_percent_mean,
            CO_mean_top_outlier,
            CO_mean_bottom_outlier,
        ]
        data = []
        df = pd.DataFrame(csv_data,
                          columns=["Time", "CO2", "CO", "NO",
                                   "Temperature", "Humidity",
                                   "Pressure", "Spirometry"])
        for function in functions:
            value, name = function(df, json.loads('""'))
            data.append({'Name': name, 'Value': round(value, 4)})

        return data

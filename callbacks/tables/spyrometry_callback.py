import json
import os

import pandas as pd
from dash.dependencies import Input, Output

from functions.table_functions import (
    Spirometry_mean,
    Spirometry_min,
    Spirometry_max,
    Spirometry_var,
    Spirometry_mode,
    Spirometry_top_5_percent_mean,
    Spirometry_bottom_5_percent_mean,
    Spirometry_mean_top_outlier,
    Spirometry_mean_bottom_outlier,
)

current_directory = os.getcwd()
relative_path = 'data/synthetic_data.csv'
csv_file_path = os.path.join(current_directory, relative_path)
df = pd.read_csv(csv_file_path)


def register_spirometry_callback(app):
    # Обновление таблицы с помощью функций
    @app.callback(
        Output('spy-table', 'data'),
        Input('spy-table', 'id'),
        Input('csv-store', 'data'),
        Input('json-store', 'data')
    )
    def update_table(_, csv_data, json_data):
        # Вызываем функции и добавляем их результаты в список
        functions = [
            Spirometry_mean,
            Spirometry_min,
            Spirometry_max,
            Spirometry_var,
            Spirometry_mode,
            Spirometry_top_5_percent_mean,
            Spirometry_bottom_5_percent_mean,
            Spirometry_mean_top_outlier,
            Spirometry_mean_bottom_outlier,
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

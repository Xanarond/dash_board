import json
import os

import pandas as pd
from dash.dependencies import Input, Output

from functions.table_functions import (
    Spyrometry_mean,
    Spyrometry_min,
    Spyrometry_max,
    Spyrometry_var,
    Spyrometry_mode,
    Spyrometry_top_5_percent_mean,
    Spyrometry_bottom_5_percent_mean,
    Spyrometry_mean_top_outlier,
    Spyrometry_mean_bottom_outlier,
)

current_directory = os.getcwd()
relative_path = 'data/synthetic_data.csv'
csv_file_path = os.path.join(current_directory, relative_path)
df = pd.read_csv(csv_file_path)


def register_spyrometry_callback(app):
    # Обновление таблицы с помощью функций
    @app.callback(
        Output('spy-table', 'data'),
        Input('spy-table', 'id')
    )
    def update_table(_):
        # Вызываем функции и добавляем их результаты в список
        functions = [
            Spyrometry_mean,
            Spyrometry_min,
            Spyrometry_max,
            Spyrometry_var,
            Spyrometry_mode,
            Spyrometry_top_5_percent_mean,
            Spyrometry_bottom_5_percent_mean,
            Spyrometry_mean_top_outlier,
            Spyrometry_mean_bottom_outlier,
        ]
        data = []

        for function in functions:
            value, name = function(df, json.loads('""'))
            data.append({'Name': name, 'Value': round(value, 4)})

        return data

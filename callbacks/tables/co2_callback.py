import json
import os

import pandas as pd
from dash.dependencies import Input, Output

from functions.table_functions import (
    CO2_mean,
    CO2_min,
    CO2_max,
    CO2_var,
    CO2_mode,
    CO2_top_5_percent_mean,
    CO2_bottom_5_percent_mean,
)

current_directory = os.getcwd()
relative_path = 'data/synthetic_data.csv'
csv_file_path = os.path.join(current_directory, relative_path)
df = pd.read_csv(csv_file_path)


def register_co2_callback(app):
    # Обновление таблицы с помощью функций
    @app.callback(
        Output('co2-table', 'data'),
        Input('co2-table', 'id')
    )
    def update_table(_):
        # Вызываем функции и добавляем их результаты в список
        functions = [
            CO2_mean,
            CO2_min,
            CO2_max,
            CO2_var,
            CO2_mode,
            CO2_top_5_percent_mean,
            CO2_bottom_5_percent_mean,
            # CO_mean_top_outlier,
            # CO_mean_bottom_outlier,
        ]
        data = []

        for function in functions:
            value, name = function(df, json.loads('""'))
            data.append({'Name': name, 'Value': value})

        return data

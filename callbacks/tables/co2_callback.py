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
    CO_mean_top_outlier,
    CO_mean_bottom_outlier,
)


# current_directory = os.getcwd()
# relative_path = 'data/synthetic_data.csv'
# csv_file_path = os.path.join(current_directory, relative_path)
# print(type(csv_file_path))
# df = pd.read_csv(csv_file_path, index_col=0)


# print('co2-22', df)

def register_co2_callback(app):
    # Обновление таблицы с помощью функций
    @app.callback(
        Output('co2-table', 'data'),
        Input('co2-table', 'id'),
        Input('csv-store', 'data'),
        Input('json-store', 'data')
    )
    def update_table(_, csv_input, json_data):
        # Вызываем функции и добавляем их результаты в список
        functions = [
            CO2_mean,
            CO2_min,
            CO2_max,
            CO2_var,
            CO2_mode,
            CO2_top_5_percent_mean,
            CO2_bottom_5_percent_mean,
            CO_mean_top_outlier,
            CO_mean_bottom_outlier,
        ]
        csv_data = []

        df = pd.DataFrame(csv_input,
                          columns=["Time", "CO2", "CO", "NO",
                                   "Temperature", "Humidity",
                                   "Pressure", "Spirometry"])
        for function in functions:
            value, name = function(df, json.loads('""'))
            csv_data.append({'Name': name, 'Value': round(value, 4)})

        return csv_data

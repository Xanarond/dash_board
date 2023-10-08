import json
import os

import pandas as pd
from dash.dependencies import Input, Output

from functions.table_functions import (
    generate_table_1)

dataf = pd.read_csv('data/synthetic_data.csv')


def register_biomarkers_callback(app):
    @app.callback(
        Output('biomarkers-table', 'data'),
        Input('biomarkers-table', 'id'),
        Input('csv-store', 'data'),
        Input('json-store', 'data')
    )
    def update_table(_, csv_input, json_data):
        transformed_data_list = []
        # if csv_input is not None:
        df = pd.DataFrame(dataf,
                          columns=["Time", "CO2", "CO", "NO", "CH3", "Temperature", "Humidity", "Pressure",
                                   "Spirometry"])

        # print(generate_table_1(df, '').columns.values)
        data_list = generate_table_1(df, '').to_dict('records')
        keys_to_add = generate_table_1(df, '').index.values.tolist()
        transformed_data_list = [
            {'': keys_to_add[i], 'CO, ppm': data['CO, ppm'], 'NO, ppb': data['NO, ppb'],
             'CO2, %': data['CO2, %'], 'Ch3, ppb': data['Ch3, ppb']} for i, data in enumerate(data_list)]
        return transformed_data_list

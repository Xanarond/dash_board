import pandas as pd
from dash.dependencies import Input, Output
from functions.table_functions import generate_table_2

dataf = pd.read_csv('data/synthetic_data.csv')


def register_spirometry_callback(app):
    # Обновление таблицы с помощью функций
    @app.callback(
        Output('spirometry-table', 'data'),
        Input('spirometry-table', 'id'),
        Input('csv-store', 'data'),
        Input('json-store', 'data')
    )
    def update_table(_, csv_data, json_data):
        # if csv_data is not None:
        df = pd.DataFrame(dataf,
                          columns=["Time", "CO2", "CO", "NO",
                                   "Temperature", "Humidity",
                                   "Pressure", "Spirometry"])

        data_list = generate_table_2(df, '').to_dict('records')
        keys_to_add = generate_table_2(df, '').index.values.tolist()
        transformed_data_list = [{'': keys_to_add[i], 'SPIROMETRY': data['SPIROMETRY']} for i, data in
                                 enumerate(data_list)]
        return transformed_data_list

import json

from dash import Output, Input, State

from layouts.buttons.input_button_layout import parse_contents


def file_reading_callback(app):
    @app.callback(Output('csv-store', 'data'),
                  Input('upload-data', 'contents'),
                  State('upload-data', 'filename'),
                  )
    def store_csv_data(list_of_contents, list_of_names):
        if list_of_contents is not None:
            for c, n in zip(list_of_contents, list_of_names):
                if 'csv' in n:
                    df = parse_contents(c, n)
                    if df is not None:
                        return df.to_dict()

    # Separate callback to store JSON data
    @app.callback(Output('json-store', 'data'),
                  Input('upload-data', 'contents'),
                  State('upload-data', 'filename'),
                  )
    def store_json_data(list_of_contents, list_of_names):
        if list_of_contents is not None:
            for c, n in zip(list_of_contents, list_of_names):
                if 'json' in n:
                    df = parse_contents(c, n)
                    if df is not None:
                        json_string = json.dumps(df)
                        data = json.loads(json_string)
                        return [data]

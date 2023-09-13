from dash import Output, Input


def register_survey_callback(app):
    @app.callback(
        Output('survey-table', 'data'),
        Input('json-store', 'data')
    )
    def update_table(json_data):
        # print(10, json_data)
        if json_data is not None:
            return json_data

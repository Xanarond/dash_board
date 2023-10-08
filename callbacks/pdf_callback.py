from dash import Output, Input


def register_pdf_callback(app):
    @app.callback(
        Output("save-pdf-button", "n_clicks"),
        Input("save-pdf-button", "n_clicks"),
    )
    def save_pdf(n_clicks):
        print(app.index())
        return n_clicks + 1

from dash import Output, Input
import plotly.express as px


def register_blox_callback(app):
    @app.callback(
        Output("graph", "figure"),
        Input("x-axis", "value"),
        Input("y-axis", "value"))
    def generate_chart(x, y):
        df = px.data.tips()
        fig = px.box(df, x=x, y=y)
        return fig

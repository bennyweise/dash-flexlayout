import dash
import dash_mantine_components as dmc
from dash import Input, Output, html

import dash_flexlayout as dfl

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = dfl.MantineProvider(
    theme={"colorScheme": "dark"},
    children=html.Div([dfl.MyComponent(), dfl.MyComponent()]),
)


@app.callback(
    Output("button-3-output", "children"),
    [
        Input("button-3", "n_clicks"),
    ],
)
def update_button_3_output(n_clicks):
    return f"Clicked {n_clicks} times!"


@app.callback(Output("layout-model", "children"), [Input("flex-layout", "model")])
def show_model_layout(layout):
    return str(layout)


if __name__ == "__main__":
    app.run_server(debug=True)

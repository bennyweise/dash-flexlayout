import dash
from dash import Input, Output, html

import dash_flexlayout as dfl

app = dash.Dash(__name__, suppress_callback_exceptions=True)

config = {
    "global": {"tabEnableClose": False, "tabEnableFloat": True},
    "borders": [
        {
            "type": "border",
            "location": "bottom",
            "size": 100,
            "children": [{"type": "tab", "name": "four", "component": "text"}],
        },
        {"type": "border", "location": "left", "size": 100, "children": []},
    ],
    "layout": {
        "type": "row",
        "weight": 100,
        "children": [
            {
                "type": "tabset",
                "weight": 50,
                "selected": 0,
                "children": [
                    {
                        "type": "tab",
                        "name": "One",
                        "component": "text",
                        "enableFloat": True,
                        "id": "tab-1",
                    }
                ],
            },
            {
                "type": "tabset",
                "weight": 50,
                "selected": 0,
                "children": [
                    {
                        "type": "tab",
                        "name": "Two",
                        "component": "text",
                        "id": "tab-2",
                    },
                    {
                        "type": "tab",
                        "name": "Three",
                        "component": "text",
                        "id": "tab-3",
                    },
                ],
            },
        ],
    },
}


nodes = [
    dfl.Tab(id="tab-1", children=["this is tab 1", html.Div(id="button-3-output")]),
    dfl.Tab(id="tab-2", children=["this is TAB2!", html.Div(id="layout-model")]),
    dfl.Tab(
        id="tab-3",
        children=[
            "this is a div in tab 3! :)",
            html.Button(id="button-3", children="Click me"),
        ],
    ),
]

app.layout = html.Div(
    children=[
        dfl.DragFrom(html.Span("Drag Me"), name="New Tab++"),
        html.Div(
            dfl.FlexLayout(
                id="flex-layout",
                model=config,
                children=nodes,
                useStateForModel=False,
                # style={"top": "120px"},
            ),
        ),
    ]
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

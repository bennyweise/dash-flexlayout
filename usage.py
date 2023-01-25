import dash
from dash import Input, Output, html

import dash_flexlayout as dfl

app = dash.Dash(__name__, suppress_callback_exceptions=True)

config = {
    "global": {"tabEnableClose":False, "tabEnableFloat": True},
    "borders":[
        {
          "type": "border",
          "location":"bottom",
          "size": 100,
          "children": [
              {
              "type": "tab",
              "name": "four",
              "component": "text"
              }
            ]
        },
    		{
          "type": "border",
          "location":"left",
          "size": 100,
          "children": []
         }
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
                ]
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
                    }
                ]
            }
        ]
    }
}

# nodes = {
#     "tab-1": "this is tab 1",
#     "tab-2": "this is TAB2!",
#     "tab-3": html.Div(id="tab-3", children=[
#         "this is a div in tab 3! :)",
#         html.Button(id="button-3", children="Click me"),
#         html.Div(id="button-3-output")
#     ]    
#     ),
# }

nodes = [
    html.Div(id="tab-1", children="this is tab 1"),
    html.Div(id="tab-2", children="this is TAB2!"),
    html.Div(id="tab-3", children=[
            "this is a div in tab 3! :)",
            html.Button(id="button-3", children="Click me"),
            html.Div(id="button-3-output")
        ]
    ),
]

app.layout = dfl.FlexLayout(id='component', config=config, children=nodes)

@app.callback(
    Output('button-3-output', 'children'),
    [
        Input("button-3", "n_clicks"),
    ],
)
def update_button_3_output(n_clicks):
    return f"Clicked {n_clicks} times!"

if __name__ == '__main__':
    app.run_server(debug=True)

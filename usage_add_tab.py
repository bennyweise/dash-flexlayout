from typing import Dict, List

import dash
import plotly.express as px
from dash import MATCH, Input, Output, State, dcc, html

import dash_flexlayout as dfl

app = dash.Dash(__name__, suppress_callback_exceptions=True)

config = {
    "global": {"tabEnableClose":False, "tabEnableFloat": True},
    "borders":[],
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
                        "name": "One",
                        "type": "tab",
                        "id": "tab-base",
                    }
                ]
            },
            {
                "type": "tabset",
                "weight": 50,
                "selected": 0,
                "children": [
                ]
            }
        ]
    }
}

def get_all_children(parent: Dict, ls: List = None) -> List[Dict]:
    ls = ls or []
    ls.append(parent)
    if "children" in parent:
        if isinstance(parent["children"], list):
            [get_all_children(child, ls) for child in parent["children"]]
        else:
            get_all_children(parent["children"], ls)
    return ls


def add_tab_to_tabset(model: Dict, n: int) -> Dict:
    """Add a tab to the tab model
    """
    print(model)
    all_children = get_all_children(model["layout"])
    all_tabs = [child for child in all_children if child.get("type") == "tab"]
    all_tabsets = [child for child in all_children if child.get("type") == "tabset"]
    print(len(all_children))

    new_tab = {
        "name": f"Plot {len(all_tabs)}",
        "type": "tab",
        "id": f"tab-plot:{len(all_tabs)}"
    }
    all_tabsets[-1]["children"].append(new_tab)
    return model

def create_nodes(model: Dict) -> List[dfl.Tab]:
    """Most nodes are just an empty div that will be populated layer
    """
    all_tab_ids = []
    for row in model["layout"]["children"]:
        all_tab_ids.extend([tab["id"] for tab in row["children"]])
    tabs = []
    for tab_id in all_tab_ids:
        if tab_id == "tab-base":
            tabs.append(dfl.Tab(id=tab_id, children=html.Div(children=html.Button(id="add-tab", children="Add tab"))))
        else:
            typ, n = tab_id.split(":")
            tabs.append(dfl.Tab(id=tab_id, children=html.Div(id={"type": typ, "index": n}, children=f"This is tab with ID {tab_id}")))
            # tabs.append(html.Div(id=tab_id, children=html.Div(id={"type": typ, "index": n}, children=f"This is tab with ID {tab_id}")))
    return tabs



app.layout = html.Div(children=[
    dfl.FlexLayout(id='flex-layout', model=config, children=create_nodes(config), useStateForModel=False),
])

@app.callback(
    [
        Output('flex-layout', 'model'),
        Output('flex-layout', 'children'),
    ],
    [
        Input("add-tab", "n_clicks"),
    ],
    [
        State("flex-layout", "model"),
        State("flex-layout", "children"),
    ],
    prevent_initial_call = True
)
def add_tab(n_clicks, model, children):
    print("adding tabs")
    add_tab_to_tabset(model, n_clicks)
    print(model)
    return model, create_nodes(model)

@app.callback(
    Output({"type": "tab-plot", "index": MATCH}, "children"),
    [
        Input({"type": "tab-plot", "index": MATCH}, "n_clicks")
    ],
    [
        State({"type": "tab-plot", "index": MATCH}, "id"),
    ]
)
def render_tab(n_clicks, id):
    print("rendering stuff")
    

    df = px.data.iris()  # iris is a pandas DataFrame
    fig = px.scatter(df, x="sepal_width", y="sepal_length")

    return dcc.Graph(figure=fig)
    return f"Tab with {id} --> n_clicks is {n_clicks}"


if __name__ == '__main__':
    app.run_server(debug=True)

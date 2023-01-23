import dash_flexlayout
import dash

app = dash.Dash(__name__)

app.layout = dash_flexlayout.FlexLayout(id='component')


if __name__ == '__main__':
    app.run_server(debug=True)

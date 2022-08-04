import dash
from dash import html, dcc

app = dash.Dash(__name__, use_pages=True, suppress_callback_exceptions=True)

app.layout = html.Div(
    [
        # main app framework
        html.Div("DBC.26 Final Project on Python for Data Science using Dash", style={
                 'fontSize': 50, 'textAlign': 'center'}),
        html.Div([
            dcc.Link(page['name']+"  |  ", href=page['path'])
            for page in dash.page_registry.values()
        ]),
        html.Hr(),

        # content of each page
        dash.page_container
    ]
)


if __name__ == "__main__":
    app.run(debug=True)

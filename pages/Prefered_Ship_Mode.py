import dash
from math import prod
from turtle import color
from unicodedata import category
from dash import Dash, html, dcc, Input, Output, State, callback, ctx
import plotly.express as px
import pandas as pd


dash.register_page(__name__)

df1 = pd.read_csv("C:\\dataAnalytics\\GlobalSuperStore.csv")


Prefered_Ship_pivot = pd.pivot_table(df1[["Ship_Mode", "Count"]], index=[
                                     "Ship_Mode"], aggfunc="count")
Prefered_Ship_pivot = Prefered_Ship_pivot.reset_index()
Prefered_Ship_pivot.sort_values(by=["Count"],
                                ascending=False)


Prefered_Ship_pivot["Prefered_Ship_Count"] = Prefered_Ship_pivot["Count"]
Prefered_Ship_pivot["Class_Mode"] = Prefered_Ship_pivot["Ship_Mode"]


layout = html.Div(children=[
    html.H1(children='Which is the Prefered Ship Mode'),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.RadioItems(id="Count-Button",
                   options=[
                       {"label": "Count",
                           "value": "Prefered_Ship_Count"}
                   ],
                   value="Prefered_Ship_Count",
                   labelStyle={'display': 'none'}
                   ),
    dcc.RadioItems(id="Ship_Mode-Button",
                   options=[
                      {"label": "Most Prefered Ship_Mode",
                       "value": "Class_Mode"},
                   ],
                   labelStyle={'width': '50%'}
                   ),
    html.Button(id="Button", n_clicks=0, children="Show breakdown"),
    dcc.Graph(
        id='bar-graph6'
        # figure=fig
    )
])


@ callback(
    Output("bar-graph6", "figure"),
    State("Count-Button", "value"),
    State("Ship_Mode-Button", "value"),
    Input("Button", "n_clicks"),
    prevent_initial_call=True
)
def display_graph(Count, Mode, n):

    if Mode == Mode:

        fig = px.bar(Prefered_Ship_pivot, x=Mode,
                     y=Count, title=f"The Most {Mode} sold", color=Prefered_Ship_pivot["Ship_Mode"])
        return fig

    print(n)

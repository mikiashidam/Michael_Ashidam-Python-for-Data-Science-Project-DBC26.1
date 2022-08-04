import dash
from math import prod
from turtle import color
from unicodedata import category
from dash import Dash, html, dcc, Input, Output, State, callback, ctx
import plotly.express as px
import pandas as pd

dash.register_page(__name__)
df1 = pd.read_csv("C:\\dataAnalytics\\GlobalSuperStore.csv")


most_profitable_cat = pd.pivot_table(df1[["Category", "Sales", "Profit_Margin"]], index=[
                                     "Category", "Sales", "Profit_Margin"], aggfunc="sum")
most_profitable_cat = most_profitable_cat.reset_index()
most_profitable_cat = most_profitable_cat.groupby(["Category"]).sum()
most_profitable_cat = most_profitable_cat.reset_index()

most_profitable_cat["Profitable_Category"] = most_profitable_cat["Category"]
most_profitable_cat["Most_CatProfitable"] = most_profitable_cat["Profit_Margin"]

layout = html.Div(children=[
    html.H1(children='Which Category is Best Selling And the Moost Profitable'),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.RadioItems(id="ProfitCat-Button",
                   options=[
                       {"label": "ProfitabilityCat",
                           "value": "Most_CatProfitable"}
                   ],
                   value="Most_CatProfitable",
                   labelStyle={'display': 'none'}
                   ),
    dcc.RadioItems(id="Category-Button",
                   options=[
                       {"label": "Most Profitable Category",
                        "value": "Profitable_category"}
                   ],
                   labelStyle={'width': '50%'}
                   ),
    html.Button(id="Button", n_clicks=0, children="Show breakdown"),
    dcc.Graph(
        id='bar-graph2'
        # figure=fig
    )
])


@ callback(
    Output("bar-graph2", "figure"),
    # State("Category-dropdown", "value"),
    # State("Sales-dropdown", "value"),
    # Input("ProfitSub-Button", "value"),
    # Input("SubCategory-Button", "value"),
    State("ProfitCat-Button", "value"),
    State("Category-Button", "value"),
    Input("Button", "n_clicks"),
    prevent_initial_call=True
)
def display_graph(ProfitableCat, Catprofit, n):
    if Catprofit == Catprofit:

        fig = px.bar(most_profitable_cat, x="Category",
                     y=ProfitableCat, title=f"The Most {Catprofit}sold", color=most_profitable_cat["Category"])
    return fig


# if __name__ == '__main__':
#     app.run_server(debug=True)

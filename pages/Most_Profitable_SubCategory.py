import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output, State, callback, ctx
from unicodedata import category
from turtle import color
from math import prod
import dash

dash.register_page(__name__, path="/")

df1 = pd.read_csv("C:\\dataAnalytics\\GlobalSuperStore.csv")

most_profitable_subCat = pd.pivot_table(df1[["Sub_Category", "Sales", "Profit_Margin"]], index=[
    "Sub_Category", "Sales", "Profit_Margin"], aggfunc="sum")
most_profitable_subCat = most_profitable_subCat.reset_index()
most_profitable_subCat = most_profitable_subCat.groupby(
    ["Sub_Category"]).sum()
most_profitable_subCat = most_profitable_subCat.reset_index()


most_profitable_subCat["Most_SubProfitable"] = most_profitable_subCat["Profit_Margin"]
most_profitable_subCat["Profitable_SubCategory"] = most_profitable_subCat["Sub_Category"]

layout = html.Div(children=[
    html.H1(children='What are the Best Selling And the Moost Profitable Sub-Category'),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.RadioItems(id="ProfitSub-Button",
                   options=[
                       {"label": "ProfitabilitySub",
                           "value": "Most_SubProfitable"}
                   ],
                   value="Most_SubProfitable",
                   labelStyle={'display': 'none'}
                   ),
    dcc.RadioItems(id="SubCategory-Button",
                   options=[
                      {"label": "Most Profitable Sub_Category",
                       "value": "Profitable_SubCategory"},
                   ],
                   labelStyle={'width': '50%'}
                   ),
    html.Button(id="Button", n_clicks=0, children="Show breakdown"),
    dcc.Graph(
        id='bar-graph3'
        # figure=fig
    )
])


@ callback(
    Output("bar-graph3", "figure"),
    State("ProfitSub-Button", "value"),
    State("SubCategory-Button", "value"),
    Input("Button", "n_clicks"),
    prevent_initial_call=True
)
def display_graph(ProfitableSub, Subprofit, n):
    if Subprofit == Subprofit:

        fig = px.bar(most_profitable_subCat, x="Sub_Category",
                     y=ProfitableSub, title=f"The Most {Subprofit} sold", color=Subprofit)
        return fig
    return fig


# if __name__ == '__main__':
#     app.run_server(debug=True)

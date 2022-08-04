import dash
from math import prod
from turtle import color
# from unicodedata import market
from dash import Dash, html, dcc, Input, Output, State, callback, ctx
import plotly.express as px
import pandas as pd

dash.register_page(__name__)

df1 = pd.read_csv("C:\\dataAnalytics\\GlobalSuperStore.csv")


layout = html.Div(children=[
    html.H1(children='Which City has the Highest Number of Sales'),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Dropdown(id="Market-dropdown",
                 options=[
                     {"label": i, "value": i} for i in df1["Market"].unique()],
                 placeholder="Select a Market",
                 ),

    dcc.Graph(
        id='bar-graph7'
        # figure=fig
    )
])


@ callback(
    Output("bar-graph7", "figure"),
    Input("Market-dropdown", "value"),

)
def display_graph(market):

    if market == None:
        best_selling_pivot = pd.pivot_table(
            df1[["City", "Count"]], index=["City"], aggfunc="count")
        best_selling_pivot = best_selling_pivot.reset_index()
        best_selling_pivot.sort_values(by=["Count"],
                                       ascending=False)

        fig = px.bar(best_selling_pivot, x="City",
                     y="Count", title="The Highest Number of Sales", color=best_selling_pivot["City"])
        return fig
    else:
        best_selling_pivot = pd.pivot_table(df1[["Market", "Country", "Sales"]], index=[
            "Market", "Country"], aggfunc="sum")
        best_selling_pivot = best_selling_pivot.reset_index()
        best_selling_pivot = best_selling_pivot.groupby(
            ["Market", "Country"]).sum()

        best_selling_pivot = best_selling_pivot.reset_index()

        productdf = best_selling_pivot[best_selling_pivot["Market"] ==
                                       market]

        fig = px.bar(productdf, x="Country",
                     y="Sales", title=f"The Highest Sales in {market} ", color=productdf["Country"])

        return fig


# if __name__ == '__main__':
#     app.run_server(debug=True)

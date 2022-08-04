import dash
from math import prod
from turtle import color
from unicodedata import category
from dash import Dash, html, dcc, Input, Output, State, callback, ctx
import plotly.express as px
import pandas as pd

app = Dash.register_page(__name__)

df1 = pd.read_csv("C:\\dataAnalytics\\GlobalSuperStore.csv")
df1["Most_SellingSub"] = df1["Sub_Category"]

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Dropdown(id="Category-dropdown",
                 options=[
                     {"label": i, "value": i} for i in df1["Category"].unique()],
                 placeholder="Select a Category",
                 ),

    dcc.Graph(
        id='bar-graph'
        # figure=fig
    )
])


@ app.callback(
    Output("bar-graph", "figure"),
    Input("Category-dropdown", "value"),

)
def display_graph(category):
    #    Which Category is Best Selling
    if category == None:
        best_selling_pivot = pd.pivot_table(df1[["Sub_Category", "Sales", "Profit_Margin"]], index=[
                                            "Sub_Category", "Sales", "Profit_Margin"], aggfunc="sum")
        best_selling_pivot = best_selling_pivot.reset_index()
# best_selling_pivot.sort_values(by=["Profit_Margin"],
#                               ascending=False).tail(20).sort_values(by="Sales",ascending=False)
        best_selling_pivot = best_selling_pivot.groupby(["Sub_Category"]).sum()
        best_selling_pivot = best_selling_pivot.reset_index()

        fig = px.bar(best_selling_pivot, x="Sub_Category",
                     y="Sales", title="The best Selling Sub_Category", color=best_selling_pivot["Sub_Category"])
        return fig
    else:
        best_selling_pivot = pd.pivot_table(df1[["Category", "Sub_Category", "Sales"]], index=[
            "Category", "Sub_Category"], aggfunc="sum")
        best_selling_pivot = best_selling_pivot.reset_index()
        best_selling_pivot = best_selling_pivot.groupby(
            ["Category", "Sub_Category"]).sum()

        best_selling_pivot = best_selling_pivot.reset_index()

        productdf = best_selling_pivot[best_selling_pivot["Category"] ==
                                       category]

        fig = px.bar(productdf, x="Sub_Category",
                     y="Sales", title=f"The Most {category} sold", color=productdf["Sub_Category"])

        return fig


# if __name__ == '__main__':
#     app.run_server(debug=True)

import dash
from math import prod
from turtle import color
from unicodedata import category
from dash import Dash, html, dcc, Input, Output, State, callback, ctx
import plotly.express as px
import pandas as pd


dash.register_page(__name__)

df1 = pd.read_csv("C:\\dataAnalytics\\GlobalSuperStore.csv")


Profitable_Region = pd.pivot_table(df1[["Region", "Sales", "Profit_Margin"]], index=[
                                   "Region", "Profit_Margin"], aggfunc="sum")
Profitable_Region = Profitable_Region.reset_index()
Profitable_Region = Profitable_Region.groupby(["Region"]).sum()
Profitable_Region = Profitable_Region.reset_index()


Profitable_Region["Most_Region_Profitable"] = Profitable_Region["Profit_Margin"]
Profitable_Region["Region_Profitable"] = Profitable_Region["Region"]


layout = html.Div(children=[
    html.H1(children='which Region is Most Profitable'),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.RadioItems(id="Profit-Button",
                   options=[
                       {"label": "Profit_Margin",
                           "value": "Most_Region_Profitable"}
                   ],
                   value="Most_Region_Profitable",
                   labelStyle={'display': 'none'}
                   ),
    dcc.RadioItems(id="Region-Button",
                   options=[
                      {"label": "Most Profitable Customer Region",
                       "value": "Region_Profitable"},
                   ],
                   labelStyle={'width': '50%'}
                   ),
    html.Button(id="Button", n_clicks=0, children="Show breakdown"),
    dcc.Graph(
        id='bar-graph5'
        # figure=fig
    )
])


@ callback(
    Output("bar-graph5", "figure"),
    State("Profit-Button", "value"),
    State("Region-Button", "value"),
    Input("Button", "n_clicks"),
    prevent_initial_call=True
)
def display_graph(Profit, Region, n):

    if Region == Region:

        fig = px.bar(Profitable_Region, x=Region,
                     y=Profit, title=f"The Most {Region} sold", color=Profitable_Region["Region"])
        return fig

    print(n)


# if __name__ == '__main__':
#     app.run_server(debug=True)

import dash
from math import prod
from turtle import color
from unicodedata import category
from dash import Dash, html, dcc, Input, Output, State, callback, ctx
import plotly.express as px
import pandas as pd


dash.register_page(__name__)

df1 = pd.read_csv("C:\\dataAnalytics\\GlobalSuperStore.csv")


best_customer_segment = pd.pivot_table(df1[["Segment", "Sales", "Profit_Margin"]], index=[
                                       "Segment", "Profit_Margin"], aggfunc="sum")
best_customer_segment = best_customer_segment.reset_index()
best_customer_segment = best_customer_segment.groupby(["Segment"]).sum()
best_customer_segment = best_customer_segment.reset_index()
print(best_customer_segment.head(100))


best_customer_segment["Most_Customer_Profitable"] = best_customer_segment["Profit_Margin"]
best_customer_segment["Segment_Profitable"] = best_customer_segment["Segment"]


layout = html.Div(children=[
    html.H1(children='which Customer Segment is Most Profitable'),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.RadioItems(id="Profit-Button",
                   options=[
                       {"label": "Profit_Margin",
                           "value": "Most_Customer_Profitable"}
                   ],
                   value="Most_Customer_Profitable",
                   labelStyle={'display': 'none'}
                   ),
    dcc.RadioItems(id="Segment-Button",
                   options=[
                      {"label": "Most Profitable Customer Segment",
                       "value": "Segment_Profitable"},
                   ],
                   labelStyle={'width': '50%'}
                   ),
    html.Button(id="Button", n_clicks=0, children="Show breakdown"),
    dcc.Graph(
        id='bar-graph4'
        # figure=fig
    )
])


@ callback(
    Output("bar-graph4", "figure"),
    State("Profit-Button", "value"),
    State("Segment-Button", "value"),
    Input("Button", "n_clicks"),
    prevent_initial_call=True
)
def display_graph(Profit, segment, n):

    if segment == segment:

        fig = px.bar(best_customer_segment, x=segment,
                     y=Profit, title=f"The Most {segment} sold", color=best_customer_segment["Segment"])
        return fig

    print(n)


# if __name__ == '__main__':
#     app.run_server(debug=True)

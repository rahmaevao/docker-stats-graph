from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

from src.dockerstats import *

ds = DockerStats("scripts/data.csv")

fig = px.line(
    ds.df,
    x="DATE",
    y="MEM Usage",
    color="NAME",
    title="Memory usage by containers",
    height=1000,
)

app.layout = html.Div(
    children=[
        html.H1(children="Docker Stats Graph"),
        dcc.Graph(id="example-graph", figure=fig),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)

import dash
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import dash_core_components as dcc
import pandas as pd
import math
from flask import Flask
import read_data


def functionfigH():
    df = read_data.read_data()

    dfH = df[['ID', 'Stone masonry typology', 'fc [MPa]', 'IQMip']].copy()
    dfH.sort_values(by=['Stone masonry typology'],inplace=True)

    # Creating the column which will contain the values of N
    X = 1
    Y = 1

    for index, row in dfH.iterrows():
        X = 1
        Y = 1
        N = 2
        if (row['IQMip'] == 'NaN'):
            X = 0
        else:
            X = 1
        if (row['fc [MPa]'] == 'NaN'):
            Y = 0
        else:
            Y = 1
        if (X + Y < 2):
            N = 1
        else:
            N = 2
        dfH['N'] = math.sqrt(N) * 12
    figure = px.scatter(
        dfH,
        x='IQMip',
        y='fc [MPa]',
        color='Stone masonry typology',
        template='simple_white',
        labels={
            "IQMip": "MQIᵢₙₚₗₐₙₑ",
            "fc [MPa]": "f꜀[MPa]"
        }

    ).update_layout(
        {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
         'paper_bgcolor': 'rgba(0, 0, 0, 0)',
         'font': {'color': '#7f7f7f'}}
    )

    figure.update_traces(marker=dict(size=dfH['N']))
    return figure

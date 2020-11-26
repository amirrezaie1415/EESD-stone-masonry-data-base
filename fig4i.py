import dash
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import dash_core_components as dcc
import pandas as pd
import math
from flask import Flask

import read_data

def functionfigI(df):

    dfI = df.copy()
    dfI.sort_values(by=['Stone masonry typology'], inplace=True)
    dfI = dfI[['ID', 'Stone masonry typology', 'σ0,tot /fc', 'IQMip']]

    # Creating the column which will contain the values of N
    X = 1
    Y = 1
    dfI['N'] = ""

    for index, row in df.iterrows():
        X = 1
        Y = 1
        N = 2
        if (row['IQMip'] == 'NaN'):
            X = 0
        else:
            X = 1
        if (row['σ0,tot /fc'] == 'NaN'):
            Y = 0
        else:
            Y = 1
        if (X + Y < 2):
            N = 1
        else:
            N = 2
        dfI['N'] = math.sqrt(N) * 12
    figure = px.scatter(
        dfI,
        x='IQMip',
        y='σ0,tot /fc',
        color='Stone masonry typology',
        template='simple_white',
        labels={
            "IQMip": "MQIᵢₙₚₗₐₙₑ",
            "σ0,tot /fc": "σ₀/f꜀"
        }
    ).update_layout(
        {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
         'paper_bgcolor': 'rgba(0, 0, 0, 0)',
         'font': {'color': '#7f7f7f'}}
    )

    figure.update_traces(marker=dict(size=dfI['N']))
    return figure

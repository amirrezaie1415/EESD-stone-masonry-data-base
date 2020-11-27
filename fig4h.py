import dash
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import dash_core_components as dcc
import pandas as pd
import math
from flask import Flask
import read_data


def functionfigH(df):
    dfH = df[['ID', 'Stone masonry typology', 'fc [MPa]', 'IQMip']].copy()
    dfH = dfH.fillna(0)
    dfH['N'] = 0

    #Clean up fc and IQMip columns, round up values
    for index, row in dfH.iterrows():
        dfH.at[index,'IQMip'] = round(row['IQMip'] * 10) / 10
        dfH.at[index,'fc [MPa]'] = round(row['fc [MPa]'] / 1) * 1

    #get N, the size of each point
    for index,row in dfH.iterrows():
        # print(row['ID'], row['IQMip'], row['fc [MPa]'])
        # print(dfH[(dfH['IQMip']==row['IQMip']) & (dfH['fc [MPa]']==row['fc [MPa]'])])
        N = len(dfH[(dfH['IQMip']==row['IQMip']) & (dfH['fc [MPa]']==row['fc [MPa]'])])
        if(N== 0):
            dfH.at[index,'N']= 1
        else:
            dfH.at[index, 'N'] = 16*(N**(1./4))

    dfH = dfH.drop_duplicates(subset=['IQMip','fc [MPa]'])
    dfH.sort_values(by=['Stone masonry typology'],inplace=True)
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

    figure.update_traces(marker=dict(size=dfH['N'],opacity=1))
    return figure
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
    dfI = dfI[['ID', 'Stone masonry typology', 'σ0,pc [MPa]','fc [MPa]', 'IQMip']]
    dfI['σ0/fc'] = dfI['σ0,pc [MPa]']/dfI['fc [MPa]']

    # Creating the column which will contain the values of N
    dfI = dfI.fillna(0)
    dfI['N'] = 0

    for index, row in dfI.iterrows():
        dfI.at[index,'IQMip'] = round(row['IQMip']*10) / 10
        dfI.at[index,'σ0/fc'] = round(row['σ0/fc']*10)/10

    #get N, the size of each point
    for index,row in dfI.iterrows():
        N = len(dfI[(dfI['IQMip']==row['IQMip']) & (dfI['σ0/fc']==row['σ0/fc'])])
        if(N== 0):
            dfI.at[index,'N']= 1
        else:
            dfI.at[index, 'N'] = 12*(N**(1./2))

    dfI = dfI.drop_duplicates(subset=['IQMip','σ0/fc'])
    for index,row in dfI.iterrows():
        if row['σ0/fc']==0 and row['IQMip']==0:
            dfI.drop(index,inplace=True)
    for index,row in dfI.iterrows():
        if row['IQMip']==0:
            dfI.drop(index,inplace=True)

    dfI.sort_values(by=['Stone masonry typology'], inplace=True)
    figure = px.scatter(
        dfI,
        x='IQMip',
        y='σ0/fc',
        color='Stone masonry typology',
        template='simple_white',
        labels={
            "IQMip": "MQIᵢₙₚₗₐₙₑ",
            "σ0/fc": "σ₀/f꜀"
        }
    ).update_layout(
        {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
         'paper_bgcolor': 'rgba(0, 0, 0, 0)',
         'font': {'color': '#7f7f7f'}}
    )
    figure.update_traces(marker=dict(size=dfI['N'],opacity=1))
    return figure
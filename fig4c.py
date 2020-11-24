
import pandas as pd
import dash
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import dash_core_components as dcc
from flask import Flask
import read_data



def functionfigC():
    df = read_data.read_data()

    # Setting constants for the figure.
    Nunits = df['H [mm]'].count()
    HL_min = 0.25
    Nbars = 7

    # Adding the Ho/L calculation to each row:
    H0L = df['H0 [mm]'] / df['L [mm]']
    df['H0L'] = H0L

    # Selecting only the columns of interest in a new dataframe
    df = df[['ID', 'Stone masonry typology', 'H0L', 'H [mm]']].copy()

    # replacing spaces in column names with "_"
    df.columns = [column.replace(" ", "_") for column in df.columns]

    dfFigC = pd.DataFrame(0, index=['A', 'B', 'C', 'D', 'E', 'E1'],
                          columns=[0.375, 0.625, 0.875, 1.125, 1.375, 1.625, 1.875])

    for bar in range(1, Nbars + 1):
        for index, row in df.iterrows():
            if (row['H0L'] > (bar - 1) * 0.25 + HL_min and row['H0L'] <= bar * 0.25 + HL_min):
                if (row['Stone_masonry_typology'] == 'A'):
                    dfFigC.iloc[0, bar - 1] += 1
                elif (row['Stone_masonry_typology'] == 'B'):
                    dfFigC.iloc[1, bar - 1] += 1
                elif (row['Stone_masonry_typology'] == 'C'):
                    dfFigC.iloc[2, bar - 1] += 1
                elif (row['Stone_masonry_typology'] == 'D'):
                    dfFigC.iloc[3, bar - 1] += 1
                elif (row['Stone_masonry_typology'] == 'E'):
                    dfFigC.iloc[4, bar - 1] += 1
                elif (row['Stone_masonry_typology'] == 'E1'):
                    dfFigC.iloc[5, bar - 1] += 1

    # print(dfFigB.loc['A'])
    # print(dfFigB.columns[0])

    dfFigC = dfFigC.transpose()
    type = ['A', 'B', 'C', 'D', 'E', 'E1']

    fig = px.bar(dfFigC,
                 labels=dict(
                     index="H₀/L",
                     value="# Tests",
                     variable="Type",
                 ),template='simple_white'
                 )
    fig.update_xaxes(dtick=0.25, ticks="inside", range=[0.2,2])
    fig.update_yaxes(ticks="inside", range=[0, 60], showgrid=False)
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                       'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                       'font': {'color': '#7f7f7f'},
                       'title': {
                           'text': "Fig C - Shear Span Ratio",
                           'y': 0.9,
                           'x': 0.5,
                           'xanchor': 'center',
                           'yanchor': 'top'
                       }
                       }
                      )
    return fig

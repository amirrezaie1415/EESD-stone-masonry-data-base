import dash
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import dash_core_components as dcc
import pandas as pd
import math
from flask import Flask

df = pd.read_excel('/data/StoneMasonryDatabase.xls', index_col=None)

app=dash.Dash(__name__)
 server = app.server()


# def read_data(input_dir):
#     """
#     Read all the data from input_dir into a pandas dataframe.
#
#     Args:
#
#         input_dir: the directory where data is stored
#     """
#     from glob import glob
#
#     input_files = glob('{}/*.xls'.format(input_dir))
#     dataframes = [
#         pd.read_excel(file, index_col=None) for file in input_files
#     ]
#     df = pd.concat(dataframes)
#     return df

def functionfigA(df):
    # Selecting only the columns of interest
    df = df[['ID', 'Stone masonry typology', 'Lab / In-situ', 'H [mm]']].copy()

    # replacing spaces in column names with "_"
    df.columns = [column.replace(" ", "_") for column in df.columns]

    Nunits = df['H_[mm]'].count()
    h_min = 750
    Nbars = 7

    dfFigA = pd.DataFrame(0, index=['Lab', 'In-Situ'],
                          columns=['A', 'B', 'C', 'D', 'E', 'E1'])

    # dfFigA['Lab/In-Situ']= ['Lab','In-Situ']

    str = 'Lab'

    for index, row in df.iterrows():
        if (row['Lab_/_In-situ'].find('Lab') != -1):
            if (row['Stone_masonry_typology'] == 'A'):
                dfFigA.iloc[0, 0] += 1
            elif (row['Stone_masonry_typology'] == 'B'):
                dfFigA.iloc[0, 1] += 1
            elif (row['Stone_masonry_typology'] == 'C'):
                dfFigA.iloc[0, 2] += 1
            elif (row['Stone_masonry_typology'] == 'D'):
                dfFigA.iloc[0, 3] += 1
            elif (row['Stone_masonry_typology'] == 'E'):
                dfFigA.iloc[0, 4] += 1
            elif (row['Stone_masonry_typology'] == 'E1'):
                dfFigA.iloc[0, 5] += 1
        else:
            if (row['Stone_masonry_typology'] == 'A'):
                dfFigA.iloc[1, 0] += 1
            elif (row['Stone_masonry_typology'] == 'B'):
                dfFigA.iloc[1, 1] += 1
            elif (row['Stone_masonry_typology'] == 'C'):
                dfFigA.iloc[1, 2] += 1
            elif (row['Stone_masonry_typology'] == 'D'):
                dfFigA.iloc[1, 3] += 1
            elif (row['Stone_masonry_typology'] == 'E'):
                dfFigA.iloc[1, 4] += 1
            elif (row['Stone_masonry_typology'] == 'E1'):
                dfFigA.iloc[1, 5] += 1

    dfFigA = dfFigA.transpose()

    dfFigA['Type'] = ['A', 'B', 'C', 'D', 'E', 'E1']

    fig = px.bar(dfFigA,
                 x=['A', 'B', 'C', 'D', 'E', 'E1'],
                 y=dfFigA.Lab,
                 color=dfFigA.Type,
                 labels=dict(
                     index=" ",
                     value="# Tests",
                     variable="Lab - Masonry Type"
                             ),
                 template='simple_white')
    fig.add_trace(go.Bar(x=['A', 'B', 'C', 'D', 'E', 'E1'], y=dfFigA['In-Situ'], name='In-Situ'))
    fig.update_xaxes(dtick=0.25, ticks="inside")
    fig.update_yaxes(ticks="inside",range=[0,60], showgrid=False)
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                       'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                       'font':{'color':'#7f7f7f'},
                       'title': {
                           'text': "Fig A - Masonry typology & Type of test",
                           'y': 0.9,
                           'x': 0.5,
                           'xanchor': 'center',
                           'yanchor': 'top'
                            }
                       }
                      )
    # fig = go.Figure(data=[
    #     go.Bar(x=['A', 'B', 'C', 'D', 'E', 'E1'],y= dfFigA['Lab']),
    #     go.Bar(x=['A', 'B', 'C', 'D', 'E', 'E1'],y= dfFigA['In-Situ'])
    # ])


    fig.update_layout(barmode='stack')

    return fig


#Creating Figure B:
def functionfigB(df):
    # Selecting only the columns of interest
    df = df[['ID', 'Stone masonry typology', 'H [mm]']].copy()

    # replacing spaces in column names with "_"
    df.columns = [column.replace(" ", "_") for column in df.columns]

    Nunits = df['H_[mm]'].count()
    h_min = 750
    Nbars = 7

    dfFigB = pd.DataFrame(0, index=['A', 'B', 'C', 'D', 'E', 'E1'],
                         columns=[0.875, 1.125, 1.375, 1.625, 1.875, 2.125, 2.375])

    for bar in range(1, Nbars + 1):
        for index, row in df.iterrows():
            if (row['H_[mm]'] > (bar - 1) * 250 + h_min and row['H_[mm]'] <= bar * 250 + h_min):
                if (row['Stone_masonry_typology'] == 'A'):
                    dfFigB.iloc[0, bar - 1] += 1
                elif (row['Stone_masonry_typology'] == 'B'):
                    dfFigB.iloc[1, bar - 1] += 1
                elif (row['Stone_masonry_typology'] == 'C'):
                    dfFigB.iloc[2, bar - 1] += 1
                elif (row['Stone_masonry_typology'] == 'D'):
                    dfFigB.iloc[3, bar - 1] += 1
                elif (row['Stone_masonry_typology'] == 'E'):
                    dfFigB.iloc[4, bar - 1] += 1
                elif (row['Stone_masonry_typology'] == 'E1'):
                    dfFigB.iloc[5, bar - 1] += 1

    dfFigB = dfFigB.transpose()
    type = ['A', 'B', 'C', 'D', 'E', 'E1']
    fig = px.bar(dfFigB,
                 labels=dict(
                     index="Height [m]",
                     value="# Tests",
                     variable="Type",
                     ),
                 template='simple_white',
                 )
    fig.update_xaxes(dtick=0.25, ticks="inside")
    fig.update_yaxes(ticks="inside",range=[0,60], showgrid=False)
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                       'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                       'font':{'color':'#7f7f7f'},
                       'title': {
                           'text': "Fig B - Height of Test Unit",
                           'y': 0.9,
                           'x': 0.5,
                           'xanchor': 'center',
                           'yanchor': 'top'
                            }
                       }
                      )
    return fig


#Creating Figure C:
def functionfigC(df):
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


def functionfigF(df):
    # Selecting only the columns of interest
    dfF = df[['ID', 'Stone masonry typology', 'H [mm]', 'σ0,tot /fc']].copy()

    # replacing spaces in column names with "_"
    dfF.columns = [column.replace(" ", "_") for column in dfF.columns]

    Nunits = dfF['H_[mm]'].count()
    Nbars = 7

    dffigF = pd.DataFrame(0, index=['A', 'B', 'C', 'D', 'E', 'E1'], columns=[0.05, 0.15, 0.25, 0.35, 0.45, 0.55])

    for bar in range(1, Nbars + 1):
        for index, row in dfF.iterrows():
            if (row['σ0,tot_/fc'] > (bar - 1) * 0.1 and row['σ0,tot_/fc'] <= bar * 0.1):
                if (row['Stone_masonry_typology'] == 'A'):
                    dffigF.iloc[0, bar - 1] += 1
                elif (row['Stone_masonry_typology'] == 'B'):
                    dffigF.iloc[1, bar - 1] += 1
                elif (row['Stone_masonry_typology'] == 'C'):
                    dffigF.iloc[2, bar - 1] += 1
                elif (row['Stone_masonry_typology'] == 'D'):
                    dffigF.iloc[3, bar - 1] += 1
                elif (row['Stone_masonry_typology'] == 'E'):
                    dffigF.iloc[4, bar - 1] += 1
                elif (row['Stone_masonry_typology'] == 'E1'):
                    dffigF.iloc[5, bar - 1] += 1

    dffigF = dffigF.transpose()
    type = ['A', 'B', 'C', 'D', 'E', 'E1']

    fig = px.bar(dffigF,
                 labels=dict(
                     index="σ₀/f꜀",
                     value="# Tests",
                     variable="Type",
                 ),
                 template='simple_white')
    fig.update_xaxes(dtick=0.1, ticks="inside")
    fig.update_yaxes(ticks="inside")
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                       'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                       'font': {'color': '#7f7f7f'},
                       'title': {
                           'text': "Fig F - Axial Stress Ratio",
                           'y': 0.9,
                           'x': 0.5,
                           'xanchor': 'center',
                           'yanchor': 'top'
                       }
                       }
                      )
    return fig

def functionfigH(df):
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

# df = read_data('C:/Users/patri/Documents')
app.layout = html.Div()


app.layout = html.Div(children=[
    html.Div(className='row',
             children=[
                 html.Div(className='four columns div-user-controls', children=[
                     html.H2('EESD - Stonmasonry Data'),
                     html.P('''Visualising data with Plotly - Dash'''),
                     html.P('''Pick one or more versions from the dropdown below.'''),
                     html.Div(className='div-for-DropDown',
                              children=[
                                  dcc.Dropdown(id='versionSelector',
                                               options=[
                                                   {'label': 'Version 1', 'value':'version 1'},
                                                   {'label': 'Version 2', 'value': 'version 2'},
                                               ],
                                               value=['Version 1'],
                                               className='versionSelector')
                                  ])
                 ]),
                 html.Div(className='eight columns div-for-charts bg-grey',children=[
                     #Figure A
                     dcc.Graph(
                         id='figA',
                         figure=functionfigA(df)
                     ),

                     #Figure B
                     dcc.Graph(
                         id='figB',
                         figure=functionfigB(df)
                     )
                     ,
                     #Figure C
                     dcc.Graph(
                         id='figC',
                         figure=functionfigC(df)
                     ),
                     dcc.Graph(
                         id='figF',
                         figure=functionfigF(df)
                     )
                     ,
                     dcc.Graph(
                         id='figH',
                         figure=functionfigH(df)
                     ),
                     dcc.Graph(
                         id='figI',
                         figure=functionfigI(df)
                     )
                 ])
             ])
])
if __name__ =='__main__':
    app.run_server(debug=True)



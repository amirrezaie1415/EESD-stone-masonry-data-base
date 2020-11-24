import os
import dash
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import dash_core_components as dcc
import pandas as pd
import math
from flask import Flask

import fig4a
import fig4b
import fig4c
import fig4f
import fig4h
import fig4i

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app=dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

#Calling all figures from different Python files:
figA = fig4a.functionfigA()
figB = fig4b.functionfigB()
figC = fig4c.functionfigC()
figF = fig4f.functionfigF()
figH = fig4h.functionfigH()
figI = fig4i.functionfigI()


#Creating web app design:
app.layout = html.Div()
app.layout = html.Div(children=[
    html.Div(className='header',
             children=[
                 html.H1(['EESD - Stonmasonry Data'], style={'textAlign': 'center'}),
                 html.P([
                            '''This web page presents data from a database of shear-compression tests on stone masonry walls.''',
                            #html.Br(),
                            ''' 6 graphs have been produced to visualise the distribution with regard to various parameters.''',
                            #html.Br(),
                            '''The colours refer to the masonry typology (see figure A).''']),
                 html.P('''Pick one or more versions from the dropdown below.''')]
             )
    ,
    html.Div(className='row',
             children=[
                 html.Div(className='four columns div-user-controls', children=[
                     html.Div(className='div-for-DropDown',
                              children=[
                                  dcc.Dropdown(id='versionSelector',
                                               options=[
                                                   {'label': 'Version 1', 'value':'version 1'},
                                                   {'label': 'Version 2', 'value': 'version 2'},
                                               ],
                                               value='version 1',
                                               className='versionSelector')
                                  ])
                 ]),
                 html.Div(className='eight columns div-for-charts bg-grey',children=[
                     #Figure A
                     dcc.Graph(
                         id='figA',
                         figure=figA
                     ),

                     #Figure B
                     dcc.Graph(
                         id='figB',
                         figure=figB
                     )
                     ,
                     #Figure C
                     dcc.Graph(
                         id='figC',
                         figure=figC
                     ),
                     dcc.Graph(
                         id='figF',
                         figure=figF
                     )
                     ,
                     dcc.Graph(
                         id='figH',
                         figure=figH
                     ),
                     dcc.Graph(
                         id='figI',
                         figure=figI
                     )
                 ])
             ])
])
if __name__ =='__main__':
    app.run_server(debug=True)



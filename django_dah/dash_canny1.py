import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
import time

from datetime import datetime as dt
from django_plotly_dash import DjangoDash
from demo.models import Userstagecn
from demo.models import Usersessionscn
import plotly.express as px
import dash_table
import plotly
import plotly.graph_objects as go

from dash_extensions.snippets import send_data_frame

def canny_userstage(**kwargs):
    

    #kwargs['stage'] = 'Final Response'
    #kwargs['stage_result'] = 'SUCCESS'
    df = pd.DataFrame(Userstagecn.objects.using('canny').values_list('customer','transaction_id','transaction_intent', 'channel','timestamp').filter(stage="Final Response" , stage_result="SUCCESS").filter(**kwargs))
    df.columns = ['Customer', 'Transaction ID', 'Intent used', 'Channels','Date and Time']
    print(df[:5])

    df1 = Usersessionscn.objects.using('canny').values('customer').filter(**kwargs).distinct().count()

    df2 = Usersessionscn.objects.using('canny').values('user_session_id').filter(**kwargs).distinct().count()

    fig = go.Figure()

    fig.add_trace(go.Indicator(
    mode = "number",
    value = df1,
    domain = {'row': 0, 'column': 0}))

    fig1 = go.Figure()

    fig1.add_trace(go.Indicator(
    mode = "number",
    value = df2,
    domain = {'row': 0, 'column': 1}))

    external_stylesheets=['https://codepen.io/amyoshino/pen/jzXypZ.css']

    app = DjangoDash('dash_integration_id')

    app.layout = html.Div([
        html.Div([
            # Adding one extar Div
            html.Div([
                html.H1(children='Canny User Stage'),
            ], className = 'row'),

    app.css.append_css({
    "external_url": external_stylesheets
    }),

    html.Div([
                dash_table.DataTable(
                    id='datatable_id',
                    columns = [
                        {"name": i, "id":i} for i in df.columns
                    ],
                    data = df.to_dict('records'),
                    editable=False,
                    filter_action="native",
                    sort_action = "native",
                    sort_mode="multi",
                    row_selectable="multi",
                    row_deletable=False,
                    selected_rows=[],
                    page_action="native",
                    page_current=0,
                    page_size=10,
                    #page_action='none',
                    style_cell={
                    'whiteSpace':'normal'
                    },
                    fixed_rows={'headers':True, 'data':0},
                    virtualization=False,
                    ),
                ],className='row'),
            ]),

        html.Div([
                html.H1(children='Canny Usersessions'),
                dcc.Graph(figure=fig),
                dcc.Graph(figure=fig1)
            ], className = 'row'),
        


       
             
        

        
    ])
    if __name__ == '__main__':
        app.run_server(8052, debug=True)
    


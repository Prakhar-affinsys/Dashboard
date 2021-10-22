import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from demo.models import Usersessionscn
from django_plotly_dash import DjangoDash
import plotly.graph_objects as go


def canny_usersession(**kwargs):

    df = Usersessionscn.objects.using('canny').values('customer').filter(**kwargs).distinct().count()

    app = DjangoDash('dash_integration_id')

    fig = go.Figure()

    fig.add_trace(go.Indicator(
    mode = "number",
    value = df,
    domain = {'row': 0, 'column': 0}))
    
    app.layout = html.Div([
        html.Div([
            # Adding one extar Div
            html.Div([
                html.H1(children='Canny Usersessiomns'),
            ], className = 'row'),

         html.Div([
             dcc.Graph(figure=fig)
         ])

        
    

    
            

       ])
   ])

    if __name__ == '__main__':
        app.run_server(8052, debug=True)


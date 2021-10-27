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
    dff = pd.DataFrame()
    df = pd.DataFrame(Userstagecn.objects.using('canny').values_list('customer','transaction_id','transaction_intent', 'channel','timestamp').filter(stage="Final Response" , stage_result="SUCCESS").filter(**kwargs))
    df.columns = ['Customer', 'Transaction ID', 'Intent used', 'Channels','date']
    df["date"] = pd.to_datetime(df['date'], utc=True)
    print(df[:5])

    df1 = Usersessionscn.objects.using('canny').values('customer').filter(**kwargs).distinct().count()

    df2 = Usersessionscn.objects.using('canny').values('user_session_id').filter(**kwargs).distinct().count()

    df3 =  pd.DataFrame()
    
    fig = go.Figure()    # cannyusersession big number

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

    
    # html.Div([
    #             dash_table.DataTable(
    #                 id='datatable_id',
    #                 columns = [
    #                     {"name": i, "id":i} for i in df.columns
    #                 ],
    #                 data = df.to_dict('records'),
    #                 editable=False,
    #                 filter_action="native",
    #                 sort_action = "native",
    #                 sort_mode="multi",
    #                 row_selectable="multi",
    #                 row_deletable=False,
    #                 selected_rows=[],
    #                 page_action="native",
    #                 page_current=0,
    #                 page_size=10,
    #                 #page_action='none',
    #                 style_cell={
    #                 'whiteSpace':'normal'
    #                 },
    #                 fixed_rows={'headers':True, 'data':0},
    #                 virtualization=False,
    #                 ),
    #             ],className='row'),
    #         ]),

    html.Div([
            dcc.DatePickerRange(
                id="my-date-picker-range",
                min_date_allowed=dt(2021, 1, 1),
                max_date_allowed=dt(2022, 1, 4),
                initial_visible_month=dt(2021, 1, 1),
                end_date=dt(2022, 1, 4),
            ),
            dash_table.DataTable(
                id="datatable-interactivity",
                columns=[
                    {
                        "name": i,
                        "id": i,
                        "deletable": True,
                        "selectable": True,
                        "hideable": True,
                    }
                    if i == "iso_alpha3" or i == "year" or i == "id"
                    else {"name": i, "id": i, "deletable": True, "selectable": True}
                    for i in df.columns
                ],
                data=df.to_dict("records"),  # the contents of the table
                editable=True,  # allow editing of data inside all cells
                filter_action="native",  # allow filtering of data by user ('native') or not ('none')
                sort_action="native",  # enables data to be sorted per-column by user or not ('none')
                sort_mode="single",  # sort across 'multi' or 'single' columns
                column_selectable="multi",  # allow users to select 'multi' or 'single' columns
                row_selectable="multi",  # allow users to select 'multi' or 'single' rows
                row_deletable=True,  # choose if user can delete a row (True) or not (False)
                selected_columns=[],  # ids of columns that user selects
                selected_rows=[],  # indices of rows that user selects
                page_action="native",  # all data is passed to the table up-front or not ('none')
                page_current=0,  # page number that user is on
                page_size=6,  # number of rows visible per page
                style_cell={  # ensure adequate header width when text is shorter than cell's text
                    "minWidth": 95,
                    "maxWidth": 95,
                    "width": 95,
                },
                style_cell_conditional=[  # align text columns to left. By default they are aligned to right
                    {"if": {"column_id": c}, "textAlign": "left"}
                    for c in ["country", "iso_alpha3"]
                ],
                style_data={  # overflow cells' content into multiple lines
                    "whiteSpace": "normal",
                    "height": "auto",
                },
            ),
        ]),
    html.Div([html.Button("Download csv", id="btn"), dcc.Download(id="download")]),

    html.Div([
            html.H1(children='Canny Usersessions'),
            dcc.Graph(figure=fig),
            dcc.Graph(figure=fig1),
            
        ], className = 'row'),

    html.Div([
        html.H1(children='Total completed Transactions'),
        dcc.Graph(id = 'big_number3')
    ]), 
    html.Div([
        html.H1(children='Failed Transactions'),
        dcc.Graph(id = 'big_number4')
    ])    
    ])
    ])

    def date_string_to_date(date_string):
        return pd.to_datetime(date_string, utc=True)

    @app.callback(
        [
        dash.dependencies.Output("datatable-interactivity", "data"),
        dash.dependencies.Output("big_number3", "figure"),
        dash.dependencies.Output("big_number4", "figure"),
        ],
        [
            dash.dependencies.Input("my-date-picker-range", "start_date"),
            dash.dependencies.Input("my-date-picker-range", "end_date"),
        ],
    )
    def update_data(start_date, end_date):
        data = df.to_dict("records")
        if start_date and end_date:
            mask = (date_string_to_date(df["date"]) >= date_string_to_date(start_date)) & (
                    date_string_to_date(df["date"]) <= date_string_to_date(end_date)
            )
            data = df.loc[mask].to_dict("records")
            dff = data
            #print(dff)
            print(start_date)
            print(end_date)
        df3 = Userstagecn.objects.using('canny').all().filter(stage = "Final Response" , stage_result = "SUCCESS").filter(timestamp__gte=start_date, timestamp__lte=end_date).count()
        print(df3)
        fig2 = go.Figure()

        fig2.add_trace(go.Indicator(
        mode = "number",
        value = df3,
        domain = {'row': 0, 'column': 1}))

        df4 = Userstagecn.objects.using('canny').filter(stage_result__in=[ 'Sign Up Failed', 'No channel found', 'Business Name Search Fail', 'Fetch UBO/Director Details Fail', 'Personal Information Error', 'KYC Validation Fail', 'Bank Account Validation Fail', 'Get Value Date Failure', 'AFEX Get Quote Failure', 'Rational Get Quote Failure', 'AFEX Post Deal Failure', 'Rational Post Deal Failure', 'Payment Overview (Post Deal) Fail', 'Manual Bank Transfer Settement Instructions Failure', 'Get Value Date Failure', 'AFEX Get Fee Failure', 'Rational Get Fee Failure', 'Get Quote Failure', 'Post Deal Failure', 'Payment Overview (Post Deal) Fail', 'Manual Bank Transfer Settement Instructions Failure','User does not exist', 'Preview Invoice Email Fail', 'KYC Validation Fail', 'Preview Request Email Fail']).filter(timestamp__gte=start_date, timestamp__lte=end_date).count()

        print(df4)
        fig3 = go.Figure()

        fig3.add_trace(go.Indicator(
        mode = "number",
        value = df4,
        domain = {'row': 0, 'column': 1}))

        return data, fig2, fig3
    
    '''
    @app.callback(Output("download", "data"), [Input("btn", "n_clicks")], prevent_initial_call=True, )
    def generate_csv(n_nlicks):
        return send_data_frame(dff.to_csv, filename=str(round(time.time())) + '.csv')
    
    # for getting big number in the given time range
    @app.callback(
        dash.dependencies.Output("big_number3", "figure"),
        [
            dash.dependencies.Input("my-date-picker-range", "start_date"),
            dash.dependencies.Input("my-date-picker-range", "end_date"),
        ],
    )
    def update_data(start_date, end_date):
        data = df.to_dict("records")
        if start_date and end_date:
            mask = (date_string_to_date(df["date"]) >= date_string_to_date(start_date)) & (
                    date_string_to_date(df["date"]) <= date_string_to_date(end_date)
            )
            data = df.loc[mask].to_dict("records")
            print(start_date)
            print(end_date)
        df3 = Userstagecn.objects.using('canny').all().filter(stage = "Final Response" , stage_result = "SUCCESS").filter(timestamp__gte=start_date, timestamp__lte=end_date).count()
        
        fig2 = go.Figure()

        fig2.add_trace(go.Indicator(
        mode = "number",
        value = df3,
        domain = {'row': 0, 'column': 1}))

        return fig2
    
  '''

    #print(df3)
    #if __name__ == '__main__':
     #   app.run_server(8052, debug=True)
        

    


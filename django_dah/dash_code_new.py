import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
import time

from datetime import datetime as dt
from django_plotly_dash import DjangoDash
from demo.models import Person
import plotly.express as px
import dash_table
import plotly

from dash_extensions.snippets import send_data_frame


def new_plot_clean(**kwargs):
    

    df = pd.DataFrame(Person.objects.filter(**kwargs).values())

    dff = pd.DataFrame(Person.objects.filter(**kwargs).values())

    dff["date"] = pd.to_datetime(dff.date,utc=True)
    dff.index = dff["date"]
    print(dff)


    external_stylesheets=['https://codepen.io/amyoshino/pen/jzXypZ.css']

    # Important: Define Id for Plotly Dash integration in Django
    app = DjangoDash('dash_integration_id')

    app.css.append_css({
    "external_url": external_stylesheets
    })

    app.layout = html.Div([
        html.Div([
            # Adding one extar Div
            html.Div([
                html.H1(children='Multiple Application'),
                html.H3(children='Just for check'),
                html.Div(children='Dash: Python framework to build web application'),
            ], className = 'row'),


        html.Div([html.Button("Download csv", id="btn"), dcc.Download(id="download")]),

             
            html.Div([
                dash_table.DataTable(
                    id='datatable_id',
                    data = df.to_dict('records'),
                    columns = [
                        {"name": i, "id":i,"deletable":False, "selectable":False} for i in df.columns
                    ],
                    editable=False,
                    filter_action="native",
                    sort_action = "native",
                    sort_mode="multi",
                    row_selectable="multi",
                    row_deletable=False,
                    selected_rows=[],
                    #page_action="native",
                    #page_current=0,
                    #page_size=6,
                    page_action='none',
                    style_cell={
                    'whiteSpace':'normal'
                    },
                    fixed_rows={'headers':True, 'data':0},
                    virtualization=False,
                    ),
                ],className='row'),

            html.Div([
                html.Div([
                    dcc.Dropdown(id='bardropdown',
                        options = [
                        {'label': 'income', 'value':'income'},
                        {'label': 'age', 'value':'age'}
                        ],
                        value ='name',
                        multi=False,
                        clearable=False
                        ),
                    ],className='six columns'),

                 html.Div([
                    dcc.Dropdown(id='linedropdown',
                        options = [
                        {'label': 'income', 'value':'income'},
                        {'label': 'age', 'value':'age'}
                        ],
                        value ='name',
                        multi=False,
                        clearable=False
                        ),
                    ],className='six columns'),

                ],className = 'row'),

            html.Div([
                html.Div([
                    dcc.Graph(id='barchart'),
                    ],className='six columns'),

                 html.Div([
                    dcc.Graph(id='linechart'),
                    ],className='six columns'),
                 ],className = 'row'),

            ]),

            html.Div([
            html.Pre(children= "Bar Chart Display",
            style={"text-align": "center", "font-size":"100%", "color":"black"})
        ]),

        html.Div([
            html.Label(['X-axis categories to compare:'],style={'font-weight': 'bold'}),
            dcc.RadioItems(
                id='xaxis_raditem',
                options=[
                         {'label': 'Name', 'value': 'name'},
                         {'label': 'City', 'value': 'city'},
                         {'label': 'Income', 'value': 'income'},
                         {'label': 'Age', 'value': 'age'},

                ],
                value='age',
                style={"width": "50%"}
            ),
        ]),

        html.Div([
            html.Br(),
            html.Label(['Y-axis values to compare:'], style={'font-weight': 'bold'}),
            dcc.RadioItems(
                id='yaxis_raditem',
                options=[
                         {'label': 'Age', 'value': 'age'},
                         {'label': 'Income', 'value': 'income'},
                ],
                value='income',
                style={"width": "50%"}
            ),
        ]),

        html.Div([
            dcc.Graph(id='the_graph')
        ]),

        html.Div(
        [
        dcc.DatePickerRange(
            id="my-date-picker-range",
            min_date_allowed=dt(2021, 1, 1),
            max_date_allowed=dt(2022, 1, 4),
            initial_visible_month=dt(2019, 1, 1),
            end_date=dt(2019, 1, 4),
        ),

        html.Div([html.Button("Download csv", id="btn"), dcc.Download(id="download")]),

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
        ]
        ),



    ])

    @app.callback(Output("download", "data"), [Input("btn", "n_clicks")],prevent_initial_call=True,)
    def generate_csv(n_nlicks):
        return send_data_frame(df.to_csv, filename=str(round(time.time()))+'.csv')
    
    @app.callback(
        [Output('barchart','figure'),
        Output('linechart','figure')],
        [Input('datatable_id','selected_rows'),
        Input('bardropdown','value'),
        Input('linedropdown','value')]
            )

    def update_data(chosen_rows,bardropval,linedropval):
        if len(chosen_rows) == 0:
            df_filtered = df[df['name'].isin(['jack1', 'jack2', 'jack3'])]
        else:
            print(chosen_rows)
            df_filtered = df[df.index.isin(chosen_rows)]


        pie_chart = px.pie(
            data_frame=df_filtered,
            names='name',
            values=bardropval,
            hole=.3,
            labels={'name':'person data'}
            )

        list_chosen=df_filtered['name'].tolist()
        df_line = df[df['name'].isin(list_chosen)]
        print(df_line)
        line_chart=px.line(
            data_frame=df_line,
            x='income',
            y=linedropval,
            color='name',
            labels={'name':'person', 'income':'Income'},
            )
        line_chart.update_layout(uirevision='foo')

        return (pie_chart,line_chart)

    @app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='xaxis_raditem', component_property='value'),
     Input(component_id='yaxis_raditem', component_property='value')]
    )

    def update_graph(x_axis, y_axis):

        dff = df
        # print(dff[[x_axis,y_axis]][:1])

        barchart=px.bar(
                data_frame=dff,
                x=x_axis,
                y=y_axis,
                title=y_axis+': by '+x_axis,
                #facet_col='Borough',
                #color='Borough',
                # barmode='group',
                )

        barchart.update_layout(xaxis={'categoryorder':'total ascending'},
                               title={'xanchor':'center', 'yanchor': 'top', 'y':0.9,'x':0.5,})

        return (barchart)

    def date_string_to_date(date_string):
        return pd.to_datetime(date_string, utc=True)



    @app.callback(
        dash.dependencies.Output("datatable-interactivity", "data"),
        [
            dash.dependencies.Input("my-date-picker-range", "start_date"),
            dash.dependencies.Input("my-date-picker-range", "end_date"),
        ],
    )

    def update_data(start_date, end_date):
        data = dff.to_dict("records")
        if start_date and end_date:
            mask = (date_string_to_date(df["date"]) >= date_string_to_date(start_date)) & (
                date_string_to_date(df["date"]) <= date_string_to_date(end_date)
            )
            data = dff.loc[mask].to_dict("records")
        return data

    if __name__ == '__main__':
        app.run_server(8052, debug=True)

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

'''

df = pd.DataFrame(Person.objects.all().values())
dff = df.groupby('city',as_index=False)[['age','income']].sum()
print(dff)

# Important: Define Id for Plotly Dash integration in Django
app = DjangoDash('dash_integration_id')



app.layout = html.Div(
    html.Div([
        # Adding one extar Div
        html.Div([
            html.H1(children='Multiple Application'),
            html.H3(children='Indian Population over time'),
            html.Div(children='Dash: Python framework to build web application'),
        ], className = 'row'),
         

        html.Div([
            html.Div([
                dcc.Graph(
                    id='bar-chart',
                    figure={
                        'data': [
                            {'x': df['income'], 'y': df['age'], 'type': 'bar', 'name': 'SF'},
                        ],
                        'layout': {
                            'title': 'Bar Chart Visualization'
                        }
                    }
                ),
            ], className = 'six columns'),

            # Adding one more app/component
            html.Div([
                dcc.Graph(
                    id='line-chart',
                    figure={
                        'data': [
                            {'x': df['income'], 'y': df['age'], 'type': 'line', 'name': 'SF'},
                        ],
                        'layout': {
                            'title': 'Line Chart Visualization'
                        }
                    }
                )
            ], className = 'six columns')

        ], className = 'row')
    ])
)

if __name__ == '__main__':
    app.run_server(8052, debug=False)

----------------------------------------------------------------------------------------------------------


df = px.data.gapminder().query("country=='India'")

external_stylesheets=['https://codepen.io/amyoshino/pen/jzXypZ.css']

# Important: Define Id for Plotly Dash integration in Django
app = DjangoDash('dash_integration_id')

app.css.append_css({
"external_url": external_stylesheets
})
app.layout = html.Div(
    html.Div([
        # Adding one extar Div
        html.Div([
            html.H1(children='Multiple Application'),
            html.H3(children='Indian Population over time'),
            html.Div(children='Dash: Python framework to build web application'),
        ], className = 'row'),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='bar-chart',
                    figure={
                        'data': [
                            {'x': df['year'], 'y': df['pop'], 'type': 'bar', 'name': 'SF'},
                        ],
                        'layout': {
                            'title': 'Bar Chart Visualization'
                        }
                    }
                ),
            ], className = 'six columns'),

            # Adding one more app/component
            html.Div([
                dcc.Graph(
                    id='line-chart',
                    figure={
                        'data': [
                            {'x': df['year'], 'y': df['pop'], 'type': 'line', 'name': 'SF'},
                        ],
                        'layout': {
                            'title': 'Line Chart Visualization'
                        }
                    }
                )
            ], className = 'six columns')

        ], className = 'row')
    ])
)

if __name__ == '__main__':
    app.run_server(8052, debug=False)
'''

df = pd.DataFrame(Person.objects.all().values())

df1 = pd.DataFrame(Person.objects.all().values())
df1['date'] = pd.to_datetime(df1['date'])
df1.set_index('date', inplace=True)

#dff = df.groupby('city',as_index=False)[['age','income']].sum()

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
            html.H3(children='Indian Population over time'),
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

    html.Div([
    dcc.DatePickerRange(
        id='my-date-picker-range',  # ID to be used for callback
        calendar_orientation='horizontal',  # vertical or horizontal
        day_size=39,  # size of calendar image. Default is 39
        end_date_placeholder_text="Return",  # text that appears when no end date chosen
        with_portal=False,  # if True calendar will open in a full screen overlay portal
        first_day_of_week=0,  # Display of calendar when open (0 = Sunday)
        reopen_calendar_on_clear=True,
        is_RTL=False,  # True or False for direction of calendar
        clearable=True,  # whether or not the user can clear the dropdown
        number_of_months_shown=1,  # number of months shown when calendar is open
        min_date_allowed=dt(2020, 1, 1),  # minimum date allowed on the DatePickerRange component
        max_date_allowed=dt(2021, 10, 20),  # maximum date allowed on the DatePickerRange component
        initial_visible_month=dt(2020, 5, 1),  # the month initially presented when the user opens the calendar
        start_date=dt(2018, 8, 7).date(),
        end_date=dt(2020, 5, 15).date(),
        display_format='MMM Do, YY',  # how selected dates are displayed in the DatePickerRange component.
        month_format='MMMM, YYYY',  # how calendar headers are displayed when the calendar is opened.
        minimum_nights=2,  # minimum number of days between start and end date

        persistence=True,
        persisted_props=['start_date'],
        persistence_type='session',  # session, local, or memory. Default is 'local'

        updatemode='singledate'  # singledate or bothdates. Determines when callback is triggered
    ),

    html.H3("Implementing date filter", style={'textAlign': 'center'}),
    dcc.Graph(id='datatble__id'),

])


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
    #print(df_line)
    line_chart=px.line(
        data_frame=df_line,
        x='date',
        y=linedropval,
        color='name',
        #labels={'name':'person', 'income':'Income'},
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

@app.callback(
    Output('datatble__id', 'figure'),
    [Input('my-date-picker-range', 'start_date'),
     Input('my-date-picker-range', 'end_date')]
)

def update_output1(start_date, end_date):
    # print("Start date: " + start_date)
    # print("End date: " + end_date)
    print(df1)
    dfff = df1.loc[start_date:end_date]
    print(dfff)

    fig = dash_table.DataTable(
        data=dfff.to_dict('records'),
        id='datatable_id',
        columns=[{"name": i, "id": i} 
                 for i in dfff.columns],
         )
    return fig



#---------------------------------------------------------------
'''
            html.Div([
                dcc.Graph(
                    id='bar-chart',
                    figure={
                        'data': [
                            {'x': df['income'], 'y': df['age'], 'type': 'bar', 'name': 'SF'},
                        ],
                        'layout': {
                            'title': 'Bar Chart Visualization'
                        }
                    }
                ),
            ], className = 'six columns'),

            # Adding one more app/component
            html.Div([
                dcc.Graph(
                    id='line-chart',
                    figure={
                        'data': [
                            {'x': df['income'], 'y': df['age'], 'type': 'line', 'name': 'SF'},
                        ],
                        'layout': {
                            'title': 'Line Chart Visualization'
                        }
                    }
                )
            ], className = 'six columns')

        ], className = 'row')
    ])
)


if __name__ == '__main__':
    app.run_server(8052, debug=True)


'''


def new_plot(name):

    df = pd.DataFrame(Person.objects.filter(name=name).values())

#dff = df.groupby('city',as_index=False)[['age','income']].sum()

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
                html.H3(children='Indian Population over time'),
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

    if __name__ == '__main__':
        app.run_server(8052, debug=True)











def new_plot1(city):

    df = pd.DataFrame(Person.objects.filter(city=city).values())

#dff = df.groupby('city',as_index=False)[['age','income']].sum()

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
                html.H3(children='Indian Population over time'),
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

    if __name__ == '__main__':
        app.run_server(8052, debug=True)

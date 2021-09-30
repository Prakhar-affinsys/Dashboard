import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
import time


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

    app.layout = html.Div(
        html.Div([
            # Adding one extar Div
            html.Div([
                html.H1(children='Multiple Application'),
                html.H3(children='Indian Population over time'),
                html.Div(children='Dash: Python framework to build web application'),
            ], className = 'row'),
             
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

            ])

    )

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

    if __name__ == '__main__':
        app.run_server(8052, debug=True)

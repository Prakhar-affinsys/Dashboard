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


def new_dash(**kwargs):
    '''
	df1 = pd.DataFrame(Person.objects.filter(**kwargs).values())
	df1["date"] = pd.to_datetime(df1["date"],unit="ns", utc=True)
	#df1.index = df1["date"]
	print(df1)

	

	external_stylesheets=['https://codepen.io/amyoshino/pen/jzXypZ.css']
	app = DjangoDash('dash_integration_id')

	app.css.append_css({
	"external_url": external_stylesheets
	})
	
	app.layout = html.Div(
	[

	html.Div([html.Button("Download csv", id="btn"), dcc.Download(id="download")]),
	
	 html.Div(
		[
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
				for i in df1.columns
			],
			data=df1.to_dict("records"),  # the contents of the table
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
		])
	]
	)

	@app.callback(Output("download", "data"), [Input("btn", "n_clicks")],prevent_initial_call=True,)
	def generate_csv(n_nlicks):
		return send_data_frame(df1.to_csv, filename=str(round(time.time()))+'.csv')

	def date_string_to_date(date_string):
		return pd.to_datetime(date_string, infer_datetime_format=True)


	@app.callback(
		dash.dependencies.Output("datatable-interactivity", "data"),
	[
		dash.dependencies.Input("my-date-picker-range", "start_date"),
		dash.dependencies.Input("my-date-picker-range", "end_date"),
	],
	)

	def update_data(start_date, end_date):
		data = df1.to_dict("records")
		print(df1[:2])
		if start_date and end_date:
			mask = (date_string_to_date(df1["date"]) >= date_string_to_date(start_date)) & (
				date_string_to_date(df1["date"]) <= date_string_to_date(end_date)
			)
			data = df1.loc[mask].to_dict("records")
		return data

	if __name__ == '__main__':
		app.run_server(8052, debug=True)

	'''
    df1 = pd.DataFrame(Person.objects.filter(**kwargs).values())
    # 	df1["date"] = pd.to_datetime(df1.date,utc=True)
    # 	df1.index = df1["date"]
    # 	print(df1)
    #
    # 	dff = pd.DataFrame()
    #
    # 	external_stylesheets=['https://codepen.io/amyoshino/pen/jzXypZ.css']
    # 	app = DjangoDash('dash_integration_id')
    df1["date"] = pd.to_datetime(df1['date'], utc=True)
    app = DjangoDash('dash_integration_id')

    app.layout = html.Div(
        [

            html.Div([
                dcc.DatePickerRange(
                    id="my-date-picker-range",
                    min_date_allowed=dt(2021, 1, 1),
                    max_date_allowed=dt(2022, 1, 4),
                    initial_visible_month=dt(2019, 1, 1),
                    end_date=dt(2019, 1, 4),
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
                        for i in df1.columns
                    ],
                    data=df1.to_dict("records"),  # the contents of the table
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

        ]
    )

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
        data = df1.to_dict("records")
        if start_date and end_date:
            mask = (date_string_to_date(df1["date"]) >= date_string_to_date(start_date)) & (
                    date_string_to_date(df1["date"]) <= date_string_to_date(end_date)
            )
            data = df1.loc[mask].to_dict("records")
            dff = data
        return data

    @app.callback(Output("download", "data"), [Input("btn", "n_clicks")], prevent_initial_call=True, )
    def generate_csv(n_nlicks):
        return send_data_frame(dff.to_csv, filename=str(round(time.time())) + '.csv')

    if __name__ == "__main__":
        app.run_server(8052, debug=True)

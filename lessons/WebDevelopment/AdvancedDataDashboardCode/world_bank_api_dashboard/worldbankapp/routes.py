from worldbankapp import app

import json, plotly
from flask import render_template, request, Response, jsonify
from scripts.data import return_figures


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():

	# List of countries for filter
	country_codes = [['Canada','CAN'],['United States','USA'],['Brazil','BRA'],
	['France','FRA'],['India','IND'],['Italy','ITA'],['Germany','DEU'],
	['United Kingdom','GBR'],['China','CHN'],['Japan','JPN']]

	countries_selected = []

	# Parse the POST request countries list
	if (request.method == 'POST') and request.form:
		figures = return_figures(request.form)
		countries_selected.extend(country[1][0] for country in request.form.lists())
	else:
		figures = return_figures()
		countries_selected.extend(country[1] for country in country_codes)
	# plot ids for the html id tag
	ids = [f'figure-{i}' for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	return render_template('index.html', ids=ids,
		figuresJSON=figuresJSON,
		all_countries=country_codes,
		countries_selected=countries_selected)
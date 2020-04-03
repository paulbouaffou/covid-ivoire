#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Paul Bouaffou

from flask import Flask
from flask import render_template
from flask import request
import functions

app = Flask(__name__)

@app.route("/")
def home():

	# API(format JSON) of COVID-19 data in Ivory Cost 
	url = "https://corona.lmao.ninja/countries/civ"

	# Resultat JSON
	info = functions.resultatJson(url)
	
	# Cases confirmed 
	info_cases = int(info['cases'])

	# Deaths 
	info_deaths = int(info['deaths'])

	# Recovered
	info_recovered = int(info['recovered'])

	# Cases active
	info_active = int(info['active'])

	#return home page
	return render_template('index.html', title = "Covid Ivoire | Site de la situation du COVID-19 en Côte d'Ivoire", info_cases=info_cases, info_deaths=info_deaths, info_recovered=info_recovered, info_active=info_active)

# Execute the application
if __name__ == '__main__':
	app.run()
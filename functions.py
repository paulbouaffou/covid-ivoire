#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Paul Bouaffou
# Description: Functions utils
# License: MIT

import requests
import json

# ----- Start function resultatJson -----

def resultatJson(url):

	# To give resultat of url request
	content=requests.get(url)
	data=content.json()

	return data 

# ----- End function resultatJson -----



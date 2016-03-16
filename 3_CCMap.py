#!/usr/bin/python

import requests
import json
url = 'https://restcountries.eu/rest/v1/all'
response = requests.get(url)

j_obj = json.loads(response.text)

#count = 0
data = {}

for country in j_obj:
	conti = str(country['region'])

	if conti == "":
		conti == "unknown"

	if conti not in data.keys():
		data[conti] = {}

	data[conti][str(country['name'])]=[]
		
	#count = count + 1
	#if count > 10:
	#	break

#print (data)

f1 = open('Conti_country_mapping.json', 'w')
f1.write(json.dumps(data))
f1.close()


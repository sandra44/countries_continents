#!/usr/bin/python

import requests
import json
url = 'https://restcountries.eu/rest/v1/all'
response = requests.get(url)

j_obj = json.loads(response.text)

#count = 0
data = {}

for country in j_obj:

	if country['region'] not in data.keys():
		data[country['region']] = {}

	data[country['region']][country['name']]=[]
		
	#count = count + 1
	#if count > 10:
	#	break

print (data)

f1 = open('final.json', 'w')
f1.write(json.dumps(data))
f1.close()


import requests
import json
url = 'https://restcountries.eu/rest/v1/all'
response = requests.get(url)
output = {}
for items in json.loads(response.text):
	if str(items["region"]) in output.keys():
		output[str(items['region'])].update({str(items['name']) : []})
	else:
		output[str(items['region'])] = {str(items['name']) : []}

with open('geophysicaldata.json', 'w') as outfile:
    json.dump(output, outfile)
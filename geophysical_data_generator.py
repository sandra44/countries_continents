import requests
import json
url = 'https://restcountries.eu/rest/v1/all'
response = requests.get(url)
output = {}

f = open("author_final.json","r")
j = json.loads(f.read())

for items in json.loads(response.text):
	temp = str(items["name"])
	if str(items["region"]) in output.keys():
		output[str(items["region"])].update({str(items["name"]) : {"subregion": str(items["subregion"]), "area": str(items["area"]), "gini": str(items["gini"]), "cities" : []}})
	else:
		output[str(items["region"])] = {str(items["name"]) : {"subregion": str(items["subregion"]), "area": str(items["area"]), "gini": str(items["gini"]), "cities" : []}}

	if temp in j.keys():
		output[items["region"]][items["name"]]["cities"]=j[temp]		

with open('geophysicaldata.json', 'w') as outfile:
    json.dump(output, outfile)

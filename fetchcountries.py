# Run this script by typing python3 fetchcountries.py

# Import modules
import requests
import json

# Define url
url = 'https://restcountries.eu/rest/v1/all'

# Send a GET request to the URL and capture result in "response" variable
response = requests.get(url)

# parse the "text" part of "response" as JSON.
# The response structure is a list of dictionaries --> [{"name":"Afganistan",...}, {"name":"Afganistan2",...}, {"name":"Afganistan3",...s}]
for items in json.loads(response.text):
	print(items['name'])


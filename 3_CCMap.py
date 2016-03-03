#!/usr/bin/python
import urllib2
import json


j = urllib2.urlopen('http://restcountries.eu/rest/v1/all')
j_obj = json.load(j)

data = {}
temp = {}
for country in j_obj:
        if country['region'] in data.keys():
                temp=data[country['region']]
                temp[country['name']]=[]
        else:
                temp[country['name']]=[]
                data[country['region']]=temp

final = json.dumps(data)

#print final

f1 = open('final.json', 'w')
f1.write(final)
f1.close()

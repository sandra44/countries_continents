#!/usr/bin/python
import urllib2
import json


j = urllib2.urlopen('http://restcountries.eu/rest/v1/all')
j_obj = json.load(j)
continent = []
for country in j_obj:
        temp = country ['region']
        if temp in continent:
                continue
        continent.append(temp)

print continent
print '\n\n\n'

list_of_cities = []
dict_of_continents = {}
for conti in continent:
        dict_of_countries = {}
        for country in j_obj:
                if country ['region']== conti:
                        dict_of_countries[country['name']] = list_of_cities

        dict_of_continents[conti] = dict_of_countries


final = json.dumps(dict_of_continents)

print final
 
f1 = open('final.json', 'w')
f1.write(final)
f1.close()



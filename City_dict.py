# -*- coding: utf-8 -*-

import pycountry
from bs4 import BeautifulSoup
import urllib, sys
import json


t = list(pycountry.countries)
country_codes = []
country_name = []
for country in t:
    country_codes.append(country.alpha2)
    country_name.append(country.name)



city1 = {}



for code,name1 in zip(country_codes,country_name):   
    i = 0
    city1[name1] = []
    while i <= 50:
        url = "http://www.geonames.org/search.html?q=&country=" + code + "&startRow=" + str(i)
        i += 50
        hdr = {'User-Agent' : 'Chrome/6.0'}
        req = urllib.request.Request(url, headers = hdr)
        page = urllib.request.urlopen(req)
        soup = BeautifulSoup(page, 'html.parser')
        cities = soup.find('table', {'class':'restable'}).find_all('tr')
        for city in cities[2:len(cities)-1:]:
            links = city.find_all('td')[1]
            name2 = links.find_all('a')[0]
            city1[name1].append(name2.get_text())
ß
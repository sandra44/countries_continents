import urllib2 from urlopen,Request

world = { asia = {},africa = {},europe = {},americas = {},oceania = {} }


for continent in world:
      c = Request('https://restcountries.eu/rest/v1/region/continent')
      continent = c.read()
    

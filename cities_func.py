
from SPARQLWrapper import SPARQLWrapper, JSON



sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
SELECT DISTINCT ?citylabel ?countrylabel ?pop
WHERE {
   ?city rdf:type dbo:City.
   ?city rdfs:label ?citylabel.
   ?city dbo:country ?country.
   ?country rdfs:label ?countrylabel.
   ?city dbo:populationTotal ?pop .
   FILTER (lang(?countrylabel)='en' and lang(?citylabel) = 'en' and ?pop>10000)

}
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
def city_list():
        #print (results)
        j=[]
        #f1 = open('city_output','w')

        for result in results["results"]["bindings"]:
                j.append(result["citylabel"]["value"])

                #print result["citylabel"]["value"]
                #f1.write(result["citylabel"]["value"])


        #f1.close()
        #print j[0:len(j)]
        return j
                 


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

for result in results["results"]["bindings"]:
    print(result["citylabel"]["value"])

#!usr/bin/python


import json

import cities_func 

f2 = open("ieee_author_1-40k.json","r")
author = json.loads(f2.read())
#print author
f2.close()
j2 = cities_func.city_list()

def isCity(given_city):
	if given_city in j2:
		return True
	else:
		return False
			

unknown = "unknown"
info = {}
final_info = {}
#count = 0
f3 = open("organised.json","w")
for every in author:
	affiliation = every["affiliation"].split(',')
	#print affiliation
	length = len(affiliation)
	name = every["first_name"] + "_" + every["last_name"]
	country = every["country"]
	#print length
	if length == 0:
		city = unknown
                state = unknown
                dept = unknown
                inst = unknown

	elif length == 1: 
		city = unknown
                state = unknown
                dept = unknown
                inst = affiliation[0]

	elif length == 2:
		if isCity(affiliation[1]):
			city = affiliation[1]
			state = unknown
			dept = unknown
			inst = affiliation[0]
		#else:

	elif length == 3:
		if isCity(affiliation[2]):
			city = affiliation[2]
			state = unknown
			dept = affiliation[0]
			inst = affiliation[1]

		elif isCity(affiliation[1]):
			city = affiliation[1]
                        state = affiliation[2]
                        dept = unknown
                        inst = affiliation[0]
		
		#else:


	else:
                city = affiliation[2]
                state = affiliation[3]
                dept = affiliation[0]
                inst = affiliation[1]
	
	info={"first_name" : every["first_name"], "last_name" : every["last_name"], "dept" : dept, "institute/university" : inst, "city" : city, "state" : state, "country" : country}
	final_info[name]= info
	f3.write(json.dumps(final_info))
	#count = count + 1
	#if count > 5:
	#	break

print final_info		
	


f3.close()


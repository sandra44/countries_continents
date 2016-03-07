#!usr/bin/python


import json

import cities_func

f2 = open("ieee_author_affiliation.json","r")
author = json.loads(f2.read())
#print author
f2.close()
j2 = cities_func.city_list()
f4 = open("city_output","w")
f4.write(str(j2))
f4.close()

unknown = "unknown"
info = {}
final_info = {}
#count = 0
f3 = open("organised.json","w")
j=0
auth_name = ""

def isCity(given_city):
        if given_city in j2:
                return True
        else:
                return False

def isCountry(aff_list):
	#j=0
	flag = False
	for s in aff_list:
		if any(i in s for i in['|C|','|c|']):#if '|c|' in s:
			flag = True
			global j 
			j = aff_list.index(s)
			return s.strip('|c|').strip('|C|')

	if flag == False:
		return unknown		 

def name_func(name_list): 
	name_len = len(name_list)
	if name_len == 1:
		info = {"first_name" : name_list[0], "last_name" : unknown}
		auth_name = name_list[0]
	else:
		if name_len == 3:
			info = {"suffix" : name_list[2]}
		info = {"first_name" : name_list[1], "last_name" : name_list[0]}
		auth_name = name_list[1] + "_" + name_list[0]
		if name_len == 3:
			auth_name = auth_name + "_" + name_list[2]
	return auth_name

for every in author:
        affiliation1 = every["author_affiliations"].replace('.',' ').split(',')
	affiliation = [p.strip() for p in affiliation1]
        #print affiliation
        length = len(affiliation)
	#print length
	name2 = every["author_name"].replace('.',' ').split(', ')
	name1 = [p.strip() for p in name2]
	name = name_func(name1)
	#print name
	country = isCountry(affiliation)		
	#print country
	if length == 1:
		state = unknown
                city = unknown
                inst = unknown
                dept = unknown

        elif length == 2:
		state = unknown
		city = unknown
		inst = affiliation[j-1]
		dept = unknown
	
	elif length == 3:
		if isCity(affiliation[j-1]):
			state = unknown
			city = affiliation[j-1]
			inst = affiliation[j-2]
			dept = unknown
		# else part includes two cases 1) institute,state,country 2) dept,institute,country

	elif length == 4:
		if isCity(affiliation[j-1]):
			state = unknown
			city = affiliation[j-1]
			inst = affiliation[j-2]
			dept = affiliation[j-3]

		elif isCity(affiliation[j-2]):
			state = affiliation[j-1]
                        city = affiliation[j-2]
                        inst = affiliation[j-3]
                        dept = unknown
			
		else:
			state = affiliation[j-1]
                        city = unknown
                        inst = affiliation[j-2]
			dept = affiliation[j-3]

	else:
                state = affiliation[j-1]
		city = affiliation[j-2]
                inst = affiliation[j-3]
                dept = affiliation[j-4]

        info={"dept" : dept, "institute/university" : inst, "city" : city, "state" : state, "country" : country}
        final_info[name]= info
	#print info,"\n\n\n"
        #count = count + 1
        #if count >= 3:
        #        break

f3.write(json.dumps(final_info))

#print json.dumps(final_info)

f3.close()

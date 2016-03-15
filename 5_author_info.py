#!usr/bin/python


import json

import cities_func

f2 = open("ieee_author_affiliation.json","r")
author = json.loads(f2.read())
f2.close()

j2 = cities_func.city_list()

unknown = "unknown"
info = {}
final_info = {}
count = 0
f3 = open("author.json","w")
j=0

def isCity(given_city):
	for every in j2:
        	if given_city in every:
                	return True
        return False


def isCountry(aff_list):
	flag = False
	for s in aff_list:
		if '|c|' in s:
			flag = True
			global j
 			j = aff_list.index(s)
			return s.strip('|c|')

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

def initialise():

	global state
	state = unknown
	global city
	city = unknown
	global inst
	inst = unknown
	global dept
	dept = unknown
	global country
	country = unknown
	global name
	name = unknown
	return

"""
def inst_dept(num,affiliation):

	if num-1 >= 0:
		global inst
		inst = affiliation[num]
		num = num-1

	if num-1 >= 0:
		global dept
		dept = affiliation[num]
		num = num-1

	return num
"""

for every in author:
	initialise()
	nocity = True
        affiliation1 = every["author_affiliations"].replace('.',' ').split(',')
	affiliation = [p.strip() for p in affiliation1]
	name2 = every["author_name"].replace('.',' ').split(', ')
	name1 = [p.strip() for p in name2]
	name = name_func(name1)
	country = isCountry(affiliation)		
	if not(country == unknown):
		k=j
		k=k-1
		if k >= 0:
			if isCity(affiliation[k]):

				city = affiliation[k]
				nocity = False

			elif k-1 >=0 and  isCity(affiliation[k-1]):
				
				k=k-1
				state = affiliation[k+1]
				city = affiliation[k]
				nocity = False
		
	
		if nocity == False:	
		#	k=inst_dept(k,affiliation)
		
			if k-1 >= 0:
				inst = affiliation[k-1]
				k = k-1
	
			if k-1 >= 0:
				dept = affiliation[k-1]
	
	
		else:
		#	j=inst_dept(j,affiliation)
		
			if j-1 >= 0:
				inst = affiliation[j-1]
				j=j-1
			if j-1 >= 0:
				dept = affiliation[j-1]
			 
	info={"dept" : dept , "institute/university" : inst , "city" : city , "state" : state, "country" : country}
	final_info[name]= info


f3.write(json.dumps(final_info))

#print json.dumps(final_info)

f3.close()	 

from IMDB_task_1 import *
from IMDB_task_4 import *
from IMDB_task_5 import *

# Task-6
#This function returns a dictionary that states how many movies fall in a particular language
def analyse_movies_language(movies_list):
	lang=[]
	unique_lang=[]
	store={}

	for i in movies_list:  #Iterating loop over all movies while holding one dictionary key in 'j' at a time
		for j in i["Language"]:  #Iterating loop over the 'Languages' key of each movie dictionary
			lang.append(j)	

	for i in lang:
		if i not in unique_lang:
			unique_lang.append(i)

	for i in unique_lang:
		count=0  #Creating key of every language and assigning its initial value 0
		for j in lang:
			if i==j:
				count+=1   #Incrementing the value if languages match
		store[i]=count #Creating key of every language and assigning its initial value 0

	return store

pprint(analyse_movies_language(movies_list))

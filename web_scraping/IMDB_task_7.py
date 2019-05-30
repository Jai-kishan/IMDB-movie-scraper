from IMDB_task_1 import *
from IMDB_task_4 import *
from IMDB_task_5 import *

#Task 7
#This function returns a dictionary that states how many movies each director made
def analyse_movies_directors(movies_list):
	director=[]
	unique_director=[]
	store={}	

	for i in movies_list:  #Iterating loop over all movies
		for j in i["Director"]: #Iterating loop over 'Directors' list of each movie
			director.append(j)

	for i in director:
		if i not in unique_director: #Iterating loop over newly created dictionary
			unique_director.append(i)

	for i in unique_director:
		count=0
		for j in director:  #Iterating loop over 'Directors' list of each movie
			if i == j :
				count+=1 #Incrementing the value if directors match
		store[i]=count

	return store

pprint(analyse_movies_directors(movies_list))

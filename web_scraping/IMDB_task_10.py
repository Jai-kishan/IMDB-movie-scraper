from IMDB_task_9 import *

# Task_10
#This function returns a dictionary stating numbers of movies in each language for each directors
def analyse_language_and_directors(movies_list):
	list_of_directors={}
	for i in movies_list:
		for director in i["Director"]:
			list_of_directors[director]={}  #Creating dictionary key for each director


	for i in range(len(movies_list)):  #Iterating loop over all movies
		for director in list_of_directors:  #Iterating loop over newly created dictionary
			if director in movies_list[i]["Director"]:
				for lang in movies_list[i]["Language"]: #Creating a new key of the language
					list_of_directors[director][lang]=0 

	for i in range(len(movies_list)):
		for director in list_of_directors:
			if director in movies_list[i]["Director"]:   #Iterating loop over 'Directors' key of each movie
				for lang in movies_list[i]["Language"]:
					list_of_directors[director][lang]+=1   #Incrementing the value if it already exists

	return list_of_directors

pprint(analyse_language_and_directors(movies_list))
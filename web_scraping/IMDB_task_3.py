from IMDB_task_1 import *
# Task-3
# Task 2 mein humne movies ko year ke hisaab se group karne ka code toh likh liya. 
# Ab hum inn hi movies ko decade ke hisaab se group karenge. 10 saal se milakar ek decade banta hai. Jaise:

#This function return Top 250 movies sorted in decades they are released in
def group_by_decade(movies): 
	start_year=1950
	lst_of_year=[]
	decade_year=[]
	movie_list_by_decade = []

	#All movies details mein se "Movie year" ke key ko call krke ek list me all year ko stroe krenge
	for i in movies:
		lst_of_year.append(i["Movie Year"])
		lst_of_year.sort()

	#Now we need to store decade fro storeing data decades wise
	for i in range(start_year,lst_of_year[-1],10):
		decade_year.append(i)

	#sort reverse list
	decade_year.sort(reverse=True)

	for i in decade_year:
		movie_store_in_dict={}
		movie_store_in_dict[i] = []  #Creating keys of the decades in which the movies were released
		for j in movies:
			if j["Movie Year"] >= i and j["Movie Year"] <= i+9:
				movie_store_in_dict[i].append(j)  #Appending all movies of same decades in a list
		movie_list_by_decade.append(movie_store_in_dict)
	
	return (movie_list_by_decade)
pprint(group_by_decade(movies))

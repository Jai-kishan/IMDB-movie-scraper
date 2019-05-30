from IMDB_task_1 import *
from IMDB_task_4 import *
#task 5 
#pichle task-4 me humne bas ek movie ki Details nikali thi ab hume top 250 movies ke details nikali hai 

#This function returns a list with many major details of many movies
def get_movie_list_details(movies_list):

	url_lst=[]
	top_movies=[]
	for i in movies_list[:2]:
		url_lst.append(i["URL"]) #Calling 4th function for 250 movies
	
	for url in url_lst:
		top_movies.append(scrape_movie_details(url))   #Appending the returned data into a list
	
	return top_movies

movies_list=(get_movie_list_details(movies))
# pprint(movies_list)

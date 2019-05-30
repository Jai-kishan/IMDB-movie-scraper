from IMDB_task_1 import *
#Task 2
#This functions returns Top 250 movies sorted in a list according to year they are released in
def group_by_year(movies):
	lst_of_year=[]
	yearly_movies={}
	for i in movies:
		if i["Movie Year"] not in lst_of_year:
			lst_of_year.append(i["Movie Year"])   #Creating keys of every year in which movies are released

	#this mehthos use for sort the list element reverse
	lst_of_year.sort(reverse=True)
	print(lst_of_year)
	for j in lst_of_year:
		same_year=[]
		for k in movies:
			if j==k["Movie Year"]:
				same_year.append(k) #Appending movies in the key of the year they were released in
		yearly_movies[j]=same_year
	return yearly_movies
pprint(group_by_year(movies))

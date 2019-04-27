from urllib.request import urlopen
# Beautiful Soup is a Python library for pulling data out of HTML and XML files.
from bs4 import BeautifulSoup
#pprint — Data pretty printer. 
#The pprint module provides a capability to “pretty-print” arbitrary Python data structures in a form which can be used as input to the interpreter.
from pprint import pprint
import os.path ##The OS module in python provides functions for interacting with the operating system.

#The JSON module is mainly used to convert the python dictionary above into a JSON string that can be written into a file.
#While the JSON module will convert strings to Python datatypes,
#normally the JSON functions are used to read and write directly from JSON files
import json

# Task 1
# This function returns list of Top 250 movies according to IMDB with minor details
def scrape_top_list():
	if os.path.exists("Top_250_movies.json"):
		with open("Top_250_movies.json") as file:
			#Python has a built-in function open() to open a file.
			#This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.
			read_file=file.read()
			file_store=json.loads(read_file)
		return file_store

	imdb_url=urlopen("https://www.imdb.com/india/top-rated-indian-movies/") # Scraping data of this URL
	soup=BeautifulSoup(imdb_url, "lxml") # Parsing data that we get from requests
	main_div=soup.find("tbody", class_="lister-list")  # Finding the first 'tbody' tag whose class is "lister-list"
	table_row=main_div.find_all("tr") # Finding all 'tr' tags

	movie_detail=[]
	for tr in table_row:

		#movie position 
		position=tr.find("td",class_="titleColumn").get_text().strip().split() # Getting Rank from 'td' tag
		position=int(position[0].strip("."))

		#Movie Name
		movie_name=tr.find("td",class_="titleColumn").a.get_text()  # Getting Name from 'td' tag

		#Movie Year
		movie_year=tr.find("td",class_="titleColumn").span.get_text() # Getting Year from 'td' tag
		movie_year=movie_year.replace("(","").replace(")","")

		#Movie Rating
		rating=tr.find("td",class_="imdbRating").strong.get_text()  # Geting Rating from 'td' tag

		#Movie URL
		url="https://www.imdb.com"
		make_url=tr.find("td",class_="titleColumn").a["href"] # Getting URL of the movie
		for i in make_url:
			if "?" in i:
				break
			else:
				url+=i
		
		store={
		"position":position,
		"Movie Name":movie_name,
		"Movie Year":int(movie_year),
		"Rating":float(rating),
		"URL":url
		}
		
		movie_detail.append(store)

	# return(movie_detail)
	with open("Top_250_movies.json","w") as file:
		json.dump(movie_detail,file,indent=4)
	return movie_detail


movies=scrape_top_list()
# pprint(movies)


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
# pprint(group_by_year(movies))

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
		print(decade_year)

	#sort reverse list
	decade_year.sort(reverse=True)

	for i in decade_year:
		movie_store_in_dict={}
		movie_store_in_dict[i] = []  #Creating keys of the decades in which the movies were released
		for j in movies:
			if j["Movie Year"] >= i and j["Movie Year"] <= i+9:
				movie_store_in_dict[i].append(j)  #Appending all movies of same decades in a list
		movie_list_by_decade.append(movie_store_in_dict)
	
	# return (movie_list_by_decade)
(group_by_decade(movies))

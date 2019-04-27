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

def scrape_top_list():
	if os.path.exists("Top_250_movies.json"):
		with open("Top_250_movies.json") as file:
			read_file=file.read()
			file_store=json.loads(read_file)
		return file_store

	imdb_url=urlopen("https://www.imdb.com/india/top-rated-indian-movies/")
	soup=BeautifulSoup(imdb_url, "lxml")
	main_div=soup.find("tbody", class_="lister-list")
	table_row=main_div.find_all("tr")

	movie_detail=[]
	for tr in table_row:

		#for movie position 
		position=tr.find("td",class_="titleColumn").get_text().strip().split()
		position=int(position[0].strip("."))

		#Movie Name
		movie_name=tr.find("td",class_="titleColumn").a.get_text()

		#Movie Year
		movie_year=tr.find("td",class_="titleColumn").span.get_text()
		movie_year=movie_year.replace("(","").replace(")","")

		#Movie Rating
		rating=tr.find("td",class_="imdbRating").strong.get_text()

		#Movie URL
		url="https://www.imdb.com"
		make_url=tr.find("td",class_="titleColumn").a["href"]
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

# Task-3
# Task 2 mein humne movies ko year ke hisaab se group karne ka code toh likh liya. 
# Ab hum inn hi movies ko decade ke hisaab se group karenge. 10 saal se milakar ek decade banta hai. Jaise:
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
		movie_store_in_dict[i] = []
		for j in movies:
			if j["Movie Year"] >= i and j["Movie Year"] <= i+9:
				movie_store_in_dict[i].append(j)
		movie_list_by_decade.append(movie_store_in_dict)
	
	# return (movie_list_by_decade)
(group_by_decade(movies))
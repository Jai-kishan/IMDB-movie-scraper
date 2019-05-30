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

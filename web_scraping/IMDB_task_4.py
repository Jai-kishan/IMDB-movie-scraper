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

#Task 4

movie_url = "https://www.imdb.com/title/tt0066763/"

def scrape_movie_details(movie_url):

	store={
	"Movie Title": "",
	"Director": [],
	"Country": "",
	"Language": [],
	"Poster_image_url": "",
	"Bio": "",
	"RunTime":"",
	"Genres":[]
	}


	movie_url=urlopen(movie_url)
	soup=BeautifulSoup(movie_url,"lxml")

	#for movie title (movie name)
	title=""
	movie_title=soup.find("title").get_text()
	for i in movie_title:
		if "(" in i:
			break
		else:
			title+=i
	store["Movie Title"]=title

	#poster image url
	poster=soup.find("div", class_="poster").a.img["src"]
	store["Poster_image_url"]=poster

	#Movie bio
	bio=soup.find("div", class_="summary_text").get_text().strip()
	store["Bio"]=bio

	#Movie Director Name
	mai_director=soup.find(class_="credit_summary_item")
	director=mai_director.find_all("a")
	for i in director:
		store["Director"].append(i.get_text())

	#Movie Genres
	all_genre=soup.find("div", id="titleStoryLine")
	find_div=all_genre.find_all("div", class_="see-more inline canwrap")
	for i in find_div:
		data=i.find("h4", class_="inline").get_text()
		if data == "Genres:":
			Genres=i.find_all("a")
			for i in Genres:
				store["Genres"].append(i.get_text())

	#Which country made by this movie also which languages in this movie
	find_country=soup.find("div", id="titleDetails")
	find_all_class=find_country.find_all("div",class_="txt-block")
	count=0
	for i in find_all_class:
		h4_tag=i.find("h4",class_="inline")
		if count==2:
			break
		if h4_tag.get_text() == "Country:":
			country=i.find("a").get_text()
			store["Country"]=country
			count=count+1
		#How many languages in this Movies
		if h4_tag.get_text()=="Language:":
			language=i.find_all("a")
			for i in language:
				store["Language"].append(i.get_text())
			count+=1

	sub_div=soup.find("div",class_="subtext")
	movie_runtime=sub_div.find("time").get_text().strip().split()
	if len(movie_runtime)==2:
		for i in movie_runtime:
			if "h" in i:
				time=int(i.strip("h"))
			if "min" in i:
				minutes=int(i.strip("min"))
		runtime=(str(time*60+minutes)+"min")
	if len(movie_runtime)==1:
		time=movie_runtime[0][:-1]
		runtime=str(int(time)*60)+"min"
	
	store["RunTime"]=runtime
	return store

scrape_single_movie=(scrape_movie_details(movie_url))
# pprint (scrape_single_movie)
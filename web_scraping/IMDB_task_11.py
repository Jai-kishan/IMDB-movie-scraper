from urllib.request import urlopen # Importing requests to get request data from a Web URL
from bs4 import BeautifulSoup # Importing BeautifulSoup from BS4, BeautifulSoup is a scraping tool
from pprint import pprint # Importing pprint for pretty print
import os.path
import json ## Importing JSON module to load and dump from json file and dump dictionary in json respectively
#randint is a function that is part of the random module.
import random, time #Importing time library to 'sleep' our program between two requests

#task_1
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

#Task 4 and Task 8 and Task 9.
# This movie returns major details of a movies from the file if it exists,
# otherwise it scrapes and write the data into a file and then returns the data
def scrape_movie_details(movie_url):
	
	import time
	sleep=random.randint(1,3) #Generate a random number between 1 and 3, both inclusive
	time.sleep(sleep) #Sleeping the program for the randomly generated seconds

	movies_id=movie_url[27:-1]
	movies_path=(f"Movies_Details/{movies_id}.json")
	if os.path.exists(movies_path):  #Checks whether JSON file already exists or not
		with open(movies_path,"r") as file:
			read_file = file.read()
			file_store=json.loads(read_file)
		return (file_store)

	store={
	"Movie Title": "",
	"Director": [],
	"Country": "",
	"Language": [],
	"Poster_image_url": "",
	"Bio": "",
	"RunTime":"",
	"Genres": []
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

	with open(movies_path,"w") as file:
		json.dump(store,file,indent=4)
	return store

#task 5 

def get_movie_list_details(movies_list):

	url_lst=[]
	top_movies=[]
	for i in movies_list[:10]:
		url_lst.append(i["URL"])
	
	for url in url_lst:
		top_movies.append(scrape_movie_details(url))
	
	return top_movies

# movies_list=(get_movie_list_details(movies))
# pprint(movies_list)

movies_list=(get_movie_list_details(movies))

# Task_11
#This function returns a dictionary that provides the number of movies of each Genre
def analyse_movies_genre(movies_list):
	genres={}
	for i in movies_list:  #Iterating loop over all movies
		for gen in i["Genres"]:  #Iterating lop over 'genre' key of each movie
			genres[gen]=0 #Creating a key of the genre if it doesn't exist in genreDict dictionary

	for i in movies_list:   #Iterating loop over all movies
		for gen in genres:  #Iterating loop over genreDict dictionary
			if gen in i["Genres"]:  #Iterating loop of 'genre' of each movie
				genres[gen]+=1  #Incrementing the value of the key
	return(genres)

print(analyse_movies_genre(movies_list))


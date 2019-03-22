from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint
import os.path
import json
import random, time

#task_1
def scrape_top_list():
	if os.path.exists("Top_250_movies.json"):
		with open("Top_250_movies.json") as file:
			read_file=file.read()
			file_store=json.loads(read_file)
		return file_store

	# rand=random.randint(1,3)
	# time.sleep(rand)

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


#Task 2
def group_by_year(movies):
	lst_of_year=[]
	yearly_movies={}
	for i in movies:
		if i["Movie Year"] not in lst_of_year:
			lst_of_year.append(i["Movie Year"])

	#this mehthos use for sort the list element reverse
	lst_of_year.sort(reverse=True)
	print(lst_of_year)
	for j in lst_of_year:
		same_year=[]
		for k in movies:
			if j==k["Movie Year"]:
				same_year.append(k)
		yearly_movies[j]=same_year
	return yearly_movies
# pprint(group_by_year(movies))


#Task 3
def group_by_decade(movies):
	start_year=1950
	lst_of_year=[]
	decade_year=[]
	movie_list_by_decade = []

	for i in movies:
		lst_of_year.append(i["Movie Year"])
		lst_of_year.sort()

	for i in range(start_year,lst_of_year[-1],10):
		decade_year.append(i)

	decade_year.sort(reverse=True)

	for i in decade_year:
		movie_store_in_dict={}
		movie_store_in_dict[i] = []
		for j in movies:
			if j["Movie Year"] >= i and j["Movie Year"] <= i+9:
				movie_store_in_dict[i].append(j)
		movie_list_by_decade.append(movie_store_in_dict)
	
	return (movie_list_by_decade)
# pprint(group_by_decade(movies))


#Task_12

def scrape_movie_cast(movie_caste_url):

	movie_cast=[]

	movie_caste_url=urlopen(movie_caste_url)
	soup=BeautifulSoup(movie_caste_url,"lxml")

	table=soup.find("table", class_="cast_list")
	table_row=table.find_all("td", class_="")

	#actore name
	for i in table_row:
		store={}
		a=(i.get_text().strip())
		b=i.find("a")["href"][6:15]
		store={"Name":a,"IMDB_ids":b}
		movie_cast.append(store)

	return movie_cast

# pprint(scrape_movie_cast(movie_caste_url))



#Task 4
def scrape_movie_details(movie_url):
	# task_13
	cast= scrape_movie_cast(movie_url)

	movies_id=movie_url[27:-1]
	movies_path=(f"Movies_Details/{movies_id}.json")
	if os.path.exists(movies_path):
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
	"Genres":[],
	"Cast":cast
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

	file= open(movies_path,"w+")
	raw=json.dumps(store,indent=4, sort_keys=True)
	file.write(raw)
	file.close()
	return store

#task 5 

def get_movie_list_details(movies_list):

	url_lst=[]
	top_movies=[]
	for i in movies_list[:2]:
		url_lst.append(i["URL"])
	
	for url in url_lst:
		top_movies.append(scrape_movie_details(url))
	
	return top_movies

movies_list=(get_movie_list_details(movies))
# pprint(movies_list)

#task 6
def analyse_movies_language(movies_list):
	lang=[]
	unique_lang=[]
	store={}

	for i in movies_list:
		for j in i["Language"]:
			lang.append(j)	

	for i in lang:
		if i not in unique_lang:
			unique_lang.append(i)

	for i in unique_lang:
		count=0
		for j in lang:
			if i==j:
				count+=1
		store[i]=count

	return store
	

# (analyse_movies_language(movies_list))

#Task 7
def analyse_movies_directors(movies_list):
	director=[]
	unique_director=[]
	store={}	

	for i in movies_list:
		for j in i["Director"]:
			director.append(j)

	for i in director:
		if i not in unique_director:
			unique_director.append(i)

	for i in unique_director:
		count=0
		for j in director:
			if i == j :
				count+=1
		store[i]=count

	return store

# (analyse_movies_directors(movies_list))

def analyse_language_and_directors(movies_list):
	list_of_directors={}
	for i in movies_list:
		for director in i["Director"]:
			list_of_directors[director]={}


	for i in range(len(movies_list)):
		for director in list_of_directors:
			if director in movies_list[i]["Director"]:
				for lang in movies_list[i]["Language"]:
					list_of_directors[director][lang]=0

	for i in range(len(movies_list)):
		for director in list_of_directors:
			if director in movies_list[i]["Director"]:
				for lang in movies_list[i]["Language"]:
					list_of_directors[director][lang]+=1

	return list_of_directors

# (analyse_language_and_directors(movies_list))


# Task_11
def analyse_movies_genre(movies_list):
	genres={}
	for i in movies_list:
		for gen in i["Genres"]:
			genres[gen]=0

	for i in movies_list:
		for gen in genres:
			if gen in i["Genres"]:
				genres[gen]+=1
	return(genres)

# print(analyse_movies_genre(movies_list))

#task14

def analyse_co_actors(movies_list):
	# store={}
	for i in movies_list:
		for j in i["Cast"]:
			a=(j["IMDB_ids"])
			b=j["Name"]
			store={a:{"Name":b,"frequent_co_actors":[{"IMDB_ids":"","Name":"","Num_movies":""}]}}


			store[a]["frequent_co_actors"][0]["IMDB_ids"]=1


			pprint(store)
analyse_co_actors(movies_list)
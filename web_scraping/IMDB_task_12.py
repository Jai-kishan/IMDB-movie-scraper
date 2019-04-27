from urllib.request import urlopen
from bs4 import BeautifulSoup

#Task 12
#This function returns a list of full cast of a movie
new_movie_url="https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast"
def scrape_movie_cast(movie_caste_url):

	movie_cast=[]

	movie_caste_url=urlopen(movie_caste_url)
	soup=BeautifulSoup(movie_caste_url,"lxml")

	table=soup.find("table", class_="cast_list") #Finding 'table' tag
	table_row=table.find_all("td", class_="") #Finding all 'td' tags

	#actore name
	for i in table_row:
		store={}
		a=(i.get_text().strip()) 
		b=i.find("a")["href"][6:15]  #Getting IMDB ID of the cast
		#Creating key as IMDB_ID and assigning its value
		store={"Name":a,"IMDB_ids":b}  #Creating key as Name and assigning its value
		movie_cast.append(store) #Appending the dictionary in a main list

	return movie_cast

print(scrape_movie_cast(new_movie_url))
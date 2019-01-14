from bs4 import BeautifulSoup	
from urllib.request import urlopen
from pprint import pprint

url=urlopen("https://www.imdb.com/india/top-rated-indian-movies/")
# response=requests.get(url)

soup=BeautifulSoup(url,"lxml")
# print(soup.prettify())



data_container=soup.find('div', class_='lister')
table_body=data_container.find('tbody', class_='lister-list')
table_row=table_body.find_all('tr')

i=1
for tr in table_row:
	name=tr.find('td',class_='titleColumn').a.get_text()

	movie_detail=tr.find('td',class_='titleColumn').a.get('href')
	movie_url="https://www.imdb.com"
	for k in range(len(movie_detail)):
		if movie_detail[k]=="?":
			break
		else:
			movie_url+=movie_detail[k]

	year=tr.find('td',class_='titleColumn').span.get_text()
	year=year.replace("(","").replace(")","")
	# print(year)

	rating=tr.find('td',class_='imdbRating').strong.get_text()
	rating_new=float(rating)

	store={
		'Movie Name':name,
		"Year":int(year),
		"Position":i,
		"Rationg":rating_new,
		"url":movie_url
		}
	i+=1
	return(store)
# IMDB-movie-scraper
Using Beautiful-soup and Requests library  implemented scraper to scrape details of Top 250 Indian movies according to IMDB.com  and performed different analysis based on year, decade, genres, director, language and cast.

## Requirements
If you’re using a recent version of Debian or Ubuntu Linux, you can install Beautiful Soup with the system package manager:
```
$ apt-get install python-bs4 (for Python 2)
```
```
$ apt-get install python3-bs4 (for Python 3)
```
## Installing a parser
Beautiful Soup supports the HTML parser included in Python’s standard library, but it also supports a number of third-party Python parsers. One is the lxml parser. Depending on your setup, you might install lxml with one of these commands:
```
$ apt-get install python-lxml
```
```
$ easy_install lxml
```
```
$ pip install lxml
```
Another alternative is the pure-Python html5lib parser, which parses HTML the way a web browser does. Depending on your setup, you might install html5lib with one of these commands:
```
$ apt-get install python-html5lib
```
```
$ easy_install html5lib
```
```
$ pip install html5lib
```
if you want to read more about Beautiful Soup so visite on this link https://www.crummy.com/software/BeautifulSoup/bs4/doc/:- https://www.crummy.com/software/BeautifulSoup/bs4/doc/

## Installing Request packages

pip install requests # this will install latest request package
```
pip install requests==2.6.0 # this will install requests 2.6.0 package not the latest package
```
```
pip install requests==2.6.0 # this will install requests 2.6.0 package not the latest package
```
```
pip install requests>=2.6.0 # specify a minimum version if it's not available pip will install the latest version
```
```
pip install requests>=2.6.0 # specify a minimum version if it's not available pip will install the latest version
```

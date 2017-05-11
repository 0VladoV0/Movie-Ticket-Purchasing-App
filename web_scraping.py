from bs4 import BeautifulSoup
import urllib.request

#Find Date

def date_list():
    week_list = []
    page = urllib.request.urlopen('http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage')
    soup = BeautifulSoup(page.read(), 'html.parser')
    soup.prettify()
    url_list = [x.get('href') for x in soup.findAll('a', {'class' : 'date-area'})][:7]
    for i in range(7):
        week_list.append([x.text.strip() for x in soup.findAll('div', {'class': 'date-week-day'})][i] + " " + [x.text.strip() for x in soup.findAll('div', {'class': 'date-day'})][i] + " " + [x.text.strip() for x in soup.findAll('div', {'class': 'date-month'})][i])
    return week_list, url_list

#Find movie titles

def movie_title(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), 'html.parser')
    soup.prettify()
    movie_list = [x.text.strip() for x in soup.findAll('a', {'class': 'dark showtimes-movie-title'})]
    return movie_list

#Find times

def find_time(index, url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), 'html.parser')
    soup.prettify()
    time_list = [[z.text.strip() for z in y.findAll('time', {'class': 'timeInfo'})] for y in [x for x in soup.findAll('div', {'class': 'showtimes-movie-container'})]][index]
    return time_list


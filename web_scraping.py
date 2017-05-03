from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage'

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page.read(), 'html.parser')

#Find Date
def day_of_week():
    day_of_week = [x.text.strip() for x in soup.findAll('div', {'class' : 'date-week-day'})][:7]
def day():
    day = [x.text.strip() for x in soup.findAll('div', {'class' : 'date-day'})][:7]
def month():
    month = [x.text.strip() for x in soup.findAll('div', {'class' : 'date-month'})][:7]



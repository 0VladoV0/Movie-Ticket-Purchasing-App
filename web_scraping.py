from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage'

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page.read(), 'html.parser')

def date():
    day_of_week = [x.text.strip() for x in soup.findAll('div', {'class' : 'date-week-day'})][:7]
    day = [x.text.strip() for x in soup.findAll('div', {'class' : 'date-day'})][:7]
    month = [x.text.strip() for x in soup.findAll('div', {'class' : 'date-month'})][:7]
    print(day_of_week)
    print(day)
    print(month)
date()


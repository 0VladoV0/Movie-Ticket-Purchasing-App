from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage'

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page.read(), 'html.parser')

week_list=[]




#Find Date
def date_list():
    for i in range(7):
         week_list.append([x.text.strip() for x in soup.findAll('div', {'class' : 'date-week-day'})][i] + " " + [x.text.strip() for x in soup.findAll('div', {'class' : 'date-day'})][i] + " " + [x.text.strip() for x in soup.findAll('div', {'class' : 'date-month'})][i])
    return week_list






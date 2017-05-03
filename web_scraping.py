from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage'

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page.read(), 'html.parser')

days = soup.find
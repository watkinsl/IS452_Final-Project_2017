# Lisa Watkins
# netID: watkinsl
# IS 452AO
# 2 Credit Hour
# Final Project
# 12/21/17

# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify the url
quote_page = 'http://is452.lisamwatkins.com/bruno-mars.html'

# query the website and return the html to the variable ‘page’
page = urlopen(quote_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

artist_name = soup.find('h2', attrs={'id': 'name'})
name = artist_name.text.strip() # strip() is used to remove starting and trailing
print("Artist name:", name)

artist_rating = soup.find('td', attrs={'id': 'rating_num'})
rating = artist_rating.text.strip() # strip() is used to remove starting and trailing
print(name, "is rated", rating, "out of 5.")

artist_review = soup.find('td', attrs={'id': 'review_num'})
reviews = artist_review.text.strip() # strip() is used to remove starting and trailing
print(name, "has", reviews, "reviews.")

file_in = open('2017-ama-nominees.txt', 'r')

print(file_in.readlines())

file_in.close()

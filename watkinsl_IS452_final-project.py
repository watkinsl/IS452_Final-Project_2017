# Lisa Watkins
# netID: watkinsl
# IS 452AO
# 2 Credit Hour
# Final Project
# 12/21/17

# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

filein = open('artist_Bruno-Mars.html', 'r')
insta_in = open('IG_Bruno-Mars.htm', 'r')
twitter_in = open('Twitter_Bruno-Mars.htm', 'r')

bruno_page = filein.read()
insta_bruno = insta_in.read()
twitter_bruno = twitter_in.read()

filein.close()
insta_in.close()
twitter_in.close()

# specify the url
#quote_page = 'http://is452.lisamwatkins.com/bruno-mars.html'

# query the website and return the html to the variable ‘page’
#page = urlopen(quote_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(bruno_page, 'html.parser')
IG_soup = BeautifulSoup(insta_bruno, 'html.parser')
twitter_soup = BeautifulSoup(twitter_bruno, 'html.parser')

#print(soup)
artist_name = soup.find('div', attrs={'class': 'artistDetails'}) # line 4230
name = artist_name.find('h1')
only_name = name.text.strip() # strip() is used to remove starting and trailing
print(only_name)

# finding ticketmaster rating for artist
artist_rating = soup.find('span', attrs={'itemprop': 'ratingValue'}) # line 4333
rating_text = artist_rating.text.strip()
print(rating_text)

# finding number of reviews on artist via ticketmaster
artist_reviews = soup.find('span', attrs={'class': 'BVRRCount BVRRNonZeroCount'}) # line 4333
reviews_text = artist_reviews.text.strip()
print("Bruno Mars has", reviews_text, "overall on Ticketmaster.")

#rating breakdown on Ticketmaster
artist_reviews_breakdown = soup.find('div', attrs={'class': 'BVRRHistogramContent'}) # line 4333
reviews_breakdown_text = artist_reviews_breakdown.text.strip()
print(reviews_breakdown_text)

# ------------------------

# instagram followers
IG_followers = IG_soup.find('span', attrs={'title': '15,721,693'})
IG_followers_text = IG_followers.text.strip()
print("Bruno's Insta has", IG_followers_text, "followers.")

#instagram posts
IG_posts = IG_soup.find('span', attrs={'class': '_fd86t'})
IG_posts_text = IG_posts.text.strip()
print("Bruno's Insta has", IG_posts_text, "posts.")

# ------------------------
# twitter followers
Twitter_followers = twitter_soup.find('li', attrs={'class': 'ProfileNav-item ProfileNav-item--followers'})
Twitter_followers_text = Twitter_followers.find('span', attrs={'class': 'ProfileNav-value'})
Twitter_followers_num = Twitter_followers_text.text.strip()
print("Bruno's Twitter has", Twitter_followers_num, "followers.")

# number of tweets
tweets = twitter_soup.find('li', attrs={'class': 'ProfileNav-item ProfileNav-item--tweets is-active'})
tweets_text = tweets.find('span', attrs={'class': 'ProfileNav-value'})
tweets_num = tweets_text.text.strip()
print("Bruno's Twitter has", tweets_num, "tweets.")

# ------------------------
#old code
# artist_rating = soup.find('td', attrs={'id': 'rating_num'})
# rating = artist_rating.text.strip() # strip() is used to remove starting and trailing
# print(name, "is rated", rating, "out of 5.")

# artist_review = soup.find('td', attrs={'id': 'review_num'})
# reviews = artist_review.text.strip() # strip() is used to remove starting and trailing
# print(name, "has", reviews, "reviews.")

# file_in = open('2017-ama-nominees.txt', 'r')
#
# print(file_in.readlines())
#
# file_in.close()

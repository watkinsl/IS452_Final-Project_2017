# Lisa Watkins
# netID: watkinsl
# IS 452AO
# 2 Credit Hour
# Final Project
# 12/21/17

# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

# ------------------------
# CREATING PROGRAM
# ------------------------

filenames = ['artist_Bruno-Mars.html', 'IG_Bruno-Mars.htm', 'Twitter_Bruno-Mars.htm', 'artist_Drake.html',
            'IG_Drake.htm', 'Twitter_Drake.htm']

artist_rows = []

for file_path in filenames:
    with open(file_path, 'r') as f_input:
        read_in = f_input.read()
        soup = BeautifulSoup(read_in, 'html.parser')
        if file_path.startswith('artist'):
            #artist's name
            artist_name = soup.find('div', attrs={'class': 'artistDetails'}) # line 4230
            name = artist_name.find('h1')
            only_name = name.text.strip() # strip() is used to remove starting and trailing

            # rating on Ticketmaster
            artist_rating = soup.find('span', attrs={'itemprop': 'ratingValue'}) # line 4333
            rating_text = artist_rating.text.strip()

            # no. of Ticketmaster reviews
            artist_reviews = soup.find('span', attrs={'class': 'BVRRCount BVRRNonZeroCount'}) # line 4333
            artist_reviews_num = artist_reviews.find('span', attrs={'class': 'BVRRNumber'})
            reviews_text = artist_reviews_num.text.strip()

            artist_rows.extend([only_name, rating_text, reviews_text])

        elif file_path.startswith('IG'):
            # no. of Instagram posts
            IG_posts = soup.find('span', attrs={'class': '_fd86t'})
            #IG_followers_num = IG_followers.find('title')
            IG_post_num = IG_posts.text.strip()
            artist_rows.append(IG_post_num)

        elif file_path.startswith('Twitter'):
            # no. of tweets
            tweets = soup.find('li', attrs={'class': 'ProfileNav-item ProfileNav-item--tweets is-active'})
            tweets_text = tweets.find('span', attrs={'class': 'ProfileNav-value'})
            tweets_num = tweets_text.text.strip()

            # no. of Twitter followers
            Twitter_followers = soup.find('li', attrs={'class': 'ProfileNav-item ProfileNav-item--followers'})
            Twitter_followers_text = Twitter_followers.find('span', attrs={'class': 'ProfileNav-value'})
            Twitter_followers_num = Twitter_followers_text.text.strip()

            artist_rows.extend([tweets_num, Twitter_followers_num])

print(artist_rows)

# ------------------------
# WORKING CODE
# ------------------------

# filein = open('artist_Bruno-Mars.html', 'r')
# insta_in = open('IG_Bruno-Mars.htm', 'r')
# twitter_in = open('Twitter_Bruno-Mars.htm', 'r')
#
# bruno_page = filein.read()
# insta_bruno = insta_in.read()
# twitter_bruno = twitter_in.read()
#
# filein.close()
# insta_in.close()
# twitter_in.close()
#
# artists_list = []
#
# # parse the html using beautiful soap and store in variable `soup`
# soup = BeautifulSoup(bruno_page, 'html.parser')
# IG_soup = BeautifulSoup(insta_bruno, 'html.parser')
# twitter_soup = BeautifulSoup(twitter_bruno, 'html.parser')
#
# # EXTRACTING ARTIST'S NAME
# artist_name = soup.find('div', attrs={'class': 'artistDetails'}) # line 4230
# name = artist_name.find('h1')
# only_name = name.text.strip() # strip() is used to remove starting and trailing
# artists_list.append(only_name.strip("\xa0Tickets"))
#
# # FINDING TICKETMASTER RATING FOR ARTIST
# artist_rating = soup.find('span', attrs={'itemprop': 'ratingValue'}) # line 4333
# rating_text = artist_rating.text.strip()
# artists_list.append(rating_text)
#
# # FINDING NUMBER OF REVIEWS ON ARTIST VIA TICKETMASTER
# artist_reviews = soup.find('span', attrs={'class': 'BVRRCount BVRRNonZeroCount'}) # line 4333
# artist_reviews_num = artist_reviews.find('span', attrs={'class': 'BVRRNumber'})
# reviews_text = artist_reviews_num.text.strip()
# #print("Bruno Mars has", reviews_text, "overall on Ticketmaster.")
# artists_list.append(reviews_text)
#
# # RATING BREAKDOWN ON TICKETMASTER
# artist_reviews_breakdown = soup.find('div', attrs={'class': 'BVRRHistogramContent'}) # line 4333
# reviews_breakdown_text = artist_reviews_breakdown.text.strip()
# artists_list.append(reviews_breakdown_text)
#
# # ------------------------
#
# # NO. OF INSTAGRAM FOLLOWERS
# IG_followers = IG_soup.find('span', attrs={'title': '15,721,693'})
# IG_followers_text = IG_followers.text.strip()
# #print("Bruno's Insta has", IG_followers_text, "followers.")
# artists_list.append(IG_followers_text)
#
# # # NO. OF INSTAGRAM POSTS
# IG_posts = IG_soup.find('span', attrs={'class': '_fd86t'})
# IG_posts_text = IG_posts.text.strip()
# #print("Bruno's Insta has", IG_posts_text, "posts.")
# artists_list.append(IG_posts_text)
#
# # ------------------------
# # NUMBER OF TWITTER FOLLOWERS
# Twitter_followers = twitter_soup.find('li', attrs={'class': 'ProfileNav-item ProfileNav-item--followers'})
# Twitter_followers_text = Twitter_followers.find('span', attrs={'class': 'ProfileNav-value'})
# Twitter_followers_num = Twitter_followers_text.text.strip()
# #print("Bruno's Twitter has", Twitter_followers_num, "followers.")
# artists_list.append(Twitter_followers_num)
#
# # NUMBER OF TWEETS
# tweets = twitter_soup.find('li', attrs={'class': 'ProfileNav-item ProfileNav-item--tweets is-active'})
# tweets_text = tweets.find('span', attrs={'class': 'ProfileNav-value'})
# tweets_num = tweets_text.text.strip()
# #print("Bruno's Twitter has", tweets_num, "tweets.")
# artists_list.append(tweets_num)
#
# # need to create a tuple for the row contents
# print(artists_list)


# ------------------------
# EXPORTING A CSV FILE [x]
# ------------------------

# Now, use the CSV module to write out this data.
# Let the header values be:  id, status, occupation
# Let the file name be hamlet-character-data.csv
# You must use the CSV module to receive full credit
# This should yield a csv file with 3 columns and 34 rows.


# Here's a template. (Source:  http://chimera.labs.oreilly.com/books/1230000000393/ch06.html#to_write_csv_da)
# import csv
#
# headers = ['Artist Name', 'Ticketmaster (TM) Rating', '# of TM Reviews', 'TM Review Breakdown', '# of Instagram (IG) Followers',
#            '# of IG Posts', '# of Twitter Followers', '# of Tweets']
#
# outfile = open('bruno-mars.csv', 'w')
# csv_out = csv.writer(outfile)
# csv_out.writerow(headers) # add your
# csv_out.writerow([only_name, rating_text, reviews_text, reviews_breakdown_text, IG_followers_text, IG_posts_text,
#                    Twitter_followers_num, tweets_num])
# outfile.close()

# ------------------------
# OLD CODE
# ------------------------

# specify the url
# quote_page = 'http://is452.lisamwatkins.com/bruno-mars.html'

# query the website and return the html to the variable ‘page’
# page = urlopen(quote_page)

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

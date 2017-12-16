# Lisa Watkins
# netID: watkinsl
# IS 452AO
# 2 Credit Hour
# Final Project
# 12/21/17

# ------------------------
# PROGRAM TO-DO LIST:
# [x] Be able to extract data from webpages
# [x] Be able to write to a CSV file in correct rows & columns
# [x] Combine tasks into a loop that will go over multiple files
# [x] Save out results to a nested list that will be used for the CSV file
# [don't need] Use pandas to create a visualization based on the data saved to the CSV file
# [don't need] Export and post on a website (?)
# - OR - [don't need] Be able to create different visualizations to figure out different aspects of the data
# [x] create function split on period to evaluate the millions into an actual number (i.e. 38.9M) * find package
# [x] accumulator to create list of lists (xpathb homework to make lists of lists)
# ------------------------

# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import html
import csv

# ------------------------
# ACTUAL PROGRAM
# ------------------------
# define function for convert strings of numbers into integers


def convert_num(num):
    if num.endswith('M'):
        mil_num = num.split('M')
        mil_num_float = float(mil_num[0])
        m_to_num = int(mil_num_float * 1000000)
        return m_to_num

    elif num.endswith('K'):
        k_num = num.split('K')
        k_num_float = float(k_num[0])
        k_to_num = int(k_num_float * 1000)
        return k_to_num

    else:
        int_num = int(num.replace(',', ''))
        return int_num


filenames = [['artist_Bruno-Mars.html', 'IG_Bruno-Mars.htm', 'Twitter_Bruno-Mars.htm'], ['artist_Drake.html',
            'IG_Drake.htm', 'Twitter_Drake.htm'], ['artist_Kendrick-Lamar.html', 'IG_Kendrick-Lamar.htm',
            'Twitter_Kendrick-Lamar.htm'], ['artist_Ed-Sheeran.html', 'IG_Ed-Sheeran.htm', 'Twitter_Ed-Sheeran.htm'],
             ['artist_The-Chainsmokers.html', 'IG_The-Chainsmokers.htm', 'Twitter_The-Chainsmokers.htm']]

artist_rows = []

for list_of_files in filenames:
    artist_data = []
    for file_path in list_of_files:
        with open(file_path, 'r') as f_input:
            read_in = f_input.read()
            soup = BeautifulSoup(read_in, 'html.parser')
            if file_path.startswith('artist'):
                # artist's name
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

                artist_data.extend([only_name.split('\xa0Tickets')[0], float(rating_text), int(reviews_text.replace(',', ''))])

            elif file_path.startswith('IG'):
                tree = html.fromstring(read_in)

                # no. of Instagram posts
                IG_posts = soup.find('span', attrs={'class': '_fd86t'})
                IG_post_num = IG_posts.text.strip()

                # no. of Instagram followers (needs work)
                IG_followers = tree.xpath('//span[@class="_fd86t"]/@title')
                # refer to assignment to get rid of xpath list
                artist_data.extend([int(IG_post_num.replace(',', '')), int(IG_followers[0].replace(',', ''))])

            elif file_path.startswith('Twitter'):
                # no. of tweets
                tweets = soup.find('li', attrs={'class': 'ProfileNav-item ProfileNav-item--tweets is-active'})
                tweets_text = tweets.find('span', attrs={'class': 'ProfileNav-value'})
                tweets_num = tweets_text.text.strip()
                tweets_convert = convert_num(tweets_num)

                # no. of Twitter followers
                Twitter_followers = soup.find('li', attrs={'class': 'ProfileNav-item ProfileNav-item--followers'})
                Twitter_followers_text = Twitter_followers.find('span', attrs={'class': 'ProfileNav-value'})
                Twitter_followers_num = Twitter_followers_text.text.strip()
                Twit_num = convert_num(Twitter_followers_num)

                # artist_data.extend([int(tweets_num.replace(',', '')), Twit_num])
                artist_data.extend([tweets_convert, Twit_num])

    artist_rows.append(artist_data)

print(artist_rows)

# ------------------------
# EXPORTING A CSV FILE [x]
# ------------------------

headers = ['Artist Name', 'Ticketmaster (TM) Rating', '# of TM Reviews', '# of Instagram (IG) Posts',
           '# of IG Followers', '# of Tweets', '# of Twitter Followers']

outfile = open('artists.csv', 'w')
csv_out = csv.writer(outfile)
csv_out.writerow(headers)
csv_out.writerows(artist_rows)
outfile.close()


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

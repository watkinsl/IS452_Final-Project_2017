# Lisa Watkins
# netID: watkinsl
# IS 452AO
# 2 Credit Hour
# Final Project
# 12/21/17

# ------------------------
# PROGRAM TO-DO LIST:
# ------------------------
# [x] Be able to extract data from webpages
# [x] Combine tasks into a loop that will go over multiple files
# [x] create function split on period to evaluate the millions into an actual number (i.e. 38.9M)
# [x] accumulator to create list of lists (xpathb homework to make lists of lists)
# [x] Save out results to a nested list that will be used for the CSV file
# [x] Be able to write to a CSV file in correct rows & columns

# ------------------------
# ACTUAL PROGRAM [x]
# ------------------------
# import libraries
# - using BeautifulSoup library for web scraping to parse HTML information & pinpoint attributes easily
# - used XPath in one instance to pinpoint Instagram follower info. This info was wrapped in a variable attribute
#   that was hard to pinpoint with BeautifulSoup
# - the results will be output to a csv file
from bs4 import BeautifulSoup
from lxml import html
import csv

# defining function for converting strings of numbers into integers
# - when extracting information on each artist and the number of Twitter followers they have, the numbers were
#   written as, for example, 34M or 3.5M.
# - also, there is one instance where one of the artists tweeted tens of thousands of times (i.e. 29.3K)
# - this function will take in those strings of numbers, split them by the letter included (M or K),
#   run an appropriate expression over the string leftover and change it into an integer
# - if the string doesn't include such letters, the function will just return the string of the number as an integer
#   cleaned up of any commas it might've included


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

    # other strings passed through the function without an M or K included
    else:
        # cleaning up the string by removing commas and changing it into an integer
        int_num = int(num.replace(',', ''))
        return int_num

# a list containing lists that include web files attributed to each of the artists that were nominated for
#   the artist of the year award at the american music awards, which is stored in the "filenames" variable
# artists include: Bruno Mars, Drake, Kendrick Lamar, Ed Sheeran, and The Chainsmokers
filenames = [['artist_Bruno-Mars.html', 'IG_Bruno-Mars.htm', 'Twitter_Bruno-Mars.htm'], ['artist_Drake.html',
            'IG_Drake.htm', 'Twitter_Drake.htm'], ['artist_Kendrick-Lamar.html', 'IG_Kendrick-Lamar.htm',
            'Twitter_Kendrick-Lamar.htm'], ['artist_Ed-Sheeran.html', 'IG_Ed-Sheeran.htm', 'Twitter_Ed-Sheeran.htm'],
             ['artist_The-Chainsmokers.html', 'IG_The-Chainsmokers.htm', 'Twitter_The-Chainsmokers.htm']]

# an empty list stored in the variable called "artist_rows," which will be written to the csv file at the end
#   of the program
artist_rows = []

# a for loop that will progress through the list stored in the "filenames" variable
for list_of_files in filenames:
    # an empty list stored in a variable called, "artist_data" that will hold all of the artist's info as it
    #   is extracted
    artist_data = []
    # a nested list that will progress through the file paths included in the list within the list
    #   stored in the "filenames" variable
    for file_path in list_of_files:
        # the file_path in the current position with in the loop will be open for reading and
        #   stored under the variable "f_input"
        with open(file_path, 'r') as f_input:
            # the file stored in "f_input" will be read into the program entirely and stored in the "read_in" variable
            read_in = f_input.read()
            # using the capabilities within the BeautifulSoup library, the html.parser will be applied to the
            #   "read_in" variable and stored in the variable called, "soup."
            soup = BeautifulSoup(read_in, 'html.parser')

            # an if-elif loop that will consider each file_path as it loops through the program to see if the file path
            #   begins with either of the following prefixes: artist, IG or Twitter
            if file_path.startswith('artist'):
                # extracting artist's name from web files saved from Ticketmaster
                artist_name = soup.find('div', attrs={'class': 'artistDetails'}) # line 4230
                name = artist_name.find('h1')
                only_name = name.text.strip()  # strip() is used to remove starting and trailing

                # extracting average rating from web files saved from Ticketmaster
                artist_rating = soup.find('span', attrs={'itemprop': 'ratingValue'}) # line 4333
                rating_text = artist_rating.text.strip()  # strip() is used to remove starting and trailing

                # extracting number of reviews from web files saved from Ticketmaster
                artist_reviews = soup.find('span', attrs={'class': 'BVRRCount BVRRNonZeroCount'}) # line 4333
                artist_reviews_num = artist_reviews.find('span', attrs={'class': 'BVRRNumber'})
                reviews_text = artist_reviews_num.text.strip()  # strip() is used to remove starting and trailing

                # adding each of the results from the above operations to the "artist_data" list
                #   includes some conversion of output types including cleaning up the information extracted for the
                #   artist's name since it included other text; converting average review string to a float; and
                #   converting the number of reviews string into an integer and cleaning it up by removing the commas
                artist_data.extend([only_name.split('\xa0Tickets')[0], float(rating_text), int(reviews_text.replace(',', ''))])

            # else-if the file_path starts with IG, it will retrieve Instagram-specific information from web files
            #   saved from Instagram
            elif file_path.startswith('IG'):
                # XPath is needed for one specific portion of this program since the targeted information is
                #   wrapped in a variable attribute
                # this will consider the HTML aspects of the string read into the program and stored in the "read_in" variable
                # this information will stored in the variable called, "tree"
                tree = html.fromstring(read_in)

                # extracting number of Instagram posts from web files saved from Instagram
                IG_posts = soup.find('span', attrs={'class': '_fd86t'})
                IG_post_num = IG_posts.text.strip()  # strip() is used to remove starting and trailing

                # extracting number of Instagram followers from web files saved from Instagram using XPath
                IG_followers = tree.xpath('//span[@class="_fd86t"]/@title')

                # adding each of the results from the above operations to the "artist_data" list
                #   includes the cleaning of the output by converting the strings into an integer and
                #   cleaning it up by removing the commas
                artist_data.extend([int(IG_post_num.replace(',', '')), int(IG_followers[0].replace(',', ''))])

            # else-if the file_path starts with Twitter, it will retrieve Twitter-specific information from web files
            #   saved from Twitter
            elif file_path.startswith('Twitter'):
                # extracting number of tweets from web files saved from Twitter
                tweets = soup.find('li', attrs={'class': 'ProfileNav-item ProfileNav-item--tweets is-active'})
                tweets_text = tweets.find('span', attrs={'class': 'ProfileNav-value'})
                tweets_num = tweets_text.text.strip()  # strip() is used to remove starting and trailing
                # calling on the "convert_num" function and feeding in the information extracted and stored in the
                #   "tweets_num" variable
                # this will convert or return the string extracted from the Twitter web file into an integer and
                #   perform an expression that will provide an actual number in the instances that the number is
                #   represented by abbreviations containing letters (i.e. 39M for 39000000)
                tweets_num_convert = convert_num(tweets_num)

                # extracting number of Twitter followers from web files saved from Twitter
                Twitter_followers = soup.find('li', attrs={'class': 'ProfileNav-item ProfileNav-item--followers'})
                Twitter_followers_text = Twitter_followers.find('span', attrs={'class': 'ProfileNav-value'})
                Twitter_followers_num = Twitter_followers_text.text.strip()  # strip() is used to remove starting and trailing
                # calling on the convert_num function and feeding in the information extracted and stored in the
                #   "Twitter_followers_num" variable
                # this will convert or return the string extracted from the Twitter web file into an integer and
                #   perform an expression that will provide an actual number in the instances that the number is
                #   represented by abbreviations containing letters (i.e. 39M for 39000000)
                Twitter_followers_num_convert = convert_num(Twitter_followers_num)

                # adding each of the results from the above operations to the "artist_data" list
                artist_data.extend([tweets_num_convert, Twitter_followers_num_convert])

    # appending the list stored in the "artist_data" variable in to the list stored in the "artist_rows" variable
    artist_rows.append(artist_data)

# since the program will write the output to a CSV file, printing the list of lists stored in the "artist_rows" variable
# will allow you to see the output that can be expected in the CSV file.
print(artist_rows)

# ------------------------
# EXPORTING A CSV FILE [x]
# ------------------------

# establishing headers corresponding to the information extracted by the program that will be featured in the CSV file
#   that will be written at the end of the program
headers = ['Artist Name', 'Ticketmaster (TM) Rating', '# of TM Reviews', '# of Instagram (IG) Posts',
           '# of IG Followers', '# of Tweets', '# of Twitter Followers']

# opening a newly created file that I called "AMA-nominated_artists_info.csv" that will be written to.
outfile = open('AMA-nominated_artists_info.csv', 'w')
# determines that the output file will be written as a CSV
csv_out = csv.writer(outfile)
# writing a single row featuring the header names stored in the "headers" variable
csv_out.writerow(headers)
# writing multiple rows according to the nested list stored in the "artist_rows" variable
csv_out.writerows(artist_rows)
# closing the output file as the operation is completed
outfile.close()

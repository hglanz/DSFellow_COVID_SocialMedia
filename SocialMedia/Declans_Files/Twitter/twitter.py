# Imports
import snscrape.modules.twitter as sntwitter
import pandas as pd



# Query by Username
# The code below will scrape for 100 tweets by a username I choose, then it will make a CSV file with Pandas


# Setting variables to be used below
maxTweets = 100

# Creating list to append tweet data to
tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:decdec2323').get_items()):
	if i>maxTweets:
		break
	tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])


# Creating a dataframe from the tweets list above
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# Display first 5 entries from dataframe
#tweets_df1.head()

# Export dataframe into a CSV
#tweets_df1.to_csv('decdec2323.csv', sep=',', index=False)

##################################################################################################



##################################################################################################

maxTweets = 500

# Creating list to append tweet data to
tweets_list3 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid since:2020-01-01 until:2020-01-31').get_items()):
    if i>maxTweets:
        break
    tweets_list3.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

tweets_df3 = pd.DataFrame(tweets_list3, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# Export dataframe into a CSV
tweets_df3.to_csv('january_covid.csv', sep=',', index=False)
# Imports
import snscrape.modules.instagram as sninstagram
import pandas as pd

maxPosts = 100

# Creating list to append facebook data to
insta_posts_list = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid since:2020-02-01 until:2020-02-29 lang:en').get_items()):
    if i>maxPosts:
        break
    tweets_list3.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

tweets_df3 = pd.DataFrame(tweets_list3, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# Export dataframe into a CSV
tweets_df3.to_csv('february_covid.csv', sep=',', index=False)


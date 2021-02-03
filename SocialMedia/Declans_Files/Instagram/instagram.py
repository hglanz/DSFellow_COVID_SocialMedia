# Imports
import snscrape.modules.instagram as sninstagram
import pandas as pd

maxPosts = 10

# Creating list to append facebook data to
insta_posts_list = []

# Using InstagramCommonScraper to scrape data and append instagram posts to list
for i,post in enumerate(sninstagram.InstagramCommonScraper('covid since:2020-02-01 until:2020-02-29 lang:en').get_items()):
    if i>maxPosts:
        break
    insta_posts_list.append([post.date, post.id, post.content, post.user.username])

insta_df = pd.DataFrame(insta_posts_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# Export dataframe into a CSV
insta_df.to_csv('february_covid.csv', sep=',', index=False)


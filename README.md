# DSFellow_COVID_SocialMedia

#### Note to self: readme formatting for github:
https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax

### October 26th, 2020
Began uploading material

### October 28-29th, 2020
Trying out different visualizations using Matplotlib and pandas

### October 30th, 2020
Produce html output or pdf output from .py file


### January 17th, 2021
Scrape individual twitter accounts for recent tweets


### January 18th, 2021
Scrape for keywords, like hashtags, across a span of dates/times


### January 20th, 2021
Able to now scrape Twitter for keywords suchas #covid, #covid19, etc. 'snscrape' library also has the capability to scrape Facebook and Instagram, that's next


### January 27th, 2021
Produced a csv file of 100,000 tweets from February 25th-28th, 2020 on keyword 'covid'

### January 30th, 2021
[(1,000, 8seconds), (10,000, 86seconds), (100,000, 12minutes), (223,360, 30minutes)]
223,360 is the total english tweets with keyword 'covid' in February

### February 5th, 2021
Data Pipeline (any dataset can be read-in at the top, then you can run all)
https://colab.research.google.com/drive/1KGuQdoQ0ZtVGTuy0ASXpvhQFMAolFrDe?usp=sharing

### February 7th, 2021
Tried to obtain March 28th-30th, took over 2 hours and is too large to be uploaded to github (226MB)

### February 13th, 2021
Fixed the issue with Github... 
**git reset --hard HEAD~4**
by using this code in *git bash* to remove the last 4 commits to github

### February 21st, 2021
Began scraping for the month of March

### February 22nd, 2021
It appears that the scraping tool is not functioning at full capacity, it's only scraping part way through on some days

### Februrary 25th, 2021
The issue from Feb 22nd was resolved. Twitter seems to be temp-banning my searches with some daily limit. But each day that limit is erased and I can go back to querying.
Placing a time.sleep(10) after every 1000 queries seems to allow me to scrape more each day

### February 28th, 2021
I'm slowly filling out the month of March. 
The bulk of tweets with word 'covid' seem to be around the 2nd week of March, when the "two-week shutdown until we can go back to normal" began, lol.

### March 1st, 2021
Date is no longer a string and is now a datetime object. Graph for February 'covid' data looks a lot cleaner. I made a regression line for mean daily sentiment score across February. I also made a mean weekly score, but
https://colab.research.google.com/drive/1GCYOvSut2lhp0X5iAXLjG-0vHUE8d1Dx?usp=sharing

### March 2nd, 2021
I've got 2/3rds of March data. I suspect collecting April, May, etc. will be *much* faster.
I just have to keep collecting ~600,000 tweets per day seems to be the temp-ban limit (will investigate this further)

### March 5th, 2021
I finally have all of March 2020 (1st to 31st). In total, I'd estimate there are ~10,000,000 tweets with the word 'covid' in them.

### March 6th, 2021
I'm now beginning to clean each file by storing the date and sentiment score of each day in March.
I started with my February file (~233,000 Tweets) by cleaning it and running my sentiment analysis on it. It took 1.3 hours to complete and save the cleaned dataframe to a new csv file.

### March 7th, 2021
I just realized that I can scrape for more variables other than Tweet text, datetime, tweetID, and username... Here's a list of variables worth considering:


**Great Variables to Use**
| Variable     | Description   |
|:------------:|:------------- |
Datetime       | Date and Time of the Tweet
Tweet Text     | Content of the Tweet
Reply Count    | # of people who responded to the Tweet
Retweet Count  | # of retweets
Likes per Tweet| # of likes per tweet
Verified       | Boolean of whether or not the Tweet's user is verified
Follower Count | # of followers the Tweet's user has

**Variables that Could be Good to Use**
| Variable   | Description   |
|:----------:|:------------- |
Location     | User-entered location (not always present)
Username     | Username of the Tweeter
TweetID      | ID associated with that individual tweet
URL          | The URL of the tweet can be used to access it online
Language     | World Language (english is abbreviated 'en')
Friends Count| # of people the twitter user follows

**Variables that are probably Useless**
| Variable         | Description   |
|:----------------:|:------------- |
tcooutlinks        | # creates a list of hyperlinks used in the tweet
Quote Count        | # of times the tweet has been retweeted with a new comment
ConversationID     | Twitter thread ID 
User Description   | Twitter user description at the top of their profile
Favourites Count   | # of likes the user has accumulated thru all their Tweets
Listed Count       | # of public lists the user is a member of
Media              | Type of Media (ex: photo, gif, video)


### March 8th, 2021
I was using a bunch of different programs at the same time, but it took 10290 seconds (2.86 hours to run the sentiment_scores() function on the March01_07_2020 file which contains 387903 tweets.
It's definitely worth looking into faster sentiment analysis methods.

### March 29th, 2021
Summary of Goals for Spring Quarter:
- Graphs
  - US map showing average sentiment on Twitter per day by state
  - Regression of daily and weekly sentiment
- Prediction
  - Covid case rates by state by using sentiment as the key predictor
    - Can a state's reaction to the coronavirus predict its number of cases?
- Summary of Existing Data
  - Currently have all tweets in February & March that contain the word 'covid'
    - This is about ~10,000,000 tweets
    - Variables collected: 'Datetime', 'Tweet_Text', 'ReplyCount', 'RetweetCount', '#_of_likes', 'verified', '#_of_followers', 'location', 'Sentiment_score'
  - Other target dates are: 
    - October 1st-12th, 2020 (when President Trump got the virus)
    - December 2020, vaccines are released to the public


### April 7th, 2021
I was able to extract state names from the location variable and began working on constructing a map of the US showing average sentiment per day by state

### April 13th, 2021
I averaged sentiment score across each day by state. This will be the basis for the coloring of the map.

### April 17th, 2021
I found which mapping tool in Python I want to use: choropleth using the geopandas library.
I found this github content (https://raw.githubusercontent.com/python-visualization/folium/master/examples/data) that contains the geoJSON file for the US states

### April 20th, 2021
I completed a working map that shows the average sentiment scores by state. So far, it covers March 1st to 7th 2020 and you can interactively move between dates.
Next is:
- Gather sentiment scores for the rest of the data I have
  - Write script that updates the datasets in Sublime, rather than google collab
- Graph all the data I have
- Start building a model to predict either COVID cases or deaths based on a state's sentiment scores.

### April 21st, 2021
Uploaded images of regression graph and choropleth. Note: the actual choropleth is interactive, this is just a PNG of that graph.

![February Daily Regression Graph](https://github.com/hglanz/DSFellow_COVID_SocialMedia/blob/main/SocialMedia/Declans_Files/Twitter/feb%20sentiment%20regression.png?raw=true)

![US Map](https://github.com/hglanz/DSFellow_COVID_SocialMedia/blob/main/SocialMedia/Declans_Files/Twitter/us%20map%20sentiment%20march%2001%20to%2007%202020.PNG?raw=true)

### April 25th, 2021
After ~4 days of running code on my machine, I now have sentiment scores for all of February & March 2020. 
I need to filter out the covid tweet files to capture the correct location data (ie: by state).

### April 28th, 2021
I'm still working on a pipeline to capture location data.
I found a dataset that contains case and death rates. It's a little messy so I need to clean it first.
This covid dataset contains the following variables:
- ObservationDate
- Province/State
- Country/Region
- Confirmed
- Deaths
- Recovered



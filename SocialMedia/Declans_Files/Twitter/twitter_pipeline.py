#libraries
import pandas as pd
import nltk
from nltk.corpus import stopwords
import twython
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#!pip install vaderSentiment    ----->   for google collab
import vaderSentiment
#nltk.download('vader_lexicon')


################################################################################################################

# insert any twitter dataset here
df_covid = pd.read_csv("covid_mar20_2020.csv")

# Split Date variable to date and time
df_covid[['Date','Time']] = df_covid.Datetime.str.split(expand=True)
# Convert Date to datetime object
df_covid.Date = pd.to_datetime(df_covid["Date"], format="%Y-%m-%d")

# drop Time variable
df_covid.drop(['Time'], axis = 1, inplace = True)



# For stopword removal
#nltk.download('stopwords')
stop = set(stopwords.words('english'))

# new column for cleaned for stopwords (and lowercase) tweet Text
df_covid['Clean_text'] = df_covid['Tweet_Text'].apply(lambda x: ' '.join([word for word in x.lower().split() if word not in (stop)]))



# function that prints just the overall compound score of each tweet
def sentiment_scores(sentence): 
	# Create a SentimentIntensityAnalyzer object.
	sid_obj = SentimentIntensityAnalyzer()

	# polarity_scores method of SentimentIntensityAnalyzer 
	# object gives a sentiment dictionary which contains pos, neg, neu, and compound scores
	sentiment_dict = sid_obj.polarity_scores(sentence)

	return sentiment_dict['compound']



# create senitment score column
df_covid['Sentiment_score'] = df_covid["Clean_text"].apply(sentiment_scores)


# drop Clean_text variable
df_covid.drop(['Clean_text'], axis = 1, inplace = True)


df_covid.to_csv('covid_mar20_2020_clean.csv', sep=',', index=False)
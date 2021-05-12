import pandas as pd




df_covid = pd.read_csv("covid_mar01_07_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar01_07 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar01_07.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar08_11_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar08_11 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar08_11.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar12_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar12 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar12.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar13_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar13 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar13.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar14_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar14 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar14.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar15_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar15 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar15.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar16_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar16 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar16.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar17_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar17 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar17.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar18_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar18 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar18.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar19_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar19 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar19.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar20_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar20 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar20.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar21_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar21 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar21.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar22_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar22 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar22.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar23_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar23 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar23.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar24_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar24 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar24.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar25_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar25 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar25.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar26_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar26 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar26.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar27_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar27 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar27.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar28_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar28 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar28.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar29_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar29 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar29.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar30_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar30 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar30.reset_index(inplace=True)


df_covid = pd.read_csv("covid_mar31_2020_clean_location.csv")
# create new columns of date and time
df_covid[['Date','Time']] = df_covid['Datetime'].str.split(expand=True)

state_sentiment_mar31 = pd.DataFrame(df_covid.groupby(['Date', 'my_state'])['Sentiment_score'].mean())
state_sentiment_mar31.reset_index(inplace=True)









df = pd.concat([state_sentiment_mar01_07, 
	state_sentiment_mar08_11,
	state_sentiment_mar12,
	state_sentiment_mar13,
	state_sentiment_mar14,
	state_sentiment_mar15,
	state_sentiment_mar16,
	state_sentiment_mar17,
	state_sentiment_mar18,
	state_sentiment_mar19,
	state_sentiment_mar20,
	state_sentiment_mar21,
	state_sentiment_mar22,
	state_sentiment_mar23,
	state_sentiment_mar24,
	state_sentiment_mar25,
	state_sentiment_mar26,
	state_sentiment_mar27,
	state_sentiment_mar28,
	state_sentiment_mar29,
	state_sentiment_mar30,
	state_sentiment_mar31], ignore_index = True)

df.to_csv('daily_covid_sent_avg.csv', sep=',', index=False)

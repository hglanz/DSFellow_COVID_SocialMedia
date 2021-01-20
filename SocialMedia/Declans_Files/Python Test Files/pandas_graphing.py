# even better pandas tutorial
# https://realpython.com/pandas-plot-python/#:~:text=%20Plot%20With%20Pandas%3A%20Python%20Data%20Visualization%20for,you%20a%20general%20overview%20of%20a...%20More%20


import pandas as pd



download_url = ("https://raw.githubusercontent.com/fivethirtyeight/"
	"data/master/college-majors/recent-grads.csv")


df = pd.read_csv(download_url)

# This is a dataframe for pandas
type(df)

# .set_option is for displaying more than the minimum number of columns that .head() usually displays
pd.set_option("display.max.columns", None)

# Default number of rows is 5, but you can change that

#print(df.head(10))
print(df.head())



import matplotlib.pyplot as plt

#df.plot(x="Rank", y=["P25th", "Median", "P75th"], kind = "hist", alpha = 0.5)     # alpha is for transparency
df.plot(x = "Rank", y = ["P25th", "Median", "P75th"], kind = "line")
#df.plot(x = "Rank", y = "P25th", kind = "scatter")


plt.show()


# different options for the optional 'kind' parameter that .plot() uses

'''
"area" is for area plots.
"bar" is for vertical bar charts.
"barh" is for horizontal bar charts.
"box" is for box plots.
"hexbin" is for hexbin plots.
"hist" is for histograms.
"kde" is for kernel density estimate charts.
"density" is an alias for "kde".
"line" is for line graphs.
"pie" is for pie charts.
"scatter" is for scatter plots.
'''



# This is how to graph using plt:
import matplotlib.pyplot as plt
plt.plot(df["Rank"], df["P75th"])
plt.show()

# This is how to graph using the dataframe's name:
# This version, which relies on 
df.plot(x = "Rank", y = "P75th")
plt.show()
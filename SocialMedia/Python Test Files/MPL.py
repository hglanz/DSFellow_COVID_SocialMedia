# pandas
# https://pythonbasics.org/read-excel/#:~:text=Read%20Excel%20files%20%28extensions%3A.xlsx%2C.xls%29%20with%20Python%20Pandas.%20To,DataFrame%20structure%2C%20which%20is%20a%20tabular%20like%20structure.

# matplotlib
# https://pbpython.com/effective-matplotlib.html#:~:text=%20If%20you%20take%20nothing%20else%20away%20from,seaborn%20for%20the%20more%20complex%20statist...%20More%20

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns


df = pd.read_excel("https://github.com/chris1610/pbpython/blob/master/data/sample-salesv3.xlsx?raw=true")

print(df.head())


#print(df)     # 1500 rows by 7 columns

print()

#print(plt.style.available)


top_10 = (df.groupby('name')['ext price', 'quantity'].agg({'ext price': 'sum', 'quantity': 'count'})
          .sort_values(by='ext price', ascending=False))[:10].reset_index()
top_10.rename(columns={'name': 'Name', 'ext price': 'Sales', 'quantity': 'Purchases'}, inplace=True)

#print(top_10)

plt.style.use('seaborn-dark')

top_10.plot(kind = 'barh', y="Sales", x="Name")

# This will print the plot in another window
#plt.show()


%matplotlib inline




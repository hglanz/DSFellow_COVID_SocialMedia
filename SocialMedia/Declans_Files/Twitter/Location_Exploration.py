import pandas as pd

df_covid = pd.read_csv("covid_mar20_2020_clean.csv")

df_covid.dropna(inplace=True)

state_abbrev = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'fl', 'ga', 'hi', 'id', 'il', 'in', 'ia', 
                'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 
                'nm', 'ny', 'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']
state_long = ['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida',
              'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine',
              'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska',
              'nevada', 'new hampshire', 'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'ohio',
              'oklahoma', 'oregon', 'pennsylvania', 'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas',
              'utah', 'vermont', 'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming']

# combine these two lists
state_list = state_abbrev + state_long

###########################################################################################################

import re
import numpy as np

state_abbrev_upper = [state.upper() for state in state_abbrev]

index_list = []

# convert each location observation to lowercase and split by white space
for row in df_covid['location'].str.lower().str.split():
  # This is used to see if a US state was found in each observation
  did_i_find_a_state = False
  # each 'row' is an observation, split into multiple words. Ex: ['Washington', 'USA']
  for item in row:
    # each item need to be alpha characters only
    item = re.sub('[^a-zA-Z]+', '', item)
    # check to see if an item is in the state's list. If it is, break because the state 
    #(full name or abbreviation) is the only thing I care about for each observation
    if item in state_list:
      did_i_find_a_state = True
      break
  if did_i_find_a_state is True:
    # find the index (number) of the state in the state_list
    spot = state_list.index(item)
    # the state list is 100 items long, the last 50 are the full names of states, and I only want the abbreviations
    if spot >= 50:
      spot = spot - 50
    # This is what I want: the uppercase abbreviation of states.
    index_list.append(state_abbrev_upper[spot])
  # if a US state was not found in the observation, enter this string that can be filtered out later
  else:
    index_list.append('state_not_found')

###########################################################################################################

# use the uppercase state abbreviations as a new column
df_covid['my_state'] = index_list

# filter out observations that did not include US states
df_covid = df_covid[df_covid.my_state != "state_not_found"]

df_covid.to_csv('covid_mar20_2020_clean_location.csv', sep=',', index=False)
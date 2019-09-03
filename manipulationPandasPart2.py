# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:40:21 2019

@author: dcamp
"""

# Import pandas
import pandas as pd 
import os
# Set directory where the information is 
os. chdir(r"C:\Users\dcamp\Documents\python-practice\Pandas")

# Import Twitter data as DataFrame: df
df = pd.read_csv('tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
        langs_count[entry] += 1 
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print('Number of tweets in different languages'.upper())
print(langs_count)

# AS A FUNCTION
# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count

print('Number of tweets in different languages as a function'.upper())
count_langs = count_entries(df, 'lang')
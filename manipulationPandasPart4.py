# -*- coding: utf-8 -*-
"""
Created on Sun May 24 19:33:25 2020

@author: dcamp
"""

# Creating pandas from lists of data

import pandas as pd 

cities = ['New York', 'Paris', 'Brussels', 'Rome']
visitors = [150, 100, 50, 75]
number_holidays = [10, 8, 6, 12]
weekdays = ['Sun', 'Sun', 'Mon', 'Mon']
list_labels = ['cities', 'visitors', 'n_hollidays', 'weekdays']
list_cols = [cities, visitors, number_holidays, weekdays]
zipped = list(zip(list_labels,list_cols))
data = dict(zipped)
df = pd.DataFrame(data)
print(df)
# Broadcasting new key
df['money_spent'] = 1
print(df)

heights = [180, 170, 156]
# Broadcasting sex:M without making for loops
results = {'height': heights, 'sex': 'M'}
df_2 = pd.DataFrame(results)
print(df_2)
df_2.columns = ['height (cm)', 'gender']
df_2.index = ['a', 'b', 'c']

# Making a plot and saving it on a PFD format 
import matplotlib.pyplot as plt
df.plot()
plt.yscale('log')
plt.savefig('example.pdf')
plt.show()

df.plot(subplots=True)
plt.savefig('example_subplots.pdf')
plt.show()


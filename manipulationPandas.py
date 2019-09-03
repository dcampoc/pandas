# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import os
# Set directory where the information is 
os. chdir(r"C:\Users\dcamp\Documents\python-practice\Pandas")
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)

# Viualization of a particular row as data frames
print('AUSTRALIA -EXAMPLE-')
print('Type 1')
print(cars.loc['AUS'])
print('Type 2')
print(cars.iloc[1])

# Viualization of a particular row as data 
print('RUSSIA -EXAMPLE-')
print('Type 1')
print(cars.loc[['RU']])
print('Type 2')
print(cars.iloc[[4]])


# Viualization of particular data 
print('DATA ADQUISITION -EXAMPLE-')
print('The cars per cap of ' + cars.iloc[-1,1] + ' is: ' + str(cars.iloc[-1,0]))

# Viualization of a particular column as data frame and data
print('All countries as dataframe:'.upper())
print(cars.iloc[:,1])

print('All countries as data:'.upper())
print(cars.iloc[:,[1]])

# Extraction of colums in the easiest way
print('All countries as data (again):'.upper())
print(cars[['country']])

# Add new row of particular data 
print('add new colum with for structure'.upper())
for lab, row in cars.iterrows():
    cars.loc[lab, 'COUNTRY'] = row['country'].upper()
print(cars)

# Use .apply(str.upper)
print('add new column more efficiently'.upper())
cars['country'.upper()] = cars['country'].apply(str.upper)

print(cars)

# Extraction of several colums in the easiest way
print('Extraction of several colums'.upper())
print(cars[['COUNTRY','drives_right']])





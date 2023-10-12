# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:37:24 2023

@author: Personal
"""

import pandas as pd;

file_path = 'D:\FILES_MEDIATED/data.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Now you can work with the DataFrame 'df'
# For example, you can print the first few rows using the head() method
print(df.head(1))
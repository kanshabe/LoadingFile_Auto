# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 13:04:02 2023

@author: Personal
"""

import os

# Specify the directory path where you want to list files
directory_path = "D:\AIRTEL_Vou_Files\combined"

# Use list comprehension to generate an array of file names
file_names = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

# Print the list of file names
for file in file_names:
    print(file)

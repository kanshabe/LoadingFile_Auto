import os
import csv

from file_directory import Dir_path

# directory of the file with headers or tablecolumns
columnsfile = os.path.join(Dir_path, 'headers_test.csv')

with open(columnsfile, 'r') as fr:
    csvf = csv.reader(fr)
    headers = next(csvf)

#print(headers)
# removing the last column.
headers.pop()
#print(headers)


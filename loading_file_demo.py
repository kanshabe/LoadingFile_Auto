import gzip

import os
import sys
import csv

#sys.path.append('c:\\users\\personal\\appdata\\local\\programs\\python\\python311\\lib\\site-packages')

import pymysql
from dsn_connectivity import conn, table_name

#print(dir(pymysql))

Dir_path ='D:\\DATA_LOADING_FILES'
out_dir = os.path.join(Dir_path, 'output_demo')
csvfile = os.path.join(Dir_path, 'headers_test.csv')

with open(csvfile, 'r') as fr:
    csvf = csv.reader(fr)
    headers = next(csvf)


#print(headers)
headers.pop()
#print(headers)

#exit()

if not os.path.exists(out_dir):
    os.mkdir(out_dir)

input_file = os.path.join(Dir_path, "cbs_cdr_voice_20230910_601_101_486076.add.gz")

try:
    print(input_file)
    #print(dir(zf))
    with gzip.open(input_file, 'rt') as obj:
        data_to_insert = list()
        for line in obj:
            data = line.strip().split('|')
            data_to_insert.append(data)
        #print(obj.read())
        #print(len(data))
except Exception as e:
    print(f'Error {e}')
fields = "?"   
for _ in range(447):
    fields += ", ""?"
    
cols = ", ".join(headers)
#print(cols)
#print(data_to_insert)
#table_name = 'headers_test'
sql = f"INSERT INTO {table_name} ({cols}) VALUES ({fields})"
#print(sql)

# Create a cursor and execute the INSERT query using executemany
cursor = conn.cursor()
try:
    cursor.executemany(sql, data_to_insert)
    
    # Commit the transaction
    conn.commit()
except Exception as err:
    print(f"Error : {err}")
    
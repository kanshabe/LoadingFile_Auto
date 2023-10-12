import os
import gzip


from file_directory import Dir_path
from loading_to_db import load_data_into_db

# directory to the input files
#input_file = os.path.join(Dir_path, "cbs_cdr_voice_20230910_601_101_486076.add.gz")

# unzip the input file
def file_loader():
   try:
    # print(input_file)
    #print(dir(zf)) 
    for root, dirs, files in os.walk(Dir_path):
        for file_name in files:
            if file_name.endswith('.gz') and file_name.startswith('cbs_cdr'):
                # Create the full path to the gzip-compressed file
                 gz_file_path = os.path.join(root, file_name)
                 
                 # Check if the file exists
                 #if os.path.exists(gz_file_path):
                
                 with gzip.open(gz_file_path, 'rt') as obj:
                      data_to_insert = list()
                      for line in obj:
                          data = line.strip().split('|')
                          data_to_insert.append(data)
                      load_data_into_db(data_to_insert)
                #print(obj.read())
                #print(len(data))
   except Exception as e:
    print(f'Error {e}')

# Call the function
file_loader()




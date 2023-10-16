import os

# directory of the files to load
Dir_path ='D:\\MULTIPROCESSING_FILES'

# directory for output files
out_dir = os.path.join(Dir_path, 'output_folder')
if not os.path.exists(out_dir):
    os.mkdir(out_dir)




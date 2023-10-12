import csv
import os

BASEPATH="D:\\"
workingpath=os.path.join(os.path.join(BASEPATH, 'AIRTEL_Vou_Files'), 'combined')
outputpath = os.path.join(os.path.join(BASEPATH, 'AIRTEL_Vou_Files'), 'output')

def check_dir_exist(d):
    if not os.path.exists(d):
        os.makedirs(d)
check_dir_exist(outputpath)
os.chdir(workingpath)

def create_from_csv_list(f):
    row = []
    with open(f, 'r') as fr:
        csv_reader = csv.reader(fr)
        for line in csv_reader:
            #print(line)
            row.append(line)
    return row
    
data1 = create_from_csv_list('cbs_cdr_vou_20230827_601_101_567867.add')
data2= create_from_csv_list('cbs_cdr_vou_20230827_601_101_567685.add')
data3 = create_from_csv_list('cbs_cdr_vou_20230827_601_101_567687.add')
data4 = create_from_csv_list('cbs_cdr_vou_20230827_601_101_567733.add')
print(len(data1))
data = list()
#data.extend(data1)
#data.extend(data2)
#data.extend(data3)

for root, dirs, files in os.walk(workingpath):
    for file in files:
        if file.endswith('.add') and file.startswith('cbs_cdr'):
            rows = create_from_csv_list(file)
            data.extend(rows)

print(len(data))
with open(os.path.join(os.path.dirname(workingpath), 'merge_file.add'), 'w') as fw:
    csv_writer = csv.writer(fw)
    #for line in data:
    csv_writer.writerows(data)
#print(data)

output_file = os.path.join(outputpath, "merged.add")

try:
    # Open the output file in write mode
    with open(output_file, "w") as merged_file:
        for root, dirs, files in os.walk(workingpath):
            for input_file in files:
                if input_file.endswith('.add') and input_file.startswith('cbs_cdr'):
                    try:
                        # Open each input file in read mode
                        print(input_file)
                        with open(input_file, "r") as current_file:
                            # Read the contents of the current input file
                            file_contents = current_file.read()
                            print(file_contents)
                            # Write the contents to the output file
                            merged_file.write(file_contents)
                            # Optionally, add a separator between file contents
                            merged_file.write("\n---\n")
                    except FileNotFoundError:
                        print(f"File not found: {input_file}")
                    except Exception as e:
                        print(f"Error processing {input_file}: {e}")
    print("Merging completed successfully.")
except Exception as e:
    print(f"Error merging files: {e}")


'''
cbs_cdr_vou_20230827_601_101_567685.add
-a----         8/27/2023   9:26 AM          93745 cbs_cdr_vou_20230827_601_101_567687.add
-a----         8/27/2023   9:26 AM          68748 cbs_cdr_vou_20230827_601_101_567689.add
-a----         8/27/2023   9:26 AM          99681 cbs_cdr_vou_20230827_601_101_567733.add
-a----         8/27/2023   9:26 AM          94403 cbs_cdr_vou_20230827_601_101_567745.add

os.chdir('D:\\AIRTEL_Vou_Files\\combined')



# List of file names to be merged
input_files = []

# Output file where the merged contents will be saved
output_file = "merged.add"

try:
    # Open the output file in write mode
    with open(output_file, "w") as merged_file:
        for input_file in input_files:
            try:
                # Open each input file in read mode
                with open(input_file, "r") as current_file:
                    # Read the contents of the current input file
                    file_contents = current_file.read()
                    # Write the contents to the output file
                    merged_file.write(file_contents)
                    # Optionally, add a separator between file contents
                    merged_file.write("\n---\n")
            except FileNotFoundError:
                print(f"File not found: {input_file}")
            except Exception as e:
                print(f"Error processing {input_file}: {e}")
    print("Merging completed successfully.")
except Exception as e:
    print(f"Error merging files: {e}")


'''
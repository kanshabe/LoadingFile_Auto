
import gzip
import csv

# Path to the gzip-compressed file
gzip_file_path = 'D:\AIRTEL_CDR/cbs_cdr_vou_20230829_601_101_262429.add.gz'

# Path for the output Excel file
output_excel_path = 'D:\AIRTEL_CDR/cbs_cdr_vou_20230829_601_101_262429.add.csv'

# Open the gzip-compressed file and read its contents
with gzip.open(gzip_file_path, 'rt') as f:
    # Read the decompressed data
    data = f.read()

# Split the data into lines (assuming it's in a line-separated format)
lines = data.splitlines()

# Create a CSV writer and open the output CSV file
with open(output_excel_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Iterate through the lines and write them as CSV rows
    for line in lines:
        # Process the line if needed (e.g., split by a delimiter)
        # For example, if the data is tab-separated:
        row = line.split('\t')
        csv_writer.writerow(row)

print(f"Converted {gzip_file_path} to {output_excel_path}")



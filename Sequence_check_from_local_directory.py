import os

def check_file_sequence(local_directory):
    # List files in the local directory
    local_files = os.listdir(local_directory)

    # Sort the file names
    local_files.sort()

    # Check the file sequence
    previous_file = None
    in_sequence = True

    for local_file_name in local_files:
        if previous_file:
            # Compare the current file to the previous one
            if local_file_name != previous_file:
                in_sequence = False
                print(f"File '{local_file_name}' is out of sequence.")
        previous_file = local_file_name

    if in_sequence:
        print("All files are in sequence.")

# Example usage:
local_directory = 'D:\\FILES_FROM_PYTHON'

check_file_sequence(local_directory)


import paramiko

import fnmatch

# SFTP Configuration
sftp_host = '192.168.90.25'
sftp_port = 22  # Default SFTP port
sftp_username = 'dkanshabe'
sftp_password = 'mYO4F1ML9T'
remote_directory = '/media/data1/trvs/airtel/04_ocs/OVOICE'
pattern = 'cbs_cdr_voice_20231003_'  # Modify this to your desired pattern

# Establish an SFTP connection
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(sftp_host, sftp_port, sftp_username, sftp_password)
sftp_client = ssh_client.open_sftp()

        
# List files in the remote directory
remote_files = sftp_client.listdir(remote_directory)


# Filter files based on the pattern
matching_files = fnmatch.filter(remote_files, pattern)

# Print the matching file names
for remote_file_name in matching_files:
    print(matching_files)
    
# Sort the file names
matching_files.sort()

# Check the file sequence
previous_file = None
in_sequence = True

for remote_file_name in matching_files:
    if previous_file:
        # Compare the current file to the previous one
        if remote_file_name != previous_file:
            in_sequence = False
            print(f"File '{remote_file_name}' is out of sequence.")
    previous_file = remote_file_name

if in_sequence:
    print("All files are in sequence.")

# Close the SFTP connection
sftp_client.close()
ssh_client.close()



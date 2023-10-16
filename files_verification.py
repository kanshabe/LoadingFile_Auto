import paramiko

import fnmatch

import os



# SFTP Configuration
sftp_host = '192.168.90.25'
sftp_port = 22  # Default SFTP port
sftp_username = 'dkanshabe'
sftp_password = 'mYO4F1ML9T'
remote_directory = '/media/data1/trvs/airtel/04_ocs/OVOICE'
pattern = 'cbs_cdr_voice_20231013_'  # Modify this to your desired pattern

# Establish an SFTP connection
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(sftp_host, sftp_port, sftp_username, sftp_password)
sftp_client = ssh_client.open_sftp()

        
# List files in the remote directory
remote_files = sftp_client.listdir(remote_directory)


# Filter files based on the pattern
matching_files = fnmatch.filter(remote_files, pattern)

def file_exists(matching_files):
    return os.path.exists(matching_files)

if file_exists(matching_files):
    print(f"The file '{matching_files}' exists.")
else:
    print(f"The file '{matching_files}' does not exist.")

# Close the SFTP connection
sftp_client.close()
ssh_client.close()


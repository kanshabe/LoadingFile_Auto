import paramiko



def download_files_with_pattern(sftp, remote_directory, local_directory, pattern):
    remote_files = sftp.listdir(remote_directory)

    for remote_file in remote_files:
        if remote_file.startswith(pattern) and remote_file.endswith('.gz'):
            remote_file_path = remote_directory + '/' + remote_file
            local_file_path = local_directory + '/' + remote_file

            # Download the file
            sftp.get(remote_file_path, local_file_path)

def main():
    host = '192.168.90.25'
    port = 22  # Default SFTP port
    username = 'dkanshabe'
    password = 'mYO4F1ML9T'

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(host, port, username, password)
    sftp_client = ssh_client.open_sftp()

    remote_directory = '/media/data1/trvs/airtel/04_ocs/OVOICE'
    local_directory = 'D:\\SEQUENCE_TEST_FILES'
    pattern = 'cbs_cdr_voice_20231008_'  # Modify this to your desired pattern

    download_files_with_pattern(sftp_client, remote_directory, local_directory, pattern)

    sftp_client.close()
    ssh_client.close()

if __name__ == "__main__":
    main()


#!/usr/bin/env python3
# -*- coding: utf-8  -*-

#
# Simple and Secure Backup
#
# GNU General Public License (GPL) 3.0
#
# Gerard Tost (recull@digipime.com)
# https://github.com/gerardtost/
#

import sys
import os
import paramiko
import datetime
import download_config

access = dict(hostname=download_config.remote_server,
             port=download_config.remote_port,
             username=download_config.remote_user,
             password=download_config.remote_psswd)

dir_log = download_config.log_path + "/" + download_config.log_name 
cd_dir_files = "cd " + download_config.remote_path

# Simple log
def write_log(line):  
    with open(dir_log, "a") as log:
        log.write("{} {}{}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), line, "\n"))

# SSH/SFTP clients
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())

try:
    client.connect(**access)
except paramiko.ssh_exception.NoValidConnectionsError:
    print("\nConnection Error: Please, verify your network connection or modify your remotes server or port in the config file.")
    sys.exit(1)
except paramiko.ssh_exception.AuthenticationException:
    print("\nAuthentication Error: Please, verify your connection data in the config file.")
    sys.exit(1)  

sftp = client.open_sftp()

try:
    sftp.chdir(download_config.remote_path)
except FileNotFoundError:
    print("\nWrong path: Please, verify your remote path in the config file.")
    sys.exit(1) 

if download_config.log_active:
    if not os.path.exists(download_config.log_path):
        print("\nWrong path: Please, verify your log path or disable log in the config file.")
        sys.exit(1) 

if not os.path.exists(download_config.local_path):
    print("\nWrong path: Please, verify your local path in the config file.")
    sys.exit(1)

myfiles = sftp.listdir()
print(myfiles)
total_myfiles = len(myfiles)

if not total_myfiles:
    if download_config.log_active:
        write_log("There are no files in the remote directory")
    print("There are no files in the remote directory")
    sys.exit(0)
else:
    if download_config.log_active:
        write_log("Total files and directories: {}".format(total_myfiles))
    print("Total files and directories: {}".format(total_myfiles))

    # Starting downloads
    print("Starting: downloading files to local directory")

for myfile in myfiles:
    verify_dir = str(sftp.lstat(myfile))
    if "d" not in verify_dir[0]:
        print("Starting the download of the \"{}\" file".format(myfile))
        if download_config.log_active:
            write_log("Starting the download of the \"{}\" file".format(myfile))

        myfile_remote = "{}/{}".format(download_config.remote_path, myfile)
        myfile_local = "{}/{}{}".format(download_config.local_path, datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S_"), myfile)

        sftp.get(myfile_remote, myfile_local)

        # File downloaded
        print("File \"{}\" downloaded successfully".format(myfile))
        if download_config.log_active:
            write_log("File \"{}\"  downloaded successfully".format(myfile))

        print("File renamed to {}{}".format(datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S_"), myfile))
        if download_config.log_active:
            write_log("File renamed to {}{}".format(datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S_"), myfile))

        # Delete remote files?
        if download_config.delete_active: 
            print("Deleting the remote file {}".format(myfile))

            if download_config.log_active:
                write_log("Deleting the remote file {}".format(myfile))

            sftp.remove(myfile_remote)
            print("Successfully deleted the remote file {}".format(myfile))

            if download_config.log_active:
                write_log("Successfully deleted the remote file {}".format(myfile))

sftp.close()
client.close()

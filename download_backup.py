#!/usr/bin/env python3
# -*- coding: utf-8  -*-

#
# Simple and Secure Backup 
# GNU General Public License (GPL) 3.0
# Gerard Tost (recull@digipime.com)
#

import paramiko
import datetime
import regex as re
import download_config

access = dict(hostname=download_config.remote_server,
             port=download_config.remote_port,
             username=download_config.remote_user,
             password=download_config.remote_psswd)

dir_log = download_config.log_path + "/" + download_config.log_name 
cd_dir_files = "cd " + download_config.remote_path

# Time details
search_today_date = re.search(r"^(\d{4}-\d{2}-\d{2}) (\d{2}):(\d{2})", str(datetime.datetime.now()))

today_date = "{}_{}-{}_".format(
    search_today_date[1], search_today_date[2], search_today_date[3])

today_date_log = "{} {}:{}".format(
    search_today_date[1], search_today_date[2], search_today_date[3])

# Simple log
def write_log(line):  
    with open(dir_log, "a") as log:
        log.write("{} {}{}".format(today_date_log, line, "\n"))

# SSH/SFTP clients
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect(**access)

sftp = client.open_sftp()
sftp.chdir(download_config.remote_path)

myfiles = sftp.listdir()
print(myfiles)
total_myfiles = len(myfiles)

if total_myfiles == 0:
    if download_config.log_active:
        write_log("There are no files in the remote directory")
    print("There are no files in the remote directory")
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
        myfile_local = "{}/{}{}".format(download_config.local_path, today_date, myfile)

        sftp.get(myfile_remote, myfile_local)

        # File downloaded
        print("File \"{}\" downloaded successfully".format(myfile))
        if download_config.log_active:
            write_log("File \"{}\"  downloaded successfully".format(myfile))

        print("File renamed to {}{}".format(today_date, myfile))
        if download_config.log_active:
            write_log("File renamed to {}{}".format(today_date, myfile))

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

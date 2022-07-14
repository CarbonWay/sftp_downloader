#!/usr/bin/env python3
# -*- coding: utf-8  -*-

import sys
import os
import datetime
from pathlib import Path

import paramiko
import tqdm

import download_config

access = dict(hostname=download_config.remote_server,
              port=download_config.remote_port,
              username=download_config.remote_user,
              password=download_config.remote_psswd,
              allow_agent=False,
              look_for_keys=False)

dir_log = "{}/{}".format(download_config.log_path, download_config.log_name)
allowed_extension = download_config.allowed_extension

def write_log(line):
    """Simple log """
    with open(dir_log, "a") as log:
        log.write("{} {}{}".format(datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"), line, "\n"))


class TqdmWrapper(tqdm.tqdm):
    """Progress bars by tqdm"""

    def viewBar(self, a, b):
        self.total = int(b)
        self.update(int(a - self.n))


def download_remote_file(connection, filename, remote_file, local_file):
    """Download the remote file in a local directory with a progress bar """
    attribs = vars(connection.lstat(remote_file))
    file_size = int(attribs["st_size"])

    print("File found: {}, Size: {} KB".format(
        filename, str(round(file_size/1024))))

    print("Starting the download of the \"{}\" file".format(filename))
    if download_config.log_active:
        write_log("Starting the download of the \"{}\" file".format(filename))

    with TqdmWrapper(ascii=False, unit='b', unit_scale=True) as pbar:
        connection.get(remote_file, local_file, callback=pbar.viewBar)

    print("File \"{}\" downloaded successfully".format(filename))
    if download_config.log_active:
        write_log("File \"{}\"  downloaded successfully".format(filename))


def delete_remote_file(connection, filename, remote_file):
    """Delete the remote file """

    attribs = vars(connection.lstat(remote_file))
    file_size = int(attribs["st_size"])

    print("Deleting the remote file {} with size {} KB".format(
        filename, str(round(file_size/1024))))
    if download_config.log_active:
        write_log("Deleting the remote file {}".format(filename))

    connection.remove(remote_file)

    print("Successfully deleted the remote file {}".format(filename))
    if download_config.log_active:
        write_log(
            "Successfully deleted the remote file {}".format(filename))

def file_exists(path):
    file_exists = os.path.exists(path)
    return file_exists

def match_extension(path):
    extension = Path(path).suffix
    match = True if extension == allowed_extension else False
    return match

# SSH/SFTP clients
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

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
    sftp.close()
    client.close()
    sys.exit(1)

if download_config.log_active:
    if not os.path.exists(download_config.log_path):
        print(
            "\nWrong path: Please, verify your log path or disable log in the config file.")
        sftp.close()
        client.close()
        sys.exit(1)

if not os.path.exists(download_config.local_path):
    print("\nWrong path: Please, verify your local path in the config file.")
    sftp.close()
    client.close()
    sys.exit(1)

myfiles = sftp.listdir()
print(myfiles)
total_myfiles = len(myfiles)

if not total_myfiles:
    if download_config.log_active:
        write_log("There are no files in the remote directory")
    print("There are no files in the remote directory")
    sftp.close()
    client.close()
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
        myfile_remote = "{}/{}".format(download_config.remote_path, myfile)
        myfile_local = "{}/{}".format(download_config.local_path, myfile)

        if match_extension(myfile):
            if file_exists(myfile_local):
                write_log("File is already here: {}. Skipping...".format(myfile))
                print("File is already here: {}. Skipping...".format(myfile))
                continue

            download_remote_file(sftp, myfile, myfile_remote,
                                myfile_local)

            # Delete remote files?
            if download_config.delete_active:
                delete_remote_file(sftp, myfile, myfile_remote)
        else:
            if download_config.log_active:
                write_log("{} is not a {} file. Skipping...".format(myfile, allowed_extension))
            print("{} is not a {} file. Skipping...".format(myfile, allowed_extension))
            continue

sftp.close()
client.close()
sys.exit(0)

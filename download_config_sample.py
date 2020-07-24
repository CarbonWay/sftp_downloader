# -*- coding: utf-8  -*-

#
# Sample config file for Simple and Secure Backup 
# GNU General Public License (GPL) 3.0
# Gerard Tost (recull@digipime.com)
#
# You can ask your ISP if you have doubts 
# about remote server, SSH or SFTP.
#

# SSH user
remote_user = "username" 

# SSH password
remote_psswd = "password-remote" 

# Server address
remote_server = "myserver.com" 
# or server IP address
remote_server = "78.192.6.122"

# Remote SSH Port
remote_port = "22"

# Remote folder
remote_path = "/home/remoteuser/files"

# Local folder
local_path = "/home/localuser/backups"

# Log configuration:
#
# Activity log ON: True
# Activity log OFF: False
log_active = True 

# Log folder and file name
log_path = "/home/localuser/backups"
log_name = "download_backups.log"

# Delete files after downloading?
#
# Yes, delete all files: True
# Nooo! Do not delete anything: False
delete_active = True
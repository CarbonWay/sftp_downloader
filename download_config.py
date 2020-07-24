# -*- coding: utf-8  -*-

#
# Config file for Simple and Secure Backup 
# GNU General Public License (GPL) 3.0
#
# Gerard Tost (recull@digipime.com)
# https://github.com/gerardtost/
#
# See download_config_sample.py for examples
#

# Remote
remote_user = "gerard"
remote_psswd = "unusuarimes"
remote_server = "192.168.1.100"
remote_port = "22"
remote_path = "/home/gerard/backupsproves"

# Local
local_path = "/home/base/proves"

# Logs
log_active = True
log_path = "/home/base/proves"
log_name = "download_backups.log"

# Delete files after downloading?
delete_active = False
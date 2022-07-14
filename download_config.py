# -*- coding: utf-8  -*-

#
# Config file for Simple and Secure Backup
#
# GNU General Public License (GPL) 3.0
#
# Gerard Tost (recull@digipime.com)
# https://github.com/gerardtost/
#
# See download_config_sample.py for examples
#

# Remote
remote_user = "demo"
remote_psswd = "password"
remote_server = "test.rebex.net"
remote_port = "22"
remote_path = ""
allowed_extension = ".txt"

# Local
local_path = "/home/carnation/Downloads/data"

# Logs
log_active = True
log_path = "/home/carnation/Downloads/data/logs"
log_name = "download_backups.log"

# Delete files after downloading?
delete_active = False

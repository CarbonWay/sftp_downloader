# SFTP Downloader

## Configuration

### Before installation

#### Main settings

The sample config file can be found in `src/download_config.py`.

#### Timer settings

The timer is implemented using systemd. The repeat interval can be changed in `/service/sftp-downloader.timer` file in `[Timer]` `OnUnitActiveSec` section.

### After installation

If you want to edit the config file after installation, it is located in `/opt/SFTPDownloader`.

#### Timer settings

1. `sudo systemctl stop sftp-downloader.timer`
2. Edit the file
3. Reload daemons: `sudo systemctl daemon-reload`
4. Start again: `sudo systemctl start sftp-downloader.timer`

## Install

```
git clone git@github.com:CarbonWay/sftp_downloader.git
cd sftp_downloader
sudo make install
```

## Remove

```
cd sftp_downloader
sudo make uninstall
```




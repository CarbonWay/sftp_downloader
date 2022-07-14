install: install_dependencies copy_files copy_service reload_services start_enable_service

uninstall:
	sudo rm -rf /opt/SFTPDownloader
	sudo systemctl stop sftp-downloader.timer
	sudo systemctl disable sftp-downloader.timer
	sudo rm /etc/systemd/system/sftp-downloader.timer
	sudo rm /etc/systemd/system/sftp-downloader.service
	sudo systemctl daemon-reload

install_dependencies: ./src/requirements.txt
	sudo pip install -r ./src/requirements.txt

copy_files: ./src/download_config.py ./src/download_backup.py
	sudo mkdir -p /opt/SFTPDownloader
	sudo cp ./src/download_config.py ./src/download_backup.py /opt/SFTPDownloader

copy_service: ./service/sftp-downloader.service ./service/sftp-downloader.timer
	sudo cp ./service/sftp-downloader.service ./service/sftp-downloader.timer /etc/systemd/system

reload_services:
	sudo systemctl daemon-reload

start_enable_service:
	sudo systemctl enable sftp-downloader.timer
	sudo systemctl start sftp-downloader.timer

clean:
	rm -rf __pycache__
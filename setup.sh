#!/bin/bash

# Update and Upgrade
sudo apt-get update
sudo apt-get upgrade -y

# Install Python, PIP, and Bluetooth packages
sudo apt-get install python3 python3-pip bluetooth bluez libbluetooth-dev wget -y
pip3 install pybluez

# Setup and move blover.py to /opt/blover/
sudo mkdir -p /opt/blover/
sudo cp blover.py /opt/blover/
sudo chmod +x /opt/blover/blover.py

# Enable and start Bluetooth service
sudo systemctl enable bluetooth
sudo systemctl start bluetooth

# Setup systemd service for blover
sudo cp blover.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable blover.service

# Download and setup Plover
wget -O /opt/plover.AppImage $(curl -s https://api.github.com/repos/openstenoproject/plover/releases/latest | grep browser_download_url | grep 'AppImage' | cut -d '"' -f 4)
sudo chmod +x /opt/plover.AppImage

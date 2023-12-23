#!/bin/bash

# Update and Upgrade
sudo apt-get update
sudo apt-get upgrade -y

# Install Python, PIP, and Bluetooth packages
sudo apt-get install python3 python3-pip bluetooth bluez libbluetooth-dev -y
pip3 install pybluez plover

# Setup Plover
# Here, add any necessary configuration or steps to setup Plover

# Enable and start Bluetooth service
sudo systemctl enable bluetooth
sudo systemctl start bluetooth

# Copy systemd service file
sudo cp blover.service /etc/systemd/system/

# Reload systemd manager and enable blover service
sudo systemctl daemon-reload
sudo systemctl enable blover.service

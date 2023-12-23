#!/usr/bin/env python3
import bluetooth
import sys

class BluetoothConnection:
    def __init__(self, address, port=3):
        self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.socket.connect((address, port))

    def send(self, text):
        if text:
            self.socket.send(text)

    def close(self):
        if self.socket:
            self.socket.close()

def find_bluetooth_device():
    nearby_devices = bluetooth.discover_devices()
    if not nearby_devices:
        print("No Bluetooth devices found.")
        sys.exit(1)
    return nearby_devices[0]  # Returns the address of the first found device

if __name__ == "__main__":
    # Find a Bluetooth device and establish a connection
    device_address = find_bluetooth_device()
    bt_conn = BluetoothConnection(device_address)
    try:
        # Your code to send data goes here
        pass
    finally:
        bt_conn.close()

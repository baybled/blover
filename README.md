# blover

blover is a Python application for Raspberry Pi that automatically connects to a Bluetooth device and communicates with it.

## Setup

0. One liner of the below
```
sudo git clone https://github.com/baybled/blover.git && cd blover && sudo chmod +x setup.sh && sudo ./setup.sh
```

1. Clone this repository:
```
git clone https://github.com/baybled/blover/
```
2. Navigate to the blover directory:
```
cd blover
```
3. Run the setup script:
```
sudo chmod +x setup.sh
./setup.sh
```


## Usage

- The `blover.py` script will automatically handle Bluetooth communication.
- The `blover_extension.py` extends Plover's translation module to send data via Bluetooth.
- Customize as needed for specific use-cases.

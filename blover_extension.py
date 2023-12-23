from plover.translation import Translator as BaseTranslator
import bluetooth

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

class BloverTranslator(BaseTranslator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        device_address = self.find_bluetooth_device()
        self.bt_conn = BluetoothConnection(device_address)

    def find_bluetooth_device(self):
        nearby_devices = bluetooth.discover_devices()
        if not nearby_devices:
            print("No Bluetooth devices found.")
            raise RuntimeError("No Bluetooth devices found")
        return nearby_devices[0]  # Connect to the first found device

    def translate(self, stroke):
        super().translate(stroke)
        translated_text = self.get_last_translation()
        self.bt_conn.send(translated_text)

    def get_last_translation(self):
        # Implement based on Plover's translation storage mechanism
        return "example"  # Placeholder

    def __del__(self):
        self.bt_conn.close()

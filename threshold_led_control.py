import smbus
import time

bus = smbus.SMBus(1)
address = 0x08
threshold = 50

while True:
    try:
        value = bus.read_byte(address)
        print(f"Received from Arduino: {value}")
        if value > threshold:
            print("Value crossed threshold! Sending ON signal.")
            bus.write_byte(address, 1)
        else:
            print("Value below threshold. Sending OFF signal.")
            bus.write_byte(address, 0)
        time.sleep(1)
    except Exception as e:
        print("Error:", e)

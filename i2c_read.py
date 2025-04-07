import smbus2
import time

# Create I2C bus instance
bus = smbus2.SMBus(1)

# I2C address of Arduino Nano (based on your earlier `i2cdetect`, it was 0x08)
DEVICE_ADDRESS = 0x08

while True:
    try:
        # Read one byte from Arduino
        data = bus.read_byte(DEVICE_ADDRESS)
        print("Received from Arduino:", data)
        time.sleep(1)
    except Exception as e:
        print("Error:", e)
        time.sleep(1)

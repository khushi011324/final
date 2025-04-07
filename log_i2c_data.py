import smbus
import time
import csv
from datetime import datetime

bus = smbus.SMBus(1)
address = 0x08

with open("i2c_data_log.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Value"])
    while True:
        try:
            value = bus.read_byte(address)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([timestamp, value])
            print(f"{timestamp} - Value: {value}")
            time.sleep(1)
        except Exception as e:
            print("Error:", e)

import time
from datetime import datetime
import board
from adafruit_bme280 import basic as adafruit_bme280
import json

i2c = board.I2C()

bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

while True:
    tempc = bme280.temperature
    tempf = tempc * 1.8 + 32

    temperature = "{:.2f} F".format(tempf)
    pressure = "{:.2f} hPa".format(bme280.pressure)
    humidity = "{:.2f} %".format(bme280.humidity)
    
    data = {
        "feed_url": "http://192.168.0.89/bme280.json",
        "title_image": "https://tidbyt-json-display.s3.eu-west-1.amazonaws.com/heart.png",
        "title_text": "BME280",
        "data": [
            {
                "title": "Temperature",
                "value": temperature,
                "color": "FF0000"
            },
            {
                "title": "Pressure",
                "value": pressure,
                "color": "00FF00"
            },
            {
                "title": "Humidity",
                "value": humidity,
                "color": "0000FF"
            }
        ]
    }
    
    # Convert the dictionary to a JSON string
    json_string = json.dumps(data, indent=4)
    print(json_string)
    time.sleep(4)

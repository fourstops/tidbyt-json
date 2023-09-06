import time
from datetime import datetime
import board
from adafruit_bme280 import basic as adafruit_bme280
import json

i2c = board.I2C()

bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

data = {
    "feed_url": "https://tidbyt-json-display.s3.eu-west-1.amazonaws.com/example.json",
    "title_image": "https://tidbyt-json-display.s3.eu-west-1.amazonaws.com/heart.png",
    "title_text": "BME280",
    "data": [
        {
            "title": "Temperature",
            "value": bme280.temperature,
            "color": "FF0000"
        },
        {
            "title": "Pressure",
            "value": bme280.pressure,
            "color": "00FF00"
        },
        {
            "title": "Humidity",
            "value": bme280.humidity,
            "color": "0000FF"
        }
    ]
}

# Convert the dictionary to a JSON string
json_string = json.dumps(data, indent=4)

# Print the JSON string
print(json_string)

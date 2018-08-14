
import time
from Adafruit_IO import Client, Feed


ADAFRUIT_IO_KEY = '3737c351de8e4f2b851d5dfd62118ef7'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username).
ADAFRUIT_IO_USERNAME = 'ChriisBrown'

# Create an instance of the REST client.
aio = Client(ChriisBrown, 3737c351de8e4f2b851d5dfd62118ef7)

temperature_feed = aio.feeds('temperature')

def temperatures():
    from w1thermsensor import W1ThermSensor
    for sensor in W1ThermSensor.get_available_sensors():
        data.append(sensor.get_temperature())
    return(data)
	

while True:
    temperature = temperatures
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature))
        # Send humidity and temperature feeds to Adafruit IO
        temperature = '%.2f'%(temperature)
        aio.send(temperature_feed.key, str(temperature))
    else:
        print('Failed to get DHT22 Reading, trying again in ', '10', 'seconds')
    # Timeout to avoid flooding Adafruit IO
    time.sleep(10)
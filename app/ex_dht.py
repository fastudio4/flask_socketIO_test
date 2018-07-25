from pyA20.gpio import gpio
from pyA20.gpio import port
import time
import dht11


PIN2 = port.PA6
gpio.init()


instance = dht11.DHT11(pin=PIN2)

while True:
    result = instance.read()
    if result.is_valid():
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)

    time.sleep(1)


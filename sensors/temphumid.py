import Adafruit_DHT


def run_dht():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        global temp
        global humid
        temp = '{0:0.1f} C'.format(temperature)
        humid = '{0:0.1f} %'.format(humidity)

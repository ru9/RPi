import _thread
import time
from sensors import *
import httpserver

print('Initiating temp and humidity sensor')
_thread.start_new_thread(temphumid.run_dht, tuple())
print('Temp and humidity sensor started')

time.sleep(6)

print('Initiating Server')
httpserver.run_server()

#!/usr/bin/python
#import sys
import time
import Adafruit_DHT
humidity, temperature = Adafruit_DHT.read_retry(22, 4)
print temperature

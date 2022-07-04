import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT)
GPIO.output(27, GPIO.LOW)
try:
	while True:
		time.sleep(0.1)		

except:
	GPIO.cleanup()


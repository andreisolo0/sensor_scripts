#!/usr/bin/python
# Flame sensor script for using with RaspberryPI
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
FLAME_SENSOR_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME_SENSOR_PIN, GPIO.IN)

#initialization
previous_value=GPIO.input(FLAME_SENSOR_PIN)
if GPIO.input(FLAME_SENSOR_PIN) == 1:
    print("CLEAR")
else:
    print("FIRE")

# infinite loop
#while True:
#        time.sleep(1)
#        if previous_value != GPIO.input(FLAME_SENSOR_PIN):
#            if GPIO.input(FLAME_SENSOR_PIN) == 1:
#                print("CLEAR")
#            else:
#                print("FIRE")
#            previous_value = GPIO.input(FLAME_SENSOR_PIN)

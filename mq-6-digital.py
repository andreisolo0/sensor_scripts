#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
MQ6_SENSOR_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(MQ6_SENSOR_PIN, GPIO.IN)

#initialization
previous_value=GPIO.input(MQ6_SENSOR_PIN)
if GPIO.input(MQ6_SENSOR_PIN) == 1:
    print("CLEAR")
else:
    print("LPG")
#while True:
#        time.sleep(1)
#        if previous_value != GPIO.input(MQ6_SENSOR_PIN):
#            if GPIO.input(MQ6_SENSOR_PIN) == 1:
#                print("CLEAR")
#            else:
#                print("LPG")
#            previous_value = GPIO.input(MQ6_SENSOR_PIN)


# arduino-cli
# create the .ino file. Check mq-6 directory
# arduino-cli lib install MQUnifiedsensor - to add library
# arduino-cli compile -b arduino:avr:uno . - to compile .ino in current directory
# arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno . 
# arduino-cli  monitor -p /dev/ttyACM0
# https://roboticsbackend.com/raspberry-pi-arduino-serial-communication/
# read from serial

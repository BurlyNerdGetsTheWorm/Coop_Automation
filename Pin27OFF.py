#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)


def trigger():
    GPIO.output(27,True)
try:
    trigger()

except KeyboardInterrupt:
    print ("Quit")
    GPIO.cleanup()
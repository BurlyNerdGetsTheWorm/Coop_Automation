#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)


def trigger():
    GPIO.output(2,True)
try:
    trigger()

except KeyboardInterrupt:
    print ("Quit")
    GPIO.cleanup()
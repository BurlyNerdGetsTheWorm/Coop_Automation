#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)


def trigger():
    GPIO.output(17,True)
try:
    trigger()

except KeyboardInterrupt:
    print ("Quit")
    GPIO.cleanup()
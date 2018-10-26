#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(9,GPIO.OUT)


def trigger():
    GPIO.output(9,False)
try:
    trigger()

except KeyboardInterrupt:
    print ("Quit")
    GPIO.cleanup()
#!/usr/bin/python

import json

#import/set values

with open('values.json', 'r') as values:
	json_data = json.load(values)
	#Plug1 = json_data['plug1']

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(3,GPIO.OUT)


def trigger():
    GPIO.output(3,False)

#Update JSON file that the Plug 2 is now on

json_data['plug2'] = "On"

with open('values.json', 'w') as values:
		values.write(json.dumps(json_data))

try:
    trigger()
    print("Plug 2 is now on")

except KeyboardInterrupt:
    print ("Quit")
    GPIO.cleanup()

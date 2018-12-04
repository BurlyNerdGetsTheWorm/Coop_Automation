#!/usr/bin/python
import json

#import/set values

with open('values.json', 'r') as values:
	json_data = json.load(values)
	#Plug1 = json_data['plug1']

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)


def trigger():
    GPIO.output(22,True)

#Update JSON file that the Plug 6 is now off

json_data['plug6'] = "Off"

with open('values.json', 'w') as values:
		values.write(json.dumps(json_data))
try:
    trigger()

except KeyboardInterrupt:
    print ("Quit")
    GPIO.cleanup()

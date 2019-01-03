#This file is responsible for opening the door

#import/set values
from time import sleep
import RPi.GPIO as GPIO
import json

with open('values.json', 'r') as values:
    json_data = json.load(values)
    DoorStatus = json_data['doorstatus']
    AutomationEnabled = json_data['automationenabled']


if  (DoorStatus == 'Closed'):
	print("Door must open")
	#This will now do whatever is needed to move the stepper motor appropriately
	#Update JSON file that the door is now open
    DIR = 20   # Direction GPIO Pin
    STEP = 21  # Step GPIO Pin
    ACTIVE = 16 #GPIO pin that sends power to Rest/Sleep pins to enable the driver, instead of constantly setting Enable pin to high
    CW = 1     # Clockwise Rotation
    CCW = 0    # Counterclockwise Rotation
    PULSES = 75   #Amount of pulses to send, which controls steps (200 pulses would be one rotation for a 200 steps per rotation stepper motor)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.setup(ACTIVE, GPIO.OUT)
    GPIO.output(ACTIVE, 1)
    sleep(.5)
    GPIO.output(DIR, CCW)

    step_count = SPR
    delay = .0208

    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)


    GPIO.output(ACTIVE, 0)
    GPIO.cleanup

	json_data['doorstatus'] = "Open"

	with open('values.json', 'w') as values:
    		values.write(json.dumps(json_data))
else:
	print("The door is already open")

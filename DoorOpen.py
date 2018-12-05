#This file is responsible for opening the door

import json

#import/set values

with open('values.json', 'r') as values:
    json_data = json.load(values)
    DoorStatus = json_data['doorstatus']
    AutomationEnabled = json_data['automationenabled']


if  (DoorStatus == 'Closed') and (AutomationEnabled is True):
	print("Door must open")
	#This will now do whatever is needed to move the stepper motor appropriately 
	#Update JSON file that the door is now open
	json_data['doorstatus'] = "Open"

	with open('values.json', 'w') as values:
    		values.write(json.dumps(json_data))
else:
	print("The door is already open")
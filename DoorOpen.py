#This file is responsible for opening the door

import json

#import/set values

with open('values.json', 'r') as values:
    json_data = json.load(values)
    OpenState = json_data['open']
    Enabled = json_data['enabled']


if  (OpenState == 'Closed') and (Enabled is True):
	print("Door must open")
	#This will now do whatever is needed to move the stepper motor appropriately 
	#Update JSON file that the door is now open
	json_data['open'] = "Open"

	with open('values.json', 'w') as values:
    		values.write(json.dumps(json_data))
else:
	print("The door is already open")
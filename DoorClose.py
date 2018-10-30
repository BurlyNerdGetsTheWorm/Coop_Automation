#This file is responsible for opening the door

import json

#import/set values

with open('values.json', 'r') as values:
    json_data = json.load(values)
    OpenState = json_data['open']
    Enabled = json_data['enabled']


if  (OpenState == 'Open') and (Enabled is True):
	print("Door must close")
	#This will now do whatever is needed to move the stepper motor appropriately 
	#Update JSON file that the door is now closed
	json_data['open'] = "Closed"

	with open('values.json', 'w') as values:
    		#values.write(json.dumps(json_data))
else:
	print("The door is already closed")
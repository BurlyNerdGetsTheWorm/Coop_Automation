#This file is responsible for changing the automation value in the JSON file to on

import json

#import/set values

with open('values.json', 'r') as values:
    json_data = json.load(values)
    AutomationEnabled = json_data['automationenabled']


if  (AutomationEnabled is False):
	#Update JSON file to turn on automation
	json_data['automationenabled'] = True
	
	print("Automation is now on")

	with open('values.json', 'w') as values:
    		values.write(json.dumps(json_data))


else:
	print("Automation is already on")

#This script will be called by a CRON job. It is not called by the page or any other script. It does, however, execute other scripts.

import requests
import json

#import/set values

with open('values.json', 'r') as values:
    json_data = json.load(values)
    DoorStatus = json_data['doorstatus']
    AutomationEnabled = json_data['automationenabled']


print"Door is currently",DoorStatus
#print "Automation is set to",AutomationEnabled
#Display automation vs manual
if (AutomationEnabled is True):
	print("The door is currently in automatic mode with manual override.")
else:
	print("The door is currently set to manual mode only.")



#Set Sunrise and set times
response = requests.get("https://apps.tsa.dhs.gov/MyTSAWebService/GetEventInfo.ashx?eventtype=sunrise_sunset&airportcode=FNT&output=json")
SunRiseSetData = response.json()

SunriseTime = SunRiseSetData["Sunrise"]
SunsetTime = SunRiseSetData["Sunset"]

json_data['sunrisetime'] = SunriseTime
json_data['sunsettime'] = SunsetTime

#print sunrise sunset
print "Sunrise is",SunriseTime
print "Sunset is",SunsetTime

#Get Current time (no date)
from datetime import datetime
Currenthour = datetime.now().time().strftime("%I")
AMPM = datetime.now().time().strftime("%p")
int_Currenthour = int(Currenthour)

#print time values
print "Current time is",datetime.now().time()
print "Current hour is between",int_Currenthour,AMPM,"and",int_Currenthour+1,AMPM
print "Opening hour is between",int(SunriseTime[:2])+1,AMPM,"and",int(SunriseTime[:2])+2,AMPM
print "Closing hour is between",int(SunsetTime[:2])+1,AMPM,"and",int(SunsetTime[:2])+2,AMPM

#Is it after sunrise?
if ((int_Currenthour == (int(SunriseTime[:2])+1)) and (AMPM == "AM") and (AutomationEnabled is True)):
	print("Sunrise conditional is true")
	exec(open("DoorOpen.py").read())
else:
	print("It is not currently time to open and/or automation is currently disabled")

#Is it after Sunset?
if ((int_Currenthour == (int(SunsetTime[:2])+1)) and (AMPM == "PM") and (AutomationEnabled is True)):
	print("Sunset conditional is true")
	exec(open("DoorClose.py").read())
else:
	print("It is not currently time to close and/or automation is currently disabled")

#Write Sunrise and Sunset times to JSON
	with open('values.json', 'w') as values:
		values.write(json.dumps(json_data))

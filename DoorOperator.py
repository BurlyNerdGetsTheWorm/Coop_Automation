import requests
import json

#import/set values

with open('values.json', 'r') as values:
    json_data = json.load(values)
    OpenState = json_data['open']
    Enabled = json_data['enabled']
    

print"Door is currently",OpenState
print "Enabled is",Enabled

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
if ((int_Currenthour == (int(SunriseTime[:2])+1)) and (AMPM == "AM") and (Enabled is True)):
	print("Sunrise conditional is true")
	exec(open("DoorOpen.py").read())
else:
	print("It is not currently time to open")

#Is it after Sunset?
if ((int_Currenthour == (int(SunsetTime[:2])+1)) and (AMPM == "PM") and (Enabled is True)):
	print("Sunset conditional is true")
	exec(open("DoorClose.py").read())
else:
	print("It is not currently time to close")

#Write Sunrise and Sunset times to JSON
	with open('values.json', 'w') as values:
		values.write(json.dumps(json_data))
import requests
import json

#import/set values

with open('values.json', 'r') as values:
    json_data = json.load(values)
    OpenState = json_data['open']
    Enabled = json_data['enabled']

print(OpenState)

#Set Sunrise and set times

response = requests.get("https://apps.tsa.dhs.gov/MyTSAWebService/GetEventInfo.ashx?eventtype=sunrise_sunset&airportcode=FNT&output=json")
SunRiseSetData = response.json()

SunriseTime = SunRiseSetData["Sunrise"]
SunsetTime = SunRiseSetData["Sunset"]

print(SunriseTime)
print(SunsetTime)

#Get Current time (no date)
from datetime import datetime
Currenthour = datetime.now().time().strftime("%I")
AMPM = datetime.now().time().strftime("%p")
int_Currenthour = int(Currenthour)

#print the current time
print(datetime.now().time())

print(int_Currenthour)
print(AMPM)
print(Enabled)
print(int(SunriseTime[:2]))
print(int(SunsetTime[:2])+1)

#Is it after sunrise?
if ((int_Currenthour == (int(SunriseTime[:2])+1)) and (AMPM == "AM") and (Enabled is True)):
	print("Sunrise conditional is true")
	exec(open("DoorOpen.py").read())
else:
	print("It is not currently sunrise")




#Is it after Sunset?
if ((int_Currenthour == (int(SunsetTime[:2])+1)) and (AMPM == "PM") and (Enabled is True)):
	print("Sunset conditional is true")
	exec(open("DoorClose.py").read())
else:
	print("It is not currently sunset")
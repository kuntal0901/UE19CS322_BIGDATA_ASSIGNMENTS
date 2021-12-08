#!/usr/bin/env python3
import json
import datetime as dt
import sys
desc="lane blocked|shoulder blocked|overturned".split("|")
weather=["heavy snow", "thunderstorm", "heavy rain", "heavy rain showers","blowing dust"]
for line in sys.stdin:
    l1=(json.loads(line))
    temp=-1
    if(("lane blocked" in str(l1["Description"]).lower() or "shoulder blocked" in str(l1["Description"]).lower() or "overturned" in str(l1["Description"]).lower())and l1["Severity"]>=2 and str(l1["Sunrise_Sunset"]).lower()=="night" and str(l1["Weather_Condition"]).lower() in weather and l1["Visibility(mi)"]<=10 and l1["Precipitation(in)"] >= 0.2):
	    try:
		    temp=l1["Start_Time"][11:13]
		    print(temp)
	    except ValueError:
		    pass
	    
	    	



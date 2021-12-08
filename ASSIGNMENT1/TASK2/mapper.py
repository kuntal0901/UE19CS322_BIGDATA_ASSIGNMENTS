#!/usr/bin/env python3
import json
import datetime as dt
import sys
import requests
lat_input=float(sys.argv[1])
long_input=float(sys.argv[2])
dis=float(sys.argv[3])
for line in sys.stdin:
    l1=(json.loads(line))
    u=" http://20.185.44.219:5000/"
    try:
        
        distance=((l1["Start_Lat"]-lat_input)**2+(l1["Start_Lng"]-long_input)**2)**(0.5)
        if(distance<dis):
            #print("in")
            Start_Lat1=l1["Start_Lat"]
            Start_Lng1=l1["Start_Lng"]
            data={
             "latitude": Start_Lat1,
             "longitude": Start_Lng1
            }
            r=requests.post(url=u,json=data)            
            res=r.json()
            print(res["state"],res["city"],sep=" ")
    except ValueError:
        pass
    

   
	    	



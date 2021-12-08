#!/usr/bin/env python3

import sys
		
		
link_points={}
for line in sys.stdin:
	line=line.strip().split("?")
	page=int(line[0])
	line[1]=eval(line[1])
	if page not in link_points:
	    link_points[page]=0.15
	for i in line[1]:
		if i not in link_points:
		    link_points[i]=0.15
		link_points[i]+=line[1][i]*0.85
for key in sorted(link_points.keys(),key=lambda x:str(x)):
    print(key,round(link_points.pop(key),2),sep=',')


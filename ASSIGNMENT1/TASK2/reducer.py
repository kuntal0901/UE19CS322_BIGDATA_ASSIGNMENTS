#!/usr/bin/env python3
import sys
temp_dict={}
macity=0
mastate=0
def fix(a):
    z_length=macity-len(a)
    a+=" "+"z"*(z_length-1)
    return a
def fix1(a):
    z_length=mastate-len(a)
    a+=" "+"z"*(z_length-1)
    return a
for line in sys.stdin:
    line = line.strip()
    s1=line.split(' ')
    state=s1[0]
    if(len(state)>mastate):
        mastate=len(state)
    city =' '.join(s1[1:])
    if(len(city)>macity):
        macity=len(city)    
    if state not in temp_dict:
        temp_dict[state]={}
        temp_dict[state][city]=1
    else:
        if city not in temp_dict[state]:
                temp_dict[state][city]=1
        else:
	        temp_dict[state][city]+=1
for a in sorted(temp_dict.keys(),key=fix1):
    print(a,end="\n")
    counter=0
    b=temp_dict[a]    
    for i in sorted(b.keys(),key=fix):
        counter+=b[i]
        print(i,b[i],sep=" ")
    print(a,counter,sep=" ")

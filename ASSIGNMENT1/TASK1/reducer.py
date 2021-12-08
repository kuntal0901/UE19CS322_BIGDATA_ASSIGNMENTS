#!/usr/bin/env python3
#from operator import itemgetter
import sys
lists=[0]*24
for line in sys.stdin:
	lists[int(line)]+=1
for i in range(24):
	if(lists[i]!=0):
		sys.stdout.write(str(i)+' '+str(lists[i]))
		sys.stdout.write('\n')


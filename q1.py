#!/usr/bin/python
import calendar
count=0
for y in range(2015,2017):
	for x in range(1,13):
		c=calendar.weekday(y,x,01)
		if c==0:
			count=count+1

print "No of Monday on First day of Month in 2015 & 2016 :" ,count
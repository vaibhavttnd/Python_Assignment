#!/bin/sh
import datetime

d=input("input date in dd format: ")
m=input("input date in mm format: ")
y=input("input date in yyyy format: ")

d1=input("input date in dd format: ")
m1=input("input date in mm format: ")
y1=input("input date in yyyy format: ")

date1=datetime.date(y,m,d)
date2=datetime.date(y1,m1,d1)

difference=date1-date2

print difference
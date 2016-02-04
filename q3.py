#!/usr/bin/python
import re

value = "voorheesvilleAASDDW"

m = re.search(r'([a-z].*)', value)
n = re.search("([A-Z].*)", value)
if m and n:
    print "Password valid"
else:
	print "Both [a-z] and [A-Z] should be present"


print "condition one over"

value = "0258938589"
m = re.search(r'([0-9].*)', value)
if m and n:
    print "Password valid"
else:
	print "[0-9] should be present"

print "condition two over"

value = "0258$22#89789@"
m = re.search(r'([$#@].*)', value)
if m:
    print "Password valid"
else:
	print "[$#@] atleast one should be present"

print "condition three over"

value = "0258$22#89789@"
if len(value)>=6:
    print "Password valid"
else:
	print "Length should be greater than equal to 6"

print "condition four over"

value = "0258$22#89789@"
if len(value)<=16:
    print "Password valid"
else:
	print "Length should be less than equal to 16"

print "condition five over"
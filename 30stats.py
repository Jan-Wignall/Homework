#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math


num = []
for number in sys.argv[1:]:
	float(number)
	num.append(number)
	
#for i in range (1, len(sys.argv)):
#	probs.append(float(sys.argv[i]))
#	sum += float(sys.argv[i])
	

#Count
numcount = len(num)

#Min
minval= num[0]
for ding in num:
	if (minval is 0 or ding < minval):
		minval= ding


#Max

maxval= num[0]
for voorwerp in num:
	if (maxval is 0 or voorwerp > maxval):
		maxval= voorwerp

	

#MEAN
n = len(num)
totsum=0
for i in num:
	x = int(i)
	totsum += x
mean = totsum / numcount

#Std. Dev
othersum = 0
for i in num:
	othersum += (int(i)-mean)**2
stdev = math.sqrt(othersum/(n-1))


#Median
num.sort()
for dev in num: 
	if n % 2 == 0:
		medA= int(num[n//2])
		medB= int(num[n//2-1])
		median = int((medA + medB)//2)
	else:
		median = int(num[n//2])
print('count:', numcount, 'Minimum:', minval, 'Maximum:', maxval, 'Mean:', mean, 'Std. Dev:', stdev, 'Median:', median)
#Collab with Josh
"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""

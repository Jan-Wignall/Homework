#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git.push them a random birthday
#	push it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

#calendar=[]
#for i in range(365): calendar.append(0)
days = 365
people = 22
trials = 5000
share = 0
for i in range(trials):
	calendar = [0] * days 
	for j in range(people):
		birthday = random.randint(0, days -1)
		calendar[birthday] += 1
	#print(calendar)
	for value in calendar:
		if value > 1:
			share += 1
			break
	

print(share/trials)

#Collab in Office Hours 
"""
python3 33birthday.py
0.571
"""


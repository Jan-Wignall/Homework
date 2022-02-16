#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

genomelen = int(sys.argv[1])
read = int(sys.argv[2])
readlen = int(sys.argv[3])

#make genome
genome = [0]* genomelen
for i in range(read):
	rand = random.randint(0,genomelen - read)
	for j in range(read):
		genome[j+rand]+=1
min = genome[read]
max = genome[read]

Cov = 0 #coverage

for a in genome[read:-read]:
	if a < min: min = a
	if a > max: max = a
	Cov += a

#print(min, max, f'{Cov/(genomelen - 2*read):.5f}')
print(min, max, '{:.2f}'.format(Cov/(genomelen-2*read)))


#collab with Jojo and class in general
"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""

#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

dna = ''
at = 0
n = 0
for i in range(30):
	r = random.random()
	if r > 0.6:
		if r > 0.8:
			dna = dna + 'G'
		else:
			dna = dna + 'C'
	else:
		if r > 0.3: #0.3 is half of 0.6 so half the time it will print an A. Half time it will print T.
			dna = dna + 'A'
			at += 1
		else:
			dna = dna + 'T'
			at += 1
print(len(dna))
fracgc = at/len(dna)
print('%.2f' % fracgc)
print(dna)

#worked with Joshua and Yaniel
#need variable for DNA
# every time the loop occurs need to add an AT or GC.

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence


"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""

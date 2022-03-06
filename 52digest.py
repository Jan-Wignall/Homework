#!/usr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments

filename = sys.argv[1]
cutsite = sys.argv[2] 
def readfile(filename):
	with open(filename) as fp:
		sequence = ''
		flag_origin = False
		for line in fp.readlines():
			if 'ORIGIN' in line:
				flag_origin = True
				continue
			elif flag_origin:
				words = line.split()
				for word in words[1:]:
					sequence += word
	return sequence


def digest(sequence, cutsite): 
	fragments = [0] 
	for match in re.finditer(cutsite, sequence): #finds the cutsites in sequence
		fragments.append(match.start()) #creates fragments from the cuts
	fragments.append(len(sequence)) 
	return fragments


sequence = readfile(filename)
fragments = digest(sequence, cutsite)
for i in range(len(fragments)-1):
	lengths = fragments[i + 1] - fragments[i]
	print(lengths)


#collab with Jojo. 
"""def readfasta(filename):
	records = []
	seq = ''	
	with open(filename) as fp:
		for line in fp.readlines():
			line = line.rstrip()
			if len(line) == 0: continue
			if line[0] == '>':
				if seq != '':
					records.append((id,seq))
				words = line.split()
				id = words[0][1:]
				seq = ''
			else:
				seq += line.upper()
		records.append((id,seq))
	return records
"""


"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""

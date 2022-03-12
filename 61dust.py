#!/usr/bin/env python3
# 61dust.py

import argparse
import math
# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

import mcb185 as mcb

parser = argparse.ArgumentParser(description='Open file, returns masked low entropy file.')
parser.add_argument('--file', type=str, metavar='<file>', required = True, help = 'required file argument')
parser.add_argument('--window', type = int, metavar = '<int>', required= True, help = 'required int argument')
parser.add_argument('--entropythreshold', type=float, metavar='<float>', required=True, help= 'required int argument entropy thresh')
parser.add_argument('--masking', type=str, metavar='<str>', required=True, help='enter masking preferences')

args= parser.parse_args()



for entry in mcb.read_fasta(args.file):
	name = entry[0]
	sequence = entry[1].upper()
window = args.window
entropythreshold= args.entropythreshold
masking= args.masking

new_sequence= ''

for i in range(0, len(sequence),window):
	entropy = mcb.entropy_calc(seq[i:i+window], window)
	if entropy >= entropythreshold:
		new_sequence += sequence[i:i+window].upper()
	else:
		if masking.upper() == 'N':
				new_sequence += 'N'*window
		else:
				new_sequence += sequence[i:i+window].lower()	

with open('newfasta.fa', 'w') as fp:
	fp.write(name)
	fp.write('\n')
	for i in range(0,len(new_sequence), 50):
		fp.write(new_sequence[i:i+50])
		fp.write('\n')				
#collaboration with Josh
	
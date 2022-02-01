#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change
gc = 0
for i in range(len(dna)):
	if   dna[i] == 'G': gc += 1
	elif dna[i] == 'C': gc += 1
fracgc = gc/len(dna)
print('%.2f' % fracgc)
print('{:.2f}'.format(fracgc))
print(f'{fracgc:.2f}')

"""
python3 21gc.py
0.42
0.42
0.42
"""

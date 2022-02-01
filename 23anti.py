#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
Revdna=dna[::-1]
for i in Revdna:
	if i == 'A': print('T',end='')
	elif (i=='T'): print('A',end='')
	elif (i =='C'): print('G',end='')
	elif (i =='G'): print('C',end='')


"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""

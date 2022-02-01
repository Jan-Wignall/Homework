#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna='ATGGCCTTT'
for i in range(len(dna)):
  print(i, end=" ")
  print(i % 3, end = " ")
  print(dna[i])

dna='ATGGCCTTT'
for i in range(0,len(dna) -2, 3):
	for j in range(3):
		print(i+j, k, dna[i+j])

 			

"""
#Ignore all this garbage lmao
for i in range(len(dna)):
#	print(dna[i:i+3])     #kmers
#print(pos, codon, dna)
for frame in range(3):
	print(f'reading frame {frame+1}')
	for position in range(frame, len(dna) -2, 3):
		codon = dna[position:position+3]
		print(codon)
	print()

python3 24frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""

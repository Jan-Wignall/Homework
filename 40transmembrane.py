#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix

#read the files
filename = sys.argv[1]
def readfasta(filename):
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
				seq += line
		records.append((id,seq))
	return records
			
#KD equation
def KDfxn(peptide): #calculate hydrophobicity of aa
	kdscore = 0
	for aa in peptide:
			if aa == "I": kdscore += 4.5
			elif aa == "V": kdscore += 4.2
			elif aa == "L": kdscore += 3.8
			elif aa == "F": kdscore += 2.8
			elif aa == "C": kdscore += 2.5
			elif aa == "M": kdscore += 1.9
			elif aa == "A": kdscore += 1.8
			elif aa == "G": kdscore -= 0.4
			elif aa == "T": kdscore -= 0.7
			elif aa == "S": kdscore -= 0.8
			elif aa == "W": kdscore -= 0.9
			elif aa == "Y": kdscore -= 1.3
			elif aa == "P": kdscore -= 1.6
			elif aa == "H": kdscore -= 3.2
			elif aa == "E": kdscore -= 3.5
			elif aa == "Q": kdscore -= 3.5
			elif aa == "D": kdscore -= 3.5
			elif aa == "N": kdscore -= 3.5
			elif aa == "K": kdscore -= 3.9
			elif aa == "R": kdscore -= 4.5
			"""
			else: 
				print("NOT AMINO ACID")
				sys.exit()
			"""
	return kdscore/len(peptide) #prints out average Hphobicity
	
#print(KDfxn(RASGDHTGR)
#function for amphipathic alpha-helix.

def fattyhelix(sequence, length, threshold):
	for i in range(len(sequence)-length +1): #length = window length
		pep = sequence[i:i+length] #length of the smoll peptide
		if 'P'  in pep: continue #stop with the Prolines
		if KDfxn(pep) > threshold: #no threshold
			#print(pep, KDfxn(pep))
			return True
	return False		
	
for id, seq in readfasta(filename): #reads through the protein sequences
	if fattyhelix(seq[0:30],8,2.5) and fattyhelix(seq[30:], 11, 2.0): 
		# if there are two helices, print id ^^. First one is signal peptide
		print(id) #this prints the ID of the protein.
print(sys.argv)
#Signal peptide: large stretch of hydrophobic amino acids immediately
#large hydrophobic regions (TM bit)
#no prolines in Hphobic regions.


#Collaboration in office hours
"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""

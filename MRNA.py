'''
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. 
'''

def infer(protein):
	table = {}
	num = 0
	result = 3       # 3 possible mRNAs will translated into stop codon.
	
	# create a table from CodonTable.txt
	table = {}
	with open("CodonTable.txt") as t:                             
		for line in t.read().split(" "):
			if line[0:3].isalpha():
				table[line[0:3]] = line[3:]	
			else:
				table[line[1:4]] = line[4:]

	for s in protein:
		for v in table.values():
			if v == s:
				num += 1
		result *= (num % 1000000)
		num = 0

	return result % 1000000



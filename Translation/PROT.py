'''
Given: An RNA string ss corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by ss.
'''

def Translate(codons):
	codons = [codons[i:i + 3] for i in range(0, len(codons), 3)]     #separate each codon
	table = {}
	protein = ""

	with open("CodonTable.txt") as t:                             #create a table from CodonTable.txt
		for line in t.read().split(" "):
			if line[0:3].isalpha():
				table[line[0:3]] = line[3:]	
			else:
				table[line[1:4]] = line[4:]

	for codon in codons:
		if table[codon] == "Stop" :
			break
		else:
			protein = protein + table[codon]

	return protein	

with open("protein.txt", "w") as p:
	i = open(input("data input: ")) 
	p.write(Translate(i.read()))
	i.close()

'''
Given: A DNA string s in FASTA format.

Return: The 4-mer composition array of s, lexicographically.
'''
from DataProcess import ReadFASTA
from itertools import product

def four_mer(dna):
	dna = ReadFASTA(dna)
	composition = {}
	new_dna = ""

	# convert dna list into string
	for s in dna:
		new_dna += s

	# construct 4-mer composition array
	for x in product("ATCG", repeat = 4):
		temp = ""
		for i in range(0, len(x)):
			temp += x[i]
		composition.update({temp: 0})
		temp = "" 

	# count the number of 4-mer in dna string
	for x in range(0, len(new_dna) - 3):
		if new_dna[x:x + 4] in composition:
			composition[new_dna[x:x + 4]] += 1
		
	return [value for (key, value) in sorted(composition.items())]

if __name__ == '__main__':
	with open(input("file input: ")) as f:
		result = list(map(str, four_mer(f)))
		with open("output_kmer.txt", "w") as o:
			o.write(" ".join(result))

'''
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string 
having length between 4 and 12.

A DNA string is a reverse palindrome if it is equal to its reverse complement.
'''

from DataProcess import ReadFASTA, compliment_DNAbase, reverse_base

def palindrome(dna):
	result = []
	new_dna = ""

	# convert dna from list into string
	for s in dna:
		new_dna += s

	for l in range(4, 13):
		for start_index in range(0, len(new_dna) - l + 1):
			pal = new_dna[start_index:start_index + l]		
			if compliment_DNAbase(reverse_base(pal)) == pal:
				result.append("")
				result[len(result) - 1] += str(start_index + 1) + " " + str(l) 

	return result

if __name__ == '__main__':
	with open(input("file input: ")) as f:
		p = palindrome(ReadFASTA(f))
		with open("output_revp.txt", "w") as o:
			for line in p:
				o.write(line)
				o.write("\n")

'''
Given: A DNA string ss of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of ss. 
'''
from PROT import Build_Table
import sys
sys.path.append("D:/GitHub/My_Rosalind_solution/")
from DataProcess import ReadFASTA, compliment_DNAbase, reverse_base
from RNA import transcribe
'''
Extract substrings which begins with start codon and ends with stop codon
and translate each substring into amino acids.
''' 
def open_reading(DNA):
	RNA = transcribe(DNA) 
	Codon_table = Build_Table()
	protein = []
	pro_num = 0

	# index the beginning of each substring 
	for start_index in range(len(RNA)):
		
		# Start translation only if it begins with start codon "AUG"
		if RNA[start_index:start_index + 3] == "AUG":            
			codons = [RNA[i:i + 3] for i in range(start_index, len(RNA), 3)]

			for codon in codons:
				if len(codon) == 3:  # omit the uncomplete codons
					if Codon_table[codon] == "Stop" :
						break
					else:
						protein.append("")
						protein[pro_num] += Codon_table[codon]
			pro_num += 1
	protein = [i for i in protein if i != ""]
	return protein

if __name__ == '__main__':
	with open(input("file input: ")) as f:
		normal = ReadFASTA(f)
		cr = reverse_base(compliment_DNAbase(normal[0]))
		protein = set(open_reading(normal[0]) + open_reading(cr))
		with(open("output_orf.txt", "w")) as o:
			for pro in protein:
				o.write(str(pro) + "\n")

		
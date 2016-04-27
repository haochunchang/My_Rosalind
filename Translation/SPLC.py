'''
Given: A DNA string ss and a collection of substrings of ss acting as introns. 
       All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of ss. 
'''
from PROT import Translate
import sys
sys.path.append("D:/GitHub/My_Rosalind_solution/")
from DataProcess import ReadFASTA
from RNA import transcribe

# splice the fisrt element of the list according to the remaining elements.
def Splice(DNA):
	dna = ReadFASTA(DNA)
	exons = str(dna[0])
	introns = dna[1:]

	# splice the exons
	for intron in introns:
		index = exons.find(intron)
		exons = exons[0:index] + exons[index + len(intron):]

	rna = transcribe(exons)
	protein = Translate(rna)

	return protein

if __name__ == '__main__':
	with open(input("file input: ")) as f:
		with open("output_splc.txt", "w") as o:
			o.write(Splice(f))
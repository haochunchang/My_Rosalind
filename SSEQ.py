'''
Given: Two DNA strings s and t in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. 
If multiple solutions exist, it may return any one.
'''

from DataProcess import ReadFASTA

def find_spliced_motif(s, t):
	location = [0]
	for x in range(0, len(t)):
		location.append(s.find(t[x], location[x]) + 1)
	
	location = [i for i in location if i > 0]
	return location

if __name__ == '__main__':
	with open(input("file input: ")) as f:
		dna = ReadFASTA(f)
		location = find_spliced_motif(dna[0], dna[1])
		with open("output_sseq.txt", "w") as o:
			for l in location:
				o.write(str(l))
				o.write(" ")
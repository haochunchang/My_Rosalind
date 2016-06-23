'''
Given: A collection of DNA strings in FASTA format.

Return: The adjacency list corresponding to O3.

Ok : string s is connected to string t with a directed edge when 
there is a length k suffix of s that matches a length k prefix of t,
as long as s≠t
'''
from DataProcess import ReadFASTA_dic

def overlap(data):
	dna = ReadFASTA_dic(data)
	prefix = {}
	suffix = {} 
	adj_lst = []

	for key, value in dna.items():
		prefix[key] = value[:3]
		suffix[key] = value[-3:]

	for s_key, s_value in suffix.items():
		for p_key, p_value in prefix.items():
			if s_value == p_value and s_key != p_key:	
				adj_lst.append(s_key + " " + p_key)

	return adj_lst

if __name__ == '__main__':
	with open(input("file input: ")) as f:
		result = overlap(f)
		with open("output_grph.txt", "w") as o:
			for l in result:
				o.write(l)
				o.write("\n")

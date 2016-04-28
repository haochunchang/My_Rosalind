'''
Given: A DNA string s of length at most 100 bp and an array A containing 
		at most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] represents the common logarithm 
		of the probability that a random string constructed with the GC-content 
		found in A[k] will match ss exactly.
'''
from math import log10

# Calculate the probability of constructing exactly as dna given a GC content.
def cal_prob(dna, GC):
	GC = float(GC)
	prob = {"A": (1 - GC) / 2, 
			"T": (1 - GC) / 2, 
			"C": GC / 2,
			"G": GC / 2}
	result = 1

	for base in dna:
		result *= prob[base]

	return log10(result)

if __name__ == '__main__':
	with open(input("file input: ")) as f:
		f = f.readlines()
		with open("output_prob.txt", "w") as o:
			for GC in f[1].split(" "):
				o.write(str(cal_prob(f[0].rstrip(), GC)))
				o.write(" ")
					
					

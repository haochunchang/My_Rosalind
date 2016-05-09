'''
Given: A collection of at most 10 symbols defining an ordered alphabet, 
and a positive integer n .

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically.
'''
from itertools import product

def lexi_kmers(symbol, n):
	lexi = list(product(symbol, repeat = n))
	new_lexi = []

	for x in lexi:
		temp = ""
		for i in range(0, n):
			temp += x[i]
		new_lexi.append(temp)
		temp = ""

	return new_lexi

if __name__ == '__main__':
	with open(input("file input: ")) as f:
		symbol = "".join(f.readline().split())
		n = int(f.readline())
		lexi = lexi_kmers(symbol, n)
		with open("output_lexf.txt", "w") as o:
			for l in lexi:
				o.write(l + "\n")

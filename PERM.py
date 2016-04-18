'''
Given: A positive integer n.

Return: The total number of permutations of length nn, 
followed by a list of all such permutations (in any order).
'''

from itertools import permutations
from math import factorial

#generate a list of all permutations of length n
def perm_list(n):
	perm_list = list(permutations(range(1, n + 1)))
	new_perm = []
	for perm in perm_list:
		new_perm.append(" ".join(map(str, perm)))	
	return new_perm

if __name__ == '__main__':
	with open(input("file input: ")) as f:
		perm_list = perm_list(int(f.read()))
		with open("output/output_perm.txt", "w") as o:
			o.write(str(len(perm_list)) + "\n")
			for perm in perm_list:
				o.write(perm)
				o.write("\n")
'''
Given: A positive integer n≤6.

Return: The total number of signed permutations of length n, 
followed by a list of all such permutations.
'''
from itertools import permutations
import sys

def sign_perm(n):
	perm = []
	new_perm = []

	for x in range(1, n + 1):
		perm.append(x)
		perm.append(-x)
	perm = list(permutations(perm, n))
	
	for l in perm:
		abs_l = list(map(abs, l))
		if len(set(abs_l)) == len(abs_l):
			new_perm.append(l)

	return new_perm

if __name__ == '__main__':
	if int(sys.argv[1]) > 0:
		lst = sign_perm(int(sys.argv[1]))
	else:
		print("please add a positive integer as argument")
	with open("output_sign.txt", "w") as o:
		o.write(str(len(lst)) + "\n")
		for l in lst:
			for x in range(0, len(l)):
				o.write(str(l[x]) + " ")
			o.write("\n")
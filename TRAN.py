'''
Given: Two DNA strings s1 and s2 of equal length in FASTA format.

Return: The transition/transversion ratio R(s1,s2).
'''

from DataProcess import ReadFASTA, validate_base

def tt_ratio(s1, s2):
	if validate_base(s1) == False or validate_base(s2) == False:
		return "Input Error!"

	transition = 0
	transversion = 0

	for x in range(0, len(s1)):
		if s1[x] == s2[x]:
			continue

		s_list = set([s1[x], s2[x]])
		if s_list <= set("AG") or s_list <= set("CT"):
			transition += 1
		elif s_list <= set("ACT") or s_list <= set("GCT"):
			transversion += 1

	return transition / transversion

if __name__ == '__main__':
	with open(input("file input: ")) as f:
		dna = ReadFASTA(f)
		print("The transition/transversion ratio of these two DNA is: " + str(tt_ratio(dna[0], dna[1])))
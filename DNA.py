'''
Given: A DNA string ss of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in ss
'''

def count_DNA(s):
	Nu = {"A" : 0,
	      "C" : 0,
	      "G" : 0,
	      "T" : 0}
	x = "ACGT"
	i = 0
	copy_s = s
	while i < 4:	
		while copy_s.find(x[i]) != -1:
			Nu[x[i]] += 1
			copy_s = copy_s[copy_s.find(x[i]) + 1:]
		copy_s = s
		i += 1
	return Nu["A"], Nu["C"], Nu["G"], Nu["T"]

	

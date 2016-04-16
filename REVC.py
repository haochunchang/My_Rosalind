'''
Given: A DNA string ss of length at most 1000 bp.

Return: The reverse complement scsc of ss.
'''

def validate_base(base, RNAflag = False):
	RNAbase = set("AUCG")
	DNAbase = set("ATCG")
	return base <= RNAbase if RNAflag else DNAbase

def compliment(base):
	RNA = "AUCG"
	DNA = "ATCG"
	new_base = ""
	if validate_base(base):
		for b in base:
			if b == "A":
				new_base += "T"
			elif b == "T":
				new_base += "A"
			elif b == "C":
				new_base += "G"
			elif b == "G":
				new_base += "C"
	base = new_base
	return base

def reverse(base):
	new_base = ""
	for i in base[::-1]:
		new_base += i
	base = new_base
	return base

firstbase = "AAAACCCGGT"
print(reverse(compliment(firstbase)))

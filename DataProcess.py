'''
	It is a library of methods of data processing

Table of contents:
1. ReadFASTA
2. validate_base
3. complement_DNAbase
4. reverse_base
5. ReadFASTA_dic
'''
# 1.process FASTA into a list of seq.
def ReadFASTA(file):
	case = -1
	seq = []
	for line in file:
		if line[0] == ">":
			case += 1
		else:
			seq.append("")
			seq[case] += line.rstrip()
	seq = [i for i in seq if i != ""]
	return seq

# 2. check if the bases belongs to DNA or RNA nucleotides.
def validate_base(base, rnaflag = False):
	validate = "ACGTacgt"
	if rnaflag == True:
		validate = validate.replace("T", "U")
		validate = validate.replace("t", "u") 

	if len(set(base) - set(validate)) != 0:
		return False
	else:
		return True

# 3. complement the DNA nucleotide base
def complement_DNAbase(base):
	new_base = ""
	if validate_base(base.upper()):
		for b in base:
			if b == "A":
				new_base += "T"
			elif b == "T":
				new_base += "A"
			elif b == "C":
				new_base += "G"
			elif b == "G":
				new_base += "C"
	return new_base

# 4. reverse the nucleotide base
def reverse_base(base):
	new_base = ""
	for i in base[::-1]:
		new_base += i
	return new_base

# 5. convert FASTA file into dictionary with seq as value
def ReadFASTA_dic(file):
	dic = {}
	fasta_key = ""
	fasta_seq = ""
	for line in file:
		if line[0] == ">":
			if fasta_key != None and fasta_seq != None:
				dic[fasta_key] = fasta_seq
			fasta_key = line[1:].replace("\n", "")
			fasta_seq = ""
		else:
			fasta_seq += line.replace("\n", "")
	del dic[""]
	return dic



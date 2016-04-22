'''
	It is a library of methods of data processing

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




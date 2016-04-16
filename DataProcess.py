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
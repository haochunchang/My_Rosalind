
def Compute_GC(seq):   
	if len(seq) > 0:                  
		return (seq.count("G") + seq.count("C")) / (seq.count("G") + seq.count("C") + \
			    seq.count("T") + seq.count("A"))
	else:
		return None

def Compare(data):                              #return seq which has the largest GC%
	percent = [0]
	name = []
	for x in data:
		if isinstance(x, float):
			percent.append(x)
		else:
			name.append(x)
	Max_pos = percent.index(max(percent)) - 1
	return name[Max_pos][1:-1] + "\n" + str(max(percent) * 100)

def Process():
	f = open(input("file input: "), "r")
	result = []
	lst = ""                               
	for line in f:                              #process each line
		if line[0] != ">":                      
			lst = lst + line
		else:
			result.append(Compute_GC(lst))
			lst = ""
			result.append(line)
	result.append(Compute_GC(lst))
	result = result[1:]                         #delete the initial "none"
	f.close()
	return Compare(result)                      #result = a list of ['Rosalind_xxxx', 'GC%']

output = open("output.txt", "w")
output.write(Process())
output.close()

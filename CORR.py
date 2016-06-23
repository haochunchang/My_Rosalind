'''
Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. 
       Some of these reads were generated with a single-nucleotide error. 

For each read s in the dataset, one of the following applies:
1. s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
2. s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to 
   exactly one correct read in the dataset (or its reverse complement).

Return: A list of all corrections in the form "[old read]->[new read]". 
       (Each correction must be a single symbol substitution, and you may return the corrections in any order.)
'''

from DataProcess import reverse_base as r
from DataProcess import complement_DNAbase as c
from DataProcess import ReadFASTA_dic

# compute Hamming distance for each s and t
def Hamming(s, t):
	d = 0
	for x in range(len(s)):
		if s[x] != t[x]: 
			d += 1
	return d

# return a list of each element contains "old_read" + "->" + "new_read"
def correction(reads):
    correction = []
    correct_read = []    
    value = list(reads.values())    

    # record correct and wrong read in reads list
    correct_read = [seq for seq in value if value.count(seq) + value.count(r(c(seq))) >= 2] 
    wrong_read = [seq for seq in value if seq not in correct_read]    
       
    # for each incorrect read, search other read and their reverse complement which Hamming distance is exactly 1.
    for seq in wrong_read:
        for x in range(len(correct_read)):
            if Hamming(seq, correct_read[x]) == 1:
                correction.append(seq + "->" + correct_read[x])
            elif Hamming(seq, r(c(correct_read[x]))) == 1:
                correction.append(seq + "->" + r(c(correct_read[x])))     

    return set(correction)

if __name__ == "__main__":
    with open("data/rosalind_corr.txt", "r") as f:
        reads = ReadFASTA_dic(f)
        correct = "\n".join(map(str, correction(reads)))
        with open("data/output_corr.txt", "w") as o:
            o.write(correct)
            print(correct)

'''
Given: At most 50 DNA strings whose length does not exceed 1 kbp in FASTA format
 (which represent reads deriving from the same strand of a single linear chromosome).

Return: A shortest superstring containing all the given strings(thus corresponding to a reconstructed chromosome)
'''
'''
sample output: ATTAGACCTGCCGGAATAC
'''
from DataProcess import ReadFASTA

def suffixPrefixMatch(x, y, k = 3):
    ''' Return length of longest suffix of x of length at least k that
        matches a prefix of y.  Return 0 if there no suffix/prefix
        match has length at least k. '''
    if len(x) < k or len(y) < k:
        return 0
    idx = len(y) # start at the right end of y
    # Search right-to-left in y for length-k suffix of x
    while True:
        hit = y.rfind(x[-k:], 0, idx)
        if hit == -1: # not found
            return 0
        ln = hit + k
        # See if match can be extended to include entire prefix of y
        if x[-ln:] == y[:ln]:
            return ln # return length of prefix
        idx = hit + k - 1 # keep searching to left in Y

def max_overlap(dna_list):
    max_len = 0
    max_index = []
    for prefix_index in range(len(dna_list)):
        for suffix_index in [i for i in range(len(dna_list)) if i != prefix_index]:
            prefix, suffix = dna_list[prefix_index], dna_list[suffix_index]
            match = suffixPrefixMatch(prefix, suffix)
            if match > max_len:
                max_len = match
                max_index = [prefix_index, suffix_index]                
        
    return [dna_list[j] for j in range(len(dna_list)) if j not in max_index] + [dna_list[max_index[0]] + dna_list[max_index[1]][max_len:]]

def shortest_superstring(dna_list):
    while len(dna_list) > 1:
        dna_list = max_overlap(dna_list)
    return dna_list[0]

if __name__ == "__main__":
    with open("data/rosalind_long.txt", "r") as f:
        dna_list = ReadFASTA(f)
        chrom = shortest_superstring(dna_list)
        with open("data/output_long.txt", "w") as o:
            print(chrom)
            o.write(chrom) 

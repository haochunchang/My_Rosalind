'''
Given: A DNA string s (of length at most 100 kbp) in FASTA format.

Return: The failure array of s.

The failure array of s is an array P of length n for which P[k] is the length of the longest substring s[j:k] 
that is equal to some prefix s[1:k−j+1], where j cannot equal 1 (otherwise, P[k] would always equal k). 
By convention, P[1]=0.
'''

# example input: CAGCATGGTATCACAGCAGAG

from DataProcess import ReadFASTA

def farray(seq):
    P = [0 for x in range(len(seq))] 
    j = 0
    for k in range(2, len(seq)):
        # if next bases of substring and prefix is not identical, j goes back to the previous longest substring length.
        while j > 0 and seq[j] != seq[k - 1]:
            j = P[j - 1]
        # if next bases of substring and prefix is identical, increase length by 1.
        if seq[j] == seq[k - 1]:
            j += 1
        # add length result to failure array
        P[k - 1] = j
    
    return P

if __name__ == "__main__":
    with open("data/rosalind_kmp.txt", "r") as f:
        seq = str(ReadFASTA(f))[2:-2] 
        result = farray(seq)
        with open("data/output_kmp.txt", "w") as o:
            o.write(" ".join(map(str, result)))
            print(" ".join(map(str, result)))

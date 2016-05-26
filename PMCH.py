'''
Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' 
and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.
'''

from DataProcess import ReadFASTA
from math import factorial

def perfect_match(rna):
    au = 0
    cg = 0
    # count "A, U" and "C, G" occurence
    for base in rna:
        if base == "A":
            au += 1
        elif base == "C":
            cg += 1
    return factorial(au) * factorial(cg)

if __name__ == "__main__":
    with open("data/rosalind_pmch.txt", "r") as f:
        with open("data/output_pmch.txt", "w") as o:
            result = perfect_match(ReadFASTA(f)[0])
            print(result)
            o.write(str(result))  

'''
Given: An RNA string s of length at most 100.

Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s.
'''

from DataProcess import ReadFASTA
from math import factorial
import decimal 

decimal.getcontext().prec = 100

def maximum_matching(rna):
    # count the occurrence of A, U, C, G
    au_num = [rna.count(base) for base in 'AU']
    cg_num = [rna.count(base) for base in 'CG']
 
    # compute "A", "U" and "C", "G" seperately
    AU = factorial(max(au_num)) / factorial(max(au_num) - min(au_num))
    CG = factorial(max(cg_num)) / factorial(max(cg_num) - min(cg_num))

    return AU * CG
    
if __name__ == "__main__":
    with open("data/rosalind_mmch.txt", "r") as f:
        rna = ReadFASTA(f)[0]
        with open("data/output_mmch.txt", "w") as o:
            result = maximum_matching(rna)
            print result
            o.write(str(result))

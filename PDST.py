'''
Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). 
Strings are given in FASTA format.

Return: The matrix D corresponding to the p-distance dp
on the given strings. As always, note that your answer is allowed an absolute error of 0.001.
'''

from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO
import pandas as pd

def distance_matrix(data):
    align = AlignIO.read(data, "fasta")
    matrix = list(DistanceCalculator("identity").get_distance(align))
    new_matrix = pd.DataFrame(matrix, index = None, dtype = "float16").to_string(index = False)
    return new_matrix

if __name__ == "__main__":
    with open("data/rosalind_pdst.txt", "r") as f:
        result = distance_matrix(f)
        with open("data/output_pdst.txt", "w+") as o:
            o.write(result)
            print(result)

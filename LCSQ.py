'''
Given: Two DNA strings s and t in FASTA format.

Return: A longest common subsequence of s and t.
'''

from DataProcess import ReadFASTA
from numpy import zeros

def lcs(s, t):
    matrix = zeros((len(s) + 1, len(t) + 1))
    for row in range(len(s)):
        for col in range(len(t)):
            if s[row] == t[col]:
                matrix[row + 1][col + 1] = matrix[row][col] + 1 
            else:
                matrix[row + 1][col + 1] = max(matrix[row + 1][col], matrix[row][col + 1])
    
    row = len(s)
    col = len(t)
    lcs = ""
    while row * col != 0:
        if matrix[row][col] == matrix[row - 1][col]:
            row -= 1
        elif matrix[row][col] == matrix[row][col - 1]:
            col -= 1
        else:
            lcs = s[row - 1] + lcs
            row -= 1
            col -= 1
    return lcs

if __name__ == "__main__":
    with open("data/rosalind_lcsq.txt", "r") as f:
        data = ReadFASTA(f)
        with open("data/output_lcsq.txt", "w") as o:
            o.write(lcs(data[0], data[1]))

'''
Given: A positive integer n.

Return: The total number of subsets of {1,2,…,n} modulo 1,000,000.
'''

from math import factorial

def count_subset(n):
    total = 0
    for x in range(n + 1):
        total += (factorial(n) / (factorial(n - x) * factorial(x)))
    
    return int(total % 1000000)

if __name__ == "__main__":
    with open("data/rosalind_sset.txt", "r") as f:
        with open("data/output_sset.txt", "w") as o:
            result = count_subset(int(f.read()))
            print(result)
            o.write(str(result))

'''
Given: A positive integer n (n≤1,000,000), a DNA string s of even length at most 10, 
and an array A of length at most 20, containing numbers between 0 and 1.

Return: An array B having the same length as A in which B[i] represents the expected number of times 
that s will appear as a substring of a random DNA string t of length n, where t is formed with GC-content A[i]
'''
from math import floor

def exp_num(n, s, A):
    exp = [0 for i in range(len(A))]
    for i in range(len(A)):
        t = n
        # different GC-content for each given A[i]
        gc = {"A": (1 - A[i]) / 2,
              "T": (1 - A[i]) / 2,
              "C": A[i] / 2,
              "G": A[i] / 2}
        # compute P(exactly equals to s)
        prob = 1
        for b in s:
            prob *= gc[b]
        # what we want is 1 - P(s is not a substring of t)
        

    return exp

if __name__ == "__main__":
    with open("data/rosalind_eval.txt", "r") as f:
        lines = f.readlines()
        n = int(lines[0].rstrip())
        s = lines[1].rstrip()
        A = [float(i) for i in lines[2].rstrip().split(" ")]
        with open("data/output_eval.txt", "w") as o:
            for line in list(map(int, exp_num(n, s, A))):
                o.write(str(line))
                o.write("\n")
            print(exp_num(n, s, A))

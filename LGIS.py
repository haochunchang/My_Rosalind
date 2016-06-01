'''
Given: A positive integer n≤10000 followed by a permutation π of length n

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
'''
'''
This implementation is copied from 
https://github.com/jschendel/Rosalind/blob/master/024_LGIS.py
'''
from math import ceil

def BinarySearchLEQ(S, data, value):
    '''Use a binary search to return the index of the smallest item in 'S' greater than or equal to 'value'.'''
    original_S = S
    while len(S) > 1:
        # index is the exact middle if odd, and the lower value if even.
        index = int(ceil(len(S) / 2.0 - 1))
        if data[S[index]] < value:
            S = S[index+1:]

        else:
            S = S[:index+1]

    return original_S.index(S[0])

def longest_subseq(data, decrease = False):
    '''Returns an ordered list of the longest increasing substring.'''
    S = [0]
    parent = [None] * len(data)

    for index in range(1, len(data)):

        if data[index] > data[S[len(S) - 1]]:
            parent[index] = S[len(S) - 1] 
            S.append(index)

        else:
            update_index = BinarySearchLEQ(S, data, data[index])
            S[update_index] = index
            parent[index] = S[update_index - 1] 

    # Get the indicies of each element in the longest increasing subsequence in reverse order.
    LIS = [S[len(S) - 1]]
    for i in range(0,len(S) - 1):
        LIS.append(parent[LIS[len(LIS) - 1]])
    
    # Convert indicies to values and reverse.
    LIS = [data[i] for i in LIS]
    LIS.reverse()
    
    # if longest decreasing subseq, eliminate the "-" sign
    if decrease:
        LIS = [-x for x in LIS]
        
    new_lis = ""
    for s in LIS:
        new_lis += str(s) + " "
       
    return new_lis

if __name__ == "__main__":
    with open("data/rosalind_lgis.txt", "r") as f:
        f = f.readlines()
        perm = list(map(int, f[1].rstrip().split(" "))) 
        with open("data/output_lgis.txt", "w") as o:
            lis = longest_subseq(perm)
            lds = longest_subseq([-x for x in perm], decrease = True)
            print(lis, lds)
            o.write(lis)
            o.write("\n")
            o.write(lds)

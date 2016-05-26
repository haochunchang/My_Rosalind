'''
Given: A positive integer n.

Return: The number of internal nodes of any unrooted binary tree having n leaves.

unrooted binary tree: A tree in which every node has degree equal to 1 or 3.
'''
import sys
from math import floor

def n_leaves_node(n):
    total = 0
    left = 0
    # exception when n = 3
    if n == 3:
        return 1
    
    while n > 1:
        total += floor(n / 2)
        left += n % 2
        n = floor(n / 2)
    if left > 0:
        total -= 1
        total += left
    else:
        total -= 1     
    return total

if __name__ == "__main__":
    print(n_leaves_node(int(sys.argv[1])))

'''
Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after
 the n-th month if all rabbits live for m months.

Notes: THIS METHOD IS FROM jschendel, I DO NOT UNDERSTAND THE DETAILS YET.
'''

def mortal_rabbit(n, m):
    
    #record the number of rabbit at every age
    rabbits = [1] + [0] * (m - 1)
    
    for month in range(1, n):
        bunnies = 0
        # get the number of rabbits old enough to give birth
        for birth in range(1, m):  
            bunnies += rabbits[(month - birth - 1) % m]

        # replace dead rabbits with newborn bunnies
        rabbits[month % m] = bunnies
    
    return sum(rabbits)

if __name__ == "__main__":
    with open("data/rosalind_fibd.txt") as f:
        n, m = map(int, f.read().split())
        with open("output_fibd.txt", "w") as o:
            o.write(str(mortal_rabbit(n, m)))

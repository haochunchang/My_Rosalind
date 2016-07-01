'''
Given: A positive integer N≤100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.

Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x 
(see “Introduction to Random Strings”), then at least one of the strings equals s. 
We allow for the same random string to be created more than once.
'''

# P(at least one of the strings equals to s) = 1 - P(none of the strings equals s)
def random_motif_match(N, x, s):
    s_construct = {"A": (1 - x) / 2,
                   "T": (1 - x) / 2,
                   "C": x / 2,
                   "G": x / 2}
    prob = 1
    # probability of exactly equals to s
    for b in s:
        prob *= s_construct[b]
    
    return 1 - (1 - prob) ** N

if __name__ == "__main__":
    with open("data/rosalind_rstr.txt", "r") as f:
        lines = f.readlines()
        N = int(lines[0].rstrip().split(" ")[0])
        x = float(lines[0].rstrip().split(" ")[1])
        s = lines[1].rstrip()
        with open("data/output_rstr.txt", "w") as o:
            o.write(str(random_motif_match(N, x, s)))
            print(random_motif_match(N, x, s))    

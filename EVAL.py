'''
Given: A positive integer n (n≤1,000,000), a DNA string s of even length at most 10, 
and an array A of length at most 20, containing numbers between 0 and 1.

Return: An array B having the same length as A in which B[i] represents the expected number of times 
that s will appear as a substring of a random DNA string t of length n, where t is formed with GC-content A[i]
'''

def exp_num(n, s, A):
	exp = []
	for gc in A:
		# compute gc content of s
		count = [s.count("C") + s.count("G"), s.count("A") + s.count("T")]
		# the number of slots which substring s can fit into t
		substring_slot = n - len(s) + 1
		prob = ((0.5 * gc) ** count[0]) * (0.5 * (1 - gc)) ** count[1]
		exp.append(str(prob * substring_slot)) 
		
	return exp

if __name__ == "__main__":
    with open("data/rosalind_eval.txt", "r") as f:
        lines = f.readlines()
        n = int(lines[0].rstrip())
        s = lines[1].rstrip()
        A = [float(i) for i in lines[2].rstrip().split(" ")]
        with open("data/output_eval.txt", "w") as o:
            for line in exp_num(n, s, A):
                o.write(line)
                o.write(" ")
                print(line)

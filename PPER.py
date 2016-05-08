'''
Given: Positive integers n and k

Return: The total number of partial permutations P(n,k), modulo 1,000,000.
'''

def partial_per(n, k):

	result = 1
	for i in range(n - k + 1, n + 1):
		result = (result * i) % 1000000

	return result

if __name__ == '__main__':
	with open(input("file input: ")) as f:
		n, k = map(int, f.read().split(" "))
		with open("output_pper.txt", "w") as o:
			o.write(str(partial_per(n, k)))
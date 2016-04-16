"""
Given: Two positive integers k and N. 
       The 0th generation has genotype AaBb. 
       0th has two children in the 1st generation, each of whom has two children, and so on. 
       Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N AaBb organisms will belong to the k-th generation.
        Assume that Mendel's second law holds for the factors.
"""
# Return the probability of exactly n AaBb offspring after k generations.
# success: 0.25, failure: 0.75
from math import factorial
def P(k, n):
	co = factorial(2**k) / (factorial(n) * factorial(2**k - n))
	return co * 0.25**n * 0.75**(2**k - n)

# Return the probability of at least n AaBb offspring
def prob(k, n):

	return 1 - sum([P(k, n) for n in range(n)])

if __name__ == "__main__":
	print(round(prob(6, 16), 3))	

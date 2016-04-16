# Return the expected number of offspring displaying the dominant phenotype in the next generation
# under the assumption that every couple has exactly two offspring.

def offspring(a, b, c, d, e, f):
	"""
		The six alphabets represent the number of couples having the following genotypes:
	    a. AA-AA
		b. AA-Aa
		c. AA-aa
		d. Aa-Aa
		e. Aa-aa
		f. aa-aa
	"""
	return 2 * (a + b + c) + 1.5 * d + e 

print(offspring(17327, 17395, 17285, 16053, 17185, 19775))
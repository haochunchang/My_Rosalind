'''
Given: Positive integers n≤40n≤40 and k≤5k≤5.

Return: The total number of rabbit pairs that will be present after nn months if we begin with 1 pair and in each generation, 
every pair of reproduction-age rabbits produces a litter of kk rabbit pairs (instead of only 1 pair).
'''

def pairs(month, child):
	if month == 1 or month == 2:
		result = 1
	elif month >= 3:
		result = pairs(month - 1, child) + child * pairs(month - 2, child)
	return result

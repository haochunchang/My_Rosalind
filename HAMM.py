'''
Given: Two DNA strings ss and tt of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
'''

def Hamming(s, t):
	d = 0
	for x in xrange(0,len(s)):
		if s[x] != t[x]: 
			d = d + 1
	return d


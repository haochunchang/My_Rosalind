def Hamming(s, t):
	d = 0
	for x in xrange(0,len(s)):
		if s[x] != t[x]: 
			d = d + 1
	return d


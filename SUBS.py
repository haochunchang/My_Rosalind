'''
Given: Two DNA strings ss and tt (each of length at most 1 kbp).
Return: All locations of tt as a substring of ss.
'''

def get_index(s, char):
	return [i[0] for i in enumerate(s) if i[1] == char]     #return a list of index of char in s

def Motif(s, subs):
	position = []
	index = get_index(s, subs[0])
	for i in range(0, len(index)):
		if subs == s[index[i]:index[i] + len(subs)]:
			position.append(index[i] + 1)

	return position

with open(input("file input: ")) as f:
	s = f.readline()[:-1]
	subs = f.readline()[:-1]
	m = open("motif.txt", "w")
	m.write(str(Motif(s, subs)))
	m.close()

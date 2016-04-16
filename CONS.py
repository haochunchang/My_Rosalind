'''
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. 
(If several possible consensus strings exist, then you may return any one of them.)
'''

from DataProcess import ReadFASTA

#Build profile from DNA seqence list
def profile(DNA):
	default = [0] * len(DNA[0])
	profile = {
	    "A": default[:],
	    "C": default[:],
	    "G": default[:],
	    "T": default[:],
	}	
	
	for s in DNA:
		for r, c in enumerate(s):
			profile[c][r] += 1

	return profile

#Turn profile dictionary into matrix
def matrix(profile):
	matrix1 = "A: "
	matrix2 = "C: "
	matrix3 = "G: "
	matrix4 = "T: "

	for col in range(0, len(profile["A"])): 
		matrix1 = matrix1 + str(profile["A"][col]) + " "

	for col in range(0, len(profile["A"])): 
		matrix2 = matrix2 + str(profile["C"][col]) + " "

	for col in range(0, len(profile["A"])): 
		matrix3 = matrix3 + str(profile["G"][col]) + " "

	for col in range(0, len(profile["A"])): 
		matrix4 = matrix4 + str(profile["T"][col]) + " "

	return " \n" + matrix1 + " \n" + matrix2 + " \n" + matrix3 + " \n" + matrix4

#Build consensus seq from profile
def consensus(profile):
	con = ""
	keys = profile.keys()

	for i in range(0, len(profile[list(keys)[0]])):
		max_v = 0
		max_k = None
		for k in keys:
			v = profile[k][i]
			if v > max_v:
				max_v = v
				max_k = k
		con += max_k

	return con
	
if __name__ == "__main__":
	with open(input("file input: ")) as f:
		data = ReadFASTA(f)
		pro = profile(data)
		con = consensus(pro)
	with open("cons_output.txt", "w") as o:
		o.write(con)
		o.write(" ")
		o.write(str(matrix(pro)))

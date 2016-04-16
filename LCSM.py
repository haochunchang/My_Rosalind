"""
	Given: A collection of k DNA strings in FASTA format.
	Return: A longest common substring of the collection. 
"""

from DataProcess import ReadFASTA

#Extract all substring of the first element in a list and check the longest substring
def LongestSubstring(string_list):
	longest = ""

	for start_index in range(len(string_list[0])):
		for end_index in range(len(string_list[0]), start_index, -1):
			if end_index - start_index <= len(longest):
				break
			elif Check(string_list[0][start_index:end_index], string_list):
				longest = string_list[0][start_index:end_index]
	return longest

#Check the given substring appears in all members of a given collection of strings
def Check(substring, string_list):
	for string in string_list:
		if substring not in string:
			return False
	return True

if __name__ == '__main__':
	with open(input("file input: ")) as f:
		dna = ReadFASTA(f)
		longest = LongestSubstring(dna)
		print(longest)
		with open("output_lcsm.txt", "w") as o:
			o.write(longest)
		





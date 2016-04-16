import os

def split(string, a, b, c, d):
	return string[a:b + 1] + "\t" + string[c:d + 1]

def odd(a, b):    #The sum of all odd integers from a through b, inclusively.
	result = 0
	for x in xrange(a, b + 1):
		if x % 2 == 1:
			result += x
	return result

def file_process(filename):       #Output a file containing all the even-numbered lines from the original file.
	filename = input("file: ")
	number = 0
	with open(filename) as f:
		new = open("newfile.txt", "w")
		while True: 
			line = f.readline()
			number += 1
			if number % 2 == 0:
				new.write(line)
		new.close()

def Dict(string):          #Return how many times any word occurred in string. 
	dic = {}
	for word in string.split(" "):
		if word in dic:
			dic[word] = dic[word] + 1
		else:
			dic[word] = 1
	for key, value in dic.items():
		print key
		print value



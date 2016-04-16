'''
Given: Three positive integers kk, mm, and nn, representing a population containing k+m+nk+m+n organisms: 
kk individuals are homozygous dominant for a factor, mm are heterozygous, and nn are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele 
(and thus displaying the dominant phenotype). Assume that any two organisms can mate.
'''
import random
	
def MFL(k, m, n):   
	# "YY" * k, "Yy" * m, "yy" * n
	# Mathematical model 
	denon = (k + m + n) * (k + m + n - 1)
	YYxYY = (k * (k - 1)) / denon
	YYxYy = 2 * ((k * m) / denon)
	YYxyy = 2 * k * n / denon
	YyxYy = 0.75 * m * (m - 1) / denon
	Yyxyy = m * n / denon
	return YYxYY + YYxYy + YYxyy + YyxYy + Yyxyy

def Population(k, m, n):
	#Simulation model
	P = ["YY"] * k + ["Yy"] * m + ["yy"] * n       #create a list of organisms
	times = 1000000
	d = 0
	for x in range(0, times):
		A = random.randint(0, k + m + n - 1)
		B = random.randint(0, k + m + n - 1)
		if Mating(P[A], P[B]):
			d = d + 1
	return d / times

def Mating(A, B):    #return True if child is dominant
	if A == "YY" or B == "YY":
		return True
	elif A == "Yy" and B == "Yy":
		if random.randint(1, 4) % 4 != 0:
			return True
		else:
			return False
	elif A == "yy" and B == "yy":
		return False 
	else:          #Yyxyy
		return random.randint(0, 1)

print(MFL(19, 15, 21))

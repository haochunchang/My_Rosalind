def pairs(month, child):
	if month == 1 or month == 2:
		result = 1
	elif month >= 3:
		result = pairs(month - 1, child) + child * pairs(month - 2, child)
	return result

print(pairs(5, 3))
def collatz(x,listdict):
	count = 1
	while x != 1:
		if listdict.has_key(x):
			count += listdict[x]
			x = 1
		elif x % 2 == 0:
			x /= 2
		else:
			x = 3*x +1
		count += 1
	return count

def longest():
	maxlen = 0
	length = 0
	value = 0
	index = {}
	for x in range(1,1000001):
		length = collatz(x,index)
		index[x] = length
		if length >= maxlen:
			maxlen = length
			value = x
	return value 

print longest()


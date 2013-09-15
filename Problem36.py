def ispoly(number):
	if str(number) == str(number)[::-1]:
		return True
	else:
		return False

def isbin(number):
	binary = bin(number)
	string = str(binary)[2:]
	rev = string[::-1]
	if string == rev:
		return True
	else:
		return False

mysum = 0
for i in range(1, 1000001):
	if ispoly(i):
		if isbin(i):
			mysum += i
print mysum
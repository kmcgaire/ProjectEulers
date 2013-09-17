def ismultiple(number, x):
		if number % x == 0:
			return True
		return False

def smallest_multiple(x):
	if x<1:
		return False
	elif x == 1:
		return 1
	else:
		Increment = smallest_multiple(x-1)
		number = 0
		found = False
		while not found:
			number += Increment
			found = ismultiple(number, x)
		return number

print smallest_multiple(20)
                     

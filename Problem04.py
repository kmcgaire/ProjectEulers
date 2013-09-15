def is_palindrome(value):
	return str(value) == str(value)[::-1]

def twofactors():
	for n in reversed(xrange(100*100,999*999)):
		if is_palindrome(n):
			for factor1 in reversed(xrange(100,1000)):
				for factor2 in reversed(xrange(100,1000)):
					if n == (factor2 * factor1):
						return n
print twofactors()

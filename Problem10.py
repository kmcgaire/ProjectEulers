def is_prime(n):
	p = 3
	sqrt_divided = int(n**(0.5)+1)
	while p < sqrt_divided:
		if n % p == 0:
			return False
		p += 2
	return True

def main():
	value = 2
	for i in xrange(3,2000000, +2):
		if is_prime(i):
			value += i
	return value

print main()

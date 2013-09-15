def triangle(x):
	return x*(x+1) / 2

	

def num_divisors(n):
	if n % 2 == 0: n /= 2
	divisor = 1
	count = 0
	while n % 2 == 0:
		count += 1
		n /= 2
	divisor *= (count + 1)
	x = 3
	while n != 1:
		count = 0
		while n % x == 0:
			count += 1
			n /= x
		divisor *= (count + 1)
		x += 2
	return divisor

def main():
	n = 1
	x, y = num_divisors(n), num_divisors(n+1)
	while x * y < 500:
		n += 1
		x, y = y, num_divisors(n+1)
	return n*(n+1) / 2

print main()

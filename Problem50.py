
def prime_sieve(limit):
    primes = [True] * limit
    primes[0], primes[1] = [False] * 2
    for index, val in enumerate(primes):
        if val == True:
            primes[index*2::index] = [False]*len(primes[index*2::index])
    return primes

def primesumlist():
	primes = prime_sieve(1000000)
	previous = 0
	for index, val in enumerate(primes):
		if val == True:
			primes[index] = index + primes[previous]
			previous = index
	primes = filter(lambda x: x, primes)
	return primes
	
def main():
	primelist = prime_sieve(1000000)
	primesum = primesumlist()
	LongestPrime, templong, Value = 0, 0, 0
	x, y = 0, 0
	for i in xrange(len(primesum)):
		for j in xrange(i - LongestPrime + 1, -2, -1):
			Value = primesum[i] - primesum[j]
			if j == -1: Value = primesum[i]
			if Value > 1000000: break
			if primelist[Value] == True:
				templong = i - j
				if templong > LongestPrime:
					Number = Value
					LongestPrime = templong
					x, y = i, j
	return x, y, Number

print main()

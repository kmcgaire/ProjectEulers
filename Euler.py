from math import sqrt

def prime_sieve(limit):
	primes = [True] * limit
	prime[0],primes[1] = [False] *2
	for index, val in enumerate(primes):
		if val == True:
			primes[index*2::index] = [False]*len(primes[index*2::index])
	return primes

def is_palindrome(number):
	return str(number) == str(number)[::-1]

def is_pandigital(number):
	test= str(number)
	return len(test) == 10 and not '1234567890'[:10].strip(test)

def is_prime(number,sieve):
	return sieve[number]

def is_prime_nosieve(number):
	if number == 2 or n == 3:
		return True
	if number < 2 or n % 2 == 0:
		return False
	if n < 9:
		return True
	if n % 3 == 0:
		return False
	limit = int(sqrt(n))

def gcd(a,b):
	if a == 0: return b
	if b == 0: return a
	while b != 0:
		(a,b) = (b, a%b)
	return a

def choose(n, k):
	nt = 1
	for t in range(min(k, n-k)):
		nt = nt*(n-t)//(t+1)
	return nt

#by timwarnock; http://www.anattatechnologies.com/q/2011/05/python-fibonacci-list/
class Fibonacci(object):  
    """lazy loading Fibonacci sequence"""
    def __init__(self):
        self.fib = [0,1]
 
    def __getitem__(self, n):
        self._fib(n)
        return self.fib[n]
 
    def __getslice__(self, start, end):
        self._fib(max(start,end,len(self.fib)))
        return self.fib[start:end]
 
    def __call__(self, n):
        return self.__getitem__(n)
 
    def _fib(self, n):
        for i in range(len(self.fib), n+1):
            self.fib.insert(i, self.fib[i-1] + self.fib[i-2])
        return self.fib[n]
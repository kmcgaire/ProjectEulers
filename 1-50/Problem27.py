import time
start = time.time()
def prime_sieve(limit):
    primes = [True] * limit
    primes[0], primes[1] = [False] * 2
    for index, val in enumerate(primes):
        if val == True:
            primes[index*2::index] = [False]*len(primes[index*2::index])
    return primes
 

P = prime_sieve(751000) #largest possible value with a,b being 1000 and n being insanely huge
amax, bmax, cmax = 0, 0, 0
for a in range(-1000,1001):
    for b in range(1,1001):
        if P[b] == False: continue
        c, n = 0, 0
        while P[n**2 + a*n + b] == True:
             c += 1
             n += 1
        if c > cmax:
            amax, bmax, cmax = a, b, c
 
#print prime_sieve(20)
print amax * bmax
print "function is"
print "n**2 + %s*n + %s" % (amax, bmax)
print "Produces %s primes in a row" % (cmax)
print "completed in " + str(time.time() - start) + "seconds"

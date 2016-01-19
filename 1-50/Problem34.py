from math import factorial
fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
s = 0
 
MaxPossible = factorial(9) * 7

for n in xrange(10, MaxPossible):
  x = sum( fact[int(d)] for d in str(n) )
  if n == x: s+=n
 
print s
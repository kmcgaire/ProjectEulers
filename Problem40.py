decimal = "0"
for i in xrange(1,1000000):
	if len(decimal) > 1000000: break
	decimal += str(i)
myproduct = 1
for i in range(0,7):
	myproduct *= int(decimal[10**i])
print myproduct
n, d, c = 3, 2, 0
for x in xrange(2,1001):
	n, d = n+d*2, n+d
	if len(str(n)) > len(str(d)): c+=1
print c
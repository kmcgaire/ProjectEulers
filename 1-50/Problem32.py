
p = set()
for i in range(2,100):
	start = 1234
	if i > 0: start = 123
	for j in range(start, 10000/(i+1)):
		string = str(i) + str(j) + str(i*j)
		for k in range(1,10):
			if str(k) not in string: break
			if k == 9: p.add(i*j)

print sum(p)

import itertools
x = itertools.permutations('0123456789',10)

count = 0
for i in x:
	count += 1
	if count == 1000000:
		print i
	else: continue

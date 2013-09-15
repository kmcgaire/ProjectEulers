n = 7*9**5

largesum = 0
for i in range (2,n):
	smallsum = 0
	for j in str(i):
		smallsum += int(j)**5
	if smallsum == i:
		largesum += smallsum

print largesum

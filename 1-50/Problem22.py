
f = open("names.txt","r")
L=f.read().split(",")
L.sort()
mysum = 0
namesum = 0
for i,name in enumerate(L):
	for j in name:
		if j.isalpha():
			mysum += (i + 1) * (ord(j) - ord("A") +1)
		else: continue

print mysum




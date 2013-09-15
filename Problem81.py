import time
matrix = [[int(n) for n in f.split(',')] for f in open('matrix.txt').readlines()]
length = len(matrix) - 1

start = time.time()

for i in range(length, -1, -1):
	for j in range(length, -1, -1):
		if (i == length and j == length): continue
		elif (j == length):
			localmin = matrix[i+1][j]
		elif (i == length):
			localmin = matrix[i][j+1]
		else:
			localmin = min(matrix[i][j+1],matrix[i+1][j])
		matrix[i][j] += localmin

print matrix[0][0]
elapsed = time.time() - start
print elapsed
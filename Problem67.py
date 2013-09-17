d = open('triangle.txt')
triangle = []
for line in d:
	triangle.append([int(i) for i in line.split(" ")])

for i,j in [(i,j) for i in range(len(triangle)-2,-1,-1) for j in range(i +1)]:
	triangle[i][j] += max([triangle[i+1][j],triangle[i+1][j+1]])

print triangle[0][0]
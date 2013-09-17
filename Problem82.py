import time
matrix = [[int(n) for n in f.split(',')] for f in open('matrix1.txt').readlines()]

start = time.time()
def main():
  col, row, search, current, accum = 78,0,0,0,0
  for i in range(col,-1,-1):
    for j in range(0,80):
      current, accum = matrix[j][i + 1], 0
      for search in range(j+1,80):
        if accum + matrix[search][i] > current: break
        if current > matrix[search][i+1] + matrix[search][i] + accum:
          current = matrix[search][i+1] + matrix[search][i] + accum
        accum += matrix[search][i]
      if j != 0:
        if current > matrix[j - 1][i]:
          current = matrix[j - 1][i]
      matrix[j][i] += current
  minpath = matrix[0][0]
  for i in range(0,80):
    if matrix[i][0] < minpath:
      minpath = matrix[i][0]
  return minpath

print main()
print "completed in " + str(time.time() - start) + "seconds"
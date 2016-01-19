import time

def cube_sorted_sieve(limit):
   cubes = [0]*limit
   for i in xrange(0,limit):
      cubes[i] = sorted(str(i*i*i))
   return cubes
   
def Problem62():
   limit = 10000
   cubes = cube_sorted_sieve(limit)
   count = 0
   first = 0
   for i in range(0,limit):
      count = 0
      for j in range(i,limit):
         if (cubes[i] == cubes[j]):
            count += 1
      if (count == 5):
         first = i
         break        
   return i*i*i
   
   
start = time.time()
print "Answer to Problem 62: ", Problem62()
print "Solution took: ", time.time() - start, "seconds"   

#Looking back, may have been easier to implement using a dictionary and
#their keys. As I iterate over the range, add the sorted cube of the string
#to the dictionary and once the key has a length of 5, break and thats the number.

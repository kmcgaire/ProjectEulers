from Euler import is_palindrome
import time

def nextIteration(num):
   return num + int(str(num)[::-1])
   
def Problem55():
   maxIter = 50
   iterations = 0
   count = 10000
   for i in xrange(1,10001):
      check = i
      iterations = 0
      while(iterations < maxIter):
         check = nextIteration(check)
         if(is_palindrome(check)):
            count -= 1
            break
         iterations += 1
   return count  

start = time.time()      
print "Answer to Problem 55: ", Problem55()
print "Answer took: ", time.time() - start, "seconds"
            

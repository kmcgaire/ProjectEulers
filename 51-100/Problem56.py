import time

def Problem56():
   maxDigitSum = 0
   for a in xrange(1,100):      
      for b in xrange(1,100):
         currentSum = 0
         num = a ** b
         while (num != 0):
            currentSum = currentSum + num % 10
            num = num // 10
         if (currentSum > maxDigitSum):
            maxDigitSum = currentSum
   return maxDigitSum
   
start = time.time()
print "Answer to Problem 56: ", Problem56()
print "Solved in: ", time.time() - start, " seconds"
 
 

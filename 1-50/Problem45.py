import time

def triangle(n):
   return n*(n+1)/2
   
def pentagonal(n):
   return n*(3 * n - 1) / 2
   
def hexagonal(n):
   return n*(2 * n - 1)


def Problem45():
   nt = 286
   np = 165
   nh = 143
   newHex = 0
   newPent = 0
   newTriangle = 0
   foundPent = False
   found = False
   while(not found):
      newTriangle = triangle(nt)
      newPent = 0
      newHex = 0
      i = np
      while (newPent < newTriangle):
         newPent = pentagonal(i)
         if(newPent == newTriangle):
            break
         i += 1
      np = i - 1
      i = nh
      if (newPent == newTriangle):
         while (newHex < newTriangle):
            newHex = hexagonal(i)
            if (newHex == newTriangle):
               found = True
               break
            i += 1
         nh = i - 1 
      nt += 1     
   return newTriangle
   
start = time.time()
print "Answer to Problem 45: ", Problem45()
print "Answer took ", time.time() - start, "seconds"
         
      

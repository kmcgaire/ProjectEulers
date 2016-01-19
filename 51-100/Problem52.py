
import time

def compareNum(a,b):
   stringA = sorted(str(a))
   stringB = sorted(str(b))
   return stringA == stringB
   
def Problem52():

   newInt = 1
   while (True):
      if (compareNum(newInt, newInt * 2)):
         if (compareNum(newInt, newInt * 3)):
            if (compareNum(newInt, newInt * 4)):
               if (compareNum(newInt, newInt * 5)):
                  if (compareNum(newInt, newInt * 6)):
                     break
      newInt += 1
   return newInt

start = time.time()   
print "Answer to Problem52: ", Problem52()
print "Time to Complete: ", time.time() - start



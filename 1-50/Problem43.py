from itertools import permutations
import time
#Analysis
#Going through Rule by Rule to reduce the amount of brute force calc needed.
#since d2d3d4 is divisable by 2, d4 is from the set {0,2,4,6,8}
#since d4d5d6 is divisable by 5, d6 is from the set {0, 5}
#since d6d7d8 has to be 11, and starts with {0, 5}:
#       Can't start with 0, else it yields unpossible numbers, 011, 022 etc.
#d6 = 5
#All 500s that are divisable by 11 are {506,517,528,539,561,572,583,594}
#d7d8d9 is divisable by 13, and starts with either {06,17,28,39,61,72,83,94}
#This gives the set for that to be {286,390,728,832} that are divisable by 13 
#     and do not contain 5s
#d8d9d10 divisible by 17 and begin with {28,32,86,90} and contains no 5s, or repeats
#  set is {289,867,901}

#Therefore
#d6 = {5}
#d7d8d9 = {286,390,728}
#d8d9d10 = {289,867,901}
#Therefore:
# d6d7d8d9d10 = {52867,57289,53901}

#Furthermore d5d6d7 must be divisable by 7, and we are left with ones ending with {52,53,57}
# this gives {357,952} as the only two combinations.

#therefore d5d6d7d8d9d10 = {357289, 952867}

#The above sets cover everything except the first 2 rules need a quick check

def checkRule2and3(string):
	return (int(string[1:4]) % 2 == 0) and (int(string[2:5]) % 3 == 0)

def Problem42():
	mysum = 0
	for i in permutations('0146',4):
		a = ''.join(i) + '357289'
		if (checkRule2and3(a)): mysum += int(a)
	for i in permutations('0134',4):
		a =  ''.join(i) + '952867'
		if (checkRule2and3(a)): mysum += int(a)
	return mysum

start = time.time()
print Problem42()
print time.time() - start


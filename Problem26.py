from decimal import *

def main():
    Longest = 0
    max_number = 0
    getcontext().prec = 1000
    for i in range(1, 1001):
        num_string = str(Decimal(1) / Decimal(i))
        period_length = period(num_string)
        if period_length > Longest:
            Longest = period_length
            max_number = i
    return max_number

 
def period(decimalstr):
    length = len(decimalstr)
    zero_location = 0
    lookup = []
    if decimalstr[2:3] != '0': #case first number isn't 0
        lookup = decimalstr[2:8]
        zero_location = 0
    elif decimalstr[2:3] == '0' and decimalstr[3:4] != '0': #case first number is 0 and second isnt
        lookup = decimalstr[3:9]
        zero_location = 1
    elif decimalstr[2:3] == '0' and decimalstr[3:4] == '0': #First two numbers are 0
        lookup = decimalstr[4:10]
        zero_location = 2
    max_period = 0
    check = []
    for i in range(3, length):
        if zero_location == 0:
            check = decimalstr[i:(i + 6)]
        elif zero_location == 1:
            check = decimalstr[(i + 1):(i + 7)]
        elif zero_location == 2:
            check = decimalstr[(i + 2):(i + 8)]
        else:
            print "guess this didn't work"
        if lookup == check:
            max_period = i
            break
    return max_period
 
print main()

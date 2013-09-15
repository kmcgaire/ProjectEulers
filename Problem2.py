x,y = 0, 1
value = 0
while y < 4000000:
    if y%2 == 0:
        value += y
    x,y = y, x+y
print value

def main():
	#wikipedia page on pythagorean triples HELPFUL!!
    for n in range(1, 500):
        for m in range(n + 1, 500):
            a = int(m ** 2 - n ** 2)
            b = 2 * m * n
            c = int(m ** 2 + n ** 2)
            if a + b + c == 1000:
                product = a * b * c
    return product
 
print main()


def letter_value(letter):
    return ord(letter) - 64

def get_word_value(word):
    return sum(letter_value(letter) for letter in word)
 
def triangle(n):
    return int((0.5) * n * (n + 1))
    
 
def main():
    """Main Program"""
    triangle_numbers = [triangle(n) for n in range(1,100)]
    f = open('words.txt', "r")
    words = [word.strip('"') for word in open('words.txt', "r").read().split(',')]
    total = 0
    print words
    total = 0
    for word in words:
        if get_word_value(word) in triangle_numbers:
            total += 1
    print total
             
if __name__ == '__main__':
    main()


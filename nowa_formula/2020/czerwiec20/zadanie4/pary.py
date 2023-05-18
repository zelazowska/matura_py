from math import sqrt
from math import factorial
temporary = open("pary.txt")
file = temporary.readlines()
temporary.close()

results = open("wyniki4.txt", "w")

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(sqrt(n))+1):
            if n%i == 0:
                return False
    return True

results.write("ZADANIE 4\n\nZad. 4.1\n")
for lines in file:
    number, word = lines.rstrip().split(" ")
    
    if int(number)%2 == 0:
        i = 0
        for i in range(3, int(number)+i):
            if is_prime(i) and is_prime(int(number)-i):
                results.write(f"{number} {i} {int(number)-i}\n")
                break

results.write("\n\nZad. 4.2\n")
for lines in file:
    number, word = lines.rstrip().split(" ")
    max_sequence = word[0]
    max_sequence_len = 1
    
    sequence_len = 1
    new_word = word[0]
    for i in range(1, len(word)):
        if word[i-1] == word[i]:
            new_word += word[i]
            sequence_len += 1
            if sequence_len > max_sequence_len:
                max_sequence_len = sequence_len
                max_sequence = new_word
                
        else:
            sequence_len = 1
            new_word = word[i]
    results.write(f"{max_sequence} {max_sequence_len}\n")
    
smallest = []
for lines in file:
    number, word = (lines.rstrip().split(" "))
    if int(number) == len(word):
        smallest.append(word)
    
results.write(f"\n\nZad 4.3\n{sorted(smallest)[0]} {len(sorted(smallest)[0])}")
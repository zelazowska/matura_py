import math
from collections import Counter

temp = open("NAPIS.TXT")
file = temp.readlines()
temp.close()
results = open("ZADANIE5.TXT", "w")

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
 
words = []   
primes_counter = 0
for lines in file:
    ascii_sum = 0
    lines = lines.rstrip()
    words.append(lines)
    for character in lines:
        ascii_sum += ord(character)
    
    if isPrime(ascii_sum):
        primes_counter += 1
        
results.write(f"ZADANIE 5\n\n5a) Napisow pierwszych w pliku: {primes_counter}")
results.write(f"\n\n5b)\n")
for lines in file:
    last_ascii, flag = 0, 0
    lines = lines.rstrip()
    for character in lines:
        if ord(character) > last_ascii:
            last_ascii = ord(character)
        else:
            flag = 1
    if flag == 0:
        results.write(f"{lines}\n")

results.write(f"\n\n5c)\n")       
keys = [key for key, value in Counter(words).items() if value > 1]
for key in keys:
    results.write(f"{key}\n")


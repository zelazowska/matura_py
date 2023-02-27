import math
from collections import Counter

file = open("liczby.txt")
numbers = file.read().split()
results = open("wyniki4.txt", "w")
file.close()


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
    

#4.1
results.write("ZADANIE 4\n\nZadanie 4.1\n")
for lines in numbers:
    if int(lines[::-1])%17 == 0:
        results.write(f"{lines.strip()[::-1]}\n")

#4.2
max_diff = -1000000009
max_diff_number = 0
for lines in numbers:
    lines = lines.strip()
    diff = abs(int(lines) - int(lines[::-1]))
    if diff > max_diff:
        max_diff = diff
        max_diff_number = lines
        
results.write(f"\nZadanie 4.2\n{max_diff_number} {max_diff}\n\n")

#4.3
results.write("Zadanie 4.3\n")
for lines in numbers:
    if isPrime(int(lines)) and isPrime(int(lines[::-1])):
        results.write(f"{lines}\n")

#4.4
unique_numbers = []
all_numbers = []
for lines in numbers:
    lines = lines.strip()
    all_numbers.append(int(lines))
    if lines not in unique_numbers:
        unique_numbers.append(lines)

counter_list = Counter(all_numbers)       
two_times = 0
three_times = 0 
for count in counter_list.values():
    if count == 2:
        two_times += 1
    elif count == 3:
        three_times += 1
        
results.write(f"\nZadanie 4.4\n{len(unique_numbers)} {two_times} {three_times}")
results.close()

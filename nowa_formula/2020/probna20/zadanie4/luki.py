import math
from collections import Counter

file = open("dane4.txt", "r")
example = open("przyklad.txt", "r")
results = open("zadanie4.txt", "w")

#4.1
numbers = []
for lines in file:
    numbers.append(int(lines.strip()))

biggest_jump = -10000009
smallest_jump = 10000009

for i in range(1, len(numbers)):
    biggest_jump = max(biggest_jump, int(math.fabs(numbers[i]-numbers[i-1])))
    smallest_jump = min(smallest_jump, int(math.fabs(numbers[i]-numbers[i-1])))

results.write("ZADANIE 4\n\nZadanie 4.1\n")
results.write(f"Najwieksza luka: {biggest_jump}\nNajmniejsza luka: {smallest_jump}\n\n")

#4.2
nums = []
for line in example:
    nums.append(int(line.strip()))
    
#4.3
absolutes = []
for i in range(1, len(numbers)):
    absolutes.append(abs(numbers[i]-numbers[i-1]))
    
print(absolutes)
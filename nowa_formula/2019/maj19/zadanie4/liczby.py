from math import factorial
from math import gcd

temp = open("przyklad.txt")
file = temp.readlines()
results = open("wyniki4.txt", "w")
temp.close()

threes = [pow(3, i) for i in range(12)]
counter = 0

for lines in file:
    lines = lines.rstrip()
    if int(lines) in threes:
        counter += 1
results.write(f"4.1\nLiczb bedacych potegami trojki: {counter}\n\n")

results.write(f"4.2\n")
for lines in file:
    lines = lines.rstrip()
    factorial_sum = 0
    for number in lines:
        factorial_sum += factorial(int(number))
    if int(lines) == factorial_sum:
        results.write(f"{lines}\n")
        
numbers = []
for lines in file:
    numbers.append(int(lines.rstrip()))
#xdddddddddddddddd
# all_gcds = [0]]
# for i in range(1, len(numbers)):
#     all_gcds.append(gcd(numbers[i-1], numbers[i]))
# for i in range(1, len(numbers)):
#     print(numbers[i-1], numbers[i])
    
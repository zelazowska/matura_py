import math
from collections import Counter

temp = open("liczby.txt")
numbers = temp.readlines()
temp.close()

def uneven_factors(n):
    uneven_factors = []
    i = 2
    while n > 1:
        if n%i != 0:
            i+=1
        else:
            n//=i
            if i%2 != 0:
                uneven_factors.append(i)
            else:
                return False
    if len(set(uneven_factors)) == 3:
        return True
    else:
        return False
    
print("59.1")      
# not optimal, rather brute
counter = 0
for number in numbers:
    number = int(number.rstrip())
    if uneven_factors(number):
        counter += 1
        
print(f"{counter}\n")

print("59.2")
palindromic_sums = 0
for number in numbers:
    number = number.rstrip()
    number_sum = int(number) + int(number[::-1])
    if str(number_sum) == str(number_sum)[::-1]:
        palindromic_sums += 1
        
print(f"{palindromic_sums}\n")

print("59.3")
initial_numbers = []
powers = []
max_power1 = 0
min_power1 = 100009
for number in numbers:
    lines = number.rstrip()
    number = number.rstrip()
    power = 0 
    while int(number) > 9:
        product = 1
        for char in str(number):
            product *= int(char)
        power += 1
        number = product
    powers.append(power)
    initial_numbers.append(int(lines))
    if power == 1:
        max_power1 = max(int(lines), max_power1)
        min_power1 = min(int(lines), min_power1)
        
for key, value in Counter(powers).items():
    print(key, value)
    
print(f"Maksymalna dla mocy 1: {max_power1}\nMinimalna: {min_power1}")

    
    
        

    
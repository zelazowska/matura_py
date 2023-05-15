import math

temp = open("59/liczby.txt", "r")
numbers = temp.readlines()
temp.close()

# 59.1
counter = 0
for number in numbers:
    number = int(number)
    num = number
    unique_factors = []
    factors = []
    divider = 2
    while number >= 2:
        while number%divider == 0:
            number //= divider
            factors.append(divider)
        divider += 1
    for factor in factors:
        if factor not in unique_factors and factor%2 != 0:
            unique_factors.append(factor)

    if len(unique_factors) == 3:
        counter = counter + 1
        print(num, unique_factors)
    
print(counter)
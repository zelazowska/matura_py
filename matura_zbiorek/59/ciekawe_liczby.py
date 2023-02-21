import math

numbers = open("liczby.txt", "r")

def prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors 
"""
def primeFactors(n):
    factors = []
    divider = 2
    while n != 1:
        while n%divider == 0:
            n = n//divider
            factors.append(divider)
    return factors
"""
#59.1 
count = 0
for lines in numbers:
    number = int(lines.strip())
    liczby = prime_factors(number)

    if len(liczby) == 3 and all(i%2 != 0 for i in liczby):
        count += 1
            
print(prime_factors(7), count)

    
numbers.close()

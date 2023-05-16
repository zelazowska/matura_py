file = open("ciagi.txt")
temp = file.read().split()
file.close()
results = open("wyniki_ciagi.txt", "w")

def Primes(n):
    prime_factors = [] 
    divider = 2
    while n!=1:
        while n%divider == 0:
            prime_factors.append(divider)
            n//=divider
        divider += 1
    return(prime_factors)
               
#63.1
results.write(f"Zadanie 63.1\n")
for lines in temp:
    number = lines.strip()
    if len(number)%2==0:
        half = int(len(number)/2)
        if number[:half] == number[half:]:
            results.write(f"{number}\n")

    
#63.2
without_11 = 0
for lines in temp:
    if "11" not in lines:
        without_11 += 1
results.write(f"\nZadanie 63.2\nCiagow, w ktorych nie wystepuja obok siebie dwie jedynki: {without_11}\n\n")

#63.3
half_prime = 0
for lines in temp:
    number = lines.strip()
    num = int(number, 2)
    if len(Primes(num)) == 2:
        half_prime += 1

results.write(f"\nZadanie 63.3\nCiagow reprezentujacych liczby polpierwsze: {half_prime}\n\n")
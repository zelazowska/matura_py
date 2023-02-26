import math

file_1 = open("liczby.txt", "r")
file_2 = open("pierwsze.txt", "r")
file_3 = open("pierwsze.txt", "r")
results_4_1 = open("wyniki4_1.txt", "w")
results_4_2 = open("wyniki4_2.txt", "w")
results_4_3 = open("wyniki4_3.txt", "w")


def isPrime(n): # sieve of erastotanes can also be implemented, but this function is used two times
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def weight(n):
    number_sum = 0
    while(len(str(n))) > 1:
        for numbers in n:
            number_sum += int(numbers)
        n = str(number_sum)
        number_sum = 0
    return n 
   
   
#4.1
results_4_1.write("Zadanie 4.1\n")
for numbers in file_1:
    if int(numbers.rstrip()) in range(100,5001) and isPrime(int(numbers.rstrip())):
        results_4_1.write(f"{numbers}")

#4.2
results_4_2.write("Zadanie 4.2\n")
for primes in file_2:
    if isPrime(int(primes.rstrip()[::-1])):
        results_4_2.write(f"{primes.rstrip()}\n")
    
#4.3
results_4_3.write("Zadanie 4.3\n")
counter = 0
for lines in file_3:
    lines = lines.rstrip()
    if weight(lines) == '1':
        counter += 1
results_4_3.write(f"Pierwszych, ktorych waga jest rowna 1: {counter}")


file_1.close()
file_2.close()
file_3.close()
results_4_1.close()
results_4_2.close()
results_4_3.close()


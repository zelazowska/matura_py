results = open("wyniki.txt", "w")

def isAmountOfDividers18(n):
    dividers = [n]
    for i in range(1, (n//2)+1):
        if n%i == 0:
            dividers.append(i)
    dividers = sorted(dividers)
    if len(dividers) == 18:
        return dividers

#60.1
file = open("liczby.txt")
with open("liczby.txt") as file:
    smaller_than_1000 = []
    for lines in file:
        number = int(lines.strip())
        if number < 1000:
            smaller_than_1000.append(number)       
results.write(f"60.1\nAmount of numbers smaller than 1000:\n{len(smaller_than_1000)}\nLast two numbers smaller than 1000:\n{smaller_than_1000[-2]}, {smaller_than_1000[-1]}\n\n")

#60.2
with open("liczby.txt") as file: 
    results.write(f"60.2\nNumbers with 18 dividers:\n") 
    for lines in file:
        number = int(lines.strip())
        if isAmountOfDividers18(number):
            results.write(f"{number} {isAmountOfDividers18(number)}\n")
    results.write("\n\n")

#60.3
dividers = []
biggest_number = 0
with open("liczby.txt") as file:
    for lines in file:
        number = int(lines.strip())
        dividers.append(number)
        for i in range(2, (int(number**(0.5)))+1):
            if number%i == 0:
                dividers.append(i)

with open("liczby.txt") as file:
    for lines in file:
        number = int(lines.strip())
        num_dividers = [number]
        unique = 0
        for i in range(2, (int(number**(0.5)))+1):
            if number%i == 0:
                num_dividers.append(i)
                
        for divider in num_dividers:
            if dividers.count(divider) == 1:
                unique += 1
        if unique == len(set(num_dividers)):
            biggest_number = max(number, biggest_number)

results.write(f"60.3\nBiggest coprime integer:\n{biggest_number}") 
results.close()
file.close()

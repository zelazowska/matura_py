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
with open("liczby.txt") as file:
    all_numbers = []
    for lines in file:
        number = int(lines.strip())
        all_numbers.append(number)


results.close()
file.close()

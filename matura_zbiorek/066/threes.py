import math

temp = open("trojki.txt")
file = temp.readlines()
temp.close()

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
  
print("6.1\n")  
for lines in file:
    temp = lines.rstrip()
    lines = lines.rstrip().split(" ")
    a, b, c = lines[0], lines[1], lines[2]
    
    ab_sum = 0
    for numbers in a:
        ab_sum += int(numbers)
    for numbers in b:
        ab_sum += int(numbers)
    if ab_sum == int(c):
        print(temp)

print("\n66.2\n")
for lines in file:
    temp = lines.rstrip()
    lines = lines.rstrip().split(" ")
    a, b, c = int(lines[0]), int(lines[1]), int(lines[2])
    if isPrime(a) and isPrime(b) and a*b == c:
        print(temp)
        
print("\n66.3\n")
values = []
sides = []
for lines in file:
    sides.append(lines.rstrip())
    lines = lines.rstrip().split(" ")
    a, b, c = int(lines[0]), int(lines[1]), int(lines[2])
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        values.append(True)
    else:
        values.append(False)
        
for i in range(1, len(values)):
    if values[i-1] == values[i] == True:
        print(f"{sides[i-1]}\n{sides[i]}")

print("\n66.4\n")        
triangular = []
for lines in file:
    sides.append(lines.rstrip())
    lines = lines.rstrip().split(" ")
    a, b, c = int(lines[0]), int(lines[1]), int(lines[2])
    if a + b > c and a + c > b and c + b > a:
        triangular.append(True)
    else:
        triangular.append(False)

longest_sequence, sequence = 0, 1   
for i in range(1, len(triangular)):
        if triangular[i-1] == triangular[i] == True:
            sequence += 1
            longest_sequence = max(sequence, longest_sequence)
        else:
            sequence = 1
    
print(f"{triangular.count(True)}\n{longest_sequence}")
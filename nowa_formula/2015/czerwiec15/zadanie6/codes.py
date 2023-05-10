temp = open("kody.txt")
file = temp.readlines()
results1 = open("kody1.txt", "w")
results2 = open("kody2.txt", "w")
results3 = open("kody3.txt", "w")
temp.close()

temp2 = open("cyfra_kodkreskowy.txt")
file2 = temp2.readlines()
numbers = []
codes = []
temp2.close()

for lines in file2:
    lines = lines.split()
    numbers.append(lines[0])
    codes.append(lines[1])

dictionary = dict(zip(numbers, codes))

start = "11011010"
stop = "11010110"

#6.1
results1.write("ZADANIE 6.1\n\n")
results2.write("ZADANIE 6.2\n\n")
results3.write("ZADANIE 6.3\n\n")

for lines in file:
    lines = lines.rstrip()
    
    total_sum = sum(int(i) for i in lines)
    odd_sum = sum(int(i) for i in lines[::2])    
    even_sum = total_sum - odd_sum
    
    results1.write(f"{even_sum} {odd_sum}\n")
    
#6.2
    control = str((10-(((3*even_sum)+odd_sum)%10))%10)
    results2.write(f"{control} {dictionary.get(control)}\n")

#6.3
    final = start
    for numbers in lines:
        final += dictionary.get(numbers)
    final += dictionary.get(control) + stop
    results3.write(f"{final}\n")

results1.close()
results2.close()
results3.close()
    
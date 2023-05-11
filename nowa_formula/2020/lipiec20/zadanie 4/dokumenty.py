temp = open("identyfikator.txt")
file = temp.readlines()
results1 = open("wyniki4_1.txt", "w")
results2 = open("wyniki4_2.txt", "w")
results3 = open("wyniki4_3.txt", "w")
temp.close()

results1.write("ZADANIE 4.1\n")
#4.1
max_sum = 0
for lines in file:
    id_sum = sum(int(number) for number in lines.rstrip()[3:])
    max_sum = max(max_sum, id_sum)
    
for lines in file: 
    if sum(int(number) for number in lines.rstrip()[3:]) == max_sum:
        results1.write(f"{lines}")

#4.2
results2.write("ZADANIE 4.2\n")
for lines in file:
    lines = lines.rstrip()
    word, number = lines[:3], lines[3:]
    
    if word == word[::-1] or number == number[::-1]:
        results2.write(f"{lines}\n")
        
#4.3
results3.write("ZADANIE 4.3\n")        
for lines in file:
    lines = lines.rstrip()
    values, weighted = [], []
    control_number = int(lines[3])
    new_str = lines[:3] + lines[4:]
    
    for character in new_str[:3]:
        values.append(int(ord(character) - 55))
    for character in new_str[3:]:
        values.append(int(character))
    
    for value in values[::3]:
        weighted.append(int(value)*7)
        
    for value in values[1::3]:
        weighted.append(int(value)*3)
        
    for value in values[2::3]:
        weighted.append(int(value)*1)
    
    if sum(i for i in weighted)%10 != control_number:
        results3.write(f"{lines}\n")       

results1.close()
results2.close()
results3.close()
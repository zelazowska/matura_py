temp = open("dane.txt")
file = temp.readlines()
temp.close()
results = open("wyniki6.txt", "w")

counter_sorted, counter_dec, counter_oct = 0, 0, 0
biggest, smallest = 0, 100000000009
for lines in file:
    whole_number = []
    final = ""
    #6a
    lines = lines.rstrip()
    if lines[0] == lines[-1]:
        counter_oct += 1 
    #6b
    number = str(int(lines, 8))
    if number[0] == number[-1]:
        counter_dec += 1 
    #6c  
    for characters in lines: 
        whole_number.append(int(characters))
    for number in sorted(whole_number):
        final += str(number)
    if lines == final:
        counter_sorted += 1
        smallest = min(int(lines), smallest)
        biggest = max(int(lines), biggest)
        
results.write(f"ZADANIE 6\n\n6a\n{counter_oct}\n\n6b\n{counter_dec}\n\n")
results.write(f"6c\nLiczb: {counter_sorted}\nNajmniejsza: {smallest}\nNajwieksza: {biggest}")
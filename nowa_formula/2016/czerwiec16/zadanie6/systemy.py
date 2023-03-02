temp = open("liczby.txt", "r")
numbers = temp.readlines()
temp.close()
results1 = open("wyniki6_1.txt", "w")
results2 = open("wyniki6_2.txt", "w")
results3 = open("wyniki6_3.txt", "w")
results4 = open("wyniki6_4.txt", "w")
results5 = open("wyniki6_5.txt", "w")

#6.1
counter = 0
for number in numbers:
    number = number.rstrip()
    if number[-1] == "8":
        counter+=1
        
results1.write(f"Zadanie 6.1\nW osemkowym:{counter}")

#6.2
counter_fours = 0
for number in numbers:
    number = number.rstrip()
    if number[-1] == "4" and "0" not in number[:-1]:
        counter_fours+=1

results2.write(f"Zadanie 6.2\nW czworkowym bez zer:{counter_fours}")

#6.3
counter_even = 0
for number in numbers:
    number = number.rstrip()
    if number[-1] == "2" and int(number[:-1])%2 == 0:
        counter_even+=1  
        
results3.write(f"Zadanie 6.3\nBinarnych parzystych:{counter_even}")

#6.4
counter_oct = 0
for number in numbers:
    number = number.rstrip()
    if number[-1] == "8":
        counter_oct+=(int(number[:-1], 8))
        
results4.write(f"Zadanie 6.4\nSuma osemkowych:{counter_oct}")

#I/O section
file1 = open("ciagi.txt", "r")
file2 = open("bledne.txt", "r")

wynik1 = open("wynik1.txt", "w")
wynik2 = open("wynik2.txt", "w")
wynik3 = open("wynik3.txt", "w")

numbers = []
for lines in file1:
    sequence = lines.strip()
    numbers.append(sequence)
    
sequences = [] #every second line is a sequence, we dont really need the 
               #sequence lenght - its for easier c++ input
for i in range(1, len(numbers), 2):
    sequences.append(numbers[i])
    
#61.1 
arithmetic_sequences = 0
biggest_difference = -1000000000009

for i in sequences:
    i = list(map(int, i.split()))
    #could also use something like int(i) for i in input.split()
    #list(map(int,input().split())): !!!USEFUL
    #INPUT: 1 2 3 4 5 -> OUTPUT: Out[]: [1, 2, 3, 4, 5]
    difference = abs(i[1]-i[0])
    if all(i[j] == i[j-1] + difference for j in range(1, len(i))) :
        arithmetic_sequences += 1
        if difference > biggest_difference:
            biggest_difference = difference
                
wynik1.write(f"61.1\nAmount of arithemtic sequences:\n{arithmetic_sequences}\n"
             "Biggest difference:\n{biggest_difference}\n\n")
        
    
    
    
    
    
    
    
    
    
file1.close()
file2.close()
wynik1.close()
wynik2.close()
wynik3.close()
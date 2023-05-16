#I/O section
file1 = open("ciagi.txt").readlines()
file2 = open("bledne.txt").readlines()

wynik1 = open("wynik1.txt", "w")
wynik2 = open("wynik2.txt", "w")
wynik3 = open("wynik3.txt", "w")

pow_of_3 = [pow(i,3) for i in range(1, 100)]

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
                
wynik1.write(f"61.1\nAmount of arithemtic sequences:\n{arithmetic_sequences}\nBiggest difference:\n{biggest_difference}\n\n")

wynik2.write(f"61.2\nBiggest powers of 3 in sequence:\n")       
for sequence in sequences:
    biggest_pow_of_3 = 0
    sequence = sequence.rstrip()
    for number in sequence.split(" "):
        if int(number) in pow_of_3:
            biggest_pow_of_3 = max(biggest_pow_of_3, int(number))
    if biggest_pow_of_3 > 0:
        wynik2.write(f"{biggest_pow_of_3}\n")

wynik3.write(f"61.3\nImpostors:\n") 
wrong_file = []
wrong_sequences = []
for lines in file2:
    wrong_file.append(lines.rstrip())
    
for i in range(1, len(wrong_file), 2):
    wrong_sequences.append(wrong_file[i])

for sequence in wrong_sequences:
    differences = []
    sequence = list(map(int, sequence.split(" ")))
    for i in range(1, len(sequence)):
        difference = abs(sequence[i] - sequence[i-1])
        differences.append(difference)
    sequence_diff = max(differences, key = differences.count)
    
    for j in range(1, len(differences)):
        if differences[j] != differences[j-1] and differences[j] != sequence_diff:
            index = j+1
            break
    wynik3.write(f"{sequence[j+1]}\n")

wynik1.close()
wynik2.close()
wynik3.close()
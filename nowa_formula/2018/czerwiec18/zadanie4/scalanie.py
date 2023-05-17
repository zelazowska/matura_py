temp1 = open("dane1.txt")
temp2 = open("dane2.txt")
file1 = temp1.readlines()
file2 = temp2.readlines()
results1 = open("wyniki4_1.txt", "w")
results2 = open("wyniki4_2.txt", "w")
results3 = open("wyniki4_3.txt", "w")
results4 = open("wyniki4_4.txt", "w")
temp1.close()
temp2.close()

#4.1, 4.2, 4.3
sequences = zip(file1, file2)

results4.write(f"4.4\n")
same_ending = 0
even_uneven = 0
same_number = 0
same_number_index = []
i = 0
for sequence in sequences:
    sequence1 = []
    sequence2 = []
    sorted = []
    even1 = even2 = uneven1 = uneven2 = 0
    a, b = sequence[0], sequence[1]
    i = i+1
    for number in a.rstrip().split(" "):
        sequence1.append(int(number))
        if int(number)%2 == 0:
            even1 += 1

    for number in b.rstrip().split(" "):
        sequence2.append(int(number))
        if int(number)%2 == 0:
            even2 += 1

    if sequence1[-1] == sequence2[-1]:
        same_ending += 1

    if even1 == even2 == 5:
        even_uneven += 1

    if set(sequence1) == set(sequence2):
        same_number += 1
        same_number_index.append(i)

    #xddddddddddddddddddddddddddddd
    sequence1.sort()
    sequence2.sort()
    final = []

    while len(sequence1) != 0 and len(sequence2) != 0:
        if sequence1[0] <= sequence2[0]:
            final.append(sequence1[0])
            sequence1 = sequence1[1:]
        else:
            final.append(sequence2[0])
            sequence2 = sequence2[1:]

    for number in final:
        results4.write(f"{number} ")
    results4.write("\n")

results1.write(f"4.1\nCiagow, ktorych ostatnia liczba jest taka sama: {same_ending}")
results2.write(f"4.2\nPar ciagow, w ktorych jest 5 liczb parzystych i 5 nieparzystych: {even_uneven}")
results3.write(f"4.2\nPar ciagow utworzonych z tych samych liczb: {same_number}\nWiersze:\n{same_number_index}")


results1.close()
results2.close()
results3.close()
results4.close()
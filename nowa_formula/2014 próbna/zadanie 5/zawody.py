temp = open("dziennik.txt")
file = temp.readlines()
results = open("wynik5.txt", "w")
temp.close()

jumps = []
for lines in file:
    jumps.append(int(lines.rstrip()))
    
streak = 1
max_streak = 0
counter = 0
sequence = [jumps[0]]
max_sequence = []

for i in range(1, len(jumps)):
    if jumps[i-1] < jumps[i]:
        streak += 1
        sequence.append(jumps[i])
        #5.3
        max_streak = max(max_streak, streak)
        if streak > len(max_sequence):
            max_sequence = sequence
    else:
        streak = 1
        sequence = [jumps[i]]
    #5.1
    if streak == 4: 
        counter += 1

#5.1
results.write(f"5.1\nPozytywnych serii treningowych dluzszych niz 3 dni: {counter}\n\n")
#5.2
results.write(f"5.2\nNajdluzszy: {max(jumps)}, dzien {jumps.index(max(jumps))+1}\n"),
results.write(f"Najkrotszy: {min(jumps)}, dzien {jumps.index(min(jumps))+1}\n\n")
#5.3
results.write(f"5.3\nDlugosc serii: {len(max_sequence)}\n")
results.write(f"Poprawa wyniku o {max(max_sequence)-min(max_sequence)} cm")

results.close()
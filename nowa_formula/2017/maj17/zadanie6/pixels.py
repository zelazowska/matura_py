temporary = open("przyklad.txt")
file = temporary.readlines()
temporary.close()
results = open("wyniki6.txt", "w")

#6.1
brightest = -1000009
darkest = 100009
for lines in file:
    line = list(map(int, lines.rstrip().split()))
    brightest = max(max(line), brightest)
    darkest = min(min(line), darkest)
        
results.write(f"ZADANIE 6\n\nZadanie 6.1\nNajjasniejszy: {brightest}\nNajciemniejszy: {darkest}\n\n")

#6.2
counter = 0 
for lines in file:
    line = list(map(int, lines.rstrip().split()))
    left = line[:160]
    right = line[160:]
    if left != list(reversed(right)):
        counter += 1

results.write(f"Zadanie 6.2\nMinimalna liczba do usuniecia, by otrzymac linie symetrii: {counter}\n\n")    

        
file = open("dane_anagramy.txt", "r")
results = open("wyniki_anagramy.txt", "w")

def zadanie4a():
    anagramy = 0
    for lines in file:
        a, b = sorted(lines.split()[0]), sorted(lines.split()[1])
        if a == b:
            anagramy+=1
    results.write(f"ZAD 4 a)\nLiczba wierszy z anagramami:\n{anagramy}\n\n")
    
zadanie4a()
file.close()
results.close()

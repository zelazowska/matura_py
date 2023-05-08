temp = open("przyklad.txt").readlines()
file = open("napisy.txt").readlines()
results = open("wyniki4.txt", "w")

results.write(f"ZADANIE 4\n\n")

#4.1
numbers = 0
for lines in file:
    for character in lines:
        if character.isdecimal() == True:
            numbers+=1

results.write(f"4.1\n{numbers}\n\n")

#4.2
word = ''
i=0
for lines in file[19::20]:
    lines = lines.rstrip()
    word += lines[i]
    i+=1
    
results.write(f"4.2\n{word}\n\n")

#4.3
from_palindromes = ''
for lines in file:
    lines = lines.rstrip()
    word1 = lines[1:]
    word2 = lines[:-1]
    if word1 == word1[::-1]:
        from_palindromes += lines[25]
    elif word2 == word2[::-1]:
        from_palindromes += lines[24]
 
results.write(f"4.3\n{from_palindromes}\n\n")

#4.4
for lines in temp:
    counter = 0
    for character in lines:
        
            
    
            
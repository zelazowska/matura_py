from collections import Counter

temp = open("dane.txt")
file = temp.readlines()
temp.close()
results = open("wyniki.txt", "w")

words = []
non_unique, even, palindromes = 0, 0, 0

for lines in file:
    lines = lines.rstrip()
    words.append(lines)
    if int(lines, 16)%2 == 0: #6b
        even += 1
    if lines == lines[::-1]:
        palindromes += 1 #6c

for values in Counter(words).values(): #6a
    if values > 1: 
        non_unique += 1
#6a looking cringe but I have a thing for oneliners
results.write(f"6a\n{non_unique}\n{max(Counter(words))} {sorted((Counter(words)).values(), reverse = True)[0]}\n\n")
results.write(f"6b\n{even}\n\n6c\n{palindromes}")
    
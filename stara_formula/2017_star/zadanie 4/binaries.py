temp = open("binarne.txt")
file = temp.readlines()
temp.close()
results = open("zadanie4.txt", "w")

cyclic_words = []
biggest = []
incorrect = []
for lines in file:
    lines = lines.rstrip()
    word = lines
    if lines[:len(lines)//2] == lines[len(lines)//2:]: #4.1
        cyclic_words.append(lines)
    #4.2
    while word != '':
        segment = word[:4]
        if int(segment, 2) > 9:
            incorrect.append(word)
            break 
        word = word[4:]      
    #4.3   
    if int(lines, 2) <= 65535:
          biggest.append(int(lines,2))
#4.2          
shortest_incorrect = len(sorted(incorrect, key = len)[0]) 
          
max_len_word = sorted(cyclic_words, key = len, reverse = True)[0]
max_len = len(max_len_word)
    
results.write(f"4.1\n{len(cyclic_words)}\n{max_len_word} {max_len}\n\n")
results.write(f"4.2\n{len(incorrect)} {shortest_incorrect}\n\n")
results.write(f"4.3\n{max(biggest)} {bin(max(biggest))[2:]}")

results.close()
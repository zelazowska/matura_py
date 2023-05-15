temp = open("slowa.txt")
file = temp.readlines()
temp.close()
results = open("wynik4.txt", "w")

counter = 0
longest_zeros_sequence = 0
blocks_counter = 0
for lines in file:
    zeros, ones, zeros_sequence, word = 0, 0, 1, [] 
    for character in lines.rstrip():
        word.append(character)
        if character == '0':
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        counter += 1
    #4.3    
    for i in range(1, len(word)):
        if word[i-1] == word[i] == '0':
            zeros_sequence += 1
            longest_zeros_sequence = max(zeros_sequence, longest_zeros_sequence)
        else:
            zeros_sequence = 1
    #4.2        
    blocks = 1
    for i in range(1, len(word)):
        if word[i-1] != word[i]:
            blocks += 1
                     
    if blocks == 2 and lines[0] == '0':
        blocks_counter += 1
 
results.write(f"ZADANIE 4\n\n4.1\n{counter}\n\n")
results.write(f"4.2\n{blocks_counter}\n\n")
results.write(f"4.3\nDlugosc najdluzszego ciagu: {longest_zeros_sequence}\n") 
        
for lines in file:
    word = []
    
    for character in lines.rstrip():
        word.append(character)
    for i in range(1, len(word)):
        if word[i-1] == word[i] == '0':
            zeros_sequence += 1
            if zeros_sequence == longest_zeros_sequence:
                results.write(lines)
        else:
            zeros_sequence = 1   

results.close()
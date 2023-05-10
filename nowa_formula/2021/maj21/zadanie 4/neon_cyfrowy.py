from collections import Counter

temp = open("instrukcje.txt")
file = temp.readlines()
temp.close()
results = open("wyniki4.txt", "w")

results.write("ZADANIE 4\n\n")

word = []
letter = []
instructions = []
for lines in file:
    lines = lines.rstrip().split()
    instruction, element = lines[0], lines[1]
    instructions.append(instruction)
    
    #4.1, 4.4
    if instruction == "DOPISZ":
        word.append(element)
    elif instruction == "ZMIEN":
        word[-1] = element
    elif instruction == "USUN":
        word = word[:-1]
    else:
        order = ord(element)
        for i in range(len(word)):
            if word[i] == element:
                if word[i] != 'Z':
                    word[i] = chr(order+1)
                else:
                    word[i] = 'A'
                break
                              
    if instruction == "DOPISZ":
        letter.append(element)
        
#4.1
results.write(f"4.1\n{len(word)}\n\n")

#4.2
occurences = Counter(letter)
maxvalue = max(occurences.values()) 

for letter, occurence in occurences.items():
    if occurence == maxvalue:
        results.write(f"4.2\n{letter} {maxvalue}\n\n")

#4.3
longest_sequence_instruction = ""
sequence = 1
longest_sequence = 1
for i in range(1, len(instructions)):
    if instructions[i] == instructions[i-1]:
        sequence += 1
        longest_sequence = max(sequence, longest_sequence)
        longest_sequence_instruction = instructions[i]
    else:
        sequence = 1

results.write(f"4.3\n{longest_sequence_instruction} {longest_sequence}\n\n")

#4.4
word = "".join(character for character in word)
results.write(f"4.4\n{word}")

results.close()
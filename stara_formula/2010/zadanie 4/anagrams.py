from collections import Counter

temp = open("anagram.txt")
file = temp.readlines()
temp.close()
results4_a = open("odp_4a.txt", "w")
results4_b = open("odp_4b.txt", "w")

results4_a.write(f"ZADANIE 4a)\n")
for lines in file:
    words, lengths = [], []
    
    all_words = lines.rstrip().split()
    for word in all_words:
        lengths.append(len(word))
        
    if len(set(lengths)) == 1:
        results4_a.write(f"{lines}")

results4_b.write(f"ZADANIE 4b)\n")
for lines in file:
    sorted_words = []
    flag = 0
    
    all_words = lines.rstrip().split()
    for word in all_words:
        sorted_words.append(sorted(word))
        
    for i in range(1, len(sorted_words)):
        if sorted_words[i-1] != sorted_words[i]:
            flag = 1
    if flag != 1:
        results4_b.write(f"{lines}")
    
results4_a.close()
results4_b.close()
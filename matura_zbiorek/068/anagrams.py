from collections import Counter

temp = open("dane_napisy.txt")
file = temp.readlines()
temp.close()

homogeneous_count, anagrams_count, most_occurences = 0, 0, 0
anagrams_list = []

for lines in file:
    lines = lines.rstrip().split(" ")
    a, b = lines[0], lines[1] 
    if len(a) == len(b): #68.1
        if set(a) == set(b) and len(set(a)) == len(set(b)) == 1:
            homogeneous_count += 1 
    #68.2, 68.3
    if sorted(list(a)) == sorted(list(b)):
        anagrams_count += 1 
    anagrams_list.append(''.join(sorted(list(a))))
    anagrams_list.append(''.join(sorted(list(b))))
    
most_occurences = max(Counter(anagrams_list).values())

        
print(f"68.1. {homogeneous_count}\n68.2. {anagrams_count}\n68.3. {most_occurences}")
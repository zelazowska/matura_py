file = open("napisy.txt").readlines()
results = open("wynik_napisy.txt", "w")

counter = 0
pairs = []

for lines in file:
    word1, word2 = lines.split(" ")[0], lines.split(" ")[1].rstrip()
    if len(word1) >= 3*len(word2) or len(word2) >= 3*len(word1):
        counter += 1
        pairs.append(lines)
results.write(f"72.1\nPierwsza para: {pairs[0]}Par: {counter}\n\n")

results.write("72.2\n")
for lines in file:
    word1, word2 = lines.split(" ")[0], lines.split(" ")[1].rstrip()
    if word1 in word2 and word1[0] == word2[0]:
        rest = ""
        results.write(f"{lines}")
        for i in range(len(word1), len(word2)):
            rest += word2[i]
        results.write(f"{rest}\n\n")

for lines in file:
 
    word1, word2 = lines.split(" ")[0], lines.split(" ")[1].rstrip()
    reverse_word1 = word1[::-1]
    reverse_word2 = word2[::-1]
    ending_len = 0
    
    for i in range(len(reverse_word2)):
        print(reverse_word1[i], reverse_word2[i])
        # if reverse_word1[i] == reverse_word2[i]:
        #     print(reverse_word1[i])
        


            
    
    

file1 = open("dane_6_1.txt").readlines()
file2 = open("dane_6_2.txt").readlines()
file3 = open("dane_6_3.txt").readlines()
results1 = open("wyniki_6_1.txt", "w")
results2 = open("wyniki_6_2.txt", "w")
results3 = open("wyniki_6_3.txt", "w")


results1.write("ZADANIE 6.1\n\n")
for lines in file1:
    cipher = ''
    k = 107
    word = lines.rstrip()
    for letter in word:
        if k+ord(letter) > 95:
            new_order = ((k+ord(letter)-65)%26)+65
            cipher += chr(new_order)
    results1.write(f"{cipher}\n")
    
results2.write("ZADANIE 6.2\n\n")
for lines in file2:
    lines = lines.rstrip()
    ciphered = ''
    
    try:
        word, key = lines.split(" ")[0], lines.split(" ")[1], 
    except IndexError:
        key = 0

    for letter in word:
        new_ord = ((ord(letter)-int(key)-65)%26)+65
        ciphered += chr(new_ord)
    results2.write(f"{ciphered}\n")


results3.write("ZADANIE 6.3\n\n")
for lines in file3:
    words = lines.rstrip().split()
    word, encoded = words[0], words[1]
    
    new_key = (ord(word[0])-ord(encoded[0]))%26
    flag = True
    
    for i in range(len(word)):
        if (ord(word[i])-ord(encoded[i]))%26 != new_key:
            flag = False
            break
    
    if not flag:
        results3.write(f"{word}\n")


    
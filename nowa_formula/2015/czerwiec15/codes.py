# I/O
file = open("kody.txt", "r")
kody1 = write("kody1.txt", "w")
kody2 = write("kody2.txt", "w")
kody3 = write("kody3.txt", "w")

#main
for lines in file:
    line = lines.strip()
    print(line)
    
    
file.close()
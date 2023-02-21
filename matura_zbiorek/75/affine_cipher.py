import string

# I/O 
tekst = open("tekst.txt", "r")
probka = open("probka.txt", "r")

#ascii for 'a' = 97
#ascii for 'z' = 122

lines = tekst.readlines()
x = ascii(lines)
print(x)
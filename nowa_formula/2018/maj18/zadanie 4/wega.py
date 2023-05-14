temp = open("sygnaly.txt")
file = temp.read().split()
temp.close()

results = open("wyniki4.txt", "w")

#4.1
decoded = ''
for i in range(39, len(file), 40):
    decoded += file[i][9]
    
results.write(f"4.1\n{decoded}\n\n")
  
#4.2
unique = 0
for lines in file:
    if len(set(lines)) > unique:
        unique = len(set(lines))

for lines in file:
    if len(set(lines)) == unique:
        results.write(f"4.2\n{lines} {unique}\n\n")
        break
 
#4.3 
results.write("4.3\n")   
for lines in file:
    flag = 0
    code = ""
    #for i in range(1, len(lines)):
    if(ord(sorted(lines)[-1]))-ord(sorted(lines)[0]) > 10:
        flag = 1
    if flag == 0:
        results.write(f"{lines}\n")
   
results.close()
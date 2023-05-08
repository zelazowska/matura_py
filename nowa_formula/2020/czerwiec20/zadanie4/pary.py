temporary = open("pary.txt")
file = temporary.readlines()
temporary.close()
temp = open("przyklad.txt")
example = temp.readlines()
temp.close()

for lines in example:
    lines = lines.strip()
    number, word = lines.split(" ")
    number = int(number)
    temp_num = number
    if number%2 == 0:
        divider = 2
        dividers = []
        while number > 2:
            if number%divider == 0:
                dividers.append(divider)
                number = number//divider
            else:
                divider+=1
        print(temp_num, dividers)
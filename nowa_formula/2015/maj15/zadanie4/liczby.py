file = open("liczby.txt")
results = open("wynik4.txt", "w")

def zadanie41():
    with open("liczby.txt") as file:
        more_zeros = 0
        for lines in file:
            zeros = ones = 0
            for numbers in lines.rstrip():
                if numbers == '0':
                    zeros+=1
                else:
                    ones+=1
            if zeros > ones:
                more_zeros+=1  
    results.write(f"Zadanie 4.1\nWiecej zer niz jednek:\n{more_zeros}\n\n")
    file.close()

def zadanie42():
    with open("liczby.txt") as file:
        divisible_by_2 = 0
        divisible_by_8 = 0
        for lines in file:
            if(int(lines, 2)%2 == 0):
                    divisible_by_2+=1
            if(int(lines, 2)%8 == 0):
                divisible_by_8+=1
    results.write(f"Zadanie 4.2\nPodzielne przez 2:\n{divisible_by_2}\nPodzielne przez 8: \n{divisible_by_8}\n\n")
    file.close()
    
def zadanie43():
    numbers = []
    with open("liczby.txt") as file:
        for lines in file:
            numbers.append(int(lines,2))
    results.write(f"Zadanie 4.3\nNajmniejsza: {numbers.index(max(numbers)) + 1}\nNajwieksza: {numbers.index(min(numbers)) + 1}")
        
    
zadanie41()
zadanie42()
zadanie43()
results.close()
            

# I/O
liczby1 = open("liczby1.txt", "r")
liczby2 = open("liczby2.txt", "r")
wyniki = open("wyniki.txt", "w")

# 
# main
def zadanie61():
    biggest_number = -100009
    smallest_number = 100009
    for lines in liczby1:
        numbers = lines.strip()
        decimal_number = int(numbers, 8)
        biggest_number = max(biggest_number, decimal_number)
        smallest_number = min(smallest_number, decimal_number)   
    biggest_number = oct(biggest_number).replace("0o", "")
    smallest_number = oct(smallest_number).replace("0o", "")
    
    wyniki.write(f"62.1\nBiggest number (octal):{biggest_number}\n"
                 f"smallest number (octal):{smallest_number}\n\n")

def zadanie62():
    pass
    """
    all_numbers = []
    for lines in liczby2:
        numbers = int(lines.strip())
        all_numbers.append(numbers)
        
    longest_sequence = 0 
    current_sequence_len = 0 
    nondecreasing = []
    prev = 10000000000
    for i in range(1, len(all_numbers)):
        if(all_numbers[i] >= all_numbers{i-1}):
            if(current_sequence_len > longest_sequence):
                longest_sequence = max(current_sequence_len, longest_sequence)
                first_in_longest = first 
    """
            
def zadanie63():
    same_numbers = 0
    bigger_octals = 0 
    with open("liczby1.txt", "r") as file1:
        with open("liczby2.txt", "r") as file2:
            for octal, decimal in zip(file1, file2):
                octal = int(octal.strip(), 8)
                decimal = int(decimal.strip())
                if octal == decimal:
                    same_numbers += 1
                elif octal > decimal:
                    bigger_octals += 1
                    
    wyniki.write(f"62.3\nAmount of equal numbers: {same_numbers}\n" 
           f"Octal numbers bigger than decimal: {bigger_octals}\n\n")
                    
            
def zadanie64():
    six_occuring = 0
    six_in_octal = 0
    for lines in liczby2:
        number = lines.strip()
        six_occuring += int(number.count("6"))
        octal_number = str(oct(int(number)))
        six_in_octal += int(octal_number.count("6"))
        
    wyniki.write(f"62.4\nAmount of numbers with 6: {six_occuring}\n"
                 f"Amount of numbers with 6 in octal representation: "
                 f"{six_in_octal}\n\n")
            




zadanie61()
zadanie62()
zadanie63()
zadanie64()